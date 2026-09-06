"""FastAPI router for backend-controlled topic learning flow APIs."""
from __future__ import annotations

from typing import Any, Dict, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.topic_catalog import PYTHON_TOPICS, TOPIC_CATALOG
from app.services import python_service

router = APIRouter(prefix="/api", tags=["Topic Learning API"])


@router.get("/topics")
def get_all_topics(student_id: str = Query("1"), db: Session = Depends(get_db)):
    """Return all topics in the curriculum with live DB student progress."""
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
    return {"success": True, "topics": response}


@router.get("/topics/{topic_id}")
def get_topic_overview(
    topic_id: int,
    student_id: str = Query("1"),
    db: Session = Depends(get_db),
):
    """Get topic details and student progress status."""
    topic = PYTHON_TOPICS.get(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    return {
        "success": True,
        "topic": {
            "id": topic["id"],
            "title": topic["title"],
            "difficulty": topic["difficulty"],
            "duration": topic["duration"],
        },
        "progress": prog.to_dict(),
    }


@router.get("/topics/{topic_id}/information")
def get_topic_information(
    topic_id: int,
    student_id: str = Query("1"),
    db: Session = Depends(get_db),
):
    """Retrieve Information section for a topic."""
    topic = PYTHON_TOPICS.get(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    python_service.validate_topic_unlocked(prog)

    return {
        "success": True,
        "topic_id": topic_id,
        "section": "information",
        "title": topic["title"],
        "data": {
            "concept": topic["concept"],
            "theory": topic["theory"],
            "syntax": topic["syntax"],
        },
        "progress": prog.to_dict(),
    }


@router.get("/topics/{topic_id}/examples")
def get_topic_examples(
    topic_id: int,
    student_id: str = Query("1"),
    db: Session = Depends(get_db),
):
    """Retrieve Examples section for a topic. Validates sequence."""
    topic = PYTHON_TOPICS.get(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    python_service.validate_section_access(prog, "examples")

    return {
        "success": True,
        "topic_id": topic_id,
        "section": "examples",
        "title": topic["title"],
        "data": {
            "example": topic["example"],
            "output": topic["output"],
            "theory_examples": topic["theory"].get("examples", []),
        },
        "progress": prog.to_dict(),
    }


@router.get("/topics/{topic_id}/programming")
def get_topic_programming(
    topic_id: int,
    student_id: str = Query("1"),
    db: Session = Depends(get_db),
):
    """Retrieve Programming section for a topic. Validates sequence."""
    topic = PYTHON_TOPICS.get(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    python_service.validate_section_access(prog, "programming")

    return {
        "success": True,
        "topic_id": topic_id,
        "section": "programming",
        "title": topic["title"],
        "data": {
            "compiler": topic["compiler"],
            "practice": topic["practice"],
        },
        "progress": prog.to_dict(),
    }


@router.get("/topics/{topic_id}/fill-blanks")
def get_topic_fill_blanks(
    topic_id: int,
    student_id: str = Query("1"),
    db: Session = Depends(get_db),
):
    """Retrieve Fill in the Blanks section for a topic. Validates sequence."""
    topic = PYTHON_TOPICS.get(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    python_service.validate_section_access(prog, "fill-blanks")

    return {
        "success": True,
        "topic_id": topic_id,
        "section": "fill-blanks",
        "title": topic["title"],
        "data": {
            "fill_blanks": topic["fill_blanks"],
        },
        "progress": prog.to_dict(),
    }


@router.get("/topics/{topic_id}/test")
def get_topic_test(
    topic_id: int,
    student_id: str = Query("1"),
    db: Session = Depends(get_db),
):
    """Retrieve SkillExa Test section for a topic. Validates sequence."""
    topic = PYTHON_TOPICS.get(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    python_service.validate_section_access(prog, "test")

    # Sanitize questions for student view (exclude direct answer keys if needed, or include for scoring)
    questions = topic["skill_exa_test"]
    client_questions = []
    for q in questions:
        client_questions.append({
            "question": q["question"],
            "options": q["options"],
        })

    return {
        "success": True,
        "topic_id": topic_id,
        "section": "test",
        "title": topic["title"],
        "data": {
            "questions": client_questions,
            "total_questions": len(questions),
        },
        "progress": prog.to_dict(),
    }


@router.get("/progress/{student_id}/{topic_id}")
def get_student_topic_progress(
    student_id: str,
    topic_id: int,
    db: Session = Depends(get_db),
):
    """Retrieve detailed progress state for a student on a specific topic."""
    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    return {
        "success": True,
        "student_id": student_id,
        "topic_id": topic_id,
        "progress": prog.to_dict(),
    }


@router.get("/progress/{student_id}")
def get_all_student_progress(
    student_id: str,
    db: Session = Depends(get_db),
):
    """Retrieve progress records across all topics for a student."""
    progresses = []
    for topic in TOPIC_CATALOG:
        t_id = topic["id"]
        prog = python_service.get_or_create_progress(db, student_id, t_id)
        progresses.append(prog.to_dict())
    return {
        "success": True,
        "student_id": student_id,
        "progress": progresses,
    }


@router.post("/progress/{student_id}/{topic_id}/complete-information")
def complete_information(
    student_id: str,
    topic_id: int,
    db: Session = Depends(get_db),
):
    """Mark Information section as completed and advance sequence to Examples."""
    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    updated_prog = python_service.complete_information_section(db, prog)
    return {
        "success": True,
        "message": "Information section completed.",
        "next_section": "examples",
        "progress": updated_prog.to_dict(),
    }


@router.post("/progress/{student_id}/{topic_id}/complete-examples")
def complete_examples(
    student_id: str,
    topic_id: int,
    db: Session = Depends(get_db),
):
    """Mark Examples section as completed and advance sequence to Programming."""
    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    updated_prog = python_service.complete_examples_section(db, prog)
    return {
        "success": True,
        "message": "Examples section completed.",
        "next_section": "programming",
        "progress": updated_prog.to_dict(),
    }


@router.post("/progress/{student_id}/{topic_id}/complete-programming")
def complete_programming(
    student_id: str,
    topic_id: int,
    payload: Optional[Dict[str, Any]] = None,
    db: Session = Depends(get_db),
):
    """Mark Programming section as completed and advance sequence to Fill in Blanks."""
    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    updated_prog = python_service.complete_programming_section(db, prog)
    return {
        "success": True,
        "message": "Programming section completed.",
        "next_section": "fill-blanks",
        "progress": updated_prog.to_dict(),
    }


@router.post("/progress/{student_id}/{topic_id}/complete-fill-blanks")
def complete_fill_blanks(
    student_id: str,
    topic_id: int,
    payload: Optional[Dict[str, Any]] = None,
    db: Session = Depends(get_db),
):
    """Validate Fill in Blanks answers, mark section complete, and advance sequence to Test."""
    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    
    # Validate answers if passed
    topic = PYTHON_TOPICS.get(topic_id)
    if topic and payload and "answers" in payload:
        fill_data = topic.get("fill_blanks", {})
        expected = fill_data.get("answers") or ([fill_data.get("answer")] if fill_data.get("answer") else [])
        user_ans = payload["answers"]
        if expected and isinstance(user_ans, list):
            correct = len(expected) == len(user_ans) and all(
                str(expected[i]).strip().lower() == str(user_ans[i]).strip().lower()
                for i in range(len(expected))
            )
            if not correct:
                raise HTTPException(
                    status_code=400,
                    detail=f"Answers incorrect. Expected: {', '.join(expected)}",
                )

    updated_prog = python_service.complete_fill_blanks_section(db, prog)
    return {
        "success": True,
        "message": "Fill in the Blanks section completed.",
        "next_section": "test",
        "progress": updated_prog.to_dict(),
    }


@router.post("/progress/{student_id}/{topic_id}/submit-test")
def submit_test(
    student_id: str,
    topic_id: int,
    payload: Optional[Dict[str, Any]] = None,
    db: Session = Depends(get_db),
):
    """
    Submit SkillExa Test, compute score, mark topic COMPLETED, unlock next topic,
    and return next topic information.
    """
    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    answers = (payload.get("answers") or payload.get("submitted_answers")) if payload else None

    updated_prog, score, next_topic = python_service.submit_skill_exa_test(db, prog, answers)

    return {
        "success": True,
        "message": "SkillExa Test completed successfully!",
        "score": score,
        "topic_completed": True,
        "status": updated_prog.status,
        "progress": updated_prog.to_dict(),
        "next_topic": next_topic,
    }
