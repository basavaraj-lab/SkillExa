from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.app.dependencies.db import get_db
from backend.app.models.quiz import Question
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.quiz import QuestionForStudentResponse

router = APIRouter(prefix="/questions", tags=["Topic Questions"])


@router.get("", response_model=ApiResponse[List[QuestionForStudentResponse]])
def get_topic_questions(
    section: Optional[str] = Query(None, description="'engineering', 'competitive', 'programming', 'dsa'"),
    subject: Optional[str] = Query(None),
    topic: Optional[str] = Query(None),
    subtopic: Optional[str] = Query(None),
    language: Optional[str] = Query(None),
    difficulty: Optional[str] = Query(None),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    """
    Section 10: Topic-Specific Questions.
    Ensures questions strictly belong to the requested subject/topic/subtopic/language.
    """
    query = db.query(Question)

    if section:
        query = query.filter(Question.section.ilike(f"%{section}%"))
    if subject:
        query = query.filter(Question.subject.ilike(f"%{subject}%"))
    if topic:
        query = query.filter(Question.topic.ilike(f"%{topic}%"))
    if subtopic:
        query = query.filter(Question.subtopic.ilike(f"%{subtopic}%"))
    if language:
        query = query.filter(Question.language.ilike(f"%{language}%"))
    if difficulty:
        query = query.filter(Question.difficulty == difficulty)

    questions = query.order_by(Question.order_index, Question.created_at.desc()).limit(limit).all()
    results = [QuestionForStudentResponse.model_validate(q) for q in questions]

    return ApiResponse(
        success=True,
        message=f"Retrieved {len(results)} topic-specific questions.",
        data=results,
    )
