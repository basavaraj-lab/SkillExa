from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import get_current_student
from backend.app.dependencies.db import get_db
from backend.app.models.notification import StudentProgress
from backend.app.models.user import StudentProfile
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.progress import StudentStatsResponse, TopicProgressResponse
from backend.app.services.progress_service import ProgressService

router = APIRouter(prefix="/progress", tags=["Progress & Analytics"])


@router.get("/summary", response_model=ApiResponse[StudentStatsResponse])
def get_my_progress_summary(
    student: StudentProfile = Depends(get_current_student),
    db: Session = Depends(get_db),
):
    stats = ProgressService.get_student_stats(db, student)
    return ApiResponse(
        success=True,
        message="Student progress summary retrieved.",
        data=stats,
    )


@router.get("/topics", response_model=ApiResponse[List[TopicProgressResponse]])
def get_topics_progress(
    section: Optional[str] = Query(None),
    subject: Optional[str] = Query(None),
    student: StudentProfile = Depends(get_current_student),
    db: Session = Depends(get_db),
):
    query = db.query(StudentProgress).filter(StudentProgress.student_id == student.id)
    if section:
        query = query.filter(StudentProgress.section == section)
    if subject:
        query = query.filter(StudentProgress.subject.ilike(f"%{subject}%"))

    records = query.order_by(StudentProgress.last_activity_at.desc()).all()
    results = [TopicProgressResponse.model_validate(r) for r in records]
    return ApiResponse(
        success=True,
        message="Topic progress records retrieved.",
        data=results,
    )
