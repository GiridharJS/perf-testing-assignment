# perf_api/routers/reports

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/reports/user-activity")
def user_activity(user_id: int, start: str, end: str, db: Session = Depends(get_db)):
    return crud.get_user_activity(db, user_id, start, end)
