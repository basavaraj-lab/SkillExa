"""FastAPI router for the Python learning curriculum."""
from __future__ import annotations

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.topic_catalog import PYTHON_TOPICS, TOPIC_CATALOG
from app.services import python_service

router = APIRouter(prefix="/python", tags=["Python"])


@router.get("/topics")
def get_python_topics(student_id: str = Query("1"), db: Session = Depends(get_db)) -> dict[str, object]:
    """Return the topic list shown in the learning path with dynamic DB progress."""
    response = []
    for meta in TOPIC_CATALOG:
        t_id = meta["id"]
        prog = python_service.get_or_create_progress(db, student_id, t_id)
        response.append({
            **meta,
            "status": prog.status,
            "is_unlocked": prog.status != "LOCKED",
            "current_section": prog.current_section,
            "completeness": 100 if prog.topic_completed else (
                20 * (
                    int(prog.information_completed) +
                    int(prog.examples_completed) +
                    int(prog.programming_completed) +
                    int(prog.fill_blanks_completed) +
                    int(prog.test_completed)
                )
            ),
        })
    return {
        "success": True,
        "total_topics": len(response),
        "topics": response,
    }


@router.get("/topics/{topic_id}")
def get_topic_details(topic_id: int) -> dict[str, object]:
    """Return full content for a single topic id."""
    topic = PYTHON_TOPICS.get(topic_id)
    if topic is None:
        return {
            "success": False,
            "message": "Topic not found",
        }

    return {
        "success": True,
        "topic": topic,
    }
