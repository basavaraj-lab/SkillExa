import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for i, p in enumerate(data):
    smap = p.get("starter_code_map", {})
    keys = list(smap.keys())
    if set(keys) != {"c", "cpp", "java", "python"}:
        print(f"Problem {p['id']} starter_code_map keys: {keys}")

