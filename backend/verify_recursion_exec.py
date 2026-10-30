import json
import sys
import os

sys.path.insert(0, os.path.abspath("."))

from backend.app.services.execution_service import SandboxedExecutionService
from backend.app.models.coding import SubmissionStatusEnum

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    problems = json.load(f)

rec_ids = {
    "dsa-rec-factorial", "dsa-rec-fibonacci", "dsa-rec-sum-of-digits",
    "dsa-rec-reverse-string", "dsa-rec-check-palindrome", "dsa-rec-power",
    "dsa-rec-all-subsequences", "dsa-rec-permutations", "dsa-rec-combination-sum",
    "dsa-rec-generate-parentheses", "dsa-rec-n-queens", "dsa-rec-sudoku-solver",
    "dsa-rec-word-search", "dsa-rec-rat-in-maze", "dsa-rec-palindrome-partitioning"
}

rec_problems = [p for p in problems if p.get("id") in rec_ids]

print(f"Testing {len(rec_problems)} Recursion problems...")

failures = []

for prob in rec_problems:
    pid = prob["id"]
    title = prob["title"]
    solutions = json.loads(prob["solution_code"])
    test_cases = prob["test_cases"]

    for lang in ["python", "c", "cpp"]:
        code = solutions.get(lang)
        if not code:
            continue
        try:
            status, passed, total, logs = SandboxedExecutionService.run_test_cases(lang, code, test_cases)
            if status == SubmissionStatusEnum.PASSED and passed == total:
                print(f"[PASS] {pid} ({title}) in {lang} ({passed}/{total})")
            else:
                print(f"[FAIL] {pid} ({title}) in {lang}: status={status}, passed={passed}/{total}")
                print(f"       Logs:\n{logs}\n")
                failures.append((pid, lang))
        except Exception as e:
            print(f"[ERROR] {pid} ({title}) in {lang}: {e}")
            failures.append((pid, lang))

if failures:
    print(f"\nCompleted with {len(failures)} failures: {failures}")
    sys.exit(1)
else:
    print("\nALL 15 RECURSION PROBLEMS PASSED PERFECTLY FOR ALL LANGUAGES!")
