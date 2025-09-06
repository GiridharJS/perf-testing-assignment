from sqlalchemy.orm import Session
from sqlalchemy import text
from . import models, cache

def get_user_activity(db: Session, user_id: int, start, end):
    """
    Optimized query with caching.
    """
    cache_key = f"user:{user_id}:report:{start}:{end}"
    cached = cache.get_cache(cache_key)
    if cached:
        return cached

    sql = text("""
        SELECT u.name,
               COUNT(t.id) AS total_tasks,
               COALESCE(SUM(CASE WHEN t.status='DONE' THEN 1 ELSE 0 END), 0) AS completed
        FROM users u
        LEFT JOIN tasks t
          ON u.id = t.user_id AND t.created_at BETWEEN :start AND :end
        WHERE u.id = :uid
        GROUP BY u.name
    """)
    row = db.execute(sql, {"uid": user_id, "start": start, "end": end}).fetchone()

    result = {"user": "Unknown", "total_tasks": 0, "completed": 0}
    if row:
        result = {"user": row[0], "total_tasks": int(row[1]), "completed": int(row[2])}

    # Cache for 5 minutes
    cache.set_cache(cache_key, result, ttl=300)
    return result
