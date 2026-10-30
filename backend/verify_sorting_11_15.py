import sys, os
sys.path.insert(0, os.path.abspath('.'))
import json
from backend.app.services.execution_service import SandboxedExecutionService

with open('backend/app/data/dsa_problems_seed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

sorting = [p for p in data if p.get('category') == 'Sorting' and p.get('id', '').startswith('dsa-sort-')]

for p in sorting[10:15]:
    smap = json.loads(p['solution_code'])
    pid = p['id']
    print(f"--- {pid} ({p['title']}) ---")
    for lang in ['c', 'cpp', 'python']:
        status, passed, total, logs = SandboxedExecutionService.run_test_cases(lang, smap[lang], p['test_cases'])
        print(f"  [{lang}] {status.value} ({passed}/{total})")
        if status.value != "PASSED":
            print(f"    Logs: {logs}")

