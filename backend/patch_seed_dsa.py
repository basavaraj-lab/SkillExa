with open("backend/app/seed_dsa.py", "r", encoding="utf-8") as f:
    text = f.read()

# In if existing:
old_update = """            existing.starter_code_map = starter_map
            existing.test_cases = prob.get("test_cases", existing.test_cases)
            existing.hidden_test_cases = prob.get("hidden_test_cases", existing.hidden_test_cases)
            updated += 1"""

new_update = """            existing.starter_code_map = starter_map
            sol_val = prob.get("solution_code")
            existing.solution_code = json.dumps(sol_val) if isinstance(sol_val, dict) else (sol_val if isinstance(sol_val, str) else None)
            existing.test_cases = prob.get("test_cases", existing.test_cases)
            existing.hidden_test_cases = prob.get("hidden_test_cases", existing.hidden_test_cases)
            updated += 1"""

text = text.replace(old_update, new_update)

# In else:
old_insert = """                starter_code_map=starter_map,
                test_cases=prob.get("test_cases", []),"""

new_insert = """                starter_code_map=starter_map,
                solution_code=json.dumps(prob.get("solution_code")) if isinstance(prob.get("solution_code"), dict) else prob.get("solution_code"),
                test_cases=prob.get("test_cases", []),"""

text = text.replace(old_insert, new_insert)

with open("backend/app/seed_dsa.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated seed_dsa.py to persist solution_code!")

