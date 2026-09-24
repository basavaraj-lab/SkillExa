from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from backend.app.models.interview import InterviewStatusEnum, InterviewTypeEnum


class CreateInterviewQuestionRequest(BaseModel):
    question_text: str = Field(..., min_length=3)
    category: Optional[str] = "Technical"
    marks: float = 10.0
    order_index: int = 0


class CreateInterviewRequest(BaseModel):
    student_id: str
    title: str = Field(..., min_length=2, max_length=255)
    interview_type: InterviewTypeEnum = InterviewTypeEnum.TECHNICAL
    subject_or_role: str = Field(..., min_length=2, max_length=100)
    difficulty: Optional[str] = "Medium"
    scheduled_at: datetime
    duration_minutes: int = 30
    questions: Optional[List[CreateInterviewQuestionRequest]] = Field(default_factory=list)


class InterviewQuestionResponse(BaseModel):
    id: str
    question_text: str
    category: str
    marks: float
    order_index: int

    class Config:
        from_attributes = True


class InterviewEvaluationRequest(BaseModel):
    technical_score: float = Field(..., ge=0.0, le=100.0)
    communication_score: float = Field(..., ge=0.0, le=100.0)
    confidence_score: float = Field(..., ge=0.0, le=100.0)
    problem_solving_score: float = Field(..., ge=0.0, le=100.0)
    strengths: List[str] = Field(default_factory=list)
    weaknesses: List[str] = Field(default_factory=list)
    suggestions: List[str] = Field(default_factory=list)
    overall_feedback: str = Field(..., min_length=5)


class InterviewResultResponse(BaseModel):
    id: str
    interview_id: str
    technical_score: float
    communication_score: float
    confidence_score: float
    problem_solving_score: float
    overall_score: float
    strengths: List[str] = []
    weaknesses: List[str] = []
    suggestions: List[str] = []
    overall_feedback: str
    evaluated_at: datetime

    class Config:
        from_attributes = True


class VideoSessionResponse(BaseModel):
    room_id: str
    interview_id: str
    faculty_id: str
    student_id: str
    session_status: str
    faculty_joined: bool
    student_joined: bool
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None


class WebRTCSignalingMessage(BaseModel):
    room_id: str
    sender_id: str
    type: str  # 'offer', 'answer', 'candidate', 'join', 'leave'
    payload: Dict[str, Any] = Field(default_factory=dict)


class InterviewResponse(BaseModel):
    id: str
    faculty_id: str
    faculty_name: Optional[str] = None
    student_id: str
    student_name: Optional[str] = None
    college_id: Optional[str] = None
    title: str
    interview_type: InterviewTypeEnum
    subject_or_role: str
    difficulty: str
    scheduled_at: datetime
    duration_minutes: int
    status: InterviewStatusEnum
    questions: List[InterviewQuestionResponse] = []
    result: Optional[InterviewResultResponse] = None
    room_id: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
