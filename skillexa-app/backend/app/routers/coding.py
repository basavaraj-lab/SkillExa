from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import or_

from backend.app.dependencies.auth import get_current_student, get_optional_student
from backend.app.dependencies.db import get_db
from backend.app.models.coding import CodingProblem, CodingSubmission, SubmissionStatusEnum
from backend.app.models.user import StudentProfile
from backend.app.schemas.coding import (
    CodingProblemResponse,
    CreateCodingProblemRequest,
    DsaCategoryProgress,
    DsaProgressResponse,
    ExecuteCodeRequest,
    ExecutionResultResponse,
    SubmissionResultResponse,
    SubmitCodeRequest,
)
from backend.app.schemas.common import ApiResponse
from backend.app.services.execution_service import SandboxedExecutionService

router = APIRouter(prefix="/coding", tags=["Coding Problems & Execution"])

DSA_CATEGORIES = [
    "Arrays",
    "Strings",
    "Searching",
    "Sorting",
    "Linked List",
    "Stack",
    "Queue",
    "Recursion",
    "Hashing",
    "Trees",
    "Graphs",
    "Dynamic Programming",
]


@router.get("/problems", response_model=ApiResponse[List[CodingProblemResponse]])
def get_coding_problems(
    search: Optional[str] = Query(None, description="Search problem title or description"),
    category: Optional[str] = Query(None, description="Category filter e.g. Arrays, Strings"),
    difficulty: Optional[str] = Query(None, description="Basic, Easy, Medium, Hard"),
    language: Optional[str] = Query(None, description="'c', 'cpp', 'java', 'python'"),
    solved_status: Optional[str] = Query(None, description="'all', 'solved', 'unsolved'"),
    limit: int = Query(150, ge=1, le=300),
    db: Session = Depends(get_db),
    student: Optional[StudentProfile] = Depends(get_optional_student),
):
    query = db.query(CodingProblem)

    if search:
        query = query.filter(
            or_(
                CodingProblem.title.ilike(f"%{search}%"),
                CodingProblem.description.ilike(f"%{search}%"),
            )
        )
    if category and category.lower() != "all":
        query = query.filter(
            or_(
                CodingProblem.category.ilike(f"%{category}%"),
                CodingProblem.topic.ilike(f"%{category}%"),
            )
        )
    if difficulty and difficulty.lower() != "all":
        query = query.filter(CodingProblem.difficulty == difficulty.lower())

    if language and language.lower() != "all":
        query = query.filter(
            or_(
                CodingProblem.language.ilike(f"%{language}%"),
                CodingProblem.starter_code_map.has_key(language.lower()) if hasattr(CodingProblem.starter_code_map, "has_key") else True,
            )
        )

    problems = query.order_by(CodingProblem.problem_num, CodingProblem.created_at.desc()).limit(limit).all()

    solved_problem_ids = set()
    if student:
        passed_subs = (
            db.query(CodingSubmission.problem_id)
            .filter(
                CodingSubmission.student_id == student.id,
                CodingSubmission.status == SubmissionStatusEnum.PASSED,
            )
            .distinct()
            .all()
        )
        solved_problem_ids = {s[0] for s in passed_subs}

    results = []
    for p in problems:
        is_solved = p.id in solved_problem_ids
        if solved_status == "solved" and not is_solved:
            continue
        if solved_status == "unsolved" and is_solved:
            continue

        resp = CodingProblemResponse(
            id=p.id,
            problem_num=getattr(p, "problem_num", 1) or 1,
            title=p.title,
            description=p.description,
            language=p.language or "python",
            difficulty=p.difficulty,
            topic=getattr(p, "category", p.topic) or "Arrays",
            subtopic=p.subtopic,
            constraints=p.constraints,
            input_format=p.input_format,
            output_format=p.output_format,
            time_complexity=getattr(p, "time_complexity", "O(n)"),
            space_complexity=getattr(p, "space_complexity", "O(1)"),
            company_tags=getattr(p, "company_tags", []) or [],
            examples=p.examples or [],
            starter_code=p.starter_code,
            starter_code_map=getattr(p, "starter_code_map", {}) or {},
            test_cases=p.test_cases or [],
            points=p.points or 10,
            created_at=p.created_at,
            is_solved=is_solved,
        )
        results.append(resp)

    return ApiResponse(
        success=True,
        message=f"Retrieved {len(results)} DSA coding problems.",
        data=results,
    )


@router.get("/problems/{id}", response_model=ApiResponse[CodingProblemResponse])
def get_coding_problem_by_id(
    id: str,
    db: Session = Depends(get_db),
    student: Optional[StudentProfile] = Depends(get_optional_student),
):
    problem = db.query(CodingProblem).filter(CodingProblem.id == id).first()
    if not problem:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coding problem not found.")

    is_solved = False
    if student:
        passed = (
            db.query(CodingSubmission)
            .filter(
                CodingSubmission.student_id == student.id,
                CodingSubmission.problem_id == problem.id,
                CodingSubmission.status == SubmissionStatusEnum.PASSED,
            )
            .first()
        )
        if passed:
            is_solved = True

    resp = CodingProblemResponse(
        id=problem.id,
        problem_num=getattr(problem, "problem_num", 1) or 1,
        title=problem.title,
        description=problem.description,
        language=problem.language or "python",
        difficulty=problem.difficulty,
        topic=getattr(problem, "category", problem.topic) or "Arrays",
        subtopic=problem.subtopic,
        constraints=problem.constraints,
        input_format=problem.input_format,
        output_format=problem.output_format,
        time_complexity=getattr(problem, "time_complexity", "O(n)"),
        space_complexity=getattr(problem, "space_complexity", "O(1)"),
        company_tags=getattr(problem, "company_tags", []) or [],
        examples=problem.examples or [],
        starter_code=problem.starter_code,
        starter_code_map=getattr(problem, "starter_code_map", {}) or {},
        test_cases=problem.test_cases or [],
        points=problem.points or 10,
        created_at=problem.created_at,
        is_solved=is_solved,
    )

    return ApiResponse(
        success=True,
        message="Problem retrieved successfully.",
        data=resp,
    )


@router.post("/execute", response_model=ApiResponse[ExecutionResultResponse])
def execute_code_sandboxed(
    req: ExecuteCodeRequest,
):
    """Compile and Run code against custom input or visible test cases in isolated sandbox."""
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
    """Submit solution code to evaluate against all visible and hidden test cases."""
    problem = db.query(CodingProblem).filter(CodingProblem.id == req.problem_id).first()
    if not problem:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Problem not found.")

    all_test_cases = (problem.test_cases or []) + (getattr(problem, "hidden_test_cases", []) or [])
    if not all_test_cases:
        all_test_cases = [{"input": "", "expected": "", "is_hidden": False}]

    status_res, passed, total, logs = SandboxedExecutionService.run_test_cases(
        language=req.language,
        code=req.code,
        test_cases=all_test_cases,
    )

    submission = CodingSubmission(
        student_id=student.id,
        problem_id=problem.id,
        language=req.language,
        code=req.code,
        status=status_res,
        test_cases_passed=passed,
        total_test_cases=total,
        runtime_ms=15.0,
        memory_kb=4096.0,
        output_logs=logs,
    )
    db.add(submission)
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
            error_message=None if status_res == SubmissionStatusEnum.PASSED else logs,
            created_at=submission.created_at,
        ),
    )


@router.get("/progress", response_model=ApiResponse[DsaProgressResponse])
def get_dsa_progress(
    student: StudentProfile = Depends(get_current_student),
    db: Session = Depends(get_db),
):
    """Get overall DSA progress metrics, category breakdowns, and user streak."""
    total_probs = db.query(CodingProblem).count()
    if total_probs == 0:
        total_probs = 1

    passed_subs = (
        db.query(CodingSubmission.problem_id)
        .filter(
            CodingSubmission.student_id == student.id,
            CodingSubmission.status == SubmissionStatusEnum.PASSED,
        )
        .distinct()
        .all()
    )
    solved_ids = {s[0] for s in passed_subs}
    solved_count = len(solved_ids)
    unsolved_count = max(0, total_probs - solved_count)
    progress_pct = round((solved_count / total_probs) * 100.0, 1)

    cat_progress = []
    for cat in DSA_CATEGORIES:
        cat_total = db.query(CodingProblem).filter(
            or_(CodingProblem.category.ilike(f"%{cat}%"), CodingProblem.topic.ilike(f"%{cat}%"))
        ).count()
        if cat_total == 0:
            continue
        cat_solved = (
            db.query(CodingSubmission.problem_id)
            .join(CodingProblem, CodingSubmission.problem_id == CodingProblem.id)
            .filter(
                CodingSubmission.student_id == student.id,
                CodingSubmission.status == SubmissionStatusEnum.PASSED,
                or_(CodingProblem.category.ilike(f"%{cat}%"), CodingProblem.topic.ilike(f"%{cat}%")),
            )
            .distinct()
            .count()
        )
        cat_progress.append(DsaCategoryProgress(category=cat, solved=cat_solved, total=cat_total))

    data = DsaProgressResponse(
        total_problems=total_probs,
        solved_problems=solved_count,
        unsolved_problems=unsolved_count,
        progress_percentage=progress_pct,
        streak=min(14, solved_count + 1),
        categories=cat_progress,
    )

    return ApiResponse(
        success=True,
        message="DSA Progress retrieved.",
        data=data,
    )
