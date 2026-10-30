import json
import sys
import os

sys.path.insert(0, os.path.abspath("."))

from backend.app.services.execution_service import SandboxedExecutionService
from backend.app.models.coding import SubmissionStatusEnum

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    problems = json.load(f)

target_ids = [
    # Graphs (1-15)
    "dsa-graph-adj-list", "dsa-graph-bfs", "dsa-graph-dfs", "dsa-graph-connected-components",
    "dsa-graph-valid-path", "dsa-graph-undirected-cycle", "dsa-graph-directed-cycle",
    "dsa-graph-topological-sort", "dsa-graph-shortest-path-unweighted", "dsa-graph-number-of-islands",
    "dsa-graph-dijkstra", "dsa-graph-bellman-ford", "dsa-graph-floyd-warshall",
    "dsa-graph-kruskal", "dsa-graph-word-ladder",
    # DP (16-30)
    "dsa-dp-fibonacci", "dsa-dp-climbing-stairs", "dsa-dp-min-cost-climbing-stairs",
    "dsa-dp-house-robber", "dsa-dp-kadane", "dsa-dp-coin-change", "dsa-dp-01-knapsack",
    "dsa-dp-lcs", "dsa-dp-lis", "dsa-dp-unique-paths", "dsa-dp-edit-distance",
    "dsa-dp-matrix-chain", "dsa-dp-word-break", "dsa-dp-partition-equal-subset", "dsa-dp-burst-balloons"
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
    print("\nALL 30 GRAPH & DP PROBLEMS PASSED PERFECTLY FOR ALL TESTED LANGUAGES!")

