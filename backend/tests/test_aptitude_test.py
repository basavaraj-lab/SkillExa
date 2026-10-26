import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.models.user import RoleEnum, User
from backend.app.services.auth_service import AuthService
from backend.app.services.llm_aptitude_generator import LLMAptitudeGenerator


from backend.app.models.user import RoleEnum, User
from backend.app.utils.security import create_access_token, hash_password


@pytest.fixture
def student_auth_headers(student_token):
    return {"Authorization": f"Bearer {student_token}"}


@pytest.fixture
def other_student_headers(db_session):
    user = db_session.query(User).filter(User.email == "other_student@kvgce.edu.in").first()
    if not user:
        user = User(
            id="test-user-other-std",
            email="other_student@kvgce.edu.in",
            password_hash=hash_password("password123"),
            name="Other Student",
            role=RoleEnum.STUDENT,
            is_active=True,
        )
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)

    token = create_access_token(subject=user.id, claims={"role": user.role.value})
    return {"Authorization": f"Bearer {token}"}


def test_get_aptitude_categories(client):
    res = client.get("/api/aptitude/categories")
    assert res.status_code == 200
    data = res.json()["data"]
    assert "Quantitative Aptitude" in data["categories"]
    assert "Logical Reasoning" in data["categories"]
    assert "Verbal Ability" in data["categories"]
    assert "Data Interpretation" in data["categories"]
    assert len(data["categories"]["Quantitative Aptitude"]) >= 10
    assert "Easy" in data["difficulties"]
    assert "Intermediate" in data["difficulties"]
    assert "Advanced" in data["difficulties"]


def test_generate_10_easy_quantitative_questions(client, student_auth_headers):
    res = client.post(
        "/api/aptitude/attempts",
        json={
            "category": "Quantitative Aptitude",
            "topic": "Percentages",
            "difficulty": "Easy",
            "question_count": 10,
            "test_mode": "quick",
        },
        headers=student_auth_headers,
    )
    assert res.status_code == 201
    data = res.json()["data"]
    assert data["question_count"] == 10
    assert len(data["questions"]) == 10
    assert data["status"] == "in_progress"

    # CRITICAL: Verify answers and explanations are HIDDEN from candidate while test is active
    for q in data["questions"]:
        assert "correct_answer" not in q
        assert "explanation" not in q
        assert len(q["options"]) == 4
        opt_ids = [opt["id"] for opt in q["options"]]
        assert set(opt_ids) == {"A", "B", "C", "D"}


def test_generate_20_intermediate_logical_reasoning_questions(client, student_auth_headers):
    res = client.post(
        "/api/aptitude/attempts",
        json={
            "category": "Logical Reasoning",
            "topic": "Mixed Topics",
            "difficulty": "Intermediate",
            "question_count": 20,
            "test_mode": "standard",
        },
        headers=student_auth_headers,
    )
    assert res.status_code == 201
    data = res.json()["data"]
    assert data["question_count"] == 20
    assert len(data["questions"]) == 20
    assert data["status"] == "in_progress"


def test_generate_30_advanced_mixed_aptitude_questions(client, student_auth_headers):
    res = client.post(
        "/api/aptitude/attempts",
        json={
            "category": "Mixed Aptitude",
            "topic": "Mixed Topics",
            "difficulty": "Advanced",
            "question_count": 30,
            "test_mode": "full",
        },
        headers=student_auth_headers,
    )
    assert res.status_code == 201
    data = res.json()["data"]
    assert data["question_count"] == 30
    assert len(data["questions"]) == 30


def test_refresh_preserves_active_attempt_and_responses(client, student_auth_headers):
    # 1. Start an attempt
    start_res = client.post(
        "/api/aptitude/attempts",
        json={
            "category": "Quantitative Aptitude",
            "topic": "Time and Work",
            "difficulty": "Intermediate",
            "question_count": 5,
            "test_mode": "custom",
        },
        headers=student_auth_headers,
    )
    attempt_id = start_res.json()["data"]["attempt_id"]
    first_q_id = start_res.json()["data"]["questions"][0]["id"]

    # 2. Save an answer
    save_res = client.put(
        f"/api/aptitude/attempts/{attempt_id}/save-response",
        json={"question_id": first_q_id, "selected_option": "B", "time_spent_seconds": 25},
        headers=student_auth_headers,
    )
    assert save_res.status_code == 200

    # 3. Simulate page refresh / re-fetching the attempt
    get_res = client.get(
        f"/api/aptitude/attempts/{attempt_id}",
        headers=student_auth_headers,
    )
    assert get_res.status_code == 200
    get_data = get_res.json()["data"]
    assert get_data["attempt_id"] == attempt_id
    assert get_data["status"] == "in_progress"
    assert get_data["saved_responses"][first_q_id] == "B"
    # Answers still hidden
    for q in get_data["questions"]:
        assert "correct_answer" not in q
        assert "explanation" not in q


def test_submit_test_scoring_and_negative_marking(client, student_auth_headers):
    # 1. Create a 5-question test
    res = client.post(
        "/api/aptitude/attempts",
        json={
            "category": "Quantitative Aptitude",
            "topic": "Percentages",
            "difficulty": "Easy",
            "question_count": 5,
        },
        headers=student_auth_headers,
    )
    attempt_data = res.json()["data"]
    attempt_id = attempt_data["attempt_id"]
    questions = attempt_data["questions"]

    # We submit answers for Q0 (we don't know correct yet), Q1, etc.
    # Submit 2 answers, leave 3 unattempted
    submit_res = client.post(
        f"/api/aptitude/attempts/{attempt_id}/submit",
        json={
            "responses": {
                questions[0]["id"]: "A",
                questions[1]["id"]: "B",
            },
            "time_spent_seconds": 120,
        },
        headers=student_auth_headers,
    )
    assert submit_res.status_code == 200
    report = submit_res.json()["data"]
    assert report["attempt_id"] == attempt_id
    assert report["question_count"] == 5
    assert report["correct_count"] + report["incorrect_count"] + report["unattempted_count"] == 5
    assert report["unattempted_count"] == 3
    assert report["time_spent_seconds"] == 120

    # AFTER SUBMISSION: correct answers and explanations ARE present!
    for q in report["questions"]:
        assert "correct_answer" in q
        assert "explanation" in q
        assert q["correct_answer"] in ("A", "B", "C", "D")
        assert len(q["explanation"]) > 5

    # Negative marking verification: incorrect questions deduct 0.25
    expected_negative = report["incorrect_count"] * 0.25
    assert report["total_negative_marks"] == expected_negative


def test_student_isolation_cannot_access_others_attempt(client, student_auth_headers, other_student_headers):
    # Student 1 creates attempt
    res = client.post(
        "/api/aptitude/attempts",
        json={"category": "Quantitative Aptitude", "question_count": 5},
        headers=student_auth_headers,
    )
    attempt_id = res.json()["data"]["attempt_id"]

    # Student 2 tries to access Student 1's attempt -> 403 Forbidden
    other_get = client.get(
        f"/api/aptitude/attempts/{attempt_id}",
        headers=other_student_headers,
    )
    assert other_get.status_code == 403


def test_aptitude_history(client, student_auth_headers):
    # Ensure an attempt exists
    client.post(
        "/api/aptitude/attempts",
        json={"category": "Quantitative Aptitude", "question_count": 5},
        headers=student_auth_headers,
    )
    res = client.get(
        "/api/aptitude/history",
        headers=student_auth_headers,
    )
    assert res.status_code == 200
    history = res.json()["data"]
    assert isinstance(history, list)
    assert len(history) >= 1
