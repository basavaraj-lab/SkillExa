"""Curriculum dataset catalog and content builder for Python topics."""
from __future__ import annotations

TOPIC_CATALOG = [
    {"id": 1, "title": "Introduction to Python", "difficulty": "Beginner", "duration": "20 min"},
    {"id": 2, "title": "Installation & Setup", "difficulty": "Beginner", "duration": "20 min"},
    {"id": 3, "title": "Variables", "difficulty": "Beginner", "duration": "25 min"},
    {"id": 4, "title": "Data Types", "difficulty": "Beginner", "duration": "30 min"},
    {"id": 5, "title": "Type Casting", "difficulty": "Beginner", "duration": "20 min"},
    {"id": 6, "title": "Operators", "difficulty": "Beginner", "duration": "30 min"},
    {"id": 7, "title": "Input & Output", "difficulty": "Beginner", "duration": "25 min"},
    {"id": 8, "title": "Conditional Statements", "difficulty": "Beginner", "duration": "30 min"},
    {"id": 9, "title": "Loops", "difficulty": "Intermediate", "duration": "35 min"},
    {"id": 10, "title": "Functions", "difficulty": "Intermediate", "duration": "35 min"},
    {"id": 11, "title": "Strings", "difficulty": "Intermediate", "duration": "30 min"},
    {"id": 12, "title": "Lists", "difficulty": "Intermediate", "duration": "35 min"},
    {"id": 13, "title": "Tuples", "difficulty": "Intermediate", "duration": "25 min"},
    {"id": 14, "title": "Sets", "difficulty": "Intermediate", "duration": "25 min"},
    {"id": 15, "title": "Dictionaries", "difficulty": "Intermediate", "duration": "30 min"},
    {"id": 16, "title": "File Handling", "difficulty": "Intermediate", "duration": "35 min"},
    {"id": 17, "title": "Exception Handling", "difficulty": "Intermediate", "duration": "30 min"},
    {"id": 18, "title": "Modules & Packages", "difficulty": "Intermediate", "duration": "30 min"},
    {"id": 19, "title": "Object Oriented Programming", "difficulty": "Advanced", "duration": "45 min"},
    {"id": 20, "title": "NumPy Basics", "difficulty": "Advanced", "duration": "40 min"},
    {"id": 21, "title": "Advanced Functions", "difficulty": "Advanced", "duration": "35 min"},
    {"id": 22, "title": "Iterators & Generators", "difficulty": "Advanced", "duration": "35 min"},
    {"id": 23, "title": "Final Assessment", "difficulty": "Advanced", "duration": "60 min"},
]

TOPIC_CORE = {
    1: {
        "concept": "Python is a readable, high-level language used in automation, web, data, and AI.",
        "syntax": "print('Hello, Python')",
        "example": "print('Welcome to SkillExa')",
        "output": "Welcome to SkillExa",
    },
    2: {
        "title": "Install Python",
        "theory": {
            "overview": "Python installation allows running scripts locally via terminal or IDE.",
            "steps": [
                "Download Python",
                "Install Python",
                "Verify Installation"
            ]
        },
        "example": {
            "code": "import sys\nprint(sys.version)",
            "output": "3.14.0"
        },
        "fill_blanks": {
            "question": "import _____\nprint(_____.version)",
            "answers": ["sys", "sys"]
        },
        "practice": {
            "title": "Print Python Version",
            "starter_code": "import sys\n\n# Write your code here"
        },
        "skill_exa_test": [
            {
                "question": "Python is a ____ language?",
                "options": ["Interpreted", "Compiled", "Machine", "Assembly"],
                "answer": "Interpreted"
            },
            {
                "question": "Which command checks Python version?",
                "options": ["python --version", "version python", "py version", "python install"],
                "answer": "python --version"
            }
        ],
        "xp": 50,
        "unlock_next": 3
    },
    3: {
        "title": "Variables",
        "theory": {
            "definition": "A variable is a name used to store data in memory. Variables allow you to save values and use them later in your program.",
            "why": "Variables make programs flexible and reusable because you can change the stored value without changing the rest of the code.",
            "rules": [
                "Variable names can contain letters, numbers, and underscores (_).",
                "A variable name cannot start with a number.",
                "Variable names are case-sensitive.",
                "Avoid using Python keywords like if, for, while, class, etc."
            ],
            "examples": [
                "name = 'SkillExa'",
                "age = 20",
                "price = 99.99",
                "is_student = True"
            ]
        },
        "syntax": "variable_name = value",
        "example": {
            "code": "count = 5\ncount = count + 1\nprint(count)",
            "output": "6",
            "explanation": "The variable 'count' stores 5. We increase it by 1, so the final value becomes 6."
        },
        "fill_blanks": {
            "question": "_____ = 10\nprint(number)",
            "answer": "number"
        },
        "compiler": {
            "title": "Create a Variable",
            "question": "Write a Python program that stores your name in a variable and prints it.",
            "starter_code": "# Write your code below\n"
        },
        "skill_exa_test": [
            {
                "question": "What is a variable?",
                "options": [
                    "A function",
                    "A memory location used to store data",
                    "A loop",
                    "A keyword"
                ],
                "answer": "A memory location used to store data"
            },
            {
                "question": "Which is a valid variable name?",
                "options": ["2name", "my_name", "class", "@name"],
                "answer": "my_name"
            },
            {
                "question": "Fill in the blank:\n_____ = 'Python'\nprint(language)",
                "options": ["language", "Python", "print", "value"],
                "answer": "language"
            }
        ],
        "completion": {
            "xp": 50,
            "badge": "Variables Beginner",
            "unlock_next": 4
        }
    },
    4: {
        "concept": "Common built-in types include int, float, str, bool, list, tuple, set, and dict.",
        "syntax": "print(type(10), type('A'))",
        "example": "a = 10\nb = 2.5\nprint(type(a).__name__, type(b).__name__)",
        "output": "int float",
    },
    5: {
        "concept": "Type casting converts values explicitly using int(), float(), str(), and bool().",
        "syntax": "age = int('18')",
        "example": "x = '12'\nprint(int(x) + 3)",
        "output": "15",
    },
    6: {
        "concept": "Operators perform arithmetic, comparison, and logical operations.",
        "syntax": "result = (10 + 2) * 3",
        "example": "a = 10\nb = 3\nprint(a // b, a % b)",
        "output": "3 1",
    },
    7: {
        "concept": "input() reads text and print() displays output with optional formatting.",
        "syntax": "name = input('Name: ')\nprint(f'Hi {name}')",
        "example": "name = 'Learner'\nprint(f'Hi {name}')",
        "output": "Hi Learner",
    },
    8: {
        "concept": "if, elif, and else branch program flow based on conditions.",
        "syntax": "if score >= 40:\n    print('Pass')",
        "example": "score = 82\nif score >= 80:\n    print('A')\nelse:\n    print('B')",
        "output": "A",
    },
    9: {
        "concept": "for loops iterate over sequences and while loops repeat until a condition changes.",
        "syntax": "for i in range(3):\n    print(i)",
        "example": "for i in range(1, 4):\n    print(i)",
        "output": "1\n2\n3",
    },
    10: {
        "concept": "Functions package reusable logic and can accept parameters and return values.",
        "syntax": "def add(a, b):\n    return a + b",
        "example": "def square(x):\n    return x * x\nprint(square(5))",
        "output": "25",
    },
    11: {
        "concept": "Strings are immutable text sequences with rich methods for manipulation.",
        "syntax": "text = 'python'\nprint(text.upper())",
        "example": "text = 'SkillExa'\nprint(text[0:5])",
        "output": "Skill",
    },
    12: {
        "concept": "Lists are ordered and mutable collections.",
        "syntax": "items = [1, 2, 3]\nitems.append(4)",
        "example": "nums = [4, 2, 8]\nnums.sort()\nprint(nums)",
        "output": "[2, 4, 8]",
    },
    13: {
        "concept": "Tuples are ordered and immutable collections.",
        "syntax": "point = (10, 20)",
        "example": "pair = (1, 2)\nprint(pair[1])",
        "output": "2",
    },
    14: {
        "concept": "Sets store unique unordered values and support union/intersection operations.",
        "syntax": "unique = {1, 2, 2, 3}",
        "example": "a = {1, 2, 3}\nb = {3, 4}\nprint(a & b)",
        "output": "{3}",
    },
    15: {
        "concept": "Dictionaries map keys to values and are optimized for lookups.",
        "syntax": "user = {'name': 'Ana'}",
        "example": "user = {'name': 'Ana', 'age': 20}\nprint(user['name'])",
        "output": "Ana",
    },
    16: {
        "concept": "File handling reads and writes data safely using with open(...).",
        "syntax": "with open('a.txt', 'w') as f:\n    f.write('hello')",
        "example": "with open('demo.txt', 'w') as f:\n    f.write('ok')\nwith open('demo.txt') as f:\n    print(f.read())",
        "output": "ok",
    },
    17: {
        "concept": "try/except catches runtime errors and keeps applications stable.",
        "syntax": "try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('error')",
        "example": "try:\n    int('abc')\nexcept ValueError:\n    print('invalid')",
        "output": "invalid",
    },
    18: {
        "concept": "Modules split code into files; packages group modules in folders.",
        "syntax": "from math import sqrt",
        "example": "import math\nprint(math.sqrt(16))",
        "output": "4.0",
    },
    19: {
        "concept": "OOP organizes logic into classes and objects with attributes and methods.",
        "syntax": "class User:\n    pass",
        "example": "class Greeter:\n    def hello(self):\n        return 'Hi'\nprint(Greeter().hello())",
        "output": "Hi",
    },
    20: {
        "concept": "NumPy provides efficient numerical arrays and vectorized operations.",
        "syntax": "import numpy as np",
        "example": "import numpy as np\na = np.array([1, 2, 3])\nprint((a * 2).tolist())",
        "output": "[2, 4, 6]",
    },
    21: {
        "concept": "Advanced function topics include lambda, map, filter, and recursion.",
        "syntax": "double = lambda x: x * 2",
        "example": "nums = [1, 2, 3]\nprint(list(map(lambda x: x * 2, nums)))",
        "output": "[2, 4, 6]",
    },
    22: {
        "concept": "Iterators and generators produce values lazily and reduce memory use.",
        "syntax": "def gen():\n    yield 1",
        "example": "def countdown(n):\n    while n:\n        yield n\n        n -= 1\nprint(list(countdown(3)))",
        "output": "[3, 2, 1]",
    },
    23: {
        "concept": "Final assessment combines all concepts through integrated coding tasks.",
        "syntax": "# Solve and test mixed-concept problems",
        "example": "def ready(score):\n    return 'Pass' if score >= 70 else 'Retry'\nprint(ready(85))",
        "output": "Pass",
    },
}


def _build_topic(topic_meta: dict[str, object]) -> dict[str, object]:
    topic_id = int(topic_meta["id"])
    core = TOPIC_CORE.get(topic_id, {})
    title = str(topic_meta["title"])

    theory = core.get("theory")
    if not isinstance(theory, dict):
        theory = {
            "definition": str(core.get("concept", "")),
            "why": f"{title} builds a foundation for practical Python work.",
            "rules": [
                "Read the syntax carefully before running the code.",
                "Change one value at a time when experimenting.",
                "Use print() to confirm what the program returns.",
            ],
            "examples": [str(core.get("example", ""))],
        }

    example = core.get("example")
    if not isinstance(example, dict):
        example = {
            "code": str(example or ""),
            "output": str(core.get("output", "")),
            "explanation": f"This example demonstrates {title.lower()} in action.",
        }

    fill_blanks = core.get("fill_blanks")
    if not isinstance(fill_blanks, dict):
        fill_blanks = {
            "question": f"Topic {topic_id} title is _______.",
            "answer": title,
        }

def _build_programming_exercise(topic_id: int, title: str, example: dict, fill_data: dict, compiler_raw: dict) -> dict:
    """Build programming exercise by converting topic example code into fill-in-the-blank code with option pills."""
    starter_code = compiler_raw.get("starter_code")
    options = compiler_raw.get("options")

    if topic_id == 1:
        starter_code = starter_code or "_____('Welcome to SkillExa')"
        options = options or ["print", "input", "write", "sys"]
    elif topic_id == 2:
        starter_code = starter_code or "import _____\nprint(_____.version)"
        options = options or ["sys", "os", "math", "platform"]
    elif topic_id == 3:
        starter_code = starter_code or "_____ = 5\ncount = count + 1\nprint(count)"
        options = options or ["count", "number", "price", "val"]
    elif topic_id == 4:
        starter_code = starter_code or "a = 10\nb = 2.5\nprint(_____(a).__name__, _____(b).__name__)"
        options = options or ["type", "int", "float", "print"]
    elif topic_id == 5:
        starter_code = starter_code or "x = '12'\nprint(_____(x) + 3)"
        options = options or ["int", "float", "str", "bool"]
    elif topic_id == 6:
        starter_code = starter_code or "a = 10\nb = 3\nprint(a _____ b, a % b)"
        options = options or ["//", "+", "*", "=="]
    elif topic_id == 7:
        starter_code = starter_code or "name = 'Learner'\nprint(f'Hi {_____}')"
        options = options or ["name", "text", "str", "input"]
    elif topic_id == 8:
        starter_code = starter_code or "score = 82\n_____ score >= 80:\n    print('A')\nelse:\n    print('B')"
        options = options or ["if", "elif", "else", "while"]
    elif topic_id == 9:
        starter_code = starter_code or "_____ i in range(1, 4):\n    print(i)"
        options = options or ["for", "while", "if", "def"]
    elif topic_id == 10:
        starter_code = starter_code or "_____ square(x):\n    return x * x\nprint(square(5))"
        options = options or ["def", "class", "lambda", "return"]
    elif topic_id == 11:
        starter_code = starter_code or "text = 'SkillExa'\nprint(_____[0:5])"
        options = options or ["text", "string", "str", "len"]
    elif topic_id == 12:
        starter_code = starter_code or "nums = [4, 2, 8]\nnums._____()\nprint(nums)"
        options = options or ["sort", "append", "pop", "reverse"]
    elif topic_id == 13:
        starter_code = starter_code or "pair = (1, 2)\nprint(_____[1])"
        options = options or ["pair", "tuple", "list", "dict"]
    elif topic_id == 14:
        starter_code = starter_code or "a = {1, 2, 3}\nb = {3, 4}\nprint(a _____ b)"
        options = options or ["&", "|", "^", "+"]
    elif topic_id == 15:
        starter_code = starter_code or "user = {'name': 'Ana', 'age': 20}\nprint(user['_____'])"
        options = options or ["name", "age", "user", "key"]
    elif topic_id == 16:
        starter_code = starter_code or "with _____'demo.txt', 'w') as f:\n    f.write('ok')\nwith open('demo.txt') as f:\n    print(f.read())"
        options = options or ["open(", "read(", "write(", "close("]
    elif topic_id == 17:
        starter_code = starter_code or "_____\n    int('abc')\nexcept ValueError:\n    print('invalid')"
        options = options or ["try:", "if:", "while:", "def:"]
    elif topic_id == 18:
        starter_code = starter_code or "import _____\nprint(math.sqrt(16))"
        options = options or ["math", "sys", "os", "random"]
    elif topic_id == 19:
        starter_code = starter_code or "_____ Greeter:\n    def hello(self):\n        return 'Hi'\nprint(Greeter().hello())"
        options = options or ["class", "def", "import", "object"]
    elif topic_id == 20:
        starter_code = starter_code or "import numpy as _____\na = np.array([1, 2, 3])\nprint((a * 2).tolist())"
        options = options or ["np", "numpy", "pd", "num"]
    elif topic_id == 21:
        starter_code = starter_code or "nums = [1, 2, 3]\nprint(list(map(_____ x: x * 2, nums)))"
        options = options or ["lambda", "def", "func", "for"]
    elif topic_id == 22:
        starter_code = starter_code or "def countdown(n):\n    while n:\n        _____ n\n        n -= 1\nprint(list(countdown(3)))"
        options = options or ["yield", "return", "print", "break"]
    elif topic_id == 23:
        starter_code = starter_code or "def ready(score):\n    _____ 'Pass' if score >= 70 else 'Retry'\nprint(ready(85))"
        options = options or ["return", "yield", "print", "if"]
    else:
        ex_code = str(example.get("code", ""))
        starter_code = starter_code or (ex_code.replace("print(", "____(", 1) if "print(" in ex_code else f"_____\n{ex_code}")
        options = options or ["print", "sys", "int", "input"]

    return {
        "title": compiler_raw.get("title", f"Practice {title}"),
        "question": compiler_raw.get("question", f"Click an option below to fill in the blanks in the example code, then click Run Code."),
        "starter_code": starter_code,
        "options": options,
    }


def _build_topic(topic_meta: dict[str, object]) -> dict[str, object]:
    topic_id = int(topic_meta["id"])
    core = TOPIC_CORE.get(topic_id, {})
    title = str(topic_meta["title"])

    theory = core.get("theory")
    if not isinstance(theory, dict):
        theory = {
            "definition": str(core.get("concept", "")),
            "why": f"{title} builds a foundation for practical Python work.",
            "rules": [
                "Read the syntax carefully before running the code.",
                "Change one value at a time when experimenting.",
                "Use print() to confirm what the program returns.",
            ],
            "examples": [str(core.get("example", ""))],
        }

    example = core.get("example")
    if not isinstance(example, dict):
        example = {
            "code": str(example or ""),
            "output": str(core.get("output", "")),
            "explanation": f"This example demonstrates {title.lower()} in action.",
        }

    fill_blanks = core.get("fill_blanks")
    if not isinstance(fill_blanks, dict):
        fill_blanks = {
            "question": f"Topic {topic_id} title is _______.",
            "answer": title,
        }

    compiler_raw = core.get("compiler")
    if not isinstance(compiler_raw, dict):
        compiler_raw = {}

    compiler = _build_programming_exercise(topic_id, title, example, fill_blanks, compiler_raw)

    skill_exa_test = core.get("skill_exa_test")
    if not isinstance(skill_exa_test, list):
        skill_exa_test = [
            {
                "question": f"Which topic number corresponds to {title}?",
                "options": [str(topic_id), "1", "10", "20"],
                "answer": str(topic_id),
            }
        ]

    practice = core.get("practice")
    if not isinstance(practice, list):
        practice = [
            f"Write one short program that demonstrates {title}.",
            "Add input validation and clear output formatting.",
            "Refactor your code into at least one function.",
            "Test with normal, edge, and invalid inputs.",
            "Document what you learned in 3-5 lines.",
        ]

    completion = core.get("completion")
    if not isinstance(completion, dict):
        completion = {
            "xp": 50,
            "badge": f"{title} Beginner",
            "unlock_next": topic_id + 1,
        }

    theory_definition = str(core.get("concept") or theory.get("definition") or theory.get("overview") or "")

    return {
        "id": topic_id,
        "title": title,
        "difficulty": topic_meta["difficulty"],
        "duration": topic_meta["duration"],
        "concept": theory_definition,
        "syntax": str(core.get("syntax", "")),
        "example": example,
        "output": str(example.get("output", core.get("output", ""))),
        "theory": theory,
        "fill_blanks": fill_blanks,
        "compiler": compiler,
        "skill_exa_test": skill_exa_test,
        "completion": completion,
        "notes": [
            f"{title} is part of the SkillExa guided Python path.",
            "Review syntax first, then run the example code.",
            "Practice with at least one custom variation.",
            "Focus on correctness before optimization.",
            "Revisit the quiz to reinforce retention.",
        ],
        "quiz": skill_exa_test,
        "practice": practice,
        "mastery_test": {"mcq": 5, "coding": 2, "passing_marks": 70},
    }


PYTHON_TOPICS = {item["id"]: _build_topic(item) for item in TOPIC_CATALOG}
