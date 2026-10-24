from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field


class StartAIInterviewRequest(BaseModel):
    interview_category: str = Field(default="Technical", description="Technical, HR, or Behavioral")
    job_role: str = Field(default="Software Developer", description="Target job role")
    subject: str = Field(default="Python", description="Subject or programming language")
    programming_language: Optional[str] = Field(default=None, description="Optional programming language")
    difficulty: str = Field(default="Intermediate", description="Beginner, Intermediate, or Advanced")
    experience_level: str = Field(default="Student", description="Student, Fresher, or Experienced")
    total_questions: int = Field(default=5, ge=1, le=15, description="Number of questions in session")
    interview_mode: str = Field(default="text", description="'text' or 'voice'")
    preferred_language: str = Field(default="English")
    duration_minutes: int = Field(default=30, ge=5, le=90)


class AIInterviewQuestionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    interview_id: str
    question_number: int
    total_questions: int = 5
    question_text: str
    topic: str
    difficulty: str
    hints: List[str] = []
    generated_follow_up: bool = False
    question_source: str = "predefined"
    source_reference: Optional[str] = None
    verified_dates: List[str] = []
    asked_at: datetime


class SubmitAnswerRequest(BaseModel):
    question_id: str
    answer_text: str = Field(..., min_length=2, max_length=100000, description="Candidate response text, supports comprehensive answers up to 1,000+ words")
    answer_mode: str = Field(default="text", description="'text' or 'voice'")
    speech_metrics: Optional[Dict[str, Any]] = None


class AnswerEvaluationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    answer_id: str
    question_id: str
    technical_score: float
    completeness_score: float
    clarity_score: float
    communication_score: float
    overall_score: float
    feedback: str
    strengths: List[str] = []
    improvement_areas: List[str] = []
    missing_concepts: List[str] = []
    model_answer: Optional[str] = None
    is_interview_complete: bool = False
    next_question_number: Optional[int] = None


class QuestionAnswerDetail(BaseModel):
    question_number: int
    question_text: str
    student_answer: Optional[str] = None
    technical_score: Optional[float] = None
    clarity_score: Optional[float] = None
    feedback: Optional[str] = None
    model_answer: Optional[str] = None


class AIInterviewReportResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    interview_id: str
    overall_score: float
    technical_summary: str
    communication_summary: str
    strengths: List[str] = []
    improvement_areas: List[str] = []
    recommended_topics: List[str] = []
    final_feedback: str
    generated_at: datetime
    questions_breakdown: List[QuestionAnswerDetail] = []


class AIInterviewSessionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    user_id: str
    interview_category: str
    job_role: str
    subject: str
    difficulty: str
    interview_mode: str
    status: str
    started_at: datetime
    completed_at: Optional[datetime] = None
    total_questions: int
    questions_answered: int
    total_score: float
    current_question: Optional[AIInterviewQuestionResponse] = None
    report: Optional[AIInterviewReportResponse] = None


class AIInterviewHistoryItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    interview_category: str
    job_role: str
    subject: str
    difficulty: str
    interview_mode: str
    status: str
    total_questions: int
    questions_answered: int
    total_score: float
    started_at: datetime
    completed_at: Optional[datetime] = None


class AIInterviewHistoryListResponse(BaseModel):
    total: int
    page: int
    limit: int
    items: List[AIInterviewHistoryItem]


class CreateQuestionBankRequest(BaseModel):
    category: str
    subject: str
    programming_language: Optional[str] = None
    job_role: Optional[str] = "Software Developer"
    difficulty: str = "Intermediate"
    question_text: str = Field(..., min_length=10)
    expected_concepts: List[str] = []
    evaluation_criteria: Dict[str, float] = {}
    sample_answer: Optional[str] = None
    hints: List[str] = []


class QuestionBankResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    category: str
    subject: str
    job_role: Optional[str] = None
    difficulty: str
    question_text: str
    expected_concepts: List[str] = []
    sample_answer: Optional[str] = None
    hints: List[str] = []
    question_source: str
    validation_status: str
    is_active: bool
    created_at: datetime


class TTSRequest(BaseModel):
    text: str = Field(..., min_length=2, max_length=2000)
    voice: str = Field(default="alloy")
    language: str = Field(default="en")


class TTSResponse(BaseModel):
    success: bool
    audio_url: Optional[str] = None
    format: str
    text: str
    cached: bool
    client_tts_ready: bool = True


class STTResponse(BaseModel):
    success: bool
    transcript: str
    duration_seconds: float
    words_count: int
    words_per_minute: float
    is_fallback: bool
    status: str
