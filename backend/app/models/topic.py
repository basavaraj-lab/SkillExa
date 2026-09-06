"""Data classes and models for topic structures."""
from pydantic import BaseModel
from typing import Any, List, Optional


class TopicMeta(BaseModel):
    id: int
    title: str
    difficulty: str
    duration: str


class FillBlanksQuestion(BaseModel):
    question: str
    answers: Optional[List[str]] = None
    answer: Optional[str] = None


class SkillExaTestQuestion(BaseModel):
    question: str
    options: List[str]
    answer: str


class CodeExecutionPayload(BaseModel):
    code: str


class FillBlanksSubmissionPayload(BaseModel):
    answers: List[str]


class TestSubmissionPayload(BaseModel):
    answers: dict[str, str]  # mapping question index/question string -> selected option
