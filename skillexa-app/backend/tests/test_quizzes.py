def test_quiz_creation_attempt_and_scoring(client, faculty_token, student_token):
    # 1. Faculty creates quiz with 2 questions
    create_quiz_res = client.post(
        "/api/faculty/quizzes",
        headers={"Authorization": f"Bearer {faculty_token}"},
        json={
            "title": "Python Closures Assessment",
            "section": "programming",
            "subject": "Programming in Python",
            "topic": "Functions & Scope",
            "duration_minutes": 10,
            "total_marks": 4.0,
            "negative_marks": 0.5,
            "visibility": "college",
            "published": True,
            "questions": [
                {
                    "section": "programming",
                    "subject": "Programming in Python",
                    "topic": "Functions & Scope",
                    "question_text": "Which rule dictates variable scope resolution order in Python?",
                    "options": ["LEGB Rule", "FIFO Rule", "BODMAS Rule", "LIFO Rule"],
                    "correct_answer": 0,
                    "explanation": "LEGB stands for Local, Enclosing, Global, Built-in.",
                    "marks": 2.0,
                    "negative_marks": 0.5,
                },
                {
                    "section": "programming",
                    "subject": "Programming in Python",
                    "topic": "Functions & Scope",
                    "question_text": "What keyword defines an anonymous inline function in Python?",
                    "options": ["def", "lambda", "inline", "func"],
                    "correct_answer": 1,
                    "explanation": "lambda creates lightweight anonymous functions.",
                    "marks": 2.0,
                    "negative_marks": 0.5,
                },
            ],
        },
    )
    assert create_quiz_res.status_code == 201
    quiz_id = create_quiz_res.json()["data"]["id"]

    # 2. Student starts quiz attempt (Verify NO correct answers are leaked)
    start_res = client.post(
        f"/api/quizzes/{quiz_id}/start",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert start_res.status_code == 200
    start_data = start_res.json()["data"]
    attempt_id = start_data["attempt_id"]
    questions = start_data["questions"]
    assert len(questions) == 2
    for q in questions:
        assert "correct_answer" not in q
        assert "explanation" not in q

    q1_id = questions[0]["id"]
    q2_id = questions[1]["id"]

    # 3. Student submits attempt: Q1 Correct (0), Q2 Wrong (0 instead of 1)
    submit_res = client.post(
        "/api/quizzes/submit",
        headers={"Authorization": f"Bearer {student_token}"},
        json={
            "attempt_id": attempt_id,
            "time_taken_seconds": 120,
            "answers": {
                q1_id: 0,  # Correct (+2.0)
                q2_id: 0,  # Wrong (-0.5)
            },
        },
    )
    assert submit_res.status_code == 200
    result_data = submit_res.json()["data"]
    assert result_data["correct_count"] == 1
    assert result_data["wrong_count"] == 1
    assert result_data["score"] == 1.5  # 2.0 - 0.5 = 1.5
    assert result_data["accuracy_percentage"] == 50.0
    assert len(result_data["breakdown"]) == 2
