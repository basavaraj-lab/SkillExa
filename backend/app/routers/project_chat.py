import logging
from typing import Any, Dict, List, Optional
from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from sqlalchemy.orm import Session

from backend.app.dependencies.auth import get_optional_student
from backend.app.dependencies.db import get_db
from backend.app.models.user import StudentProfile
from backend.app.schemas.project_chat import (
    AIChatRequest,
    AIChatResponse,
    AIConversationCreate,
    AIConversationDetailResponse,
    AIConversationListItem,
    AIConversationUpdate,
    AIProjectCreate,
    AIProjectResponse,
    AIProjectUpdate,
    ProjectMemoryResponse,
)
from backend.app.services.project_chat_service import (
    VARIED_ACKNOWLEDGEMENTS,
    ProjectChatService,
)
from backend.app.services.gemini_service import GeminiService

logger = logging.getLogger("skillexa.project_chat_router")

router = APIRouter(prefix="/ai", tags=["SkillExa AI Voice & Project Chat"])


def resolve_student_id(
    student_profile: Optional[StudentProfile] = None,
    x_student_id: Optional[str] = None,
    email: Optional[str] = None,
) -> str:
    if student_profile and student_profile.user_id:
        return student_profile.user_id
    if x_student_id and x_student_id.strip():
        return x_student_id.strip()
    if email and email.strip():
        return email.strip()
    return "ganesh@kvgce.edu.in"


# -------------------------------------------------------------
# 1. PROJECTS ENDPOINTS
# -------------------------------------------------------------
@router.get("/projects", response_model=List[AIProjectResponse])
def get_projects(
    student_profile: Optional[StudentProfile] = Depends(get_optional_student),
    x_student_id: Optional[str] = Header(None, alias="X-Student-Id"),
    email: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    student_id = resolve_student_id(student_profile, x_student_id, email)
    return ProjectChatService.list_projects(db, student_id)


@router.post("/projects", response_model=AIProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    data: AIProjectCreate,
    student_profile: Optional[StudentProfile] = Depends(get_optional_student),
    x_student_id: Optional[str] = Header(None, alias="X-Student-Id"),
    email: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    student_id = resolve_student_id(student_profile, x_student_id, email)
    project = ProjectChatService.create_project(db, student_id, data)
    return {
        "id": project.id,
        "student_id": project.student_id,
        "name": project.name,
        "description": project.description,
        "icon": project.icon,
        "context_prompt": project.context_prompt,
        "is_pinned": project.is_pinned,
        "conversation_count": 0,
        "created_at": project.created_at,
        "updated_at": project.updated_at,
    }


@router.put("/projects/{project_id}", response_model=AIProjectResponse)
def update_project(
    project_id: str,
    data: AIProjectUpdate,
    student_profile: Optional[StudentProfile] = Depends(get_optional_student),
    x_student_id: Optional[str] = Header(None, alias="X-Student-Id"),
    email: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    student_id = resolve_student_id(student_profile, x_student_id, email)
    updated = ProjectChatService.update_project(db, project_id, student_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found or unauthorized.")
    return {
        "id": updated.id,
        "student_id": updated.student_id,
        "name": updated.name,
        "description": updated.description,
        "icon": updated.icon,
        "context_prompt": updated.context_prompt,
        "is_pinned": updated.is_pinned,
        "conversation_count": len(updated.conversations or []),
        "created_at": updated.created_at,
        "updated_at": updated.updated_at,
    }


@router.delete("/projects/{project_id}")
def delete_project(
    project_id: str,
    student_profile: Optional[StudentProfile] = Depends(get_optional_student),
    x_student_id: Optional[str] = Header(None, alias="X-Student-Id"),
    email: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    student_id = resolve_student_id(student_profile, x_student_id, email)
    success = ProjectChatService.delete_project(db, project_id, student_id)
    if not success:
        raise HTTPException(
            status_code=400,
            detail="Cannot delete default 'General Chats' project or project not found.",
        )
    return {"success": True, "message": "Project and its conversations deleted."}


@router.get("/projects/{project_id}/memory", response_model=ProjectMemoryResponse)
def get_project_memory(
    project_id: str,
    student_profile: Optional[StudentProfile] = Depends(get_optional_student),
    x_student_id: Optional[str] = Header(None, alias="X-Student-Id"),
    email: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    student_id = resolve_student_id(student_profile, x_student_id, email)
    memory = ProjectChatService.get_project_memory(db, project_id, student_id)
    if not memory:
        raise HTTPException(status_code=404, detail="Project memory not found.")
    return memory


# -------------------------------------------------------------
# 2. CONVERSATION ENDPOINTS
# -------------------------------------------------------------
@router.get("/conversations", response_model=List[AIConversationListItem])
def list_conversations(
    project_id: Optional[str] = Query(None),
    student_profile: Optional[StudentProfile] = Depends(get_optional_student),
    x_student_id: Optional[str] = Header(None, alias="X-Student-Id"),
    email: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    student_id = resolve_student_id(student_profile, x_student_id, email)
    return ProjectChatService.list_conversations(db, student_id, project_id)


@router.post("/conversations", status_code=status.HTTP_201_CREATED)
def create_conversation(
    data: AIConversationCreate,
    student_profile: Optional[StudentProfile] = Depends(get_optional_student),
    x_student_id: Optional[str] = Header(None, alias="X-Student-Id"),
    email: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    student_id = resolve_student_id(student_profile, x_student_id, email)
    conv = ProjectChatService.create_conversation(db, student_id, data)
    return {
        "id": conv.id,
        "project_id": conv.project_id,
        "project_name": conv.project.name if conv.project else "General Chats",
        "student_id": conv.student_id,
        "title": conv.title,
        "created_at": conv.created_at,
        "updated_at": conv.updated_at,
    }


@router.get("/conversations/{conversation_id}", response_model=AIConversationDetailResponse)
def get_conversation_detail(
    conversation_id: str,
    student_profile: Optional[StudentProfile] = Depends(get_optional_student),
    x_student_id: Optional[str] = Header(None, alias="X-Student-Id"),
    email: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    student_id = resolve_student_id(student_profile, x_student_id, email)
    detail = ProjectChatService.get_conversation_detail(db, conversation_id, student_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Conversation not found.")
    return detail


@router.put("/conversations/{conversation_id}")
def update_conversation(
    conversation_id: str,
    data: AIConversationUpdate,
    student_profile: Optional[StudentProfile] = Depends(get_optional_student),
    x_student_id: Optional[str] = Header(None, alias="X-Student-Id"),
    email: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    student_id = resolve_student_id(student_profile, x_student_id, email)
    conv = ProjectChatService.update_conversation(db, conversation_id, student_id, data)
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found.")
    return {
        "id": conv.id,
        "project_id": conv.project_id,
        "title": conv.title,
        "updated_at": conv.updated_at,
    }


@router.delete("/conversations/{conversation_id}")
def delete_conversation(
    conversation_id: str,
    student_profile: Optional[StudentProfile] = Depends(get_optional_student),
    x_student_id: Optional[str] = Header(None, alias="X-Student-Id"),
    email: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    student_id = resolve_student_id(student_profile, x_student_id, email)
    success = ProjectChatService.delete_conversation(db, conversation_id, student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Conversation not found.")
    return {"success": True, "message": "Conversation deleted."}


# -------------------------------------------------------------
# 3. UNIVERSAL VOICE & TEXT CHAT
# -------------------------------------------------------------
@router.post("/chat", response_model=AIChatResponse)
async def ai_chat(
    request: AIChatRequest,
    student_profile: Optional[StudentProfile] = Depends(get_optional_student),
    x_student_id: Optional[str] = Header(None, alias="X-Student-Id"),
    email: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    student_id = resolve_student_id(student_profile, x_student_id, email)
    return await ProjectChatService.chat(db, student_id, request)


@router.get("/acknowledgements")
def get_acknowledgements():
    """Return natural varied acknowledgements for client-side wake word response."""
    return {"acknowledgements": VARIED_ACKNOWLEDGEMENTS}


@router.get("/health/gemini")
def check_gemini_health():
    """Diagnostic check for Google Gemini API configuration & connectivity."""
    return {
        "provider": "Google Gemini",
        "configured": GeminiService.is_configured(),
        "model": GeminiService.get_model_name(),
        "google_cloud_project": "projects/411579227111",
        "status": "READY" if GeminiService.is_configured() else "API_KEY_REQUIRED_IN_ENV",
    }


@router.post("/gemini/test")
def test_gemini_connection():
    """Runs a live test prompt against the Google Gemini API."""
    return GeminiService.test_connection("Respond with 'SkillExa Gemini Connection Verified' in 5 words.")

