from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import get_current_student
from backend.app.dependencies.db import get_db
from backend.app.models.coding import CodingProblem, CodingSubmission, SubmissionStatusEnum
from backend.app.models.notification import StudentProgress
from backend.app.models.user import StudentProfile
from backend.app.schemas.coding import (
    CodingProblemResponse,
    CreateCodingProblemRequest,
    ExecuteCodeRequest,
    ExecutionResultResponse,
    SubmissionResultResponse,
    SubmitCodeRequest,
)
from backend.app.schemas.common import ApiResponse
from backend.app.services.execution_service import SandboxedExecutionService

router = APIRouter(prefix="/coding", tags=["Coding Problems & Execution"])


@router.get("/problems", response_model=ApiResponse[List[CodingProblemResponse]])
def get_coding_problems(
    language: Optional[str] = Query(None, description="'c', 'cpp', 'java', 'python', 'javascript', 'html_css', 'react_native'"),
    topic: Optional[str] = Query(None, description="e.g. 'Arrays', 'Linked List', 'Pointers'"),
    difficulty: Optional[str] = Query(None),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    query = db.query(CodingProblem)
    if language:
        query = query.filter(CodingProblem.language.ilike(f"%{language}%"))
    if topic:
        query = query.filter(CodingProblem.topic.ilike(f"%{topic}%"))
    if difficulty:
        query = query.filter(CodingProblem.difficulty == difficulty)

    problems = query.order_by(CodingProblem.order_index, CodingProblem.created_at.desc()).limit(limit).all()
    results = [CodingProblemResponse.model_validate(p) for p in problems]
    return ApiResponse(
        success=True,
        message=f"Retrieved {len(results)} coding problems.",
        data=results,
    )


@router.get("/problems/{id}", response_model=ApiResponse[CodingProblemResponse])
def get_coding_problem_by_id(
    id: str,
    db: Session = Depends(get_db),
):
    problem = db.query(CodingProblem).filter(CodingProblem.id == id).first()
    if not problem:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coding problem not found.")
    return ApiResponse(
        success=True,
        message="Problem retrieved.",
        data=CodingProblemResponse.model_validate(problem),
    )


@router.post("/execute", response_model=ApiResponse[ExecutionResultResponse])
def execute_code_sandboxed(
    req: ExecuteCodeRequest,
):
    """
    Section 19: Execute code in isolated sandbox with CPU/Memory/Process limits and automatic scratch cleanup.
    """
    result = SandboxedExecutionService.execute_code(
        language=req.language,
        code=req.code,
        custom_input=req.custom_input,
    )
    return ApiResponse(
        success=True,
        message="Code execution completed.",
        data=result,
    )


@router.post("/submit", response_model=ApiResponse[SubmissionResultResponse])
def submit_problem_code(
    req: SubmitCodeRequest,
    student: StudentProfile = Depends(get_current_student),
    db: Session = Depends(get_db),
):
    problem = db.query(CodingProblem).filter(CodingProblem.id == req.problem_id).first()
    if not problem:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Problem not found.")

    status_res, passed, total, logs = SandboxedExecutionService.run_test_cases(
        language=req.language,
        code=req.code,
        test_cases=problem.test_cases or [],
    )

    submission = CodingSubmission(
        student_id=student.id,
        problem_id=problem.id,
        language=req.language,
        code=req.code,
        status=status_res,
        test_cases_passed=passed,
        total_test_cases=total,
        runtime_ms=12.5,
        memory_kb=4096.0,
        output_logs=logs,
    )
    db.add(submission)

    # If passed, record progress
    if status_res == SubmissionStatusEnum.PASSED:
        progress = (
            db.query(StudentProgress)
            .filter(
                StudentProgress.student_id == student.id,
                StudentProgress.topic == problem.topic,
            )
            .first()
        )
        if progress:
            progress.coding_solved += 1
            progress.mastery_percentage = min(100.0, progress.mastery_percentage + 15.0)

    db.commit()
    db.refresh(submission)

    return ApiResponse(
        success=True,
        message=f"Submission evaluated: {status_res.value} ({passed}/{total} test cases passed).",
        data=SubmissionResultResponse(
            submission_id=submission.id,
            problem_id=problem.id,
            status=status_res,
            test_cases_passed=passed,
            total_test_cases=total,
            runtime_ms=submission.runtime_ms or 0.0,
            memory_kb=submission.memory_kb or 0.0,
            output_logs=logs,
            error_message=None,
            created_at=submission.created_at,
        ),
    )
