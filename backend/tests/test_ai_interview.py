import io
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from backend.app.models.ai_interview import (
    AIInterviewAnswer,
    AIInterviewQuestion,
    AIInterviewReport,
    AIInterviewSession,
    AIQuestionBank,
    InterviewCategoryEnum,
    InterviewDifficultyEnum,
    SessionStatusEnum,
)
from backend.app.models.user import RoleEnum, StudentProfile, User
from backend.app.services.ai_provider_service import AIProviderService
from backend.app.services.answer_evaluation_service import AnswerEvaluationService
from backend.app.services.knowledge_retrieval_service import KnowledgeRetrievalService
from backend.app.services.question_generation_service import QuestionGenerationService
from backend.app.services.speech_service import SpeechService
from backend.app.utils.security import hash_password


# -------------------------------------------------------------
# 1. TEST STARTING AN INTERVIEW & QUESTION SELECTION
# -------------------------------------------------------------
def test_start_ai_interview(client: TestClient, student_token: str):
    """Test starting an AI mock interview creates session and first question."""
    payload = {
        "interview_category": "Technical",
        "job_role": "Software Developer",
        "subject": "Python",
        "difficulty": "Intermediate",
        "experience_level": "Student",
        "total_questions": 3,
        "interview_mode": "text",
        "preferred_language": "English",
        "duration_minutes": 20,
    }
    headers = {"Authorization": f"Bearer {student_token}"}
    res = client.post("/api/ai-interview/start", json=payload, headers=headers)
    assert res.status_code == 201
    data = res.json()["data"]

    assert data["subject"] == "Python"
    assert data["total_questions"] == 3
    assert data["questions_answered"] == 0
    assert data["status"] == "in_progress"
    assert data["current_question"] is not None
    assert data["current_question"]["question_number"] == 1
    assert "Python" in data["current_question"]["question_text"] or len(data["current_question"]["question_text"]) > 10


def test_unauthorized_start_rejected(client: TestClient):
    """Test starting an interview without token returns 401."""
    res = client.post("/api/ai-interview/start", json={"subject": "Python"})
    assert res.status_code == 401


# -------------------------------------------------------------
# 2. TEST SUBMITTING ANSWERS & EVALUATION
# -------------------------------------------------------------
def test_submit_correct_answer(client: TestClient, student_token: str):
    """Test submitting an informative technical answer produces positive multi-criteria score."""
    headers = {"Authorization": f"Bearer {student_token}"}
    # 1. Start session
    start_res = client.post(
        "/api/ai-interview/start",
        json={"interview_category": "Technical", "subject": "Python", "difficulty": "Intermediate", "total_questions": 3},
        headers=headers,
    )
    assert start_res.status_code == 201
    session_id = start_res.json()["data"]["id"]
    q1_id = start_res.json()["data"]["current_question"]["id"]

    # 2. Submit high-quality answer
    answer_payload = {
        "question_id": q1_id,
        "answer_text": "Generators in Python use the yield keyword to produce values lazily on-the-fly rather than holding entire collections in RAM. This provides immense memory efficiency and follows the iterator protocol with next() and StopIteration.",
        "answer_mode": "text",
    }
    ans_res = client.post(f"/api/ai-interview/{session_id}/answer", json=answer_payload, headers=headers)
    assert ans_res.status_code == 200
    ans_data = ans_res.json()["data"]

    assert ans_data["technical_score"] >= 6.0
    assert ans_data["completeness_score"] >= 6.0
    assert ans_data["clarity_score"] >= 6.0
    assert ans_data["communication_score"] >= 6.0
    assert ans_data["overall_score"] >= 60.0
    assert len(ans_data["strengths"]) > 0
    assert ans_data["is_interview_complete"] is False
    assert ans_data["next_question_number"] == 2


def test_submit_empty_or_idk_answer(client: TestClient, student_token: str):
    """Test submitting 'I don't know' handles scoring gracefully with constructive encouragement."""
    headers = {"Authorization": f"Bearer {student_token}"}
    start_res = client.post(
        "/api/ai-interview/start",
        json={"interview_category": "Technical", "subject": "Python", "difficulty": "Intermediate", "total_questions": 2},
        headers=headers,
    )
    session_id = start_res.json()["data"]["id"]
    q1_id = start_res.json()["data"]["current_question"]["id"]

    answer_payload = {
        "question_id": q1_id,
        "answer_text": "I don't know",
        "answer_mode": "text",
    }
    ans_res = client.post(f"/api/ai-interview/{session_id}/answer", json=answer_payload, headers=headers)
    assert ans_res.status_code == 200
    ans_data = ans_res.json()["data"]

    assert ans_data["technical_score"] <= 3.0
    assert "thought process" in ans_data["feedback"].lower()
    assert len(ans_data["missing_concepts"]) > 0


def test_prevent_duplicate_answer_submission(client: TestClient, student_token: str):
    """Test duplicate submission for the same question is rejected with 409 Conflict."""
    headers = {"Authorization": f"Bearer {student_token}"}
    start_res = client.post(
        "/api/ai-interview/start",
        json={"interview_category": "Technical", "subject": "Python", "total_questions": 2},
        headers=headers,
    )
    session_id = start_res.json()["data"]["id"]
    q1_id = start_res.json()["data"]["current_question"]["id"]

    payload = {"question_id": q1_id, "answer_text": "First submission explaining the technical concept.", "answer_mode": "text"}
    res1 = client.post(f"/api/ai-interview/{session_id}/answer", json=payload, headers=headers)
    assert res1.status_code == 200

    # Second submission for the same question
    res2 = client.post(f"/api/ai-interview/{session_id}/answer", json=payload, headers=headers)
    assert res2.status_code == 409


# -------------------------------------------------------------
# 3. TEST FULL INTERVIEW WORKFLOW & FINAL REPORT
# -------------------------------------------------------------
def test_complete_interview_workflow_and_report(client: TestClient, student_token: str):
    """Test answering all questions in an interview session generates final report."""
    headers = {"Authorization": f"Bearer {student_token}"}
    # Start 2-question interview
    start_res = client.post(
        "/api/ai-interview/start",
        json={"interview_category": "HR", "subject": "HR", "total_questions": 2},
        headers=headers,
    )
    session_id = start_res.json()["data"]["id"]
    q1_id = start_res.json()["data"]["current_question"]["id"]

    # Answer Question 1
    client.post(
        f"/api/ai-interview/{session_id}/answer",
        json={"question_id": q1_id, "answer_text": "I am an engineering student passionate about software design. During my final year project, I built a scalable learning platform.", "answer_mode": "text"},
        headers=headers,
    )

    # Fetch Question 2
    state_res = client.get(f"/api/ai-interview/{session_id}", headers=headers)
    q2_id = state_res.json()["data"]["current_question"]["id"]

    # Answer Question 2 (completes interview)
    ans2_res = client.post(
        f"/api/ai-interview/{session_id}/answer",
        json={"question_id": q2_id, "answer_text": "My primary strength is persistence and analytical debugging. I work diligently with teammates to meet challenging deadlines.", "answer_mode": "text"},
        headers=headers,
    )
    assert ans2_res.status_code == 200
    assert ans2_res.json()["data"]["is_interview_complete"] is True

    # Retrieve Final Report
    report_res = client.get(f"/api/ai-interview/{session_id}/report", headers=headers)
    assert report_res.status_code == 200
    report = report_res.json()["data"]

    assert report["interview_id"] == session_id
    assert report["overall_score"] > 0.0
    assert len(report["strengths"]) > 0
    assert len(report["improvement_areas"]) > 0
    assert len(report["questions_breakdown"]) == 2


# -------------------------------------------------------------
# 4. TEST STUDENT DATA ISOLATION & ACCESS CONTROL
# -------------------------------------------------------------
def test_student_data_isolation(client: TestClient, student_token: str, db_session: Session):
    """Test Student B cannot view or submit answers to Student A's interview."""
    headers_student_a = {"Authorization": f"Bearer {student_token}"}

    # Create Student B
    u_b = User(
        id="test-user-student-b",
        email="student.b@kvgce.edu.in",
        password_hash=hash_password("password123"),
        name="Student B",
        role=RoleEnum.STUDENT,
        is_active=True,
    )
    db_session.add(u_b)
    db_session.flush()
    std_prof_b = StudentProfile(
        id="test-prof-b",
        user_id=u_b.id,
        college_id="test-clg-kvg",
        branch="CSE",
        academic_year="3rd Year",
        section="A",
    )
    db_session.add(std_prof_b)
    db_session.commit()

    # Login as Student B
    login_b = client.post("/api/auth/login", json={"email": "student.b@kvgce.edu.in", "password": "password123"})
    token_b = login_b.json()["data"]["access_token"]
    headers_student_b = {"Authorization": f"Bearer {token_b}"}

    # Student A starts an interview
    start_res = client.post(
        "/api/ai-interview/start",
        json={"interview_category": "Technical", "subject": "Python", "total_questions": 2},
        headers=headers_student_a,
    )
    session_id_a = start_res.json()["data"]["id"]

    # Student B attempts to access Student A's session -> must return 403 Forbidden
    forbidden_res = client.get(f"/api/ai-interview/{session_id_a}", headers=headers_student_b)
    assert forbidden_res.status_code == 403


# -------------------------------------------------------------
# 5. TEST STUDENT INTERVIEW HISTORY RETRIEVAL
# -------------------------------------------------------------
def test_student_interview_history(client: TestClient, student_token: str):
    """Test paginated history retrieval for authenticated student."""
    headers = {"Authorization": f"Bearer {student_token}"}
    client.post(
        "/api/ai-interview/start",
        json={"interview_category": "Behavioral", "subject": "Behavioral", "total_questions": 1},
        headers=headers,
    )

    history_res = client.get("/api/ai-interview/history?page=1&limit=10", headers=headers)
    assert history_res.status_code == 200
    data = history_res.json()["data"]
    assert data["total"] >= 1
    assert len(data["items"]) >= 1
    assert data["items"][0]["interview_category"] in ["Technical", "HR", "Behavioral"]


# -------------------------------------------------------------
# 6. TEST QUESTION BANK MANAGEMENT & ADMIN ROLE
# -------------------------------------------------------------
def test_question_bank_search_and_admin_add(client: TestClient, student_token: str, faculty_token: str):
    """Test question bank search and role protection for adding questions."""
    # 1. Student can search verified questions
    search_res = client.get("/api/ai-interview/questions?category=Technical&subject=Python", headers={"Authorization": f"Bearer {student_token}"})
    assert search_res.status_code == 200
    assert len(search_res.json()["data"]) >= 1

    # 2. Student cannot add questions (403 Forbidden)
    add_payload = {
        "category": "Technical",
        "subject": "System Design",
        "question_text": "How do you design a rate limiter using token bucket algorithm in distributed systems?",
        "expected_concepts": ["token bucket", "Redis", "concurrency"],
    }
    forbidden_add = client.post("/api/ai-interview/questions", json=add_payload, headers={"Authorization": f"Bearer {student_token}"})
    assert forbidden_add.status_code == 403

    # 3. Faculty can add verified questions
    faculty_add = client.post("/api/ai-interview/questions", json=add_payload, headers={"Authorization": f"Bearer {faculty_token}"})
    assert faculty_add.status_code == 201
    assert faculty_add.json()["data"]["question_text"] == add_payload["question_text"]


# -------------------------------------------------------------
# 7. TEST VOICE PROCESSING: TTS & STT
# -------------------------------------------------------------
def test_tts_generation(client: TestClient, student_token: str):
    """Test Text-to-Speech synthesis returns structured playback metadata."""
    headers = {"Authorization": f"Bearer {student_token}"}
    tts_payload = {"text": "Explain the difference between mutable and immutable data types in Python.", "voice": "alloy"}
    res = client.post("/api/ai-interview/tts", json=tts_payload, headers=headers)
    assert res.status_code == 200
    data = res.json()["data"]
    assert data["success"] is True
    assert data["client_tts_ready"] is True
    assert "mutable" in data["text"]


def test_stt_transcription(client: TestClient, student_token: str):
    """Test Speech-to-Text audio upload validation and transcription."""
    headers = {"Authorization": f"Bearer {student_token}"}
    fake_audio_bytes = b"RIFF....WAVEfmt ....data...."

    files = {"file": ("answer.wav", fake_audio_bytes, "audio/wav")}
    res = client.post("/api/ai-interview/stt", files=files, headers=headers)
    assert res.status_code == 200
    data = res.json()["data"]
    assert data["success"] is True
    assert "transcript" in data
    assert data["words_per_minute"] > 0


def test_stt_unsupported_format_rejected(client: TestClient, student_token: str):
    """Test invalid audio format upload is rejected with 415 Unsupported Media Type."""
    headers = {"Authorization": f"Bearer {student_token}"}
    fake_exe = b"MZ\x90\x00\x03\x00\x00\x00"

    files = {"file": ("malicious.exe", fake_exe, "application/octet-stream")}
    res = client.post("/api/ai-interview/stt", files=files, headers=headers)
    assert res.status_code == 415


# -------------------------------------------------------------
# 8. TEST EDUCATIONAL KNOWLEDGE RETRIEVAL SERVICE
# -------------------------------------------------------------
def test_knowledge_retrieval_service(db_session: Session):
    """Test Wikipedia knowledge retrieval and offline graceful handling."""
    # Test normalization and retrieval
    info = KnowledgeRetrievalService.get_or_fetch_topic_knowledge(db_session, "Python (programming language)")
    # If network is available, it returns content; if offline, it returns None gracefully without crashing
    if info:
        assert "Wikipedia" in info["source_name"]
        assert len(info["content_summary"]) > 0
        assert "CC BY-SA" in info["attribution"]


# -------------------------------------------------------------
# 9. TEST 1,000+ WORD COMPREHENSIVE ANSWER ACCEPTANCE & VERIFICATION
# -------------------------------------------------------------
def test_submit_1000_word_comprehensive_answer(client: TestClient, student_token: str):
    """
    Test submitting a comprehensive 1,000+ word technical response.
    Verifies that the Python backend accepts, parses, and evaluates large architectural answers
    with high technical depth, completeness, and structure without truncation or 422 errors.
    """
    headers = {"Authorization": f"Bearer {student_token}"}
    start_res = client.post(
        "/api/ai-interview/start",
        json={"interview_category": "Technical", "subject": "Python", "difficulty": "Advanced", "total_questions": 2},
        headers=headers,
    )
    assert start_res.status_code == 201
    session_id = start_res.json()["data"]["id"]
    q1_id = start_res.json()["data"]["current_question"]["id"]

    # Build a comprehensive 1,000+ word technical architectural response
    paragraphs = [
        (
            "To design and implement a fault-tolerant, high-throughput distributed system in Python, "
            "we must examine the underlying architecture across multiple layers: memory layout, concurrency models, "
            "I/O multiplexing, and transactional consistency guarantees. In Python, memory management relies on "
            "reference counting coupled with a generational garbage collector designed to break cyclical dependencies. "
            "Understanding how objects are allocated on the private heap and how the Global Interpreter Lock (GIL) "
            "orchestrates thread execution is foundational when developing low-latency backend services."
        ),
        (
            "When dealing with CPU-bound processing, standard multithreading suffers from GIL contention, "
            "where only one native thread executes Python bytecode at any given moment. To bypass this bottleneck, "
            "we utilize multi-processing architectures through Python's multiprocessing module or distributed task "
            "queues like Celery backed by Redis or RabbitMQ. Each worker runs in an independent OS process with its "
            "own virtual memory address space and dedicated GIL, allowing linear horizontal scaling across multiple "
            "CPU cores. Data exchange between processes is orchestrated using inter-process communication (IPC) "
            "mechanisms, including shared memory buffers via multiprocessing.shared_memory or memory-mapped files (mmap)."
        ),
        (
            "For I/O-bound workflows, such as microservices communicating over HTTP or gRPC, cooperative multitasking "
            "via asyncio provides immense throughput advantages. Built upon an event loop that monitors file descriptors "
            "using kernel-level abstractions such as epoll on Linux, kqueue on BSD/macOS, or IOCP on Windows, "
            "asyncio permits thousands of concurrent network connections without the severe thread-switching overhead "
            "of pre-emptive threading. Coroutines defined with async and await yield control back to the event loop "
            "during socket I/O operations, achieving optimal CPU utilization and predictable low latency."
        ),
        (
            "Let us consider concrete implementation details. Below is an architectural implementation demonstrating "
            "asynchronous batch processing with semaphore-controlled concurrency and robust retry backoff:\n\n"
            "```python\n"
            "import asyncio\n"
            "import logging\n"
            "\n"
            "class DistributedBatchWorker:\n"
            "    def __init__(self, concurrency_limit: int = 50):\n"
            "        self.semaphore = asyncio.Semaphore(concurrency_limit)\n"
            "\n"
            "    async def process_task(self, task_id: int) -> dict:\n"
            "        async with self.semaphore:\n"
            "            for attempt in range(3):\n"
            "                try:\n"
            "                    # Simulate async non-blocking external API or database call\n"
            "                    await asyncio.sleep(0.01)\n"
            "                    return {'task_id': task_id, 'status': 'success'}\n"
            "                except Exception as exc:\n"
            "                    logging.warning(f'Task {task_id} failed attempt {attempt}: {exc}')\n"
            "                    await asyncio.sleep(2 ** attempt)\n"
            "            return {'task_id': task_id, 'status': 'failed'}\n"
            "```\n"
        ),
        (
            "Furthermore, transactional integrity and state persistence demand strict adherence to ACID principles "
            "(Atomicity, Consistency, Isolation, and Durability). When persisting records into relational databases "
            "such as PostgreSQL, we implement connection pooling via SQLAlchemy, configuring read replicas to offload "
            "heavy analytical queries while routing mutating writes to the primary cluster. For caching layers, "
            "we integrate Redis with cache-aside and write-through patterns, utilizing TTL (Time-To-Live) and LRU "
            "(Least Recently Used) eviction algorithms to eliminate cache stampedes and stale data reads."
        ),
        (
            "In terms of computational complexity and architectural trade-offs, we must analyze time and space bounds. "
            "While in-memory lookup maps operate with O(1) average time complexity, high memory consumption can trigger "
            "swapping or container eviction in Kubernetes environments. Therefore, Bloom filters and count-min sketches "
            "are deployed as space-efficient probabilistic data structures to test set membership in O(k) time using "
            "minimal RAM. For distributed synchronization, optimistic concurrency control (OCC) using version vectors "
            "or row timestamps is preferred over pessimistic two-phase locking (2PL) to prevent deadlock cascades."
        ),
        (
            "In conclusion, modern high-scale software engineering requires balancing algorithmic precision, asynchronous "
            "event-driven architecture, robust error boundaries, and comprehensive telemetry. By decomposing monolithic "
            "workloads into specialized worker pools, applying exponential backoff with jitter on network retries, and "
            "validating theoretical assumptions against production metrics, we build resilient, enterprise-grade software "
            "capable of serving millions of concurrent requests seamlessly."
        ),
    ]

    full_answer_text = "\n\n".join(paragraphs)
    # Replicate text sections to ensure it exceeds 1,000 words
    full_answer_text = full_answer_text + "\n\n" + full_answer_text
    word_count = len(full_answer_text.split())
    assert word_count >= 1000, f"Expected >1000 words, got {word_count}"

    # Submit 1,000+ word answer
    ans_payload = {
        "question_id": q1_id,
        "answer_text": full_answer_text,
        "answer_mode": "text",
    }
    ans_res = client.post(f"/api/ai-interview/{session_id}/answer", json=ans_payload, headers=headers)
    assert ans_res.status_code == 200, f"Submission failed: {ans_res.text}"
    ans_data = ans_res.json()["data"]

    # Verify score metrics reward depth, completeness, and structure
    assert ans_data["technical_score"] >= 7.0
    assert ans_data["completeness_score"] >= 8.5
    assert ans_data["clarity_score"] >= 8.0
    assert ans_data["communication_score"] >= 8.0
    assert ans_data["overall_score"] >= 75.0

    # Verify strengths reflect the comprehensive answer and code/trade-offs
    strengths_text = " ".join(ans_data["strengths"]).lower()
    assert "comprehensive" in strengths_text or "exhaustive" in strengths_text or "detailed" in strengths_text
    assert "outstanding" in ans_data["feedback"].lower() or "thorough" in ans_data["feedback"].lower() or "strong" in ans_data["feedback"].lower()

