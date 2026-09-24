import json
import os
import sys
from sqlalchemy import text

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from backend.app.database import SessionLocal, Base, engine
from backend.app.models.coding import CodingProblem, DifficultyEnum

def migrate_db_columns():
    """Ensure missing columns are added to existing SQLite database tables."""
    with engine.connect() as conn:
        try:
            # Check existing columns in coding_problems
            result = conn.execute(text("PRAGMA table_info(coding_problems)"))
            existing_cols = [row[1] for row in result.fetchall()]

            if existing_cols:
                cols_to_add = [
                    ("problem_num", "INTEGER DEFAULT 1"),
                    ("category", "VARCHAR(100) DEFAULT 'Arrays'"),
                    ("time_complexity", "VARCHAR(100)"),
                    ("space_complexity", "VARCHAR(100)"),
                    ("company_tags", "JSON DEFAULT '[]'"),
                    ("starter_code_map", "JSON DEFAULT '{}'"),
                    ("hidden_test_cases", "JSON DEFAULT '[]'"),
                ]
                for col_name, col_type in cols_to_add:
                    if col_name not in existing_cols:
                        conn.execute(text(f"ALTER TABLE coding_problems ADD COLUMN {col_name} {col_type}"))
                conn.commit()
        except Exception as e:
            print(f"Migration note: {e}")

def seed_dsa_problems():
    migrate_db_columns()
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    seed_file = os.path.join(os.path.dirname(__file__), "data", "dsa_problems_seed.json")
    if not os.path.exists(seed_file):
        print(f"Seed file not found: {seed_file}")
        return

    with open(seed_file, "r", encoding="utf-8") as f:
        problems_data = json.load(f)

    inserted = 0
    updated = 0

    for prob in problems_data:
        p_id = str(prob.get("id"))
        existing = db.query(CodingProblem).filter(CodingProblem.id == p_id).first()

        diff_str = prob.get("difficulty", "Medium").upper()
        if diff_str == "BASIC":
            diff_enum = DifficultyEnum.BASIC
        elif diff_str == "EASY":
            diff_enum = DifficultyEnum.EASY
        elif diff_str == "HARD":
            diff_enum = DifficultyEnum.HARD
        else:
            diff_enum = DifficultyEnum.MEDIUM

        starter_map = prob.get("starter_code", {})
        fallback_code = starter_map.get("python") or starter_map.get("c") or "def solution():\n    pass"

        if existing:
            existing.title = prob.get("title", existing.title)
            existing.category = prob.get("category", existing.category)
            existing.difficulty = diff_enum
            existing.description = prob.get("description", existing.description)
            existing.constraints = prob.get("constraints", existing.constraints)
            existing.time_complexity = prob.get("time_complexity", existing.time_complexity)
            existing.space_complexity = prob.get("space_complexity", existing.space_complexity)
            existing.company_tags = prob.get("company_tags", existing.company_tags)
            existing.examples = prob.get("examples", existing.examples)
            existing.starter_code = fallback_code
            existing.starter_code_map = starter_map
            existing.test_cases = prob.get("test_cases", existing.test_cases)
            existing.hidden_test_cases = prob.get("hidden_test_cases", existing.hidden_test_cases)
            updated += 1
        else:
            new_prob = CodingProblem(
                id=p_id,
                problem_num=prob.get("problem_num", 1),
                title=prob.get("title", ""),
                category=prob.get("category", "General"),
                difficulty=diff_enum,
                topic=prob.get("category", "General"),
                description=prob.get("description", ""),
                constraints=prob.get("constraints", ""),
                time_complexity=prob.get("time_complexity", ""),
                space_complexity=prob.get("space_complexity", ""),
                company_tags=prob.get("company_tags", []),
                examples=prob.get("examples", []),
                starter_code=fallback_code,
                starter_code_map=starter_map,
                test_cases=prob.get("test_cases", []),
                hidden_test_cases=prob.get("hidden_test_cases", []),
                points=10,
            )
            db.add(new_prob)
            inserted += 1

    db.commit()
    db.close()
    print(f"Successfully seeded DSA problems! Inserted: {inserted}, Updated: {updated}")

if __name__ == "__main__":
    seed_dsa_problems()
