import logging
import os
import sys
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

# Bootstrapping sys.path for both root and backend directory execution
_current_dir = os.path.dirname(os.path.abspath(__file__))  # .../backend/app
_backend_dir = os.path.dirname(_current_dir)               # .../backend
_repo_root = os.path.dirname(_backend_dir)                 # .../skillexa-app
for p in [_repo_root, _backend_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

from backend.app.config import settings
from backend.app.database import Base, engine
from backend.app.dependencies.db import get_db
from backend.app.middleware.error_handler import register_error_handlers
from backend.app.middleware.security import register_security_middleware
from backend.app.models.college import College
from backend.app.models.note import FacultyNote
from backend.app.models.quiz import Quiz
from backend.app.models.user import User
from backend.app.routers import (
    assignments_router,
    auth_router,
    coding_router,
    community_router,
    faculty_router,
    interviews_router,
    notes_router,
    notifications_router,
    pdf_notes_router,
    progress_router,
    questions_router,
    quizzes_router,
    student_router,
    topics_router,
    videos_router,
)

from backend.app.seed import seed_database

logging.basicConfig(level=logging.INFO if not settings.DEBUG else logging.DEBUG)
logger = logging.getLogger("skillexa.main")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing SkillExa database tables...")
    Base.metadata.create_all(bind=engine)
    seed_database()
    logger.info("SkillExa FastAPI Backend started successfully.")
    yield
    logger.info("SkillExa FastAPI Backend shutting down.")


app = FastAPI(
    title=settings.APP_NAME,
    description="Comprehensive Python FastAPI Backend for SkillExa — Student Learning, College Connection, Faculty Portal, Coding/DSA & Community Engine.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# 1. Register Security & CORS Middleware
register_security_middleware(app)

# 2. Register Centralized Error Handling
register_error_handlers(app)

# 3. Mount API Routers under /api
app.include_router(auth_router, prefix=settings.API_V1_STR)
app.include_router(student_router, prefix=settings.API_V1_STR)
app.include_router(faculty_router, prefix=settings.API_V1_STR)
app.include_router(community_router, prefix=settings.API_V1_STR)
app.include_router(notes_router, prefix=settings.API_V1_STR)
app.include_router(pdf_notes_router, prefix=settings.API_V1_STR)
app.include_router(videos_router, prefix=settings.API_V1_STR)
app.include_router(quizzes_router, prefix=settings.API_V1_STR)
app.include_router(questions_router, prefix=settings.API_V1_STR)
app.include_router(assignments_router, prefix=settings.API_V1_STR)
app.include_router(coding_router, prefix=settings.API_V1_STR)
app.include_router(interviews_router, prefix=settings.API_V1_STR)
app.include_router(notifications_router, prefix=settings.API_V1_STR)
app.include_router(progress_router, prefix=settings.API_V1_STR)
app.include_router(topics_router, prefix=settings.API_V1_STR)


@app.get("/", tags=["Health"])
def root():
    return {
        "app": settings.APP_NAME,
        "status": "ok",
        "message": "SkillExa backend is running",
        "docs": "/docs",
    }


@app.get("/health", tags=["Health"])
@app.get("/api/health", tags=["Health"])
def health_check():
    """Requirement 6: Health Endpoint"""
    return {
        "status": "ok",
        "message": "SkillExa backend is running",
    }


@app.get("/api/health/fullstack", tags=["Health"])
def fullstack_health_check(db: Session = Depends(get_db)):
    """Requirement 9 & 10: Real Full-Stack Database & API Verification"""
    try:
        colleges_count = db.query(College).count()
        users_count = db.query(User).count()
        notes_count = db.query(FacultyNote).count()
        quizzes_count = db.query(Quiz).count()

        return {
            "status": "ok",
            "backend": "SkillExa FastAPI is online",
            "database": {
                "status": "connected",
                "engine": "SQLite / PostgreSQL",
                "records": {
                    "colleges": colleges_count,
                    "users": users_count,
                    "notes": notes_count,
                    "quizzes": quizzes_count,
                },
            },
            "environment": settings.ENVIRONMENT,
        }
    except Exception as e:
        return {
            "status": "error",
            "backend": "online",
            "database": {
                "status": "disconnected",
                "error": str(e),
            },
        }
