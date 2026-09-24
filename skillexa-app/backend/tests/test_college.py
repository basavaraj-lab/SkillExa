def test_my_college_workspace_targeting(client, faculty_token, student_token):
    # 1. Faculty posts department announcement for ECE
    ann_res = client.post(
        "/api/faculty/announcements",
        headers={"Authorization": f"Bearer {faculty_token}"},
        json={
            "title": "ECE Embedded Lab Submissions",
            "content": "Final project report submission due on Monday.",
            "priority": "HIGH",
            "is_pinned": True,
            "target_departments": ["ECE"],
            "target_years": ["3rd Year"],
            "target_sections": ["A"],
        },
    )
    assert ann_res.status_code == 201

    # 2. Student (ECE 3rd Year A) opens My College workspace
    workspace_res = client.get(
        "/api/student/my-college",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert workspace_res.status_code == 200
    data = workspace_res.json()["data"]
    assert data["college"]["name"] == "KVG College of Engineering"
    assert len(data["announcements"]) == 1
    assert data["announcements"][0]["title"] == "ECE Embedded Lab Submissions"
