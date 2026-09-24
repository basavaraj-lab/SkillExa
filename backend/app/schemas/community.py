from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


class CommunityFilterParams(BaseModel):
    search: Optional[str] = None
    category: Optional[str] = "all"  # 'all', 'engineering', 'competitive', 'programming', 'dsa'
    content_type: Optional[str] = "all"  # 'all', 'notes', 'pdf', 'quiz', 'video', 'coding'
    subject: Optional[str] = None
    topic: Optional[str] = None
    language: Optional[str] = None
    college_id: Optional[str] = None
    faculty_id: Optional[str] = None
    page: int = Field(1, ge=1)
    limit: int = Field(20, ge=1, le=100)


class CommunityContentItemResponse(BaseModel):
    id: str
    type: str  # 'note', 'pdf', 'quiz', 'video', 'coding'
    title: str
    subject: str
    topic: str
    subtopic: Optional[str] = None
    language: Optional[str] = None
    
    faculty_id: str
    faculty_name: str
    faculty_designation: str
    college_id: Optional[str] = None
    college_name: str
    is_verified_faculty: bool = True
    
    published_date: str
    summary: Optional[str] = None
    duration: Optional[str] = None
    questions_count: Optional[int] = None
    rating: float = 4.9
    views_count: int = 0
    
    target_params: Dict[str, Any] = {}
