def test_student_registration_and_login(client):
    # 1. Register new student
    reg_res = client.post(
        "/api/auth/register/student",
        json={
            "name": "Arun Kumar",
            "email": "arun.kumar@kvgce.edu.in",
            "password": "securepassword123",
            "branch": "CSE",
            "academic_year": "2nd Year",
            "section": "B",
            "target_exam": "GATE",
        },
    )
    assert reg_res.status_code == 201
    assert reg_res.json()["success"] is True
    assert reg_res.json()["data"]["email"] == "arun.kumar@kvgce.edu.in"

    # 2. Login with registered student
    login_res = client.post(
        "/api/auth/login",
        json={
            "email": "arun.kumar@kvgce.edu.in",
            "password": "securepassword123",
        },
    )
    assert login_res.status_code == 200
    token_data = login_res.json()["data"]
    assert "access_token" in token_data
    assert token_data["user"]["role"] == "student"

    # 3. Access current user /api/auth/me with Bearer token
    token = token_data["access_token"]
    me_res = client.get(
        "/api/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert me_res.status_code == 200
    assert me_res.json()["data"]["email"] == "arun.kumar@kvgce.edu.in"


def test_faculty_registration_and_role_protection(client):
    # 1. Register Faculty
    reg_res = client.post(
        "/api/auth/register/faculty",
        json={
            "name": "Dr. Maya Sharma",
            "email": "dr.maya@kvgce.edu.in",
            "password": "facultyPassword123",
            "department": "ECE",
            "designation": "Assistant Professor",
            "subjects_taught": ["VLSI", "Digital Electronics"],
        },
    )
    assert reg_res.status_code == 201
    assert reg_res.json()["data"]["department"] == "ECE"

    # 2. Login
    login_res = client.post(
        "/api/auth/login",
        json={"email": "dr.maya@kvgce.edu.in", "password": "facultyPassword123"},
    )
    assert login_res.status_code == 200
    token = login_res.json()["data"]["access_token"]

    # 3. Access faculty dashboard stats
    fac_res = client.get(
        "/api/faculty/dashboard-stats",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert fac_res.status_code == 200
    assert fac_res.json()["success"] is True


def test_invalid_login_credentials(client):
    res = client.post(
        "/api/auth/login",
        json={"email": "nonexistent@kvgce.edu.in", "password": "wrongpassword"},
    )
    assert res.status_code == 401
    assert res.json()["success"] is False
    assert res.json()["code"] == "UNAUTHORIZED"
