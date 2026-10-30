import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for p in data:
    if p["id"] == "dsa-search-linear":
        print("STARTER CODE MAP:")
        for k, v in p.get("starter_code_map", {}).items():
            print(f"--- {k} ---")
            print(v)
        print("SOLUTION CODE:")
        print(p.get("solution_code"))

