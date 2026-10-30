import uuid
from typing import Optional, Tuple
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.app.models.college import College
from backend.app.models.user import (
    FacultyProfile,
    RoleEnum,
    StudentProfile,
    User,
    VerificationStatusEnum,
)
from backend.app.schemas.auth import (
    GoogleLoginRequest,
    LoginRequest,
    RegisterFacultyRequest,
    RegisterStudentRequest,
    TokenResponse,
)
from backend.app.utils.security import (
    create_access_token,
    hash_password,
    verify_password,
)


class AuthService:
    @staticmethod
    def register_student(db: Session, req: RegisterStudentRequest) -> Tuple[User, StudentProfile]:
        # 1. Check existing email
        if db.query(User).filter(User.email == req.email.lower()).first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An account with this email already exists.",
            )

        # 2. Resolve college if provided
        college_id = req.college_id
        if college_id:
            college = db.query(College).filter((College.id == college_id) | (College.code == college_id)).first()
            if college:
                college_id = college.id

        # 3. Create User
        user = User(
            email=req.email.lower(),
            password_hash=hash_password(req.password),
            name=req.name.strip(),
            role=RoleEnum.STUDENT,
            is_active=True,
        )
        db.add(user)
        db.flush()

        # 4. Create Student Profile
        student_profile = StudentProfile(
            user_id=user.id,
            college_id=college_id,
            branch=req.branch.upper().strip(),
            academic_year=req.academic_year.strip(),
            section=req.section.upper().strip(),
            roll_number=req.roll_number.strip() if req.roll_number else None,
            phone=req.phone.strip() if req.phone else None,
            target_exam=req.target_exam or "Placement",
        )
        db.add(student_profile)
        db.commit()
        db.refresh(user)
        db.refresh(student_profile)

        # Cross-platform sync: Ensure competitive track has this unified profile under the same Gmail
        try:
            AuthService._sync_to_competitive_db({
                "name": user.name,
                "email": user.email,
                "phone": student_profile.phone,
                "branch": student_profile.branch,
                "academic_year": student_profile.academic_year,
                "section": student_profile.section,
                "roll_number": student_profile.roll_number,
                "target_exam": student_profile.target_exam,
                "role": "student",
            })
        except Exception:
            pass

        return user, student_profile

    @staticmethod
    def register_faculty(db: Session, req: RegisterFacultyRequest) -> Tuple[User, FacultyProfile]:
        # 1. Check existing email
        if db.query(User).filter(User.email == req.email.lower()).first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An account with this email already exists.",
            )

        # 2. Resolve college
        college_id = req.college_id
        if college_id:
            college = db.query(College).filter((College.id == college_id) | (College.code == college_id)).first()
            if college:
                college_id = college.id

        # 3. Create User
        user = User(
            email=req.email.lower(),
            password_hash=hash_password(req.password),
            name=req.name.strip(),
            role=RoleEnum.FACULTY,
            is_active=True,
        )
        db.add(user)
        db.flush()

        # 4. Create Faculty Profile (default status: PENDING unless configured)
        faculty_profile = FacultyProfile(
            user_id=user.id,
            college_id=college_id,
            department=req.department.upper().strip(),
            designation=req.designation.strip(),
            office_room=req.office_room.strip() if req.office_room else None,
            subjects_taught=req.subjects_taught or [],
            verification_status=VerificationStatusEnum.APPROVED,  # Default approved for smooth seed/demo flow
            bio=req.bio,
        )
        db.add(faculty_profile)
        db.commit()
        db.refresh(user)
        db.refresh(faculty_profile)
        return user, faculty_profile

    @staticmethod
    def login(db: Session, req: LoginRequest) -> TokenResponse:
        user = db.query(User).filter(User.email == req.email.lower()).first()
        if not user or not verify_password(req.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Your account has been deactivated.",
            )

        # Generate JWT
        token = create_access_token(
            subject=user.id,
            claims={
                "email": user.email,
                "name": user.name,
                "role": user.role.value,
            },
        )

        user_info = {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "role": user.role.value,
        }

        if user.role == RoleEnum.STUDENT and user.student_profile:
            user_info["student_profile"] = {
                "id": user.student_profile.id,
                "college_id": user.student_profile.college_id,
                "branch": user.student_profile.branch,
                "academic_year": user.student_profile.academic_year,
                "section": user.student_profile.section,
            }
            try:
                AuthService._sync_to_competitive_db({
                    "name": user.name,
                    "email": user.email,
                    "phone": user.student_profile.phone,
                    "branch": user.student_profile.branch,
                    "academic_year": user.student_profile.academic_year,
                    "section": user.student_profile.section,
                    "roll_number": user.student_profile.roll_number,
                    "target_exam": user.student_profile.target_exam,
                    "role": "student",
                })
            except Exception:
                pass
        elif user.role == RoleEnum.FACULTY and user.faculty_profile:
            user_info["faculty_profile"] = {
                "id": user.faculty_profile.id,
                "college_id": user.faculty_profile.college_id,
                "department": user.faculty_profile.department,
                "designation": user.faculty_profile.designation,
                "verification_status": user.faculty_profile.verification_status.value,
            }

        return TokenResponse(
            access_token=token,
            token_type="bearer",
            expires_in_minutes=1440,
            user=user_info,
        )

    @staticmethod
    def google_login(db: Session, req: GoogleLoginRequest) -> TokenResponse:
        email_clean = req.email.lower().strip()
        user = db.query(User).filter(User.email == email_clean).first()

        if not user:
            # New account: resolve role based on explicit role hint or if email has faculty/prof/dr, or default to student
            is_faculty_hint = (
                (req.role and req.role.lower() in ["faculty", "admin", "teacher", "lecturer"])
                or "faculty" in email_clean
                or "prof" in email_clean
                or email_clean.startswith("dr.")
            )
            assigned_role = RoleEnum.FACULTY if is_faculty_hint else RoleEnum.STUDENT
            user_name = req.name.strip() if req.name and req.name.strip() else email_clean.split("@")[0].capitalize()
            user = User(
                email=email_clean,
                password_hash=hash_password(uuid.uuid4().hex),
                name=user_name,
                role=assigned_role,
                is_active=True,
                avatar=req.avatar,
            )
            db.add(user)
            db.flush()

            # Resolve default college
            first_college = db.query(College).first()
            college_id = first_college.id if first_college else "clg-kvg"

            if assigned_role == RoleEnum.STUDENT:
                student_profile = StudentProfile(
                    user_id=user.id,
                    college_id=college_id,
                    branch="ECE",
                    academic_year="3rd Year",
                    section="A",
                    target_exam="Placement",
                )
                db.add(student_profile)
            else:
                faculty_profile = FacultyProfile(
                    user_id=user.id,
                    college_id=college_id,
                    department="ECE",
                    designation="Professor & HOD",
                    subjects_taught=["Embedded Systems", "VLSI", "Programming in C"],
                    verification_status=VerificationStatusEnum.APPROVED,
                )
                db.add(faculty_profile)

            db.commit()
            db.refresh(user)
        else:
            # Existing user: Preserve role, but upgrade if email/hint explicitly indicates faculty
            is_faculty_hint = (
                (req.role and req.role.lower() in ["faculty", "admin", "teacher", "lecturer"])
                or "faculty" in email_clean
                or "prof" in email_clean
                or email_clean.startswith("dr.")
            )
            updated = False
            if is_faculty_hint and user.role != RoleEnum.FACULTY:
                user.role = RoleEnum.FACULTY
                if not user.faculty_profile:
                    first_college = db.query(College).first()
                    college_id = first_college.id if first_college else "0f669a91-5c8d-4304-a815-818bde05e996"
                    user.faculty_profile = FacultyProfile(
                        user_id=user.id,
                        college_id=college_id,
                        department="ECE",
                        designation="Professor & HOD",
                        subjects_taught=["Embedded Systems", "VLSI", "Programming in C"],
                        verification_status=VerificationStatusEnum.APPROVED,
                    )
                    db.add(user.faculty_profile)
                updated = True

            if req.name and req.name.strip() and (not user.name or user.name in ["Scholar", "Student", "Learner", "faculty"]):
                user.name = req.name.strip()
                updated = True
            if req.avatar and not user.avatar:
                user.avatar = req.avatar
                updated = True
            if updated:
                db.commit()
                db.refresh(user)

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Your account has been deactivated.",
            )

        # Generate JWT with verified user role from database
        token = create_access_token(
            subject=user.id,
            claims={
                "email": user.email,
                "name": user.name,
                "role": user.role.value,
            },
        )

        college_name = "KVG College of Engineering"
        user_info = {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "role": user.role.value,
            "college_name": college_name,
        }

        if user.role == RoleEnum.STUDENT and user.student_profile:
            if user.student_profile.college:
                user_info["college_name"] = user.student_profile.college.name
            user_info["student_profile"] = {
                "id": user.student_profile.id,
                "college_id": user.student_profile.college_id,
                "college_name": user_info["college_name"],
                "branch": user.student_profile.branch,
                "academic_year": user.student_profile.academic_year,
                "section": user.student_profile.section,
            }
            try:
                AuthService._sync_to_competitive_db({
                    "name": user.name,
                    "email": user.email,
                    "phone": user.student_profile.phone,
                    "branch": user.student_profile.branch,
                    "academic_year": user.student_profile.academic_year,
                    "section": user.student_profile.section,
                    "roll_number": user.student_profile.roll_number,
                    "target_exam": user.student_profile.target_exam,
                    "role": "student",
                })
            except Exception:
                pass
        elif user.role in [RoleEnum.FACULTY, RoleEnum.COLLEGE_ADMIN] and user.faculty_profile:
            if user.faculty_profile.college:
                user_info["college_name"] = user.faculty_profile.college.name
            user_info["faculty_profile"] = {
                "id": user.faculty_profile.id,
                "college_id": user.faculty_profile.college_id,
                "college_name": user_info["college_name"],
                "department": user.faculty_profile.department,
                "designation": user.faculty_profile.designation,
                "verification_status": user.faculty_profile.verification_status.value,
            }

        return TokenResponse(
            access_token=token,
            token_type="bearer",
            expires_in_minutes=1440,
            user=user_info,
        )

    @staticmethod
    def _sync_to_competitive_db(user_data: dict):
        """
        Synchronizes the student profile across SkillExa Engineering & Competitive tracks.
        Ensures both tracks recognize the same Gmail account and exact profile details.
        """
        import json, os
        from datetime import datetime

        candidate_paths = [
            os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../competative-skillexa/server/data/skillexa.json")),
            os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../competative-skillexa/server/data/skillexa.json")),
        ]
        db_path = next((p for p in candidate_paths if os.path.exists(p)), None)
        if not db_path:
            return

        with open(db_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        users = data.get("users", [])
        email = user_data["email"].lower().strip()
        existing = next((u for u in users if u.get("email", "").lower() == email), None)

        education = " • ".join(
            filter(
                None,
                [
                    user_data.get("branch"),
                    user_data.get("academic_year"),
                    "KVG College of Engineering",
                ],
            )
        ) or "Engineering & Competitive Track"

        if existing:
            existing["name"] = user_data.get("name", existing.get("name"))
            if user_data.get("phone"):
                existing["phone"] = user_data["phone"]
            existing["education"] = education
            existing["branch"] = user_data.get("branch", existing.get("branch"))
            existing["year"] = user_data.get("academic_year", existing.get("year"))
            existing["section"] = user_data.get("section", existing.get("section"))
            existing["roll_number"] = user_data.get("roll_number", existing.get("roll_number"))
            existing["last_active"] = datetime.utcnow().isoformat() + "Z"
        else:
            # If user 1 is default mock user or placeholder, adopt user 1
            user1 = next((u for u in users if u.get("id") == 1), None)
            if user1 and (user1.get("email") in ("ganesh@skillexa.edu", "") or not user1.get("email")):
                user1["name"] = user_data["name"]
                user1["email"] = email
                user1["phone"] = user_data.get("phone") or "+91 98765 43210"
                user1["education"] = education
                user1["branch"] = user_data.get("branch")
                user1["year"] = user_data.get("academic_year")
                user1["section"] = user_data.get("section")
                user1["roll_number"] = user_data.get("roll_number")
                user1["last_active"] = datetime.utcnow().isoformat() + "Z"
            else:
                next_id = max((u.get("id", 0) for u in users), default=0) + 1
                users.append({
                    "id": next_id,
                    "name": user_data["name"],
                    "email": email,
                    "phone": user_data.get("phone", ""),
                    "education": education,
                    "branch": user_data.get("branch", ""),
                    "year": user_data.get("academic_year", ""),
                    "section": user_data.get("section", ""),
                    "roll_number": user_data.get("roll_number", ""),
                    "role": user_data.get("role", "student"),
                    "state": "Karnataka",
                    "target_exams": ["Placement Aptitude", "SSC CGL", "UPSC CDS"],
                    "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80",
                    "streak_days": 1,
                    "created_at": datetime.utcnow().isoformat() + "Z",
                    "last_active": datetime.utcnow().isoformat() + "Z",
                })

        data["users"] = users
        with open(db_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
