import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for i, p in enumerate(data):
    sol = p.get("solution_code")
    keys = []
    if sol:
        try:
            d = json.loads(sol) if isinstance(sol, str) else sol
            if isinstance(d, dict):
                keys = list(d.keys())
            else:
                keys = ["raw_str"]
        except:
            keys = ["raw_str"]
    print(f"{i+1}. id='{p['id']}', category='{p.get('category')}', title='{p.get('title')}', keys={keys}")

