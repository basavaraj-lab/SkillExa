import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for p in data[30:45]:
    print("--------------------------------------------------")
    print(p["id"], "|", p["title"])
    sol = p.get("solution_code")
    if sol:
        try:
            d = json.loads(sol) if isinstance(sol, str) else sol
            if isinstance(d, dict):
                for k, v in d.items():
                    print(f"[{k}] {v[:100]}...")
            else:
                print(str(sol)[:100])
        except:
            print(str(sol)[:100])

