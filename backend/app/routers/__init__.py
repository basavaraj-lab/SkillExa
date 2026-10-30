from backend.app.routers.auth import router as auth_router
from backend.app.routers.student import router as student_router
from backend.app.routers.faculty import router as faculty_router
from backend.app.routers.community import router as community_router
from backend.app.routers.notes import router as notes_router
from backend.app.routers.pdf_notes import router as pdf_notes_router
from backend.app.routers.videos import router as videos_router
from backend.app.routers.quizzes import router as quizzes_router
from backend.app.routers.questions import router as questions_router
from backend.app.routers.assignments import router as assignments_router
from backend.app.routers.coding import router as coding_router
from backend.app.routers.interviews import router as interviews_router
from backend.app.routers.notifications import router as notifications_router
from backend.app.routers.progress import router as progress_router
from backend.app.routers.topics import router as topics_router
from backend.app.routers.ai_interview import router as ai_interview_router
from backend.app.routers.live_interview import router as live_interview_router
from backend.app.routers.aptitude_test import router as aptitude_test_router
from backend.app.routers.govt_jobs import router as govt_jobs_router
from backend.app.routers.project_chat import router as project_chat_router

__all__ = [
    "auth_router",
    "student_router",
    "faculty_router",
    "community_router",
    "notes_router",
    "pdf_notes_router",
    "videos_router",
    "quizzes_router",
    "questions_router",
    "assignments_router",
    "coding_router",
    "interviews_router",
    "notifications_router",
    "progress_router",
    "topics_router",
    "ai_interview_router",
    "live_interview_router",
    "aptitude_test_router",
    "govt_jobs_router",
    "project_chat_router",
]
