from typing import Generator
from sqlalchemy.orm import Session
from backend.app.database import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """FastAPI Dependency for database sessions."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
