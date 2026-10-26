from typing import Any, List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import get_current_user
from backend.app.dependencies.db import get_db
from backend.app.models.user import User
from backend.app.schemas.aptitude_test import (
    AptitudeCategoriesResponse,
    AptitudeTestActiveResponse,
    AptitudeTestHistoryItem,
    AptitudeTestResultResponse,
    CreateAptitudeTestRequest,
    SaveAptitudeResponseRequest,
    SubmitAptitudeTestRequest,
)
from backend.app.schemas.common import ApiResponse
from backend.app.services.aptitude_service import AptitudeService

router = APIRouter(prefix="/aptitude", tags=["LLM Aptitude Test"])


@router.get("/categories", response_model=ApiResponse[AptitudeCategoriesResponse])
def get_aptitude_categories():
    """
    Retrieve all supported aptitude categories, topics, difficulty levels, and test presets.
    """
    categories_data = AptitudeService.get_categories()
    return ApiResponse(
        success=True,
        message="Aptitude categories and presets retrieved successfully.",
        data=categories_data,
    )


@router.post("/attempts", response_model=ApiResponse[AptitudeTestActiveResponse], status_code=status.HTTP_201_CREATED)
def start_aptitude_test_attempt(
    req: CreateAptitudeTestRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Generate a fresh set of aptitude questions using the configured LLM provider,
    securely store the answer key, and initialize a new test attempt for the student.
    Correct answers and explanations are strictly omitted while the test is active.
    """
    attempt = AptitudeService.start_test_attempt(db, current_user, req)
    return ApiResponse(
        success=True,
        message="Aptitude test generated successfully.",
        data=attempt,
    )


@router.get("/attempts/{attempt_id}", response_model=ApiResponse[Any])
def get_aptitude_test_attempt(
    attempt_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Retrieve an active or completed aptitude test attempt.
    If active, questions are returned without answer keys.
    If completed, full score breakdown and step-by-step explanations are returned.
    """
    data = AptitudeService.get_attempt(db, current_user, attempt_id)
    return ApiResponse(
        success=True,
        message="Aptitude attempt retrieved.",
        data=data,
    )


@router.put("/attempts/{attempt_id}/save-response", response_model=ApiResponse[dict])
def save_aptitude_question_response(
    attempt_id: str,
    req: SaveAptitudeResponseRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Auto-save an option selection for a question while the test is in progress.
    Preserves state across page refreshes.
    """
    res = AptitudeService.save_response(db, current_user, attempt_id, req)
    return ApiResponse(
        success=True,
        message="Response saved.",
        data=res,
    )


@router.post("/attempts/{attempt_id}/submit", response_model=ApiResponse[AptitudeTestResultResponse])
def submit_aptitude_test_attempt(
    attempt_id: str,
    req: SubmitAptitudeTestRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Submit test attempt for final backend evaluation, score calculation with negative marking,
    and release of official answer keys with detailed explanations.
    """
    results = AptitudeService.submit_attempt(db, current_user, attempt_id, req)
    return ApiResponse(
        success=True,
        message="Aptitude test evaluated and scored successfully.",
        data=results,
    )


@router.get("/history", response_model=ApiResponse[List[AptitudeTestHistoryItem]])
def get_aptitude_test_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Retrieve past aptitude test attempts and score history for the authenticated student.
    """
    history = AptitudeService.get_user_history(db, current_user)
    return ApiResponse(
        success=True,
        message="Aptitude history retrieved.",
        data=history,
    )
