import logging
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from backend.app.database import Base, SessionLocal, engine
from backend.app.models.college import College, CollegeAnnouncement
from backend.app.models.curriculum import SectionTypeEnum, Subject, Topic
from backend.app.models.note import FacultyNote, PDFNote, VisibilityEnum
from backend.app.models.notification import Notification, NotificationTypeEnum, StudentProgress
from backend.app.models.quiz import DifficultyEnum, Question, Quiz
from backend.app.models.coding import CodingProblem
from backend.app.models.user import (
    FacultyProfile,
    RoleEnum,
    StudentProfile,
    User,
    VerificationStatusEnum,
)
from backend.app.utils.security import hash_password

logger = logging.getLogger("skillexa.seed")


def seed_database():
    """Seed initial demo data if database is empty."""
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()

    try:
        # Check if already seeded
        if db.query(College).first():
            print("Database already contains data. Skipping seed.")
            return

        print("Seeding SkillExa database...")

        # 1. Colleges
        clg_kvg = College(code="KVG001", name="KVG College of Engineering", city="Sullia", state="Karnataka", is_verified=True)
        clg_rvce = College(code="RVCE01", name="R.V. College of Engineering (RVCE)", city="Bengaluru", state="Karnataka", is_verified=True)
        clg_bms = College(code="BMSCE01", name="B.M.S. College of Engineering", city="Bengaluru", state="Karnataka", is_verified=True)
        clg_nitk = College(code="NITK01", name="National Institute of Technology Karnataka (NITK)", city="Surathkal", state="Karnataka", is_verified=True)
        clg_dit = College(code="DIT01", name="Delhi Institute of Technology", city="Delhi", state="Delhi", is_verified=True)
        clg_pres = College(code="PRES01", name="Presidency College", city="Kolkata", state="West Bengal", is_verified=True)

        db.add_all([clg_kvg, clg_rvce, clg_bms, clg_nitk, clg_dit, clg_pres])
        db.flush()

        # 2. Users & Faculty Profiles
        # Faculty 1: Dr. Ramesh Kumar (KVGCE - ECE)
        u_ramesh = User(email="dr.ramesh@kvgce.edu.in", password_hash=hash_password("faculty123"), name="Dr. Ramesh Kumar", role=RoleEnum.FACULTY)
        db.add(u_ramesh)
        db.flush()
        f_ramesh = FacultyProfile(
            user_id=u_ramesh.id,
            college_id=clg_kvg.id,
            department="ECE",
            designation="Professor & HOD",
            office_room="EC-302",
            subjects_taught=["Embedded Systems", "Microcontrollers", "VLSI"],
            verification_status=VerificationStatusEnum.APPROVED,
            bio="20+ years of academic research and embedded hardware design mentoring.",
        )
        db.add(f_ramesh)

        # Faculty 2: Dr. Sunita Rao (RVCE - CSE)
        u_sunita = User(email="dr.sunita@rvce.edu.in", password_hash=hash_password("faculty123"), name="Dr. Sunita Rao", role=RoleEnum.FACULTY)
        db.add(u_sunita)
        db.flush()
        f_sunita = FacultyProfile(
            user_id=u_sunita.id,
            college_id=clg_rvce.id,
            department="CSE",
            designation="Professor & Senior Educator",
            office_room="CS-401",
            subjects_taught=["Programming in Python", "Data Science", "Algorithms"],
            verification_status=VerificationStatusEnum.APPROVED,
        )
        db.add(f_sunita)

        # Faculty 3: Prof. Vikram Hegde (BMSCE - ECE)
        u_vikram = User(email="prof.vikram@bmsce.edu.in", password_hash=hash_password("faculty123"), name="Prof. Vikram Hegde", role=RoleEnum.FACULTY)
        db.add(u_vikram)
        db.flush()
        f_vikram = FacultyProfile(
            user_id=u_vikram.id,
            college_id=clg_bms.id,
            department="ECE",
            designation="Associate Professor",
            subjects_taught=["Programming in C", "Microprocessors", "Operating Systems"],
            verification_status=VerificationStatusEnum.APPROVED,
        )
        db.add(f_vikram)

        # 3. Student User: Ganesh Sharan (KVGCE - ECE 3rd Year A)
        u_ganesh = User(email="ganesh@kvgce.edu.in", password_hash=hash_password("student123"), name="Ganesh Sharan", role=RoleEnum.STUDENT)
        db.add(u_ganesh)
        db.flush()
        s_ganesh = StudentProfile(
            user_id=u_ganesh.id,
            college_id=clg_kvg.id,
            branch="ECE",
            academic_year="3rd Year",
            section="A",
            roll_number="4KV22EC018",
            target_exam="Placement",
        )
        db.add(s_ganesh)

        # 4. Announcements
        ann1 = CollegeAnnouncement(
            college_id=clg_kvg.id,
            faculty_id=u_ramesh.id,
            faculty_name="Dr. Ramesh Kumar",
            faculty_dept="ECE Department",
            title="📢 ECE 3rd Year Embedded Systems Lab Practical Assessment",
            content="Final lab submissions and viva for Microcontroller Timers and ADC modules are scheduled for Friday at 10:00 AM.",
            priority="HIGH",
            is_pinned=True,
            target_departments=["ECE"],
            target_years=["3rd Year"],
            target_sections=["A"],
        )
        db.add(ann1)

        # 5. Faculty Notes (Targeted & Community)
        # Note 1: College Targeted
        note1 = FacultyNote(
            faculty_id=f_ramesh.id,
            college_id=clg_kvg.id,
            title="Embedded Systems: Microcontroller Architecture & GPIO Protocols",
            description="Complete hardware register mapping, push-pull vs open-drain configuration, and interrupt vector tables.",
            content="Microcontroller units (MCUs) integrate CPU cores, SRAM, Flash memory, and I/O peripherals onto a single monolithic die...",
            section="engineering",
            subject="Embedded Systems",
            topic="Microcontrollers",
            important_concepts=[
                "Registers dictate pin modes (Input, Output, Alternate Function, Analog).",
                "Push-pull drives both VDD and GND actively; open-drain requires external pull-up resistor.",
                "NVIC (Nested Vectored Interrupt Controller) provides deterministic low-latency interrupt handling.",
            ],
            quick_revision="GPIO = General Purpose Input Output. Ensure MODER is configured before reading IDR or writing ODR.",
            visibility=VisibilityEnum.COLLEGE,
            published=True,
            target_departments=["ECE"],
            target_years=["3rd Year"],
            target_sections=["A"],
        )
        db.add(note1)

        # Note 2: Community Note by Dr. Sunita Rao (RVCE)
        note2 = FacultyNote(
            faculty_id=f_sunita.id,
            college_id=clg_rvce.id,
            title="Python Functions Mastery: First-Class Citizens, Closures & Decorator Patterns",
            description="Deep dive into execution frames, lexical scoping, closure cell objects, and functools wrappers.",
            content="In Python, functions are first-class objects, meaning they can be passed as arguments, assigned to variables, and returned from other functions...",
            section="programming",
            subject="Programming in Python",
            topic="Functions & Scope",
            important_concepts=[
                "Lexical scoping follows LEGB (Local, Enclosing, Global, Built-in).",
                "Closures remember free variables from enclosing scopes via __closure__ cells.",
                "Decorators accept a callable and return an enhanced wrapper function.",
            ],
            quick_revision="Use @functools.wraps(fn) inside decorators to preserve docstrings and original function metadata.",
            visibility=VisibilityEnum.COMMUNITY,
            published=True,
        )
        db.add(note2)

        # 6. Faculty Quizzes
        quiz1 = Quiz(
            faculty_id=f_ramesh.id,
            college_id=clg_kvg.id,
            title="Embedded Systems & Microcontroller Registers Assessment",
            description="Timed evaluation on GPIO modes, Interrupt NVIC priorities, and timer prescalers.",
            section="engineering",
            subject="Embedded Systems",
            topic="Microcontrollers",
            difficulty=DifficultyEnum.MEDIUM,
            duration_minutes=15,
            total_marks=10.0,
            negative_marks=0.5,
            visibility=VisibilityEnum.COLLEGE,
            published=True,
            target_departments=["ECE"],
            target_years=["3rd Year"],
            target_sections=["A"],
        )
        db.add(quiz1)
        db.flush()

        q1 = Question(
            quiz_id=quiz1.id,
            section="engineering",
            subject="Embedded Systems",
            topic="Microcontrollers",
            question_text="Which GPIO output configuration requires an external pull-up resistor to pull the line high?",
            options=["Push-Pull Mode", "Open-Drain Mode", "Analog Mode", "Floating Input"],
            correct_answer=1,
            explanation="Open-drain pins can only pull the line to ground (active low); a pull-up resistor is mandatory to establish high state (e.g., I2C bus).",
            marks=2.0,
            negative_marks=0.5,
            order_index=0,
        )
        q2 = Question(
            quiz_id=quiz1.id,
            section="engineering",
            subject="Embedded Systems",
            topic="Microcontrollers",
            question_text="In ARM Cortex-M MCUs, which hardware unit manages priority levels and rapid vectoring of hardware interrupts?",
            options=["DMA Controller", "NVIC (Nested Vectored Interrupt Controller)", "SysTick Timer", "Watchdog Timer"],
            correct_answer=1,
            explanation="NVIC handles nested preemptive interrupts with fixed low latency.",
            marks=2.0,
            negative_marks=0.5,
            order_index=1,
        )
        db.add_all([q1, q2])

        # 7. Coding Problems
        prob1 = CodingProblem(
            title="Two Sum — Target Sum Finder",
            description="Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.",
            language="python",
            difficulty=DifficultyEnum.EASY,
            topic="Arrays",
            starter_code="def two_sum(nums, target):\n    # Write your solution here\n    pass\n",
            test_cases=[
                {"input": "[2, 7, 11, 15]\n9", "expected": "[0, 1]"},
                {"input": "[3, 2, 4]\n6", "expected": "[1, 2]"},
            ],
            points=10,
        )
        prob2 = CodingProblem(
            title="Reverse Linked List in C",
            description="Given the pointer to the head node of a singly linked list, reverse the list in-place in O(N) time and O(1) space.",
            language="c",
            difficulty=DifficultyEnum.MEDIUM,
            topic="Linked List",
            starter_code="#include <stdio.h>\n#include <stdlib.h>\n\nstruct Node {\n    int data;\n    struct Node* next;\n};\n",
            test_cases=[
                {"input": "1->2->3->4->5", "expected": "5->4->3->2->1"},
            ],
            points=20,
        )
        prob3 = CodingProblem(
            title="Binary Search in C++",
            description="Implement binary search algorithm to find target value in sorted vector `nums` in O(log N) time.",
            language="cpp",
            difficulty=DifficultyEnum.EASY,
            topic="Binary Search",
            starter_code="#include <iostream>\n#include <vector>\nusing namespace std;\n\nint binarySearch(const vector<int>& nums, int target) {\n    // Write solution\n    return -1;\n}\n",
            test_cases=[
                {"input": "nums=[1,3,5,7,9], target=7", "expected": "3"},
            ],
            points=15,
        )
        prob4 = CodingProblem(
            title="Valid Parentheses in Java",
            description="Given a string `s` containing just parentheses `()`, `{}` and `[]`, determine if input string is valid.",
            language="java",
            difficulty=DifficultyEnum.EASY,
            topic="Stacks",
            starter_code="import java.util.Stack;\n\npublic class Solution {\n    public static boolean isValid(String s) {\n        // Write solution\n        return true;\n    }\n}\n",
            test_cases=[
                {"input": "()[]{}", "expected": "true"},
            ],
            points=15,
        )
        prob5 = CodingProblem(
            title="Palindrome String Check in JS",
            description="Check if a string is a palindrome ignoring non-alphanumeric characters and case.",
            language="javascript",
            difficulty=DifficultyEnum.EASY,
            topic="Strings",
            starter_code="function isPalindrome(str) {\n  // Write solution\n  return true;\n}\n",
            test_cases=[
                {"input": "race a car", "expected": "false"},
            ],
            points=10,
        )
        db.add_all([prob1, prob2, prob3, prob4, prob5])

        # 8. Student Progress Record
        prog = StudentProgress(
            student_id=s_ganesh.id,
            section="engineering",
            subject="Embedded Systems",
            topic="Microcontrollers",
            mastery_percentage=85.0,
            quizzes_completed=5,
            quiz_accuracy=86.0,
            notes_read=18,
            coding_solved=45,
            last_activity_at=datetime.utcnow(),
        )
        db.add(prog)

        db.commit()
        print("Database seeded successfully with initial colleges, faculty, student, notes, quizzes, and coding problems!")

    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
