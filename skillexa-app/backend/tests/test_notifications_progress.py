def test_notifications_lifecycle(client, student_token):
    # 1. Fetch student notifications
    notifs_res = client.get(
        "/api/notifications",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert notifs_res.status_code == 200
    notifs = notifs_res.json()["data"]

    # 2. Mark all as read
    read_all_res = client.post(
        "/api/notifications/read-all",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert read_all_res.status_code == 200
    assert read_all_res.json()["data"]["all_read"] is True


def test_student_progress_summary(client, student_token):
    res = client.get(
        "/api/progress/summary",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert res.status_code == 200
    data = res.json()["data"]
    assert "overall_score" in data
    assert "quiz_accuracy" in data
    assert "dsa_progress_percentage" in data
