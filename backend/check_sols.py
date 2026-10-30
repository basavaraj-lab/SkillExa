import json

with open('backend/app/data/dsa_problems_seed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, p in enumerate(data):
    cat = p.get('category')
    sol = p.get('solution_code')
    sol_map = p.get('solution_code_map')
    parsed_langs = []
    if isinstance(sol_map, dict):
        parsed_langs = list(sol_map.keys())
    elif isinstance(sol, dict):
        parsed_langs = list(sol.keys())
    elif isinstance(sol, str):
        try:
            d = json.loads(sol)
            if isinstance(d, dict):
                parsed_langs = list(d.keys())
            else:
                parsed_langs = ['str_json']
        except Exception:
            parsed_langs = ['raw_text']

    print(f"{i+1:2d}. {p['id']} [{cat}] - {p['title']} => {parsed_langs}")
