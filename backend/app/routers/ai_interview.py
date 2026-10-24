import os
from typing import List, Optional
from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    Query,
    UploadFile,
    status,
)
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import get_current_user, get_current_user_optional, require_role
from backend.app.dependencies.db import get_db
from backend.app.models.ai_interview import (
    AIInterviewAnswer,
    AIInterviewQuestion,
    AIInterviewReport,
    AIInterviewSession,
    AIQuestionBank,
    QuestionValidationStatusEnum,
    SessionStatusEnum,
)
from backend.app.models.user import RoleEnum, User
from backend.app.schemas.ai_interview import (
    AIInterviewHistoryItem,
    AIInterviewHistoryListResponse,
    AIInterviewQuestionResponse,
    AIInterviewReportResponse,
    AIInterviewSessionResponse,
    AnswerEvaluationResponse,
    CreateQuestionBankRequest,
    QuestionAnswerDetail,
    QuestionBankResponse,
    StartAIInterviewRequest,
    STTResponse,
    SubmitAnswerRequest,
    TTSRequest,
    TTSResponse,
)
from backend.app.schemas.common import ApiResponse
from backend.app.services.ai_interview_service import AIInterviewService
from backend.app.services.speech_service import SpeechService, TTS_CACHE_DIR

router = APIRouter(prefix="/ai-interview", tags=["AI Mock Interview"])


# -------------------------------------------------------------
# 1. STATIC INTERVIEW ROUTES (Declared before parameterized paths)
# -------------------------------------------------------------
@router.post("/start", response_model=ApiResponse[AIInterviewSessionResponse], status_code=status.HTTP_201_CREATED)
def start_ai_interview(
    req: StartAIInterviewRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Start a new AI Mock Interview session and prepare the first question.
    """
    session = AIInterviewService.start_session(db=db, user=current_user, req=req)

    q1 = session.questions[0] if session.questions else None
    q_resp = None
    if q1:
        q_resp = AIInterviewQuestionResponse(
            id=q1.id,
            interview_id=session.id,
            question_number=q1.question_number,
            total_questions=session.total_questions,
            question_text=q1.question_text,
            topic=q1.topic,
            difficulty=q1.difficulty,
            hints=[],
            generated_follow_up=q1.generated_follow_up,
            question_source=q1.question_source,
            source_reference=q1.source_reference,
            asked_at=q1.asked_at,
        )

    session_resp = AIInterviewSessionResponse(
        id=session.id,
        user_id=session.user_id,
        interview_category=session.interview_category.value if hasattr(session.interview_category, "value") else str(session.interview_category),
        job_role=session.job_role,
        subject=session.subject,
        difficulty=session.difficulty.value if hasattr(session.difficulty, "value") else str(session.difficulty),
        interview_mode=session.interview_mode.value if hasattr(session.interview_mode, "value") else str(session.interview_mode),
        status=session.status.value if hasattr(session.status, "value") else str(session.status),
        started_at=session.started_at,
        completed_at=session.completed_at,
        total_questions=session.total_questions,
        questions_answered=session.questions_answered,
        total_score=session.total_score,
        current_question=q_resp,
        report=None,
    )

    return ApiResponse(
        success=True,
        message="AI Mock Interview session started successfully.",
        data=session_resp,
    )


@router.get("/history", response_model=ApiResponse[AIInterviewHistoryListResponse])
def get_student_interview_history(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Retrieve authenticated student's paginated interview history.
    """
    history_data = AIInterviewService.get_student_history(db, current_user, page, limit)
    items = []
    for s in history_data["items"]:
        items.append(
            AIInterviewHistoryItem(
                id=s.id,
                interview_category=s.interview_category.value if hasattr(s.interview_category, "value") else str(s.interview_category),
                job_role=s.job_role,
                subject=s.subject,
                difficulty=s.difficulty.value if hasattr(s.difficulty, "value") else str(s.difficulty),
                interview_mode=s.interview_mode.value if hasattr(s.interview_mode, "value") else str(s.interview_mode),
                status=s.status.value if hasattr(s.status, "value") else str(s.status),
                total_questions=s.total_questions,
                questions_answered=s.questions_answered,
                total_score=s.total_score,
                started_at=s.started_at,
                completed_at=s.completed_at,
            )
        )

    return ApiResponse(
        success=True,
        data=AIInterviewHistoryListResponse(
            total=history_data["total"],
            page=page,
            limit=limit,
            items=items,
        ),
    )


# -------------------------------------------------------------
# 2. QUESTION BANK ROUTES
# -------------------------------------------------------------
@router.get("/questions", response_model=ApiResponse[List[QuestionBankResponse]])
def get_question_bank(
    category: Optional[str] = None,
    subject: Optional[str] = None,
    difficulty: Optional[str] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Search and filter reusable verified questions from the question bank.
    """
    from backend.app.services.question_generation_service import QuestionGenerationService
    QuestionGenerationService.seed_question_bank_if_empty(db)

    query = db.query(AIQuestionBank).filter(
        AIQuestionBank.is_active == True,
        AIQuestionBank.validation_status == QuestionValidationStatusEnum.VERIFIED,
    )
    if category:
        query = query.filter(AIQuestionBank.category == category)
    if subject:
        query = query.filter(AIQuestionBank.subject.ilike(f"%{subject}%"))
    if difficulty:
        query = query.filter(AIQuestionBank.difficulty == difficulty)

    items = query.limit(50).all()
    resp_items = [
        QuestionBankResponse(
            id=item.id,
            category=item.category.value if hasattr(item.category, "value") else str(item.category),
            subject=item.subject,
            job_role=item.job_role,
            difficulty=item.difficulty.value if hasattr(item.difficulty, "value") else str(item.difficulty),
            question_text=item.question_text,
            expected_concepts=item.expected_concepts or [],
            sample_answer=item.sample_answer,
            hints=item.hints or [],
            question_source=item.question_source,
            validation_status=item.validation_status.value if hasattr(item.validation_status, "value") else str(item.validation_status),
            is_active=item.is_active,
            created_at=item.created_at,
        )
        for item in items
    ]
    return ApiResponse(success=True, data=resp_items)


@router.post("/questions", response_model=ApiResponse[QuestionBankResponse], status_code=status.HTTP_201_CREATED)
def add_question_to_bank(
    req: CreateQuestionBankRequest,
    current_user: User = Depends(require_role([RoleEnum.FACULTY, RoleEnum.COLLEGE_ADMIN])),
    db: Session = Depends(get_db),
):
    """
    Administrative / Faculty workflow for adding verified questions to the reusable question bank.
    """
    new_q = AIQuestionBank(
        category=req.category,
        subject=req.subject,
        programming_language=req.programming_language,
        job_role=req.job_role,
        difficulty=req.difficulty,
        question_text=req.question_text,
        expected_concepts=req.expected_concepts,
        evaluation_criteria=req.evaluation_criteria or {"correctness": 5.0, "clarity": 5.0},
        sample_answer=req.sample_answer,
        hints=req.hints,
        question_source="faculty_curated",
        created_by=current_user.id,
        validation_status=QuestionValidationStatusEnum.VERIFIED,
        is_active=True,
    )
    db.add(new_q)
    db.commit()
    db.refresh(new_q)

    return ApiResponse(
        success=True,
        message="Question added to Question Bank successfully.",
        data=QuestionBankResponse(
            id=new_q.id,
            category=new_q.category.value if hasattr(new_q.category, "value") else str(new_q.category),
            subject=new_q.subject,
            job_role=new_q.job_role,
            difficulty=new_q.difficulty.value if hasattr(new_q.difficulty, "value") else str(new_q.difficulty),
            question_text=new_q.question_text,
            expected_concepts=new_q.expected_concepts,
            sample_answer=new_q.sample_answer,
            hints=new_q.hints,
            question_source=new_q.question_source,
            validation_status=new_q.validation_status.value if hasattr(new_q.validation_status, "value") else str(new_q.validation_status),
            is_active=new_q.is_active,
            created_at=new_q.created_at,
        ),
    )


@router.get("/questions/{question_id}", response_model=ApiResponse[QuestionBankResponse])
def get_question_by_id(
    question_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Retrieve specific question bank item."""
    q = db.query(AIQuestionBank).filter(AIQuestionBank.id == question_id).first()
    if not q:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found in question bank.")

    return ApiResponse(
        success=True,
        data=QuestionBankResponse(
            id=q.id,
            category=q.category.value if hasattr(q.category, "value") else str(q.category),
            subject=q.subject,
            job_role=q.job_role,
            difficulty=q.difficulty.value if hasattr(q.difficulty, "value") else str(q.difficulty),
            question_text=q.question_text,
            expected_concepts=q.expected_concepts,
            sample_answer=q.sample_answer,
            hints=q.hints,
            question_source=q.question_source,
            validation_status=q.validation_status.value if hasattr(q.validation_status, "value") else str(q.validation_status),
            is_active=q.is_active,
            created_at=q.created_at,
        ),
    )


# -------------------------------------------------------------
# 3. VOICE INTERVIEW & SPEECH ROUTES
# -------------------------------------------------------------
@router.post("/tts", response_model=ApiResponse[TTSResponse])
def generate_speech_for_question(
    req: TTSRequest,
    current_user: Optional[User] = Depends(get_current_user_optional),
):
    """
    Convert interview question text into speech audio or synthesis instructions.
    """
    tts_result = SpeechService.synthesize_question_speech(
        text=req.text,
        voice=req.voice,
        language=req.language,
    )
    return ApiResponse(
        success=True,
        data=TTSResponse(
            success=tts_result["success"],
            audio_url=tts_result.get("audio_url"),
            format=tts_result["format"],
            text=tts_result["text"],
            cached=tts_result.get("cached", False),
            client_tts_ready=tts_result.get("client_tts_ready", True),
        ),
    )


@router.api_route("/tts/audio/{filename}", methods=["GET", "HEAD"])
def stream_tts_audio(filename: str):
    """
    Serve cached synthetic speech audio files.
    """
    safe_filename = os.path.basename(filename)
    filepath = os.path.join(TTS_CACHE_DIR, safe_filename)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Audio file not found.")
    media_type = "audio/wav" if safe_filename.endswith(".wav") else "audio/mpeg"
    return FileResponse(filepath, media_type=media_type)


@router.post("/stt", response_model=ApiResponse[STTResponse])
async def transcribe_audio_recording(
    file: UploadFile = File(...),
    language: str = Form("en"),
    current_user: User = Depends(get_current_user),
):
    """
    Accept supported audio recording and return speech-to-text transcript.
    """
    stt_result = await SpeechService.transcribe_audio_file(file=file, language=language)
    return ApiResponse(
        success=True,
        message="Audio transcribed successfully.",
        data=STTResponse(**stt_result),
    )


# -------------------------------------------------------------
# 4. ADMINISTRATION & MONITORING ROUTES
# -------------------------------------------------------------
@router.get("/admin/stats")
def get_ai_interview_admin_stats(
    current_user: User = Depends(require_role([RoleEnum.FACULTY, RoleEnum.COLLEGE_ADMIN])),
    db: Session = Depends(get_db),
):
    """
    Administrative monitoring: session counts, question bank metrics, average scores.
    """
    total_sessions = db.query(AIInterviewSession).count()
    completed_sessions = db.query(AIInterviewSession).filter(AIInterviewSession.status == SessionStatusEnum.COMPLETED).count()
    total_bank_questions = db.query(AIQuestionBank).count()
    verified_questions = db.query(AIQuestionBank).filter(AIQuestionBank.validation_status == QuestionValidationStatusEnum.VERIFIED).count()

    reports = db.query(AIInterviewReport).all()
    avg_score = round(sum(r.overall_score for r in reports) / len(reports), 1) if reports else 0.0

    return ApiResponse(
        success=True,
        data={
            "total_sessions": total_sessions,
            "completed_sessions": completed_sessions,
            "in_progress_sessions": total_sessions - completed_sessions,
            "total_bank_questions": total_bank_questions,
            "verified_bank_questions": verified_questions,
            "average_overall_score": avg_score,
        },
    )


# -------------------------------------------------------------
# 5. PARAMETERIZED INTERVIEW SESSION ROUTES (/{interview_id}/...)
# -------------------------------------------------------------
@router.get("/{interview_id}", response_model=ApiResponse[AIInterviewSessionResponse])
def get_interview_state(
    interview_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Retrieve current state of an interview session, active question, or completed report.
    """
    session = AIInterviewService.get_session(db, interview_id, current_user)

    # Find first unanswered question
    current_q = None
    for q in session.questions:
        if not q.answer:
            current_q = q
            break

    q_resp = None
    if current_q:
        q_resp = AIInterviewQuestionResponse(
            id=current_q.id,
            interview_id=session.id,
            question_number=current_q.question_number,
            total_questions=session.total_questions,
            question_text=current_q.question_text,
            topic=current_q.topic,
            difficulty=current_q.difficulty,
            hints=[],
            generated_follow_up=current_q.generated_follow_up,
            question_source=current_q.question_source,
            source_reference=current_q.source_reference,
            asked_at=current_q.asked_at,
        )

    # Format report if completed
    report_resp = None
    if session.report:
        report_resp = AIInterviewReportResponse(
            id=session.report.id,
            interview_id=session.id,
            overall_score=session.report.overall_score,
            technical_summary=session.report.technical_summary,
            communication_summary=session.report.communication_summary,
            strengths=session.report.strengths or [],
            improvement_areas=session.report.improvement_areas or [],
            recommended_topics=session.report.recommended_topics or [],
            final_feedback=session.report.final_feedback,
            generated_at=session.report.generated_at,
            questions_breakdown=[],
        )

    session_resp = AIInterviewSessionResponse(
        id=session.id,
        user_id=session.user_id,
        interview_category=session.interview_category.value if hasattr(session.interview_category, "value") else str(session.interview_category),
        job_role=session.job_role,
        subject=session.subject,
        difficulty=session.difficulty.value if hasattr(session.difficulty, "value") else str(session.difficulty),
        interview_mode=session.interview_mode.value if hasattr(session.interview_mode, "value") else str(session.interview_mode),
        status=session.status.value if hasattr(session.status, "value") else str(session.status),
        started_at=session.started_at,
        completed_at=session.completed_at,
        total_questions=session.total_questions,
        questions_answered=session.questions_answered,
        total_score=session.total_score,
        current_question=q_resp,
        report=report_resp,
    )

    return ApiResponse(success=True, data=session_resp)


@router.post("/{interview_id}/answer", response_model=ApiResponse[AnswerEvaluationResponse])
def submit_interview_answer(
    interview_id: str,
    req: SubmitAnswerRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Submit text answer or confirmed speech transcript for evaluation.
    """
    eval_data = AIInterviewService.submit_answer(db, interview_id, current_user, req)
    return ApiResponse(
        success=True,
        message="Answer evaluated successfully.",
        data=AnswerEvaluationResponse(**eval_data),
    )


@router.post("/{interview_id}/next-question", response_model=ApiResponse[AIInterviewQuestionResponse])
def get_next_interview_question(
    interview_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Retrieve next question when the interview workflow requires an explicit fetch.
    """
    session = AIInterviewService.get_session(db, interview_id, current_user)

    for q in session.questions:
        if not q.answer:
            return ApiResponse(
                success=True,
                data=AIInterviewQuestionResponse(
                    id=q.id,
                    interview_id=session.id,
                    question_number=q.question_number,
                    total_questions=session.total_questions,
                    question_text=q.question_text,
                    topic=q.topic,
                    difficulty=q.difficulty,
                    hints=[],
                    generated_follow_up=q.generated_follow_up,
                    question_source=q.question_source,
                    source_reference=q.source_reference,
                    asked_at=q.asked_at,
                ),
            )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No further unanswered questions. The interview is ready to be finalized.",
    )


@router.post("/{interview_id}/finish", response_model=ApiResponse[AIInterviewReportResponse])
def finish_interview(
    interview_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Explicitly complete an interview session and generate the final report.
    """
    session = AIInterviewService.get_session(db, interview_id, current_user)
    if not session.report:
        report = AIInterviewService._finalize_interview(db, session)
        db.commit()
    else:
        report = session.report

    breakdown = []
    for q in session.questions:
        breakdown.append(
            QuestionAnswerDetail(
                question_number=q.question_number,
                question_text=q.question_text,
                student_answer=q.answer.answer_text if q.answer else None,
                technical_score=q.answer.technical_score if q.answer else None,
                clarity_score=q.answer.clarity_score if q.answer else None,
                feedback=q.answer.feedback if q.answer else None,
                model_answer=q.answer.model_answer if q.answer else None,
            )
        )

    report_resp = AIInterviewReportResponse(
        id=report.id,
        interview_id=session.id,
        overall_score=report.overall_score,
        technical_summary=report.technical_summary,
        communication_summary=report.communication_summary,
        strengths=report.strengths or [],
        improvement_areas=report.improvement_areas or [],
        recommended_topics=report.recommended_topics or [],
        final_feedback=report.final_feedback,
        generated_at=report.generated_at,
        questions_breakdown=breakdown,
    )
    return ApiResponse(success=True, message="Interview concluded successfully.", data=report_resp)


@router.get("/{interview_id}/report", response_model=ApiResponse[AIInterviewReportResponse])
def get_interview_report(
    interview_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Retrieve final comprehensive interview report for a completed session.
    """
    session = AIInterviewService.get_session(db, interview_id, current_user)
    report = AIInterviewService.get_report(db, interview_id, current_user)

    breakdown = []
    for q in session.questions:
        breakdown.append(
            QuestionAnswerDetail(
                question_number=q.question_number,
                question_text=q.question_text,
                student_answer=q.answer.answer_text if q.answer else None,
                technical_score=q.answer.technical_score if q.answer else None,
                clarity_score=q.answer.clarity_score if q.answer else None,
                feedback=q.answer.feedback if q.answer else None,
                model_answer=q.answer.model_answer if q.answer else None,
            )
        )

    report_resp = AIInterviewReportResponse(
        id=report.id,
        interview_id=session.id,
        overall_score=report.overall_score,
        technical_summary=report.technical_summary,
        communication_summary=report.communication_summary,
        strengths=report.strengths or [],
        improvement_areas=report.improvement_areas or [],
        recommended_topics=report.recommended_topics or [],
        final_feedback=report.final_feedback,
        generated_at=report.generated_at,
        questions_breakdown=breakdown,
    )
    return ApiResponse(success=True, data=report_resp)
