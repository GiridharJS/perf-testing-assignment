# perf_api/cache.py
import redis, json
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB   = int(os.getenv("REDIS_DB", 0))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

def get_cache(key):
    data = r.get(key)
    return json.loads(data) if data else None

def set_cache(key, value, ttl=300):
    r.setex(key, ttl, json.dumps(value))

def invalidate_user_cache(user_id):
    pattern = f"user:{user_id}:report:*"
    
    for k in r.scan_iter(match=pattern):
        r.delete(k)

