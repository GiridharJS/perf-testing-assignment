# create_index.py
# perf_api/create_index.py

from sqlalchemy import create_engine, text
from perf_api.database import DATABASE_URL

# If your database URL lives in perf_api.database, import it or paste it here:
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    conn.execute(text("CREATE INDEX IF NOT EXISTS idx_task_user_date ON tasks (user_id, created_at);"))
    conn.commit()
    print("Index created (or already existed).")
