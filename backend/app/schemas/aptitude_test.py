from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class AptitudeQuestionOption(BaseModel):
    id: str = Field(..., description="Option identifier e.g. 'A', 'B', 'C', 'D'")
    text: str = Field(..., description="Option textual answer")


class AptitudeQuestionPublic(BaseModel):
    """Public question representation sent to candidate while test is active (Answers strictly hidden)."""
    id: str
    order_index: int
    question_text: str
    options: List[AptitudeQuestionOption]
    category: str
    topic: str
    difficulty: str
    marks: float = 1.0
    negative_marks: float = 0.25


class AptitudeQuestionGraded(BaseModel):
    """Detailed question representation with score, correct answer, and explanation (Shown after submit)."""
    id: str
    order_index: int
    question_text: str
    options: List[AptitudeQuestionOption]
    selected_option: Optional[str] = None
    correct_answer: str
    is_correct: bool
    marks_awarded: float
    explanation: str
    category: str
    topic: str
    difficulty: str


class CreateAptitudeTestRequest(BaseModel):
    category: str = Field("Quantitative Aptitude", description="Aptitude category")
    topic: str = Field("Mixed Topics", description="Specific topic or 'Mixed Topics'")
    difficulty: str = Field("Intermediate", description="'Easy', 'Intermediate', or 'Advanced'")
    question_count: int = Field(10, ge=5, le=50, description="Requested number of questions")
    test_mode: str = Field("quick", description="'quick' (10), 'standard' (20), 'full' (30), or 'custom'")
    duration_minutes: Optional[int] = Field(None, ge=1, le=180, description="Optional custom test duration")


class SaveAptitudeResponseRequest(BaseModel):
    question_id: str
    selected_option: Optional[str] = None  # 'A', 'B', 'C', 'D', or None
    time_spent_seconds: Optional[int] = 0


class SubmitAptitudeTestRequest(BaseModel):
    responses: Optional[Dict[str, Optional[str]]] = None  # question_id -> 'A' | 'B' | 'C' | 'D'
    time_spent_seconds: Optional[int] = 0


class AptitudeTestActiveResponse(BaseModel):
    """Response returned when an aptitude test is active (in-progress)."""
    attempt_id: str
    category: str
    topic: str
    difficulty: str
    test_mode: str
    question_count: int
    duration_minutes: int
    status: str
    started_at: datetime
    time_remaining_seconds: int
    total_marks: float
    negative_marks_per_question: float
    questions: List[AptitudeQuestionPublic]
    saved_responses: Dict[str, Optional[str]]
    llm_provider: Optional[str] = None


class AptitudeTestResultResponse(BaseModel):
    """Full performance report returned upon test submission or review."""
    attempt_id: str
    category: str
    topic: str
    difficulty: str
    question_count: int
    total_marks: float
    marks_obtained: float
    total_negative_marks: float
    final_score: float
    accuracy_percentage: float
    correct_count: int
    incorrect_count: int
    unattempted_count: int
    time_spent_seconds: int
    started_at: datetime
    submitted_at: Optional[datetime] = None
    questions: List[AptitudeQuestionGraded]
    topic_breakdown: Dict[str, Any]
    llm_provider: Optional[str] = None


class AptitudeTestHistoryItem(BaseModel):
    attempt_id: str
    category: str
    topic: str
    difficulty: str
    question_count: int
    final_score: float
    total_marks: float
    accuracy_percentage: float
    correct_count: int
    incorrect_count: int
    unattempted_count: int
    time_spent_seconds: int
    submitted_at: Optional[datetime] = None
    status: str


class AptitudeCategoriesResponse(BaseModel):
    categories: Dict[str, List[str]]
    difficulties: List[str]
    test_modes: List[Dict[str, Any]]
