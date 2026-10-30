from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class TopicProgressResponse(BaseModel):
    section: str
    subject: str
    topic: str
    subtopic: Optional[str] = None
    mastery_percentage: float
    quizzes_completed: int
    quiz_accuracy: float
    notes_read: int
    coding_solved: int
    last_activity_at: datetime

    class Config:
        from_attributes = True


class WeeklyDayActivity(BaseModel):
    day: str          # "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
    date: str         # "2026-10-26"
    count: int = 0
    is_today: bool = False
    is_future: bool = False


class RecommendedPractice(BaseModel):
    category: str
    topic: str
    difficulty: str = "Medium"
    accuracy_percentage: float = 0.0
    reason: str
    practice_route: str


class WeeklyProgressAnalysis(BaseModel):
    current_date: str
    week_start: str
    week_end: str
    total_solved_this_week: int
    today_solved: int
    today_goal: int = 20
    today_progress_pct: float
    daily_breakdown: List[WeeklyDayActivity]
    recommendation: Optional[RecommendedPractice] = None
    strong_topics: List[str] = []
    weak_topics: List[str] = []
    streak_days: int = 1


class StudentStatsResponse(BaseModel):
    student_id: str
    overall_score: float
    quiz_accuracy: float
    total_quizzes_completed: int
    total_notes_read: int
    total_coding_solved: int
    dsa_progress_percentage: float
    interview_average_score: float
    class_rank: Optional[int] = None
    questions_solved: int = 0
    code_submissions: int = 0
    total_ai_interviews: int = 0
    topic_breakdown: List[TopicProgressResponse] = []
    weekly_progress: Optional[WeeklyProgressAnalysis] = None


class FacultyStudentPerformanceItem(BaseModel):
    student_id: str
    student_name: str
    email: str
    branch: str
    academic_year: str
    section: str
    overall_score: float
    quiz_accuracy: float
    quizzes_completed: int
    notes_read: int
    coding_solved: int
    dsa_progress_pct: float
    interviews_conducted: int
    interviews_score: float
    top_mastered_topics: List[str] = []
    topic_mastery: List[dict] = []


class FacultyDashboardStatsResponse(BaseModel):
    total_students: int
    active_students: int
    notes_published: int
    quizzes_created: int
    interviews_conducted: int
    pending_evaluations: int
    average_student_score: float
