from datetime import datetime, timedelta


def test_interview_scheduling_and_multi_criterion_evaluation(client, faculty_token, student_token):
    # 1. Schedule Interview
    scheduled_time = (datetime.utcnow() + timedelta(days=2)).isoformat()
    sched_res = client.post(
        "/api/interviews",
        headers={"Authorization": f"Bearer {faculty_token}"},
        json={
            "student_id": "test-std-prof-1",
            "title": "Embedded Systems Core Viva",
            "interview_type": "Engineering Viva",
            "subject_or_role": "Embedded Systems",
            "scheduled_at": scheduled_time,
            "duration_minutes": 30,
            "questions": [
                {"question_text": "Explain differences between Cortex-M3 and Cortex-M4."},
                {"question_text": "How is ISR context saved onto the stack?"},
            ],
        },
    )
    assert sched_res.status_code == 201
    int_data = sched_res.json()["data"]
    interview_id = int_data["id"]
    assert int_data["room_id"] is not None

    # 2. Faculty conducts and evaluates interview
    eval_res = client.post(
        f"/api/interviews/{interview_id}/evaluate",
        headers={"Authorization": f"Bearer {faculty_token}"},
        json={
            "technical_score": 90.0,
            "problem_solving_score": 85.0,
            "communication_score": 92.0,
            "confidence_score": 88.0,
            "strengths": ["Strong understanding of NVIC vectoring", "Clear technical communication"],
            "weaknesses": ["Minor hesitation on floating point registers"],
            "suggestions": ["Review FPU lazy stacking mechanisms"],
            "overall_feedback": "Outstanding viva performance! Well prepared for embedded core placement roles.",
        },
    )
    assert eval_res.status_code == 200
    res_data = eval_res.json()["data"]
    assert res_data["overall_score"] > 80.0
    assert len(res_data["strengths"]) == 2
