from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field


class CreateLiveInterviewBookingRequest(BaseModel):
    student_id: str = Field(..., description="ID of student to interview")
    interview_category: str = Field(
        default="Technical Interview",
        description="Technical Interview, HR Interview, Python Interview, C Interview, C++ Interview, Java Interview, DSA Interview, SQL and DBMS Interview, Engineering Subjects, Custom Interview"
    )
    subject: str = Field(..., min_length=2, max_length=150, description="Subject, programming language, or role focus")
    scheduled_at: datetime = Field(..., description="ISO-8601 scheduled start timestamp")
    duration_minutes: int = Field(default=45, ge=15, le=180, description="Planned interview duration in minutes")
    instructions: Optional[str] = Field(default=None, max_length=2000, description="Specific instructions for candidate")
    preparation_materials: Optional[str] = Field(default=None, max_length=2000, description="Optional preparation reading or syllabus")


class RescheduleLiveInterviewRequest(BaseModel):
    scheduled_at: datetime = Field(..., description="New ISO-8601 scheduled start timestamp")
    duration_minutes: Optional[int] = Field(default=None, ge=15, le=180, description="Updated duration in minutes")


class LiveInterviewBookingResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    student_id: str
    student_name: str
    student_email: str
    teacher_id: str
    teacher_name: str
    teacher_email: str
    college_id: Optional[str] = None
    interview_category: str
    subject: str
    scheduled_at: datetime
    duration_minutes: int
    instructions: Optional[str] = None
    preparation_materials: Optional[str] = None
    booking_status: str
    room_id: Optional[str] = None
    secure_room_id: Optional[str] = None
    has_feedback: bool = False
    created_at: datetime


class LiveMeetingParticipantResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: str
    name: str
    role: str
    join_time: datetime
    connection_status: str


class LiveMeetingRoomResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    room_id: str
    booking_id: str
    secure_room_id: str
    room_status: str
    student_id: str
    student_name: str
    teacher_id: str
    teacher_name: str
    interview_category: str
    subject: str
    scheduled_at: datetime
    duration_minutes: int
    current_user_role: str
    is_waiting: bool = False
    host_present: bool = False
    active_participants: List[LiveMeetingParticipantResponse] = []
    ice_servers: List[Dict[str, Any]] = []


class LiveMeetingChatMessageRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000, description="Chat text content")


class LiveMeetingChatMessageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    room_id: str
    sender_id: str
    sender_name: str
    sender_role: str
    message_content: str
    created_at: datetime


class SubmitLiveInterviewFeedbackRequest(BaseModel):
    technical_score: float = Field(..., ge=0.0, le=100.0, description="Technical knowledge score (0-100)")
    communication_feedback: str = Field(..., min_length=5, max_length=3000, description="Qualitative communication assessment")
    problem_solving_feedback: str = Field(..., min_length=5, max_length=3000, description="Problem solving & critical thinking assessment")
    strengths: List[str] = Field(default=[], description="Identified candidate strengths")
    areas_for_improvement: List[str] = Field(default=[], description="Identified growth / revision areas")
    teacher_comments: Optional[str] = Field(default=None, max_length=3000, description="General notes or observations")
    recommended_topics: List[str] = Field(default=[], description="Recommended concepts to practice")


class LiveInterviewFeedbackResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    booking_id: str
    teacher_id: str
    teacher_name: str
    technical_score: float
    communication_feedback: str
    problem_solving_feedback: str
    strengths: List[str] = []
    areas_for_improvement: List[str] = []
    teacher_comments: Optional[str] = None
    recommended_topics: List[str] = []
    submitted_at: datetime
