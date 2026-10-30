import json
import sys
import os

sys.path.insert(0, os.path.abspath("."))

from backend.app.services.execution_service import SandboxedExecutionService
from backend.app.models.coding import SubmissionStatusEnum

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    problems = json.load(f)

target_ids = [
    # Hashing (1-15)
    "dsa-hash-two-sum", "dsa-hash-contains-duplicate", "dsa-hash-frequency-counter",
    "dsa-hash-intersection-two-arrays", "dsa-hash-first-unique-char", "dsa-hash-group-anagrams",
    "dsa-hash-longest-consecutive-sequence", "dsa-hash-subarray-sum-equals-k", "dsa-hash-top-k-frequent",
    "dsa-hash-4sum-ii", "dsa-hash-min-window-substring", "dsa-hash-count-smaller-after-self",
    "dsa-hash-longest-duplicate-substring", "dsa-hash-substring-concat-all-words", "dsa-hash-distinct-echo-substrings",
    # Trees (16-30)
    "dsa-tree-max-depth", "dsa-tree-count-nodes", "dsa-tree-inorder-traversal",
    "dsa-tree-preorder-traversal", "dsa-tree-postorder-traversal", "dsa-tree-level-order-traversal",
    "dsa-tree-invert-binary-tree", "dsa-tree-diameter-binary-tree", "dsa-tree-check-balanced",
    "dsa-tree-lowest-common-ancestor", "dsa-tree-max-path-sum", "dsa-tree-serialize-deserialize",
    "dsa-tree-construct-from-pre-in", "dsa-tree-max-width", "dsa-tree-recover-bst"
]

target_problems = [p for p in problems if p.get("id") in target_ids]
print(f"Testing {len(target_problems)} problems across Python, C, C++...")

failures = []

for prob in target_problems:
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
    print("\nALL 30 HASHING & TREE PROBLEMS PASSED PERFECTLY FOR ALL LANGUAGES!")

