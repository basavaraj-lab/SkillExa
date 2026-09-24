from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from backend.app.models.note import VisibilityEnum


class CreateVideoRequest(BaseModel):
    title: str = Field(..., min_length=2, max_length=255)
    description: Optional[str] = None
    video_url: str = Field(..., min_length=5, max_length=500)
    thumbnail_url: Optional[str] = None
    duration: Optional[str] = "20 mins"

    section: str = Field(default="engineering")
    subject: str = Field(..., min_length=2, max_length=100)
    topic: str = Field(..., min_length=2, max_length=100)
    subtopic: Optional[str] = None
    language: Optional[str] = None

    visibility: VisibilityEnum = VisibilityEnum.COLLEGE
    published: bool = True

    target_departments: Optional[List[str]] = None
    target_years: Optional[List[str]] = None
    target_sections: Optional[List[str]] = None
    target_student_ids: Optional[List[str]] = None


class UpdateVideoRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    video_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    duration: Optional[str] = None
    subject: Optional[str] = None
    topic: Optional[str] = None
    subtopic: Optional[str] = None
    visibility: Optional[VisibilityEnum] = None
    published: Optional[bool] = None


class VideoResponse(BaseModel):
    id: str
    faculty_id: str
    faculty_name: Optional[str] = None
    faculty_designation: Optional[str] = None
    college_id: Optional[str] = None
    college_name: Optional[str] = None
    is_verified_faculty: Optional[bool] = None

    title: str
    description: Optional[str] = None
    video_url: str
    thumbnail_url: Optional[str] = None
    duration: str

    section: str
    subject: str
    topic: str
    subtopic: Optional[str] = None
    language: Optional[str] = None

    visibility: VisibilityEnum
    published: bool
    views_count: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
