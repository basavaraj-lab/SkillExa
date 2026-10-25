import pytest
from datetime import datetime, timedelta
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from backend.app.models.user import RoleEnum, User, StudentProfile
from backend.app.utils.security import create_access_token, hash_password


def test_schedule_interview_and_conflict_detection(
    client: TestClient,
    db_session: Session,
    faculty_token: str,
    student_token: str,
):
    # 1. Fetch the seeded student from db_session
    student = db_session.query(User).filter(User.email == "student.test@kvgce.edu.in").first()
    assert student is not None
    student_id = student.id

    # 2. Register second student to test unauthorized access
    reg_res = client.post(
        "/api/auth/register/student",
        json={
            "name": "Second Student",
            "email": "student2.test@kvgce.edu.in",
            "password": "password123",
            "branch": "ECE",
            "academic_year": "3rd Year",
            "section": "B",
        },
    )
    assert reg_res.status_code == 201

    login_res = client.post(
        "/api/auth/login",
        json={
            "email": "student2.test@kvgce.edu.in",
            "password": "password123",
        },
    )
    assert login_res.status_code == 200
    student2_token = login_res.json()["data"]["access_token"]

    future_time = (datetime.utcnow() + timedelta(days=2)).replace(minute=0, second=0, microsecond=0)

    # 3. Successful scheduling by faculty
    payload = {
        "student_id": student_id,
        "interview_category": "Technical Interview",
        "subject": "Full Stack React & FastAPI",
        "scheduled_at": future_time.isoformat(),
        "duration_minutes": 45,
        "instructions": "Be prepared with System Architecture & Database schema design.",
        "preparation_materials": "Review WebRTC and state management fundamentals.",
    }
    resp = client.post(
        "/api/live-interview/bookings",
        json=payload,
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert resp.status_code == 201
    data = resp.json()["data"]
    assert data["subject"] == "Full Stack React & FastAPI"
    assert data["student_name"] == "Test Student"
    assert data["booking_status"] == "Scheduled"
    assert data["secure_room_id"] is not None
    booking_id = data["id"]
    secure_room_id = data["secure_room_id"]

    # 4. Rejection if student tries to schedule
    bad_resp = client.post(
        "/api/live-interview/bookings",
        json=payload,
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert bad_resp.status_code == 403

    # 5. Conflict detection: teacher trying to book overlapping session
    conflict_payload = {
        "student_id": student_id,
        "interview_category": "HR Interview",
        "subject": "Culture Fit",
        "scheduled_at": (future_time + timedelta(minutes=15)).isoformat(),
        "duration_minutes": 30,
    }
    conflict_resp = client.post(
        "/api/live-interview/bookings",
        json=conflict_payload,
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert conflict_resp.status_code == 409
    err_body = conflict_resp.json()
    assert "Scheduling conflict detected" in err_body.get("message", err_body.get("detail", ""))

    # 6. View Bookings as Student & Teacher
    s_resp = client.get(
        "/api/live-interview/bookings",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert s_resp.status_code == 200
    assert len(s_resp.json()["data"]) >= 1

    f_resp = client.get(
        "/api/live-interview/bookings",
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert f_resp.status_code == 200
    assert len(f_resp.json()["data"]) >= 1

    # 7. Unauthorized student blocked from viewing this booking
    unauth_resp = client.get(
        f"/api/live-interview/bookings/{booking_id}",
        headers={"Authorization": f"Bearer {student2_token}"},
    )
    print("UNAUTH RESP JSON:", unauth_resp.json())
    assert unauth_resp.status_code == 403

    # 8. Room Join by authorized student
    join_resp = client.post(
        f"/api/live-interview/rooms/{secure_room_id}/join",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert join_resp.status_code == 200
    room_data = join_resp.json()["data"]
    assert room_data["current_user_role"] == "student"
    assert len(room_data["ice_servers"]) > 0

    # 9. Unauthorized student blocked from joining room
    bad_join = client.post(
        f"/api/live-interview/rooms/{secure_room_id}/join",
        headers={"Authorization": f"Bearer {student2_token}"},
    )
    assert bad_join.status_code == 403

    # 10. In-meeting chat
    msg_resp = client.post(
        f"/api/live-interview/rooms/{secure_room_id}/messages",
        json={"message": "Hello Professor, my video and audio are ready."},
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert msg_resp.status_code == 200
    assert msg_resp.json()["data"]["sender_name"] == "Test Student"

    # Get chat history
    get_msgs = client.get(
        f"/api/live-interview/rooms/{secure_room_id}/messages",
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert get_msgs.status_code == 200
    assert len(get_msgs.json()["data"]) >= 1

    # 11. Submit Evaluation Feedback by Teacher
    fb_payload = {
        "technical_score": 88.5,
        "communication_feedback": "Excellently articulated architectural decisions and tradeoffs.",
        "problem_solving_feedback": "Handled edge cases cleanly with strong reasoning.",
        "strengths": ["Clear communication", "Solid React & WebRTC knowledge", "Confident explanation"],
        "areas_for_improvement": ["Review database indexing best practices for large tables"],
        "teacher_comments": "Recommended for senior technical placement rounds.",
        "recommended_topics": ["Database Indexing", "Connection Pooling"],
    }
    fb_resp = client.post(
        f"/api/live-interview/bookings/{booking_id}/feedback",
        json=fb_payload,
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert fb_resp.status_code == 200
    fb_data = fb_resp.json()["data"]
    assert fb_data["technical_score"] == 88.5

    # 12. Student reads their completed feedback
    student_fb = client.get(
        f"/api/live-interview/bookings/{booking_id}/feedback",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert student_fb.status_code == 200
    assert student_fb.json()["data"]["technical_score"] == 88.5

    # 13. Unauthorized student blocked from reading feedback
    bad_fb = client.get(
        f"/api/live-interview/bookings/{booking_id}/feedback",
        headers={"Authorization": f"Bearer {student2_token}"},
    )
    assert bad_fb.status_code == 403


def test_booking_confirmation_cancellation_and_past_validation(
    client: TestClient,
    db_session: Session,
    faculty_token: str,
    student_token: str,
):
    student = db_session.query(User).filter(User.email == "student.test@kvgce.edu.in").first()
    student_id = student.id

    # 1. Past timestamp is rejected
    past_time = datetime.utcnow() - timedelta(days=1)
    past_resp = client.post(
        "/api/live-interview/bookings",
        json={
            "student_id": student_id,
            "interview_category": "Java Interview",
            "subject": "Java Core & Spring Boot",
            "scheduled_at": past_time.isoformat(),
            "duration_minutes": 30,
        },
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert past_resp.status_code == 400

    # 2. Future booking
    future_time = datetime.utcnow() + timedelta(days=5)
    create_resp = client.post(
        "/api/live-interview/bookings",
        json={
            "student_id": student_id,
            "interview_category": "DSA Interview",
            "subject": "Binary Search & Dynamic Programming",
            "scheduled_at": future_time.isoformat(),
            "duration_minutes": 60,
        },
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert create_resp.status_code == 201
    booking_id = create_resp.json()["data"]["id"]
    secure_room_id = create_resp.json()["data"]["secure_room_id"]

    # 3. Confirm booking
    conf_resp = client.post(
        f"/api/live-interview/bookings/{booking_id}/confirm",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert conf_resp.status_code == 200
    assert conf_resp.json()["data"]["booking_status"] == "Confirmed"

    # 4. Cancel booking
    canc_resp = client.post(
        f"/api/live-interview/bookings/{booking_id}/cancel",
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert canc_resp.status_code == 200
    assert canc_resp.json()["data"]["booking_status"] == "Cancelled"

    # 5. Cannot confirm after cancellation
    bad_conf = client.post(
        f"/api/live-interview/bookings/{booking_id}/confirm",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert bad_conf.status_code == 400


def test_webrtc_websocket_signaling(
    client: TestClient,
    db_session: Session,
    faculty_token: str,
    student_token: str,
):
    student = db_session.query(User).filter(User.email == "student.test@kvgce.edu.in").first()
    future_time = datetime.utcnow() + timedelta(days=7)

    # 1. Schedule interview
    create_resp = client.post(
        "/api/live-interview/bookings",
        json={
            "student_id": student.id,
            "interview_category": "SQL and DBMS Interview",
            "subject": "ACID Properties & Normalization",
            "scheduled_at": future_time.isoformat(),
            "duration_minutes": 45,
        },
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert create_resp.status_code == 201
    secure_room_id = create_resp.json()["data"]["secure_room_id"]

    # 2. Connect via WebSocket signaling
    with client.websocket_connect(f"/api/live-interview/ws/{secure_room_id}?token={faculty_token}") as ws:
        # Should receive room-joined welcome payload
        welcome = ws.receive_json()
        assert welcome["type"] == "room-joined"
        assert welcome["room_id"] == secure_room_id

        # Send media state update
        ws.send_text('{"type": "media-state", "mic_on": false, "cam_on": true}')

        # Send chat message via WebSocket
        ws.send_text('{"type": "chat-message", "message": "Testing real-time WebRTC chat"}')
        chat_broadcast = ws.receive_json()
        assert chat_broadcast["type"] == "chat-message"
        assert chat_broadcast["message"] == "Testing real-time WebRTC chat"


def test_reschedule_validation_admit_and_end_interview(
    client: TestClient,
    db_session: Session,
    faculty_token: str,
    student_token: str,
):
    student = db_session.query(User).filter(User.email == "student.test@kvgce.edu.in").first()
    future_time = datetime.utcnow() + timedelta(days=8)

    # 1. Faculty schedules interview
    create_resp = client.post(
        "/api/live-interview/bookings",
        json={
            "student_id": student.id,
            "interview_category": "DSA Interview",
            "subject": "Graph Algorithms & Dynamic Programming",
            "scheduled_at": future_time.isoformat(),
            "duration_minutes": 60,
        },
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert create_resp.status_code == 201
    booking_id = create_resp.json()["data"]["id"]
    secure_room_id = create_resp.json()["data"]["secure_room_id"]

    # 2. Validate room code
    val_res = client.get(
        f"/api/live-interview/validate-room/{secure_room_id}",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert val_res.status_code == 200
    assert val_res.json()["data"]["secure_room_id"] == secure_room_id

    # Invalid room code returns 404
    bad_val = client.get(
        "/api/live-interview/validate-room/NON-EXISTENT-CODE",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert bad_val.status_code == 404

    # 3. Reschedule booking
    resched_time = (future_time + timedelta(hours=3)).isoformat()
    # Student cannot reschedule (403)
    bad_resched = client.post(
        f"/api/live-interview/bookings/{booking_id}/reschedule",
        json={"scheduled_at": resched_time, "duration_minutes": 90},
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert bad_resched.status_code == 403

    # Faculty can reschedule
    good_resched = client.post(
        f"/api/live-interview/bookings/{booking_id}/reschedule",
        json={"scheduled_at": resched_time, "duration_minutes": 90},
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert good_resched.status_code == 200
    assert good_resched.json()["data"]["duration_minutes"] == 90

    # 4. Admit student
    # Student cannot admit (403)
    bad_admit = client.post(
        f"/api/live-interview/rooms/{secure_room_id}/admit",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert bad_admit.status_code == 403

    # Faculty can admit
    good_admit = client.post(
        f"/api/live-interview/rooms/{secure_room_id}/admit",
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert good_admit.status_code == 200

    # 5. End interview for everyone
    # Student cannot end interview (403)
    bad_end = client.post(
        f"/api/live-interview/rooms/{secure_room_id}/end",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert bad_end.status_code == 403

    # Faculty ends interview
    good_end = client.post(
        f"/api/live-interview/rooms/{secure_room_id}/end",
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert good_end.status_code == 200
    assert good_end.json()["data"]["booking_status"] == "Completed"

    # Completed room cannot be joined (400)
    join_after_end = client.post(
        f"/api/live-interview/rooms/{secure_room_id}/join",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert join_after_end.status_code == 400


