from typing import List, Optional
from sqlalchemy.orm import Session
from backend.app.models.college import College, CollegeAnnouncement
from backend.app.models.user import StudentProfile


class CollegeService:
    @staticmethod
    def matches_student_targeting(
        item_college_id: Optional[str],
        target_departments: Optional[List[str]],
        target_years: Optional[List[str]],
        target_sections: Optional[List[str]],
        target_student_ids: Optional[List[str]],
        student: StudentProfile,
    ) -> bool:
        """
        Check if a given student matches college-based targeting rules.
        """
        # 1. College Match (Must belong to the same college)
        if item_college_id and student.college_id and item_college_id != student.college_id:
            return False

        # 2. Specific Student IDs targeting
        if target_student_ids and len(target_student_ids) > 0:
            if student.id in target_student_ids or student.user_id in target_student_ids:
                return True
            # If explicit student targets exist and this student is not in the list, check if other targets match

        # 3. Department / Branch Target
        if target_departments and len(target_departments) > 0:
            match_dept = any(
                dept.lower() in student.branch.lower() or student.branch.lower() in dept.lower()
                for dept in target_departments
            )
            if not match_dept:
                return False

        # 4. Academic Year Target
        if target_years and len(target_years) > 0:
            match_year = any(
                yr.lower() in student.academic_year.lower() or student.academic_year.lower() in yr.lower()
                for yr in target_years
            )
            if not match_year:
                return False

        # 5. Section Target
        if target_sections and len(target_sections) > 0:
            match_sec = any(
                sec.upper() == student.section.upper()
                for sec in target_sections
            )
            if not match_sec:
                return False

        return True

    @staticmethod
    def get_announcements_for_student(db: Session, student: StudentProfile) -> List[CollegeAnnouncement]:
        if not student.college_id:
            return []

        all_announcements = (
            db.query(CollegeAnnouncement)
            .filter(CollegeAnnouncement.college_id == student.college_id)
            .order_by(CollegeAnnouncement.is_pinned.desc(), CollegeAnnouncement.created_at.desc())
            .all()
        )

        filtered = []
        for ann in all_announcements:
            if CollegeService.matches_student_targeting(
                ann.college_id,
                ann.target_departments,
                ann.target_years,
                ann.target_sections,
                None,
                student,
            ):
                filtered.append(ann)
        return filtered
