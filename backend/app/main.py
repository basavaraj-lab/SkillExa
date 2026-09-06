from datetime import datetime
import subprocess
import sys

from fastapi import Depends, FastAPI, Form, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.database import Base, engine, get_db
from app.models.topic_catalog import PYTHON_TOPICS
from app.routes.api import router as api_router
from app.routes.c_program import get_c_topics_api, router as c_router
from app.routes.cpp_program import get_cpp_topics_api, router as cpp_router
from app.routes.features import router as features_router
from app.routes.java_program import get_java_topics_api, router as java_router
from app.routes.python import router as python_router
from app.services import python_service

# Initialize database schema tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SkillExa Backend Engine")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Register API routers
app.include_router(api_router)
app.include_router(c_router)
app.include_router(cpp_router)
app.include_router(features_router)
app.include_router(java_router)
app.include_router(python_router)

@app.get("/api/c/topics")
def api_c_topics_alias(student_id: str = "1", db: Session = Depends(get_db)):
    return get_c_topics_api(student_id, db)

@app.get("/api/cpp/topics")
def api_cpp_topics_alias(student_id: str = "1", db: Session = Depends(get_db)):
    return get_cpp_topics_api(student_id, db)

@app.get("/api/java/topics")
def api_java_topics_alias(student_id: str = "1", db: Session = Depends(get_db)):
    return get_java_topics_api(student_id, db)

# Keep permissive CORS for local development workflows.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory persistence used by fallback legacy endpoints.
USER_PROGRESS = {
    "highest_unlocked_topic_id": 2,
    "daily_quizzes_completed": 0,
    "last_quiz_timestamp": datetime.now().strftime("%Y-%m-%d"),
    "xp": 1450,
    "streak": 5,
}

TOPICS_DB = [
    {"id": 1, "name": "Introduction to Python Core", "difficulty": "Beginner", "time": "25 min", "completeness": 100},
    {"id": 2, "name": "Variables & Memory Registers", "difficulty": "Beginner", "time": "40 min", "completeness": 0},
    {"id": 3, "name": "Advanced Native Structures", "difficulty": "Intermediate", "time": "90 min", "completeness": 0},
    {"id": 4, "name": "Conditional Statements & Logic", "difficulty": "Intermediate", "time": "45 min", "completeness": 0},
]


class QuizSubmission(BaseModel):
    topic_id: int
    selected_option: str
    time_remaining: int


class CodeExecutionRequest(BaseModel):
    code: str


def _run_python_code(code: str) -> dict[str, object]:
    """Run lesson code in a short-lived Python subprocess and return its output."""
    try:
        completed = subprocess.run(
            [sys.executable, "-c", code],
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

    stdout = completed.stdout.rstrip("\n")
    stderr = completed.stderr.rstrip("\n")

    return {
        "success": completed.returncode == 0,
        "output": stdout,
        "error": stderr,
    }


@app.get("/python/topics")
def get_topics(student_id: str = "1", db: Session = Depends(get_db)) -> list[dict[str, object]]:
    """Return topics with dynamic unlocked status based on database user progress."""
    response: list[dict[str, object]] = []
    for topic in TOPICS_DB:
        t_id = topic["id"]
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
        response.append({
            **topic,
            "is_unlocked": is_unlocked,
            "completeness": completeness,
            "status": prog.status,
        })
    return response


@app.get("/user/limits")
def get_user_limits() -> dict[str, int]:
    """Return how many free daily quiz attempts are still available."""
    current_date = datetime.now().strftime("%Y-%m-%d")
    if USER_PROGRESS["last_quiz_timestamp"] != current_date:
        USER_PROGRESS["daily_quizzes_completed"] = 0
        USER_PROGRESS["last_quiz_timestamp"] = current_date

    return {
        "daily_quizzes_completed": USER_PROGRESS["daily_quizzes_completed"],
        "max_free_daily_quizzes": 2,
        "streak": USER_PROGRESS["streak"],
        "xp": USER_PROGRESS["xp"],
    }


@app.post("/quiz/submit")
def submit_quiz(submission: QuizSubmission) -> dict[str, object]:
    """Submit a quiz and unlock the next topic when appropriate."""
    if USER_PROGRESS["daily_quizzes_completed"] >= 2:
        raise HTTPException(
            status_code=403,
            detail="Daily free tasks completed! Upgrade to Premium or wait until tomorrow.",
        )

    if submission.topic_id > USER_PROGRESS["highest_unlocked_topic_id"]:
        raise HTTPException(
            status_code=400,
            detail="This topic is locked. Complete the previous modules first!",
        )

    USER_PROGRESS["daily_quizzes_completed"] += 1
    USER_PROGRESS["xp"] += 150

    if submission.topic_id == USER_PROGRESS["highest_unlocked_topic_id"]:
        USER_PROGRESS["highest_unlocked_topic_id"] += 1
        unlocked_new_topic = True
    else:
        unlocked_new_topic = False

    for topic in TOPICS_DB:
        if topic["id"] == submission.topic_id:
            topic["completeness"] = 100

    return {
        "status": "success",
        "message": "Lesson cracked successfully!",
        "new_topic_unlocked": unlocked_new_topic,
        "highest_unlocked_id": USER_PROGRESS["highest_unlocked_topic_id"],
        "daily_quizzes_completed": USER_PROGRESS["daily_quizzes_completed"],
        "xp_gained": 150,
    }


@app.post("/python/execute")
def execute_python_code(payload: CodeExecutionRequest) -> dict[str, object]:
    """Run lesson code in a short-lived Python subprocess and return its output."""
    return _run_python_code(payload.code)


@app.get("/")
def home(request: Request):
    """Render the starting landing page of SkillExa."""
    return templates.TemplateResponse(
        request=request,
        name="landing.html",
        context={},
    )


@app.get("/languages")
def languages_page(request: Request):
    """Render the Programming Languages track hub."""
    return templates.TemplateResponse(
        request=request,
        name="languages.html",
        context={},
    )


@app.get("/dsa")
def dsa_page(request: Request):
    """Render the Data Structures & Algorithms practice hub."""
    return templates.TemplateResponse(
        request=request,
        name="dsa.html",
        context={},
    )


@app.get("/mock-interview")
def mock_interview_page(request: Request):
    """Render the AI Mock Interview studio."""
    return templates.TemplateResponse(
        request=request,
        name="mock_interview.html",
        context={},
    )


@app.get("/resume-builder")
def resume_builder_page(request: Request):
    """Render the AI Resume Builder studio."""
    return templates.TemplateResponse(
        request=request,
        name="resume_builder.html",
        context={},
    )


@app.get("/.well-known/appspecific/com.chrome.devtools.json")
def chrome_devtools():
    """Handle Chrome DevTools auto-discovery probe silently."""
    return {}


@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"request": request},
    )


@app.get("/topics")
def topics(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="topics.html",
        context={},
    )


@app.get("/quiz")
def quiz(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="quiz.html",
        context={},
    )


# --- DEDICATED SEPARATE FRONTEND TOPIC SECTION ROUTES ---

def _render_topic_section(
    request: Request,
    topic_id: int,
    section: str,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    topic = PYTHON_TOPICS.get(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    prog = python_service.get_or_create_progress(db, student_id, topic_id)

    try:
        python_service.validate_section_access(prog, section)
    except HTTPException as exc:
        if prog.status == "LOCKED":
            raise exc
        current = prog.current_section if prog.current_section != "completed" else "test"
        if current != section:
            return RedirectResponse(url=f"/topic/{topic_id}/{current}")
        raise exc

    section_data = {}
    if section == "information":
        section_data = {
            "concept": topic["concept"],
            "theory": topic["theory"],
            "syntax": topic["syntax"],
        }
    elif section == "examples":
        section_data = {
            "example": topic["example"],
            "output": topic["output"],
            "theory_examples": topic["theory"].get("examples", []),
        }
    elif section == "programming":
        section_data = {
            "compiler": topic["compiler"],
            "practice": topic["practice"],
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
        name="python_topic_section.html",
        context={
            "request": request,
            "topic_id": topic_id,
            "topic": topic,
            "current_section": section,
            "section_data": section_data,
            "progress": prog.to_dict(),
            "student_id": student_id,
        },
    )


@app.get("/topic/{topic_id}/information")
def topic_information_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_topic_section(request, topic_id, "information", student_id, db)


@app.get("/topic/{topic_id}/examples")
def topic_examples_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_topic_section(request, topic_id, "examples", student_id, db)


@app.get("/topic/{topic_id}/programming")
def topic_programming_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_topic_section(request, topic_id, "programming", student_id, db)


@app.get("/topic/{topic_id}/fill-blanks")
def topic_fill_blanks_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_topic_section(request, topic_id, "fill-blanks", student_id, db)


@app.get("/topic/{topic_id}/test")
def topic_test_page(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return _render_topic_section(request, topic_id, "test", student_id, db)


@app.get("/topic/{topic_id}")
def topic_entry_page(
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    prog = python_service.get_or_create_progress(db, student_id, topic_id)
    python_service.validate_topic_unlocked(prog)
    target = prog.current_section if prog.current_section != "completed" else "information"
    return RedirectResponse(url=f"/topic/{topic_id}/{target}")


@app.get("/lesson/{topic_id}")
def lesson(
    request: Request,
    topic_id: int,
    student_id: str = "1",
    db: Session = Depends(get_db),
):
    return RedirectResponse(url=f"/topic/{topic_id}")


@app.post("/lesson/{topic_id}/execute")
def execute_lesson(request: Request, topic_id: int, code: str = Form(...)):
    topic = PYTHON_TOPICS.get(topic_id)
    if topic is None:
        raise HTTPException(status_code=404, detail="Lesson not found")

    execution_result = _run_python_code(code)
    return templates.TemplateResponse(
        request=request,
        name="lesson.html",
        context={
            "topic_id": topic_id,
            "topic": topic,
            "submitted_code": code,
            "execution_output": execution_result["output"] or execution_result["error"] or "[No output]",
            "execution_success": execution_result["success"],
        },
    )


@app.get("/validate")
def validate() -> dict[str, list[str]]:
    """Validate the Python topics dataset used by the backend route module."""
    from app.routes.validate_python_topic import (
        load_topics,
        validate_examples,
        validate_structure,
    )

    topics_data = load_topics()
    structure_issues = validate_structure(topics_data)
    example_issues = validate_examples(topics_data)
    return {
        "structure_issues": structure_issues,
        "example_issues": example_issues,
    }