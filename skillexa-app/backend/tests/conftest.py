import os
import sys
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Add repository root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from backend.app.database import Base
from backend.app.dependencies.db import get_db
from backend.app.main import app
from backend.app.models.college import College
from backend.app.models.user import (
    FacultyProfile,
    RoleEnum,
    StudentProfile,
    User,
    VerificationStatusEnum,
)
from backend.app.utils.security import hash_password

# In-Memory SQLite test database
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """Create a fresh in-memory database for each test."""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        # Seed test college
        test_college = College(
            id="test-clg-kvg",
            code="KVG001",
            name="KVG College of Engineering",
            city="Sullia",
            state="Karnataka",
            is_verified=True,
        )
        db.add(test_college)

        # Seed test faculty
        u_fac = User(
            id="test-user-fac-1",
            email="prof.test@kvgce.edu.in",
            password_hash=hash_password("password123"),
            name="Prof. Test Faculty",
            role=RoleEnum.FACULTY,
            is_active=True,
        )
        db.add(u_fac)
        db.flush()

        fac_prof = FacultyProfile(
            id="test-fac-prof-1",
            user_id=u_fac.id,
            college_id=test_college.id,
            department="ECE",
            designation="Associate Professor",
            subjects_taught=["Embedded Systems", "Programming in C"],
            verification_status=VerificationStatusEnum.APPROVED,
        )
        db.add(fac_prof)

        # Seed test student
        u_std = User(
            id="test-user-std-1",
            email="student.test@kvgce.edu.in",
            password_hash=hash_password("password123"),
            name="Test Student",
            role=RoleEnum.STUDENT,
            is_active=True,
        )
        db.add(u_std)
        db.flush()

        std_prof = StudentProfile(
            id="test-std-prof-1",
            user_id=u_std.id,
            college_id=test_college.id,
            branch="ECE",
            academic_year="3rd Year",
            section="A",
        )
        db.add(std_prof)
        db.commit()

        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """FastAPI TestClient with overridden database dependency."""
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def faculty_token(client):
    """Login as test faculty and return JWT bearer token."""
    res = client.post("/api/auth/login", json={"email": "prof.test@kvgce.edu.in", "password": "password123"})
    assert res.status_code == 200
    return res.json()["data"]["access_token"]


@pytest.fixture
def student_token(client):
    """Login as test student and return JWT bearer token."""
    res = client.post("/api/auth/login", json={"email": "student.test@kvgce.edu.in", "password": "password123"})
    assert res.status_code == 200
    return res.json()["data"]["access_token"]
