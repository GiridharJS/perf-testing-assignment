# perf_api/seed_data.py

from sqlalchemy.orm import Session
from perf_api.database import SessionLocal, Base, engine
from perf_api import models  # <-- your SQLAlchemy models (adjust import if needed)

def seed():
    # create all tables if not already created
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()

    try:
        # Example: If you have a Task model
        if not db.query(models.Task).first():
            tasks = [
                models.Task(title="Write docs", description="Document the API"),
                models.Task(title="Add Redis", description="Setup caching"),
                models.Task(title="Run Locust", description="Performance testing"),
            ]
            db.add_all(tasks)
            db.commit()
            print("✅ Seed data inserted into database")
        else:
            print("⚠️ Data already exists, skipping seed.")
    finally:
        db.close()

if __name__ == "__main__":
    seed()
