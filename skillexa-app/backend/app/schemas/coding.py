from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from backend.app.models.coding import SubmissionStatusEnum
from backend.app.models.quiz import DifficultyEnum


class TestCaseItem(BaseModel):
    input: str
    expected: str
    is_hidden: bool = False


class ExampleItem(BaseModel):
    input: str
    output: str
    explanation: Optional[str] = None


class CreateCodingProblemRequest(BaseModel):
    title: str = Field(..., min_length=2, max_length=255)
    description: str = Field(..., min_length=10)
    language: str = Field(..., description="c, cpp, java, python, javascript, html_css, react_native")
    difficulty: DifficultyEnum = DifficultyEnum.MEDIUM
    topic: str = Field(..., min_length=2, max_length=100)
    subtopic: Optional[str] = None
    constraints: Optional[str] = None
    input_format: Optional[str] = None
    output_format: Optional[str] = None
    examples: List[ExampleItem] = Field(default_factory=list)
    starter_code: str
    solution_code: Optional[str] = None
    test_cases: List[TestCaseItem] = Field(default_factory=list)
    points: int = 10


class CodingProblemResponse(BaseModel):
    id: str
    title: str
    description: str
    language: str
    difficulty: DifficultyEnum
    topic: str
    subtopic: Optional[str] = None
    constraints: Optional[str] = None
    input_format: Optional[str] = None
    output_format: Optional[str] = None
    examples: List[Dict[str, Any]] = []
    starter_code: str
    points: int
    created_at: datetime

    class Config:
        from_attributes = True


class ExecuteCodeRequest(BaseModel):
    language: str = Field(..., description="'python', 'c', 'cpp', 'java', 'javascript'")
    code: str = Field(..., min_length=1)
    custom_input: Optional[str] = None


class ExecutionResultResponse(BaseModel):
    status: SubmissionStatusEnum
    stdout: str
    stderr: str
    compile_output: Optional[str] = None
    runtime_ms: float
    memory_kb: float
    error_message: Optional[str] = None


class SubmitCodeRequest(BaseModel):
    problem_id: str
    language: str
    code: str


class SubmissionResultResponse(BaseModel):
    submission_id: str
    problem_id: str
    status: SubmissionStatusEnum
    test_cases_passed: int
    total_test_cases: int
    runtime_ms: float
    memory_kb: float
    output_logs: Optional[str] = None
    error_message: Optional[str] = None
    created_at: datetime
