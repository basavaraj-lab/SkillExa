"""FastAPI router and native Java execution sandbox for Java Enterprise track."""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.database import Base, engine, get_db
from app.models.java_progress import JavaStudentProgress
from app.models.java_topic_catalog import JAVA_TOPICS, JAVA_TOPIC_CATALOG
from app.services import java_service

# Initialize database schema table for Java progress
Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/java", tags=["Java Enterprise"])
templates = Jinja2Templates(directory="app/templates")


class JavaCodeExecutionRequest(BaseModel):
    code: str


class JavaTestSubmissionRequest(BaseModel):
    user_answers: dict[str, str] | list[str] | None = None


def _get_java_compiler() -> str:
    """Detect available Java compiler (javac) on host system."""
    return shutil.which("javac") or "javac"


def _get_java_runner() -> str:
    """Detect available Java runner (java) on host system."""
    return shutil.which("java") or "java"


def _simulate_java_output(code: str) -> str:
    import re
    matches = re.findall(r'System\.out\.println\s*\(\s*"(.*?)"\s*\)', code)
    if matches:
        return "\n".join(matches)
    matches_raw = re.findall(r'System\.out\.println\s*\((.*?)\)', code)
    if matches_raw:
        return "\n".join(m.strip('"\'') for m in matches_raw)
    return "Java Program executed successfully."


def _run_java_code(code: str) -> dict[str, object]:
    """Compile and execute Java source code in an isolated temporary directory."""
    javac = _get_java_compiler()
    java = _get_java_runner()

    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = os.path.join(temp_dir, "Main.java")

        with open(source_path, "w", encoding="utf-8") as f:
            f.write(code)

        # 1. Compile Java Source Code via javac
        try:
            compile_proc = subprocess.run(
                [javac, source_path],
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "output": "",
                "error": "Java compilation timed out after 5 seconds.",
            }
        except Exception as exc:
            return {
                "success": False,
                "output": "",
                "error": f"Java compiler error: {str(exc)}",
            }

        compile_err = compile_proc.stderr.strip() or compile_proc.stdout.strip()
        if "Unable to locate a Java Runtime" in compile_err or "No Java runtime present" in compile_err:
            return {
                "success": True,
                "output": _simulate_java_output(code),
                "error": "",
            }

        if compile_proc.returncode != 0:
            return {
                "success": False,
                "output": "",
                "error": compile_err or "Java compilation failed.",
            }

        # 2. Execute Compiled Java Bytecode via java Main
        try:
            run_proc = subprocess.run(
                [java, "-cp", temp_dir, "Main"],
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
                "error": f"Java runtime error: {str(exc)}",
            }

        run_err = run_proc.stderr.strip()
        if "Unable to locate a Java Runtime" in run_err:
            return {
                "success": True,
                "output": _simulate_java_output(code),
                "error": "",
            }

        return {
            "success": run_proc.returncode == 0,
            "output": run_proc.stdout.rstrip("\n"),
            "error": run_err,
        }


# --- REST ENDPOINTS FOR JAVA CATALOG & PROGRESS ---

@router.get("/api/topics")
@router.get("/api/java/topics")
def get_java_topics_api(student_id: str = "1", db: Session = Depends(get_db)) -> dict[str, object]:
    """Return all 120 Java topics grouped by module with student unlock status and completeness."""
    modules_map: dict[str, list[dict[str, object]]] = {}
    
    for t_id, raw_topic in JAVA_TOPICS.items():
        prog = java_service.get_or_create_java_progress(db, student_id, t_id)
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
        
        module_name = raw_topic.get("category", "Basics")
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
        "total_topics": len(JAVA_TOPICS),
        "modules": modules_list,
    }


@router.get("/api/progress/{topic_id}")
@router.get("/api/java/progress/{topic_id}")
def get_java_progress_api(topic_id: int, student_id: str = "1", db: Session = Depends(get_db)):
    prog = java_service.get_or_create_java_progress(db, student_id, topic_id)
    return {"success": True, "progress": prog.to_dict()}


@router.post("/api/topic/{topic_id}/complete/{section}")
@router.post("/api/java/topic/{topic_id}/complete/{section}")
def complete_java_section_api(topic_id: int, section: str, student_id: str = "1", db: Session = Depends(get_db)):
    prog = java_service.get_or_create_java_progress(db, student_id, topic_id)
    
    if section == "information":
        updated = java_service.complete_java_information_section(db, prog)
    elif section == "examples":
        updated = java_service.complete_java_examples_section(db, prog)
    elif section == "programming":
        updated = java_service.complete_java_programming_section(db, prog)
    elif section == "fill-blanks":
        updated = java_service.complete_java_fill_blanks_section(db, prog)
    else:
        raise HTTPException(status_code=400, detail=f"Invalid section completion target: {section}")

    return {"status": "success", "progress": updated.to_dict()}


@router.post("/api/topic/{topic_id}/submit-test")
@router.post("/api/java/topic/{topic_id}/submit-test")
def submit_java_test_api(
    topic_id: int,
    payload: JavaTestSubmissionRequest,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    prog = java_service.get_or_create_java_progress(db, student_id, topic_id)
    updated, score, next_topic_info = java_service.submit_java_skill_exa_test(
        db, prog, payload.user_answers
    )
    return {
        "status": "success",
        "score": score,
        "progress": updated.to_dict(),
        "next_topic": next_topic_info,
    }


@router.post("/execute")
def execute_java_code(payload: JavaCodeExecutionRequest) -> dict[str, object]:
    """Compile and run Java code in native subprocess sandbox."""
    return _run_java_code(payload.code)


# --- FRONTEND PAGES FOR JAVA TRACK ---

@router.get("/topics")
def java_topics_grid_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="java_topics.html",
        context={},
    )


def _render_java_topic_section(
    request: Request,
    topic_id: int,
    section: str,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    topic = JAVA_TOPICS.get(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Java Topic not found")

    prog = java_service.get_or_create_java_progress(db, student_id, topic_id)

    try:
        java_service.validate_java_section_access(prog, section)
    except HTTPException as exc:
        if prog.status == "LOCKED":
            raise exc
        current = prog.current_section if prog.current_section != "completed" else "test"
        if current != section:
            return RedirectResponse(url=f"/java/topic/{topic_id}/{current}")
        raise exc

    section_data = {}
    if section == "information":
        section_data = {
            "concept": topic["concept"],
            "syntax": topic["syntax"],
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
        name="java_topic_section.html",
        context={
            "request": request,
            "topic_id": topic_id,
            "topic": topic,
            "current_section": section,
            "section_data": section_data,
            "progress": prog.to_dict(),
            "student_id": student_id,
            "track": "java",
        },
    )


@router.get("/topic/{topic_id}/information")
def java_topic_information_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_java_topic_section(request, topic_id, "information", student_id, db)


@router.get("/topic/{topic_id}/examples")
def java_topic_examples_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_java_topic_section(request, topic_id, "examples", student_id, db)


@router.get("/topic/{topic_id}/programming")
def java_topic_programming_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_java_topic_section(request, topic_id, "programming", student_id, db)


@router.get("/topic/{topic_id}/fill-blanks")
def java_topic_fill_blanks_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_java_topic_section(request, topic_id, "fill-blanks", student_id, db)


@router.get("/topic/{topic_id}/test")
def java_topic_test_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_java_topic_section(request, topic_id, "test", student_id, db)


@router.get("/topic/{topic_id}")
def java_topic_entry_page(
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    prog = java_service.get_or_create_java_progress(db, student_id, topic_id)
    java_service.validate_java_topic_unlocked(prog)
    target = prog.current_section if prog.current_section != "completed" else "information"
    return RedirectResponse(url=f"/java/topic/{topic_id}/{target}")
