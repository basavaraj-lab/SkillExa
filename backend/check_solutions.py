import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total problems: {len(data)}")
categories = {}
missing_sol = []
single_sol = []
all_four = []

for idx, p in enumerate(data):
    cat = p.get("category", p.get("topic", "Unknown"))
    categories[cat] = categories.get(cat, 0) + 1
    sol = p.get("solution_code")
    if not sol:
        missing_sol.append((p.get("id"), p.get("title"), cat))
        continue
    if isinstance(sol, str):
        try:
            sol_dict = json.loads(sol)
        except Exception:
            sol_dict = {"raw": sol}
    elif isinstance(sol, dict):
        sol_dict = sol
    else:
        sol_dict = {}

    keys = set(sol_dict.keys())
    if {"c", "cpp", "java", "python"}.issubset(keys):
        all_four.append(p.get("id"))
    else:
        single_sol.append((p.get("id"), p.get("title"), cat, list(keys)))

print("Category counts:", categories)
print(f"All four languages present: {len(all_four)}")
print(f"Missing solution: {len(missing_sol)}")
print(f"Single/partial solution: {len(single_sol)}")
for s in single_sol[:15]:
    print("  Partial:", s)
for m in missing_sol[:15]:
    print("  Missing:", m)

