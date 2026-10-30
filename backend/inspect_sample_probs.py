import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for p in data:
    if p["id"] in ["dsa-string-binary-check", "dsa-string-palindrome", "dsa-search-linear", "dsa-search-binary"]:
        print("=== ID:", p["id"], "===")
        print("Title:", p["title"])
        print("Test cases:", p.get("test_cases"))
        starter_keys = list(p.get("starter_code_map", {}).keys())
        print("Starter keys:", starter_keys)
        sol = p.get("solution_code")
        if isinstance(sol, str):
            try:
                s_dict = json.loads(sol)
                print("Solution keys:", list(s_dict.keys()))
            except:
                print("Solution is raw string")
        elif isinstance(sol, dict):
            print("Solution keys:", list(sol.keys()))
        else:
            print("No solution")

