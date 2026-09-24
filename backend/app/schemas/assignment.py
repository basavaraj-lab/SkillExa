from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class CreateAssignmentRequest(BaseModel):
    title: str = Field(..., min_length=2, max_length=255)
    description: str = Field(..., min_length=5)
    subject: str = Field(..., min_length=2, max_length=100)
    topic: str = Field(..., min_length=2, max_length=100)
    max_marks: float = Field(default=100.0, ge=1.0)
    due_date: datetime
    published: bool = True
    target_departments: Optional[List[str]] = None
    target_years: Optional[List[str]] = None
    target_sections: Optional[List[str]] = None


class SubmitAssignmentRequest(BaseModel):
    submission_text: Optional[str] = None
    file_path: Optional[str] = None


class EvaluateAssignmentRequest(BaseModel):
    score: float = Field(..., ge=0.0)
    feedback: str = Field(..., min_length=2)


class AssignmentSubmissionResponse(BaseModel):
    id: str
    assignment_id: str
    student_id: str
    student_name: Optional[str] = None
    submission_text: Optional[str] = None
    file_path: Optional[str] = None
    status: str
    score: Optional[float] = None
    feedback: Optional[str] = None
    submitted_at: datetime
    evaluated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class AssignmentResponse(BaseModel):
    id: str
    faculty_id: str
    faculty_name: Optional[str] = None
    college_id: Optional[str] = None
    title: str
    description: str
    subject: str
    topic: str
    max_marks: float
    due_date: datetime
    published: bool
    submissions_count: int = 0
    created_at: datetime

    class Config:
        from_attributes = True
