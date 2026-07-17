"""FastAPI router for the Python learning curriculum."""
from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(prefix="/python", tags=["Python"])


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
        "concept": "Install Python and verify it in terminal using python --version.",
        "syntax": "python --version",
        "example": "import sys\nprint(sys.version.split()[0])",
        "output": "3.x",
    },
    3: {
        "concept": "Variables store values and can change type dynamically in Python.",
        "syntax": "name = 'SkillExa'",
        "example": "count = 5\ncount = count + 1\nprint(count)",
        "output": "6",
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
    core = TOPIC_CORE[topic_id]
    title = str(topic_meta["title"])

    return {
        "id": topic_id,
        "title": title,
        "difficulty": topic_meta["difficulty"],
        "duration": topic_meta["duration"],
        "concept": core["concept"],
        "syntax": core["syntax"],
        "example": core["example"],
        "output": core["output"],
        "notes": [
            f"{title} is part of the SkillExa guided Python path.",
            "Review syntax first, then run the example code.",
            "Practice with at least one custom variation.",
            "Focus on correctness before optimization.",
            "Revisit the quiz to reinforce retention.",
        ],
        "fill_blanks": [
            {"question": f"Topic {topic_id} title is _______.", "answer": title},
            {"question": "Python files use the .___ extension.", "answer": "py"},
            {"question": "A reusable block of code is called a _______.", "answer": "function"},
            {"question": "Errors can be handled using try and _______.", "answer": "except"},
            {"question": "Lists in Python are _______ (mutable/immutable).", "answer": "mutable"},
        ],
        "quiz": [
            {
                "question": f"Which topic number corresponds to {title}?",
                "options": [str(topic_id), "1", "10", "20"],
                "answer": str(topic_id),
            },
            {
                "question": "Which keyword defines a function in Python?",
                "options": ["func", "def", "function", "lambda"],
                "answer": "def",
            },
            {
                "question": "Which collection type is mutable?",
                "options": ["tuple", "str", "list", "frozenset"],
                "answer": "list",
            },
            {
                "question": "Which statement handles exceptions?",
                "options": ["if", "for", "try", "with"],
                "answer": "try",
            },
            {
                "question": "Which operator checks equality?",
                "options": ["=", "==", "!=", ">="],
                "answer": "==",
            },
            {
                "question": "What does input() return by default?",
                "options": ["int", "float", "str", "bool"],
                "answer": "str",
            },
            {
                "question": "Which built-in gets sequence length?",
                "options": ["size", "count", "len", "length"],
                "answer": "len",
            },
            {
                "question": "Which loop is condition based?",
                "options": ["for", "while", "repeat", "foreach"],
                "answer": "while",
            },
            {
                "question": "Which one is a dictionary literal?",
                "options": ["[]", "()", "{}", "<>"],
                "answer": "{}",
            },
            {
                "question": "Which keyword imports a module?",
                "options": ["include", "require", "import", "using"],
                "answer": "import",
            },
        ],
        "practice": [
            f"Write one short program that demonstrates {title}.",
            "Add input validation and clear output formatting.",
            "Refactor your code into at least one function.",
            "Test with normal, edge, and invalid inputs.",
            "Document what you learned in 3-5 lines.",
        ],
        "mastery_test": {"mcq": 5, "coding": 2, "passing_marks": 70},
    }


PYTHON_TOPICS = {item["id"]: _build_topic(item) for item in TOPIC_CATALOG}


@router.get("/topics")
def get_python_topics() -> dict[str, object]:
    """Return the topic list shown in the learning path."""
    return {
        "success": True,
        "total_topics": len(TOPIC_CATALOG),
        "topics": TOPIC_CATALOG,
    }


@router.get("/topics/{topic_id}")
def get_topic_details(topic_id: int) -> dict[str, object]:
    """Return full content for a single topic id."""
    topic = PYTHON_TOPICS.get(topic_id)
    if topic is None:
        return {
            "success": False,
            "message": "Topic not found",
        }

    return {
        "success": True,
        "topic": topic,
    }
