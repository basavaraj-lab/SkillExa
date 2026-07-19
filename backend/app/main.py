from datetime import datetime
import subprocess
import sys

from fastapi import FastAPI, HTTPException, Request
from fastapi import Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.routes.python import PYTHON_TOPICS

app = FastAPI(title="SkillExa Backend Engine")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Keep permissive CORS for local development workflows.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory persistence used by the existing API behavior.
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
def get_topics() -> list[dict[str, object]]:
    """Return topics with dynamic unlocked status based on user progress."""
    response: list[dict[str, object]] = []
    for topic in TOPICS_DB:
        is_unlocked = topic["id"] <= USER_PROGRESS["highest_unlocked_topic_id"]
        response.append({**topic, "is_unlocked": is_unlocked})
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
    """Render the dashboard as the root page."""
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={},
    )


@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "request": request,
        },
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


@app.get("/lesson/{topic_id}")
def lesson(request: Request, topic_id: int):
    topic = PYTHON_TOPICS.get(topic_id)
    if topic is None:
        raise HTTPException(status_code=404, detail="Lesson not found")

    return templates.TemplateResponse(
        request=request,
        name="lesson.html",
        context={"topic_id": topic_id, "topic": topic},
    )


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