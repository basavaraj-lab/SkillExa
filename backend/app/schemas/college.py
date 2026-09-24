from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class CollegeResponse(BaseModel):
    id: str
    code: str
    name: str
    city: Optional[str] = None
    state: Optional[str] = None
    is_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True


class CreateCollegeRequest(BaseModel):
    code: str = Field(..., min_length=2, max_length=50)
    name: str = Field(..., min_length=2, max_length=255)
    city: Optional[str] = None
    state: Optional[str] = None


class AnnouncementResponse(BaseModel):
    id: str
    college_id: str
    faculty_id: str
    faculty_name: str
    faculty_dept: str
    title: str
    content: str
    priority: str
    is_pinned: bool
    target_departments: List[str] = []
    target_years: List[str] = []
    target_sections: List[str] = []
    created_at: datetime

    class Config:
        from_attributes = True


class CreateAnnouncementRequest(BaseModel):
    title: str = Field(..., min_length=2, max_length=255)
    content: str = Field(..., min_length=5)
    priority: Optional[str] = "NORMAL"  # 'NORMAL', 'HIGH', 'URGENT'
    is_pinned: Optional[bool] = False
    target_departments: Optional[List[str]] = None
    target_years: Optional[List[str]] = None
    target_sections: Optional[List[str]] = None
