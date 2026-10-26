import math
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Set
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.app.models.aptitude_test import (
    AptitudeAttemptStatusEnum,
    AptitudeTestAttempt,
    AptitudeTestQuestion,
    AptitudeTestResponse,
)
from backend.app.models.user import User
from backend.app.schemas.aptitude_test import (
    AptitudeCategoriesResponse,
    AptitudeQuestionGraded,
    AptitudeQuestionOption,
    AptitudeQuestionPublic,
    AptitudeTestActiveResponse,
    AptitudeTestHistoryItem,
    AptitudeTestResultResponse,
    CreateAptitudeTestRequest,
    SaveAptitudeResponseRequest,
    SubmitAptitudeTestRequest,
)
from backend.app.services.llm_aptitude_generator import (
    APTITUDE_CATALOG,
    LLMAptitudeGenerator,
)


class AptitudeService:
    @staticmethod
    def get_categories() -> AptitudeCategoriesResponse:
        return AptitudeCategoriesResponse(
            categories=APTITUDE_CATALOG,
            difficulties=["Easy", "Intermediate", "Advanced"],
            test_modes=[
                {"id": "quick", "label": "Quick Test", "questions": 10, "duration": 15, "description": "10 questions • 15 minutes"},
                {"id": "standard", "label": "Standard Test", "questions": 20, "duration": 30, "description": "20 questions • 30 minutes"},
                {"id": "full", "label": "Full-Length Test", "questions": 30, "duration": 45, "description": "30 questions • 45 minutes"},
                {"id": "custom", "label": "Custom Test", "questions": "Custom", "duration": "Auto", "description": "Choose custom question count"},
            ],
        )

    @classmethod
    def start_test_attempt(
        cls,
        db: Session,
        user: User,
        req: CreateAptitudeTestRequest,
    ) -> AptitudeTestActiveResponse:
        """
        Creates a new test attempt.
        Generates fresh questions with the LLM / dynamic engine, stores the answer key securely,
        and returns the active attempt to the student with answers hidden.
        """
        question_count = req.question_count
        duration_minutes = req.duration_minutes or max(10, math.ceil(question_count * 1.5))

        # 1. Collect recent question fingerprints from student's past attempts to avoid duplicates
        recent_hashes: Set[str] = set()
        past_attempts = (
            db.query(AptitudeTestAttempt.id)
            .filter(AptitudeTestAttempt.user_id == user.id)
            .order_by(AptitudeTestAttempt.created_at.desc())
            .limit(10)
            .all()
        )
        if past_attempts:
            attempt_ids = [a[0] for a in past_attempts]
            hashes = (
                db.query(AptitudeTestQuestion.question_hash)
                .filter(AptitudeTestQuestion.attempt_id.in_(attempt_ids))
                .all()
            )
            recent_hashes = {h[0] for h in hashes if h[0]}

        # 2. Generate questions
        raw_questions, provider_used = LLMAptitudeGenerator.generate_questions(
            category=req.category,
            topic=req.topic,
            difficulty=req.difficulty,
            count=question_count,
            excluded_hashes=recent_hashes,
        )

        now = datetime.utcnow()

        # 3. Create AptitudeTestAttempt
        attempt = AptitudeTestAttempt(
            user_id=user.id,
            category=req.category,
            topic=req.topic,
            difficulty=req.difficulty,
            test_mode=req.test_mode,
            question_count=len(raw_questions),
            duration_minutes=duration_minutes,
            status=AptitudeAttemptStatusEnum.IN_PROGRESS.value,
            total_marks=float(len(raw_questions) * 1.0),
            negative_marks_per_question=0.25,
            started_at=now,
            llm_provider=provider_used,
        )
        db.add(attempt)
        db.flush()

        # 4. Save AptitudeTestQuestions
        public_questions: List[AptitudeQuestionPublic] = []
        for idx, q in enumerate(raw_questions):
            q_model = AptitudeTestQuestion(
                attempt_id=attempt.id,
                order_index=idx + 1,
                question_text=q["question_text"],
                options=q["options"],
                correct_answer=q["correct_answer"],
                explanation=q["explanation"],
                category=q["category"],
                topic=q["topic"],
                difficulty=q["difficulty"],
                marks=q.get("marks", 1.0),
                negative_marks=q.get("negative_marks", 0.25),
                question_hash=q.get("question_hash"),
            )
            db.add(q_model)
            db.flush()

            # Sanitize for student output (NO answers or explanations)
            opts = [AptitudeQuestionOption(id=o["id"], text=o["text"]) for o in q["options"]]
            public_questions.append(
                AptitudeQuestionPublic(
                    id=q_model.id,
                    order_index=q_model.order_index,
                    question_text=q_model.question_text,
                    options=opts,
                    category=q_model.category,
                    topic=q_model.topic,
                    difficulty=q_model.difficulty,
                    marks=q_model.marks,
                    negative_marks=q_model.negative_marks,
                )
            )

        db.commit()
        db.refresh(attempt)

        return AptitudeTestActiveResponse(
            attempt_id=attempt.id,
            category=attempt.category,
            topic=attempt.topic,
            difficulty=attempt.difficulty,
            test_mode=attempt.test_mode,
            question_count=attempt.question_count,
            duration_minutes=attempt.duration_minutes,
            status=attempt.status,
            started_at=attempt.started_at,
            time_remaining_seconds=duration_minutes * 60,
            total_marks=attempt.total_marks,
            negative_marks_per_question=attempt.negative_marks_per_question,
            questions=public_questions,
            saved_responses={},
            llm_provider=provider_used,
        )

    @classmethod
    def get_attempt(
        cls,
        db: Session,
        user: User,
        attempt_id: str,
    ) -> Any:
        attempt = db.query(AptitudeTestAttempt).filter(AptitudeTestAttempt.id == attempt_id).first()
        if not attempt:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aptitude test attempt not found.")

        if attempt.user_id != user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Unauthorized: You cannot access another student's test attempt.",
            )

        # If already completed, return full graded report
        if attempt.status == AptitudeAttemptStatusEnum.COMPLETED.value:
            return cls._build_result_response(db, attempt)

        # If in progress, return public questions (strictly hiding answers and explanations)
        questions = (
            db.query(AptitudeTestQuestion)
            .filter(AptitudeTestQuestion.attempt_id == attempt.id)
            .order_by(AptitudeTestQuestion.order_index.asc())
            .all()
        )

        responses = (
            db.query(AptitudeTestResponse)
            .filter(AptitudeTestResponse.attempt_id == attempt.id)
            .all()
        )
        saved_map = {r.question_id: r.selected_option for r in responses}

        public_questions = []
        for q in questions:
            opts = [AptitudeQuestionOption(id=o["id"], text=o["text"]) for o in q.options]
            public_questions.append(
                AptitudeQuestionPublic(
                    id=q.id,
                    order_index=q.order_index,
                    question_text=q.question_text,
                    options=opts,
                    category=q.category,
                    topic=q.topic,
                    difficulty=q.difficulty,
                    marks=q.marks,
                    negative_marks=q.negative_marks,
                )
            )

        elapsed = (datetime.utcnow() - attempt.started_at).total_seconds()
        total_seconds = attempt.duration_minutes * 60
        remaining_seconds = max(0, int(total_seconds - elapsed))

        return AptitudeTestActiveResponse(
            attempt_id=attempt.id,
            category=attempt.category,
            topic=attempt.topic,
            difficulty=attempt.difficulty,
            test_mode=attempt.test_mode,
            question_count=attempt.question_count,
            duration_minutes=attempt.duration_minutes,
            status=attempt.status,
            started_at=attempt.started_at,
            time_remaining_seconds=remaining_seconds,
            total_marks=attempt.total_marks,
            negative_marks_per_question=attempt.negative_marks_per_question,
            questions=public_questions,
            saved_responses=saved_map,
            llm_provider=attempt.llm_provider,
        )

    @classmethod
    def save_response(
        cls,
        db: Session,
        user: User,
        attempt_id: str,
        req: SaveAptitudeResponseRequest,
    ) -> Dict[str, Any]:
        attempt = db.query(AptitudeTestAttempt).filter(AptitudeTestAttempt.id == attempt_id).first()
        if not attempt or attempt.user_id != user.id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Test attempt not found.")

        if attempt.status != AptitudeAttemptStatusEnum.IN_PROGRESS.value:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Test is already submitted.")

        # Upsert response
        resp = (
            db.query(AptitudeTestResponse)
            .filter(
                AptitudeTestResponse.attempt_id == attempt_id,
                AptitudeTestResponse.question_id == req.question_id,
            )
            .first()
        )
        if not resp:
            resp = AptitudeTestResponse(
                attempt_id=attempt_id,
                question_id=req.question_id,
                selected_option=req.selected_option,
                time_spent_seconds=req.time_spent_seconds or 0,
            )
            db.add(resp)
        else:
            resp.selected_option = req.selected_option
            if req.time_spent_seconds:
                resp.time_spent_seconds = req.time_spent_seconds
            resp.answered_at = datetime.utcnow()

        db.commit()
        return {"success": True, "question_id": req.question_id, "selected_option": req.selected_option}

    @classmethod
    def submit_attempt(
        cls,
        db: Session,
        user: User,
        attempt_id: str,
        req: SubmitAptitudeTestRequest,
    ) -> AptitudeTestResultResponse:
        """
        Grades student's answers on the backend against saved keys,
        applies negative marking, updates stats, and returns full results and explanations.
        """
        attempt = db.query(AptitudeTestAttempt).filter(AptitudeTestAttempt.id == attempt_id).first()
        if not attempt or attempt.user_id != user.id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Test attempt not found.")

        # If already submitted, return existing report (idempotency)
        if attempt.status == AptitudeAttemptStatusEnum.COMPLETED.value:
            return cls._build_result_response(db, attempt)

        # Merge any responses provided in submit request
        if req.responses:
            for q_id, opt in req.responses.items():
                existing = (
                    db.query(AptitudeTestResponse)
                    .filter(
                        AptitudeTestResponse.attempt_id == attempt_id,
                        AptitudeTestResponse.question_id == q_id,
                    )
                    .first()
                )
                if existing:
                    existing.selected_option = opt
                else:
                    db.add(AptitudeTestResponse(attempt_id=attempt_id, question_id=q_id, selected_option=opt))
            db.flush()

        questions = (
            db.query(AptitudeTestQuestion)
            .filter(AptitudeTestQuestion.attempt_id == attempt_id)
            .all()
        )
        responses = (
            db.query(AptitudeTestResponse)
            .filter(AptitudeTestResponse.attempt_id == attempt_id)
            .all()
        )
        resp_map = {r.question_id: r for r in responses}

        correct_count = 0
        incorrect_count = 0
        unattempted_count = 0
        total_positive_marks = 0.0
        total_negative_deducted = 0.0

        for q in questions:
            r = resp_map.get(q.id)
            selected = r.selected_option if r else None

            if not selected:
                unattempted_count += 1
                if r:
                    r.is_correct = None
                    r.marks_awarded = 0.0
            elif selected.upper() == q.correct_answer.upper():
                correct_count += 1
                total_positive_marks += q.marks
                if r:
                    r.is_correct = True
                    r.marks_awarded = q.marks
            else:
                incorrect_count += 1
                total_negative_deducted += q.negative_marks
                if r:
                    r.is_correct = False
                    r.marks_awarded = -q.negative_marks

        # Final score calculation with negative marking
        final_score = max(0.0, round(total_positive_marks - total_negative_deducted, 2))
        total_attempted = correct_count + incorrect_count
        accuracy = round((correct_count / total_attempted) * 100, 1) if total_attempted > 0 else 0.0

        now = datetime.utcnow()
        time_spent = req.time_spent_seconds or int((now - attempt.started_at).total_seconds())

        attempt.status = AptitudeAttemptStatusEnum.COMPLETED.value
        attempt.submitted_at = now
        attempt.correct_count = correct_count
        attempt.incorrect_count = incorrect_count
        attempt.unattempted_count = unattempted_count
        attempt.marks_obtained = total_positive_marks
        attempt.total_negative_marks = total_negative_deducted
        attempt.final_score = final_score
        attempt.accuracy_percentage = accuracy
        attempt.time_spent_seconds = time_spent

        db.commit()
        db.refresh(attempt)

        return cls._build_result_response(db, attempt)

    @classmethod
    def _build_result_response(cls, db: Session, attempt: AptitudeTestAttempt) -> AptitudeTestResultResponse:
        questions = (
            db.query(AptitudeTestQuestion)
            .filter(AptitudeTestQuestion.attempt_id == attempt.id)
            .order_by(AptitudeTestQuestion.order_index.asc())
            .all()
        )
        responses = (
            db.query(AptitudeTestResponse)
            .filter(AptitudeTestResponse.attempt_id == attempt.id)
            .all()
        )
        resp_map = {r.question_id: r for r in responses}

        topic_stats: Dict[str, Dict[str, int]] = {}
        graded_questions: List[AptitudeQuestionGraded] = []

        for q in questions:
            r = resp_map.get(q.id)
            selected = r.selected_option if r else None
            is_corr = bool(selected and selected.upper() == q.correct_answer.upper())

            # Topic breakdown
            top = q.topic or "General"
            if top not in topic_stats:
                topic_stats[top] = {"total": 0, "correct": 0}
            topic_stats[top]["total"] += 1
            if is_corr:
                topic_stats[top]["correct"] += 1

            opts = [AptitudeQuestionOption(id=o["id"], text=o["text"]) for o in q.options]
            graded_questions.append(
                AptitudeQuestionGraded(
                    id=q.id,
                    order_index=q.order_index,
                    question_text=q.question_text,
                    options=opts,
                    selected_option=selected,
                    correct_answer=q.correct_answer,
                    is_correct=is_corr,
                    marks_awarded=q.marks if is_corr else (-q.negative_marks if selected else 0.0),
                    explanation=q.explanation,
                    category=q.category,
                    topic=q.topic,
                    difficulty=q.difficulty,
                )
            )

        return AptitudeTestResultResponse(
            attempt_id=attempt.id,
            category=attempt.category,
            topic=attempt.topic,
            difficulty=attempt.difficulty,
            question_count=attempt.question_count,
            total_marks=attempt.total_marks,
            marks_obtained=attempt.marks_obtained,
            total_negative_marks=attempt.total_negative_marks,
            final_score=attempt.final_score,
            accuracy_percentage=attempt.accuracy_percentage,
            correct_count=attempt.correct_count,
            incorrect_count=attempt.incorrect_count,
            unattempted_count=attempt.unattempted_count,
            time_spent_seconds=attempt.time_spent_seconds,
            started_at=attempt.started_at,
            submitted_at=attempt.submitted_at,
            questions=graded_questions,
            topic_breakdown=topic_stats,
            llm_provider=attempt.llm_provider,
        )

    @classmethod
    def get_user_history(cls, db: Session, user: User) -> List[AptitudeTestHistoryItem]:
        attempts = (
            db.query(AptitudeTestAttempt)
            .filter(AptitudeTestAttempt.user_id == user.id)
            .order_by(AptitudeTestAttempt.created_at.desc())
            .all()
        )
        return [
            AptitudeTestHistoryItem(
                attempt_id=a.id,
                category=a.category,
                topic=a.topic,
                difficulty=a.difficulty,
                question_count=a.question_count,
                final_score=a.final_score,
                total_marks=a.total_marks,
                accuracy_percentage=a.accuracy_percentage,
                correct_count=a.correct_count,
                incorrect_count=a.incorrect_count,
                unattempted_count=a.unattempted_count,
                time_spent_seconds=a.time_spent_seconds,
                submitted_at=a.submitted_at,
                status=a.status,
            )
            for a in attempts
        ]
