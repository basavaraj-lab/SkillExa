"""Pydantic schemas for API request and response bodies."""
from pydantic import BaseModel
from typing import Any, Dict, List, Optional


class SectionProgressSchema(BaseModel):
    information_completed: bool
    examples_completed: bool
    programming_completed: bool
    fill_blanks_completed: bool
    test_completed: bool
    test_score: float
    topic_completed: bool
    current_section: str
    status: str


class ProgressResponse(BaseModel):
    success: bool
    student_id: str
    topic_id: int
    progress: SectionProgressSchema


class SectionContentResponse(BaseModel):
    success: bool
    topic_id: int
    section: str
    title: str
    data: Dict[str, Any]
    progress: SectionProgressSchema
