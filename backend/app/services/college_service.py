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
        kvg_ids = {"0f669a91-5c8d-4304-a815-818bde05e996", "clg-kvg"}
        if item_college_id and student.college_id:
            if item_college_id in kvg_ids and student.college_id in kvg_ids:
                pass
            elif item_college_id != student.college_id:
                return False

        # 2. Specific Student IDs targeting
        if target_student_ids and len(target_student_ids) > 0:
            if student.id in target_student_ids or student.user_id in target_student_ids:
                return True
            # If explicit student targets exist and this student is not in the list, check if other targets match

        # 3. Department / Branch Target
        if target_departments and len(target_departments) > 0:
            has_all_dept = any(d.lower() in ["all", "all branches", "all departments", "*"] for d in target_departments)
            if not has_all_dept:
                match_dept = any(
                    dept.lower() in (student.branch or "").lower() or (student.branch or "").lower() in dept.lower()
                    for dept in target_departments
                )
                if not match_dept:
                    return False

        # 4. Academic Year Target
        if target_years and len(target_years) > 0:
            has_all_year = any(y.lower() in ["all", "all years", "*"] for y in target_years)
            if not has_all_year:
                match_year = any(
                    yr.lower() in (student.academic_year or "").lower() or (student.academic_year or "").lower() in yr.lower()
                    for yr in target_years
                )
                if not match_year:
                    return False

        # 5. Section Target
        if target_sections and len(target_sections) > 0:
            has_all_sec = any(s.upper() in ["ALL", "*"] for s in target_sections)
            if not has_all_sec:
                match_sec = any(
                    sec.upper() == (student.section or "").upper()
                    for sec in target_sections
                )
                if not match_sec:
                    return False

        return True

    @staticmethod
    def get_announcements_for_student(db: Session, student: StudentProfile) -> List[CollegeAnnouncement]:
        if not student:
            return []

        query = db.query(CollegeAnnouncement)
        if student.college_id:
            college_ids = [student.college_id]
            if student.college_id in ["0f669a91-5c8d-4304-a815-818bde05e996", "clg-kvg"]:
                college_ids = ["0f669a91-5c8d-4304-a815-818bde05e996", "clg-kvg"]
            query = query.filter(
                (CollegeAnnouncement.college_id.in_(college_ids)) | (CollegeAnnouncement.college_id == None)
            )

        all_announcements = (
            query
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
