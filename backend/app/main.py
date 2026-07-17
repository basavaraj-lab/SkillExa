from datetime import datetime

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

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
        context={},
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
    return templates.TemplateResponse(
        request=request,
        name="lesson.html",
        context={"topic_id": topic_id},
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