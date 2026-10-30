import json

with open('backend/app/routers/coding.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Add json import if needed
if "import json" not in text:
    text = "import json\n" + text

# Add helper function extract_solution_map
helper_code = '''
def extract_solution_map(problem) -> dict:
    raw = getattr(problem, "solution_code", None)
    if not raw:
        return {}
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, str):
        try:
            parsed = json.loads(raw)
            if isinstance(parsed, dict):
                return parsed
            return {"python": str(parsed)}
        except Exception:
            return {"python": raw}
    return {}
'''

if "def extract_solution_map" not in text:
    # insert before router = APIRouter
    text = text.replace("router = APIRouter", helper_code + "\nrouter = APIRouter")

# In get_coding_problems:
old_resp_list = '''            examples=p.examples or [],
            starter_code=p.starter_code,
            starter_code_map=getattr(p, "starter_code_map", {}) or {},
            test_cases=p.test_cases or [],'''

new_resp_list = '''            examples=p.examples or [],
            starter_code=p.starter_code,
            starter_code_map=getattr(p, "starter_code_map", {}) or {},
            solution_code=p.solution_code if isinstance(p.solution_code, str) else json.dumps(p.solution_code or {}),
            solution_code_map=extract_solution_map(p),
            test_cases=p.test_cases or [],'''

text = text.replace(old_resp_list, new_resp_list)

# In get_coding_problem_by_id:
old_resp_single = '''        examples=problem.examples or [],
        starter_code=problem.starter_code,
        starter_code_map=getattr(problem, "starter_code_map", {}) or {},
        test_cases=problem.test_cases or [],'''

new_resp_single = '''        examples=problem.examples or [],
        starter_code=problem.starter_code,
        starter_code_map=getattr(problem, "starter_code_map", {}) or {},
        solution_code=problem.solution_code if isinstance(problem.solution_code, str) else json.dumps(problem.solution_code or {}),
        solution_code_map=extract_solution_map(problem),
        test_cases=problem.test_cases or [],'''

text = text.replace(old_resp_single, new_resp_single)

# In submit_problem_code:
old_submit_resp = '''            error_message=None if status_res == SubmissionStatusEnum.PASSED else logs,
            created_at=submission.created_at,'''

new_submit_resp = '''            error_message=None if status_res == SubmissionStatusEnum.PASSED else logs,
            solutions=extract_solution_map(problem),
            created_at=submission.created_at,'''

text = text.replace(old_submit_resp, new_submit_resp)

with open('backend/app/routers/coding.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated backend/app/routers/coding.py successfully")

