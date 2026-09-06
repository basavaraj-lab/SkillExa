"""FastAPI router and native C execution sandbox for C Programming track."""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile

from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.database import Base, engine, get_db
from app.models.c_progress import CStudentProgress
from app.models.c_topic_catalog import C_TOPICS, C_TOPIC_CATALOG
from app.services import c_service

# Ensure C progress database table is initialized
Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/c", tags=["C Programming"])
templates = Jinja2Templates(directory="app/templates")


class CCodeExecutionRequest(BaseModel):
    code: str


class CTestSubmissionRequest(BaseModel):
    user_answers: dict[str, str] | list[str] | None = None


def _get_c_compiler() -> str:
    """Detect available C compiler on host system (gcc or clang)."""
    return shutil.which("gcc") or shutil.which("clang") or "gcc"


def _run_c_code(code: str) -> dict[str, object]:
    """Compile and execute C program code in a short-lived isolated subprocess."""
    compiler = _get_c_compiler()

    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = os.path.join(temp_dir, "main.c")
        binary_path = os.path.join(temp_dir, "main_bin")

        with open(source_path, "w", encoding="utf-8") as f:
            f.write(code)

        # 1. Compile C Source Code
        try:
            compile_proc = subprocess.run(
                [compiler, "-O2", source_path, "-o", binary_path],
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "output": "",
                "error": "Compilation timed out after 5 seconds.",
            }
        except Exception as exc:
            return {
                "success": False,
                "output": "",
                "error": f"Compiler error: {str(exc)}",
            }

        if compile_proc.returncode != 0:
            return {
                "success": False,
                "output": "",
                "error": compile_proc.stderr.strip() or "C compilation failed.",
            }

        # 2. Execute Compiled Binary
        try:
            run_proc = subprocess.run(
                [binary_path],
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
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

        return {
            "success": run_proc.returncode == 0,
            "output": run_proc.stdout.rstrip("\n"),
            "error": run_proc.stderr.rstrip("\n"),
        }


# --- API ENDPOINTS FOR C TRACK CATALOG & PROGRESS ---

@router.get("/api/topics")
@router.get("/api/c/topics")
def get_c_topics_api(student_id: str = "1", db: Session = Depends(get_db)) -> dict[str, object]:
    """Return all 48 C topics grouped by module with student unlock status and completeness."""
    modules_map: dict[str, list[dict[str, object]]] = {}
    
    for t_id, raw_topic in C_TOPICS.items():
        prog = c_service.get_or_create_c_progress(db, student_id, t_id)
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
        
        module_name = raw_topic.get("category", "General C Concepts")
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
        "total_topics": len(C_TOPICS),
        "modules": modules_list,
    }


@router.get("/api/progress/{topic_id}")
@router.get("/api/c/progress/{topic_id}")
def get_c_progress_api(topic_id: int, student_id: str = "1", db: Session = Depends(get_db)):
    prog = c_service.get_or_create_c_progress(db, student_id, topic_id)
    return {"success": True, "progress": prog.to_dict()}


@router.post("/api/topic/{topic_id}/complete/{section}")
@router.post("/api/c/topic/{topic_id}/complete/{section}")
def complete_c_section_api(topic_id: int, section: str, student_id: str = "1", db: Session = Depends(get_db)):
    prog = c_service.get_or_create_c_progress(db, student_id, topic_id)
    
    if section == "information":
        updated = c_service.complete_c_information_section(db, prog)
    elif section == "examples":
        updated = c_service.complete_c_examples_section(db, prog)
    elif section == "programming":
        updated = c_service.complete_c_programming_section(db, prog)
    elif section == "fill-blanks":
        updated = c_service.complete_c_fill_blanks_section(db, prog)
    else:
        raise HTTPException(status_code=400, detail=f"Invalid section completion target: {section}")

    return {"status": "success", "progress": updated.to_dict()}


@router.post("/api/topic/{topic_id}/submit-test")
@router.post("/api/c/topic/{topic_id}/submit-test")
def submit_c_test_api(
    topic_id: int,
    payload: CTestSubmissionRequest,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    prog = c_service.get_or_create_c_progress(db, student_id, topic_id)
    updated, score, next_topic_info = c_service.submit_c_skill_exa_test(
        db, prog, payload.user_answers
    )
    return {
        "status": "success",
        "score": score,
        "progress": updated.to_dict(),
        "next_topic": next_topic_info,
    }


@router.post("/execute")
def execute_c_code(payload: CCodeExecutionRequest) -> dict[str, object]:
    """Compile and run C code in native subprocess sandbox."""
    return _run_c_code(payload.code)


# --- FRONTEND PAGES & SECTION ROUTING FOR C TRACK ---

@router.get("/topics")
def c_topics_grid_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="c_topics.html",
        context={},
    )


def _render_c_topic_section(
    request: Request,
    topic_id: int,
    section: str,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    topic = C_TOPICS.get(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="C Topic not found")

    prog = c_service.get_or_create_c_progress(db, student_id, topic_id)

    try:
        c_service.validate_c_section_access(prog, section)
    except HTTPException as exc:
        if prog.status == "LOCKED":
            raise exc
        current = prog.current_section if prog.current_section != "completed" else "test"
        if current != section:
            return RedirectResponse(url=f"/c/topic/{topic_id}/{current}")
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
        name="c_topic_section.html",
        context={
            "request": request,
            "topic_id": topic_id,
            "topic": topic,
            "current_section": section,
            "section_data": section_data,
            "progress": prog.to_dict(),
            "student_id": student_id,
            "track": "c",
        },
    )


@router.get("/topic/{topic_id}/information")
def c_topic_information_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_c_topic_section(request, topic_id, "information", student_id, db)


@router.get("/topic/{topic_id}/examples")
def c_topic_examples_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_c_topic_section(request, topic_id, "examples", student_id, db)


@router.get("/topic/{topic_id}/programming")
def c_topic_programming_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_c_topic_section(request, topic_id, "programming", student_id, db)


@router.get("/topic/{topic_id}/fill-blanks")
def c_topic_fill_blanks_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_c_topic_section(request, topic_id, "fill-blanks", student_id, db)


@router.get("/topic/{topic_id}/test")
def c_topic_test_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_c_topic_section(request, topic_id, "test", student_id, db)


@router.get("/topic/{topic_id}")
def c_topic_entry_page(
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    prog = c_service.get_or_create_c_progress(db, student_id, topic_id)
    c_service.validate_c_topic_unlocked(prog)
    target = prog.current_section if prog.current_section != "completed" else "information"
    return RedirectResponse(url=f"/c/topic/{topic_id}/{target}")
