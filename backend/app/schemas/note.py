from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from backend.app.models.note import VisibilityEnum


class CreateNoteRequest(BaseModel):
    title: str = Field(..., min_length=2, max_length=255)
    description: Optional[str] = None
    content: str = Field(..., min_length=10, description="Detailed theory & explanation")
    
    section: str = Field(default="engineering")  # 'engineering' | 'competitive' | 'programming' | 'dsa'
    subject: str = Field(..., min_length=2, max_length=100)
    topic: str = Field(..., min_length=2, max_length=100)
    subtopic: Optional[str] = None
    language: Optional[str] = None
    
    important_concepts: Optional[List[str]] = Field(default_factory=list)
    quick_revision: Optional[str] = None
    
    visibility: VisibilityEnum = VisibilityEnum.COLLEGE
    published: bool = True
    
    target_departments: Optional[List[str]] = None
    target_years: Optional[List[str]] = None
    target_sections: Optional[List[str]] = None
    target_student_ids: Optional[List[str]] = None


class UpdateNoteRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None
    subject: Optional[str] = None
    topic: Optional[str] = None
    subtopic: Optional[str] = None
    language: Optional[str] = None
    important_concepts: Optional[List[str]] = None
    quick_revision: Optional[str] = None
    visibility: Optional[VisibilityEnum] = None
    published: Optional[bool] = None
    target_departments: Optional[List[str]] = None
    target_years: Optional[List[str]] = None
    target_sections: Optional[List[str]] = None


class NoteResponse(BaseModel):
    id: str
    faculty_id: str
    faculty_name: Optional[str] = None
    faculty_designation: Optional[str] = None
    college_id: Optional[str] = None
    college_name: Optional[str] = None
    is_verified_faculty: Optional[bool] = None
    
    title: str
    description: Optional[str] = None
    content: str
    section: str
    subject: str
    topic: str
    subtopic: Optional[str] = None
    language: Optional[str] = None
    
    important_concepts: List[str] = []
    quick_revision: Optional[str] = None
    
    visibility: VisibilityEnum
    published: bool
    views_count: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PDFNoteResponse(BaseModel):
    id: str
    note_id: Optional[str] = None
    faculty_id: str
    faculty_name: Optional[str] = None
    college_id: Optional[str] = None
    college_name: Optional[str] = None
    
    title: str
    subject: str
    topic: str
    subtopic: Optional[str] = None
    
    file_name: str
    file_size_bytes: int
    mime_type: str
    version: int
    download_url: str
    
    visibility: VisibilityEnum
    published: bool
    downloads_count: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
