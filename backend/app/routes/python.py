"""FastAPI router and native execution sandbox for Python Programming track."""
from __future__ import annotations

import re
import sys
import subprocess

from fastapi import APIRouter, Depends, Form, HTTPException, Query, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.database import Base, engine, get_db
from app.models.progress import StudentProgress
from app.models.topic_catalog import PYTHON_TOPICS, TOPIC_CATALOG
from app.services import python_service

# Ensure progress database table is initialized
Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/python", tags=["Python Programming"])
templates = Jinja2Templates(directory="app/templates")


class PythonCodeExecutionRequest(BaseModel):
    code: str
    inputs: str | None = None


class PythonTestSubmissionRequest(BaseModel):
    user_answers: dict[str, str] | list[str] | None = None
    submitted_answers: dict[str, str] | list[str] | None = None


DEFAULT_SIMULATED_STDIN = "SkillExa\n100 20.5\nHello\n42\nTest\n"


def _run_python_code(code: str, inputs: str | None = None) -> dict[str, object]:
    """Execute Python code in a short-lived isolated subprocess with standard input support."""
    stdin_data = inputs if (inputs is not None and inputs.strip()) else DEFAULT_SIMULATED_STDIN
    try:
        completed = subprocess.run(
            [sys.executable, "-c", code],
            input=stdin_data,
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        return {
            "success": completed.returncode == 0,
            "output": completed.stdout.rstrip("\n"),
            "error": completed.stderr.rstrip("\n"),
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "output": "",
            "error": "Execution timed out after 5 seconds.",
        }
    except Exception as exc:
        return {
            "success": False,
            "output": "",
            "error": f"Runtime error: {str(exc)}",
        }


# --- API ENDPOINTS FOR PYTHON TRACK CATALOG & PROGRESS ---

@router.get("/api/topics")
@router.get("/api/python/topics")
def get_python_topics_api(student_id: str = "1", db: Session = Depends(get_db)) -> dict[str, object]:
    """Return all 23 Python topics grouped by module with student unlock status and completeness."""
    modules_map: dict[str, list[dict[str, object]]] = {}
    
    for t_id, raw_topic in PYTHON_TOPICS.items():
        prog = python_service.get_or_create_progress(db, student_id, t_id)
        is_unlocked = prog.status != "LOCKED"
        completeness = 100 if prog.topic_completed else (
            20 * (
                int(prog.information_completed) +
                int(prog.examples_completed) +
                int(prog.programming_completed) +
                int(prog.fill_blanks_completed) +
                int(prog.test_completed)
            )
        )
        
        module_name = raw_topic.get("category", "General Python")
        if module_name not in modules_map:
            modules_map[module_name] = []

        modules_map[module_name].append({
            "id": t_id,
            "title": raw_topic["title"],
            "difficulty": raw_topic["difficulty"],
            "duration": raw_topic["duration"],
            "status": prog.status,
            "current_section": prog.current_section,
            "is_unlocked": is_unlocked,
            "completeness": completeness,
        })

    modules_list = [
        {"module": m_name, "topics": t_list}
        for m_name, t_list in modules_map.items()
    ]

    return {
        "success": True,
        "total_topics": len(PYTHON_TOPICS),
        "modules": modules_list,
        "topics": [
            {
                "id": t_id,
                "title": raw_topic["title"],
                "difficulty": raw_topic["difficulty"],
                "duration": raw_topic["duration"],
                "status": python_service.get_or_create_progress(db, student_id, t_id).status,
                "current_section": python_service.get_or_create_progress(db, student_id, t_id).current_section,
                "is_unlocked": python_service.get_or_create_progress(db, student_id, t_id).status != "LOCKED",
                "completeness": 100 if python_service.get_or_create_progress(db, student_id, t_id).topic_completed else 0
            }
            for t_id, raw_topic in PYTHON_TOPICS.items()
        ]
    }


@router.get("/api/progress/{topic_id}")
@router.get("/api/python/progress/{topic_id}")
def get_python_progress_api(topic_id: int, student_id: str = "1", db: Session = Depends(get_db)):
    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    return {"success": True, "progress": prog.to_dict()}


@router.post("/api/topic/{topic_id}/complete/{section}")
@router.post("/api/python/topic/{topic_id}/complete/{section}")
def complete_python_section_api(topic_id: int, section: str, student_id: str = "1", db: Session = Depends(get_db)):
    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    
    if section == "information":
        updated = python_service.complete_information_section(db, prog)
    elif section == "examples":
        updated = python_service.complete_examples_section(db, prog)
    elif section == "programming":
        updated = python_service.complete_programming_section(db, prog)
    elif section == "fill-blanks":
        updated = python_service.complete_fill_blanks_section(db, prog)
    else:
        raise HTTPException(status_code=400, detail=f"Invalid section completion target: {section}")

    return {"status": "success", "progress": updated.to_dict()}


@router.post("/api/topic/{topic_id}/submit-test")
@router.post("/api/python/topic/{topic_id}/submit-test")
def submit_python_test_api(
    topic_id: int,
    payload: PythonTestSubmissionRequest,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    user_ans = payload.user_answers if payload.user_answers is not None else payload.submitted_answers
    updated, score, next_topic_info = python_service.submit_skill_exa_test(
        db, prog, user_ans
    )
    passed = score >= 50.0
    return {
        "status": "success",
        "score": score,
        "passed": passed,
        "progress": updated.to_dict(),
        "next_topic": next_topic_info,
        "message": "Topic Mastered!" if passed else "Score is below 50%. Minimum 50% required to pass. Please try again!",
    }


@router.post("/execute")
def execute_python_code(payload: PythonCodeExecutionRequest) -> dict[str, object]:
    """Execute Python code in isolated subprocess sandbox."""
    return _run_python_code(payload.code, payload.inputs)


# --- FRONTEND PAGES & SECTION ROUTING FOR PYTHON TRACK ---

@router.get("/topics")
def python_topics_grid_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="python_topics.html",
        context={},
    )


def _render_python_topic_section(
    request: Request,
    topic_id: int,
    section: str,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    topic = PYTHON_TOPICS.get(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Python Topic not found")

    prog = python_service.get_or_create_progress(db, student_id, topic_id)

    try:
        python_service.validate_section_access(prog, section)
    except HTTPException as exc:
        if prog.status == "LOCKED":
            raise exc
        current = prog.current_section if prog.current_section != "completed" else "test"
        if current != section:
            return RedirectResponse(url=f"/python/topic/{topic_id}/{current}")
        raise exc

    section_data = {}
    if section == "information":
        section_data = {
            "concept": topic["concept"],
            "theory": topic.get("theory", {}),
            "syntax": topic["syntax"],
        }
    elif section == "examples":
        section_data = {
            "example": topic["example"],
            "output": topic["output"],
            "theory_examples": topic.get("theory", {}).get("examples", []),
        }
    elif section == "programming":
        section_data = {
            "compiler": topic["compiler"],
            "practice": topic.get("compiler", {}),
        }
    elif section == "fill-blanks":
        fb_data = dict(topic["fill_blanks"])
        raw_q = fb_data.get("question", "")
        answers = fb_data.get("answers") or ([fb_data.get("answer")] if fb_data.get("answer") else [])
        normalized_q = re.sub(r'_____|____|___|\[\?\]|\{blank\}', '_____', raw_q)
        num_placeholders = normalized_q.count('_____')
        if len(answers) > num_placeholders:
            missing_count = len(answers) - num_placeholders
            extra_lines = ["\n# Fill in missing answer field:"]
            for i in range(num_placeholders + 1, len(answers) + 1):
                extra_lines.append(f"Blank {i}: _____")
            normalized_q += "\n" + "\n".join(extra_lines)
        fb_data["question"] = normalized_q
        section_data = {
            "fill_blanks": fb_data,
        }
    elif section == "test":
        section_data = {
            "questions": topic["skill_exa_test"],
            "total_questions": len(topic["skill_exa_test"]),
        }

    return templates.TemplateResponse(
        request=request,
        name="python_topic_section.html",
        context={
            "request": request,
            "topic_id": topic_id,
            "topic": topic,
            "current_section": section,
            "section_data": section_data,
            "progress": prog.to_dict(),
            "student_id": student_id,
            "track": "python",
        },
    )


@router.get("/topic/{topic_id}/information")
def python_topic_information_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_python_topic_section(request, topic_id, "information", student_id, db)


@router.get("/topic/{topic_id}/examples")
def python_topic_examples_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_python_topic_section(request, topic_id, "examples", student_id, db)


@router.get("/topic/{topic_id}/programming")
def python_topic_programming_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_python_topic_section(request, topic_id, "programming", student_id, db)


@router.get("/topic/{topic_id}/fill-blanks")
def python_topic_fill_blanks_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_python_topic_section(request, topic_id, "fill-blanks", student_id, db)


@router.get("/topic/{topic_id}/test")
def python_topic_test_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_python_topic_section(request, topic_id, "test", student_id, db)


@router.get("/topic/{topic_id}")
def python_topic_entry_page(
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    python_service.validate_topic_unlocked(prog)
    target = prog.current_section if prog.current_section != "completed" else "information"
    return RedirectResponse(url=f"/python/topic/{topic_id}/{target}")
