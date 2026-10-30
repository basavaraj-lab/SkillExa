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
from backend.app.models.ai_interview import EducationalKnowledgeSource
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

    @classmethod
    def get_topic_learning_module(
        cls,
        db: Session,
        subject: str,
        topic: str,
        difficulty: str = "Intermediate",
        count: int = 5,
    ) -> Dict[str, Any]:
        """
        Generate or fetch verified subject topic curriculum grounded in Wikipedia theory,
        core formulas, step-by-step solved drills, and dynamic LLM MCQs.
        """
        raw_topic = (topic or "").lower()
        
        # Topic Metadata Directory for Quantitative Aptitude, Reasoning, and Verbal Ability
        TOPIC_METADATA = {
            "number": {
                "category": "Quantitative Aptitude",
                "aptitude_topic": "Number System",
                "wiki_title": "Numeral system",
                "concept": "A numeral system is a mathematical framework for representing numbers using consistent symbols. Core concepts include prime factorization, divisibility rules (2, 3, 4, 5, 8, 9, 11), HCF (Greatest Common Divisor), and LCM (Lowest Common Multiple). Fundamental Theorem: For any two positive integers A and B, A × B = HCF(A, B) × LCM(A, B).",
                "formulas": [
                    {"name": "HCF-LCM Identity", "formula": "A × B = HCF × LCM", "shortcut": "If HCF is h, numbers can be written as h·a and h·b where a, b are coprime."},
                    {"name": "Sum of First n Natural Numbers", "formula": "Sum = n(n + 1) / 2", "shortcut": "Sum of first n odd numbers = n²; Sum of first n even numbers = n(n + 1)."},
                    {"name": "Divisibility by 9 & 11", "formula": "Sum of digits divisible by 9; Alternate sum difference divisible by 11", "shortcut": "Instant verification for large numerical quantities."},
                ],
                "solved_example": {
                    "problem": "The HCF and LCM of two numbers are 12 and 240 respectively. If one of the numbers is 48, find the other number.",
                    "given": "HCF = 12, LCM = 240, Number 1 (A) = 48",
                    "formula": "A × B = HCF × LCM",
                    "steps": [
                        "Step 1: Set up the product equation: 48 × B = 12 × 240",
                        "Step 2: Calculate right-hand side: 12 × 240 = 2,880",
                        "Step 3: Solve for B: B = 2,880 / 48 = 60",
                    ],
                    "answer": "The other number is 60."
                },
                "fill_blanks": {
                    "question": "Two numbers have HCF = 16 and LCM = 160. If one number is 32, then the second number is _____.",
                    "blank_text": "Second Number = (16 × 160) / 32 = _____",
                    "options": ["80", "64", "96", "100"],
                    "answer": "80"
                }
            },
            "percent": {
                "category": "Quantitative Aptitude",
                "aptitude_topic": "Percentages",
                "wiki_title": "Percentage",
                "concept": "A percentage represents a quantity expressed as a fraction of 100. It is foundational for calculating commercial profit margins, markup, successive discounts, and depreciation. Key principle: Successive percentage changes a% and b% yield net change = a + b + (ab / 100)%.",
                "formulas": [
                    {"name": "Percentage Value", "formula": "Value = (P% / 100) × Base Amount", "shortcut": "Fraction conversions: 1/2 = 50%, 1/3 = 33.33%, 1/4 = 25%, 1/5 = 20%, 1/6 = 16.67%, 1/8 = 12.5%."},
                    {"name": "Net Successive Change", "formula": "Net % = a + b + (ab / 100)", "shortcut": "For successive discount of d1 and d2: Net Discount = d1 + d2 - (d1 × d2 / 100)%."},
                    {"name": "Profit & Loss Margin", "formula": "Profit % = (Profit / Cost Price) × 100%", "shortcut": "Profit or loss is always evaluated on Cost Price (CP), never Selling Price (SP)."},
                ],
                "solved_example": {
                    "problem": "An item priced at ₹1,500 receives two successive discounts of 20% and 10%. What is the final selling price?",
                    "given": "Marked Price (MP) = ₹1,500, Discount 1 = 20%, Discount 2 = 10%",
                    "formula": "SP = MP × (1 - d1/100) × (1 - d2/100)",
                    "steps": [
                        "Step 1: Calculate net equivalent discount: 20 + 10 - (20 × 10 / 100) = 30 - 2 = 28%",
                        "Step 2: Final selling price is (100 - 28)% = 72% of Marked Price",
                        "Step 3: SP = 0.72 × 1,500 = ₹1,080",
                    ],
                    "answer": "Final selling price is ₹1,080."
                },
                "fill_blanks": {
                    "question": "If the price of a commodity increases by 25%, by what percent must consumption be reduced so the expenditure remains constant? Answer: _____%.",
                    "blank_text": "Reduction = [25 / (100 + 25)] × 100% = _____%",
                    "options": ["20%", "25%", "15%", "18%"],
                    "answer": "20%"
                }
            },
            "ratio": {
                "category": "Quantitative Aptitude",
                "aptitude_topic": "Ratio and Proportion",
                "wiki_title": "Ratio",
                "concept": "A ratio expresses the relative magnitude of two or more quantities of the same kind. A proportion states the equality of two ratios: a/b = c/d (meaning ad = bc). In partnership investments, profits are divided strictly in proportion to (Capital × Time Duration).",
                "formulas": [
                    {"name": "Proportion Cross Product", "formula": "a : b :: c : d ⟹ a × d = b × c", "shortcut": "Mean Proportional of a and b = √(a × b). Third Proportional of a and b = b² / a."},
                    {"name": "Compounded Ratio", "formula": "Compounded ratio of (a:b) and (c:d) = (ac : bd)", "shortcut": "Duplicate ratio = a²:b²; Sub-duplicate = √a:√b."},
                    {"name": "Partnership Division", "formula": "Profit Ratio = (P1 × T1) : (P2 × T2)", "shortcut": "If time periods are identical, profits divide directly by capital invested."},
                ],
                "solved_example": {
                    "problem": "A sum of ₹4,800 is divided among A, B, and C in the ratio 2 : 3 : 5. Find the share of B.",
                    "given": "Total Sum = ₹4,800, Ratio = 2 : 3 : 5",
                    "formula": "Share of B = [Ratio of B / Sum of Ratio Terms] × Total Sum",
                    "steps": [
                        "Step 1: Sum of ratio parts = 2 + 3 + 5 = 10 parts",
                        "Step 2: Value of 1 part = 4,800 / 10 = ₹480",
                        "Step 3: B's share (3 parts) = 3 × 480 = ₹1,440",
                    ],
                    "answer": "Share of B is ₹1,440."
                },
                "fill_blanks": {
                    "question": "If a : b = 3 : 4 and b : c = 8 : 9, then the ratio a : c is _____.",
                    "blank_text": "a/c = (a/b) × (b/c) = (3/4) × (8/9) = _____.",
                    "options": ["2 : 3", "1 : 2", "3 : 4", "4 : 5"],
                    "answer": "2 : 3"
                }
            },
            "work": {
                "category": "Quantitative Aptitude",
                "aptitude_topic": "Time and Work",
                "wiki_title": "Unit rate",
                "concept": "Time and work problems utilize unit work rate theory. If a worker can finish a task in D days, their 1-day efficiency is 1/D of the total work. Combined work of individuals A and B working together is the sum of their individual daily efficiencies: (1/A + 1/B).",
                "formulas": [
                    {"name": "Two Workers Combined", "formula": "Time Together = (A × B) / (A + B) days", "shortcut": "Product over sum formula: T = (xy) / (x + y)."},
                    {"name": "Work and Efficiency", "formula": "Efficiency = Work / Time (Work = Men × Days × Hours)", "shortcut": "Chain Rule: (M1 × D1 × H1) / W1 = (M2 × D2 × H2) / W2."},
                    {"name": "Pipes & Cisterns", "formula": "Net Rate = 1/Inlet - 1/Outlet", "shortcut": "Emptying pipes contribute negative work rate."},
                ],
                "solved_example": {
                    "problem": "Pipe A can fill a tank in 12 hours, while Pipe B can fill it in 15 hours. If both pipes are opened together, how long will it take to fill the tank?",
                    "given": "Time for A = 12 hrs, Time for B = 15 hrs",
                    "formula": "Combined Time = (A × B) / (A + B)",
                    "steps": [
                        "Step 1: Compute product: 12 × 15 = 180",
                        "Step 2: Compute sum: 12 + 15 = 27",
                        "Step 3: Time taken = 180 / 27 = 20 / 3 = 6 hours and 40 minutes",
                    ],
                    "answer": "The tank will be filled in 6 hours and 40 minutes."
                },
                "fill_blanks": {
                    "question": "A can do a piece of work in 10 days and B in 15 days. Working together, they will finish the work in _____ days.",
                    "blank_text": "Time = (10 × 15) / (10 + 15) = 150 / 25 = _____ days.",
                    "options": ["6", "5", "8", "7.5"],
                    "answer": "6"
                }
            },
            "speed": {
                "category": "Quantitative Aptitude",
                "aptitude_topic": "Time, Speed and Distance",
                "wiki_title": "Speed",
                "concept": "Speed measures the distance traveled per unit time: Speed = Distance / Time. When objects move relative to each other: opposite directions add speeds (u + v), while same direction subtracts speeds (|u - v|).",
                "formulas": [
                    {"name": "Unit Conversion", "formula": "1 km/h = 5/18 m/s | 1 m/s = 18/5 km/h", "shortcut": "Multiply km/h by 5/18 to get m/s instantly."},
                    {"name": "Average Speed for Equal Distance", "formula": "Avg Speed = 2uv / (u + v)", "shortcut": "Harmonic mean of the two speeds."},
                    {"name": "Train Crossing Object", "formula": "Time = (Train Length + Platform Length) / Speed", "shortcut": "Telegraph poles and stationary people have platform length = 0."},
                ],
                "solved_example": {
                    "problem": "A 180-metre-long train traveling at 72 km/h crosses a platform in 20 seconds. What is the length of the platform?",
                    "given": "Train Length = 180 m, Speed = 72 km/h, Time = 20 s",
                    "formula": "Distance = Speed × Time",
                    "steps": [
                        "Step 1: Convert speed to m/s: 72 × (5/18) = 20 m/s",
                        "Step 2: Total distance covered = Speed × Time = 20 × 20 = 400 metres",
                        "Step 3: Platform Length = Total Distance - Train Length = 400 - 180 = 220 metres",
                    ],
                    "answer": "The platform is 220 metres long."
                },
                "fill_blanks": {
                    "question": "A car covers a distance of 150 km in 3 hours. Its speed in m/s is _____ m/s.",
                    "blank_text": "Speed = 150 / 3 = 50 km/h = 50 × (5/18) = 250 / 18 ≈ _____ m/s.",
                    "options": ["13.89", "15.0", "12.5", "14.2"],
                    "answer": "13.89"
                }
            },
            "interest": {
                "category": "Quantitative Aptitude",
                "aptitude_topic": "Simple and Compound Interest",
                "wiki_title": "Compound interest",
                "concept": "Interest is the charge for the privilege of borrowing money. Simple Interest (SI) is calculated solely on the principal, whereas Compound Interest (CI) calculates interest on principal plus accumulated past interest.",
                "formulas": [
                    {"name": "Simple Interest Formula", "formula": "SI = (P × R × T) / 100", "shortcut": "Total Amount A = P + SI = P(1 + RT/100)."},
                    {"name": "Compound Interest Formula", "formula": "A = P(1 + R/100)^T", "shortcut": "CI = Amount - Principal = P[(1 + R/100)^T - 1]."},
                    {"name": "2-Year CI - SI Difference", "formula": "Difference = P × (R / 100)²", "shortcut": "For 3 years: Difference = P × (R/100)² × (3 + R/100)."},
                ],
                "solved_example": {
                    "problem": "The difference between Compound Interest and Simple Interest on a sum of money for 2 years at 10% per annum is ₹65. Find the sum.",
                    "given": "Difference = ₹65, Rate (R) = 10%, Time (T) = 2 years",
                    "formula": "Difference = P × (R / 100)²",
                    "steps": [
                        "Step 1: Express difference formula: 65 = P × (10 / 100)²",
                        "Step 2: Simplify ratio: (1/10)² = 1/100",
                        "Step 3: Solve for P: P = 65 × 100 = ₹6,500",
                    ],
                    "answer": "The principal sum is ₹6,500."
                },
                "fill_blanks": {
                    "question": "The Simple Interest on ₹8,000 at 5% per annum for 3 years is ₹_____.",
                    "blank_text": "SI = (8000 × 5 × 3) / 100 = _____.",
                    "options": ["1200", "1000", "1500", "1250"],
                    "answer": "1200"
                }
            },
            "mensuration": {
                "category": "Quantitative Aptitude",
                "aptitude_topic": "Mensuration",
                "wiki_title": "Mensuration (mathematics)",
                "concept": "Mensuration is the geometry of measurement of 2D shapes (perimeter, area) and 3D solids (surface area, volume). Essential formulas involve circles, cylinders, cones, and spheres.",
                "formulas": [
                    {"name": "2D Circular Geometry", "formula": "Area = πr² | Perimeter = 2πr", "shortcut": "If radius is doubled, area increases 4-fold."},
                    {"name": "Right Circular Cylinder", "formula": "Volume = πr²h | Total Surface Area = 2πr(h + r)", "shortcut": "Curved surface area = 2πrh."},
                    {"name": "Solid Sphere", "formula": "Volume = (4/3)πr³ | Surface Area = 4πr²", "shortcut": "Hemisphere volume = (2/3)πr³; TSA = 3πr²."},
                ],
                "solved_example": {
                    "problem": "A cylindrical tank has a base radius of 7 m and a height of 10 m. What is its capacity in cubic metres?",
                    "given": "Radius (r) = 7 m, Height (h) = 10 m",
                    "formula": "Volume = πr²h (where π ≈ 22/7)",
                    "steps": [
                        "Step 1: Substitute values: V = (22/7) × 7 × 7 × 10",
                        "Step 2: Cancel 7: V = 22 × 7 × 10",
                        "Step 3: Multiply: V = 154 × 10 = 1,540 m³",
                    ],
                    "answer": "The tank capacity is 1,540 m³."
                },
                "fill_blanks": {
                    "question": "The area of a circle with diameter 14 cm is _____ cm² (use π = 22/7).",
                    "blank_text": "Radius = 7 cm. Area = (22/7) × 7² = _____ cm².",
                    "options": ["154", "144", "176", "132"],
                    "answer": "154"
                }
            },
            "di": {
                "category": "Quantitative Aptitude",
                "aptitude_topic": "Data Interpretation",
                "wiki_title": "Data analysis",
                "concept": "Data Interpretation assesses numerical analysis from visual representations: Bar charts, Pie charts, and Line plots. Key skills include percentage ratio comparison, average calculation, and angular conversion (100% = 360°, 1% = 3.6°).",
                "formulas": [
                    {"name": "Pie Chart Angle Conversion", "formula": "Angle (degrees) = (Value / Total) × 360°", "shortcut": "10% = 36° | 25% = 90° | 50% = 180°."},
                    {"name": "Percentage Growth", "formula": "Growth % = [(Final - Initial) / Initial] × 100%", "shortcut": "Always divide by initial baseline value."},
                    {"name": "Ratio Comparison", "formula": "Ratio = Total Category A / Total Category B", "shortcut": "Cross-multiply fractions to quickly compare magnitudes."},
                ],
                "solved_example": {
                    "problem": "In a pie chart showing a university budget, the library expenditure is represented by a central angle of 54°. What percentage of the total budget is allocated to the library?",
                    "given": "Central angle = 54°, Total angle in circle = 360°",
                    "formula": "Percentage = (Angle / 360) × 100%",
                    "steps": [
                        "Step 1: Set up the fraction: 54 / 360",
                        "Step 2: Simplify: 54 / 360 = 3 / 20",
                        "Step 3: Multiply by 100: (3 / 20) × 100 = 15%",
                    ],
                    "answer": "15% of the total budget is allocated to the library."
                },
                "fill_blanks": {
                    "question": "In a pie chart, an expenditure representing 25% of the total corresponds to a sector angle of _____°.",
                    "blank_text": "Angle = (25 / 100) × 360° = _____°.",
                    "options": ["90", "75", "100", "80"],
                    "answer": "90"
                }
            },
            "syllogism": {
                "category": "Logical Reasoning",
                "aptitude_topic": "Syllogism",
                "wiki_title": "Syllogism",
                "concept": "Syllogism is deductive reasoning where a conclusion is derived from premises. Key rules: Two affirmative premises give an affirmative conclusion; two negative premises yield no conclusion; 'Some' implies at least one.",
                "formulas": [
                    {"name": "Categorical Propositions", "formula": "A (All), E (No), I (Some), O (Some not)", "shortcut": "Venn diagrams: draw overlapping circles to test minimum overlap."},
                    {"name": "Complementary Pairs", "formula": "(All A are B + Some A are not B) OR (No A is B + Some A is B)", "shortcut": "Either-Or conditions require subject-predicate alignment."},
                ],
                "solved_example": {
                    "problem": "Statements: All roses are flowers. Some flowers are red. Conclusions: I. Some roses are red. II. Some flowers are roses.",
                    "given": "All roses are flowers (Rose ⊆ Flower); Some flowers are red (Flower ∩ Red ≠ ∅)",
                    "formula": "Venn Diagram inclusion test",
                    "steps": [
                        "Step 1: Rose circle is entirely inside Flower circle.",
                        "Step 2: Red circle overlaps Flower circle, but does not necessarily touch Rose circle.",
                        "Step 3: Conclusion I (Some roses are red) is a possibility, not definite. Conclusion II (Some flowers are roses) is definitely true because roses are inside flowers.",
                    ],
                    "answer": "Only Conclusion II follows."
                },
                "fill_blanks": {
                    "question": "In deductive syllogisms, two negative premises (No A is B; No B is C) lead to _____ definite conclusion.",
                    "blank_text": "Negative premise rule yields _____ conclusion.",
                    "options": ["no", "one", "two", "universal"],
                    "answer": "no"
                }
            },
            "comprehension": {
                "category": "Verbal Ability",
                "aptitude_topic": "Reading Comprehension",
                "wiki_title": "Reading comprehension",
                "concept": "Reading comprehension tests extraction of explicit details, tone, author's perspective, and implicit assumptions from passages. Avoid outside knowledge; rely solely on textual evidence.",
                "formulas": [
                    {"name": "Main Idea Strategy", "formula": "Thesis = Topic + Author's Specific Angle", "shortcut": "First and last sentences of each paragraph typically signal transition and main idea."},
                    {"name": "Inference Principle", "formula": "Inference = Stated Fact + Logical Deduction", "shortcut": "Eliminate extreme keywords: 'always', 'never', 'only' unless supported by passage."},
                ],
                "solved_example": {
                    "problem": "Passage: 'Technological automation displaced manual manufacturing jobs, but simultaneously stimulated employment in software engineering and data analytics.' Question: What does the passage imply about technological automation?",
                    "given": "Passage excerpt about manufacturing decrease and software increase",
                    "formula": "Contextual Inference",
                    "steps": [
                        "Step 1: Identify keywords: 'displaced manual', 'simultaneously stimulated software'.",
                        "Step 2: Synthesize: automation changes employment composition rather than merely eliminating work.",
                    ],
                    "answer": "Automation reallocates job demand across different sectors."
                },
                "fill_blanks": {
                    "question": "When an author provides contrasting arguments without favoring one, the tone is _____.",
                    "blank_text": "Balanced and factual tone is termed _____.",
                    "options": ["objective", "cynical", "biased", "satirical"],
                    "answer": "objective"
                }
            },
            "mechanics": {
                "category": "General Science",
                "aptitude_topic": "Physics & Mechanics",
                "wiki_title": "Classical mechanics",
                "concept": "Mechanics analyzes force, mass, acceleration, and kinetic energy. Newton's laws govern linear and rotational motion: F = ma, v = u + at, and s = ut + (1/2)at².",
                "formulas": [
                    {"name": "Kinematic Equations", "formula": "v = u + at | s = ut + 0.5at² | v² = u² + 2as", "shortcut": "Under free fall near Earth, acceleration a = g ≈ 9.8 m/s²."},
                    {"name": "Work and Kinetic Energy", "formula": "W = F · d | KE = (1/2)mv²", "shortcut": "Work done equals the change in kinetic energy."},
                ],
                "solved_example": {
                    "problem": "A car accelerates uniformly from rest to 20 m/s in 5 seconds. What is the distance traveled?",
                    "given": "Initial velocity u = 0, Final velocity v = 20 m/s, Time t = 5 s",
                    "formula": "Distance s = (u + v) / 2 × t",
                    "steps": [
                        "Step 1: Average velocity = (0 + 20) / 2 = 10 m/s",
                        "Step 2: Distance = 10 × 5 = 50 metres",
                    ],
                    "answer": "Distance traveled is 50 metres."
                },
                "fill_blanks": {
                    "question": "The rate of change of momentum of a body is directly proportional to the applied _____.",
                    "blank_text": "Newton's Second Law: F = dp/dt corresponds to _____.",
                    "options": ["force", "velocity", "work", "energy"],
                    "answer": "force"
                }
            },
            "polity": {
                "category": "General Awareness",
                "aptitude_topic": "Indian Polity & Constitution",
                "wiki_title": "Constitution of India",
                "concept": "The Indian Constitution establishes a sovereign democratic republic with fundamental rights, directive principles, and a separation of powers across Executive, Legislature, and Judiciary.",
                "formulas": [
                    {"name": "Key Articles", "formula": "Article 14 (Equality), Article 21 (Life & Liberty), Article 32 (Constitutional Remedies)", "shortcut": "Article 32 was termed the 'Heart and Soul of the Constitution' by Dr. B.R. Ambedkar."},
                ],
                "solved_example": {
                    "problem": "Which article of the Indian Constitution guarantees the Right to Constitutional Remedies allowing citizens to move the Supreme Court?",
                    "given": "Right to Constitutional Remedies",
                    "formula": "Constitutional Articles mapping",
                    "steps": [
                        "Step 1: Part III encompasses Fundamental Rights (Articles 12 to 35).",
                        "Step 2: Article 32 empowers the Supreme Court to issue writs (Habeas Corpus, Mandamus, etc.).",
                    ],
                    "answer": "Article 32."
                },
                "fill_blanks": {
                    "question": "The Fundamental Rights of the Indian Constitution are enshrined in Part _____.",
                    "blank_text": "Fundamental Rights reside in Part _____.",
                    "options": ["III", "IV", "II", "IVA"],
                    "answer": "III"
                }
            }
        }

        # Find matching metadata key (sort by key length descending so 'mensuration' matches before 'ratio')
        matched_meta = None
        for k, v in sorted(TOPIC_METADATA.items(), key=lambda x: len(x[0]), reverse=True):
            if k in raw_topic:
                matched_meta = v
                break
        
        if not matched_meta:
            # Fallback to percentage or generic quantitative aptitude
            matched_meta = TOPIC_METADATA["percent"]

        # Fetch Wikipedia Educational Grounding
        wiki_source = db.query(EducationalKnowledgeSource).filter(
            EducationalKnowledgeSource.article_title == matched_meta["wiki_title"]
        ).first()

        wiki_info = {
            "title": wiki_source.article_title if wiki_source else matched_meta["wiki_title"],
            "summary": wiki_source.content_summary if wiki_source else matched_meta["concept"],
            "source_url": wiki_source.source_url if wiki_source else f"https://en.wikipedia.org/wiki/{matched_meta['wiki_title'].replace(' ', '_')}",
            "attribution": wiki_source.attribution if wiki_source else f"Content derived from Wikipedia article '{matched_meta['wiki_title']}'",
        }

        # Generate fresh, dynamic topic MCQs via LLMAptitudeGenerator
        raw_qs, provider_used = LLMAptitudeGenerator.generate_questions(
            category=matched_meta["category"],
            topic=matched_meta["aptitude_topic"],
            difficulty=difficulty,
            count=count,
        )

        formatted_mcqs = []
        for idx, q in enumerate(raw_qs):
            opts = [o["text"] for o in q.get("options", [])]
            correct_id = q.get("correct_answer", "A")
            # Map 'A', 'B', 'C', 'D' to 0, 1, 2, 3
            letter_map = {"A": 0, "B": 1, "C": 2, "D": 3}
            corr_idx = letter_map.get(str(correct_id).upper(), 0)
            formatted_mcqs.append({
                "id": idx + 1,
                "question": q.get("question_text", ""),
                "options": opts,
                "correct_option": corr_idx,
                "explanation": q.get("explanation", ""),
                "difficulty": q.get("difficulty", difficulty),
                "topic": matched_meta["aptitude_topic"],
                "category": matched_meta["category"],
            })

        return {
            "subject": subject or "Quantitative Aptitude",
            "topic": topic,
            "category": matched_meta["category"],
            "aptitude_topic": matched_meta["aptitude_topic"],
            "concept": matched_meta["concept"],
            "wikipedia": wiki_info,
            "formulas": matched_meta["formulas"],
            "solved_example": matched_meta["solved_example"],
            "fill_blanks": matched_meta["fill_blanks"],
            "mcqs": formatted_mcqs,
            "provider_used": provider_used,
        }
