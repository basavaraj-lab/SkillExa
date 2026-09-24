from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from backend.app.models.note import VisibilityEnum
from backend.app.models.quiz import DifficultyEnum


class CreateQuestionRequest(BaseModel):
    section: Optional[str] = "engineering"
    subject: str = Field(..., min_length=2, max_length=100)
    topic: str = Field(..., min_length=2, max_length=100)
    subtopic: Optional[str] = None
    language: Optional[str] = None
    
    difficulty: DifficultyEnum = DifficultyEnum.MEDIUM
    question_type: str = "mcq"
    question_text: str = Field(..., min_length=5)
    options: List[str] = Field(..., min_length=2)  # List of string options
    correct_answer: int = Field(..., ge=0, description="0-indexed integer corresponding to options")
    explanation: Optional[str] = None
    marks: float = 2.0
    negative_marks: float = 0.5
    order_index: int = 0


class QuestionForStudentResponse(BaseModel):
    id: str
    quiz_id: Optional[str] = None
    section: str
    subject: str
    topic: str
    subtopic: Optional[str] = None
    language: Optional[str] = None
    difficulty: DifficultyEnum
    question_type: str
    question_text: str
    options: List[str]
    marks: float
    order_index: int

    class Config:
        from_attributes = True


class QuestionForFacultyResponse(BaseModel):
    id: str
    quiz_id: Optional[str] = None
    section: str
    subject: str
    topic: str
    subtopic: Optional[str] = None
    language: Optional[str] = None
    difficulty: DifficultyEnum
    question_type: str
    question_text: str
    options: List[str]
    correct_answer: int
    explanation: Optional[str] = None
    marks: float
    negative_marks: float
    order_index: int

    class Config:
        from_attributes = True


class CreateQuizRequest(BaseModel):
    title: str = Field(..., min_length=2, max_length=255)
    description: Optional[str] = None
    
    section: str = Field(default="engineering")
    subject: str = Field(..., min_length=2, max_length=100)
    topic: str = Field(..., min_length=2, max_length=100)
    subtopic: Optional[str] = None
    language: Optional[str] = None
    
    difficulty: DifficultyEnum = DifficultyEnum.MEDIUM
    duration_minutes: int = Field(default=15, ge=1)
    total_marks: float = Field(default=20.0, ge=1.0)
    negative_marks: float = Field(default=0.25, ge=0.0)
    
    visibility: VisibilityEnum = VisibilityEnum.COLLEGE
    published: bool = True
    
    target_departments: Optional[List[str]] = None
    target_years: Optional[List[str]] = None
    target_sections: Optional[List[str]] = None
    target_student_ids: Optional[List[str]] = None
    
    questions: Optional[List[CreateQuestionRequest]] = Field(default_factory=list)


class QuizResponse(BaseModel):
    id: str
    faculty_id: str
    faculty_name: Optional[str] = None
    faculty_designation: Optional[str] = None
    college_id: Optional[str] = None
    college_name: Optional[str] = None
    is_verified_faculty: Optional[bool] = None

    title: str
    description: Optional[str] = None
    section: str
    subject: str
    topic: str
    subtopic: Optional[str] = None
    language: Optional[str] = None
    
    difficulty: DifficultyEnum
    duration_minutes: int
    total_marks: float
    negative_marks: float
    questions_count: int = 0
    
    visibility: VisibilityEnum
    published: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class QuizDetailForStudentResponse(QuizResponse):
    questions: List[QuestionForStudentResponse] = []


class QuizDetailForFacultyResponse(QuizResponse):
    questions: List[QuestionForFacultyResponse] = []


class StartQuizAttemptResponse(BaseModel):
    attempt_id: str
    quiz_id: str
    title: str
    duration_minutes: int
    total_questions: int
    started_at: datetime
    questions: List[QuestionForStudentResponse]


class SubmitQuizRequest(BaseModel):
    attempt_id: str
    time_taken_seconds: int = Field(..., ge=0)
    answers: Dict[str, Optional[int]] = Field(
        ..., description="Dict mapping question_id to selected option index (or null if skipped)"
    )


class AnswerResultItem(BaseModel):
    question_id: str
    question_text: str
    options: List[str]
    selected_option: Optional[int] = None
    correct_option: int
    is_correct: bool
    explanation: Optional[str] = None
    marks_awarded: float


class QuizAttemptResultResponse(BaseModel):
    attempt_id: str
    quiz_id: str
    quiz_title: str
    score: float
    total_marks: float
    accuracy_percentage: float
    correct_count: int
    wrong_count: int
    unanswered_count: int
    time_taken_seconds: int
    submitted_at: datetime
    breakdown: List[AnswerResultItem] = []
