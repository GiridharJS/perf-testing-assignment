# perf_api/main.py

from fastapi import FastAPI
from .routers import reports
from .database import Base, engine

# Create tables if not already present
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Performance API")

# Add router
app.include_router(reports.router)
