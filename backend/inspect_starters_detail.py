import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for pid in ["dsa-string-palindrome", "dsa-string-anagrams", "dsa-search-linear", "dsa-search-rotated-sorted-array"]:
    p = next(x for x in data if x["id"] == pid)
    print("====================================")
    print("Problem:", p["id"], "|", p["title"])
    print("Test Cases:", p["test_cases"][:2])
    for lang, code in p["starter_code_map"].items():
        print(f"[{lang}] First 3 lines:\n", "\n".join(code.split("\n")[:3]))

