import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for idx, p in enumerate(data):
    cat = p.get("category", p.get("topic", ""))
    pid = p.get("id")
    title = p.get("title")
    sol = p.get("solution_code")
    sol_keys = []
    if sol:
        try:
            d = json.loads(sol) if isinstance(sol, str) else sol
            sol_keys = list(d.keys()) if isinstance(d, dict) else ["non-dict"]
        except:
            sol_keys = ["str"]
    print(f"[{idx+1}] ID: {pid} | Cat: {cat} | Title: {title} | Sol: {sol_keys}")

