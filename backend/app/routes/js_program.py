"""FastAPI router and native Node.js execution sandbox for JavaScript track."""
from __future__ import annotations

import os
import shutil
import subprocess

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.database import Base, engine, get_db
from app.models.js_progress import JSStudentProgress
from app.models.js_topic_catalog import JS_TOPICS, JS_TOPIC_CATALOG
from app.services import js_service

# Initialize database schema table for JS progress
Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/js", tags=["JavaScript Track"])
templates = Jinja2Templates(directory="app/templates")


class JSCodeExecutionRequest(BaseModel):
    code: str
    inputs: str | None = None


DEFAULT_SIMULATED_STDIN = "SkillExa\n100 20.5\nHello\n42\nTest\n"


class JSTestSubmissionRequest(BaseModel):
    user_answers: dict[str, str] | list[str] | None = None


def _get_js_runner() -> str:
    """Detect available Node.js runtime on host system."""
    return shutil.which("node") or "node"


def _simulate_js_output(code: str) -> dict[str, object]:
    import re
    # 1. Check for unreplaced blanks like ____
    if re.search(r'_+', code):
        return {
            "success": False,
            "output": "",
            "error": "SyntaxError: Unexpected token '____' / unreplaced blank placeholder",
        }

    # 2. Check for console.log with strings
    matches = re.findall(r'console\.log\s*\(\s*["`\'](.*?)["`\']\s*\)', code, re.DOTALL)
    if matches:
        clean_output = "\n".join(m.replace('\\n', '\n') for m in matches)
        return {
            "success": True,
            "output": clean_output,
            "error": "",
        }

    # 3. Check for general console.log(...)
    matches_raw = re.findall(r'console\.log\s*\((.*?)\)', code, re.DOTALL)
    if matches_raw:
        clean_output = "\n".join(m.strip('"\'`') for m in matches_raw)
        return {
            "success": True,
            "output": clean_output,
            "error": "",
        }

    return {
        "success": True,
        "output": "JavaScript code executed successfully.",
        "error": "",
    }


def _run_js_code(code: str, inputs: str | None = None) -> dict[str, object]:
    """Execute JavaScript code via Node.js sandbox or fallback simulation."""
    import re
    if re.search(r'_+', code):
        return {
            "success": False,
            "output": "",
            "error": "SyntaxError: Unexpected token '____' / unreplaced blank placeholder",
        }

    node_bin = _get_js_runner()
    stdin_data = inputs if (inputs is not None and inputs.strip()) else DEFAULT_SIMULATED_STDIN

    try:
        run_proc = subprocess.run(
            [node_bin, "-e", code],
            input=stdin_data,
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        run_err = run_proc.stderr.strip()
        return {
            "success": run_proc.returncode == 0,
            "output": run_proc.stdout.rstrip("\n"),
            "error": run_err,
        }
    except FileNotFoundError:
        return _simulate_js_output(code)
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "output": "",
            "error": "Execution timed out after 5 seconds.",
        }
    except Exception as exc:
        return _simulate_js_output(code)


# --- REST ENDPOINTS FOR JS CATALOG & PROGRESS ---

@router.get("/api/topics")
@router.get("/api/js/topics")
def get_js_topics_api(student_id: str = "1", db: Session = Depends(get_db)) -> dict[str, object]:
    """Return all 101 JavaScript topics grouped by module with student unlock status and completeness."""
    modules_map: dict[str, list[dict[str, object]]] = {}
    
    for t_id, raw_topic in JS_TOPICS.items():
        prog = js_service.get_or_create_js_progress(db, student_id, t_id)
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
        
        module_name = raw_topic.get("category", "Fundamentals")
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
        "total_topics": len(JS_TOPICS),
        "modules": modules_list,
    }


@router.get("/api/progress/{topic_id}")
@router.get("/api/js/progress/{topic_id}")
def get_js_progress_api(topic_id: int, student_id: str = "1", db: Session = Depends(get_db)):
    prog = js_service.get_or_create_js_progress(db, student_id, topic_id)
    return {"success": True, "progress": prog.to_dict()}


@router.post("/api/topic/{topic_id}/complete/{section}")
@router.post("/api/js/topic/{topic_id}/complete/{section}")
def complete_js_section_api(topic_id: int, section: str, student_id: str = "1", db: Session = Depends(get_db)):
    prog = js_service.get_or_create_js_progress(db, student_id, topic_id)
    
    if section == "information":
        updated = js_service.complete_js_information_section(db, prog)
    elif section == "examples":
        updated = js_service.complete_js_examples_section(db, prog)
    elif section == "programming":
        updated = js_service.complete_js_programming_section(db, prog)
    elif section == "fill-blanks":
        updated = js_service.complete_js_fill_blanks_section(db, prog)
    else:
        raise HTTPException(status_code=400, detail=f"Invalid section completion target: {section}")

    return {"status": "success", "progress": updated.to_dict()}


@router.post("/api/topic/{topic_id}/submit-test")
@router.post("/api/js/topic/{topic_id}/submit-test")
def submit_js_test_api(
    topic_id: int,
    payload: JSTestSubmissionRequest,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    prog = js_service.get_or_create_js_progress(db, student_id, topic_id)
    updated, score, next_topic_info = js_service.submit_js_skill_exa_test(
        db, prog, payload.user_answers
    )
    return {
        "status": "success",
        "score": score,
        "progress": updated.to_dict(),
        "next_topic": next_topic_info,
    }


@router.post("/execute")
def execute_js_code(payload: JSCodeExecutionRequest) -> dict[str, object]:
    """Run JavaScript code in native Node.js or simulation sandbox."""
    return _run_js_code(payload.code, payload.inputs)


# --- FRONTEND PAGES FOR JAVASCRIPT TRACK ---

@router.get("/topics")
def js_topics_grid_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="js_topics.html",
        context={},
    )


def _render_js_topic_section(
    request: Request,
    topic_id: int,
    section: str,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    topic = JS_TOPICS.get(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="JavaScript Topic not found")

    prog = js_service.get_or_create_js_progress(db, student_id, topic_id)

    try:
        js_service.validate_js_section_access(prog, section)
    except HTTPException as exc:
        if prog.status == "LOCKED":
            raise exc
        current = prog.current_section if prog.current_section != "completed" else "test"
        if current != section:
            return RedirectResponse(url=f"/js/topic/{topic_id}/{current}")
        raise exc

    section_data = {}
    if section == "information":
        section_data = {
            "concept": topic["concept"],
            "syntax": topic["syntax"],
            "theory": topic.get("theory", ""),
        }
    elif section == "examples":
        section_data = {
            "example": topic["example"],
            "output": topic.get("output", topic.get("example", {}).get("output", "")),
        }
    elif section == "programming":
        section_data = {
            "compiler": topic["compiler"],
            "practice": topic.get("compiler", {}),
        }
    elif section == "fill-blanks":
        section_data = {
            "fill_blanks": topic["fill_blanks"],
        }
    elif section == "test":
        section_data = {
            "questions": topic["skill_exa_test"],
            "total_questions": len(topic["skill_exa_test"]),
        }

    return templates.TemplateResponse(
        request=request,
        name="js_topic_section.html",
        context={
            "request": request,
            "topic_id": topic_id,
            "topic": topic,
            "current_section": section,
            "section_data": section_data,
            "progress": prog.to_dict(),
            "student_id": student_id,
            "track": "js",
        },
    )


@router.get("/topic/{topic_id}/information")
def js_topic_information_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_js_topic_section(request, topic_id, "information", student_id, db)


@router.get("/topic/{topic_id}/examples")
def js_topic_examples_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_js_topic_section(request, topic_id, "examples", student_id, db)


@router.get("/topic/{topic_id}/programming")
def js_topic_programming_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_js_topic_section(request, topic_id, "programming", student_id, db)


@router.get("/topic/{topic_id}/fill-blanks")
def js_topic_fill_blanks_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_js_topic_section(request, topic_id, "fill-blanks", student_id, db)


@router.get("/topic/{topic_id}/test")
def js_topic_test_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_js_topic_section(request, topic_id, "test", student_id, db)


@router.get("/topic/{topic_id}")
def js_topic_entry_page(
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    prog = js_service.get_or_create_js_progress(db, student_id, topic_id)
    js_service.validate_js_topic_unlocked(prog)
    target = prog.current_section if prog.current_section != "completed" else "information"
    return RedirectResponse(url=f"/js/topic/{topic_id}/{target}")
