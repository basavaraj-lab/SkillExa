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
    topic_breakdown: List[TopicProgressResponse] = []


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


class FacultyDashboardStatsResponse(BaseModel):
    total_students: int
    active_students: int
    notes_published: int
    quizzes_created: int
    interviews_conducted: int
    pending_evaluations: int
    average_student_score: float
