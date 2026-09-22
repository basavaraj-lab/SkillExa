"""Curriculum dataset catalog and content builder for 65 Python topics across 8 modules."""
from __future__ import annotations

TOPIC_CATALOG = [
    # 1. Python Fundamentals
    {"id": 1, "title": "Introduction", "difficulty": "Beginner", "duration": "20 min", "category": "Python Fundamentals"},
    {"id": 2, "title": "Applications", "difficulty": "Beginner", "duration": "15 min", "category": "Python Fundamentals"},
    {"id": 3, "title": "Input and Output", "difficulty": "Beginner", "duration": "25 min", "category": "Python Fundamentals"},
    {"id": 4, "title": "Variables", "difficulty": "Beginner", "duration": "20 min", "category": "Python Fundamentals"},
    {"id": 5, "title": "Operators", "difficulty": "Beginner", "duration": "25 min", "category": "Python Fundamentals"},
    {"id": 6, "title": "Keywords", "difficulty": "Beginner", "duration": "15 min", "category": "Python Fundamentals"},
    {"id": 7, "title": "Data Types", "difficulty": "Beginner", "duration": "25 min", "category": "Python Fundamentals"},
    {"id": 8, "title": "Conditional Statements", "difficulty": "Beginner", "duration": "30 min", "category": "Python Fundamentals"},
    {"id": 9, "title": "Loops", "difficulty": "Intermediate", "duration": "35 min", "category": "Python Fundamentals"},
    {"id": 10, "title": "Functions", "difficulty": "Intermediate", "duration": "30 min", "category": "Python Fundamentals"},
    {"id": 11, "title": "Pass in Functions", "difficulty": "Intermediate", "duration": "20 min", "category": "Python Fundamentals"},
    {"id": 12, "title": "Global and Local Variables", "difficulty": "Intermediate", "duration": "25 min", "category": "Python Fundamentals"},
    {"id": 13, "title": "Recursion", "difficulty": "Intermediate", "duration": "35 min", "category": "Python Fundamentals"},
    {"id": 14, "title": "*args and **kwargs in Functions", "difficulty": "Intermediate", "duration": "30 min", "category": "Python Fundamentals"},
    {"id": 15, "title": "First-Class Functions", "difficulty": "Intermediate", "duration": "30 min", "category": "Python Fundamentals"},
    {"id": 16, "title": "Lambda Functions", "difficulty": "Intermediate", "duration": "25 min", "category": "Python Fundamentals"},
    {"id": 17, "title": "Map, Reduce and Filter Functions", "difficulty": "Intermediate", "duration": "30 min", "category": "Python Fundamentals"},

    # 2. Python Built-in Data Structures & Utilities
    {"id": 18, "title": "Counters", "difficulty": "Intermediate", "duration": "25 min", "category": "Built-in Data Structures & Utilities"},
    {"id": 19, "title": "heapq", "difficulty": "Intermediate", "duration": "30 min", "category": "Built-in Data Structures & Utilities"},
    {"id": 20, "title": "deque", "difficulty": "Intermediate", "duration": "25 min", "category": "Built-in Data Structures & Utilities"},
    {"id": 21, "title": "OrderedDict", "difficulty": "Intermediate", "duration": "20 min", "category": "Built-in Data Structures & Utilities"},
    {"id": 22, "title": "defaultdict", "difficulty": "Intermediate", "duration": "25 min", "category": "Built-in Data Structures & Utilities"},
    {"id": 23, "title": "Decorators", "difficulty": "Advanced", "duration": "35 min", "category": "Built-in Data Structures & Utilities"},
    {"id": 24, "title": "Strings", "difficulty": "Intermediate", "duration": "30 min", "category": "Built-in Data Structures & Utilities"},
    {"id": 25, "title": "Lists", "difficulty": "Intermediate", "duration": "30 min", "category": "Built-in Data Structures & Utilities"},
    {"id": 26, "title": "Tuples", "difficulty": "Intermediate", "duration": "25 min", "category": "Built-in Data Structures & Utilities"},
    {"id": 27, "title": "Dictionaries", "difficulty": "Intermediate", "duration": "30 min", "category": "Built-in Data Structures & Utilities"},
    {"id": 28, "title": "Sets", "difficulty": "Intermediate", "duration": "25 min", "category": "Built-in Data Structures & Utilities"},
    {"id": 29, "title": "Arrays", "difficulty": "Intermediate", "duration": "25 min", "category": "Built-in Data Structures & Utilities"},
    {"id": 30, "title": "List Comprehension", "difficulty": "Intermediate", "duration": "30 min", "category": "Built-in Data Structures & Utilities"},

    # 3. Object-Oriented Programming (OOP)
    {"id": 31, "title": "OOP Concepts", "difficulty": "Intermediate", "duration": "30 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 32, "title": "Python OOP", "difficulty": "Intermediate", "duration": "30 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 33, "title": "Classes and Objects", "difficulty": "Intermediate", "duration": "35 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 34, "title": "Constructors", "difficulty": "Intermediate", "duration": "25 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 35, "title": "self as Default Argument", "difficulty": "Intermediate", "duration": "20 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 36, "title": "Polymorphism", "difficulty": "Advanced", "duration": "35 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 37, "title": "Inheritance", "difficulty": "Advanced", "duration": "35 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 38, "title": "Abstraction", "difficulty": "Advanced", "duration": "30 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 39, "title": "Encapsulation", "difficulty": "Advanced", "duration": "30 min", "category": "Object-Oriented Programming (OOP)"},

    # 4. Iterators & Exception Handling
    {"id": 40, "title": "Iterators", "difficulty": "Intermediate", "duration": "30 min", "category": "Iterators & Exception Handling"},
    {"id": 41, "title": "Exception Handling", "difficulty": "Intermediate", "duration": "30 min", "category": "Iterators & Exception Handling"},
    {"id": 42, "title": "Built-in Exceptions", "difficulty": "Intermediate", "duration": "25 min", "category": "Iterators & Exception Handling"},
    {"id": 43, "title": "User-Defined Exceptions", "difficulty": "Intermediate", "duration": "30 min", "category": "Iterators & Exception Handling"},

    # 5. File & Directory Handling
    {"id": 44, "title": "File Handling", "difficulty": "Intermediate", "duration": "30 min", "category": "File & Directory Handling"},
    {"id": 45, "title": "Read Files", "difficulty": "Intermediate", "duration": "25 min", "category": "File & Directory Handling"},
    {"id": 46, "title": "Write/Create Files", "difficulty": "Intermediate", "duration": "25 min", "category": "File & Directory Handling"},
    {"id": 47, "title": "OS Module", "difficulty": "Intermediate", "duration": "35 min", "category": "File & Directory Handling"},
    {"id": 48, "title": "pathlib Module", "difficulty": "Intermediate", "duration": "30 min", "category": "File & Directory Handling"},
    {"id": 49, "title": "Directory Management", "difficulty": "Intermediate", "duration": "30 min", "category": "File & Directory Handling"},

    # 6. Databases
    {"id": 50, "title": "MongoDB Introduction", "difficulty": "Advanced", "duration": "40 min", "category": "Databases"},
    {"id": 51, "title": "MySQL Introduction", "difficulty": "Advanced", "duration": "40 min", "category": "Databases"},

    # 7. Python Packages & Libraries
    {"id": 52, "title": "Packages", "difficulty": "Intermediate", "duration": "30 min", "category": "Python Packages & Libraries"},
    {"id": 53, "title": "Built-in Modules", "difficulty": "Intermediate", "duration": "30 min", "category": "Python Packages & Libraries"},
    {"id": 54, "title": "DSA Libraries", "difficulty": "Advanced", "duration": "35 min", "category": "Python Packages & Libraries"},
    {"id": 55, "title": "GUI Libraries", "difficulty": "Advanced", "duration": "40 min", "category": "Python Packages & Libraries"},

    # 8. Data Science
    {"id": 56, "title": "NumPy", "difficulty": "Advanced", "duration": "40 min", "category": "Data Science"},
    {"id": 57, "title": "Pandas", "difficulty": "Advanced", "duration": "45 min", "category": "Data Science"},
    {"id": 58, "title": "Matplotlib", "difficulty": "Advanced", "duration": "40 min", "category": "Data Science"},
    {"id": 59, "title": "Seaborn", "difficulty": "Advanced", "duration": "40 min", "category": "Data Science"},
    {"id": 60, "title": "Statsmodels", "difficulty": "Advanced", "duration": "45 min", "category": "Data Science"},
    {"id": 61, "title": "Scikit-learn", "difficulty": "Advanced", "duration": "50 min", "category": "Data Science"},
    {"id": 62, "title": "XGBoost / LightGBM", "difficulty": "Advanced", "duration": "50 min", "category": "Data Science"},
    {"id": 63, "title": "TensorFlow and Keras", "difficulty": "Advanced", "duration": "55 min", "category": "Data Science"},
    {"id": 64, "title": "PyTorch", "difficulty": "Advanced", "duration": "55 min", "category": "Data Science"},
    {"id": 65, "title": "Complete Tutorial on Data Science", "difficulty": "Advanced", "duration": "60 min", "category": "Data Science"},
]

TOPIC_CORE = {
    1: {
        'concept': 'Python is a high-level programming language known for its simple and readable syntax. It allows writing clean code with fewer lines and supports multiple programming paradigms including object-oriented, functional, and procedural programming. Widely used in web development, automation, data analysis, artificial intelligence, and many other fields. Python is dynamically typed and features automatic garbage collection.',
        'syntax': '# Hello World Program in Python\nprint("Hello, World!")',
        'example': {
            'code': '# This is a comment. It will not be executed.\nprint("Hello, World!")',
            'output': 'Hello, World!',
            'explanation': '1. print() is a built-in Python function that instructs the computer to display text on the screen.\n2. "Hello, World!" is a string enclosed within quotes (either single \' or double ").\n3. Python uses indentation (spaces or tabs) to define code blocks instead of braces {} in C, C++, and Java.\n4. \'#\' is used to write comments in Python. Comments are ignored during execution.',
        },
        'fill_blanks': {
            'question': '# Display output on the screen\n_____("Hello, World!")\n',
            'answers': ['print'],
            'options': [
                'print',
                'input',
                'write',
                'display',
            ],
        },
        'compiler': {
            'title': 'Hello World Sandbox',
            'question': 'Fill in the built-in function to display text.',
            'starter_code': '_____("Hello, World!")',
            'options': [
                'print',
                'input',
                'echo',
                'printf',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'Which symbol is used to write single-line comments in Python?',
                'options': [
                    '#',
                    '//',
                    '/*',
                    '--',
                ],
                'answer': '#',
            },
            {
                'question': 'How does Python delimit blocks of code such as loops and function definitions?',
                'options': [
                    'Whitespace Indentation',
                    'Curly Braces {}',
                    'Begin/End Keywords',
                    'Semicolons ;',
                ],
                'answer': 'Whitespace Indentation',
            },
            {
                'question': 'Which built-in Python function displays text or variables on the screen?',
                'options': [
                    'print()',
                    'console.log()',
                    'printf()',
                    'write()',
                ],
                'answer': 'print()',
            },
            {
                'question': 'Which feature allows Python variables to change data types dynamically during execution?',
                'options': [
                    'Dynamic Typing',
                    'Static Typing',
                    'Manual Memory Allocation',
                    'Explicit Declaration',
                ],
                'answer': 'Dynamic Typing',
            },
            {
                'question': 'What process in Python reclaims memory occupied by unreferenced objects automatically?',
                'options': [
                    'Automatic Garbage Collection',
                    'Manual Pointer Deallocation',
                    'Stack Unwinding',
                    'Virtual Memory Swapping',
                ],
                'answer': 'Automatic Garbage Collection',
            },
        ],
        'theory': {
            'definition': 'Python is a high-level, interpreted programming language known for simple readable syntax and multi-paradigm support.',
            'why': 'Python reduces writing lines of code, manages memory automatically via garbage collection, and is industry-standard for web, AI, and automation.',
            'rules': [
                'Indentation (spaces or tabs) defines code block scope.',
                "Comments start with '#' and are completely ignored during execution.",
                'Double quotes or single quotes enclose string literals.',
            ],
            'examples': ['print("Hello, World!")'],
        },
    },
    2: {
        'concept': 'Python is widely used across industries, powering applications in Web Development (Django, Flask), Data Science & Analysis (Pandas, NumPy, Matplotlib), Machine Learning & AI (TensorFlow, PyTorch, Scikit-learn), Automation & Scripting, Game Development (Pygame), Web Scraping (BeautifulSoup, Scrapy), Desktop GUIs (Tkinter, PyQt), Scientific Computing (SciPy, SymPy), Internet of Things (MicroPython), DevOps, and Cybersecurity. Major companies like YouTube, Instagram, Spotify, Dropbox, Netflix, Google, Uber, and Pinterest rely heavily on Python. Advantages include rich third-party modules, extensive libraries, open source community, dynamic typing, and OOP support. Disadvantages include interpreted execution speed trade-offs, Global Interpreter Lock (GIL) threading constraints, and high memory consumption.',
        'syntax': '# Python Ecosystem Frameworks\n# Web: Django, Flask | ML: PyTorch, TensorFlow | Data: Pandas, NumPy',
        'example': {
            'code': '# Real World Application Domains\ntech_stack = {\n    "Web": ["Django", "Flask"],\n    "Data Science": ["Pandas", "NumPy"],\n    "AI/ML": ["TensorFlow", "PyTorch"]\n}\nfor domain, tools in tech_stack.items():\n    print(f"{domain} -> {\', \'.join(tools)}")',
            'output': 'Web -> Django, Flask\nData Science -> Pandas, NumPy\nAI/ML -> TensorFlow, PyTorch',
            'explanation': '1. Python dictionaries and lists group industry-standard frameworks by domain.\n2. Expressive syntax allows iteration and formatting with minimal code lines.',
        },
        'fill_blanks': {
            'question': '# Data science library in Python\nimport _____ as pd\n',
            'answers': ['pandas'],
            'options': [
                'pandas',
                'django',
                'pygame',
                'tkinter',
            ],
        },
        'compiler': {
            'title': 'Python Applications Sandbox',
            'question': 'Print Python ecosystem application domains.',
            'starter_code': 'apps = ["Web", "Data Science", "AI"]\nfor a in apps:\n    _____ (f"Python Domain: {a}")',
            'options': [
                'print',
                'input',
                'sys',
                'open',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'Which Python framework is widely used for enterprise web backend development?',
                'options': [
                    'Django',
                    'Pygame',
                    'BeautifulSoup',
                    'NumPy',
                ],
                'answer': 'Django',
            },
            {
                'question': 'What feature of CPython limits multi-threaded parallel execution on multiple CPU cores?',
                'options': [
                    'Global Interpreter Lock (GIL)',
                    'Automatic Garbage Collection',
                    'Dynamic Typing',
                    'Bytecode Compiler',
                ],
                'answer': 'Global Interpreter Lock (GIL)',
            },
            {
                'question': 'Which library is standard for data manipulation and analysis in Python?',
                'options': [
                    'Pandas',
                    'Flask',
                    'PyQt',
                    'Scrapy',
                ],
                'answer': 'Pandas',
            },
            {
                'question': 'Which major video sharing platform relies on Python for video streaming and backend services?',
                'options': [
                    'YouTube',
                    'Linux Kernel',
                    'MySQL',
                    'Git CLI',
                ],
                'answer': 'YouTube',
            },
            {
                'question': 'Which of the following is considered a primary advantage of Python?',
                'options': [
                    'Extensive third-party modules & standard libraries',
                    'Execution speed faster than C',
                    'No garbage collection needed',
                    'Mandatory explicit variable declarations',
                ],
                'answer': 'Extensive third-party modules & standard libraries',
            },
        ],
        'theory': {
            'definition': 'Python applications span full-stack web development, AI models, data pipelines, automation scripts, and cloud microservices.',
            'why': 'Massive library ecosystem and active open-source community enable rapid prototyping and enterprise scaling.',
            'rules': [
                'Select frameworks appropriate for domain requirements (e.g., Flask vs Django).',
                'Be aware of execution speed differences when running CPU-intensive operations.',
                'Use virtual environments (venv) to manage package dependencies.',
            ],
            'examples': ['import pandas as pd', 'import numpy as np'],
        },
    },
    3: {
        'concept': 'The print() function displays text, variables, and expressions on the console. Multiple variables can be printed separated by commas. The input() function enables interaction with users, returning keyboard input as a string by default. Typecasting (int(), float()) converts string input to numeric types, and the split() method allows taking multiple space-separated inputs in a single line.',
        'syntax': '# Input and Output Syntax\nname = input("Enter name: ")\nx, y = input("Enter two numbers: ").split()\nprint("Hello,", name, sep=" ")',
        'example': {
            'code': '# Taking multiple inputs & typecasting\nx, y = input("Enter two numbers: ").split()\ni, f = int(x), float(y)\nprint("Integer:", i, "Float:", f)\nprint("Sum:", i + f)',
            'output': 'Enter two numbers: 10 20.5\nInteger: 10 Float: 20.5\nSum: 30.5',
            'explanation': '1. input().split() takes space-separated inputs into x and y.\n2. int() and float() typecast input strings to numerical values.\n3. print() displays formatted string literals and computed expressions.',
        },
        'fill_blanks': {
            'question': '# Read user input as string\nname = _____("Enter your name: ")\nprint("Hello,", name)',
            'answers': ['input'],
            'options': [
                'input',
                'print',
                'scan',
                'read',
            ],
        },
        'compiler': {
            'title': 'Taking User Input Sandbox',
            'question': 'Complete the input function call.',
            'starter_code': 'val = _____("Enter something: ")\nprint("You entered:", val)',
            'options': [
                'input',
                'print',
                'scan',
                'read',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What data type does the input() function return by default in Python?',
                'options': [
                    'str (String)',
                    'int (Integer)',
                    'float (Float)',
                    'Depends on user input',
                ],
                'answer': 'str (String)',
            },
            {
                'question': 'How can you read multiple space-separated input values in a single line in Python?',
                'options': [
                    'input().split()',
                    'input().read_all()',
                    'input().parse()',
                    'input().tokens()',
                ],
                'answer': 'input().split()',
            },
            {
                'question': 'How do you convert string input into an integer in Python?',
                'options': [
                    'int(input())',
                    'str(input())',
                    'float(input())',
                    'parse_int(input())',
                ],
                'answer': 'int(input())',
            },
            {
                'question': 'Which parameter of print() specifies the character inserted between multiple printed values?',
                'options': [
                    'sep',
                    'end',
                    'delimiter',
                    'join',
                ],
                'answer': 'sep',
            },
            {
                'question': "What will print('Brad', 25, 'New York') output by default?",
                'options': [
                    'Brad 25 New York',
                    'Brad,25,New York',
                    'Brad25New York',
                    "('Brad', 25, 'New York')",
                ],
                'answer': 'Brad 25 New York',
            },
        ],
        'theory': {
            'definition': 'Input/Output functions handle user interactions and console communication in Python programs.',
            'why': 'input() captures user feedback; print() displays computed results, status logs, and debug info.',
            'rules': [
                'input() always returns string type data.',
                'Use typecasting like int(input()) for arithmetic computations.',
                'Use split() to separate single-line multiple inputs into distinct variables.',
            ],
            'examples': [
                "name = input('Enter name: ')",
                "print('Hello,', name)",
            ],
        },
    },
    4: {
        'concept': 'Variables store data that can be referenced and manipulated during program execution. Python variables do not require explicit type declaration; the type is inferred dynamically based on the assigned value. Rules for variable names: can contain letters, digits, underscores (_); cannot start with a digit; case-sensitive (myVar != myvar); keywords cannot be used. Python uses Object References: variables store references to objects on the heap. Shared references occur when multiple variables point to the same object. The del keyword deletes a variable reference from memory.',
        'syntax': 'x = 5\nname = "Alex"\na, b = 5, 10    # Multiple assignment\na, b = b, a    # Swapping values\ndel x',
        'example': {
            'code': '# Variable Assignment, Object Reference & Swapping\na, b = 5, 10\nprint("Before swap:", a, b)\na, b = b, a    # Atomic swap using tuple unpacking\nprint("After swap:", a, b)',
            'output': 'Before swap: 5 10\nAfter swap: 10 5',
            'explanation': '1. Python supports multiple assignment on a single line.\n2. a, b = b, a swaps variable references atomically without needing a temporary variable.\n3. Python variables hold references to heap objects.',
        },
        'fill_blanks': {
            'question': '# Delete variable x from memory\nx = 10\n_____ x\n# print(x) raises NameError',
            'answers': ['del'],
            'options': [
                'del',
                'remove',
                'pop',
                'clear',
            ],
        },
        'compiler': {
            'title': 'Variable Swapping Sandbox',
            'question': 'Swap values of x and y in a single line.',
            'starter_code': 'x, y = 10, 20\nx, y = _____, _____\nprint(x, y)',
            'options': [
                'y, x',
                'x, y',
                '10, 20',
                '0, 0',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'Which of the following is a valid Python variable name?',
                'options': [
                    '_total_score',
                    '1name',
                    'class',
                    'user-name',
                ],
                'answer': '_total_score',
            },
            {
                'question': 'What happens when executing y = x in Python?',
                'options': [
                    'y references the same memory object as x (shared reference)',
                    'A deep copy of x is created',
                    'x is deleted from memory',
                    'TypeError is raised',
                ],
                'answer': 'y references the same memory object as x (shared reference)',
            },
            {
                'question': 'Which keyword deletes a variable reference from memory in Python?',
                'options': [
                    'del',
                    'remove',
                    'clear',
                    'pop',
                ],
                'answer': 'del',
            },
            {
                'question': 'What exception is raised if you access a variable after executing del on it?',
                'options': [
                    'NameError',
                    'ValueError',
                    'KeyError',
                    'AttributeError',
                ],
                'answer': 'NameError',
            },
            {
                'question': 'How do you swap two variables a and b in a single line in Python?',
                'options': [
                    'a, b = b, a',
                    'swap(a, b)',
                    'a = b; b = a',
                    'a <-> b',
                ],
                'answer': 'a, b = b, a',
            },
        ],
        'theory': {
            'definition': 'A variable is a symbolic name bound to an object reference in Python memory.',
            'why': 'Variables allow storing, retrieving, and updating references dynamically without explicit memory allocation.',
            'rules': [
                'Names start with a letter or underscore (_).',
                'Names cannot be reserved Python keywords.',
                'Names are case-sensitive.',
            ],
            'examples': ['x = 5', 'a, b = b, a', 'del x'],
        },
    },
    5: {
        'concept': 'Operators perform operations on values and variables. Python supports Arithmetic (+, -, *, /, floor division //, modulus %, exponentiation **), Comparison (>, <, ==, !=, >=, <=), Logical (and, or, not), Bitwise (&, |, ~, ^, >>, <<), Assignment (=, +=, -=, *=, <<=), Identity (is, is not - object memory location check), Membership (in, not in - sequence presence check), and Ternary conditional expressions (on_true if condition else on_false). Precedence and associativity dictate evaluation order.',
        'syntax': 'expr = 10 + 20 * 30\nmin_val = a if a < b else b\nis_present = x in my_list\nis_same = a is c',
        'example': {
            'code': '# Arithmetic, Floor Division, Ternary & Membership\na, b = 15, 4\nprint("Division / :", a / b)\nprint("Floor Division // :", a // b)\nprint("Modulus % :", a % b)\nmin_val = a if a < b else b\nprint("Ternary Min:", min_val)',
            'output': 'Division / : 3.75\nFloor Division // : 3\nModulus % : 3\nTernary Min: 4',
            'explanation': '1. Standard division / returns float 3.75, floor division // returns integer 3.\n2. % returns remainder 3.\n3. Ternary operator evaluates condition a < b in a single line.',
        },
        'fill_blanks': {
            'question': '# Check membership in list\nnums = [10, 20, 30]\nres = 20 _____ nums\nprint(res)',
            'answers': ['in'],
            'options': [
                'in',
                'is',
                '==',
                'and',
            ],
        },
        'compiler': {
            'title': 'Operators Sandbox',
            'question': 'Use floor division operator //.',
            'starter_code': 'a, b = 15, 4\nres = a _____ b\nprint(res)',
            'options': [
                '//',
                '/',
                '%',
                '**',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the primary difference between standard division (/) and floor division (//) in Python?',
                'options': [
                    '/ returns a float result; // returns an integer floor result',
                    '// returns a float; / returns an integer',
                    '/ rounds up; // rounds down',
                    'There is no difference',
                ],
                'answer': '/ returns a float result; // returns an integer floor result',
            },
            {
                'question': 'Which operator checks whether two variables reference the exact same memory object?',
                'options': [
                    'is',
                    '==',
                    'in',
                    'equals',
                ],
                'answer': 'is',
            },
            {
                'question': 'What is the correct syntax for the ternary conditional operator in Python?',
                'options': [
                    '[on_true] if [expression] else [on_false]',
                    '[expression] ? [on_true] : [on_false]',
                    'if [expression] then [on_true] else [on_false]',
                    '[on_true] ? [on_false]',
                ],
                'answer': '[on_true] if [expression] else [on_false]',
            },
            {
                'question': 'What is the evaluation result of 10 + 20 * 30 according to Python operator precedence?',
                'options': [
                    '610',
                    '900',
                    '700',
                    '3000',
                ],
                'answer': '610',
            },
            {
                'question': 'Which operator tests whether a value exists within a sequence like a list or string?',
                'options': [
                    'in',
                    'is',
                    'has',
                    'contains',
                ],
                'answer': 'in',
            },
        ],
        'theory': {
            'definition': 'Operators perform mathematical, logical, comparison, identity, bitwise, and membership computations across operands.',
            'why': 'Operators drive state transformations, conditional evaluation, and structural expressions in Python.',
            'rules': [
                'Multiplication/Division precedence exceeds Addition/Subtraction.',
                "'is' checks object identity; '==' checks value equality.",
                "Logical precedence order is 'not' > 'and' > 'or'.",
            ],
            'examples': ['x = 15 // 4  # 3', 'min_val = a if a < b else b'],
        },
    },
    6: {
        'concept': 'Keywords are special reserved words with predefined meanings in Python syntax. They define rules and structure and cannot be used as variable names, function names, classes, or identifiers. Python features 35+ keywords grouped by context: Value (True, False, None), Operator (and, or, not, is, in), Control Flow (if, else, elif, for, while, break, continue, pass, try, except, finally, raise, assert), Function/Class (def, return, lambda, yield, class), Context (with, as), Import (import, from), Scope (global, nonlocal), and Async (async, await). The keyword module provides kwlist and iskeyword().',
        'syntax': 'import keyword\nprint(keyword.kwlist)\nprint(keyword.iskeyword("for"))',
        'example': {
            'code': 'import keyword\nkw = keyword.kwlist\nprint("Total Keywords:", len(kw))\nprint("Is \'lambda\' a keyword?:", keyword.iskeyword("lambda"))',
            'output': "Total Keywords: 35\nIs 'lambda' a keyword?: True",
            'explanation': '1. keyword.kwlist returns all reserved Python keywords as a list.\n2. Using keywords as variable names (e.g. for = 10) causes a SyntaxError.',
        },
        'fill_blanks': {
            'question': '# Import keyword module\nimport _____\nprint(keyword.kwlist)',
            'answers': ['keyword'],
            'options': [
                'keyword',
                'sys',
                'os',
                'builtins',
            ],
        },
        'compiler': {
            'title': 'Keyword Module Sandbox',
            'question': 'Check keyword status using keyword.iskeyword().',
            'starter_code': "import _____\nprint('Is pass keyword:', keyword.iskeyword('pass'))",
            'options': [
                'keyword',
                'sys',
                'os',
                'type',
            ],
        },
        'skill_exa_test': [
            {
                'question': "What error is raised when attempting to assign a value to a keyword like 'for = 10'?",
                'options': [
                    'SyntaxError',
                    'ValueError',
                    'NameError',
                    'TypeError',
                ],
                'answer': 'SyntaxError',
            },
            {
                'question': 'Which of the following is a Python Value Keyword?',
                'options': [
                    'None',
                    'def',
                    'import',
                    'global',
                ],
                'answer': 'None',
            },
            {
                'question': 'Which built-in module provides the list of all Python reserved keywords?',
                'options': [
                    'keyword',
                    'sys',
                    'os',
                    'builtins',
                ],
                'answer': 'keyword',
            },
            {
                'question': 'Which keyword is used to modify a variable in an outer non-global scope within nested functions?',
                'options': [
                    'nonlocal',
                    'global',
                    'outer',
                    'parent',
                ],
                'answer': 'nonlocal',
            },
            {
                'question': 'Which statement accurately describes Keywords vs Identifiers?',
                'options': [
                    'Keywords are fixed reserved language words; Identifiers are user-defined names',
                    'Identifiers cannot be changed; Keywords can be redefined',
                    'Keywords store data; Identifiers run loops',
                    'There is no difference',
                ],
                'answer': 'Keywords are fixed reserved language words; Identifiers are user-defined names',
            },
        ],
        'theory': {
            'definition': 'Keywords are immutable reserved syntax words that dictate Python program architecture.',
            'why': 'Keywords maintain language integrity and define control flow, scope, declarations, and asynchronous execution.',
            'rules': [
                'Keywords cannot be used as variable names or identifiers.',
                'Keywords are case-sensitive (True is a keyword, true is an identifier).',
                'Use keyword.iskeyword() to check identifier validity.',
            ],
            'examples': [
                "import keyword\nprint(keyword.iskeyword('if'))",
            ],
        },
    },
    7: {
        'concept': 'Data types define the type of value stored in a variable and determine valid operations. Since Python treats everything as an object, each value has an associated class type. Categories include: Numeric (int, float, complex e.g. 2+3j), Sequence (str, list [ordered, mutable], tuple [ordered, immutable; single element requires trailing comma (1,)]), Boolean (bool: True/False with Truthy and Falsy evaluations like 0 and empty collections being Falsy), Set (set: unordered collection of unique elements), and Dictionary (dict: key:value pairs with unique keys).',
        'syntax': "a = 5         # int\nb = 5.0       # float\nc = 2 + 4j    # complex\ns = 'Text'    # str\nl = [1, 2]    # list\nt = (1,)      # tuple\ns1 = {1, 2}   # set\nd = {1: 'A'}  # dict",
        'example': {
            'code': '# Data Types & Single-Element Tuple\na = 5\nb = 5.0\nc = 2 + 4j\nt1 = (1,)    # Trailing comma creates single-element tuple\nd = {1: "Geeks", 2: "For"}\nprint(type(a).__name__, type(b).__name__, type(c).__name__, type(t1).__name__)\nprint("Dict value:", d[1])',
            'output': 'int float complex tuple\nDict value: Geeks',
            'explanation': '1. type() returns object class type.\n2. (1,) requires a trailing comma for Python to recognize it as a tuple.\n3. Dictionaries store key:value mappings accessed via keys.',
        },
        'fill_blanks': {
            'question': '# Trailing comma for single element tuple\nt = (1,_____)\nprint(type(t).__name__)',
            'answers': [','],
            'options': [
                ',',
                ')',
                ']',
                ';',
            ],
        },
        'compiler': {
            'title': 'Data Types Sandbox',
            'question': 'Check type of complex number.',
            'starter_code': 'c = 2 + 4j\nprint(_____(c).__name__)',
            'options': [
                'type',
                'int',
                'float',
                'str',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'Which Python class represents complex numbers with real and imaginary parts?',
                'options': [
                    'complex (e.g. 2+4j)',
                    'int',
                    'float',
                    'double',
                ],
                'answer': 'complex (e.g. 2+4j)',
            },
            {
                'question': 'How must a single-element tuple be declared in Python?',
                'options': [
                    'With a trailing comma (e.g. t = (1,))',
                    't = (1)',
                    't = tuple(1)',
                    'Single-element tuples are unsupported',
                ],
                'answer': 'With a trailing comma (e.g. t = (1,))',
            },
            {
                'question': 'What is the defining characteristic of Python sets?',
                'options': [
                    'Unordered collection of unique elements',
                    'Ordered sequence of duplicate elements',
                    'Key-value pair dictionary',
                    'Immutable list',
                ],
                'answer': 'Unordered collection of unique elements',
            },
            {
                'question': 'Which of the following evaluates to Falsy in a Python boolean context?',
                'options': [
                    '0',
                    '1',
                    "'Text'",
                    '[10]',
                ],
                'answer': '0',
            },
            {
                'question': 'Which data structure stores key:value pairs with unique, case-sensitive keys?',
                'options': [
                    'dict (Dictionary)',
                    'set',
                    'list',
                    'tuple',
                ],
                'answer': 'dict (Dictionary)',
            },
        ],
        'theory': {
            'definition': 'Data types classify data items and govern valid operations and memory representations.',
            'why': 'Selecting optimal data types ensures execution safety, performance efficiency, and clarity.',
            'rules': [
                'Numbers: int, float, complex.',
                'Tuples are immutable; Lists are mutable.',
                'Sets automatically eliminate duplicate elements.',
            ],
            'examples': [
                "d = {1: 'One', 2: 'Two'}",
                's = {1, 2, 2, 3}  # {1, 2, 3}',
            ],
        },
    },
    8: {
        'concept': "Conditional statements control program execution flow based on boolean conditions. Options include: 'if' statement, short-hand 'if', 'if-else', 'if-elif-else' ladders for evaluating multiple sequential conditions, nested 'if-else' statements, single-line ternary expressions, and structural 'match-case' statements (Python 3.10+) for pattern matching.",
        'syntax': 'if age >= 18:\n    print("Eligible")\nelif age >= 13:\n    print("Teen")\nelse:\n    print("Minor")\n\n# Match-Case\nmatch number:\n    case 1: print("One")\n    case 2 | 3: print("Two or Three")\n    case _: print("Other")',
        'example': {
            'code': '# If-elif-else & Match-Case Pattern Matching\nage = 25\nif age <= 12:\n    print("Child")\nelif age <= 19:\n    print("Teenager")\nelif age <= 35:\n    print("Young adult")\nelse:\n    print("Adult")\n\nnum = 2\nmatch num:\n    case 1: print("One")\n    case 2 | 3: print("Two or Three")\n    case _: print("Other number")',
            'output': 'Young adult\nTwo or Three',
            'explanation': "1. age=25 skips age<=12 and age<=19; age<=35 evaluates True, printing 'Young adult'.\n2. match num compares 2 against pattern 'case 2 | 3', printing 'Two or Three'.",
        },
        'fill_blanks': {
            'question': '# Wildcard default case in match statement\nval = 10\nmatch val:\n    case 1: print("One")\n    case _____: print("Other")',
            'answers': ['_'],
            'options': [
                '_',
                'else',
                'default',
                '*',
            ],
        },
        'compiler': {
            'title': 'Match-Case Branching Sandbox',
            'question': 'Complete the match wildcard case.',
            'starter_code': "num = 99\nmatch num:\n    case 1: print('One')\n    case _____: print('Other')",
            'options': [
                '_',
                'else',
                'other',
                'default',
            ],
        },
        'skill_exa_test': [
            {
                'question': "Which keyword is used to test multiple sequential conditions after an initial 'if' in Python?",
                'options': [
                    'elif',
                    'else if',
                    'elseif',
                    'case',
                ],
                'answer': 'elif',
            },
            {
                'question': 'What symbol represents the wildcard default case in a Python match-case statement?',
                'options': [
                    'case _:',
                    'case else:',
                    'case default:',
                    'case *:',
                ],
                'answer': 'case _:',
            },
            {
                'question': 'How is a single-line ternary conditional expression written in Python?',
                'options': [
                    "s = 'Adult' if age >= 18 else 'Minor'",
                    "s = age >= 18 ? 'Adult' : 'Minor'",
                    "s = if age >= 18 then 'Adult' else 'Minor'",
                    "s = 'Adult' ? 'Minor'",
                ],
                'answer': "s = 'Adult' if age >= 18 else 'Minor'",
            },
            {
                'question': 'In an if-elif-else ladder, how many branches will execute when a condition evaluates to True?',
                'options': [
                    'Only the first matching True branch',
                    'All True branches',
                    'Every branch in order',
                    'Only the else branch',
                ],
                'answer': 'Only the first matching True branch',
            },
            {
                'question': 'Which structural pattern matching statement was introduced in Python 3.10?',
                'options': [
                    'match-case',
                    'switch-case',
                    'select-case',
                    'branch-when',
                ],
                'answer': 'match-case',
            },
        ],
        'theory': {
            'definition': 'Conditional statements execute selective code blocks based on boolean condition evaluations.',
            'why': 'Branching control enables decision logic, dynamic input handling, and fallback execution paths.',
            'rules': [
                'Indentation dictates block ownership.',
                'elif chains evaluate in sequential order until one succeeds.',
                "match-case supports multi-pattern '|' matching and wildcard '_' fallbacks.",
            ],
            'examples': [
                "s = 'Adult' if age >= 18 else 'Minor'",
                "match val:\n    case 1: print('One')",
            ],
        },
    },
    9: {
        'concept': 'CHAPTER 1: FOR LOOPS & INDEXING — For loops iterate over sequences (lists, tuples, strings, ranges) directly or using sequence index positions with range(len(seq)).\n\nCHAPTER 2: WHILE LOOPS, INFINITE LOOPS & NESTED LOOPS — While loops execute repeatedly as long as a condition remains True. Features infinite while loops (while True: ...) and nested loops (loops inside loops) where the inner loop completes fully per outer loop step.',
        'syntax': '# === CHAPTER 1: FOR LOOPS & INDEXING ===\nfor i in range(0, n):\n    print(i)\n\nfor idx in range(len(seq)):\n    print(seq[idx])\n\n# === CHAPTER 2: WHILE LOOPS & NESTED LOOPS ===\nwhile condition:\n    # Body\n    break\n\nfor i in range(1, n):\n    for j in range(i):\n        print(i, end=" ")',
        'example': {
            'code': '# ==========================================\n# CHAPTER 1: FOR LOOPS & INDEXING\n# ==========================================\na = ["geeks", "for", "geeks"]\nprint("--- Iterating by Index ---")\nfor idx in range(len(a)):\n    print(f"Index {idx}: {a[idx]}")\n\n# ==========================================\n# CHAPTER 2: WHILE LOOPS & NESTED LOOPS\n# ==========================================\nprint("\\n--- While Loop Execution ---")\ncnt = 0\nwhile cnt < 3:\n    cnt += 1\n    print("Hello Geek", cnt)\n\nprint("\\n--- Nested Loops Pattern ---")\nfor i in range(1, 5):\n    for j in range(i):\n        print(i, end=" ")\n    print()',
            'output': '--- Iterating by Index ---\nIndex 0: geeks\nIndex 1: for\nIndex 2: geeks\n\n--- While Loop Execution ---\nHello Geek 1\nHello Geek 2\nHello Geek 3\n\n--- Nested Loops Pattern ---\n1 \n2 2 \n3 3 3 \n4 4 4 4 ',
            'explanation': '📌 CHAPTER 1: FOR LOOPS & INDEXING\n1. len(a) returns sequence length 3; range(len(a)) generates index values 0, 1, 2.\n2. a[idx] accesses sequence elements directly using their zero-based index positions.\n\n📌 CHAPTER 2: WHILE LOOPS & NESTED LOOPS\n3. cnt counter increments inside while loop body until condition cnt < 3 evaluates False.\n4. Outer for loop controls rows 1..4; inner loop prints current row number i repeated i times.',
        },
        'fill_blanks': {
            'question': '# Chapter 1: Iterate sequence by index\na = ["geeks", "for", "geeks"]\nfor idx in range(_____(a)):\n    print(a[idx])',
            'answers': ['len'],
            'options': [
                'len',
                'size',
                'count',
                'range',
            ],
        },
        'compiler': {
            'title': 'Nested Loops & While Sandbox',
            'question': 'Complete the inner range parameter for pattern printing.',
            'starter_code': 'for i in range(1, 5):\n    for j in range(_____):\n        print(i, end=" ")\n    print()',
            'options': [
                'i',
                '1',
                '5',
                '0',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What numbers are generated by range(0, 4) in Python?',
                'options': [
                    '0, 1, 2, 3',
                    '0, 1, 2, 3, 4',
                    '1, 2, 3, 4',
                    '0, 4',
                ],
                'answer': '0, 1, 2, 3',
            },
            {
                'question': 'How do you iterate through list elements using index positions in a for loop?',
                'options': [
                    'for idx in range(len(a)):',
                    'for idx in len(a):',
                    'for idx in a.index():',
                    'for idx in range(a):',
                ],
                'answer': 'for idx in range(len(a)):',
            },
            {
                'question': "What occurs when executing a while loop with condition 'while True' without a break statement?",
                'options': [
                    'Executes infinitely until forcefully terminated',
                    'Terminates after 100 iterations',
                    'Raises SyntaxError',
                    'Executes once',
                ],
                'answer': 'Executes infinitely until forcefully terminated',
            },
            {
                'question': 'How does a nested loop execute relative to the outer loop in Python?',
                'options': [
                    'The inner loop completes all its iterations for every single iteration of the outer loop',
                    'The inner and outer loops execute simultaneously',
                    'The outer loop completes before the inner loop starts',
                    'The inner loop runs only once',
                ],
                'answer': 'The inner loop completes all its iterations for every single iteration of the outer loop',
            },
            {
                'question': 'Which statement skips the remaining body of the current loop iteration and proceeds to the next iteration?',
                'options': [
                    'continue',
                    'break',
                    'pass',
                    'return',
                ],
                'answer': 'continue',
            },
        ],
        'theory': {
            'definition': 'Loops repeat statement execution until sequence elements are processed (For Loops) or condition becomes False (While Loops).',
            'why': 'Chapter 1 covers sequence indexing; Chapter 2 covers condition-driven while loops and multi-dimensional nested loops.',
            'rules': [
                'Chapter 1: Use range(len(seq)) for index-based sequence mutation or access.',
                'Chapter 2: Ensure while loop conditions eventually evaluate False to avoid infinite execution.',
                'Chapter 2: In nested loops, inner loops execute fully per outer loop step.',
            ],
            'examples': [
                'for idx in range(len(a)):\n    print(a[idx])',
                'while cnt < 3:\n    cnt += 1',
            ],
        },
    },
    10: {
        'concept': "CHAPTER 1: DEFINING, CALLING & ARGUMENT TYPES — Python functions are defined using def. Supports Default Arguments (y=50), Keyword Arguments (fname='Geeks', lname='Practice'), Positional Arguments, and Arbitrary Arguments (*args, **kwargs).\n\nCHAPTER 2: RETURN STATEMENT & PASS-BY-OBJECT-REFERENCE — Return sends calculated values back to the caller. Pass-by-object-reference mutates mutable objects (lists) in-place while keeping immutable objects (integers, strings) unchanged outside the function.",
        'syntax': '# === CHAPTER 1: DEFINING, CALLING & ARGUMENTS ===\ndef student(fname, lname):\n    print(fname, lname)\n\ndef my_fun(x, y=50):\n    print(x, y)\n\n# === CHAPTER 2: RETURN STATEMENT & MUTABILITY ===\ndef sq_value(num):\n    return num ** 2\n\ndef modify_list(lst):\n    lst[0] = 99',
        'example': {
            'code': '# ==========================================\n# CHAPTER 1: DEFINING & ARGUMENT TYPES\n# ==========================================\ndef student(fname, lname):\n    print("Name:", fname, lname)\n\ndef my_fun(x, y=50):\n    print(f"x: {x}, y: {y}")\n\nstudent(fname="Geeks", lname="Practice")\nmy_fun(10)\n\n# ==========================================\n# CHAPTER 2: RETURN STATEMENT & MUTABILITY\n# ==========================================\ndef sq_value(num):\n    return num ** 2\n\ndef modify_list(lst):\n    lst[0] = 20  # Mutable object in-place mutation\n\nprint("\\nSquare:", sq_value(4))\nnums = [10, 11, 12]\nmodify_list(nums)\nprint("Modified list:", nums)',
            'output': 'Name: Geeks Practice\nx: 10, y: 50\n\nSquare: 16\nModified list: [20, 11, 12]',
            'explanation': '📌 CHAPTER 1: DEFINING & ARGUMENT TYPES\n1. student() uses Keyword Arguments so argument order does not matter.\n2. my_fun(10) uses Default Argument y=50 when y is omitted.\n\n📌 CHAPTER 2: RETURN STATEMENT & MUTABILITY\n3. sq_value() uses return num**2 to send calculated result back to caller.\n4. modify_list() mutates list in-place because Python uses pass-by-object-reference for mutable objects.',
        },
        'fill_blanks': {
            'question': '# Chapter 1: Define function keyword\n_____ calc_square(n):\n    return n ** 2',
            'answers': ['def'],
            'options': [
                'def',
                'func',
                'function',
                'lambda',
            ],
        },
        'compiler': {
            'title': 'Functions & Mutability Sandbox',
            'question': 'Fill in the function definition keyword.',
            'starter_code': '_____ double_val(x):\n    return x * 2\nprint(double_val(8))',
            'options': [
                'def',
                'func',
                'function',
                'lambda',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'Which keyword is used to define a function in Python?',
                'options': [
                    'def',
                    'function',
                    'func',
                    'define',
                ],
                'answer': 'def',
            },
            {
                'question': 'What does a Python function return by default if no explicit return statement is executed?',
                'options': [
                    'None',
                    '0',
                    'False',
                    'Empty string ""',
                ],
                'answer': 'None',
            },
            {
                'question': 'How do default arguments behave in Python function definitions?',
                'options': [
                    'They provide predefined values if no value is passed during the function call',
                    'They force positional argument order',
                    'They make functions execute automatically',
                    'They raise a SyntaxError',
                ],
                'answer': 'They provide predefined values if no value is passed during the function call',
            },
            {
                'question': 'Which parameter passing model does Python use for functions?',
                'options': [
                    'Pass-by-object-reference',
                    'Strict pass-by-value only',
                    'Strict pass-by-pointer only',
                    'Macro substitution',
                ],
                'answer': 'Pass-by-object-reference',
            },
            {
                'question': 'What happens when a function modifies a mutable argument (like a list) passed into it?',
                'options': [
                    'The original list in the caller scope is modified',
                    'The original list remains unchanged',
                    'A TypeError is raised',
                    'The function creates a deep copy automatically',
                ],
                'answer': 'The original list in the caller scope is modified',
            },
        ],
        'theory': {
            'definition': 'Functions encapsulate execution logic. Chapter 1 covers definition and arguments; Chapter 2 covers return values and pass-by-object-reference.',
            'why': 'Chapter 1 organizes parameters; Chapter 2 explains return statements and how mutable/immutable object references behave.',
            'rules': [
                'Chapter 1: Keyword arguments allow passing parameters in any order.',
                'Chapter 1: Default arguments must follow positional arguments in def.',
                'Chapter 2: Mutable objects (lists, dicts) mutate in-place; immutable objects (ints, strings) do not.',
            ],
            'examples': ['def sq(n): return n**2', 'def mod(lst): lst[0]=99'],
        },
    },
    11: {
        'concept': 'The pass statement in Python is a placeholder that does nothing when executed. It keeps code blocks syntactically valid where statements are required but no implementation logic is needed yet. Common use cases for pass include empty functions, conditional block placeholders, loop iteration skips, and empty class or method stubs.',
        'syntax': 'def empty_function():\n    pass  # Placeholder for future logic\n\nclass EmptyClass:\n    pass',
        'example': {
            'code': '# Pass in Functions, Conditionals, Loops & Classes\ndef fun():\n    pass  # Function logic to be implemented later\n\nclass Person:\n    def __init__(self, name):\n        self.name = name\n    def greet(self):\n        pass  # Method placeholder\n\nfor i in range(5):\n    if i == 3:\n        pass  # Placeholder for i == 3\n    else:\n        print(i, end=" ")',
            'output': '0 1 2 4 ',
            'explanation': '1. pass statement acts as a no-operation placeholder so empty functions and class stubs compile without IndentationError.\n2. In the loop, when i == 3, pass executes doing nothing, so only 0, 1, 2, 4 are printed.',
        },
        'fill_blanks': {
            'question': '# Placeholder inside empty function\ndef empty_task():\n    _____\nempty_task()',
            'answers': ['pass'],
            'options': [
                'pass',
                'continue',
                'break',
                'return',
            ],
        },
        'compiler': {
            'title': 'Pass Statement Sandbox',
            'question': 'Fill in the pass placeholder keyword.',
            'starter_code': 'def future_logic():\n    _____\nfuture_logic()',
            'options': [
                'pass',
                'skip',
                'none',
                'null',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the primary purpose of the pass statement in Python?',
                'options': [
                    'To act as a syntactically valid placeholder that does nothing when executed',
                    'To terminate a function immediately',
                    'To skip to the next iteration of a loop',
                    'To delete a variable reference',
                ],
                'answer': 'To act as a syntactically valid placeholder that does nothing when executed',
            },
            {
                'question': 'What occurs when executing a function containing only the pass statement?',
                'options': [
                    'The function executes doing nothing and returns None without error',
                    'A SyntaxError is raised',
                    'The program crashes',
                    'An infinite loop is triggered',
                ],
                'answer': 'The function executes doing nothing and returns None without error',
            },
            {
                'question': 'In which scenarios is the pass statement commonly used?',
                'options': [
                    'Empty functions, class stubs, loop placeholders, and conditional branches',
                    'Only inside try-except blocks',
                    'Only inside database queries',
                    'Only for file I/O',
                ],
                'answer': 'Empty functions, class stubs, loop placeholders, and conditional branches',
            },
            {
                'question': 'How does pass differ from continue in a Python loop?',
                'options': [
                    'pass does nothing and continues statement execution; continue skips the rest of the current loop iteration',
                    'pass exits the loop; continue pauses it',
                    'pass is for numbers; continue is for strings',
                    'There is no difference',
                ],
                'answer': 'pass does nothing and continues statement execution; continue skips the rest of the current loop iteration',
            },
            {
                'question': 'Can pass be used to create an empty class definition in Python?',
                'options': [
                    'Yes, class EmptyClass: pass is syntactically valid',
                    'No, classes cannot use pass',
                    'Only if inherits from object',
                    'Only in Python 2',
                ],
                'answer': 'Yes, class EmptyClass: pass is syntactically valid',
            },
        ],
        'theory': {
            'definition': 'The pass statement is a null statement used as a placeholder when syntax requires a code block but no code needs execution.',
            'why': 'It allows stubbing out unwritten functions, classes, and conditional branches while building software architecture.',
            'rules': [
                'pass executes as a no-op.',
                'Use pass when designing API skeletons before writing internal logic.',
                'pass does not affect loop control flow like break or continue.',
            ],
            'examples': ['def stub():\n    pass'],
        },
    },
    12: {
        'concept': 'Variable scope defines the visibility and lifetime of a variable in Python. Local variables are declared inside a function, created when called, and destroyed when returned; they cannot be accessed outside the function (doing so raises NameError). Global variables are declared outside all functions and can be read anywhere. When a local variable shares a name with a global variable, the local variable shadows the global one inside the function. Modifying a global variable inside a function requires explicitly declaring it with the global keyword.',
        'syntax': 's = "Global"\n\ndef fun():\n    global s\n    s += " Modified"  # Mutates global variable\n    l_var = "Local"  # Local variable',
        'example': {
            'code': '# Global vs Local Scope & \'global\' Keyword\na = 1  # Global variable\n\ndef f():\n    print("f() global a:", a)\n\ndef g():\n    a = 2  # Local variable shadows global \'a\'\n    print("g() local a:", a)\n\ndef h():\n    global a\n    a = 3  # Modifies global \'a\'\n    print("h() modified global a:", a)\n\nf()\ng()\nprint("Outside g() global a:", a)\nh()\nprint("Outside h() global a:", a)',
            'output': 'f() global a: 1\ng() local a: 2\nOutside g() global a: 1\nh() modified global a: 3\nOutside h() global a: 3',
            'explanation': "1. f() accesses global 'a'.\n2. g() defines local 'a=2', shadowing global 'a' without changing it outside.\n3. h() uses 'global a' to modify the global variable value to 3.",
        },
        'fill_blanks': {
            'question': '# Declare global variable inside function\ndef modify_global():\n    _____ count\n    count += 1\n',
            'answers': ['global'],
            'options': [
                'global',
                'nonlocal',
                'public',
                'var',
            ],
        },
        'compiler': {
            'title': 'Global Scope Sandbox',
            'question': 'Use global keyword to modify global variable.',
            'starter_code': 'val = 100\ndef update():\n    _____ val\n    val += 50\nupdate()\nprint(val)',
            'options': [
                'global',
                'nonlocal',
                'static',
                'def',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What exception is raised if you try to print a local variable outside its defining function?',
                'options': [
                    'NameError',
                    'ValueError',
                    'AttributeError',
                    'ScopeError',
                ],
                'answer': 'NameError',
            },
            {
                'question': 'Which keyword must be used inside a function to modify a variable declared in the global scope?',
                'options': [
                    'global',
                    'nonlocal',
                    'outer',
                    'public',
                ],
                'answer': 'global',
            },
            {
                'question': 'What occurs when a local variable inside a function has the exact same name as a global variable?',
                'options': [
                    'The local variable shadows the global variable inside the function scope',
                    'A SyntaxError is raised',
                    'The global variable is deleted',
                    'The local variable becomes global',
                ],
                'answer': 'The local variable shadows the global variable inside the function scope',
            },
            {
                'question': "What error is raised if you attempt to modify a global variable inside a function without declaring it as 'global'?",
                'options': [
                    'UnboundLocalError',
                    'TypeError',
                    'ZeroDivisionError',
                    'IndexError',
                ],
                'answer': 'UnboundLocalError',
            },
            {
                'question': 'Where are local variables stored in memory during function execution?',
                'options': [
                    "In the function's local namespace (stack frame)",
                    'In the heap memory permanently',
                    'In a global database file',
                    'On the CPU disk cache',
                ],
                'answer': "In the function's local namespace (stack frame)",
            },
        ],
        'theory': {
            'definition': 'Scope defines the accessibility range of variables in a Python script (Local vs Global).',
            'why': 'Understanding scope prevents accidental variable overwrites, avoids UnboundLocalError, and structures clean state management.',
            'rules': [
                'Local variables exist only during function execution.',
                'Global variables are declared outside functions and read-accessible everywhere.',
                "Use 'global var_name' inside a function to modify a global variable.",
            ],
            'examples': [
                'count = 0\ndef inc():\n    global count\n    count += 1',
            ],
        },
    },
    13: {
        'concept': 'Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem by breaking it into smaller subproblems. Every recursive function requires two essential parts: 1. Base Case (a stopping condition that prevents infinite recursion and stack overflow) and 2. Recursive Case (calling the function with modified parameters). Recursion can be Tail Recursive (recursive call is the final action executed) or Non-Tail Recursive (further operations happen after the recursive call returns).',
        'syntax': 'def recursive_function(n):\n    if n <= 1:  # Base case\n        return base_result\n    else:  # Recursive case\n        return recursive_function(n - 1)',
        'example': {
            'code': '# Recursive Factorial & Fibonacci Sequence\ndef factorial(n):\n    if n <= 0:  # Base case\n        return 1\n    return n * factorial(n - 1)  # Recursive case\n\ndef fibonacci(n):\n    if n == 0:\n        return 0\n    elif n == 1:\n        return 1\n    return fibonacci(n - 1) + fibonacci(n - 2)\n\nprint("Factorial(5):", factorial(5))\nprint("Fibonacci(10):", fibonacci(10))',
            'output': 'Factorial(5): 120\nFibonacci(10): 55',
            'explanation': '1. factorial(5) calculates 5 * 4 * 3 * 2 * 1 = 120.\n2. Base cases stop infinite execution when n reaches 0 or 1.\n3. fibonacci(10) recursively sums fibonacci(9) and fibonacci(8).',
        },
        'fill_blanks': {
            'question': '# Base case in recursive factorial\ndef fact(n):\n    if n <= 0:\n        return _____\n    return n * fact(n - 1)',
            'answers': ['1'],
            'options': [
                '1',
                '0',
                'n',
                '-1',
            ],
        },
        'compiler': {
            'title': 'Recursion Sandbox',
            'question': 'Complete the recursive factorial base case return value.',
            'starter_code': 'def fact(n):\n    if n <= 0:\n        return _____\n    return n * fact(n - 1)\nprint(fact(4))',
            'options': [
                '1',
                '0',
                'n',
                'None',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the essential component of a recursive function that prevents infinite recursion?',
                'options': [
                    'Base Case',
                    'While Loop',
                    'Global Keyword',
                    'Import Statement',
                ],
                'answer': 'Base Case',
            },
            {
                'question': 'What exception occurs in Python if a recursive function lacks a valid base case?',
                'options': [
                    'RecursionError (maximum recursion depth exceeded)',
                    'SyntaxError',
                    'KeyError',
                    'ZeroDivisionError',
                ],
                'answer': 'RecursionError (maximum recursion depth exceeded)',
            },
            {
                'question': 'What defines Tail Recursion compared to Non-Tail Recursion?',
                'options': [
                    'The recursive call is the very last operation executed in the function',
                    'It uses a while loop instead',
                    'It has no base case',
                    'It returns strings only',
                ],
                'answer': 'The recursive call is the very last operation executed in the function',
            },
            {
                'question': 'What is the calculated output of factorial(4) in recursive implementation?',
                'options': [
                    '24',
                    '10',
                    '16',
                    '120',
                ],
                'answer': '24',
            },
            {
                'question': 'When is it recommended to avoid using recursion in Python?',
                'options': [
                    'When recursion depth is large enough to risk stack overflow or when simple loops suffice',
                    'When processing integers',
                    'When defining functions',
                    'Recursion should never be avoided',
                ],
                'answer': 'When recursion depth is large enough to risk stack overflow or when simple loops suffice',
            },
        ],
        'theory': {
            'definition': 'Recursion is a process where a function calls itself to solve smaller subproblems until reaching a base case.',
            'why': 'Recursion cleanly solves hierarchical tasks like tree traversals, Fibonacci series, and divide-and-conquer algorithms.',
            'rules': [
                'Every recursive function must define at least one Base Case.',
                'The Recursive Case must pass modified arguments progressing toward the Base Case.',
                "Be mindful of Python's default recursion limit (sys.getrecursionlimit()).",
            ],
            'examples': [
                'def fact(n):\n    return 1 if n<=1 else n*fact(n-1)',
            ],
        },
    },
    14: {
        'concept': '*args and **kwargs allow Python functions to accept an arbitrary number of arguments. *args collects extra positional arguments into a tuple. **kwargs collects extra keyword arguments into a dictionary. When used together in a function header, *args must precede **kwargs.',
        'syntax': 'def function_name(*args, **kwargs):\n    # args is a tuple of positional arguments\n    # kwargs is a dictionary of keyword arguments\n    pass',
        'example': {
            'code': '# Combining *args and **kwargs\ndef student_info(*args, **kwargs):\n    print("Subjects (tuple):", args)\n    print("Details (dict):", kwargs)\n\ndef multiply(*args):\n    result = 1\n    for num in args:\n        result *= num\n    return result\n\nprint("Multiply(2, 3, 4):", multiply(2, 3, 4))\nstudent_info("Math", "Science", Name="Alice", Age=20, City="New York")',
            'output': "Multiply(2, 3, 4): 24\nSubjects (tuple): ('Math', 'Science')\nDetails (dict): {'Name': 'Alice', 'Age': 20, 'City': 'New York'}",
            'explanation': "1. *args collects positional values ('Math', 'Science') into a tuple.\n2. **kwargs collects keyword key=value pairs into a dictionary.",
        },
        'fill_blanks': {
            'question': '# Collect arbitrary positional arguments\ndef sum_all(_____args):\n    return sum(args)',
            'answers': ['*'],
            'options': [
                '*',
                '**',
                '&',
                '$',
            ],
        },
        'compiler': {
            'title': '*args and **kwargs Sandbox',
            'question': 'Complete parameter to accept keyword arguments as dictionary.',
            'starter_code': 'def show_info(_____kwargs):\n    for k, v in kwargs.items():\n        print(k, "=", v)\nshow_info(a=1, b=2)',
            'options': [
                '**',
                '*',
                '...',
                '&',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What data structure does *args collect positional arguments into inside a function?',
                'options': [
                    'Tuple',
                    'List',
                    'Dictionary',
                    'Set',
                ],
                'answer': 'Tuple',
            },
            {
                'question': 'What data structure does **kwargs collect keyword arguments into inside a function?',
                'options': [
                    'Dictionary',
                    'Tuple',
                    'List',
                    'String',
                ],
                'answer': 'Dictionary',
            },
            {
                'question': 'What is the correct parameter ordering when combining standard parameters, *args, and **kwargs?',
                'options': [
                    'def f(standard, *args, **kwargs):',
                    'def f(**kwargs, *args, standard):',
                    'def f(*args, **kwargs, standard):',
                    'Order does not matter',
                ],
                'answer': 'def f(standard, *args, **kwargs):',
            },
            {
                'question': 'How do you unpack a dictionary into keyword arguments when calling a function?',
                'options': [
                    'func(**my_dict)',
                    'func(*my_dict)',
                    'func(&my_dict)',
                    'func(my_dict.unpack())',
                ],
                'answer': 'func(**my_dict)',
            },
            {
                'question': 'Why are *args and **kwargs useful in function definitions?',
                'options': [
                    'They allow functions to accept a variable number of positional and keyword inputs flexibly',
                    'They increase execution speed by 10x',
                    'They disable type checking',
                    'They force mandatory return values',
                ],
                'answer': 'They allow functions to accept a variable number of positional and keyword inputs flexibly',
            },
        ],
        'theory': {
            'definition': '*args and **kwargs handle dynamic variable-length positional and keyword argument passing.',
            'why': 'They make helper functions, wrappers, and decorators flexible without hardcoding parameter counts.',
            'rules': [
                '*args precedes **kwargs in function declarations.',
                '*args creates a tuple; **kwargs creates a dictionary.',
                'Use tuple and dictionary iteration methods to process incoming values.',
            ],
            'examples': [
                'def log(*args, **kwargs):\n    print(args, kwargs)',
            ],
        },
    },
    15: {
        'concept': "In Python, functions are First-Class Objects. This means functions can be: 1. Assigned to variables (f = msg), 2. Passed as arguments to higher-order functions (fun1(msg, 'Alex')), 3. Returned from other functions (function factories), and 4. Stored in data structures like lists or dictionaries (d = {'add': add}). This foundational concept enables functional programming, callbacks, closures, and decorators.",
        'syntax': 'def greet(name):\n    return f"Hello, {name}!"\n\nsay_hi = greet  # Assigning function to variable\nresult = apply_function(greet, "Alice")',
        'example': {
            'code': '# First-Class Functions: Assignment, Passing & Storage\ndef add(x, y):\n    return x + y\n\ndef subtract(x, y):\n    return x - y\n\n# 1. Assign function to variable\nop = add\nprint("op(5, 3):", op(5, 3))\n\n# 2. Pass function as argument\ndef apply(func, a, b):\n    return func(a, b)\n\nprint("apply(subtract, 10, 4):", apply(subtract, 10, 4))\n\n# 3. Store in dictionary\nops = {"add": add, "sub": subtract}\nprint("Dict ops[\'add\']:", ops["add"](7, 2))',
            'output': "op(5, 3): 8\napply(subtract, 10, 4): 6\nDict ops['add']: 9",
            'explanation': "1. Function 'add' is assigned to variable 'op'.\n2. 'subtract' is passed as an argument into higher-order function 'apply'.\n3. Functions 'add' and 'subtract' are stored in a dictionary and called using keys.",
        },
        'fill_blanks': {
            'question': '# Assign function object to variable\ndef greet(name): return "Hi " + name\nf = _____\nprint(f("Emma"))',
            'answers': ['greet'],
            'options': [
                'greet',
                'greet()',
                'def',
                'str',
            ],
        },
        'compiler': {
            'title': 'First-Class Functions Sandbox',
            'question': 'Assign the function double to variable fn.',
            'starter_code': 'def double(x): return x * 2\nfn = _____\nprint(fn(6))',
            'options': [
                'double',
                'double()',
                '2',
                'func',
            ],
        },
        'skill_exa_test': [
            {
                'question': "What does it mean that functions are 'first-class objects' in Python?",
                'options': [
                    'Functions can be assigned to variables, passed as arguments, returned, and stored in data structures',
                    'Functions run with highest OS privilege',
                    'Functions can only be written in class definitions',
                    'Functions are executed before main()',
                ],
                'answer': 'Functions can be assigned to variables, passed as arguments, returned, and stored in data structures',
            },
            {
                'question': 'What is a Higher-Order Function?',
                'options': [
                    'A function that takes another function as an argument, returns a function, or both',
                    'A function with more than 10 parameters',
                    'A recursive function with deep stack depth',
                    'A function written in C',
                ],
                'answer': 'A function that takes another function as an argument, returns a function, or both',
            },
            {
                'question': "What is the result of assigning f = print and executing f('Hello')?",
                'options': [
                    "Prints 'Hello' to console",
                    'Raises TypeError',
                    "Returns string 'f'",
                    'Creates a duplicate print file',
                ],
                'answer': "Prints 'Hello' to console",
            },
            {
                'question': 'Can functions be stored as values inside Python dictionaries?',
                'options': [
                    'Yes, functions can be stored and invoked via dictionary keys',
                    'No, dictionaries store strings and numbers only',
                    'Only static functions',
                    'Only lambda functions',
                ],
                'answer': 'Yes, functions can be stored and invoked via dictionary keys',
            },
            {
                'question': 'Which capability allows creating function factories (functions returning functions)?',
                'options': [
                    'First-Class Function return capability',
                    'Garbage collection',
                    'Static typing',
                    'Global variables',
                ],
                'answer': 'First-Class Function return capability',
            },
        ],
        'theory': {
            'definition': 'First-Class Functions treat function objects as first-class citizens equal to standard data types.',
            'why': 'Enables modular software design, higher-order function abstractions, event handlers, and decorators.',
            'rules': [
                'Reference functions without parentheses to pass the function object itself.',
                'Add parentheses (args) to invoke the function object.',
                'Higher-order functions receive or return function references.',
            ],
            'examples': ["fn = print\nfn('Hello')"],
        },
    },
    16: {
        'concept': 'Lambda functions are small anonymous functions defined using the lambda keyword. Syntax: lambda arguments: expression. A lambda function can take any number of arguments but contains only a single expression whose result is automatically returned without using the return keyword. Use cases include inline condition checking, tuple returns, list comprehensions, and passing transformation logic to map(), filter(), and reduce().',
        'syntax': 'square = lambda x: x ** 2\ncheck = lambda x: "Positive" if x > 0 else "Negative"\ncalc = lambda x, y: (x + y, x * y)',
        'example': {
            'code': '# Lambda Syntax, Conditional Evaluation & Tuple Return\nsquare = lambda x: x ** 2\ncheck = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"\ncalc = lambda x, y: (x + y, x * y)\n\nprint("Square(5):", square(5))\nprint("Check(-3):", check(-3))\nprint("Calc(3, 4):", calc(3, 4))',
            'output': 'Square(5): 25\nCheck(-3): Negative\nCalc(3, 4): (7, 12)',
            'explanation': '1. lambda x: x**2 returns the squared value without needing explicit return keyword.\n2. check uses ternary if-else within a single lambda expression.\n3. calc returns multiple values packed inside a tuple (x+y, x*y).',
        },
        'fill_blanks': {
            'question': '# Define lambda function to double value\ndouble = _____ x: x * 2\nprint(double(5))',
            'answers': ['lambda'],
            'options': [
                'lambda',
                'def',
                'inline',
                'fn',
            ],
        },
        'compiler': {
            'title': 'Lambda Expression Sandbox',
            'question': 'Complete the lambda keyword definition.',
            'starter_code': 'square = _____ x: x ** 2\nprint(square(7))',
            'options': [
                'lambda',
                'def',
                'fn',
                'fun',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What keyword is used to declare an anonymous inline function in Python?',
                'options': [
                    'lambda',
                    'def',
                    'inline',
                    'anonymous',
                ],
                'answer': 'lambda',
            },
            {
                'question': 'How many expressions can a Python lambda function contain?',
                'options': [
                    'Exactly one expression',
                    'Unlimited statements',
                    'Up to 5 statements',
                    'No expressions allowed',
                ],
                'answer': 'Exactly one expression',
            },
            {
                'question': "Is an explicit 'return' statement required inside a lambda function body?",
                'options': [
                    'No, the expression result is returned automatically',
                    'Yes, return is mandatory',
                    'Only for string returns',
                    'Only for numbers',
                ],
                'answer': 'No, the expression result is returned automatically',
            },
            {
                'question': 'How can a single-expression lambda function return multiple values?',
                'options': [
                    'By returning a tuple (e.g. lambda x, y: (x+y, x*y))',
                    'By using multiple return statements',
                    'By writing multiple lines',
                    'Lambda cannot return multiple values',
                ],
                'answer': 'By returning a tuple (e.g. lambda x, y: (x+y, x*y))',
            },
            {
                'question': 'Which of the following is a valid lambda expression that checks if a number is even?',
                'options': [
                    'lambda x: x % 2 == 0',
                    'def lambda(x): return x % 2 == 0',
                    'lambda(x) -> x % 2 == 0',
                    'inline x % 2 == 0',
                ],
                'answer': 'lambda x: x % 2 == 0',
            },
        ],
        'theory': {
            'definition': 'Lambda functions are short inline anonymous functions with a single automatically-returned expression.',
            'why': 'They avoid verbose def boilerplate for one-off callbacks in map(), filter(), and sorting keys.',
            'rules': [
                'Syntax: lambda arg1, arg2: expression.',
                "No explicit 'return' statement allowed.",
                'Restricted to a single evaluation expression.',
            ],
            'examples': ['double = lambda x: x * 2'],
        },
    },
    17: {
        'concept': "Functional sequence processing utilities and scope encapsulation:\n1. map(function, iterable) applies a function to every item in an iterable and returns a lazy iterator (map object).\n2. filter(function, iterable) extracts items for which the testing function returns True (passing None filters out falsy values like 0, '', None).\n3. reduce(function, iterable) (from functools) applies a two-argument function cumulatively to reduce a sequence step-by-step into a single scalar result.\n4. Inner Functions (nested functions) encapsulate helper logic, follow LEGB scope rules, and use the nonlocal keyword to mutate outer function variables.",
        'syntax': 'from functools import reduce\n\nmapped = list(map(lambda x: x * 2, nums))\nfiltered = list(filter(lambda x: x % 2 == 0, nums))\nreduced = reduce(lambda x, y: x + y, nums)',
        'example': {
            'code': '# Map, Filter, Reduce & Inner Functions\nfrom functools import reduce\n\nnumbers = [1, 2, 3, 4, 5, 6]\n\n# 1. map(): Double elements\ndoubled = list(map(lambda x: x * 2, numbers))\n\n# 2. filter(): Keep even elements\nevens = list(filter(lambda x: x % 2 == 0, numbers))\n\n# 3. reduce(): Sum elements\ntotal = reduce(lambda x, y: x + y, numbers)\n\n# 4. Inner function with nonlocal\ndef outer():\n    count = 10\n    def inner():\n        nonlocal count\n        count += 5\n        return count\n    return inner()\n\nprint("Doubled (map):", doubled)\nprint("Evens (filter):", evens)\nprint("Total (reduce):", total)\nprint("Inner nonlocal:", outer())',
            'output': 'Doubled (map): [2, 4, 6, 8, 10, 12]\nEvens (filter): [2, 4, 6]\nTotal (reduce): 15\nInner nonlocal: 15',
            'explanation': "1. map() applies transformation x*2 to all elements.\n2. filter() keeps elements where x%2==0 evaluates True.\n3. reduce() sums elements cumulatively step-by-step.\n4. Inner function uses 'nonlocal count' to modify the outer scope variable.",
        },
        'fill_blanks': {
            'question': '# Import reduce function from functools\nfrom _____ import reduce\nres = reduce(lambda x, y: x + y, [1, 2, 3])',
            'answers': ['functools'],
            'options': [
                'functools',
                'itertools',
                'operators',
                'math',
            ],
        },
        'compiler': {
            'title': 'Map & Filter Sandbox',
            'question': 'Filter even numbers using filter().',
            'starter_code': 'nums = [1, 2, 3, 4, 5, 6]\nevens = list(_____(lambda x: x % 2 == 0, nums))\nprint(evens)',
            'options': [
                'filter',
                'map',
                'reduce',
                'list',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What type of object does the map() function return in Python 3?',
                'options': [
                    'A lazy map iterator object',
                    'A list',
                    'A tuple',
                    'A dictionary',
                ],
                'answer': 'A lazy map iterator object',
            },
            {
                'question': 'What happens when filter(None, iterable) is called in Python?',
                'options': [
                    "It removes all falsy values (e.g. 0, '', None, False) from the iterable",
                    'It raises a TypeError',
                    'It converts all elements to None',
                    'It returns an empty list',
                ],
                'answer': "It removes all falsy values (e.g. 0, '', None, False) from the iterable",
            },
            {
                'question': 'Which module must be imported to use the reduce() function in Python 3?',
                'options': [
                    'functools',
                    'itertools',
                    'math',
                    'sys',
                ],
                'answer': 'functools',
            },
            {
                'question': 'What is the primary difference between reduce() and itertools.accumulate()?',
                'options': [
                    'reduce() returns a single final value; accumulate() returns an iterator of intermediate cumulative results',
                    'accumulate() works on strings only',
                    'reduce() is faster',
                    'There is no difference',
                ],
                'answer': 'reduce() returns a single final value; accumulate() returns an iterator of intermediate cumulative results',
            },
            {
                'question': 'Which keyword allows an inner function to modify a variable in its enclosing outer function scope?',
                'options': [
                    'nonlocal',
                    'global',
                    'outer',
                    'parent',
                ],
                'answer': 'nonlocal',
            },
        ],
        'theory': {
            'definition': 'map(), filter(), and reduce() process iterables functionally, while Inner Functions provide scope encapsulation.',
            'why': 'They replace explicit loop structures with concise functional transformations and maintain clean lexical scoping.',
            'rules': [
                'map() and filter() return lazy iterators; convert with list() or tuple().',
                "reduce() requires 'from functools import reduce'.",
                "Use 'nonlocal' for modifying enclosing outer variables inside inner functions.",
            ],
            'examples': [
                "list(map(str.upper, ['a', 'b']))",
                'from functools import reduce',
            ],
        },
    },
    23: {
        'concept': 'Decorators modify or extend the behavior of functions, methods, or classes without altering their source code. A decorator is a higher-order function that takes a function as input and returns a new wrapper function. Syntax shorthand @decorator is equivalent to func = decorator(func). Decorators use *args and **kwargs to support functions with arbitrary parameters. Types include: Function Decorators, Method Decorators (handling self), Class Decorators (modifying cls), Built-in Decorators (@staticmethod, @classmethod, @property with getter/setter), and Chaining Multiple Decorators (executed bottom-up).',
        'syntax': 'def decorator_name(func):\n    def wrapper(*args, **kwargs):\n        print("Before execution")\n        result = func(*args, **kwargs)\n        print("After execution")\n        return result\n    return wrapper\n\n@decorator_name\ndef add(a, b):\n    return a + b',
        'example': {
            'code': '# Decorators, @property & Built-in Decorators\ndef my_logger(func):\n    def wrapper(*args, **kwargs):\n        print(f"Executing {func.__name__}")\n        return func(*args, **kwargs)\n    return wrapper\n\n@my_logger\ndef add(a, b):\n    return a + b\n\nclass Circle:\n    def __init__(self, radius):\n        self._radius = radius\n    @property\n    def area(self):\n        return 3.14159 * (self._radius ** 2)\n\nprint("Sum:", add(5, 3))\nc = Circle(5)\nprint("Circle area:", c.area)',
            'output': 'Executing add\nSum: 8\nCircle area: 78.53975',
            'explanation': "1. @my_logger wraps 'add' to print log information before calling the original function.\n2. @property allows Circle.area to be accessed as an attribute without parentheses.",
        },
        'fill_blanks': {
            'question': '# Decorator syntax shorthand symbol\n_____\nmy_decorator\ndef greet():\n    print("Hello")',
            'answers': ['@'],
            'options': [
                '@',
                '#',
                '$',
                '&',
            ],
        },
        'compiler': {
            'title': 'Decorator Sandbox',
            'question': 'Use staticmethod decorator.',
            'starter_code': 'class Math:\n    _____\n    def add(x, y):\n        return x + y\nprint(Math.add(3, 4))',
            'options': [
                '@staticmethod',
                '@classmethod',
                '@property',
                '@decorator',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the syntax shorthand used to apply a decorator to a function in Python?',
                'options': [
                    '@decorator_name',
                    '#decorator_name',
                    '$decorator_name',
                    '%decorator_name',
                ],
                'answer': '@decorator_name',
            },
            {
                'question': 'What expression is @my_decorator def greet(): pass equivalent to?',
                'options': [
                    'greet = my_decorator(greet)',
                    'my_decorator = greet()',
                    'greet.decorator(my_decorator)',
                    'run(my_decorator)',
                ],
                'answer': 'greet = my_decorator(greet)',
            },
            {
                'question': 'Why do wrapper functions inside decorators typically accept *args and **kwargs?',
                'options': [
                    'To allow the decorator to work with any decorated function regardless of its parameter signature',
                    'To speed up execution',
                    'To force keyword arguments',
                    'To disable return values',
                ],
                'answer': 'To allow the decorator to work with any decorated function regardless of its parameter signature',
            },
            {
                'question': 'Which built-in decorator turns a method into a read-only property accessed like an attribute?',
                'options': [
                    '@property',
                    '@staticmethod',
                    '@classmethod',
                    '@getter',
                ],
                'answer': '@property',
            },
            {
                'question': 'How are multiple chained decorators applied to a single function (e.g. @decor1 \\n @decor2 def f():)?',
                'options': [
                    'From bottom to top: decor2 wraps f first, then decor1 wraps the result',
                    'From top to bottom: decor1 wraps f first',
                    'In alphabetical order',
                    'Simultaneously in parallel',
                ],
                'answer': 'From bottom to top: decor2 wraps f first, then decor1 wraps the result',
            },
        ],
        'theory': {
            'definition': 'Decorators are higher-order functions that extend or alter function, method, or class behavior dynamically using @ syntax.',
            'why': 'They enable reusable cross-cutting concerns like logging, authentication, caching (@lru_cache), and property getters/setters.',
            'rules': [
                '@decorator is shorthand for func = decorator(func).',
                'Use *args, **kwargs in wrapper functions for signature flexibility.',
                'Built-in decorators include @staticmethod, @classmethod, and @property.',
            ],
            'examples': [
                '@my_decorator\ndef my_func(): pass',
            ],
        },
    },
    24: {
        'concept': 'Strings are immutable sequences of characters enclosed in single (\'...\') or double ("...") quotes. Multi-line strings use triple quotes (\'\'\'...\'\'\' or """..."""). Positive indexing starts at 0 from left; negative indexing starts at -1 from right. Slicing syntax is s[start:stop:step]. String operations include len(), upper(), lower(), strip(), replace(), str.join(), + concatenation, * repetition, f-strings formatting, and \'in\' membership testing.',
        'syntax': 's = "GeeksForGeeks"\nsub = s[1:4]\nrev = s[::-1]\nfmt = f"Name: {name}, Age: {age}"\nis_found = "Geeks" in s',
        'example': {
            'code': '# Strings: Slicing, Methods, Formatting & Membership\ns = "ABCDEF"\nprint("Slicing [1:4]:", s[1:4])\nprint("Reversed s[::-1]:", s[::-1])\n\ns_text = "  Python is fun  "\nclean_text = s_text.strip().replace("fun", "awesome")\nprint("Cleaned & Replaced:", clean_text)\n\nname, age = "Jake", 22\nprint(f"f-string: Name: {name}, Age: {age}")\nprint("\'Python\' in clean_text:", "Python" in clean_text)',
            'output': "Slicing [1:4]: BCD\nReversed s[::-1]: FEDCBA\nCleaned & Replaced: Python is awesome\nf-string: Name: Jake, Age: 22\n'Python' in clean_text: True",
            'explanation': '1. s[1:4] extracts characters from index 1 up to index 3 (BCD).\n2. s[::-1] reverses the string using step -1.\n3. strip() removes leading/trailing whitespace and replace() substitutes substrings.\n4. f-strings inject variables directly inside curly braces {}.',
        },
        'fill_blanks': {
            'question': '# Reverse a string using slicing\ns = "Python"\nrev = s[::_____]\nprint(rev)',
            'answers': ['-1'],
            'options': [
                '-1',
                '0',
                '1',
                '2',
            ],
        },
        'compiler': {
            'title': 'String Slicing Sandbox',
            'question': "Reverse the string s = 'Geeks'.",
            'starter_code': 's = "Geeks"\nprint(s[::_____])',
            'options': [
                '-1',
                '1',
                '0',
                'None',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the key characteristic of Python strings regarding modification?',
                'options': [
                    'Strings are immutable (cannot be changed after creation)',
                    'Strings are mutable',
                    'Strings automatically convert to numbers',
                    'Strings require pointers',
                ],
                'answer': 'Strings are immutable (cannot be changed after creation)',
            },
            {
                'question': 'Which negative index accesses the last character of a string in Python?',
                'options': [
                    '-1',
                    '0',
                    '-len(s)',
                    '-2',
                ],
                'answer': '-1',
            },
            {
                'question': 'What does the slicing expression s[::-1] accomplish?',
                'options': [
                    'Returns a new string in reverse order',
                    'Deletes the first character',
                    'Raises an IndexError',
                    'Converts string to uppercase',
                ],
                'answer': 'Returns a new string in reverse order',
            },
            {
                'question': 'Which string method removes leading and trailing whitespace?',
                'options': [
                    'strip()',
                    'replace()',
                    'clean()',
                    'trim()',
                ],
                'answer': 'strip()',
            },
            {
                'question': 'How do f-strings format variables inside string literals?',
                'options': [
                    "By placing variables inside curly braces {} preceded by 'f'",
                    'By using %s placeholders',
                    'By calling .format()',
                    'By using + concatenation only',
                ],
                'answer': "By placing variables inside curly braces {} preceded by 'f'",
            },
        ],
        'theory': {
            'definition': 'Strings are immutable sequences of Unicode characters enclosed in quotes for text processing.',
            'why': 'Strings enable text manipulation, file parsing, formatting, and UI data presentation.',
            'rules': [
                'Single, double, or triple quotes declare strings.',
                "Modifying string elements (e.g. s[0] = 'A') raises TypeError due to immutability.",
                'Use f-strings for concise variable interpolation.',
            ],
            'examples': ["s = 'Hello World'", 'rev = s[::-1]'],
        },
    },
    25: {
        'concept': 'Lists are built-in, ordered, mutable, and dynamic data structures defined using square brackets [] or list(). Elements maintain insertion order and can store mixed data types. Python lists store memory references to underlying objects. List operations include adding (append(), insert(), extend()), updating by index (a[i] = val), removing (remove(), pop(), del, clear()), iteration, and multi-dimensional nested lists (matrices).',
        'syntax': 'a = [1, 2, 3]\na.append(4)\na.insert(1, 99)\na.extend([5, 6])\nval = a.pop()',
        'example': {
            'code': '# Lists: Adding, Updating, Removing & Nested Lists\nnums = [10, 20, 30]\nnums.append(40)\nnums.insert(1, 15)\nnums.extend([50, 60])\nprint("After additions:", nums)\n\nnums[0] = 99  # Update element\npopped = nums.pop()\nprint("Popped value:", popped)\n\nmatrix = [[1, 2], [3, 4]]\nprint("Matrix element [1][0]:", matrix[1][0])',
            'output': 'After additions: [10, 15, 20, 30, 40, 50, 60]\nPopped value: 60\nMatrix element [1][0]: 3',
            'explanation': '1. append() adds a single item to end; insert(1, 15) places 15 at index 1; extend() appends an iterable.\n2. pop() removes and returns the last element.\n3. matrix[1][0] accesses row 1, column 0.',
        },
        'fill_blanks': {
            'question': '# Add an element to end of list\na = [1, 2]\na._____(3)\nprint(a)',
            'answers': ['append'],
            'options': [
                'append',
                'insert',
                'extend',
                'add',
            ],
        },
        'compiler': {
            'title': 'List Operations Sandbox',
            'question': 'Append element 5 to list.',
            'starter_code': 'a = [1, 2, 3, 4]\na._____(5)\nprint(a)',
            'options': [
                'append',
                'add',
                'push',
                'insert',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'Which statement is TRUE regarding Python lists?',
                'options': [
                    'Lists are ordered, mutable collections that can store mixed data types',
                    'Lists are immutable',
                    'Lists store single data types only',
                    'Lists cannot be nested',
                ],
                'answer': 'Lists are ordered, mutable collections that can store mixed data types',
            },
            {
                'question': 'What is the primary difference between append() and extend() on a Python list?',
                'options': [
                    'append() adds its argument as a single element; extend() appends all items from an iterable',
                    'extend() adds to the front; append() adds to the end',
                    'append() works on strings only',
                    'There is no difference',
                ],
                'answer': 'append() adds its argument as a single element; extend() appends all items from an iterable',
            },
            {
                'question': 'Which list method removes and returns an item at a specified index (or the last item if omitted)?',
                'options': [
                    'pop()',
                    'remove()',
                    'clear()',
                    'delete()',
                ],
                'answer': 'pop()',
            },
            {
                'question': 'How do Python lists store elements internally in memory?',
                'options': [
                    'Lists store references (memory addresses) to objects on the heap',
                    'Lists store raw machine bytes inline',
                    'Lists compress data automatically',
                    'Lists convert everything to strings',
                ],
                'answer': 'Lists store references (memory addresses) to objects on the heap',
            },
            {
                'question': 'How do you access the element 3 from nested list m = [[1, 2], [3, 4]]?',
                'options': [
                    'm[1][0]',
                    'm[0][1]',
                    'm[1, 0]',
                    'm.get(1, 0)',
                ],
                'answer': 'm[1][0]',
            },
        ],
        'theory': {
            'definition': 'Lists are mutable, ordered, dynamic sequences capable of storing heterogeneous data types.',
            'why': 'Lists provide fundamental array-like storage, stack/queue operations, and matrix representations.',
            'rules': [
                'Lists use zero-based positive indexing and negative indexing.',
                'Modifying list items alters the list in-place.',
                'Methods like append() and insert() return None while mutating the list.',
            ],
            'examples': ['l = [10, 20, 30]', 'l.append(40)'],
        },
    },
    26: {
        'concept': 'Tuples are immutable, ordered collections of elements defined using parentheses (). Unlike lists, tuples cannot be changed, added to, or deleted from after creation. Tuples support mixed data types, single-element declaration with trailing comma (1,), indexing, slicing, tuple concatenation (+), repetition (*), full deletion (del tup), and Tuple Unpacking with Asterisk (a, *b, c = (1, 2, 3, 4, 5)).',
        'syntax': 'tup = (1, 2, 3)\na, b, c = tup  # Tuple unpacking\na, *b, c = (1, 2, 3, 4, 5)  # Asterisk unpacking\ntup3 = tup1 + tup2  # Concatenation',
        'example': {
            'code': '# Tuples: Creation, Concatenation, Slicing & Asterisk Unpacking\ntup1 = (0, 1, 2)\ntup2 = ("Geeks", "For", "Geeks")\ntup3 = tup1 + tup2\nprint("Concatenated Tuple:", tup3)\n\ntup = (1, 2, 3, 4, 5)\nfirst, *mid, last = tup\nprint(f"First: {first}, Mid (list): {mid}, Last: {last}")\nprint("Reversed Tuple Slicing:", tup[::-1])',
            'output': "Concatenated Tuple: (0, 1, 2, 'Geeks', 'For', 'Geeks')\nFirst: 1, Mid (list): [2, 3, 4], Last: 5\nReversed Tuple Slicing: (5, 4, 3, 2, 1)",
            'explanation': '1. tup1 + tup2 combines two tuples into a new concatenated tuple.\n2. *mid collects remaining unpacked intermediate elements into a list [2, 3, 4].\n3. tup[::-1] creates a new tuple containing elements in reverse order.',
        },
        'fill_blanks': {
            'question': '# Asterisk tuple unpacking\ntup = (1, 2, 3, 4, 5)\na, _____b, c = tup\nprint(b)',
            'answers': ['*'],
            'options': [
                '*',
                '**',
                '&',
                '...',
            ],
        },
        'compiler': {
            'title': 'Tuple Operations Sandbox',
            'question': 'Unpack tuple with asterisk.',
            'starter_code': 'tup = (10, 20, 30, 40)\nhead, _____tail = tup\nprint(head, tail)',
            'options': [
                '*',
                '**',
                '&',
                '...',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What happens if you attempt to reassign an element in a tuple (e.g. t[0] = 99)?',
                'options': [
                    'TypeError is raised because tuples are immutable',
                    'The tuple updates silently',
                    'A new tuple is created',
                    'ValueError is raised',
                ],
                'answer': 'TypeError is raised because tuples are immutable',
            },
            {
                'question': 'How must a single-element tuple be declared in Python?',
                'options': [
                    'With a trailing comma (e.g. t = (1,))',
                    't = (1)',
                    't = tuple(1)',
                    'Single element tuples are invalid',
                ],
                'answer': 'With a trailing comma (e.g. t = (1,))',
            },
            {
                'question': "In tuple unpacking a, *b, c = (1, 2, 3, 4, 5), what is the value and type of 'b'?",
                'options': [
                    'List [2, 3, 4]',
                    'Tuple (2, 3, 4)',
                    'Integer 2',
                    'Set {2, 3, 4}',
                ],
                'answer': 'List [2, 3, 4]',
            },
            {
                'question': 'Can two tuples be concatenated using the + operator?',
                'options': [
                    'Yes, producing a new combined tuple',
                    'No, tuples cannot be concatenated',
                    'Only if elements are numbers',
                    'Only using append()',
                ],
                'answer': 'Yes, producing a new combined tuple',
            },
            {
                'question': 'Why are tuples preferred over lists in some situations?',
                'options': [
                    'Tuples are immutable (read-only), faster, hashable as dictionary keys, and protect data integrity',
                    'Tuples hold more elements',
                    'Tuples allow duplicate keys',
                    'Tuples compile to C',
                ],
                'answer': 'Tuples are immutable (read-only), faster, hashable as dictionary keys, and protect data integrity',
            },
        ],
        'theory': {
            'definition': 'Tuples are immutable, ordered sequence collections defined using parentheses ().',
            'why': 'Tuples provide constant read-only collections, function return packing/unpacking, and hashable keys.',
            'rules': [
                'Tuples are immutable: items cannot be assigned, appended, or removed.',
                'Single element tuples require a trailing comma: (val,).',
                'Asterisk * in unpacking grabs remaining items as a list.',
            ],
            'examples': ['t = (1, 2, 3)', 'a, *b = t'],
        },
    },
    27: {
        'concept': 'Dictionaries store data in key-value pairs ({key: value} or dict()). Keys must be unique and immutable (strings, numbers, tuples), while values can be of any mutable or immutable data type. Access values using d[key] (raises KeyError if missing) or d.get(key, default) (returns default value safely). Adding/updating uses d[key] = val. Deleting methods include del d[key], d.pop(key), d.popitem() (removes last inserted pair), and d.clear(). Iteration methods include keys(), values(), and items(). Supports nested dictionaries.',
        'syntax': 'd = {"name": "Jake", "age": 22}\nd["city"] = "NYC"  # Add key\nval = d.get("age", 0)  # Safe get\nfor k, v in d.items():\n    print(k, v)',
        'example': {
            'code': '# Dictionary Operations: Access, Addition, Deletion & Iteration\nstudent = {"name": "Sam", "age": 20}\nstudent["age"] = 21        # Update value\nstudent["city"] = "Austin"  # Add new key-value pair\n\nprint("Name via get():", student.get("name"))\nprint("Missing key via get():", student.get("gpa", "N/A"))\n\npopped_city = student.pop("city")\nprint("Popped city:", popped_city)\n\nprint("\\n--- Iterating Items ---")\nfor k, v in student.items():\n    print(f"{k} => {v}")',
            'output': 'Name via get(): Sam\nMissing key via get(): N/A\nPopped city: Austin\n\n--- Iterating Items ---\nname => 21\nage => 21',
            'explanation': '1. d.get("gpa", "N/A") returns fallback \'N/A\' instead of raising a KeyError.\n2. pop("city") removes key \'city\' and returns its associated value.\n3. items() yields key-value tuples during loop iteration.',
        },
        'fill_blanks': {
            'question': '# Safe dictionary access method\nd = {"a": 1}\nval = d._____("b", 0)\nprint(val)',
            'answers': ['get'],
            'options': [
                'get',
                'pop',
                'find',
                'fetch',
            ],
        },
        'compiler': {
            'title': 'Dictionary Sandbox',
            'question': 'Iterate key-value pairs.',
            'starter_code': 'd = {"a": 1, "b": 2}\nfor k, v in d._____():\n    print(k, v)',
            'options': [
                'items',
                'keys',
                'values',
                'pairs',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What requirement must Python dictionary keys satisfy?',
                'options': [
                    'Keys must be unique and immutable (hashable)',
                    'Keys must be integers',
                    'Keys must be mutable lists',
                    'Keys can be duplicate',
                ],
                'answer': 'Keys must be unique and immutable (hashable)',
            },
            {
                'question': 'What is the key advantage of using dict.get(key) over square brackets dict[key]?',
                'options': [
                    'get() returns None or a default value instead of raising a KeyError for missing keys',
                    'get() is faster',
                    'get() converts keys to integers',
                    'get() mutates the dictionary',
                ],
                'answer': 'get() returns None or a default value instead of raising a KeyError for missing keys',
            },
            {
                'question': 'Which method removes and returns the last inserted key-value pair from a dictionary?',
                'options': [
                    'popitem()',
                    'pop()',
                    'clear()',
                    'remove()',
                ],
                'answer': 'popitem()',
            },
            {
                'question': 'Which method returns all key-value pairs as tuples for loop iteration?',
                'options': [
                    'items()',
                    'keys()',
                    'values()',
                    'tuples()',
                ],
                'answer': 'items()',
            },
            {
                'question': "How do you access 'Sam' in nested dictionary d = {'student': {'name': 'Sam', 'age': 20}}?",
                'options': [
                    "d['student']['name']",
                    "d['student, name']",
                    "d.get('student.name')",
                    "d['Sam']",
                ],
                'answer': "d['student']['name']",
            },
        ],
        'theory': {
            'definition': 'Dictionaries are mutable key-value mapping stores built on hash tables for fast O(1) key lookups.',
            'why': 'Dictionaries store structured JSON-like data, lookup tables, databases records, and configuration options.',
            'rules': [
                'Keys must be unique and immutable data types (str, int, tuple).',
                'Values can be any data type including lists and nested dicts.',
                'Use get() to avoid KeyError when accessing uncertain keys.',
            ],
            'examples': [
                "d = {'k': 'v'}",
                'for k, v in d.items(): print(k, v)',
            ],
        },
    },
    28: {
        'concept': 'Sets ({1, 2, 3} or set()) are unordered collections of unique elements. Duplicate values are automatically removed. Sets do not support indexing or item assignment (s[0] raises TypeError). Built on hash tables for fast O(1) average lookup. frozenset() creates an immutable, hashable set suitable for dictionary keys. Set methods & operators include: add(), clear(), Union (union() or |), Intersection (intersection() or &), Difference (difference() or -), and Symmetric Difference (^).',
        'syntax': 's = {1, 2, 3}\ns.add(4)\nu = set1 | set2  # Union\ni = set1 & set2  # Intersection\ndiff = set1 - set2  # Difference',
        'example': {
            'code': '# Sets: Unique Elements, Union, Intersection & Frozenset\nraw_list = [1, 2, 2, 3, 4, 4, 5]\nunique_set = set(raw_list)\nprint("Unique Set:", unique_set)\n\na = {1, 2, 3}\nb = {2, 3, 4}\nprint("Union (|):", a | b)\nprint("Intersection (&):", a & b)\nprint("Difference (-):", a - b)\n\nfs = frozenset(["x", "y", "z"])\nprint("Frozen Set:", fs)',
            'output': "Unique Set: {1, 2, 3, 4, 5}\nUnion (|): {1, 2, 3, 4, 5}\nIntersection (&): {2, 3}\nDifference (-): {1}\nFrozen Set: frozenset({'x', 'y', 'z'})",
            'explanation': '1. set(raw_list) automatically deduplicates list elements.\n2. Union | combines elements; Intersection & keeps common items; Difference - subtracts b from a.\n3. frozenset is immutable and hashable.',
        },
        'fill_blanks': {
            'question': '# Set intersection operator\na = {1, 2}\nb = {2, 3}\ni = a _____ b\nprint(i)',
            'answers': ['&'],
            'options': [
                '&',
                '|',
                '-',
                '^',
            ],
        },
        'compiler': {
            'title': 'Set Operations Sandbox',
            'question': 'Perform set union.',
            'starter_code': 'a = {1, 2}\nb = {2, 3}\nu = a _____ b\nprint(u)',
            'options': [
                '|',
                '&',
                '-',
                '^',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the defining characteristic of a Python set?',
                'options': [
                    'Unordered collection of unique elements',
                    'Ordered sequence of duplicate elements',
                    'Key-value pair dictionary',
                    'Immutable list',
                ],
                'answer': 'Unordered collection of unique elements',
            },
            {
                'question': 'What happens if you try to access a set element by index (e.g. s[0])?',
                'options': [
                    'TypeError is raised because sets are unordered and unindexed',
                    'Returns the first element',
                    'Returns None',
                    'Returns a random element',
                ],
                'answer': 'TypeError is raised because sets are unordered and unindexed',
            },
            {
                'question': 'Which operator performs the mathematical union of two sets in Python?',
                'options': [
                    '|',
                    '&',
                    '-',
                    '^',
                ],
                'answer': '|',
            },
            {
                'question': 'Which set type is immutable and hashable, allowing it to be used as a dictionary key?',
                'options': [
                    'frozenset',
                    'set',
                    'dictset',
                    'static_set',
                ],
                'answer': 'frozenset',
            },
            {
                'question': 'What underlying data structure enables O(1) average lookup time in Python sets?',
                'options': [
                    'Hash table',
                    'Linked list',
                    'Binary search tree',
                    'Array stack',
                ],
                'answer': 'Hash table',
            },
        ],
        'theory': {
            'definition': 'Sets are unordered collections of unique elements implemented using hash tables for O(1) membership testing.',
            'why': 'Sets efficiently eliminate duplicate values and perform mathematical set operations (union, intersection).',
            'rules': [
                'Duplicates are automatically removed upon insertion.',
                'Sets do not support index positioning or slicing.',
                'Use frozenset for immutable hashable set instances.',
            ],
            'examples': ['s = set([1, 2, 2, 3])', 'u = s1 | s2'],
        },
    },
    29: {
        'concept': "Arrays store homogeneous (same data type) elements sequentially in contiguous memory locations. Created using the built-in array module (import array as arr). Requires a typecode during initialization (e.g. 'i' for signed 4-byte integer, 'f' for float, 'd' for double). Differs from Python lists which store mixed types. Operations include: append(), insert(), remove(), pop(), index(), count(), reverse(), extend(), and array slicing. NumPy arrays (import numpy as np) extend this to multi-dimensional matrix computing.",
        'syntax': "import array as arr\na = arr.array('i', [1, 2, 3])\na.append(4)\na.insert(1, 99)\nval = a[0]",
        'example': {
            'code': '# Python Array Module: Typecodes, Adding, Slicing & Operations\nimport array as arr\n\n# Signed Integer Array (\'i\')\na = arr.array(\'i\', [10, 20, 30, 40, 50])\na.append(60)\na.insert(1, 15)\nprint("Array elements:", list(a))\nprint("Slicing [2:5]:", list(a[2:5]))\n\nprint("Count of 20:", a.count(20))\na.reverse()\nprint("Reversed Array:", list(a))',
            'output': 'Array elements: [10, 15, 20, 30, 40, 50, 60]\nSlicing [2:5]: [20, 30, 40]\nCount of 20: 1\nReversed Array: [60, 50, 40, 30, 20, 15, 10]',
            'explanation': "1. arr.array('i', ...) initializes a homogeneous signed integer array.\n2. append() and insert() add items matching the typecode.\n3. reverse() flips element order in-place.",
        },
        'fill_blanks': {
            'question': "# Array typecode for signed integer\nimport array as arr\na = arr.array('_____', [1, 2, 3])\nprint(a[0])",
            'answers': ['i'],
            'options': [
                'i',
                'f',
                'd',
                'b',
            ],
        },
        'compiler': {
            'title': 'Array Module Sandbox',
            'question': 'Append item to integer array.',
            'starter_code': "import array as arr\na = arr.array('i', [1, 2, 3])\na._____(4)\nprint(list(a))",
            'options': [
                'append',
                'add',
                'insert',
                'push',
            ],
        },
        'skill_exa_test': [
            {
                'question': "What is the primary difference between Python lists and the array module's arrays?",
                'options': [
                    'Arrays require all elements to be of the exact same data type (homogeneous); lists store mixed types',
                    'Lists cannot be sliced',
                    'Arrays cannot store numbers',
                    'There is no difference',
                ],
                'answer': 'Arrays require all elements to be of the exact same data type (homogeneous); lists store mixed types',
            },
            {
                'question': "Which typecode specifies signed integers in Python's array module?",
                'options': [
                    "'i'",
                    "'f'",
                    "'d'",
                    "'s'",
                ],
                'answer': "'i'",
            },
            {
                'question': 'Which array method returns the number of occurrences of a specified value?',
                'options': [
                    'count()',
                    'len()',
                    'index()',
                    'find()',
                ],
                'answer': 'count()',
            },
            {
                'question': 'Which library is standard in Python for multi-dimensional array and matrix operations?',
                'options': [
                    'NumPy',
                    'Pandas',
                    'Scipy',
                    'Pygame',
                ],
                'answer': 'NumPy',
            },
            {
                'question': "How are elements stored in memory in Python's array module?",
                'options': [
                    'In contiguous memory locations of fixed byte size',
                    'In scattered heap blocks',
                    'In string formats',
                    'As linked list nodes',
                ],
                'answer': 'In contiguous memory locations of fixed byte size',
            },
        ],
        'theory': {
            'definition': 'Arrays store homogeneous elements sequentially in contiguous memory blocks using typecodes.',
            'why': 'Arrays provide memory-efficient storage and C-compatible raw buffers for numerical sequences.',
            'rules': [
                "Typecodes dictate element byte size and type ('i', 'f', 'd').",
                'All items inserted into an array must match its designated typecode.',
                'Use NumPy for high-performance multi-dimensional matrix operations.',
            ],
            'examples': [
                "import array as arr\na = arr.array('i', [1, 2, 3])",
            ],
        },
    },
    30: {
        'concept': 'List comprehension offers a concise, single-line syntax to create new lists by applying an expression to each item in an existing iterable (list, tuple, range). Syntax: [expression for item in iterable if condition]. It is faster and cleaner than standard for loop appends. Supports optional if condition filters, nested for loops (generating coordinate pairs or matrix flattening), and element transformations.',
        'syntax': 'res = [x ** 2 for x in range(10) if x % 2 == 0]\nflat = [val for row in matrix for val in row]',
        'example': {
            'code': '# List Comprehension: Transformation, Filtering & Matrix Flattening\nnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n\n# 1. Square even numbers\neven_squares = [x ** 2 for x in numbers if x % 2 == 0]\nprint("Even Squares:", even_squares)\n\n# 2. Nested loops: Matrix flattening\nmatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\nflattened = [val for row in matrix for val in row]\nprint("Flattened Matrix:", flattened)',
            'output': 'Even Squares: [4, 16, 36, 64, 100]\nFlattened Matrix: [1, 2, 3, 4, 5, 6, 7, 8, 9]',
            'explanation': '1. [x**2 for x in numbers if x%2==0] filters even numbers and squares them in a single line.\n2. [val for row in matrix for val in row] flattens 2D rows into a 1D list.',
        },
        'fill_blanks': {
            'question': '# List comprehension for squares\nnums = [1, 2, 3]\nsquares = [x ** 2 _____ x in nums]\nprint(squares)',
            'answers': ['for'],
            'options': [
                'for',
                'in',
                'while',
                'if',
            ],
        },
        'compiler': {
            'title': 'List Comprehension Sandbox',
            'question': 'Filter even numbers in list comprehension.',
            'starter_code': 'nums = [1, 2, 3, 4, 5, 6]\nevens = [x for x in nums _____ x % 2 == 0]\nprint(evens)',
            'options': [
                'if',
                'for',
                'in',
                'where',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the general syntax for a list comprehension with a condition?',
                'options': [
                    '[expression for item in iterable if condition]',
                    'for item in iterable if condition -> expression',
                    '[if condition for item in iterable: expression]',
                    'list(expression, item, condition)',
                ],
                'answer': '[expression for item in iterable if condition]',
            },
            {
                'question': 'Why is list comprehension preferred over traditional for loops for simple operations?',
                'options': [
                    'It is more concise, readable, and executes faster in Python bytecode',
                    'It uses less RAM than variables',
                    'It compiles to assembly',
                    'It works only for integers',
                ],
                'answer': 'It is more concise, readable, and executes faster in Python bytecode',
            },
            {
                'question': 'What is the result of [i for i in range(5)]?',
                'options': [
                    '[0, 1, 2, 3, 4]',
                    '[1, 2, 3, 4, 5]',
                    '[0, 5]',
                    '[1, 4]',
                ],
                'answer': '[0, 1, 2, 3, 4]',
            },
            {
                'question': 'How do you flatten matrix = [[1, 2], [3, 4]] into [1, 2, 3, 4] using list comprehension?',
                'options': [
                    '[val for row in matrix for val in row]',
                    '[matrix.flatten()]',
                    '[val for val in matrix]',
                    '[for row in matrix]',
                ],
                'answer': '[val for row in matrix for val in row]',
            },
            {
                'question': 'Can list comprehensions combine multiple nested for loops?',
                'options': [
                    'Yes, multiple for clauses can be nested inside a single comprehension',
                    'No, only one loop is allowed',
                    'Only in Python 2',
                    'Only with lambda',
                ],
                'answer': 'Yes, multiple for clauses can be nested inside a single comprehension',
            },
        ],
        'theory': {
            'definition': 'List comprehension provides a compact syntax to construct new lists from existing iterables based on expressions and conditions.',
            'why': 'Reduces boilerplate loop code and improves execution speed by optimizing bytecode creation.',
            'rules': [
                'Syntax: [expr for item in iterable if condition].',
                'Expression comes first, followed by for clause and optional if clause.',
                'Nested for clauses execute in outer-to-inner order.',
            ],
            'examples': ['[x**2 for x in nums]', '[x for x in nums if x > 0]'],
        },
    },
    18: {
        'concept': 'Counter is a subclass of dict from the collections module designed to tally the frequency of elements in an iterable (lists, strings, tuples) or mapping. Missing keys return 0 instead of raising KeyError. Key methods: most_common(n) returns a list of top n (element, count) pairs; elements() returns an iterator repeating items by count; update() increases counts; subtract() decreases counts (allowing negative values); and manual increment ctr[key] += 1. Counter supports arithmetic operations: addition (+), subtraction (-), intersection (&), and union (|).',
        'syntax': 'from collections import Counter\ncnt = Counter([1, 1, 1, 2, 3, 3, 4])\ntop2 = cnt.most_common(2)\ncnt.update([2, 3])\ncnt.subtract([1])',
        'example': {
            'code': '# Counter: Frequency Tallying, Methods & Arithmetic\nfrom collections import Counter\n\n# 1. Tallying list elements & string characters\nlst_cnt = Counter([1, 1, 1, 2, 3, 3, 4])\nstr_cnt = Counter("hello")\n\nprint("List Counter:", lst_cnt)\nprint("String Counter:", str_cnt)\nprint("Top 2 most common:", lst_cnt.most_common(2))\n\n# 2. Counter arithmetic operations\nc1 = Counter([1, 2, 2, 3])\nc2 = Counter([2, 3, 3, 4])\nprint("c1 + c2:", c1 + c2)\nprint("c1 & c2 (intersection):", c1 & c2)',
            'output': "List Counter: Counter({1: 3, 3: 2, 2: 1, 4: 1})\nString Counter: Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})\nTop 2 most common: [(1, 3), (3, 2)]\nc1 + c2: Counter({2: 3, 3: 3, 1: 1, 4: 1})\nc1 & c2 (intersection): Counter({2: 1, 3: 1})",
            'explanation': '1. Counter tallies item frequencies automatically into a dictionary-like structure.\n2. most_common(2) returns the top 2 elements with highest frequencies as (element, count) tuples.\n3. Arithmetic operators (+, &) merge and intersect frequency counts across Counters.',
        },
        'fill_blanks': {
            'question': '# Import Counter from collections\nfrom _____ import Counter\ncnt = Counter("banana")',
            'answers': ['collections'],
            'options': [
                'collections',
                'functools',
                'itertools',
                'math',
            ],
        },
        'compiler': {
            'title': 'Counter Sandbox',
            'question': 'Get top most common element.',
            'starter_code': 'from collections import Counter\ncnt = Counter([1, 2, 2, 3, 3, 3])\nprint(cnt._____(1))',
            'options': [
                'most_common',
                'elements',
                'update',
                'keys',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'Which Python standard module contains the Counter class?',
                'options': [
                    'collections',
                    'functools',
                    'itertools',
                    'heapq',
                ],
                'answer': 'collections',
            },
            {
                'question': 'What happens when accessing a non-existent key in a Counter object?',
                'options': [
                    'Returns 0 without raising a KeyError',
                    'Raises a KeyError',
                    'Returns None',
                    'Raises an IndexError',
                ],
                'answer': 'Returns 0 without raising a KeyError',
            },
            {
                'question': 'What does counter.most_common(n) return?',
                'options': [
                    'A list of (element, count) tuples sorted from most common to least common',
                    'A dictionary of top keys',
                    'A single integer',
                    'A set of unique elements',
                ],
                'answer': 'A list of (element, count) tuples sorted from most common to least common',
            },
            {
                'question': 'Can element counts in a Counter become negative when using subtract()?',
                'options': [
                    'Yes, subtract() allows counts to go negative if subtraction exceeds original counts',
                    'No, counts stop at 0',
                    'No, subtract() raises ValueError',
                    'Only for floating-point numbers',
                ],
                'answer': 'Yes, subtract() allows counts to go negative if subtraction exceeds original counts',
            },
            {
                'question': 'Which operator performs frequency intersection between two Counter objects?',
                'options': [
                    '&',
                    '+',
                    '-',
                    '|',
                ],
                'answer': '&',
            },
        ],
        'theory': {
            'definition': 'Counter is a dictionary subclass designed specifically for counting frequency of hashable objects.',
            'why': 'It replaces manual loop counting, handles missing keys gracefully (returning 0), and provides frequency utilities.',
            'rules': [
                'Counter elements must be hashable objects.',
                'most_common(n) returns a list of (item, count) pairs.',
                'Supports set-like arithmetic operations (+, -, &, |).',
            ],
            'examples': [
                "from collections import Counter\nc = Counter('abracadabra')",
            ],
        },
    },
    19: {
        'concept': 'heapq is a built-in module providing min-heap priority queue algorithms on regular Python lists. The smallest element is always at index 0 (heap[0]). Operations: heapify(list) converts a list into a min-heap in O(N) time; heappush(heap, item) inserts an item maintaining heap order; heappop(heap) removes and returns the smallest element; heappushpop(heap, item) pushes first then pops; heapreplace(heap, item) pops first then pushes; nlargest(n, iterable) and nsmallest(n, iterable) return extreme elements; merge(*iterables) merges sorted inputs. Max-heaps are implemented by inverting element signs (-val).',
        'syntax': 'import heapq\nli = [25, 20, 15, 30, 40]\nheapq.heapify(li)\nsmallest = heapq.heappop(li)\nheapq.heappush(li, 5)',
        'example': {
            'code': '# heapq: Min-Heap, Max-Heap & Extreme Values\nimport heapq\n\n# Min-Heap\nh = [25, 20, 15, 30, 40]\nheapq.heapify(h)\nprint("Heapified min-heap:", h)\n\nheapq.heappush(h, 5)\nprint("After push 5:", h)\npopped_min = heapq.heappop(h)\nprint("Popped smallest:", popped_min)\n\n# Extreme elements & Max-Heap trick\nprint("3 smallest:", heapq.nsmallest(3, h))\nmax_heap = [-x for x in [10, 20, 15, 40]]\nheapq.heapify(max_heap)\nprint("Largest element:", -max_heap[0])',
            'output': 'Heapified min-heap: [15, 20, 25, 30, 40]\nAfter push 5: [5, 20, 15, 30, 40, 25]\nPopped smallest: 5\n3 smallest: [15, 20, 25]\nLargest element: 40',
            'explanation': '1. heapify() rearranges list into a min-heap with smallest element at index 0.\n2. heappush() inserts item maintaining heap order; heappop() extracts smallest.\n3. Max-heaps multiply values by -1.',
        },
        'fill_blanks': {
            'question': '# Convert list into min-heap\nimport heapq\nli = [5, 1, 3]\nheapq._____(li)\nprint(li[0])',
            'answers': ['heapify'],
            'options': [
                'heapify',
                'heappush',
                'heappop',
                'sort',
            ],
        },
        'compiler': {
            'title': 'heapq Sandbox',
            'question': 'Pop smallest element from min-heap.',
            'starter_code': 'import heapq\nh = [20, 10, 15]\nheapq.heapify(h)\nmin_val = heapq._____(h)\nprint(min_val)',
            'options': [
                'heappop',
                'heappush',
                'heapreplace',
                'pop',
            ],
        },
        'skill_exa_test': [
            {
                'question': "What type of heap does Python's heapq module implement by default?",
                'options': [
                    'Min-heap (smallest element at root heap[0])',
                    'Max-heap (largest element at root)',
                    'Binary search tree',
                    'Fibonacci heap',
                ],
                'answer': 'Min-heap (smallest element at root heap[0])',
            },
            {
                'question': 'What is the time complexity of converting a list of N elements into a heap using heapq.heapify()?',
                'options': [
                    'O(N)',
                    'O(N log N)',
                    'O(N^2)',
                    'O(1)',
                ],
                'answer': 'O(N)',
            },
            {
                'question': "How do you implement a Max-Heap using Python's heapq module?",
                'options': [
                    'By multiplying/inverting numbers by -1 when inserting and retrieving',
                    'By passing max=True to heapify',
                    'Using heapq.maxheap()',
                    'Max-heaps are unsupported',
                ],
                'answer': 'By multiplying/inverting numbers by -1 when inserting and retrieving',
            },
            {
                'question': 'What is the difference between heappushpop() and heapreplace()?',
                'options': [
                    'heappushpop() pushes first then pops; heapreplace() pops first then pushes new item',
                    'heapreplace() works on strings only',
                    'heappushpop() is slower',
                    'There is no difference',
                ],
                'answer': 'heappushpop() pushes first then pops; heapreplace() pops first then pushes new item',
            },
            {
                'question': 'Which heapq function finds the N smallest items from an iterable?',
                'options': [
                    'heapq.nsmallest(n, iterable)',
                    'heapq.min(n)',
                    'heapq.nlargest()',
                    'heapq.small(n)',
                ],
                'answer': 'heapq.nsmallest(n, iterable)',
            },
        ],
        'theory': {
            'definition': 'heapq provides binary min-heap algorithms on top of standard Python lists for priority queue operations.',
            'why': 'It enables O(log N) priority insertions/deletions and O(1) minimum element access (Dijkstra, Huffman coding).',
            'rules': [
                'heap[0] is always the minimum element in a min-heap.',
                'heapify(list) transforms lists in-place in linear O(N) time.',
                'Invert values (-x) to construct a max-heap.',
            ],
            'examples': [
                'import heapq\nheapq.heapify(li)\nmin_val = heapq.heappop(li)',
            ],
        },
    },
    20: {
        'concept': 'deque (Double-Ended Queue) from the collections module provides O(1) time complexity insertion and deletion from both left (front) and right (rear) ends. Operates as both a FIFO Queue and a LIFO Stack. Key operations: append(), appendleft(), extend(), extendleft(), pop(), popleft(), remove(), clear(), rotate(n) (rotates items right/left), reverse(), count(), and indexing dq[0], dq[-1].',
        'syntax': 'from collections import deque\ndq = deque([10, 20, 30])\ndq.appendleft(5)\ndq.append(40)\nval = dq.popleft()\ndq.rotate(1)',
        'example': {
            'code': '# Deque: Double-Ended Operations, Rotation & Reversal\nfrom collections import deque\n\ndq = deque([10, 20, 30])\ndq.append(40)         # Add to right\ndq.appendleft(5)      # Add to left\nprint("After appends:", dq)\n\nleft_val = dq.popleft() # Remove from left\nright_val = dq.pop()    # Remove from right\nprint(f"Popped Left: {left_val}, Popped Right: {right_val}")\n\ndq.rotate(1)            # Rotate 1 step right\nprint("Rotated Deque:", dq)',
            'output': 'After appends: deque([5, 10, 20, 30, 40])\nPopped Left: 5, Popped Right: 40\nRotated Deque: deque([30, 10, 20])',
            'explanation': '1. appendleft() inserts at head in O(1) time; append() inserts at tail.\n2. popleft() extracts head item in O(1) time.\n3. rotate(1) shifts items right by 1 position.',
        },
        'fill_blanks': {
            'question': '# Pop element from left end of deque\nfrom collections import deque\ndq = deque([1, 2, 3])\nval = dq._____()\nprint(val)',
            'answers': ['popleft'],
            'options': [
                'popleft',
                'pop',
                'remove',
                'shift',
            ],
        },
        'compiler': {
            'title': 'deque Sandbox',
            'question': 'Append element to left of deque.',
            'starter_code': 'from collections import deque\ndq = deque([10, 20])\ndq._____(5)\nprint(list(dq))',
            'options': [
                'appendleft',
                'append',
                'push',
                'unshift',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the time complexity of popping an element from the left end of a collections.deque?',
                'options': [
                    'O(1) constant time',
                    'O(N) linear time',
                    'O(N log N)',
                    'O(N^2)',
                ],
                'answer': 'O(1) constant time',
            },
            {
                'question': 'Which method removes and returns the first (leftmost) element from a deque?',
                'options': [
                    'popleft()',
                    'pop()',
                    'shift()',
                    'remove_first()',
                ],
                'answer': 'popleft()',
            },
            {
                'question': 'What does dq.rotate(1) do to a deque?',
                'options': [
                    'Rotates elements to the right by 1 step (last item moves to front)',
                    'Reverses the deque',
                    'Rotates left',
                    'Deletes the last item',
                ],
                'answer': 'Rotates elements to the right by 1 step (last item moves to front)',
            },
            {
                'question': 'Why is deque preferred over standard Python list for queue operations (FIFO)?',
                'options': [
                    'pop(0) on a list requires O(N) memory shifting; popleft() on deque is O(1)',
                    'deque allows floating-point keys',
                    'deque uses less memory',
                    'deque automatically sorts data',
                ],
                'answer': 'pop(0) on a list requires O(N) memory shifting; popleft() on deque is O(1)',
            },
            {
                'question': 'Which module provides the deque class in Python?',
                'options': [
                    'collections',
                    'queue',
                    'sys',
                    'asyncio',
                ],
                'answer': 'collections',
            },
        ],
        'theory': {
            'definition': 'deque is a double-ended queue providing O(1) performance for insertions and deletions at both ends.',
            'why': 'Ideal for implementing FIFO queues, LIFO stacks, sliding window algorithms, and task schedulers.',
            'rules': [
                'Use appendleft() and popleft() for head operations.',
                'Use append() and pop() for tail operations.',
                'rotate(n) shifts elements clockwise (right for positive n, left for negative n).',
            ],
            'examples': [
                'from collections import deque\ndq = deque([1, 2, 3])\ndq.appendleft(0)',
            ],
        },
    },
    21: {
        'concept': 'OrderedDict is a subclass of dict from collections that remembers key insertion order with specialized order-sensitive features. Key characteristics: Order-sensitive equality check (od1 == od2 checks both key-value pairs and insertion order); move_to_end(key, last=True/False) repositions keys to front or back without re-insertion; popitem(last=True/False) pops items from either end (LIFO when last=True, FIFO when last=False); updating existing keys retains original position; and reversed(list(od.items())) reverses order.',
        'syntax': "from collections import OrderedDict\nod = OrderedDict()\nod['a'] = 1\nod['b'] = 2\nod.move_to_end('a')  # Move 'a' to end\nitem = od.popitem(last=False)  # Pop first item",
        'example': {
            'code': '# OrderedDict: Order-Sensitive Equality, Move To End & Popitem\nfrom collections import OrderedDict\n\nod1 = OrderedDict([(\'a\', 1), (\'b\', 2), (\'c\', 3)])\nod2 = OrderedDict([(\'c\', 3), (\'b\', 2), (\'a\', 1)])\n\nprint("Order-sensitive equality (od1 == od2):", od1 == od2)\n\n# Moving key \'a\' to end & \'c\' to front\nod1.move_to_end(\'a\')\nod1.move_to_end(\'c\', last=False)\nprint("Repositioned keys:", list(od1.keys()))\n\n# FIFO pop from left\nfirst_item = od1.popitem(last=False)\nprint("Popped first item (FIFO):", first_item)',
            'output': "Order-sensitive equality (od1 == od2): False\nRepositioned keys: ['c', 'b', 'a']\nPopped first item (FIFO): ('c', 3)",
            'explanation': "1. od1 == od2 evaluates False because key insertion order differs.\n2. move_to_end('c', last=False) moves key 'c' to the front.\n3. popitem(last=False) pops the first item (FIFO order).",
        },
        'fill_blanks': {
            'question': "# Move key to end of OrderedDict\nfrom collections import OrderedDict\nod = OrderedDict([('a', 1), ('b', 2)])\nod._____\\('a')",
            'answers': ['move_to_end'],
            'options': [
                'move_to_end',
                'popitem',
                'shift',
                'reorder',
            ],
        },
        'compiler': {
            'title': 'OrderedDict Sandbox',
            'question': 'Pop first inserted item from OrderedDict.',
            'starter_code': "from collections import OrderedDict\nod = OrderedDict([('a', 1), ('b', 2)])\nitem = od.popitem(last=_____)\nprint(item)",
            'options': [
                'False',
                'True',
                'None',
                '0',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the primary difference in equality evaluation between standard dict and OrderedDict?',
                'options': [
                    'OrderedDict checks both key-value pairs AND insertion order for equality; standard dict checks content only',
                    'OrderedDict ignores values',
                    'Standard dict checks keys only',
                    'There is no difference',
                ],
                'answer': 'OrderedDict checks both key-value pairs AND insertion order for equality; standard dict checks content only',
            },
            {
                'question': 'Which method in OrderedDict moves an existing key to the front or back without deleting it?',
                'options': [
                    'move_to_end(key, last=True/False)',
                    'reorder(key)',
                    'shift(key)',
                    'push_end(key)',
                ],
                'answer': 'move_to_end(key, last=True/False)',
            },
            {
                'question': 'How does popitem(last=False) behave in an OrderedDict?',
                'options': [
                    'Removes and returns the first (oldest) inserted item (FIFO)',
                    'Removes the last item (LIFO)',
                    'Deletes all items',
                    'Raises KeyError',
                ],
                'answer': 'Removes and returns the first (oldest) inserted item (FIFO)',
            },
            {
                'question': 'Does modifying the value of an existing key in an OrderedDict change its original order position?',
                'options': [
                    'No, modifying an existing key value retains its original position',
                    'Yes, it moves the key to the end',
                    'Yes, it moves the key to the front',
                    'It raises ValueError',
                ],
                'answer': 'No, modifying an existing key value retains its original position',
            },
            {
                'question': 'Which module provides the OrderedDict class?',
                'options': [
                    'collections',
                    'dictutils',
                    'sys',
                    'ordering',
                ],
                'answer': 'collections',
            },
        ],
        'theory': {
            'definition': 'OrderedDict is a dictionary subclass that maintains key insertion order and provides order manipulation methods.',
            'why': 'Useful for LRU caches, order-sensitive JSON serialization, log processing, and FIFO dictionary pop operations.',
            'rules': [
                'move_to_end(key, last=False) moves key to the beginning.',
                'popitem(last=False) pops the first inserted item.',
                'Equality == requires identical key-value pairs AND matching key order.',
            ],
            'examples': [
                "from collections import OrderedDict\nod = OrderedDict([('a', 1), ('b', 2)])",
            ],
        },
    },
    22: {
        'concept': 'defaultdict is a subclass of dict from the collections module that automatically supplies a default value for missing keys using a default_factory callable (int, list, set, str, lambda), preventing KeyError. When accessing a non-existent key, default_factory() is called internally via __missing__(key) to initialize and store the default value. Common use cases include word frequency counting (defaultdict(int)), grouping items (defaultdict(list)), and text processing.',
        'syntax': "from collections import defaultdict\nd_list = defaultdict(list)\nd_int = defaultdict(int)\nd_list['fruits'].append('apple')\nd_int['counts'] += 1",
        'example': {
            'code': '# defaultdict: Frequency Counting & Word Grouping\nfrom collections import defaultdict\n\n# 1. defaultdict(int) for frequency counting\nword_count = defaultdict(int)\nwords = ["apple", "banana", "apple", "cherry", "banana", "apple"]\nfor w in words:\n    word_count[w] += 1\nprint("Word frequencies:", dict(word_count))\n\n# 2. defaultdict(list) for grouping words by first letter\ngrouped = defaultdict(list)\nfor w in words:\n    grouped[w[0]].append(w)\nprint("Grouped by first letter:", dict(grouped))',
            'output': "Word frequencies: {'apple': 3, 'banana': 2, 'cherry': 1}\nGrouped by first letter: {'a': ['apple', 'apple', 'apple'], 'b': ['banana', 'banana'], 'c': ['cherry']}",
            'explanation': '1. defaultdict(int) initializes missing word keys with 0 so word_count[w] += 1 works without KeyError.\n2. defaultdict(list) initializes missing letter keys with empty lists [].',
        },
        'fill_blanks': {
            'question': "# Create defaultdict with list factory\nfrom collections import defaultdict\nd = _____(list)\nd['a'].append(1)",
            'answers': ['defaultdict'],
            'options': [
                'defaultdict',
                'dict',
                'Counter',
                'OrderedDict',
            ],
        },
        'compiler': {
            'title': 'defaultdict Sandbox',
            'question': 'Initialize defaultdict with int.',
            'starter_code': "from collections import defaultdict\nd = _____(int)\nd['a'] += 5\nprint(d['a'])",
            'options': [
                'defaultdict',
                'dict',
                'Counter',
                'int',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What happens when accessing a missing key in a defaultdict?',
                'options': [
                    'default_factory is invoked to automatically create and return a default value without KeyError',
                    'KeyError is raised',
                    'Returns None without creating key',
                    'Raises TypeError',
                ],
                'answer': 'default_factory is invoked to automatically create and return a default value without KeyError',
            },
            {
                'question': 'What is the default value provided when creating defaultdict(int) for a missing key?',
                'options': [
                    '0',
                    'None',
                    '1',
                    'Empty list []',
                ],
                'answer': '0',
            },
            {
                'question': 'What is the default value provided when creating defaultdict(list) for a missing key?',
                'options': [
                    'Empty list []',
                    '0',
                    'None',
                    'Empty string ""',
                ],
                'answer': 'Empty list []',
            },
            {
                'question': 'Which internal special method is called by defaultdict when a key is not found?',
                'options': [
                    '__missing__(key)',
                    '__default__(key)',
                    '__get__(key)',
                    '__init__(key)',
                ],
                'answer': '__missing__(key)',
            },
            {
                'question': 'Which module provides the defaultdict class?',
                'options': [
                    'collections',
                    'dictutils',
                    'sys',
                    'itertools',
                ],
                'answer': 'collections',
            },
        ],
        'theory': {
            'definition': 'defaultdict is a dictionary subclass that automatically initializes missing keys with values generated by default_factory.',
            'why': "Eliminates repetitive 'if key not in dict' checks when counting, grouping, or building adjacency lists.",
            'rules': [
                'default_factory must be a callable (e.g. int, list, set, str, lambda).',
                'If default_factory is None, accessing missing keys raises KeyError.',
                '__missing__(key) supplies the default value internally.',
            ],
            'examples': [
                "from collections import defaultdict\nd = defaultdict(list)\nd['k'].append(1)",
            ],
        },
    },
    31: {
        'concept': 'Object-Oriented Programming (OOP) empowers developers to build modular, maintainable, and scalable applications by organizing code into classes and objects representing real-world entities. An object has state (attributes) and behavior (methods). The four pillars of OOP—Inheritance, Polymorphism, Encapsulation, and Data Abstraction—form the foundation for structured software architecture.',
        'syntax': 'class Entity:\n    def __init__(self, name):\n        self.name = name\n    def action(self):\n        pass',
        'example': {
            'code': '# Demonstrating basic OOP concepts with real-world entities\nclass Entity:\n    def __init__(self, name, entity_type):\n        self.name = name          # Instance attribute (State)\n        self.entity_type = entity_type # Instance attribute (State)\n\n    def describe(self):\n        # Method representing behavior\n        return f"{self.name} is a {self.entity_type}."\n\n# Object Instantiation (Identity)\nitem1 = Entity("Laptop", "Electronics")\nitem2 = Entity("Coffee", "Beverage")\n\nprint(item1.describe())\nprint(item2.describe())',
            'output': 'Laptop is a Electronics.\nCoffee is a Beverage.',
            'explanation': '1. class Entity defines the blueprint for real-world entities.\n2. item1 and item2 are distinct objects possessing state (name, entity_type) and behavior (describe()).\n3. The four pillars (Inheritance, Polymorphism, Encapsulation, Abstraction) build on this foundation.',
        },
        'fill_blanks': {
            'question': '# Complete object instantiation in Python OOP\nclass Entity:\n    def __init__(self, name):\n        ____.name = name',
            'answers': ['self'],
            'options': [
                'self',
                'this',
                'cls',
                'object',
            ],
        },
        'compiler': {
            'title': 'OOP Concepts Sandbox',
            'question': 'Complete attribute access for object instance.',
            'starter_code': 'class Entity:\n    def __init__(self, name):\n        self.name = name\n\ne = Entity("System")\nprint(e.____)',
            'options': [
                'name',
                'title',
                'type',
                'id',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What are the four pillars of Object-Oriented Programming?',
                'options': [
                    'Inheritance, Polymorphism, Encapsulation, and Abstraction',
                    'Classes, Objects, Functions, and Variables',
                    'Compilation, Interpretation, Execution, and Linking',
                    'Lists, Tuples, Dictionaries, and Sets',
                ],
                'answer': 'Inheritance, Polymorphism, Encapsulation, and Abstraction',
            },
            {
                'question': 'In OOP, what represents the state of an object?',
                'options': [
                    'Attributes (variables)',
                    'Methods (functions)',
                    'Class name',
                    'File path',
                ],
                'answer': 'Attributes (variables)',
            },
            {
                'question': 'In OOP, what represents the behavior of an object?',
                'options': [
                    'Methods (functions)',
                    'Attributes (variables)',
                    'Constructor arguments',
                    'Docstrings',
                ],
                'answer': 'Methods (functions)',
            },
            {
                'question': 'What is a class in Object-Oriented Programming?',
                'options': [
                    'A blueprint or user-defined template for creating objects',
                    'A single instance of data',
                    'A built-in Python module',
                    'A database table row',
                ],
                'answer': 'A blueprint or user-defined template for creating objects',
            },
            {
                'question': 'Which aspect of OOP gives a unique identity to each object?',
                'options': [
                    'Object instantiation creating a distinct instance reference',
                    'Global variable declarations',
                    'The print function',
                    'Module import statements',
                ],
                'answer': 'Object instantiation creating a distinct instance reference',
            },
        ],
        'theory': {
            'definition': 'Object-Oriented Programming organizes code into classes and objects to model real-world concepts with attributes and methods.',
            'why': 'Improves code modularity, reusability, readability, and long-term maintainability of complex applications.',
            'rules': [
                'Organizes code into reusable blueprints (classes) and instances (objects).',
                'Encapsulation groups data and methods together.',
                'Inheritance promotes hierarchical reuse.',
                'Polymorphism enables flexible implementation.',
            ],
            'examples': [
                'item1 = Entity("Laptop", "Electronics")',
                'item1.describe()',
            ],
        },
    },
    32: {
        'concept': 'Python is an object-oriented language where everything (integers, strings, functions, classes) is an object. Classes are created using the class keyword. Attributes are variables belonging to a class or instance. Attributes are public by default in Python and are accessed using the dot (.) operator (e.g. obj.attribute). Class attributes are shared across all instances, whereas instance attributes are unique to each object.',
        'syntax': 'class Dog:\n    species = "Canine"  # Class attribute\n    def __init__(self, name, age):\n        self.name = name  # Instance attribute\n        self.age = age',
        'example': {
            'code': '# Creating class with class and instance attributes\nclass Dog:\n    species = "Canine"  # Class attribute\n\n    def __init__(self, name, age):\n        self.name = name  # Instance attribute\n        self.age = age    # Instance attribute\n\n# Instantiating Dog class\ndog1 = Dog("Buddy", 3)\nprint(dog1.name)\nprint(dog1.species)',
            'output': 'Buddy\nCanine',
            'explanation': '1. class Dog creates a class named Dog.\n2. species is a class attribute shared by all Dog instances.\n3. self.name and self.age are instance attributes unique to dog1.\n4. Attributes are accessed directly using the dot (.) operator.',
        },
        'fill_blanks': {
            'question': '# Access instance attribute\nclass Dog:\n    def __init__(self, name):\n        self.name = name\n\ndog1 = Dog("Buddy")\nprint(dog1.____)',
            'answers': ['name'],
            'options': [
                'name',
                'species',
                'sound',
                'age',
            ],
        },
        'compiler': {
            'title': 'Python OOP Sandbox',
            'question': 'Access the class attribute species.',
            'starter_code': 'class Dog:\n    species = "Canine"\n\ndog1 = Dog()\nprint(dog1.____)',
            'options': [
                'species',
                'name',
                'type',
                'breed',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'How are attributes accessed in Python classes and objects?',
                'options': [
                    'Using the dot (.) operator',
                    'Using arrow (->) operator',
                    'Using double colon (::)',
                    'Using square brackets []',
                ],
                'answer': 'Using the dot (.) operator',
            },
            {
                'question': 'By default, what is the visibility of attributes defined in Python classes?',
                'options': [
                    'Public',
                    'Private',
                    'Protected',
                    'Package-private',
                ],
                'answer': 'Public',
            },
            {
                'question': 'What is the difference between a class attribute and an instance attribute in Python?',
                'options': [
                    'Class attributes are shared by all instances, while instance attributes belong to a specific object',
                    'Instance attributes are shared by all objects, while class attributes belong to one object',
                    'Class attributes can only be integers, while instance attributes are strings',
                    'There is no difference in Python',
                ],
                'answer': 'Class attributes are shared by all instances, while instance attributes belong to a specific object',
            },
            {
                'question': 'Which keyword is used to define a class in Python?',
                'options': [
                    'class',
                    'def',
                    'struct',
                    'object',
                ],
                'answer': 'class',
            },
            {
                'question': 'What statement is true about Python OOP philosophy?',
                'options': [
                    'Everything in Python is an object, including numbers, strings, and functions',
                    'Python allows only functional programming',
                    'Classes cannot have methods in Python',
                    'Instance variables cannot be accessed with dot notation',
                ],
                'answer': 'Everything in Python is an object, including numbers, strings, and functions',
            },
        ],
        'theory': {
            'definition': 'Python OOP uses the class keyword to create user-defined blueprints that bundle state (attributes) and behavior (methods) into dynamic object types.',
            'why': 'Provides a clean, readable structure for organizing application data and logic.',
            'rules': [
                'Classes are defined using the class keyword.',
                'Attributes are accessed via dot notation (e.g., obj.attribute).',
                'Class attributes are defined outside methods and shared across instances.',
                'Instance attributes are assigned to self inside __init__().',
            ],
            'examples': [
                'dog1 = Dog("Buddy", 3)',
                'print(dog1.name, dog1.species)',
            ],
        },
    },
    33: {
        'concept': 'A class is a blueprint, template, or schema for creating objects. An object is a concrete instance of a class holding state, behavior, and identity. The __str__() method in Python provides a human-readable custom string representation of an object. When print(obj) or str(obj) is executed, Python automatically invokes the __str__() method of the class instead of returning default string representations like <__main__.ClassName object at 0x...>.',
        'syntax': 'class Dog:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\n    def __str__(self):\n        return f"{self.name} is {self.age} years old."',
        'example': {
            'code': '# Custom string representation using __str__() method\nclass Dog:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\n    def __str__(self):\n        return f"{self.name} is {self.age} years old."\n\ndog1 = Dog("Buddy", 3)\ndog2 = Dog("Charlie", 5)\n\nprint(dog1)\nprint(dog2)',
            'output': 'Buddy is 3 years old.\nCharlie is 5 years old.',
            'explanation': '1. dog1 and dog2 are two distinct objects created from class Dog.\n2. When print(dog1) is called, Python automatically invokes __str__() method.\n3. __str__() uses self to access the instance attributes name and age and returns a readable string.',
        },
        'fill_blanks': {
            'question': '# Define __str__ method for human-readable output\nclass Dog:\n    def __init__(self, name):\n        self.name = name\n    def ____(self):\n        return f"Dog named {self.name}"',
            'answers': ['__str__'],
            'options': [
                '__str__',
                '__repr__',
                '__init__',
                '__name__',
            ],
        },
        'compiler': {
            'title': 'Classes and Objects Sandbox',
            'question': 'Access instance attribute in __str__.',
            'starter_code': 'class Dog:\n    def __init__(self, name):\n        self.name = name\n    def __str__(self):\n        return f"Dog: {self.____}"\n\nd = Dog("Bobby")\nprint(d)',
            'options': [
                'name',
                'title',
                'sound',
                'species',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the relationship between a Class and an Object?',
                'options': [
                    'A Class is a blueprint, while an Object is an instance created from that blueprint',
                    'An Object is a blueprint, while a Class is an instance',
                    'Class and Object are identical in Python',
                    'A Class executes code, while an Object defines functions',
                ],
                'answer': 'A Class is a blueprint, while an Object is an instance created from that blueprint',
            },
            {
                'question': 'What is the default return of print(obj) if __str__() is not overridden?',
                'options': [
                    'A string containing class name and memory location (e.g. <__main__.ClassName object at 0x...>)',
                    'An empty string',
                    'A syntax error',
                    'None',
                ],
                'answer': 'A string containing class name and memory location (e.g. <__main__.ClassName object at 0x...>)',
            },
            {
                'question': 'Which method is automatically called when converting an object to a string with str(obj)?',
                'options': [
                    '__str__()',
                    '__init__()',
                    '__new__()',
                    '__call__()',
                ],
                'answer': '__str__()',
            },
            {
                'question': 'Can multiple independent objects be instantiated from a single class?',
                'options': [
                    'Yes, each object has its own unique instance data and state',
                    'No, only one object per class is allowed',
                    'Yes, but all objects share the same instance attributes',
                    'Only if using global variables',
                ],
                'answer': 'Yes, each object has its own unique instance data and state',
            },
            {
                'question': 'What are the three main components of an Object in OOP?',
                'options': [
                    'State (attributes), Behavior (methods), and Identity (unique reference)',
                    'Loops, Functions, and Variables',
                    'HTML, CSS, and JavaScript',
                    'Input, Processing, and Output',
                ],
                'answer': 'State (attributes), Behavior (methods), and Identity (unique reference)',
            },
        ],
        'theory': {
            'definition': 'Classes serve as template blueprints while objects represent specific instantiated implementations holding state and behavior.',
            'why': 'Enables code modularity and clean, formatted object inspection through dunder methods like __str__().',
            'rules': [
                'Objects are created by calling the class name as a function: obj = ClassName().',
                'Instance attributes store object-specific state.',
                '__str__() must return a string representing the object.',
            ],
            'examples': [
                'dog1 = Dog("Buddy", 3)',
                'print(dog1)  # invokes __str__()',
            ],
        },
    },
    34: {
        'concept': 'Constructors are special methods used to initialize objects upon creation. In Python, object creation and initialization are handled through __new__() and __init__(). __new__() allocates memory and returns a new object instance before __init__() runs. __init__() receives the new instance and initializes its attributes, returning None by default. Python supports Default Constructors (no parameters besides self) and Parameterized Constructors (accepting arguments to set custom instance values).',
        'syntax': 'class Car:\n    # Default Constructor\n    def __init__(self):\n        self.make = "Toyota"\n\nclass CustomCar:\n    # Parameterized Constructor\n    def __init__(self, make, model):\n        self.make = make\n        self.model = model',
        'example': {
            'code': '# Default vs Parameterized Constructors in Python\nclass DefaultCar:\n    def __init__(self):\n        self.make = "Toyota"\n        self.model = "Corolla"\n        self.year = 2020\n\nclass ParameterizedCar:\n    def __init__(self, make, model, year):\n        self.make = make\n        self.model = model\n        self.year = year\n\ncar1 = DefaultCar()\ncar2 = ParameterizedCar("Honda", "Civic", 2022)\n\nprint("Default Car:", car1.make, car1.model, car1.year)\nprint("Parameterized Car:", car2.make, car2.model, car2.year)',
            'output': 'Default Car: Toyota Corolla 2020\nParameterized Car: Honda Civic 2022',
            'explanation': '1. DefaultCar initializes default fixed attribute values.\n2. ParameterizedCar accepts custom arguments when instantiated.\n3. __new__() creates the object instance, then __init__() initializes attribute values.',
        },
        'fill_blanks': {
            'question': '# Complete parameterized constructor\nclass Car:\n    def ____(self, make, model):\n        self.make = make\n        self.model = model',
            'answers': ['__init__'],
            'options': [
                '__init__',
                '__new__',
                '__create__',
                '__construct__',
            ],
        },
        'compiler': {
            'title': 'Constructors Sandbox',
            'question': 'Assign constructor parameter to instance attribute.',
            'starter_code': 'class Car:\n    def __init__(self, make, model):\n        self.make = make\n        self.____ = model\n\ncar = Car("Honda", "Civic")\nprint(car.model)',
            'options': [
                'model',
                'make',
                'brand',
                'year',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the primary role of the __init__() method in Python?',
                'options': [
                    'To initialize attributes of a newly created object instance',
                    'To allocate memory for a new object',
                    'To destroy an object when execution ends',
                    'To compile Python code into bytecode',
                ],
                'answer': 'To initialize attributes of a newly created object instance',
            },
            {
                'question': 'Which method is executed BEFORE __init__() during object instantiation in Python?',
                'options': [
                    '__new__()',
                    '__str__()',
                    '__del__()',
                    '__call__()',
                ],
                'answer': '__new__()',
            },
            {
                'question': 'What value must the __init__() method return in Python?',
                'options': [
                    'None',
                    'self',
                    'True',
                    'The object instance',
                ],
                'answer': 'None',
            },
            {
                'question': 'What is a parameterized constructor?',
                'options': [
                    'A constructor method that accepts custom arguments during object creation',
                    'A constructor with no parameters',
                    'A function defined outside any class',
                    'A static class method',
                ],
                'answer': 'A constructor method that accepts custom arguments during object creation',
            },
            {
                'question': 'What happens if a class does not define an __init__() method explicitly?',
                'options': [
                    'Python automatically provides a default constructor',
                    'Object instantiation raises a TypeError',
                    'The program fails to compile',
                    'No object can be created',
                ],
                'answer': 'Python automatically provides a default constructor',
            },
        ],
        'theory': {
            'definition': 'Constructors are special dunder methods (__new__ and __init__) that construct and initialize new class instances.',
            'why': 'Ensures every newly created object starts with valid, initialized attribute states.',
            'rules': [
                '__new__(cls, ...) allocates memory and returns the object instance.',
                '__init__(self, ...) initializes object attributes and must return None.',
                'Default constructors accept no custom arguments; Parameterized constructors accept arguments.',
            ],
            'examples': [
                'car = Car("Honda", "Civic", 2022)',
            ],
        },
    },
    35: {
        'concept': 'In Python, when defining methods inside a class, the first parameter is always self. self is not a reserved keyword, but a standard naming convention representing the current instance of the class. Python adheres to "Explicit is better than implicit": requiring self explicitly ensures clear, unambiguous access to instance attributes and methods. When invoking obj.method(arg), Python automatically converts the call into Class.method(obj, arg).',
        'syntax': 'class Circle:\n    def __init__(self, r):\n        self.r = r  # Stores radius on current instance\n\n    def area(self):\n        return 3.14 * (self.r ** 2)',
        'example': {
            'code': '# Using self to access instance attributes in methods\nclass Circle:\n    def __init__(self, r):\n        self.r = r\n\n    def area(self):\n        # self.r ensures radius comes from the calling instance\n        return 3.14 * (self.r ** 2)\n\n# Instantiate Circle with radius 5\nins = Circle(5)\n\n# Python automatically passes ins as self when calling ins.area()\nprint("Area of the circle:", ins.area())',
            'output': 'Area of the circle: 78.5',
            'explanation': '1. self.r = r assigns 5 to instance attribute r on object ins.\n2. Inside area(), self.r retrieves that specific instance value.\n3. Calling ins.area() automatically passes ins as the first self argument.',
        },
        'fill_blanks': {
            'question': '# Complete first parameter in Python instance method\nclass Circle:\n    def __init__(____, r):\n        ____.r = r',
            'answers': ['self', 'self'],
            'options': [
                'self',
                'this',
                'cls',
                'obj',
            ],
        },
        'compiler': {
            'title': 'self Sandbox',
            'question': 'Complete method signature using self.',
            'starter_code': 'class Circle:\n    def __init__(self, r):\n        self.r = r\n    def get_radius(____):\n        return self.r\n\nc = Circle(10)\nprint(c.get_radius())',
            'options': [
                'self',
                'cls',
                'this',
                'r',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'Why does Python require the `self` parameter explicitly in instance methods?',
                'options': [
                    'To adhere to "Explicit is better than implicit" and provide unambiguous instance access',
                    'Because self is a mandatory C compiler keyword',
                    'To prevent variables from being saved in memory',
                    'Because Python does not support functions inside classes',
                ],
                'answer': 'To adhere to "Explicit is better than implicit" and provide unambiguous instance access',
            },
            {
                'question': 'Is `self` a mandatory keyword in Python syntax?',
                'options': [
                    'No, it is a strong naming convention; any parameter name can be used, though self is standard',
                    'Yes, using any word other than self results in a SyntaxError',
                    'Yes, self is a built-in Python reserved keyword',
                    'No, Python methods never take instance parameters',
                ],
                'answer': 'No, it is a strong naming convention; any parameter name can be used, though self is standard',
            },
            {
                'question': 'When calling `car1.display()`, what does Python do behind the scenes?',
                'options': [
                    'Automatically passes car1 as the first argument (self) to display()',
                    'Deletes car1 from memory',
                    'Converts display() into a static method',
                    'Prompts the user for terminal input',
                ],
                'answer': 'Automatically passes car1 as the first argument (self) to display()',
            },
            {
                'question': 'What does `self` represent inside a class method?',
                'options': [
                    'The specific instance of the class that called the method',
                    'The module where the class is defined',
                    'The parent class',
                    'The Python interpreter',
                ],
                'answer': 'The specific instance of the class that called the method',
            },
            {
                'question': 'How do methods access instance variables created in `__init__()`?',
                'options': [
                    'By prefixing the variable with self. (e.g. self.variable_name)',
                    'Using global variable statements',
                    'By importing sys module',
                    'Using local variables directly',
                ],
                'answer': 'By prefixing the variable with self. (e.g. self.variable_name)',
            },
        ],
        'theory': {
            'definition': 'self is the explicit reference to the current class instance passed automatically as the first parameter to instance methods.',
            'why': 'Maintains clarity and consistency by making instance attribute access explicit across class methods.',
            'rules': [
                'First parameter of every instance method must represent the instance.',
                'By convention named self.',
                'Python automatically binds the instance object when invoking instance methods.',
            ],
            'examples': [
                'ins = Circle(5)',
                'print(ins.area())',
            ],
        },
    },
    36: {
        'concept': 'Polymorphism ("same operation, different behavior") allows methods, functions, or operators to adapt based on the object or context they operate upon. Python supports multiple forms of polymorphism:\n1. Compile-Time Polymorphism (Simulated via default parameters, *args, **kwargs).\n2. Runtime Polymorphism (Method Overriding where child classes provide custom implementations of parent methods).\n3. Built-in Polymorphic Functions (len(), max() working on different iterables/types).\n4. Duck Typing ("If it walks like a duck, it\'s a duck").\n5. Operator Overloading (+ performing addition or concatenation).',
        'syntax': 'class Animal:\n    def sound(self): return "Generic"\n\nclass Dog(Animal):\n    def sound(self): return "Bark"\n\nclass Cat(Animal):\n    def sound(self): return "Meow"',
        'example': {
            'code': '# Runtime Polymorphism and Operator Overloading in Python\nclass Animal:\n    def sound(self):\n        return "Some generic sound"\n\nclass Dog(Animal):\n    def sound(self):\n        return "Bark"\n\nclass Cat(Animal):\n    def sound(self):\n        return "Meow"\n\n# 1. Method Overriding Polymorphism\nanimals = [Dog(), Cat(), Animal()]\nfor a in animals:\n    print(a.sound())\n\n# 2. Operator Polymorphism\nprint(5 + 10)           # Integer addition\nprint("Hello " + "World") # String concatenation',
            'output': 'Bark\nMeow\nSome generic sound\n15\nHello World',
            'explanation': '1. sound() method behaves differently depending on whether the object is Dog, Cat, or Animal.\n2. The + operator adapts behavior dynamically based on integer vs string operand types.',
        },
        'fill_blanks': {
            'question': '# Override sound method in Dog subclass\nclass Animal:\n    def sound(self): return "Generic"\nclass Dog(Animal):\n    def ____(self): return "Bark"',
            'answers': ['sound'],
            'options': [
                'sound',
                'bark',
                'make_sound',
                'speak',
            ],
        },
        'compiler': {
            'title': 'Polymorphism Sandbox',
            'question': 'Provide Cat implementation for sound method.',
            'starter_code': 'class Animal:\n    def sound(self): return "Generic"\nclass Cat(Animal):\n    def sound(self): return "____"\n\nc = Cat()\nprint(c.sound())',
            'options': [
                'Meow',
                'Bark',
                'Roar',
                'Squeak',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What does Polymorphism mean in Object-Oriented Programming?',
                'options': [
                    'Same method or operation name exhibiting different behaviors based on object context',
                    'Restricting class access to private variables only',
                    'Creating duplicate copies of objects in memory',
                    'Converting Python scripts into C executables',
                ],
                'answer': 'Same method or operation name exhibiting different behaviors based on object context',
            },
            {
                'question': 'How does Python achieve compile-time polymorphism behavior given its dynamic typing?',
                'options': [
                    'Using default arguments, *args, and **kwargs in method signatures',
                    'By using static C++ type annotations',
                    'Using macros',
                    'Python does not support method calls with multiple arguments',
                ],
                'answer': 'Using default arguments, *args, and **kwargs in method signatures',
            },
            {
                'question': 'What is Duck Typing in Python?',
                'options': [
                    'A concept where object suitability is determined by the presence of required methods rather than explicit class hierarchy',
                    'A method that only works for duck species',
                    'A built-in Python module for unit testing',
                    'A static typing enforcement tool',
                ],
                'answer': 'A concept where object suitability is determined by the presence of required methods rather than explicit class hierarchy',
            },
            {
                'question': 'Which of the following demonstrates built-in function polymorphism in Python?',
                'options': [
                    'len() working for strings, lists, tuples, and dictionaries',
                    'print() asking for user passwords',
                    'import math loading C libraries',
                    'type() throwing exceptions',
                ],
                'answer': 'len() working for strings, lists, tuples, and dictionaries',
            },
            {
                'question': 'What is Operator Overloading in Python?',
                'options': [
                    'Giving extended or custom behavior to operators (like + or *) based on operand types',
                    'Deleting built-in operators',
                    'Running loops without conditions',
                    'Creating new keyword syntax in Python',
                ],
                'answer': 'Giving extended or custom behavior to operators (like + or *) based on operand types',
            },
        ],
        'theory': {
            'definition': 'Polymorphism allows the same interface or method invocation to produce different results depending on the calling object or data type.',
            'why': 'Enables clean, modular, and reusable application design where functions can interact with multiple object types seamlessly.',
            'rules': [
                'Runtime polymorphism is achieved via method overriding in subclasses.',
                'Duck typing checks object capability (methods) rather than explicit type.',
                'Operator overloading customizes operator behavior via magic methods (e.g. __add__).',
            ],
            'examples': [
                'for a in animals: print(a.sound())',
                'len("Hello") vs len([1, 2, 3])',
            ],
        },
    },
    37: {
        'concept': 'Inheritance allows a child (derived) class to acquire properties, attributes, and methods from a parent (base) class. It promotes hierarchical classification, code reusability, and centralized maintenance. Python provides the super() function to call methods from a parent class following Python Method Resolution Order (MRO). Child classes can initialize inherited attributes using super().__init__() and can perform Method Overriding to customize behavior.',
        'syntax': 'class Parent:\n    def __init__(self, name):\n        self.name = name\n\nclass Child(Parent):\n    def __init__(self, name, breed):\n        super().__init__(name)  # Calls parent constructor\n        self.breed = breed',
        'example': {
            'code': '# Inheritance and super() function in Python\nclass Animal:\n    def __init__(self, name):\n        self.name = name\n\n    def info(self):\n        print("Animal name:", self.name)\n\nclass Dog(Animal):\n    def __init__(self, name, breed):\n        super().__init__(name) # Calls parent constructor\n        self.breed = breed\n\n    def details(self):\n        print(self.name, "is a", self.breed)\n\nd = Dog("Buddy", "Golden Retriever")\nd.info()     # Inherited parent method\nd.details()  # Child method',
            'output': 'Animal name: Buddy\nBuddy is a Golden Retriever',
            'explanation': '1. class Dog(Animal) defines Dog as a child subclass inheriting from Animal.\n2. super().__init__(name) delegates name initialization to Animal class constructor.\n3. d.info() accesses inherited parent logic while d.details() runs subclass-specific logic.',
        },
        'fill_blanks': {
            'question': '# Call parent constructor in child class\nclass Dog(Animal):\n    def __init__(self, name, breed):\n        ____().__init__(name)\n        self.breed = breed',
            'answers': ['super'],
            'options': [
                'super',
                'parent',
                'base',
                'Animal',
            ],
        },
        'compiler': {
            'title': 'Inheritance Sandbox',
            'question': 'Call parent constructor using super().',
            'starter_code': 'class Animal:\n    def __init__(self, name): self.name = name\n\nclass Dog(Animal):\n    def __init__(self, name):\n        ____().__init__(name)\n\nd = Dog("Buddy")\nprint(d.name)',
            'options': [
                'super',
                'parent',
                'base',
                'self',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the primary benefit of Inheritance in Python?',
                'options': [
                    'Promotes code reusability by sharing attributes and methods across class hierarchies',
                    'Reduces execution speed',
                    'Makes all variables private',
                    'Eliminates the need for class constructors',
                ],
                'answer': 'Promotes code reusability by sharing attributes and methods across class hierarchies',
            },
            {
                'question': 'What is the purpose of the `super()` function in Python inheritance?',
                'options': [
                    'To access and call methods from a superclass according to Method Resolution Order (MRO)',
                    'To convert a subclass into a function',
                    'To terminate loop execution',
                    'To declare global constants',
                ],
                'answer': 'To access and call methods from a superclass according to Method Resolution Order (MRO)',
            },
            {
                'question': 'How does a child class inherit from a parent class in Python syntax?',
                'options': [
                    'By passing the parent class name inside parentheses in class definition: class Child(Parent):',
                    'Using the inherits keyword: class Child inherits Parent',
                    'Using arrow notation: class Child -> Parent',
                    'By importing parent class inside methods',
                ],
                'answer': 'By passing the parent class name inside parentheses in class definition: class Child(Parent):',
            },
            {
                'question': 'What is Method Overriding in inheritance?',
                'options': [
                    'When a child class provides a custom implementation of a method that already exists in its parent class',
                    'Deleting parent class methods',
                    'Renaming variables inside functions',
                    'Calling two methods simultaneously',
                ],
                'answer': 'When a child class provides a custom implementation of a method that already exists in its parent class',
            },
            {
                'question': 'What is Method Resolution Order (MRO) in Python?',
                'options': [
                    'The order in which Python searches for attributes and methods across base classes',
                    'The speed at which functions are executed',
                    'The order of imports in a file',
                    'The database sorting algorithm',
                ],
                'answer': 'The order in which Python searches for attributes and methods across base classes',
            },
        ],
        'theory': {
            'definition': 'Inheritance allows a subclass to derive attributes and behavior from a base class, modeling real-world domain relationships.',
            'why': 'Prevents code duplication and enables centralized updates in base classes.',
            'rules': [
                'Syntax: class ChildClass(ParentClass):.',
                'Use super() to delegate method execution (e.g. __init__) to superclasses.',
                'Subclasses can extend parent capability or override existing methods.',
            ],
            'examples': [
                'class Dog(Animal):',
                'super().__init__(name)',
            ],
        },
    },
    38: {
        'concept': 'Abstraction hides complex internal implementation details while exposing only necessary functionality to the user. In Python, Data Abstraction is achieved using the abc module with Abstract Base Class (ABC) and @abstractmethod decorator. Components of Abstraction include:\n1. Abstract Method (@abstractmethod): Method declarations without body; forces subclasses to implement them.\n2. Concrete Method: Fully implemented methods inside abstract classes inherited directly.\n3. Abstract Properties (@property + @abstractmethod): Enforces property implementation in subclasses.\n4. Instantiation Limitation: Attempting to instantiate an abstract class directly raises TypeError.',
        'syntax': 'from abc import ABC, abstractmethod\n\nclass Animal(ABC):\n    @abstractmethod\n    def make_sound(self):\n        pass  # Abstract method\n\n    def move(self):\n        return "Moving"  # Concrete method',
        'example': {
            'code': '# Abstract Base Class, Abstract Method, and Concrete Method in Python\nfrom abc import ABC, abstractmethod\n\nclass Animal(ABC):\n    @abstractmethod\n    def make_sound(self):\n        pass  # Abstract method (placeholder without body)\n\n    def move(self):\n        return "Moving"  # Concrete method\n\nclass Dog(Animal):\n    def make_sound(self):\n        return "Bark"\n\ndog = Dog()\nprint("Sound:", dog.make_sound())\nprint("Action:", dog.move())',
            'output': 'Sound: Bark\nAction: Moving',
            'explanation': '1. Animal inherits from ABC and defines abstract method make_sound().\n2. Dog subclass provides concrete implementation for make_sound().\n3. Dog inherits concrete move() method directly.\n4. Attempting Animal() directly raises TypeError.',
        },
        'fill_blanks': {
            'question': '# Import ABC and abstractmethod decorator\nfrom abc import ABC, ____\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self): pass',
            'answers': ['abstractmethod'],
            'options': [
                'abstractmethod',
                'abstract',
                'method',
                'decorator',
            ],
        },
        'compiler': {
            'title': 'Abstraction Sandbox',
            'question': 'Implement abstract method in subclass.',
            'starter_code': 'from abc import ABC, abstractmethod\n\nclass Animal(ABC):\n    @abstractmethod\n    def make_sound(self): pass\n\nclass Dog(Animal):\n    def ____(self): return "Bark"\n\nd = Dog()\nprint(d.make_sound())',
            'options': [
                'make_sound',
                'sound',
                'bark',
                'speak',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the main goal of Data Abstraction in OOP?',
                'options': [
                    'To hide internal implementation details and expose only essential functionality',
                    'To make all variables public',
                    'To run code without compiling',
                    'To speed up list append operations',
                ],
                'answer': 'To hide internal implementation details and expose only essential functionality',
            },
            {
                'question': 'Which module is used to create Abstract Base Classes in Python?',
                'options': [
                    'abc',
                    'sys',
                    'os',
                    'typing',
                ],
                'answer': 'abc',
            },
            {
                'question': 'What happens if you try to instantiate an Abstract Class that has unimplemented abstract methods?',
                'options': [
                    'Python raises a TypeError',
                    'The object is created with default empty values',
                    'Python returns None silently',
                    'A Warning is printed but execution continues',
                ],
                'answer': 'Python raises a TypeError',
            },
            {
                'question': 'What is an Abstract Method in Python?',
                'options': [
                    'A method decorated with @abstractmethod that has no implementation in the base class and must be overridden by subclasses',
                    'A method that only takes integers',
                    'A method defined inside standard functions',
                    'A method that deletes objects',
                ],
                'answer': 'A method decorated with @abstractmethod that has no implementation in the base class and must be overridden by subclasses',
            },
            {
                'question': 'What is a Concrete Method in an Abstract Base Class?',
                'options': [
                    'A method with a complete implementation that subclasses can inherit directly',
                    'A method without a body',
                    'A C-extension method',
                    'A method that cannot be called',
                ],
                'answer': 'A method with a complete implementation that subclasses can inherit directly',
            },
        ],
        'theory': {
            'definition': 'Data Abstraction enforces contract interfaces for subclasses while hiding complex implementation details from callers.',
            'why': 'Simplifies interaction with complex software components by decoupling interface from internal implementation.',
            'rules': [
                'Abstract classes derive from abc.ABC.',
                'Abstract methods are decorated with @abstractmethod.',
                'Subclasses must implement all abstract methods before instantiation.',
                'Instantiating an abstract base class directly raises TypeError.',
            ],
            'examples': [
                'from abc import ABC, abstractmethod',
                'class Dog(Animal): def make_sound(self): return "Bark"',
            ],
        },
    },
    39: {
        'concept': 'Encapsulation is the bundling of data attributes and methods into a single class unit while restricting unauthorized direct access to protect data integrity. Python access specifiers include:\n1. Public Members (no underscore): Fully accessible from anywhere.\n2. Protected Members (single underscore prefix _): Intended for internal class and subclass use.\n3. Private Members (double underscore prefix __): Restricts direct external access using Name Mangling (_ClassName__variable).\nEncapsulation uses Getter methods (read access) and Setter methods (write access with optional validation) to control data updates safely.',
        'syntax': 'class Employee:\n    def __init__(self, name, salary):\n        self.name = name          # Public\n        self._dept = "IT"         # Protected\n        self.__salary = salary    # Private\n\n    def get_salary(self):         # Getter\n        return self.__salary\n\n    def set_salary(self, amount): # Setter\n        if amount > 0: self.__salary = amount',
        'example': {
            'code': '# Encapsulation with Private Attributes and Getter/Setter Methods\nclass Employee:\n    def __init__(self, name, salary):\n        self.name = name           # Public attribute\n        self.__salary = salary     # Private attribute\n\n    def get_salary(self):          # Getter method\n        return self.__salary\n\n    def set_salary(self, amount):  # Setter method\n        if amount > 0:\n            self.__salary = amount\n        else:\n            print("Invalid salary amount!")\n\nemp = Employee("Robert", 50000)\nprint("Name:", emp.name)\nprint("Salary via Getter:", emp.get_salary())\n\nemp.set_salary(60000)\nprint("Updated Salary:", emp.get_salary())',
            'output': 'Name: Robert\nSalary via Getter: 50000\nUpdated Salary: 60000',
            'explanation': '1. self.__salary uses double underscores, making it private to Employee class.\n2. Accessing emp.__salary directly from outside raises AttributeError.\n3. get_salary() and set_salary() provide safe, controlled access with validation logic.',
        },
        'fill_blanks': {
            'question': '# Declare private attribute in Python class\nclass BankAccount:\n    def __init__(self, balance):\n        self.____balance = balance',
            'answers': ['__'],
            'options': [
                '__',
                '_',
                'public',
                'private',
            ],
        },
        'compiler': {
            'title': 'Encapsulation Sandbox',
            'question': 'Complete getter method to access private salary.',
            'starter_code': 'class Employee:\n    def __init__(self, salary):\n        self.__salary = salary\n    def get_salary(self):\n        return self.____\n\nemp = Employee(50000)\nprint(emp.get_salary())',
            'options': [
                '__salary',
                '_salary',
                'salary',
                'get_salary',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is Encapsulation in Object-Oriented Programming?',
                'options': [
                    'Bundling data and operating methods into a single unit while restricting direct external access',
                    'Converting object data into SQL queries',
                    'Exposing all variables globally',
                    'Splitting code into multiple files',
                ],
                'answer': 'Bundling data and operating methods into a single unit while restricting direct external access',
            },
            {
                'question': 'How do you declare a private variable in a Python class?',
                'options': [
                    'By prefixing the variable name with a double underscore (e.g. self.__salary)',
                    'Using the private keyword',
                    'By prefixing with @private decorator',
                    'Enclosing variable in curly braces',
                ],
                'answer': 'By prefixing the variable name with a double underscore (e.g. self.__salary)',
            },
            {
                'question': 'What is Name Mangling in Python?',
                'options': [
                    'The interpreter mechanism that renames double underscore variables to _ClassName__variable to restrict direct access',
                    'A syntax error caused by invalid variable names',
                    'A database encryption tool',
                    'Garbage collection process',
                ],
                'answer': 'The interpreter mechanism that renames double underscore variables to _ClassName__variable to restrict direct access',
            },
            {
                'question': 'What is the purpose of Getter and Setter methods?',
                'options': [
                    'To safely read (getter) and modify (setter) private attributes with optional validation',
                    'To delete objects from memory',
                    'To compile code faster',
                    'To import external libraries',
                ],
                'answer': 'To safely read (getter) and modify (setter) private attributes with optional validation',
            },
            {
                'question': 'How are protected members indicated by convention in Python?',
                'options': [
                    'With a single underscore prefix (e.g. self._age)',
                    'With double underscores',
                    'With protected keyword',
                    'With dollar sign prefix',
                ],
                'answer': 'With a single underscore prefix (e.g. self._age)',
            },
        ],
        'theory': {
            'definition': 'Encapsulation binds data and operating methods together into a class unit, restricting direct state modification.',
            'why': 'Protects internal data integrity and enables safe access through controlled getter/setter validation.',
            'rules': [
                'Public members have no underscore prefix.',
                'Protected members use single underscore prefix _ as internal convention.',
                'Private members use double underscore prefix __ trigger Name Mangling (_ClassName__member).',
                'Use getters and setters to validate and access private members safely.',
            ],
            'examples': [
                'self.__salary = salary',
                'emp.get_salary()',
            ],
        },
    },
    40: {
        'concept': 'An iterator in Python is an object used to traverse through all elements of a collection (list, tuple, string, dictionary) one item at a time. Iterators implement the Iterator Protocol:\n1. __iter__(): Returns the iterator object itself.\n2. __next__(): Returns the next item from sequence, raising StopIteration exception when elements are exhausted.\nIterable vs Iterator: An Iterable (e.g. list) can return an iterator when passed to iter(iterable). An Iterator performs the actual iteration state tracking and responds to next(iterator). Custom iterators are created by defining a class implementing __iter__() and __next__().',
        'syntax': 'class CustomIterator:\n    def __init__(self, limit):\n        self.limit = limit\n        self.n = 1\n    def __iter__(self):\n        return self\n    def __next__(self):\n        if self.n > self.limit: raise StopIteration\n        x = self.n; self.n += 1; return x',
        'example': {
            'code': '# Built-in Iterator and Custom Iterator Class in Python\ns = "GFG"\nit = iter(s)\nprint(next(it))\nprint(next(it))\nprint(next(it))\n\n# Custom Iterator for Even Numbers\nclass EvenNumbers:\n    def __init__(self, limit):\n        self.limit = limit\n        self.n = 2\n\n    def __iter__(self):\n        return self\n\n    def __next__(self):\n        if self.n > self.limit:\n            raise StopIteration\n        x = self.n\n        self.n += 2\n        return x\n\neven = EvenNumbers(6)\nfor num in even:\n    print(num)',
            'output': 'G\nF\nG\n2\n4\n6',
            'explanation': '1. iter(s) turns string "GFG" into an iterator, and next(it) fetches characters sequentially.\n2. EvenNumbers implements __iter__() and __next__(), raising StopIteration when self.n > self.limit.\n3. Python for loop automatically invokes iter() and handles StopIteration exception.',
        },
        'fill_blanks': {
            'question': '# Complete iterator protocol method\nclass Counter:\n    def __iter__(self): return self\n    def ____(self):\n        if self.count > 10: raise StopIteration',
            'answers': ['__next__'],
            'options': [
                '__next__',
                '__iter__',
                '__get__',
                '__step__',
            ],
        },
        'compiler': {
            'title': 'Iterators Sandbox',
            'question': 'Raise exception when iterator is exhausted.',
            'starter_code': 'class Counter:\n    def __init__(self, limit): self.limit = limit; self.n = 1\n    def __iter__(self): return self\n    def __next__(self):\n        if self.n > self.limit:\n            raise ____\n        x = self.n; self.n += 1; return x\n\nfor num in Counter(3): print(num)',
            'options': [
                'StopIteration',
                'ValueError',
                'IndexError',
                'StopAsyncIteration',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What two methods form the Python Iterator Protocol?',
                'options': [
                    '__iter__() and __next__()',
                    '__init__() and __str__()',
                    '__start__() and __stop__()',
                    '__get__() and __set__()',
                ],
                'answer': '__iter__() and __next__()',
            },
            {
                'question': 'What exception is raised by an iterator when there are no more elements to return?',
                'options': [
                    'StopIteration',
                    'IndexError',
                    'KeyError',
                    'ValueError',
                ],
                'answer': 'StopIteration',
            },
            {
                'question': 'What is the difference between an Iterable and an Iterator in Python?',
                'options': [
                    'An Iterable is an object that can return an iterator (via __iter__), while an Iterator tracks state and returns elements via __next__',
                    'Iterables and Iterators are identical',
                    'Iterators can only be integers',
                    'An Iterable can use next() directly, but an Iterator cannot',
                ],
                'answer': 'An Iterable is an object that can return an iterator (via __iter__), while an Iterator tracks state and returns elements via __next__',
            },
            {
                'question': 'Which built-in function converts an iterable into an iterator object?',
                'options': [
                    'iter()',
                    'next()',
                    'list()',
                    'str()',
                ],
                'answer': 'iter()',
            },
            {
                'question': 'What is lazy evaluation in the context of Python iterators?',
                'options': [
                    'Generating and returning items one at a time on demand, saving memory compared to storing all items at once',
                    'Delaying code execution until user keypress',
                    'Slow network requests',
                    'Skipping error checks',
                ],
                'answer': 'Generating and returning items one at a time on demand, saving memory compared to storing all items at once',
            },
        ],
        'theory': {
            'definition': 'An Iterator is a stateful object that traverses a collection sequentially using the __iter__() and __next__() protocol methods.',
            'why': 'Provides lazy evaluation (memory-efficient processing of large datasets) and uniform iteration syntax.',
            'rules': [
                '__iter__() must return the iterator object (usually self).',
                '__next__() must return the next item or raise StopIteration exception.',
                'iter(obj) creates an iterator from an iterable; next(it) fetches the next value.',
            ],
            'examples': [
                'it = iter([1, 2, 3])',
                'next(it)',
            ],
        },
    },
    41: {
        'concept': 'Exception Handling in Python allows programs to catch and handle unexpected errors during runtime gracefully without crashing abruptly. Runtime errors include invalid input, division by zero, missing files, or type mismatches. Python provides four main keywords:\n1. try: Contains code that might trigger an exception.\n2. except: Catches and handles specific or multiple exception types.\n3. else: Executes only if no exceptions occur in the try block.\n4. finally: Executes unconditionally, ideal for cleanup tasks like closing files or connections.\nExceptions can be triggered explicitly using the raise keyword (e.g. raise ValueError("Message")). Errors occur at logic/syntax compile-time, whereas exceptions occur at runtime and can be managed.',
        'syntax': 'try:\n    res = 100 / n\nexcept ZeroDivisionError:\n    print("You can\'t divide by zero!")\nexcept (ValueError, TypeError) as e:\n    print("Invalid value or type:", e)\nelse:\n    print("Result is", res)\nfinally:\n    print("Execution complete.")',
        'example': {
            'code': '# Python Exception Handling with try-except-else-finally & raise\ndef set_age(age):\n    if age < 0:\n        raise ValueError("Age cannot be negative.")\n    print(f"Age set to {age}")\n\ntry:\n    n = 0\n    res = 100 / n\nexcept ZeroDivisionError:\n    print("You can\'t divide by zero!")\nexcept ValueError:\n    print("Enter a valid number!")\nelse:\n    print("Result is", res)\nfinally:\n    print("Execution complete.")\n\ntry:\n    set_age(-5)\nexcept ValueError as e:\n    print("Caught raised exception:", e)',
            'output': "You can't divide by zero!\nExecution complete.\nCaught raised exception: Age cannot be negative.",
            'explanation': '1. try block attempts division 100/n, which raises ZeroDivisionError.\n2. except ZeroDivisionError catches the error and prints a safe message.\n3. else block is skipped because an error occurred, while finally always executes.\n4. set_age(-5) explicitly raises ValueError via raise keyword.',
        },
        'fill_blanks': {
            'question': '# Complete try-except-finally structure\ntry:\n    res = 10 / 0\n_____ ZeroDivisionError:\n    print("Division by zero")\n_____:\n    print("Cleanup actions")',
            'answers': ['except', 'finally'],
            'options': [
                'except',
                'finally',
                'else',
                'catch',
            ],
        },
        'compiler': {
            'title': 'Exception Handling Sandbox',
            'question': 'Catch ZeroDivisionError in division code.',
            'starter_code': 'n = 0\ntry:\n    res = 100 / n\n____ ZeroDivisionError:\n    print("Cannot divide by zero")',
            'options': [
                'except',
                'catch',
                'else',
                'finally',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the purpose of Exception Handling in Python?',
                'options': [
                    'To catch unexpected runtime errors and manage them gracefully without crashing the program',
                    'To fix syntax errors automatically before running',
                    'To speed up CPU processing',
                    'To encrypt source code files',
                ],
                'answer': 'To catch unexpected runtime errors and manage them gracefully without crashing the program',
            },
            {
                'question': 'Which keyword block executes ONLY if NO exception occurs in the try block?',
                'options': [
                    'else',
                    'finally',
                    'except',
                    'catch',
                ],
                'answer': 'else',
            },
            {
                'question': 'Which keyword block ALWAYS runs regardless of whether an exception occurred or not?',
                'options': [
                    'finally',
                    'else',
                    'except',
                    'try',
                ],
                'answer': 'finally',
            },
            {
                'question': 'How do you explicitly trigger an exception in Python?',
                'options': [
                    'Using the raise keyword followed by an exception instance',
                    'Using the throw keyword',
                    'Calling sys.error()',
                    'Returning False from a function',
                ],
                'answer': 'Using the raise keyword followed by an exception instance',
            },
            {
                'question': 'Why is using a bare `except:` catch-all handler generally discouraged?',
                'options': [
                    'It catches all exceptions indiscriminately, potentially masking unhandled bugs or system signals like KeyboardInterrupt',
                    'It causes a syntax error in Python 3',
                    'It runs slower than named except blocks',
                    'It can only be used inside classes',
                ],
                'answer': 'It catches all exceptions indiscriminately, potentially masking unhandled bugs or system signals like KeyboardInterrupt',
            },
        ],
        'theory': {
            'definition': 'Exception Handling enables programs to intercept runtime exceptions using try, except, else, and finally control blocks.',
            'why': 'Improves software reliability, prevents unexpected crashes, and guarantees resource cleanup.',
            'rules': [
                'try block contains risky code that might raise an exception.',
                'except block handles specific or tuple-grouped exception types.',
                'else block executes when try completes without raising an exception.',
                'finally block executes unconditionally for cleanup tasks.',
                'raise keyword manually triggers an exception instance.',
            ],
            'examples': [
                'try: res = 10 / 0\nexcept ZeroDivisionError: print("Err")',
                'raise ValueError("Invalid parameter")',
            ],
        },
    },
    42: {
        'concept': 'Python provides a standard set of built-in exceptions derived from the root class BaseException. To study built-in exceptions systematically, they are organized into chapters featuring 2 exception types per chapter:\n\n- Chapter 1: Root & Base Exceptions -> BaseException (root exception hierarchy class) & Exception (base class for non-exit exceptions).\n- Chapter 2: Arithmetic Exceptions -> ArithmeticError (base class for math calculation errors) & ZeroDivisionError (division or modulo by 0).\n- Chapter 3: Numerical Overflow & Precision -> OverflowError (numeric result too large to represent) & FloatingPointError (IEEE floating-point operation error).\n- Chapter 4: Assertion & Attribute Access -> AssertionError (assert condition failure) & AttributeError (accessing non-existent object attribute).\n- Chapter 5: Sequence & Dictionary Lookups -> IndexError (sequence index out of bounds) & KeyError (missing dictionary key).\n- Chapter 6: Memory & Name Resolution -> MemoryError (RAM allocation failure) & NameError (accessing unassigned variable name).\n- Chapter 7: Operating System & File I/O -> OSError (system I/O failure) & FileNotFoundError (subclass of OSError for missing files/directories).\n- Chapter 8: Additional Standard Exceptions -> TypeError (inappropriate operand type) & ValueError (valid type but invalid value).',
        'syntax': '# Inspecting built-in exceptions dictionary\nbuiltins_dict = locals()["__builtins__"]\n\n# Catching specific built-in exception pairs\ntry:\n    val = d["missing_key"]\nexcept (IndexError, KeyError) as e:\n    print("Lookup Exception caught:", e)',
        'example': {
            'code': '# Python Built-in Exceptions (Grouped 2 Types per Chapter)\nimport math\nimport numpy as np\n\n# Chapter 1: BaseException & Exception\ntry:\n    raise Exception("Generic non-exit exception")\nexcept Exception as e:\n    print("Ch1 Exception:", e)\n\n# Chapter 2: ArithmeticError & ZeroDivisionError\ntry:\n    res = 10 / 0\nexcept ZeroDivisionError as e:\n    print("Ch2 ZeroDivisionError:", e)\n\n# Chapter 3: OverflowError & FloatingPointError\ntry:\n    res = math.exp(1000)\nexcept OverflowError as e:\n    print("Ch3 OverflowError:", e)\n\n# Chapter 4: AssertionError & AttributeError\nclass Dummy: pass\ntry:\n    d = Dummy()\n    val = d.missing_attr\nexcept AttributeError as e:\n    print("Ch4 AttributeError:", e)\n\n# Chapter 5: IndexError & KeyError\ntry:\n    d_dict = {"key1": "val1"}\n    val = d_dict["key2"]\nexcept KeyError as e:\n    print("Ch5 KeyError:", e)\n\n# Chapter 6: MemoryError & NameError\ntry:\n    print(undefined_variable)\nexcept NameError as e:\n    print("Ch6 NameError:", e)\n\n# Chapter 7: OSError & FileNotFoundError\ntry:\n    open("non_existent_file.txt")\nexcept FileNotFoundError as e:\n    print("Ch7 FileNotFoundError:", e)',
            'output': "Ch1 Exception: Generic non-exit exception\nCh2 ZeroDivisionError: division by zero\nCh3 OverflowError: math range error\nCh4 AttributeError: 'Dummy' object has no attribute 'missing_attr'\nCh5 KeyError: 'key2'\nCh6 NameError: name 'undefined_variable' is not defined\nCh7 FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'",
            'explanation': '1. BaseException forms the root of Python\'s exception hierarchy.\n2. Built-in exceptions are paired into 7 chapters (Root, Arithmetic, Overflow, Assertion/Attribute, Lookup, Memory/Name, OS/File).\n3. Catching specific built-in exception pairs makes code safer and easier to debug.',
        },
        'fill_blanks': {
            'question': '# Catch missing dictionary key exception\nd = {"a": 1}\ntry:\n    val = d["b"]\n_____ KeyError:\n    print("Key not found!")',
            'answers': ['except'],
            'options': [
                'except',
                'catch',
                'finally',
                'else',
            ],
        },
        'compiler': {
            'title': 'Built-in Exceptions Sandbox',
            'question': 'Catch NameError for undeclared variable.',
            'starter_code': 'try:\n    print(unknown_variable)\nexcept ____:\n    print("Variable is not defined")',
            'options': [
                'NameError',
                'KeyError',
                'TypeError',
                'ValueError',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the top-level root class for all exceptions in Python?',
                'options': [
                    'BaseException',
                    'Exception',
                    'ObjectException',
                    'StandardError',
                ],
                'answer': 'BaseException',
            },
            {
                'question': 'Which built-in exception is raised when dividing a number by zero in Python?',
                'options': [
                    'ZeroDivisionError (a subclass of ArithmeticError)',
                    'OverflowError',
                    'ValueError',
                    'TypeError',
                ],
                'answer': 'ZeroDivisionError (a subclass of ArithmeticError)',
            },
            {
                'question': 'What is the relationship between FileNotFoundError and OSError in Python 3?',
                'options': [
                    'FileNotFoundError is a specific subclass of OSError',
                    'OSError is a subclass of FileNotFoundError',
                    'They are unrelated built-in exceptions',
                    'FileNotFoundError is deprecated in Python 3',
                ],
                'answer': 'FileNotFoundError is a specific subclass of OSError',
            },
            {
                'question': 'Which exception occurs when accessing an out-of-range index in a Python list?',
                'options': [
                    'IndexError',
                    'KeyError',
                    'AttributeError',
                    'NameError',
                ],
                'answer': 'IndexError',
            },
            {
                'question': 'What built-in exception is raised when trying to access a non-existent attribute on an object?',
                'options': [
                    'AttributeError',
                    'KeyError',
                    'NameError',
                    'TypeError',
                ],
                'answer': 'AttributeError',
            },
        ],
        'theory': {
            'definition': 'Built-in exceptions are predefined exception classes in Python representing runtime errors, arithmetic issues, sequence lookups, and OS failures.',
            'why': 'Provides standardized error types across the standard library for robust exception handling.',
            'rules': [
                'All built-in exceptions inherit from BaseException.',
                'User exceptions and standard runtime errors inherit from Exception.',
                'Chapter 1: BaseException & Exception (Base Hierarchy).',
                'Chapter 2: ArithmeticError & ZeroDivisionError (Math Operations).',
                'Chapter 3: OverflowError & FloatingPointError (Numerical Limits).',
                'Chapter 4: AssertionError & AttributeError (Debug & Property Access).',
                'Chapter 5: IndexError & KeyError (Collection Lookups).',
                'Chapter 6: MemoryError & NameError (RAM Allocation & Variable Names).',
                'Chapter 7: OSError & FileNotFoundError (System & File IO).',
            ],
            'examples': [
                'locals()["__builtins__"]',
                'except (IndexError, KeyError):',
            ],
        },
    },
    43: {
        'concept': 'User-Defined (Custom) Exceptions in Python are created by defining a new class that inherits from Python\'s built-in Exception class or one of its standard subclasses (e.g. RuntimeError, ValueError). Custom exceptions enable applications to define domain-specific error types (e.g. InvalidAgeError, InvalidEmailError, NetworkError).\n\nSteps to Create Custom Exceptions:\n1. Define Exception Class: Subclass Exception or a relevant standard exception.\n2. Customize Attributes & Methods: Add attributes (e.g. error_code, msg) and override __init__() and __str__() for readable error messages.\n3. Raise the Exception: Use raise CustomError(args) when a specific domain rule fails.\n4. Handle the Exception: Catch custom exceptions using targeted try-except blocks.',
        'syntax': 'class InvalidAgeError(Exception):\n    def __init__(self, age, msg="Age must be between 0 and 120", error_code=1001):\n        self.age = age\n        self.msg = msg\n        self.error_code = error_code\n        super().__init__(self.msg)\n\n    def __str__(self):\n        return f"[Error Code {self.error_code}] {self.age} -> {self.msg}"',
        'example': {
            'code': '# User-Defined Exceptions with Custom Attributes, Error Codes & Validation\nclass InvalidAgeError(Exception):\n    def __init__(self, age, msg="Age must be between 0 and 120", error_code=1001):\n        self.age = age\n        self.msg = msg\n        self.error_code = error_code\n        super().__init__(self.msg)\n\n    def __str__(self):\n        return f"[Error Code {self.error_code}] {self.age} -> {self.msg}"\n\nclass NetworkError(RuntimeError):\n    def __init__(self, arg):\n        self.args = (arg,)\n\nclass InvalidEmailError(Exception):\n    def __init__(self, email, msg="Invalid email format"):\n        self.email = email\n        self.msg = msg\n        super().__init__(self.msg)\n\n    def __str__(self):\n        return f"{self.email} -> {self.msg}"\n\ndef set_age(age):\n    if age < 0 or age > 120:\n        raise InvalidAgeError(age)\n    print(f"Age set to: {age}")\n\ndef set_email(email):\n    if "@" not in email:\n        raise InvalidEmailError(email)\n    print(f"Email set to: {email}")\n\ntry:\n    set_age(150)\nexcept InvalidAgeError as e:\n    print("Age Error caught:", e)\n\ntry:\n    set_email("userexample.com")\nexcept InvalidEmailError as e:\n    print("Email Error caught:", e)\n\ntry:\n    raise NetworkError("Connection failed")\nexcept NetworkError as e:\n    print("Network Error args:", e.args)',
            'output': '[Error Code 1001] 150 -> Age must be between 0 and 120\nuserexample.com -> Invalid email format\nNetwork Error args: (\'Connection failed\',)',
            'explanation': '1. InvalidAgeError inherits from Exception and overrides __init__ & __str__ to display error codes and age.\n2. NetworkError subclasses built-in RuntimeError for execution issues.\n3. InvalidEmailError validates email format with domain-specific exception handling.\n4. Targeted try-except blocks handle custom application errors cleanly.',
        },
        'fill_blanks': {
            'question': '# Complete custom exception class definition\nclass InvalidAgeError(____):\n    def __init__(self, msg):\n        super().__init__(msg)',
            'answers': ['Exception'],
            'options': [
                'Exception',
                'BaseClass',
                'object',
                'Error',
            ],
        },
        'compiler': {
            'title': 'User-Defined Exceptions Sandbox',
            'question': 'Raise custom exception when condition is met.',
            'starter_code': 'class CustomError(Exception): pass\n\ndef check(val):\n    if val < 0:\n        ____ CustomError("Value cannot be negative")\n\ntry:\n    check(-1)\nexcept CustomError as e:\n    print(e)',
            'options': [
                'raise',
                'return',
                'throw',
                'assert',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'How do you define a custom user-defined exception class in Python?',
                'options': [
                    'Create a new class that inherits from Exception or one of its subclasses',
                    'Write a function named custom_exception()',
                    'Use the custom keyword',
                    'Import sys.custom_error',
                ],
                'answer': 'Create a new class that inherits from Exception or one of its subclasses',
            },
            {
                'question': 'Why should custom exception classes invoke `super().__init__(msg)`?',
                'options': [
                    'To pass the error message string to the parent Exception class constructor for proper display',
                    'To allocate memory in C',
                    'To prevent the exception from being caught',
                    'To close open files automatically',
                ],
                'answer': 'To pass the error message string to the parent Exception class constructor for proper display',
            },
            {
                'question': 'Can a user-defined exception inherit from standard exceptions like RuntimeError or ValueError instead of Exception directly?',
                'options': [
                    'Yes, subclassing standard exceptions is useful when the custom error represents a specific standard error category',
                    'No, custom exceptions must ONLY inherit directly from Exception',
                    'No, subclassing RuntimeError causes a syntax error',
                    'Only in Python 2',
                ],
                'answer': 'Yes, subclassing standard exceptions is useful when the custom error represents a specific standard error category',
            },
            {
                'question': 'What method can be overridden in a custom exception to provide a custom formatted string representation when printed?',
                'options': [
                    '__str__()',
                    '__init__()',
                    '__repr__()',
                    '__format__()',
                ],
                'answer': '__str__()',
            },
            {
                'question': 'When should user-defined exceptions be used in Python applications?',
                'options': [
                    'To represent application-specific domain errors (e.g., InvalidAgeError, DatabaseConnectionError) with rich error context',
                    'For loop iteration conditions',
                    'To replace standard print statements',
                    'Only when importing third-party libraries',
                ],
                'answer': 'To represent application-specific domain errors (e.g., InvalidAgeError, DatabaseConnectionError) with rich error context',
            },
        ],
        'theory': {
            'definition': 'User-defined exceptions are custom error classes created by subclassing Exception or built-in standard exceptions to handle domain-specific application errors.',
            'why': 'Improves error readability, enables targeted exception handling, and provides custom error payloads/codes.',
            'rules': [
                'Subclass from Exception or a relevant standard exception class (e.g. RuntimeError).',
                'Call super().__init__(msg) to pass error messages to base class.',
                'Override __str__() for custom formatted error outputs.',
                'Use raise CustomException(...) when domain validation fails.',
            ],
            'examples': [
                'class InvalidAgeError(Exception): pass',
                'raise InvalidAgeError(150)',
            ],
        },
    },
    44: {
        'concept': 'File handling in Python involves performing operations on files—creating, opening, reading, writing, and closing them—to manage data flow safely between application code and secondary storage. Files are opened using open(filename, mode) where mode defaults to "r" (read mode). Once open, file object attributes can be inspected:\n1. f.name: Returns the name or path of the opened file.\n2. f.mode: Returns the access mode ("r", "w", "a", etc.).\n3. f.closed: Returns True if the file stream is closed, False otherwise.\nUsing f.close() releases system handles. The with statement (with open(...) as f:) automatically closes the file upon block termination, avoiding resource leaks. Exception handling with try-except-finally guarantees file closure even if runtime errors occur.',
        'syntax': 'with open("geek.txt", "r") as f:\n    content = f.read()\n    print("Name:", f.name, "Mode:", f.mode)',
        'example': {
            'code': '# Opening, reading, checking properties, and closing files\n# 1. Writing data using with statement\nwith open("geek.txt", "w") as file:\n    file.write("Hello, Python!\nFile handling is easy with Python.")\n\n# 2. Reading file and checking properties with try-finally\ntry:\n    file = open("geek.txt", "r")\n    print("Filename:", file.name)\n    print("Mode:", file.mode)\n    print("Is Closed before close()?", file.closed)\n    content = file.read()\n    print("Content:\n" + content)\nexcept FileNotFoundError as e:\n    print("Error:", e)\nfinally:\n    file.close()\n    print("Is Closed after close()?", file.closed)',
            'output': 'Filename: geek.txt\nMode: r\nIs Closed before close()? False\nContent:\nHello, Python!\nFile handling is easy with Python.\nIs Closed after close()? True',
            'explanation': '1. open("geek.txt", "w") opens file for writing and with statement closes it automatically.\n2. open("geek.txt", "r") opens file in read mode and file.name/file.mode return file attributes.\n3. finally block ensures file.close() runs, setting file.closed to True.',
        },
        'fill_blanks': {
            'question': '# Complete with statement file opening\n_____ open("geek.txt", "r") _____ f:\n    content = f.read()',
            'answers': ['with', 'as'],
            'options': [
                'with',
                'as',
                'using',
                'from',
            ],
        },
        'compiler': {
            'title': 'File Handling Sandbox',
            'question': 'Check if file stream is closed using file attribute.',
            'starter_code': 'file = open("geek.txt", "r")\nfile.close()\nprint("Closed:", file.____)',
            'options': [
                'closed',
                'is_closed',
                'status',
                'state',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the default mode of the open() function in Python if no mode argument is supplied?',
                'options': [
                    '"r" (read mode)',
                    '"w" (write mode)',
                    '"a" (append mode)',
                    '"x" (exclusive create)',
                ],
                'answer': '"r" (read mode)',
            },
            {
                'question': 'What is the primary advantage of using the `with` statement when opening files?',
                'options': [
                    'It automatically handles closing the file when the block exits, preventing resource leaks',
                    'It encrypts file data on disk',
                    'It speeds up network file transfers',
                    'It allows writing without opening mode',
                ],
                'answer': 'It automatically handles closing the file when the block exits, preventing resource leaks',
            },
            {
                'question': 'Which file object property returns a boolean indicating whether the file is currently closed?',
                'options': [
                    'f.closed',
                    'f.is_closed',
                    'f.status',
                    'f.mode',
                ],
                'answer': 'f.closed',
            },
            {
                'question': 'What exception is raised by open("missing.txt", "r") if the specified file does not exist?',
                'options': [
                    'FileNotFoundError',
                    'IOError',
                    'FileExistsError',
                    'AttributeError',
                ],
                'answer': 'FileNotFoundError',
            },
            {
                'question': 'Why should files always be closed using close() or `with` statements?',
                'options': [
                    'To release operating system file descriptors and ensure buffered writes are saved to storage',
                    'To clear RAM memory completely',
                    'Because unclosed files are automatically deleted by OS',
                    'To avoid SyntaxError',
                ],
                'answer': 'To release operating system file descriptors and ensure buffered writes are saved to storage',
            },
        ],
        'theory': {
            'definition': 'File handling manages operations (create, open, read, write, close) to transfer data between Python code and local storage.',
            'why': 'Persists data permanently across program restarts and interfaces with external file formats.',
            'rules': [
                'open(file, mode) returns a file stream object.',
                'close() releases system handles and flushes write buffers.',
                'with open(...) as f: ensures automatic file stream cleanup.',
                'f.name, f.mode, and f.closed reflect stream properties.',
            ],
            'examples': [
                'with open("geek.txt", "r") as f: content = f.read()',
                'f.close()',
            ],
        },
    },
    45: {
        'concept': 'Reading a file accesses text, binary data, or formatted structures (CSV, JSON). Python provides several reading strategies:\n1. read(): Reads entire file or specified N bytes/chars (e.g. read(10)).\n2. readline(): Reads a single line at a time (ideal for sequential processing of huge files).\n3. Line-by-line Loop (for line in file:): Iterates over lines in a memory-efficient manner using line.strip() to trim newlines.\n4. Reading Binary Files ("rb" mode): Reads raw byte sequences for images, executables, or non-text files.\n5. Structured Data Reading: Uses csv.reader (via csv module & io.StringIO) for tabular CSV data and json.load() for parsing JSON files into Python dictionaries.',
        'syntax': '# Reading techniques in Python\nwith open("geeks.txt", "r") as f:\n    for line in f:\n        print(line.strip())\n\n# Reading CSV and JSON\nimport csv, json\ndata = json.load(open("sample.json"))',
        'example': {
            'code': '# Comprehensive File Reading (Text, Binary, CSV, JSON)\nimport csv\nimport io\nimport json\n\n# Setup sample text file\nwith open("geeks.txt", "w") as f:\n    f.write("Hello World\nHello GeeksforGeeks\n")\n\n# 1. Reading line by line using readline()\nwith open("geeks.txt", "r") as f:\n    line = f.readline()\n    while line:\n        print("ReadLine:", line.strip())\n        line = f.readline()\n\n# 2. Reading specific partial content (first 10 chars)\nwith open("geeks.txt", "r") as f:\n    print("First 10 chars:", f.read(10))\n\n# 3. Reading In-Memory CSV data\ncsv_data = "Year,Industry,Value\n2014,Manufacturing,769400\n"\ncsv_reader = csv.reader(io.StringIO(csv_data))\nfor row in csv_reader:\n    print("CSV Row:", row)\n\n# 4. Reading JSON string/file\njson_str = \'{"fruit": "Apple", "size": "Large", "color": "Red"}\'\ndata = json.loads(json_str)\nprint("JSON Object:", data["fruit"], data["color"])',
            'output': 'ReadLine: Hello World\nReadLine: Hello GeeksforGeeks\nFirst 10 chars: Hello Worl\nCSV Row: [\'Year\', \'Industry\', \'Value\']\nCSV Row: [\'2014\', \'Manufacturing\', \'769400\']\nJSON Object: Apple Red',
            'explanation': '1. readline() fetches lines one by one to avoid loading huge files entirely in RAM.\n2. f.read(10) reads only 10 characters.\n3. csv.reader parses CSV streams into Python lists.\n4. json.loads/json.load parses JSON streams into Python dictionaries.',
        },
        'fill_blanks': {
            'question': '# Open file in read binary mode\nwith open("image.bin", "____") as f:\n    content = f.read()',
            'answers': ['rb'],
            'options': [
                'rb',
                'r',
                'wb',
                'b',
            ],
        },
        'compiler': {
            'title': 'Read Files Sandbox',
            'question': 'Read a single line from file stream.',
            'starter_code': 'with open("geeks.txt", "r") as f:\n    line = f.____()\n    print(line.strip())',
            'options': [
                'readline',
                'read',
                'readlines',
                'get_line',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the key advantage of reading large log files using `for line in file:` or `readline()` over `read()`?',
                'options': [
                    'It processes one line at a time without loading the whole file into RAM memory at once',
                    'It runs code in parallel threads',
                    'It automatically translates foreign languages',
                    'It deletes old lines after reading',
                ],
                'answer': 'It processes one line at a time without loading the whole file into RAM memory at once',
            },
            {
                'question': 'Which open mode must be specified when reading non-text binary files (like images or executables)?',
                'options': [
                    '"rb"',
                    '"r"',
                    '"wb"',
                    '"b"',
                ],
                'answer': '"rb"',
            },
            {
                'question': 'What does `f.read(10)` do when called on an open file object?',
                'options': [
                    'Reads at most the first 10 characters or bytes from the current file position',
                    'Reads the 10th line of the file',
                    'Repeats reading the file 10 times',
                    'Skips the first 10 lines',
                ],
                'answer': 'Reads at most the first 10 characters or bytes from the current file position',
            },
            {
                'question': 'Which Python standard module is used to parse JSON files into Python dictionaries?',
                'options': [
                    'json',
                    'csv',
                    'sys',
                    'pickle',
                ],
                'answer': 'json',
            },
            {
                'question': 'What string method is commonly used to strip trailing newline characters (`\\n`) when reading lines?',
                'options': [
                    'line.strip()',
                    'line.trim()',
                    'line.cut()',
                    'line.clean()',
                ],
                'answer': 'line.strip()',
            },
        ],
        'theory': {
            'definition': 'Reading files retrieves stored textual, binary, or structured data (CSV, JSON) using stream methods or module parsers.',
            'why': 'Enables processing datasets, configuration files, and binary assets efficiently.',
            'rules': [
                'read() fetches full or partial content.',
                'readline() reads a single line.',
                'for line in file: iterates over lines memory-efficiently.',
                '"rb" mode is required for binary data.',
                'csv.reader and json.load parse structured files.',
            ],
            'examples': [
                'for line in f: print(line.strip())',
                'data = json.load(f)',
            ],
        },
    },
    46: {
        'concept': 'Writing to a file creates new files or updates existing ones. Open modes for writing include:\n- "w": Overwrite mode (creates file if missing, erases/truncates content if existing).\n- "a": Append mode (creates file if missing, appends data always at the end).\n- "x": Exclusive creation mode (creates new file, fails with FileExistsError if file already exists).\n- "b": Binary flag ("wb", "ab" for raw bytes).\n- "+": Read/Write flag ("w+", "a+").\n- encoding & newline: Controls text encoding (e.g. "utf-8") and newline translations.\nWriting methods: write(str) writes a single string, writelines(sequence) writes a list of strings (newlines \\n must be included explicitly), and pathlib.Path("file.txt").write_text() provides modern path-based writing.',
        'syntax': 'with open("file.txt", "w", encoding="utf-8") as f:\n    f.write("Line 1\\n")\n\nwith open("file.txt", "a", encoding="utf-8") as f:\n    f.write("Appended line\\n")',
        'example': {
            'code': '# Overwrite, Append, Exclusive Create, Multiple Lines, and Binary Write\nfrom pathlib import Path\n\n# 1. Overwrite Mode ("w")\nwith open("file.txt", "w", encoding="utf-8") as f:\n    f.write("Created using write mode.\\n")\n\n# 2. Append Mode ("a")\nwith open("file.txt", "a", encoding="utf-8") as f:\n    f.write("Appended line.\\n")\n\n# 3. Writing multiple lines with join()\nlines = ["Line A", "Line B", "Line C"]\nwith open("file2.txt", "w", encoding="utf-8") as f:\n    f.write("\\n".join(lines) + "\\n")\n\n# 4. Binary Write Mode ("wb")\ndata = b"\\x00\\x01\\x02\\x03\\x04"\nwith open("file.bin", "wb") as f:\n    f.write(data)\n\n# 5. Pathlib write_text()\nPath("modern.txt").write_text("Hello World\\n")\n\nprint("file.txt content:\n" + Path("file.txt").read_text())\nprint("modern.txt content:\n" + Path("modern.txt").read_text())',
            'output': 'file.txt content:\nCreated using write mode.\nAppended line.\n\nmodern.txt content:\nHello World',
            'explanation': '1. Mode "w" truncates existing content before writing.\n2. Mode "a" appends text at the end of the file without deleting existing data.\n3. Mode "wb" handles binary bytes objects.\n4. Path.write_text() provides quick modern file writing.',
        },
        'fill_blanks': {
            'question': '# Open file in append mode\nwith open("log.txt", "____", encoding="utf-8") as f:\n    f.write("New entry\\n")',
            'answers': ['a'],
            'options': [
                'a',
                'w',
                'r',
                'x',
            ],
        },
        'compiler': {
            'title': 'Write/Create Files Sandbox',
            'question': 'Catch FileExistsError in exclusive mode "x".',
            'starter_code': 'try:\n    with open("file.txt", "x") as f:\n        f.write("Exclusive")\nexcept ____:\n    print("File already exists")',
            'options': [
                'FileExistsError',
                'FileNotFoundError',
                'IOError',
                'PermissionError',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What happens if you open an existing file in `"w"` (write) mode in Python?',
                'options': [
                    'Python truncates (erases) all existing content in the file before writing new data',
                    'Python appends new data at the end of the file',
                    'Python raises a FileExistsError',
                    'Python opens the file as read-only',
                ],
                'answer': 'Python truncates (erases) all existing content in the file before writing new data',
            },
            {
                'question': 'Which open mode creates a new file for writing but raises a `FileExistsError` if the file already exists?',
                'options': [
                    '"x" (Exclusive creation)',
                    '"w" (Write)',
                    '"a" (Append)',
                    '"r+" (Read/Write)',
                ],
                'answer': '"x" (Exclusive creation)',
            },
            {
                'question': 'Does the `writelines()` method automatically append newline characters (`\\n`) to each element?',
                'options': [
                    'No, you must include \\n explicitly in each string inside the list',
                    'Yes, it automatically appends \\n after each string',
                    'Yes, but only in text mode',
                    'Only if newline="auto" is set',
                ],
                'answer': 'No, you must include \\n explicitly in each string inside the list',
            },
            {
                'question': 'Which open mode must be used when writing raw bytes objects to disk?',
                'options': [
                    '"wb"',
                    '"w"',
                    '"a"',
                    '"x"',
                ],
                'answer': '"wb"',
            },
            {
                'question': 'How can you write text to a file using the pathlib module in one line?',
                'options': [
                    'Path("file.txt").write_text("content")',
                    'Path("file.txt").write("content")',
                    'Path("file.txt").save("content")',
                    'Path("file.txt").dump("content")',
                ],
                'answer': 'Path("file.txt").write_text("content")',
            },
        ],
        'theory': {
            'definition': 'Writing files outputs text or binary bytes to storage using overwrite ("w"), append ("a"), or exclusive create ("x") modes.',
            'why': 'Enables saving logs, exporting reports, updating state files, and writing binary assets.',
            'rules': [
                '"w" erases existing content or creates a new file.',
                '"a" appends data to the end of the file.',
                '"x" creates a new file, failing with FileExistsError if existing.',
                '"wb" writes raw bytes object data.',
                'writelines() writes string sequences without auto-adding newlines.',
            ],
            'examples': [
                'with open("file.txt", "w") as f: f.write("Hello")',
                'Path("file.txt").write_text("Hi")',
            ],
        },
    },
    47: {
        'concept': 'The os module provides portable operating system utility functions. To master the os module, its features are divided into two main categories:\n\n1. Directory & File System Operations: Current Working Directory (os.getcwd(), os.chdir(path)), Directory Creation (os.mkdir() for single, os.makedirs() for nested parent directories), Directory Listing (os.listdir(path)), File/Folder Deletion (os.remove(file), os.rmdir(dir)).\n\n2. Permissions, Metadata & OS Utilities: File Metadata (os.stat() returning st_size, st_mtime, st_mode), Permission Control (os.chmod(path, mode), os.chown(path, uid, gid)), OS Identifier (os.name returning "posix" or "nt"), Process Pipes (os.popen(command)), Low-level File Descriptors (os.close(fd) vs text file.close()), Renaming (os.rename(old, new)), and Path Checks (os.path.exists(path), os.path.getsize(path)).',
        'syntax': 'import os\n\ncwd = os.getcwd()\nos.chdir("../")\nos.mkdir("new_dir")\nstats = os.stat("file.txt")\nprint("Size:", os.path.getsize("file.txt"))',
        'example': {
            'code': '# OS Module Operations: Directory Handling & Permissions/Metadata\nimport os\n\n# 1. Directory Navigation & Creation\ncwd = os.getcwd()\nprint("OS Name:", os.name)\nprint("CWD:", cwd)\n\nif not os.path.exists("demo_dir"):\n    os.mkdir("demo_dir")\n    print("Created demo_dir")\n\nfile_path = os.path.join("demo_dir", "sample.txt")\nwith open(file_path, "w") as f:\n    f.write("OS Module Demo Content")\n\n# 2. Permissions & Metadata Inspection\nprint("File exists:", os.path.exists(file_path))\nprint("File size:", os.path.getsize(file_path), "bytes")\n\nstats = os.stat(file_path)\nprint("stat size:", stats.st_size, "bytes, mode:", oct(stats.st_mode)[-3:])\n\n# 3. Listing & Cleanup\nprint("Contents of demo_dir:", os.listdir("demo_dir"))\nos.remove(file_path)\nos.rmdir("demo_dir")\nprint("OS Cleanup complete.")',
            'output': 'OS Name: posix\nCWD: /workspace/backend\nCreated demo_dir\nFile exists: True\nFile size: 22 bytes\nstat size: 22 bytes, mode: 644\nContents of demo_dir: [\'sample.txt\']\nOS Cleanup complete.',
            'explanation': '1. Category 1 (Directory/File Operations): os.getcwd(), os.mkdir(), os.listdir(), os.remove(), and os.rmdir().\n2. Category 2 (Permissions/Metadata/Utilities): os.name, os.stat(), os.path.exists(), and os.path.getsize().',
        },
        'fill_blanks': {
            'question': '# Get current working directory\nimport os\ncwd = os.____()\nprint("CWD:", cwd)',
            'answers': ['getcwd'],
            'options': [
                'getcwd',
                'cwd',
                'get_path',
                'directory',
            ],
        },
        'compiler': {
            'title': 'OS Module Sandbox',
            'question': 'Check if path exists using os.path.',
            'starter_code': 'import os\nexists = os.path.____("geek.txt")\nprint("Exists:", exists)',
            'options': [
                'exists',
                'isfile',
                'isdir',
                'has_file',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the difference between os.mkdir() and os.makedirs() in Python?',
                'options': [
                    'os.mkdir() creates a single directory, while os.makedirs() recursively creates all missing parent directories',
                    'os.mkdir() works only on Linux, while os.makedirs() works only on Windows',
                    'os.makedirs() deletes files before creating directories',
                    'There is no difference in Python',
                ],
                'answer': 'os.mkdir() creates a single directory, while os.makedirs() recursively creates all missing parent directories',
            },
            {
                'question': 'What is the difference between os.remove() and os.rmdir()?',
                'options': [
                    'os.remove() deletes a file, while os.rmdir() deletes an empty directory',
                    'os.remove() deletes directories, while os.rmdir() deletes files',
                    'os.remove() renames files, while os.rmdir() copies folders',
                    'os.rmdir() deletes non-empty directories',
                ],
                'answer': 'os.remove() deletes a file, while os.rmdir() deletes an empty directory',
            },
            {
                'question': 'Which os.stat() attribute returns the file size in bytes?',
                'options': [
                    'st_size',
                    'st_mtime',
                    'st_mode',
                    'st_bytes',
                ],
                'answer': 'st_size',
            },
            {
                'question': 'Why does calling `os.close(f)` on a text file object `f = open(...)` raise a TypeError?',
                'options': [
                    'os.close() requires a low-level integer file descriptor (from os.open()), not a high-level TextIOWrapper file object',
                    'os.close() works only for binary files',
                    'os.close() requires root administrative privileges',
                    'Because open() files close automatically instantly',
                ],
                'answer': 'os.close() requires a low-level integer file descriptor (from os.open()), not a high-level TextIOWrapper file object',
            },
            {
                'question': 'Which function returns the string name of the imported OS module ("posix" or "nt")?',
                'options': [
                    'os.name',
                    'os.sysname',
                    'os.uname()',
                    'os.platform',
                ],
                'answer': 'os.name',
            },
        ],
        'theory': {
            'definition': 'The os module provides operating system-dependent interfaces for directory management, metadata querying, and permissions.',
            'why': 'Essential for cross-platform system scripting, automating file workflows, and permission management.',
            'rules': [
                'Category 1 (Directory Ops): getcwd(), chdir(), mkdir(), makedirs(), listdir(), remove(), rmdir().',
                'Category 2 (Metadata/Permissions/Utils): stat(), chmod(), name, popen(), close(), rename(), path.exists().',
                'os.mkdir() fails if parent directories are missing; os.makedirs() creates missing parents.',
                'os.stat() returns file metadata tuple (st_size, st_mtime, st_mode).',
            ],
            'examples': [
                'cwd = os.getcwd()',
                'os.mkdir("dir")',
                'os.path.exists("file.txt")',
            ],
        },
    },
    48: {
        'concept': 'The pathlib module (Python 3.4+) provides an object-oriented, cross-platform framework to work with filesystem paths. Unlike os.path which treats paths as raw strings, pathlib represents them as objects, overloading the / operator for intuitive path joining.\n\nPathlib Classes Split into 2 Main Categories:\n\n1. Pure Paths (PurePath, PurePosixPath, PureWindowsPath): Perform purely string-based path manipulations (joining, splitting, normalizing, inspecting name/suffix/parent) without touching the actual filesystem (usable cross-platform on any OS).\n\n2. Concrete Paths (Path, PosixPath, WindowsPath): Inherit from Pure paths and perform actual filesystem I/O (checking existence with exists(), creating empty files with touch(), directory listing with iterdir(), recursive file matching with rglob(), and quick file I/O with write_text() / read_text()).',
        'syntax': 'from pathlib import Path, PurePath\n\n# 1. Pure Path Manipulation\npure = PurePath("foo/bar/file.txt")\nprint(pure.name, pure.suffix, pure.parent)\n\n# 2. Concrete Path Filesystem I/O\np = Path.cwd() / "sample.txt"\np.touch()\np.write_text("Hello Pathlib")\ncontent = p.read_text()',
        'example': {
            'code': '# Pathlib Split: Pure Paths vs Concrete Paths & Operations\nfrom pathlib import Path, PurePosixPath, PureWindowsPath\n\n# 1. Pure Paths (String-based path calculations without disk access)\npure_posix = PurePosixPath("foo/bar/example.txt")\npure_win = PureWindowsPath("foo/bar/example.txt")\n\nprint("Pure Posix Path:", pure_posix)\nprint("Pure Windows Path:", pure_win)\nprint("Filename:", pure_posix.name)\nprint("Extension:", pure_posix.suffix)\nprint("Parent:", pure_posix.parent)\nprint("Is Absolute?", pure_posix.is_absolute())\n\n# 2. Concrete Paths (Interacts directly with filesystem)\np = Path.cwd()\ndemo_file = p / "sample.txt"\n\n# Create empty file with touch()\ndemo_file.touch()\nprint("File created on disk:", demo_file.exists())\nprint("Is Directory?", demo_file.is_dir())\n\n# Direct File I/O\ndemo_file.write_text("Hello from Pathlib!")\nprint("Content:", demo_file.read_text())\n\n# Cleanup\ndemo_file.unlink()\nprint("Exists after deletion:", demo_file.exists())',
            'output': 'Pure Posix Path: foo/bar/example.txt\nPure Windows Path: foo\\bar\\example.txt\nFilename: example.txt\nExtension: .txt\nParent: foo/bar\nIs Absolute? False\nFile created on disk: True\nIs Directory? False\nContent: Hello from Pathlib!\nExists after deletion: False',
            'explanation': '1. Category 1 (Pure Paths): PurePosixPath and PureWindowsPath manipulate path strings without contacting the disk.\n2. Category 2 (Concrete Paths): Path interacts with disk I/O (touch(), write_text(), read_text(), unlink()).\n3. Overloaded / operator joins paths cleanly.',
        },
        'fill_blanks': {
            'question': '# Join paths using pathlib operator\nfrom pathlib import Path\np = Path.cwd() _____ "documents" _____ "notes.txt"',
            'answers': ['/', '/'],
            'options': [
                '/',
                '/',
                '+',
                '\\',
            ],
        },
        'compiler': {
            'title': 'pathlib Module Sandbox',
            'question': 'Create an empty file using touch().',
            'starter_code': 'from pathlib import Path\nfile = Path("sample.txt")\nfile.____()\nprint("Created:", file.exists())',
            'options': [
                'touch',
                'create',
                'make',
                'build',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the key difference between Pure paths and Concrete paths in the pathlib module?',
                'options': [
                    'Pure paths only perform string-based path manipulations without disk access, while Concrete paths interact directly with the actual filesystem',
                    'Pure paths work only on Linux, while Concrete paths work only on Windows',
                    'Concrete paths cannot read or write files',
                    'Pure paths automatically delete files after access',
                ],
                'answer': 'Pure paths only perform string-based path manipulations without disk access, while Concrete paths interact directly with the actual filesystem',
            },
            {
                'question': 'Which operator is overloaded in pathlib for intuitive path joining?',
                'options': [
                    'The slash (/) operator',
                    'The plus (+) operator',
                    'The dot (.) operator',
                    'The star (*) operator',
                ],
                'answer': 'The slash (/) operator',
            },
            {
                'question': 'Which method recursively searches a directory tree for matching wildcard files (e.g. `*.py`) in pathlib?',
                'options': [
                    'rglob()',
                    'glob()',
                    'iterdir()',
                    'search()',
                ],
                'answer': 'rglob()',
            },
            {
                'question': 'What does `Path("sample.txt").touch()` do?',
                'options': [
                    'Creates an empty file if it does not exist, or updates its modification timestamp if it does',
                    'Deletes the file from disk',
                    'Reads the file content as text',
                    'Renames the file to sample.bak',
                ],
                'answer': 'Creates an empty file if it does not exist, or updates its modification timestamp if it does',
            },
            {
                'question': 'Which method in Path returns the file extension including the leading dot (e.g., ".txt")?',
                'options': [
                    'suffix',
                    'name',
                    'stem',
                    'parent',
                ],
                'answer': 'suffix',
            },
        ],
        'theory': {
            'definition': 'pathlib provides an object-oriented path library divided into Pure paths (string manipulations) and Concrete paths (filesystem I/O).',
            'why': 'Simplifies file path management, eliminates string concatenation bugs, and offers modern file read/write methods.',
            'rules': [
                'Category 1 (Pure Paths): PurePath, PurePosixPath, PureWindowsPath manipulate path strings cross-platform without disk calls.',
                'Category 2 (Concrete Paths): Path, PosixPath, WindowsPath perform disk I/O, touch(), unlink(), read_text(), write_text().',
                '/ operator joins path components cleanly.',
                'touch() creates empty files; unlink() deletes files.',
                'rglob() performs recursive file pattern matching.',
            ],
            'examples': [
                'p = Path("docs") / "notes.txt"',
                'p.touch()',
                'p.write_text("Hello")',
            ],
        },
    },
    49: {
        'concept': 'Directory Management involves programmatically managing folder structures—creating, listing, verifying, calculating directory size, renaming, copying, and deleting folders across operating systems. Directory management tools are split into two operational frameworks:\n\n1. OS & Pathlib Directory Operations: Creating (`os.mkdir`, `os.makedirs`, `Path.mkdir`), Listing (`os.listdir`, `Path.iterdir`), Directory Verification (`os.path.isdir`), Working Directory (`os.getcwd`, `os.chdir`), Timestamps (`os.path.getatime`, `os.path.getmtime`), and Recursive Tree Size calculation (`os.walk` + `os.path.getsize`).\n\n2. Shutil High-Level Management: Recursive Directory Copying (`shutil.copytree(src, dst, dirs_exist_ok=True)`), Irreversible Recursive Directory Deletion (`shutil.rmtree(path)`), and Directory Moving/Renaming (`shutil.move(src, dst)`).',
        'syntax': 'import os, shutil\nfrom pathlib import Path\n\n# OS & Pathlib directory ops\nos.makedirs("parent/child", exist_ok=True)\nis_dir = os.path.isdir("parent")\n\n# High-level Shutil directory ops\nshutil.copytree("src_dir", "dst_dir", dirs_exist_ok=True)\nshutil.rmtree("dst_dir")',
        'example': {
            'code': '# Directory Management: OS/Pathlib vs High-Level Shutil Operations\nimport os\nimport time\nimport shutil\nfrom pathlib import Path\n\n# 1. OS & Pathlib Directory Operations\nos.makedirs("test_dir/sub_dir", exist_ok=True)\nprint("Is directory?", os.path.isdir("test_dir"))\nprint("String CWD:", os.getcwd())\n\n# Create sample file\nfile_path = "test_dir/sub_dir/sample.txt"\nwith open(file_path, "w") as f:\n    f.write("Directory management sample content")\n\n# Calculate Directory Size using os.walk()\ntotal_size = 0\nfor dirpath, dirnames, filenames in os.walk("test_dir"):\n    for f in filenames:\n        fp = os.path.join(dirpath, f)\n        total_size += os.path.getsize(fp)\nprint("Total directory size:", total_size, "bytes")\n\n# Get timestamps\nacc_time = time.ctime(os.path.getatime("test_dir"))\nmod_time = time.ctime(os.path.getmtime("test_dir"))\nprint("Access Time:", acc_time)\nprint("Modification Time:", mod_time)\n\n# 2. Shutil High-Level Operations\nshutil.copytree("test_dir", "copied_dir", dirs_exist_ok=True)\nprint("Copied directory contents:", os.listdir("copied_dir"))\n\n# Cleanup\nshutil.rmtree("test_dir")\nshutil.rmtree("copied_dir")\nprint("Directory management cleanup complete.")',
            'output': 'Is directory? True\nString CWD: /workspace/backend\nTotal directory size: 36 bytes\nAccess Time: Mon Sep 21 19:45:00 2026\nModification Time: Mon Sep 21 19:45:00 2026\nCopied directory contents: [\'sub_dir\']\nDirectory management cleanup complete.',
            'explanation': '1. Framework 1 (OS/Pathlib): os.makedirs(), os.path.isdir(), os.walk() size summation, getatime()/getmtime().\n2. Framework 2 (Shutil): shutil.copytree() copies full directory trees recursively, while shutil.rmtree() deletes non-empty folder trees.',
        },
        'fill_blanks': {
            'question': '# Recursively remove directory tree using shutil\nimport shutil\nshutil.____("destination_dir")',
            'answers': ['rmtree'],
            'options': [
                'rmtree',
                'rmdir',
                'remove',
                'delete',
            ],
        },
        'compiler': {
            'title': 'Directory Management Sandbox',
            'question': 'Check if path is a directory using os.path.',
            'starter_code': 'import os\nis_folder = os.path.____("/home")\nprint("Is folder:", is_folder)',
            'options': [
                'isdir',
                'isfile',
                'exists',
                'is_path',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'Which shutil function recursively copies an entire directory tree (source directory and all contents) to a destination?',
                'options': [
                    'shutil.copytree()',
                    'shutil.copy()',
                    'shutil.move()',
                    'shutil.clone()',
                ],
                'answer': 'shutil.copytree()',
            },
            {
                'question': 'What is the main difference between os.rmdir() and shutil.rmtree()?',
                'options': [
                    'os.rmdir() deletes ONLY empty directories, while shutil.rmtree() deletes a directory and ALL its files and subdirectories recursively',
                    'shutil.rmtree() deletes single files only',
                    'os.rmdir() sends files to recycle bin',
                    'There is no difference in Python',
                ],
                'answer': 'os.rmdir() deletes ONLY empty directories, while shutil.rmtree() deletes a directory and ALL its files and subdirectories recursively',
            },
            {
                'question': 'How can you calculate the total byte size of a directory including all nested files in Python?',
                'options': [
                    'By traversing files with os.walk() and summing os.path.getsize() for each file',
                    'By calling os.path.getsize(directory_path) directly',
                    'Using sys.getsizeof(directory)',
                    'Using len(os.listdir(directory))',
                ],
                'answer': 'By traversing files with os.walk() and summing os.path.getsize() for each file',
            },
            {
                'question': 'Which function returns the last modification time of a file or directory as a timestamp?',
                'options': [
                    'os.path.getmtime()',
                    'os.path.getatime()',
                    'os.path.getctime()',
                    'os.path.time()',
                ],
                'answer': 'os.path.getmtime()',
            },
            {
                'question': 'What does shutil.move(src, dst) do if src and dst are on the same filesystem?',
                'options': [
                    'It performs a fast rename operation',
                    'It creates a duplicate backup copy',
                    'It raises a FileExistsError',
                    'It compresses the directory into a zip archive',
                ],
                'answer': 'It performs a fast rename operation',
            },
        ],
        'theory': {
            'definition': 'Directory management manages folder creation, listing, size calculation, access times, copying, moving, and recursive deletion via os, pathlib, and shutil.',
            'why': 'Required for automating project setup, file archiving, directory cloning, and disk space auditing.',
            'rules': [
                'Framework 1 (OS/Pathlib): os.mkdir(), os.makedirs(), os.listdir(), os.walk(), os.path.isdir(), os.path.getmtime().',
                'Framework 2 (Shutil): shutil.copytree(), shutil.rmtree(), shutil.move().',
                'os.rmdir() requires the target directory to be empty.',
                'shutil.rmtree() permanently deletes non-empty directory trees.',
                'os.walk() iterates recursively through all directory tree branches.',
            ],
            'examples': [
                'os.makedirs("parent/child", exist_ok=True)',
                'shutil.copytree("src", "dst")',
                'shutil.rmtree("dst")',
            ],
        },
    },
    50: {
        'concept': 'MongoDB is a document-based NoSQL database storing data in JSON-like BSON documents. In Python, pymongo enables database connections, collection management, and CRUD operations.',
        'syntax': 'import pymongo\nclient = pymongo.MongoClient("mongodb://localhost:27017/")\ndb = client["database_name"]\ncollection = db["collection_name"]\ncollection.insert_one({"key": "value"})\ncollection.find_one({"key": "value"})',
        'example': {
            'code': 'import pymongo\n\n# Simulated PyMongo CRUD demonstration\nstudent_doc = {"name": "Alice", "role": "Developer", "score": 95}\nprint(f"Document to insert: {student_doc}")\nprint(f"Query Filter: name == {student_doc[\'name\']}")',
            'output': 'Document to insert: {\'name\': \'Alice\', \'role\': \'Developer\', \'score\': 95}\nQuery Filter: name == Alice',
            'explanation': 'PyMongo uses Python dictionaries to construct BSON documents for MongoDB storage and query operations.',
        },
        'fill_blanks': {
            'question': 'Complete the PyMongo connection and document insertion snippet:',
            'answers': ['pymongo', 'MongoClient', 'insert_one'],
            'options': ['pymongo', 'MongoClient', 'insert_one', 'connect', 'save', 'push'],
        },
        'compiler': {
            'title': 'PyMongo Document Builder',
            'question': 'Arrange the lines to establish a PyMongo connection client and insert a document into a collection.',
            'starter_code': 'import pymongo\nclient = pymongo.MongoClient("mongodb://localhost:27017/")\ndb = client["school"]\nusers = db["students"]\nusers.insert_one({"name": "Bob", "grade": "A"})\nprint("Inserted successfully")',
            'options': [
                'import pymongo',
                'client = pymongo.MongoClient("mongodb://localhost:27017/")',
                'db = client["school"]',
                'users = db["students"]',
                'users.insert_one({"name": "Bob", "grade": "A"})',
                'print("Inserted successfully")',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What format does MongoDB use internally to store document data?',
                'options': ['XML', 'BSON', 'CSV', 'YAML'],
                'answer': 'BSON',
            },
            {
                'question': 'Which PyMongo function connects to a running MongoDB instance?',
                'options': ['pymongo.connect()', 'pymongo.MongoClient()', 'pymongo.Open()', 'pymongo.Server()'],
                'answer': 'pymongo.MongoClient()',
            },
            {
                'question': 'Which PyMongo collection method inserts a single document dictionary?',
                'options': ['insert_one()', 'add_doc()', 'save()', 'push()'],
                'answer': 'insert_one()',
            },
            {
                'question': 'How are MongoDB tables and rows represented in PyMongo?',
                'options': ['Tables as Matrices, Rows as Vectors', 'Collections as Collections, Rows as Lines', 'Collections as Collections, Documents as Dictionaries', 'Schemas as Files, Rows as Records'],
                'answer': 'Collections as Collections, Documents as Dictionaries',
            },
            {
                'question': 'Which method retrieves a single document matching a query filter in PyMongo?',
                'options': ['fetch_one()', 'find_one()', 'get_document()', 'select_one()'],
                'answer': 'find_one()',
            },
        ],
        'theory': {
            'definition': 'MongoDB is a leading NoSQL document database. PyMongo is the official Python driver for interacting with MongoDB databases, collections, and BSON documents.',
            'why': 'NoSQL document databases provide high performance, dynamic schemas, horizontal scalability, and effortless integration with JSON/Python dictionary data models.',
            'rules': [
                'MongoClient initializes connections via connection URI strings (e.g. mongodb://localhost:27017/).',
                'Databases and Collections are created lazily upon first document insertion.',
                'Documents in MongoDB are key-value pairs stored in binary JSON (BSON) format.',
                'Use insert_one() or insert_many() to write document dictionaries to collections.',
                'Use find() or find_one() with filter dictionaries to query stored documents.',
            ],
            'examples': [
                'client = pymongo.MongoClient("mongodb://localhost:27017/")',
                'db = client["mydb"]',
                'col = db["users"]',
                'col.insert_one({"name": "Alice", "age": 25})',
            ],
        },
    },
    51: {
        'concept': 'MySQL is a relational database management system (RDBMS) using structured tables and SQL. In Python, mysql-connector-python enables database connectivity, parameterized SQL queries, and transactional commits.',
        'syntax': 'import mysql.connector\nconn = mysql.connector.connect(host="localhost", user="root", password="pw", database="db")\ncursor = conn.cursor()\ncursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))\nresults = cursor.fetchall()\nconn.commit()\nconn.close()',
        'example': {
            'code': 'import mysql.connector\n\n# Simulated MySQL parameterized query setup\nquery = "SELECT id, name, role FROM employees WHERE department = %s"\nparams = ("Engineering",)\nprint(f"SQL Query: {query}")\nprint(f"Bound Parameters: {params}")',
            'output': 'SQL Query: SELECT id, name, role FROM employees WHERE department = %s\nBound Parameters: (\'Engineering\',)',
            'explanation': 'Parameterizing SQL queries using tuple binding (%s placeholders) prevents SQL injection vulnerabilities when executing statements via MySQL cursor.',
        },
        'fill_blanks': {
            'question': 'Complete the MySQL connection and cursor execution snippet:',
            'answers': ['mysql.connector', 'connect', 'cursor', 'execute'],
            'options': ['mysql.connector', 'connect', 'cursor', 'execute', 'query', 'run'],
        },
        'compiler': {
            'title': 'MySQL Connector Pipeline',
            'question': 'Arrange the code lines to connect to a MySQL database, create a cursor, execute a parameterized query, and fetch all matching records.',
            'starter_code': 'import mysql.connector\nconn = mysql.connector.connect(host="localhost", user="root", password="secret", database="company")\ncursor = conn.cursor()\ncursor.execute("SELECT * FROM employees WHERE status = %s", ("Active",))\nrows = cursor.fetchall()\nprint(f"Fetched {len(rows)} active employees")',
            'options': [
                'import mysql.connector',
                'conn = mysql.connector.connect(host="localhost", user="root", password="secret", database="company")',
                'cursor = conn.cursor()',
                'cursor.execute("SELECT * FROM employees WHERE status = %s", ("Active",))',
                'rows = cursor.fetchall()',
                'print(f"Fetched {len(rows)} active employees")',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'Which package is commonly used in Python to connect directly to MySQL servers?',
                'options': ['mysql-connector-python', 'pymongo', 'sqlite3_mysql', 'py-database'],
                'answer': 'mysql-connector-python',
            },
            {
                'question': 'What object executes SQL statements and retrieves database result rows?',
                'options': ['Connection', 'Cursor', 'Transaction', 'QuerySet'],
                'answer': 'Cursor',
            },
            {
                'question': 'Why should parameterized SQL queries (%s) be used instead of string formatting?',
                'options': ['To improve font rendering', 'To prevent SQL Injection attacks', 'To automatically encrypt database passwords', 'To bypass SQL syntax verification'],
                'answer': 'To prevent SQL Injection attacks',
            },
            {
                'question': 'Which connection method must be called to save INSERT, UPDATE, or DELETE changes permanently?',
                'options': ['conn.commit()', 'conn.save()', 'conn.persist()', 'conn.flush()'],
                'answer': 'conn.commit()',
            },
            {
                'question': 'Which cursor method returns all remaining rows of a query result set as a list of tuples?',
                'options': ['cursor.get_all()', 'cursor.fetchall()', 'cursor.read_all()', 'cursor.collect()'],
                'answer': 'cursor.fetchall()',
            },
        ],
        'theory': {
            'definition': 'MySQL is a popular open-source relational database (RDBMS). mysql-connector-python is an official driver allowing Python applications to interact with MySQL databases using standard SQL syntax.',
            'why': 'RDBMS systems ensure strict ACID transactions, normalized relational schemas, and complex multi-table JOIN operations essential for enterprise data integrity.',
            'rules': [
                'Establish connections using mysql.connector.connect(host, user, password, database).',
                'Create a cursor object using conn.cursor() to execute commands and fetch result sets.',
                'Use parameterized placeholders (%s) to safely bind user inputs to query execution calls.',
                'Call conn.commit() after DML operations (INSERT, UPDATE, DELETE) to persist changes.',
                'Always close cursors and connection instances using cursor.close() and conn.close().',
            ],
            'examples': [
                'conn = mysql.connector.connect(host="localhost", user="admin", password="pass", database="shop")',
                'cursor = conn.cursor()',
                'cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("Widget", 19.99))',
                'conn.commit()',
            ],
        },
    },
    52: {
        'concept': 'Python packages organize related modules into directory hierarchies containing an __init__.py file. Packages support sub-packages, module namespace isolation, and dot-notation imports across domain ecosystems like Web, AI/ML, GUI, Web Scraping, and Game Dev.',
        'syntax': '# Package Directory Structure\n# mypackage/__init__.py\n# mypackage/basic/__init__.py\n# mypackage/basic/add.py\n\nfrom mypackage.basic.add import add\nresult = add(10, 5)',
        'example': {
            'code': '# Package hierarchy demonstration: math_operations\n# Structure: math_operations/basic/add.py & sub.py\nfrom math_operations.basic import add, subtract\nfrom math_operations.advanced import multiply, divide\n\nprint(f"Addition: {add(5, 3)}")\nprint(f"Multiplication: {multiply(4, 2)}")',
            'output': 'Addition: 8\nMultiplication: 8',
            'explanation': 'Packages allow organizing functions into logical sub-packages (basic, advanced) and importing them cleanly using dot notation.',
        },
        'fill_blanks': {
            'question': 'Complete the package initialization and function import statement:',
            'answers': ['__init__.py', 'math_operations', 'basic', 'add'],
            'options': ['__init__.py', 'math_operations', 'basic', 'add', 'import_all', 'setup.py'],
        },
        'compiler': {
            'title': 'Package Builder and Exporter',
            'question': 'Arrange the lines to create sub-package imports and execute exported math functions.',
            'starter_code': 'from math_operations import calculate\nfrom math_operations.basic import add, subtract\nfrom math_operations.advanced import multiply\ncalculate()\nprint(f"Add: {add(10, 20)}")\nprint(f"Multiply: {multiply(5, 4)}")',
            'options': [
                'from math_operations import calculate',
                'from math_operations.basic import add, subtract',
                'from math_operations.advanced import multiply',
                'calculate()',
                'print(f"Add: {add(10, 20)}")',
                'print(f"Multiply: {multiply(5, 4)}")',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What special file must be present in a directory for Python to treat it as a package?',
                'options': ['__init__.py', '__main__.py', 'package.json', 'setup.py'],
                'answer': '__init__.py',
            },
            {
                'question': 'How are nested sub-packages and modules accessed during import?',
                'options': ['Using slash notation (from pkg/subpkg)', 'Using dot notation (from pkg.subpkg.module)', 'Using colon notation (from pkg::subpkg)', 'Using arrow notation (from pkg->subpkg)'],
                'answer': 'Using dot notation (from pkg.subpkg.module)',
            },
            {
                'question': 'Which Python package category includes NumPy, Pandas, Scikit-learn, and PyTorch?',
                'options': ['Web Frameworks', 'AI & Machine Learning', 'Game Development', 'GUI Applications'],
                'answer': 'AI & Machine Learning',
            },
            {
                'question': 'What is the primary benefit of organizing code into Python packages?',
                'options': ['It automatically compiles Python into machine bytecode', 'It prevents all runtime exceptions', 'It provides modularity, reusability, and clean namespace separation', 'It eliminates the need for functions'],
                'answer': 'It provides modularity, reusability, and clean namespace separation',
            },
            {
                'question': 'Which package is commonly used for Web Scraping and automation in Python?',
                'options': ['PyGame', 'BeautifulSoup', 'Tkinter', 'Kivy'],
                'answer': 'BeautifulSoup',
            },
        ],
        'theory': {
            'definition': 'A Python package is a folder containing a special __init__.py file and one or more Python modules or sub-packages.',
            'why': 'Packages enable developers to organize complex codebases into modular, reusable, and easily distributable component hierarchies.',
            'rules': [
                'Every package directory must contain an __init__.py file (can be empty or export API symbols).',
                'Sub-packages are subdirectories inside packages containing their own __init__.py file.',
                'Use relative imports (e.g. from .basic import add) inside package modules.',
                'Import functions or classes using dot notation (from package.subpackage.module import item).',
                'Organize packages by domain concerns (e.g. basic ops, advanced ops, utilities).',
            ],
            'examples': [
                '# Directory: mypkg/__init__.py, mypkg/utils.py',
                'from mypkg.utils import helper_function',
                'from mypkg import subpackage',
            ],
        },
    },
    53: {
        'concept': 'A Python module is a single .py file containing functions, classes, and variables. Python supports 4 import forms, 4 module categories (built-in, user-defined, third-party, package), and resolves paths via sys.path.',
        'syntax': 'import module_name\nfrom module_name import function_name\nfrom module_name import *\nimport module_name as alias_name\nimport sys\nprint(sys.path)',
        'example': {
            'code': '# User-defined module calc.py simulation\ndef add(x, y):\n    return x + y\n\ndef subtract(x, y):\n    return x - y\n\n# Importing module functionality using alias\nimport math as m\nprint(f"Square root via math alias: {m.sqrt(16)}")\nprint(f"Addition via calc function: {add(10, 2)}")',
            'output': 'Square root via math alias: 4.0\nAddition via calc function: 12',
            'explanation': 'Modules group related statements into reusable files. Importing specific names or using aliases keeps code organized.',
        },
        'fill_blanks': {
            'question': 'Complete the module import and search path inspection snippet:',
            'answers': ['import', 'from', 'as', 'sys.path'],
            'options': ['import', 'from', 'as', 'sys.path', 'load', 'include'],
        },
        'compiler': {
            'title': 'Module Importer and Alias System',
            'question': 'Arrange the lines to import built-in math and random modules using aliases and print results.',
            'starter_code': 'import math as m\nimport random as rnd\nval = m.factorial(5)\nnum = rnd.randint(1, 10)\nprint(f"Factorial of 5: {val}")\nprint(f"Random number: {num}")',
            'options': [
                'import math as m',
                'import random as rnd',
                'val = m.factorial(5)',
                'num = rnd.randint(1, 10)',
                'print(f"Factorial of 5: {val}")',
                'print(f"Random number: {num}")',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is a Python module?',
                'options': ['A binary executable file', 'A single Python file containing code definitions and statements', 'A database table', 'An OS environment variable'],
                'answer': 'A single Python file containing code definitions and statements',
            },
            {
                'question': 'Which list of directory paths does Python search to locate imported modules?',
                'options': ['os.environ', 'sys.path', 'pathlib.ROOT', 'site.packages_list'],
                'answer': 'sys.path',
            },
            {
                'question': 'Why is `from module import *` generally discouraged in large projects?',
                'options': ['It causes syntax errors in Python 3', 'It pollutes the local namespace and can cause silent name conflicts', 'It runs significantly slower than normal imports', 'It deletes module variables after execution'],
                'answer': 'It pollutes the local namespace and can cause silent name conflicts',
            },
            {
                'question': 'Which of the following is a built-in Python module that requires no installation?',
                'options': ['requests', 'math', 'pandas', 'django'],
                'answer': 'math',
            },
            {
                'question': 'What keyword is used to assign a shorter local name to an imported module?',
                'options': ['alias', 'as', 'with', 'using'],
                'answer': 'as',
            },
        ],
        'theory': {
            'definition': 'A module is a file containing Python code (functions, classes, variables) saved with a .py extension that can be imported and reused across programs.',
            'why': 'Modules divide large programs into small, manageable, and isolated files, preventing code duplication and variable name collisions.',
            'rules': [
                'Module names match their filename without the .py extension (e.g. calc.py -> import calc).',
                'Use import module to load the entire module namespace under the module prefix.',
                'Use from module import name to bring specific attributes into the current namespace.',
                'Use import module as alias to shorten long module names (e.g. import numpy as np).',
                'Python checks sys.path in order: current directory, PYTHONPATH, standard library, site-packages.',
            ],
            'examples': [
                'import math\nprint(math.pi)',
                'from math import sqrt\nprint(sqrt(25))',
                'import sys\nfor path in sys.path: print(path)',
            ],
        },
    },
    54: {
        'concept': 'Python provides rich built-in DSA modules (array, deque, queue.Queue, collections, heapq, bisect, NumPy basics) and specialized external libraries (treelib, intervaltree, pygtrie) for high-performance data structures.',
        'syntax': 'from collections import deque, Counter, defaultdict\nimport heapq\nimport bisect\n\nd = deque([1, 2, 3])\nd.appendleft(0)\n\nh = [5, 1, 3]\nheapq.heapify(h)\nsmallest = heapq.heappop(h)',
        'example': {
            'code': 'from collections import deque, Counter\nimport heapq\nimport bisect\n\n# 1. Double-ended queue\ndq = deque(["a", "b"])\ndq.appendleft("start")\n\n# 2. Min-Heap Priority Queue\nheap = [10, 20, 5]\nheapq.heapify(heap)\n\n# 3. Bisect binary search on sorted list\nnums = [10, 20, 30, 40]\nidx = bisect.bisect_left(nums, 25)\n\nprint(f"Deque: {list(dq)}")\nprint(f"Heap smallest: {heapq.heappop(heap)}")\nprint(f"Bisect insert index for 25: {idx}")',
            'output': 'Deque: [\'start\', \'a\', \'b\']\nHeap smallest: 5\nBisect insert index for 25: 2',
            'explanation': 'Built-in modules offer optimized data structures: deque for O(1) double-ended operations, heapq for min-heaps, and bisect for binary search on sorted lists.',
        },
        'fill_blanks': {
            'question': 'Complete the DSA library operations for deque, min-heap, and bisect:',
            'answers': ['deque', 'heapq', 'Counter', 'bisect'],
            'options': ['deque', 'heapq', 'Counter', 'bisect', 'tree', 'trie'],
        },
        'compiler': {
            'title': 'DSA Module Toolkit Explorer',
            'question': 'Arrange the lines to initialize a deque, heapify a list, count element frequencies, and find a binary search insertion point.',
            'starter_code': 'from collections import deque, Counter\nimport heapq\nimport bisect\nq = deque([10, 20])\nq.appendleft(5)\nh = [9, 3, 7]\nheapq.heapify(h)\ncounts = Counter(["a", "b", "a"])\npos = bisect.bisect_left([1, 4, 8], 5)\nprint(f"Queue head: {q[0]}, Min heap item: {heapq.heappop(h)}, Bisect pos: {pos}")',
            'options': [
                'from collections import deque, Counter',
                'import heapq',
                'import bisect',
                'q = deque([10, 20])',
                'q.appendleft(5)',
                'h = [9, 3, 7]',
                'heapq.heapify(h)',
                'counts = Counter(["a", "b", "a"])',
                'pos = bisect.bisect_left([1, 4, 8], 5)',
                'print(f"Queue head: {q[0]}, Min heap item: {heapq.heappop(h)}, Bisect pos: {pos}")',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'Which Python module provides O(1) time complexity for insertions and deletions at both ends?',
                'options': ['list', 'collections.deque', 'array', 'bisect'],
                'answer': 'collections.deque',
            },
            {
                'question': 'What type of heap order does Python\'s `heapq` module implement by default?',
                'options': ['Max-Heap', 'Min-Heap', 'Fibonacci Heap', 'Binomial Heap'],
                'answer': 'Min-Heap',
            },
            {
                'question': 'Which function in `bisect` finds the leftmost insertion index for an item in a sorted list?',
                'options': ['bisect_left()', 'search_index()', 'binary_left()', 'find_spot()'],
                'answer': 'bisect_left()',
            },
            {
                'question': 'Which external Python library provides specialized Prefix Tree (Trie) data structure support?',
                'options': ['treelib', 'intervaltree', 'pygtrie', 'heapq'],
                'answer': 'pygtrie',
            },
            {
                'question': 'When should you prefer built-in Python DSA structures (like deque/dict) over custom Python classes?',
                'options': ['Never', 'Always, because built-in structures are implemented and optimized in C', 'Only on 32-bit systems', 'Only when writing GUI applications'],
                'answer': 'Always, because built-in structures are implemented and optimized in C',
            },
        ],
        'theory': {
            'definition': 'Python DSA Libraries include standard modules (array, deque, queue, collections, heapq, bisect, NumPy) and external packages (treelib, intervaltree, pygtrie) that supply optimized data structures and algorithms.',
            'why': 'Using battle-tested DSA libraries improves memory efficiency, guarantees optimal time complexity, and avoids error-prone custom implementations.',
            'rules': [
                'Use deque for double-ended queues and stack/queue operations (O(1) pops and appends).',
                'Use heapq for priority queues and min-heap operations (heappop returns the smallest element).',
                'Use collections.Counter for element frequency counts and defaultdict for missing key handling.',
                'Use bisect for maintaining sorted lists and performing log(N) binary search lookups.',
                'Use external libraries (treelib, intervaltree, pygtrie) when custom trees or prefix lookups are required.',
            ],
            'examples': [
                'from collections import deque\nq = deque([1, 2]); q.appendleft(0); q.pop()',
                'import heapq\nh = [4, 1, 7]; heapq.heapify(h); min_val = heapq.heappop(h)',
                'import bisect\nidx = bisect.bisect_left([10, 20, 30], 25)',
            ],
        },
    },
    55: {
        'concept': 'Python GUI libraries enable building visual desktop and web application interfaces. Key toolkits include Tkinter (built-in), Kivy (mobile & multitouch), Streamlit (data apps), PyQt/PySide (Qt enterprise), wxPython (native look), and PySimpleGUI (simplified wrapper).',
        'syntax': 'import tkinter as tk\nroot = tk.Tk()\nroot.title("SkillExa App")\nlabel = tk.Label(root, text="Welcome")\nlabel.pack()\nbutton = tk.Button(root, text="Click", command=root.destroy)\nbutton.pack()\n# root.mainloop()',
        'example': {
            'code': '# Simulated Python GUI toolkit comparison\ngui_libraries = {\n    "Tkinter": "Pre-installed standard GUI toolkit",\n    "Kivy": "Cross-platform mobile & desktop with multitouch",\n    "Streamlit": "Interactive web dashboards directly from Python",\n    "PyQt": "Enterprise Qt framework bindings with rich widgets",\n    "PySimpleGUI": "Boilerplate-free wrapper around Tkinter/Qt"\n}\nfor lib, desc in gui_libraries.items():\n    print(f"{lib}: {desc}")',
            'output': 'Tkinter: Pre-installed standard GUI toolkit\nKivy: Cross-platform mobile & desktop with multitouch\nStreamlit: Interactive web dashboards directly from Python\nPyQt: Enterprise Qt framework bindings with rich widgets\nPySimpleGUI: Boilerplate-free wrapper around Tkinter/Qt',
            'explanation': 'Selecting the right GUI library depends on target platforms (desktop vs web/mobile), visual customization needs, and application scale.',
        },
        'fill_blanks': {
            'question': 'Complete the Tkinter GUI layout and widget initialization snippet:',
            'answers': ['tkinter', 'Tk', 'Label', 'pack'],
            'options': ['tkinter', 'Tk', 'Label', 'pack', 'render', 'draw'],
        },
        'compiler': {
            'title': 'GUI Widget Layout Builder',
            'question': 'Arrange the lines to configure a Tkinter window with a text label and action button.',
            'starter_code': 'import tkinter as tk\nroot = tk.Tk()\nroot.title("SkillExa Portal")\nlbl = tk.Label(root, text="Learning Python GUI")\nlbl.pack()\nbtn = tk.Button(root, text="Submit")\nbtn.pack()\nprint("GUI Window configured")',
            'options': [
                'import tkinter as tk',
                'root = tk.Tk()',
                'root.title("SkillExa Portal")',
                'lbl = tk.Label(root, text="Learning Python GUI")',
                'lbl.pack()',
                'btn = tk.Button(root, text="Submit")',
                'btn.pack()',
                'print("GUI Window configured")',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'Which Python GUI library comes pre-installed with standard Python installations?',
                'options': ['PyQt5', 'Tkinter', 'Kivy', 'wxPython'],
                'answer': 'Tkinter',
            },
            {
                'question': 'Which framework is specifically designed for mobile applications (Android/iOS) with multitouch support?',
                'options': ['Kivy', 'Tkinter', 'Streamlit', 'PyGUI'],
                'answer': 'Kivy',
            },
            {
                'question': 'Which Python framework allows building interactive web-based data dashboards directly from Python code without HTML/CSS/JS?',
                'options': ['Streamlit', 'Tkinter', 'PyQt5', 'PySimpleGUI'],
                'answer': 'Streamlit',
            },
            {
                'question': 'What advantage does wxPython provide over other GUI toolkits?',
                'options': ['It only runs on Linux OS', 'It wraps native OS GUI controls for a true native system look and feel', 'It requires no Python installation', 'It compiles code into C++ source files'],
                'answer': 'It wraps native OS GUI controls for a true native system look and feel',
            },
            {
                'question': 'Why do developers use PySimpleGUI?',
                'options': ['To build 3D video game engines', 'To wrap Tkinter/Qt with a simplified syntax that reduces boilerplate code', 'To replace the Python interpreter', 'To automate database migrations'],
                'answer': 'To wrap Tkinter/Qt with a simplified syntax that reduces boilerplate code',
            },
        ],
        'theory': {
            'definition': 'Python GUI Libraries are software toolkits providing buttons, text inputs, menus, and layout containers to create interactive visual desktop and web applications.',
            'why': 'GUIs make applications user-friendly, accessible to non-programmers, and visually interactive compared to command-line interfaces.',
            'rules': [
                'Use Tkinter for quick cross-platform desktop utilities without external dependencies.',
                'Use Kivy for mobile (Android/iOS) or touch-screen application development.',
                'Use Streamlit for data science, machine learning models, and web dashboards.',
                'Use PyQt or PySide for full-featured, complex enterprise desktop applications.',
                'Use PySimpleGUI to prototype standard GUI layouts with minimal boilerplate code.',
            ],
            'examples': [
                'import tkinter as tk\nroot = tk.Tk()\ntk.Label(root, text="Hi").pack()',
                'import streamlit as st\nst.title("Data Dashboard")',
                'from PyQt5.QtWidgets import QApplication, QLabel\napp = QApplication([])',
            ],
        },
    },
    56: {
        'concept': 'NumPy (Numerical Python) is the foundation of scientific computing in Python. It provides the N-dimensional ndarray object, contiguous memory layout for high performance, vectorization to eliminate explicit loops, broadcasting for shape alignment, and routines for linear algebra, indexing, and sorting.',
        'syntax': 'import numpy as np\na = np.array([1, 2, 3])\nzeros = np.zeros((3, 3))\nones = np.ones((2, 2))\nr = np.arange(0, 10, 2)\nfiltered = a[a > 1]\nsorted_arr = np.sort(a)',
        'example': {
            'code': 'import numpy as np\n\n# 1. Array creation and indexing\na = np.array([10, 20, 30, 40, 50])\nprint(f"Index 2: {a[2]}, Last: {a[-1]}")\n\n# 2. Boolean indexing (condition filtering)\ncond = a > 25\nprint(f"Elements > 25: {a[cond]}")\n\n# 3. Vectorized arithmetic & unary operation\nx = np.array([1, 2, 3])\ny = np.array([4, 5, 6])\nprint(f"Element-wise sum: {x + y}")\nprint(f"Unary absolute: {np.absolute(np.array([-3, -1, 2]))}")',
            'output': 'Index 2: 30, Last: 50\nElements > 25: [30 40 50]\nElement-wise sum: [5 7 9]\nUnary absolute: [3 1 2]',
            'explanation': 'NumPy ndarrays store homogeneous elements in contiguous memory, enabling vectorization without slow Python loops.',
        },
        'fill_blanks': {
            'question': 'Complete the NumPy array creation and boolean filtering snippet:',
            'answers': ['numpy', 'array', 'zeros', 'arange'],
            'options': ['numpy', 'array', 'zeros', 'arange', 'matrix', 'list'],
        },
        'compiler': {
            'title': 'NumPy Vectorized Array Engine',
            'question': 'Arrange the lines to import numpy, create an ndarray, apply boolean indexing, and execute element-wise operations.',
            'starter_code': 'import numpy as np\narr = np.array([10, 20, 30, 40, 50])\nmask = arr > 25\nfiltered = arr[mask]\nsquared = np.sqrt(filtered)\nprint(f"Filtered: {filtered}")\nprint(f"Square roots: {squared}")',
            'options': [
                'import numpy as np',
                'arr = np.array([10, 20, 30, 40, 50])',
                'mask = arr > 25',
                'filtered = arr[mask]',
                'squared = np.sqrt(filtered)',
                'print(f"Filtered: {filtered}")',
                'print(f"Square roots: {squared}")',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the core N-dimensional array data structure provided by NumPy?',
                'options': ['ndarray', 'Series', 'DataFrame', 'ArrayList'],
                'answer': 'ndarray',
            },
            {
                'question': 'Why are NumPy arrays faster than standard Python lists for numerical operations?',
                'options': ['Because NumPy converts code into HTML', 'Because NumPy arrays store elements in contiguous memory locations with homogeneous types', 'Because NumPy disables garbage collection', 'Because NumPy skips memory allocation'],
                'answer': 'Because NumPy arrays store elements in contiguous memory locations with homogeneous types',
            },
            {
                'question': 'What NumPy feature allows element-wise arithmetic operations on arrays of different shapes by aligning dimensions?',
                'options': ['Broadcasting', 'Compiling', 'Archiving', 'Serializing'],
                'answer': 'Broadcasting',
            },
            {
                'question': 'Which function generates a sequence of numbers with start, stop, and step parameters in NumPy?',
                'options': ['np.range()', 'np.arange()', 'np.sequence()', 'np.step()'],
                'answer': 'np.arange()',
            },
            {
                'question': 'How does boolean indexing work in NumPy (e.g. arr[arr > 25])?',
                'options': ['It raises a TypeError', 'It returns a new array containing only elements where the condition is True', 'It converts the array elements into strings', 'It deletes elements from memory'],
                'answer': 'It returns a new array containing only elements where the condition is True',
            },
        ],
        'theory': {
            'definition': 'NumPy is the fundamental Python package for scientific computing, offering multidimensional ndarrays, vectorized functions, and mathematical routines.',
            'why': 'NumPy provides high-performance C-based array execution, essential for data science, machine learning, and numerical analysis.',
            'rules': [
                'Import numpy using standard alias np (import numpy as np).',
                'ndarrays require homogeneous data types across all elements.',
                'Use np.zeros(), np.ones(), or np.arange() for rapid array initialization.',
                'Use vectorization (arr1 + arr2) instead of explicit for loops for performance.',
                'Use boolean indexing (arr[cond]) or integer arrays for advanced selection.',
            ],
            'examples': [
                'a = np.array([1, 2, 3]); print(a * 2)',
                'a0 = np.zeros((3, 3)); ar = np.arange(0, 10, 2)',
                'cond = a > 1; print(a[cond])',
            ],
        },
    },
    57: {
        'concept': 'Pandas is an open-source data analysis and manipulation library. It provides two primary data structures: 1D Series (labeled array) and 2D DataFrame (tabular grid with row and column labels), supporting CSV reading, missing data handling, boolean filtering, and GroupBy aggregations.',
        'syntax': 'import pandas as pd\ns = pd.Series([10, 20, 30], index=["a", "b", "c"])\ndf = pd.read_csv("data.csv")\nfiltered = df[df["age"] > 25]\ndf_filled = df.fillna(0)\ngrouped = df.groupby("category")["sales"].sum()',
        'example': {
            'code': 'import pandas as pd\nimport numpy as np\n\n# 1. Series creation\ns = pd.Series([100, 200, 300], index=["Q1", "Q2", "Q3"])\nprint("Series with custom index:")\nprint(s)\n\n# 2. DataFrame filtering & GroupBy aggregation simulation\ndata = {"name": ["Alice", "Bob", "Charlie"], "dept": ["HR", "IT", "IT"], "salary": [50000, 70000, 80000]}\ndf = pd.DataFrame(data)\nprint("\nFiltered (salary > 60000):")\nprint(df[df["salary"] > 60000])\nprint("\nMean salary by dept:")\nprint(df.groupby("dept")["salary"].mean())',
            'output': 'Series with custom index:\nQ1    100\nQ2    200\nQ3    300\ndtype: int64\n\nFiltered (salary > 60000):\n      name dept  salary\n1      Bob   IT   70000\n2  Charlie   IT   80000\n\nMean salary by dept:\ndept\nHR    50000.0\nIT    75000.0\nName: salary, dtype: float64',
            'explanation': 'Pandas DataFrames provide tabular data structures with labeled columns and rows, allowing SQL/Excel-like operations in Python.',
        },
        'fill_blanks': {
            'question': 'Complete the Pandas Series, DataFrame, and GroupBy aggregation snippet:',
            'answers': ['pandas', 'Series', 'DataFrame', 'groupby'],
            'options': ['pandas', 'Series', 'DataFrame', 'groupby', 'matrix', 'table'],
        },
        'compiler': {
            'title': 'Pandas Data Wrangling Pipeline',
            'question': 'Arrange the lines to create a DataFrame, inspect summary info, filter records, and aggregate by category.',
            'starter_code': 'import pandas as pd\ndata = {"item": ["A", "B", "A"], "price": [10, 20, 15]}\ndf = pd.DataFrame(data)\nprint(df.info())\nexpensive = df[df["price"] > 12]\ntotal_by_item = df.groupby("item")["price"].sum()\nprint(total_by_item)',
            'options': [
                'import pandas as pd',
                'data = {"item": ["A", "B", "A"], "price": [10, 20, 15]}',
                'df = pd.DataFrame(data)',
                'print(df.info())',
                'expensive = df[df["price"] > 12]',
                'total_by_item = df.groupby("item")["price"].sum()',
                'print(total_by_item)',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What are the two core data structures provided by Pandas?',
                'options': ['Series (1D) and DataFrame (2D)', 'Array (1D) and Matrix (2D)', 'Vector (1D) and Tensor (3D)', 'List (1D) and Dictionary (2D)'],
                'answer': 'Series (1D) and DataFrame (2D)',
            },
            {
                'question': 'Which Pandas function reads tabular data directly from a CSV file into a DataFrame?',
                'options': ['pd.load_csv()', 'pd.read_csv()', 'pd.open_csv()', 'pd.parse_csv()'],
                'answer': 'pd.read_csv()',
            },
            {
                'question': 'Which DataFrame method displays column names, data types, non-null counts, and memory usage?',
                'options': ['df.head()', 'df.info()', 'df.describe()', 'df.shape'],
                'answer': 'df.info()',
            },
            {
                'question': 'Which method is used to fill NaN (missing) values in a DataFrame with a default value?',
                'options': ['df.fillna()', 'df.replace_null()', 'df.clean_na()', 'df.drop_null()'],
                'answer': 'df.fillna()',
            },
            {
                'question': 'Which method splits data into groups based on category columns to compute aggregate statistics?',
                'options': ['df.aggregate()', 'df.groupby()', 'df.categorize()', 'df.pivot()'],
                'answer': 'df.groupby()',
            },
        ],
        'theory': {
            'definition': 'Pandas is a data analysis and manipulation library providing Series (1D) and DataFrame (2D) structures for tabular data.',
            'why': 'Pandas simplifies real-world data ingestion, cleaning, NaN handling, indexing, filtering, and aggregation.',
            'rules': [
                'Import pandas using standard alias pd (import pandas as pd).',
                'Use Series for 1D labeled arrays and DataFrame for 2D tabular grids.',
                'Use df.read_csv() to load CSV data and df.head() / df.info() to inspect rows.',
                'Handle missing data using df.isnull().sum() and df.fillna() or df.dropna().',
                'Use boolean masking df[df["col"] > val] for row selection and df.groupby() for aggregation.',
            ],
            'examples': [
                's = pd.Series([1, 2, 3], index=["a", "b", "c"])',
                'df = pd.read_csv("file.csv"); print(df.head())',
                'res = df.groupby("dept")["sales"].sum()',
            ],
        },
    },
    58: {
        'concept': 'Matplotlib is the primary data visualization library in Python. Pyplot (matplotlib.pyplot) provides functions for plot anatomy (Figure, Axes, Axis, Title, Labels, Legend) and plot types including Line, Bar, Histogram, Scatter, Pie, Boxplot, and Heatmap (imshow).',
        'syntax': 'import matplotlib.pyplot as plt\nfig, ax = plt.subplots()\nax.plot([1, 2, 3], [4, 5, 6], marker="o")\nax.set_title("Plot Title")\nax.set_xlabel("X Label")\nax.set_ylabel("Y Label")\n# plt.show()',
        'example': {
            'code': '# Matplotlib multi-plot type demonstration\ngui_plots = {\n    "Line Chart": "plt.plot(x, y) - Relationship trends",\n    "Bar Chart": "plt.bar(cats, vals) - Categorical comparisons",\n    "Histogram": "plt.hist(data, bins=10) - Frequency distribution",\n    "Scatter Plot": "plt.scatter(x, y) - Bivariate correlation",\n    "Pie Chart": "plt.pie(vals, labels=cats) - Proportions",\n    "Boxplot": "plt.boxplot(data) - Quartiles & outliers",\n    "Heatmap": "plt.imshow(matrix, cmap=\'viridis\') - 2D intensity"\n}\nfor p_type, desc in gui_plots.items():\n    print(f"{p_type}: {desc}")',
            'output': 'Line Chart: plt.plot(x, y) - Relationship trends\nBar Chart: plt.bar(cats, vals) - Categorical comparisons\nHistogram: plt.hist(data, bins=10) - Frequency distribution\nScatter Plot: plt.scatter(x, y) - Bivariate correlation\nPie Chart: plt.pie(vals, labels=cats) - Proportions\nBoxplot: plt.boxplot(data) - Quartiles & outliers\nHeatmap: plt.imshow(matrix, cmap=\'viridis\') - 2D intensity',
            'explanation': 'Matplotlib Pyplot provides specialized plotting functions for discrete categories, continuous distributions, and 2D heatmaps.',
        },
        'fill_blanks': {
            'question': 'Complete the Matplotlib Pyplot setup and line plot snippet:',
            'answers': ['matplotlib.pyplot', 'subplots', 'plot', 'show'],
            'options': ['matplotlib.pyplot', 'subplots', 'plot', 'show', 'draw', 'render'],
        },
        'compiler': {
            'title': 'Matplotlib Plot Builder',
            'question': 'Arrange the lines to initialize a figure subplots layout, draw a line plot, set title & labels, and display the plot.',
            'starter_code': 'import matplotlib.pyplot as plt\nx = [1, 2, 3, 4]\ny = [10, 20, 25, 30]\nfig, ax = plt.subplots()\nax.plot(x, y, marker="o", label="Trend")\nax.set_title("Sample Line Chart")\nax.set_xlabel("Time")\nax.set_ylabel("Value")\nax.legend()\nprint("Plot configured successfully")',
            'options': [
                'import matplotlib.pyplot as plt',
                'x = [1, 2, 3, 4]',
                'y = [10, 20, 25, 30]',
                'fig, ax = plt.subplots()',
                'ax.plot(x, y, marker="o", label="Trend")',
                'ax.set_title("Sample Line Chart")',
                'ax.set_xlabel("Time")',
                'ax.set_ylabel("Value")',
                'ax.legend()',
                'print("Plot configured successfully")',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the top-level container that holds all plot elements in Matplotlib?',
                'options': ['Figure', 'Axes', 'Axis', 'Canvas'],
                'answer': 'Figure',
            },
            {
                'question': 'Which Matplotlib function groups continuous numerical data into discrete interval bins to display frequency distributions?',
                'options': ['plt.bar()', 'plt.hist()', 'plt.scatter()', 'plt.pie()'],
                'answer': 'plt.hist()',
            },
            {
                'question': 'Which function creates a 2D graphical representation of data matrix values rendered as colors (heatmap)?',
                'options': ['plt.imshow()', 'plt.draw_matrix()', 'plt.colorgrid()', 'plt.heatmap()'],
                'answer': 'plt.imshow()',
            },
            {
                'question': 'What parameter in `plt.pie()` displays percentage labels on each pie wedge slice?',
                'options': ['autopct', 'percentage_format', 'show_values', 'labels_percent'],
                'answer': 'autopct',
            },
            {
                'question': 'What plot type displays median, quartiles, minimum, maximum, and outliers visually?',
                'options': ['Line chart', 'Scatter plot', 'Box plot', 'Bar chart'],
                'answer': 'Box plot',
            },
        ],
        'theory': {
            'definition': 'Matplotlib is Python\'s foundational plotting library. The Pyplot module (matplotlib.pyplot) provides functions for creating figures, axes, plots, and annotations.',
            'why': 'Data visualization helps developers analyze data distributions, spot trends, detect outliers, and present findings effectively.',
            'rules': [
                'Import Pyplot using standard alias plt (import matplotlib.pyplot as plt).',
                'Understand Figure (canvas container) vs Axes (individual plot area).',
                'Use plt.plot() for lines, plt.bar() for categorical bars, plt.hist() for distribution bins.',
                'Use plt.scatter() for point correlations and plt.imshow() for 2D matrix heatmaps.',
                'Always annotate plots with titles, axis labels (set_xlabel, set_ylabel), and legends.',
            ],
            'examples': [
                'import matplotlib.pyplot as plt\nplt.plot([1,2],[3,4]); plt.title("Line")',
                'plt.bar(["A","B"], [10,20]); plt.show()',
                'plt.hist([1,2,2,3,4], bins=5); plt.show()',
            ],
        },
    },
    59: {
        'concept': 'Seaborn is a Python statistical visualization library built on Matplotlib and integrated with Pandas. It offers dataset-oriented APIs and high-level plot functions across 6 categories: Relational, Categorical, Distribution, Regression, Matrix, and Multi-plot grids.',
        'syntax': 'import seaborn as sns\nimport matplotlib.pyplot as plt\ntips = sns.load_dataset("tips")\nsns.scatterplot(x="total_bill", y="tip", hue="day", data=tips)\nsns.histplot(tips["total_bill"], kde=True)\nsns.heatmap(df.corr(), annot=True, cmap="coolwarm")\nsns.pairplot(df, hue="category")\n# plt.show()',
        'example': {
            'code': '# Seaborn plot categories demonstration\nimport seaborn as sns\nimport matplotlib.pyplot as plt\n\n# Simulated dataset & statistical plots\nprint("1. Relational: sns.scatterplot(x=\'bill\', y=\'tip\', hue=\'day\')")\nprint("2. Distribution: sns.histplot(data, kde=True)")\nprint("3. Categorical: sns.boxplot(x=\'day\', y=\'bill\')")\nprint("4. Matrix: sns.heatmap(df.corr(), annot=True)")\nprint("5. Grid: sns.pairplot(df, hue=\'species\')")',
            'output': '1. Relational: sns.scatterplot(x=\'bill\', y=\'tip\', hue=\'day\')\n2. Distribution: sns.histplot(data, kde=True)\n3. Categorical: sns.boxplot(x=\'day\', y=\'bill\')\n4. Matrix: sns.heatmap(df.corr(), annot=True)\n5. Grid: sns.pairplot(df, hue=\'species\')',
            'explanation': 'Seaborn simplifies statistical plotting by mapping DataFrame columns directly to visual attributes like hue, style, and size.',
        },
        'fill_blanks': {
            'question': 'Complete the Seaborn scatterplot and KDE distribution plot snippet:',
            'answers': ['seaborn', 'scatterplot', 'histplot', 'heatmap'],
            'options': ['seaborn', 'scatterplot', 'histplot', 'heatmap', 'render', 'draw'],
        },
        'compiler': {
            'title': 'Seaborn Statistical Plot Builder',
            'question': 'Arrange the lines to load a Seaborn dataset, plot a scatter plot with hue grouping, overlay KDE density, and render output.',
            'starter_code': 'import seaborn as sns\nimport matplotlib.pyplot as plt\ntips = sns.load_dataset("tips")\nsns.scatterplot(x="total_bill", y="tip", hue="sex", data=tips)\nsns.histplot(tips["total_bill"], kde=True)\nplt.title("Tip vs Total Bill Analysis")\nprint("Seaborn chart generated")',
            'options': [
                'import seaborn as sns',
                'import matplotlib.pyplot as plt',
                'tips = sns.load_dataset("tips")',
                'sns.scatterplot(x="total_bill", y="tip", hue="sex", data=tips)',
                'sns.histplot(tips["total_bill"], kde=True)',
                'plt.title("Tip vs Total Bill Analysis")',
                'print("Seaborn chart generated")',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'On which core Python libraries is Seaborn built?',
                'options': ['Matplotlib and Pandas', 'TensorFlow and PyTorch', 'Flask and Django', 'NumPy and SciPy only'],
                'answer': 'Matplotlib and Pandas',
            },
            {
                'question': 'Which parameter in `sns.histplot()` adds a smooth Kernel Density Estimate curve to a histogram?',
                'options': ['density=True', 'kde=True', 'curve=True', 'smooth=True'],
                'answer': 'kde=True',
            },
            {
                'question': 'Which parameter in `sns.scatterplot()` adds color-coded categorical grouping across data points?',
                'options': ['hue', 'color_by', 'group', 'shade'],
                'answer': 'hue',
            },
            {
                'question': 'Which Seaborn function generates a grid of pairwise scatterplots across all numerical columns in a DataFrame?',
                'options': ['sns.gridplot()', 'sns.pairplot()', 'sns.matrixplot()', 'sns.multiplot()'],
                'answer': 'sns.pairplot()',
            },
            {
                'question': 'Which Seaborn function visualizes 2D correlation matrices using color intensity and numeric annotations?',
                'options': ['sns.heatmap()', 'sns.corrplot()', 'sns.gridmap()', 'sns.colormatrix()'],
                'answer': 'sns.heatmap()',
            },
        ],
        'theory': {
            'definition': 'Seaborn is a Python statistical data visualization library providing high-level dataset-oriented interfaces for drawing attractive statistical graphics.',
            'why': 'Seaborn automates complex statistical aggregations, hue color mappings, and theme styling on Pandas DataFrames.',
            'rules': [
                'Import Seaborn using alias sns (import seaborn as sns).',
                'Use Relational plots (lineplot, scatterplot) for 2-variable relationships.',
                'Use Categorical plots (barplot, boxplot, violinplot) for numeric-by-category metrics.',
                'Use Distribution plots (histplot, kdeplot) with kde=True for probability density.',
                'Use Matrix plots (heatmap) with annot=True for correlation matrices.',
            ],
            'examples': [
                'sns.scatterplot(x="x", y="y", hue="group", data=df)',
                'sns.histplot(df["col"], kde=True)',
                'sns.heatmap(df.corr(), annot=True, cmap="coolwarm")',
            ],
        },
    },
    60: {
        'concept': 'Statsmodels is a Python library for statistical modeling, hypothesis testing, and econometric data analysis. It provides classes for fitting regression models (OLS, Logistic Regression, GLS), diagnostic tables (ANOVA, Jarque-Bera, Durbin-Watson), and time series models (ARIMA, SARIMA).',
        'syntax': 'import statsmodels.api as sm\nimport statsmodels.formula.api as smf\nmodel = smf.ols("y ~ x1 + x2", data=df).fit()\nprint(model.summary())\nanova_table = sm.stats.anova_lm(model)',
        'example': {
            'code': '# Statsmodels OLS linear regression workflow simulation\nimport statsmodels.api as sm\nimport statsmodels.formula.api as smf\nimport pandas as pd\n\ndata = {"y": [1, 3, 4, 5, 8], "x": [1, 2, 3, 4, 5]}\ndf = pd.DataFrame(data)\nmodel = smf.ols("y ~ x", data=df).fit()\nprint(f"R-squared: {model.rsquared:.4f}")\nprint(f"P-values:\n{model.pvalues}")',
            'output': 'R-squared: 0.9655\nP-values:\nIntercept    0.287900\nx            0.002812\ndtype: float64',
            'explanation': 'Statsmodels formula syntax ("y ~ x") provides detailed econometric outputs including R-squared, coefficients, standard errors, and p-values.',
        },
        'fill_blanks': {
            'question': 'Complete the Statsmodels OLS regression fitting and summary snippet:',
            'answers': ['statsmodels.api', 'statsmodels.formula.api', 'ols', 'fit'],
            'options': ['statsmodels.api', 'statsmodels.formula.api', 'ols', 'fit', 'predict', 'train'],
        },
        'compiler': {
            'title': 'Statsmodels OLS Regression Pipeline',
            'question': 'Arrange the lines to import statsmodels, define a formula OLS model, fit the dataset, and output summary statistics.',
            'starter_code': 'import statsmodels.formula.api as smf\nimport pandas as pd\ndf = pd.DataFrame({"sales": [10, 15, 25, 30], "ad_spend": [1, 2, 4, 5]})\nmodel = smf.ols("sales ~ ad_spend", data=df).fit()\nprint(f"R2: {model.rsquared}")\nprint(f"Params:\\n{model.params}")',
            'options': [
                'import statsmodels.formula.api as smf',
                'import pandas as pd',
                'df = pd.DataFrame({"sales": [10, 15, 25, 30], "ad_spend": [1, 2, 4, 5]})',
                'model = smf.ols("sales ~ ad_spend", data=df).fit()',
                'print(f"R2: {model.rsquared}")',
                'print(f"Params:\\n{model.params}")',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the primary focus of the Statsmodels library in Python?',
                'options': ['Web scraping and HTML parsing', 'Statistical modeling, hypothesis testing, and econometric analysis', '3D graphic rendering', 'Building desktop GUI windows'],
                'answer': 'Statistical modeling, hypothesis testing, and econometric analysis',
            },
            {
                'question': 'Which method returns a comprehensive statistical report containing R-squared, t-statistics, and p-values for a fitted Statsmodels model?',
                'options': ['model.report()', 'model.summary()', 'model.info()', 'model.describe()'],
                'answer': 'model.summary()',
            },
            {
                'question': 'What does `smf.ols("y ~ x", data=df)` stand for in Statsmodels?',
                'options': ['Ordinary Least Squares linear regression using R-style formula syntax', 'Online Storage Optimization', 'Object Logical Search', 'Operator Line Sequence'],
                'answer': 'Ordinary Least Squares linear regression using R-style formula syntax',
            },
            {
                'question': 'Which diagnostic test in Statsmodels checks for autocorrelation in regression residuals?',
                'options': ['Durbin-Watson Test', 'ANOVA Test', 'K-Means Test', 'Confusion Matrix'],
                'answer': 'Durbin-Watson Test',
            },
            {
                'question': 'Which model class in Statsmodels is used for Time Series forecasting with seasonal patterns?',
                'options': ['SARIMA', 'KNeighborsClassifier', 'DecisionTreeRegressor', 'LinearDiscriminantAnalysis'],
                'answer': 'SARIMA',
            },
        ],
        'theory': {
            'definition': 'Statsmodels is a Python package providing classes and functions for estimating statistical models, hypothesis testing, and exploring data.',
            'why': 'Unlike pure ML libraries focused only on predictions, Statsmodels focuses on statistical inference, p-values, confidence intervals, and hypothesis validity.',
            'rules': [
                'Import statsmodels API using sm or smf (import statsmodels.formula.api as smf).',
                'Use R-style formula string "dependent ~ independent1 + independent2".',
                'Call .fit() on the model instance to estimate parameters.',
                'Use model.summary() to view comprehensive statistical diagnostic outputs.',
                'Use sm.stats.anova_lm() for Analysis of Variance tables.',
            ],
            'examples': [
                'model = smf.ols("y ~ x1 + x2", data=df).fit()',
                'print(model.summary())',
                'print(model.params, model.pvalues)',
            ],
        },
    },
    61: {
        'concept': 'Scikit-learn is the standard Python machine learning library for classification, regression, clustering, and preprocessing. It features a consistent estimator interface (.fit(), .predict(), .transform()), dataset loaders, train-test splitting, and evaluation metrics.',
        'syntax': 'from sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score\nfrom sklearn.preprocessing import OneHotEncoder, LabelEncoder\n\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)\nmodel = LogisticRegression(max_iter=200)\nmodel.fit(X_train, y_train)\npreds = model.predict(X_test)\nacc = accuracy_score(y_test, preds)',
        'example': {
            'code': '# Scikit-learn Machine Learning pipeline simulation\nfrom sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score\n\niris = load_iris()\nX, y = iris.data, iris.target\nX_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.4, random_state=1)\n\nmodel = LogisticRegression(max_iter=200)\nmodel.fit(X_tr, y_tr)\npreds = model.predict(X_te)\nacc = accuracy_score(y_te, preds)\n\nprint(f"Training shape: {X_tr.shape}")\nprint(f"Test accuracy: {acc:.4f}")',
            'output': 'Training shape: (90, 4)\nTest accuracy: 0.9667',
            'explanation': 'Scikit-learn unifies ML model building: data splitting (train_test_split), fitting parameters (model.fit), predicting test labels (model.predict), and evaluating metrics.',
        },
        'fill_blanks': {
            'question': 'Complete the Scikit-learn model fitting and evaluation snippet:',
            'answers': ['sklearn', 'train_test_split', 'LabelEncoder', 'accuracy_score'],
            'options': ['sklearn', 'train_test_split', 'LabelEncoder', 'accuracy_score', 'model_fit', 'tensor'],
        },
        'compiler': {
            'title': 'Scikit-learn Model Training Pipeline',
            'question': 'Arrange the lines to load sample data, split train/test sets, fit a Logistic Regression classifier, and calculate test accuracy.',
            'starter_code': 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn import metrics\niris = load_iris()\nX_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)\nclf = LogisticRegression(max_iter=200)\nclf.fit(X_tr, y_tr)\nacc = metrics.accuracy_score(y_te, clf.predict(X_te))\nprint(f"Accuracy: {acc:.2f}")',
            'options': [
                'from sklearn.datasets import load_iris',
                'from sklearn.model_selection import train_test_split',
                'from sklearn.linear_model import LogisticRegression',
                'from sklearn import metrics',
                'iris = load_iris()',
                'X_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)',
                'clf = LogisticRegression(max_iter=200)',
                'clf.fit(X_tr, y_tr)',
                'acc = metrics.accuracy_score(y_te, clf.predict(X_te))',
                'print(f"Accuracy: {acc:.2f}")',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'Which Scikit-learn function splits a dataset into separate training and testing subsets?',
                'options': ['train_test_split()', 'split_dataset()', 'divide_data()', 'partition_matrix()'],
                'answer': 'train_test_split()',
            },
            {
                'question': 'Which method adjusts model parameters based on input features (X) and target labels (y)?',
                'options': ['fit()', 'predict()', 'transform()', 'evaluate()'],
                'answer': 'fit()',
            },
            {
                'question': 'Which encoder creates separate binary columns for each unique categorical value?',
                'options': ['OneHotEncoder', 'LabelEncoder', 'StandardScaler', 'PCA'],
                'answer': 'OneHotEncoder',
            },
            {
                'question': 'What function measures the ratio of correct predictions to total predictions in classification?',
                'options': ['accuracy_score()', 'mean_squared_error()', 'confusion_matrix()', 'r2_score()'],
                'answer': 'accuracy_score()',
            },
            {
                'question': 'Why is setting `random_state` recommended when splitting data or training models?',
                'options': ['To speed up computation', 'To ensure reproducible results across multiple runs', 'To automatically fix missing values', 'To prevent GPU memory leakage'],
                'answer': 'To ensure reproducible results across multiple runs',
            },
        ],
        'theory': {
            'definition': 'Scikit-learn is an open-source Machine Learning library for Python built on NumPy, SciPy, and Matplotlib.',
            'why': 'Provides a clean, uniform interface for classification, regression, clustering, dimensionality reduction, and preprocessing.',
            'rules': [
                'Split dataset into training (e.g. 70-80%) and testing (e.g. 20-30%) using train_test_split.',
                'Use LabelEncoder for ordered categories and OneHotEncoder for un-ordered categories.',
                'Call model.fit(X_train, y_train) to train estimator parameters.',
                'Call model.predict(X_test) to generate predictions on unseen test data.',
                'Evaluate performance using metrics (accuracy_score, classification_report, confusion_matrix).',
            ],
            'examples': [
                'from sklearn.model_selection import train_test_split',
                'X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3)',
                'model.fit(X_tr, y_tr); acc = accuracy_score(y_te, model.predict(X_te))',
            ],
        },
    },
    62: {
        'concept': 'XGBoost and LightGBM are high-performance gradient boosting frameworks. XGBoost uses level-wise tree growth, regularization penalties, and sparsity-aware splitting. LightGBM uses leaf-wise tree growth, histogram-based binning, GOSS sampling, and EFB feature bundling for speed.',
        'syntax': '# XGBoost Classifier\nfrom xgboost import XGBClassifier\nmodel_xgb = XGBClassifier(max_depth=4, learning_rate=0.1, n_estimators=100)\nmodel_xgb.fit(X_train, y_train)\n\n# LightGBM Classifier\nimport lightgbm as lgb\ntrain_data = lgb.Dataset(X_train, label=y_train)\nmodel_lgb = lgb.train(params, train_data, num_boost_round=100)',
        'example': {
            'code': '# Gradient Boosting frameworks simulation: XGBoost vs LightGBM\nprint("1. XGBoost: Level-wise tree growth, L1/L2 regularization, feature importance")\nprint("2. LightGBM: Leaf-wise tree growth (best-first), Histogram binning, GOSS & EFB")\n\n# Hyperparameter configuration\nxgb_params = {"objective": "binary:logistic", "max_depth": 4, "n_estimators": 100}\nlgb_params = {"objective": "binary", "num_leaves": 31, "learning_rate": 0.05}\nprint(f"XGBoost config: {xgb_params}")\nprint(f"LightGBM config: {lgb_params}")',
            'output': '1. XGBoost: Level-wise tree growth, L1/L2 regularization, feature importance\n2. LightGBM: Leaf-wise tree growth (best-first), Histogram binning, GOSS & EFB\nXGBoost config: {\'objective\': \'binary:logistic\', \'max_depth\': 4, \'n_estimators\': 100}\nLightGBM config: {\'objective\': \'binary\', \'num_leaves\': 31, \'learning_rate\': 0.05}',
            'explanation': 'Both frameworks build sequential boosting decision trees, with LightGBM optimizing speed via leaf-wise splitting and histogram binning.',
        },
        'fill_blanks': {
            'question': 'Complete the XGBoost and LightGBM classifier setup snippet:',
            'answers': ['xgboost', 'XGBClassifier', 'lightgbm', 'Dataset'],
            'options': ['xgboost', 'XGBClassifier', 'lightgbm', 'Dataset', 'RandomForest', 'GridSearch'],
        },
        'compiler': {
            'title': 'Gradient Boosting Ensemble Engine',
            'question': 'Arrange the lines to set up an XGBClassifier with hyperparameters, train on dataset, and evaluate accuracy.',
            'starter_code': 'from xgboost import XGBClassifier\nfrom sklearn.metrics import accuracy_score\nmodel = XGBClassifier(max_depth=3, learning_rate=0.1, n_estimators=50)\nmodel.fit(X_train, y_train)\npreds = model.predict(X_test)\nprint(f"XGBoost Accuracy: {accuracy_score(y_test, preds):.2f}")',
            'options': [
                'from xgboost import XGBClassifier',
                'from sklearn.metrics import accuracy_score',
                'model = XGBClassifier(max_depth=3, learning_rate=0.1, n_estimators=50)',
                'model.fit(X_train, y_train)',
                'preds = model.predict(X_test)',
                'print(f"XGBoost Accuracy: {accuracy_score(y_test, preds):.2f}")',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What strategy does LightGBM use for growing decision trees compared to traditional level-wise boosting?',
                'options': ['Leaf-wise (best-first) growth', 'Random depth growth', 'Symmetric breadth growth', 'Linear regression growth'],
                'answer': 'Leaf-wise (best-first) growth',
            },
            {
                'question': 'What optimization in LightGBM bundles sparse, mutually exclusive features to reduce dimensionality?',
                'options': ['Exclusive Feature Bundling (EFB)', 'Gradient One-Side Sampling (GOSS)', 'L1 Regularization', 'Histogram Binning'],
                'answer': 'Exclusive Feature Bundling (EFB)',
            },
            {
                'question': 'How does XGBoost prevent overfitting compared to traditional decision trees?',
                'options': ['By adding L1/L2 regularization terms and learning rate (eta) parameters to objective functions', 'By converting data to text strings', 'By disabling depth evaluation', 'By turning off loss calculation'],
                'answer': 'By adding L1/L2 regularization terms and learning rate (eta) parameters to objective functions',
            },
            {
                'question': 'Which function in `xgboost` visualizes the relative importance of each feature in the trained model?',
                'options': ['xgb.plot_importance()', 'xgb.show_weights()', 'xgb.feature_rank()', 'xgb.tree_view()'],
                'answer': 'xgb.plot_importance()',
            },
            {
                'question': 'Which parameter technique stops boosting iterations when validation loss stops improving for N consecutive rounds?',
                'options': ['Early Stopping', 'Grid Search', 'Zero Padding', 'Softmax Thresholding'],
                'answer': 'Early Stopping',
            },
        ],
        'theory': {
            'definition': 'XGBoost and LightGBM are optimized gradient boosting decision tree libraries designed for speed, efficiency, and state-of-the-art predictive performance on tabular data.',
            'why': 'Gradient boosting sequentially builds trees where each new tree corrects the residual errors of prior trees, outperforming simple decision trees.',
            'rules': [
                'XGBoost grows trees level-wise; LightGBM grows trees leaf-wise (best-first).',
                'Use early stopping (callbacks/early_stopping) to halt training when validation scores plateau.',
                'Tune learning_rate (eta), max_depth, and n_estimators to balance accuracy vs overfitting.',
                'Use lgb.Dataset format in LightGBM for memory efficiency.',
                'Analyze feature importance (xgb.plot_importance / lgb.plot_importance) for interpretability.',
            ],
            'examples': [
                'clf = XGBClassifier(n_estimators=100, learning_rate=0.1); clf.fit(X_tr, y_tr)',
                'train_data = lgb.Dataset(X_tr, label=y_tr)',
                'model = lgb.train(params, train_data, num_boost_round=100)',
            ],
        },
    },
    63: {
        'concept': 'TensorFlow is Google Brain\'s open-source deep learning platform featuring computational graphs, eager execution, autograd, and Keras integration (tf.keras). Supports Sequential and Functional APIs, model compilation, training, and TFLite edge deployment.',
        'syntax': 'import tensorflow as tf\nfrom tensorflow.keras.models import Sequential\nfrom tensorflow.keras.layers import Dense\n\nmodel = Sequential([\n    Dense(128, activation="relu", input_shape=(784,)),\n    Dense(10, activation="softmax")\n])\nmodel.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])\nmodel.fit(X_train, y_train, epochs=5)',
        'example': {
            'code': '# TensorFlow / Keras Sequential neural network simulation\nimport tensorflow as tf\nfrom tensorflow.keras.models import Sequential\nfrom tensorflow.keras.layers import Dense\n\nprint(f"TensorFlow Version: {tf.__version__}")\n\n# Construct simple 2-layer classifier\nmodel = Sequential([\n    Dense(64, activation="relu", input_shape=(100,)),\n    Dense(10, activation="softmax")\n])\nmodel.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])\nprint(f"Model Layers: {len(model.layers)}")\nprint("Neural Network successfully constructed")',
            'output': 'TensorFlow Version: 2.18.0\nModel Layers: 2\nNeural Network successfully constructed',
            'explanation': 'Keras provides a high-level API inside TensorFlow, stacking Dense layers with ReLU and Softmax activations for deep learning.',
        },
        'fill_blanks': {
            'question': 'Complete the TensorFlow Keras Sequential model construction snippet:',
            'answers': ['tensorflow', 'Sequential', 'Dense', 'compile'],
            'options': ['tensorflow', 'Sequential', 'Dense', 'compile', 'fit_transform', 'tensor'],
        },
        'compiler': {
            'title': 'TensorFlow / Keras Neural Network Builder',
            'question': 'Arrange the lines to import TensorFlow Keras modules, construct a Sequential model, compile with Adam, and run training epochs.',
            'starter_code': 'import tensorflow as tf\nfrom tensorflow.keras.models import Sequential\nfrom tensorflow.keras.layers import Dense\nmodel = Sequential([\n    Dense(128, activation="relu", input_shape=(784,)),\n    Dense(10, activation="softmax")\n])\nmodel.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])\nprint("Compiled Keras Model")',
            'options': [
                'import tensorflow as tf',
                'from tensorflow.keras.models import Sequential',
                'from tensorflow.keras.layers import Dense',
                'model = Sequential([',
                '    Dense(128, activation="relu", input_shape=(784,)),',
                '    Dense(10, activation="softmax")',
                '])',
                'model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])',
                'print("Compiled Keras Model")',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the official high-level API integrated into TensorFlow for building neural networks?',
                'options': ['Keras', 'PyTorch', 'Scikit-learn', 'Statsmodels'],
                'answer': 'Keras',
            },
            {
                'question': 'Which Keras model building API is designed for simple linear stacks of single-input, single-output layers?',
                'options': ['Sequential API', 'Functional API', 'Subclassing API', 'Graph API'],
                'answer': 'Sequential API',
            },
            {
                'question': 'Which layer activation function is standard for hidden layers to introduce non-linearity?',
                'options': ['ReLU', 'Linear', 'Step', 'Identity'],
                'answer': 'ReLU',
            },
            {
                'question': 'Which tool converts trained TensorFlow models into lightweight `.tflite` binaries for mobile and edge device deployment?',
                'options': ['TensorFlow Lite Converter', 'TensorFlow Serving', 'Keras Exporter', 'Autograd Engine'],
                'answer': 'TensorFlow Lite Converter',
            },
            {
                'question': 'Which method configures the optimizer, loss function, and metrics before model training?',
                'options': ['model.compile()', 'model.fit()', 'model.evaluate()', 'model.save()'],
                'answer': 'model.compile()',
            },
        ],
        'theory': {
            'definition': 'TensorFlow is Google\'s open-source framework for deep learning, offering Keras as its official high-level model building interface.',
            'why': 'TensorFlow supports end-to-end ML workflows from multi-GPU cloud training to lightweight edge inference via TensorFlow Lite.',
            'rules': [
                'Use Sequential API for simple single-input linear stacked layers.',
                'Use Functional API for complex architectures (multiple inputs/outputs, skip connections).',
                'Use ReLU activation in hidden layers and Softmax for multi-class output probabilities.',
                'Compile models using model.compile(optimizer, loss, metrics).',
                'Convert trained models to TFLite for resource-constrained mobile and embedded deployment.',
            ],
            'examples': [
                'model = Sequential([Dense(64, activation="relu", input_shape=(10,)), Dense(1)])',
                'model.compile(optimizer="adam", loss="mse")',
                'model.fit(X_tr, y_tr, epochs=10)',
            ],
        },
    },
    64: {
        'concept': 'PyTorch is Meta\'s Pythonic deep learning library featuring dynamic computation graphs (define-by-run), CUDA GPU acceleration, autograd automatic differentiation, custom nn.Module classes, loss functions (nn.BCELoss), optimizers (optim.Adam), and custom training loops.',
        'syntax': 'import torch\nimport torch.nn as nn\nimport torch.optim as optim\n\nclass Net(nn.Module):\n    def __init__(self):\n        super().__init__()\n        self.fc1 = nn.Linear(10, 16)\n        self.fc2 = nn.Linear(16, 1)\n    def forward(self, x):\n        x = torch.relu(self.fc1(x))\n        return torch.sigmoid(self.fc2(x))\n\nmodel = Net()\ncriterion = nn.BCELoss()\noptimizer = optim.Adam(model.parameters(), lr=0.01)\n\n# Training Loop\noptimizer.zero_grad()\noutputs = model(inputs)\nloss = criterion(outputs, targets)\nloss.backward()\noptimizer.step()',
        'example': {
            'code': '# PyTorch neural network module and dynamic autograd demonstration\nimport torch\nimport torch.nn as nn\n\n# 1. Tensor creation\nx = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)\ny = x ** 2\nsum_y = y.sum()\nsum_y.backward()\nprint(f"Gradient dy/dx: {x.grad}")\n\n# 2. Neural Network module definition\nclass SimpleNet(nn.Module):\n    def __init__(self):\n        super().__init__()\n        self.fc = nn.Linear(5, 1)\n    def forward(self, x):\n        return self.fc(x)\n\nnet = SimpleNet()\nprint(f"Model parameters count: {len(list(net.parameters()))}")',
            'output': 'Gradient dy/dx: tensor([2., 4., 6.])\nModel parameters count: 2',
            'explanation': 'PyTorch uses dynamic computational graphs where autograd automatically calculates gradients during backpropagation via loss.backward().',
        },
        'fill_blanks': {
            'question': 'Complete the PyTorch neural network module and backpropagation loop snippet:',
            'answers': ['torch', 'nn.Module', 'Linear', 'backward'],
            'options': ['torch', 'nn.Module', 'Linear', 'backward', 'fit', 'tensor_flow'],
        },
        'compiler': {
            'title': 'PyTorch Training Loop Engine',
            'question': 'Arrange the lines to define a PyTorch nn.Module class, instantiate Adam optimizer, clear gradients, execute forward pass, backpropagate, and step weights.',
            'starter_code': 'import torch\nimport torch.nn as nn\nclass PyTorchModel(nn.Module):\n    def __init__(self):\n        super().__init__()\n        self.fc = nn.Linear(10, 1)\n    def forward(self, x):\n        return torch.sigmoid(self.fc(x))\nmodel = PyTorchModel()\nopt = torch.optim.Adam(model.parameters(), lr=0.01)\nopt.zero_grad()\nout = model(torch.randn((10, 10)))\nprint("PyTorch model step complete")',
            'options': [
                'import torch',
                'import torch.nn as nn',
                'class PyTorchModel(nn.Module):',
                '    def __init__(self):',
                '        super().__init__()',
                '        self.fc = nn.Linear(10, 1)',
                '    def forward(self, x):',
                '        return torch.sigmoid(self.fc(x))',
                'model = PyTorchModel()',
                'opt = torch.optim.Adam(model.parameters(), lr=0.01)',
                'opt.zero_grad()',
                'out = model(torch.randn((10, 10)))',
                'print("PyTorch model step complete")',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What type of computational graph architecture does PyTorch use during execution?',
                'options': ['Dynamic computation graphs (define-by-run)', 'Static graphs (define-before-run)', 'Fixed binary graphs', 'HTML DOM graphs'],
                'answer': 'Dynamic computation graphs (define-by-run)',
            },
            {
                'question': 'Which base class must custom PyTorch neural network models inherit from?',
                'options': ['torch.nn.Module', 'torch.Tensor', 'torch.optim.Optimizer', 'torch.autograd.Function'],
                'answer': 'torch.nn.Module',
            },
            {
                'question': 'Which method in PyTorch calculates gradients of output tensors with respect to model parameters via backpropagation?',
                'options': ['loss.backward()', 'loss.gradient()', 'loss.step()', 'loss.zero_grad()'],
                'answer': 'loss.backward()',
            },
            {
                'question': 'Why must `optimizer.zero_grad()` be called at the start of each PyTorch training loop iteration?',
                'options': ['To clear accumulated gradients from previous iterations', 'To reset random seed weights', 'To unload GPU memory tensors', 'To compile C++ binaries'],
                'answer': 'To clear accumulated gradients from previous iterations',
            },
            {
                'question': 'Which method in PyTorch updates model weights using calculated gradients?',
                'options': ['optimizer.step()', 'optimizer.backward()', 'optimizer.update()', 'optimizer.apply()'],
                'answer': 'optimizer.step()',
            },
        ],
        'theory': {
            'definition': 'PyTorch is an open-source deep learning framework providing dynamic computational graphs, automatic differentiation (autograd), and GPU acceleration.',
            'why': 'PyTorch\'s Pythonic syntax and dynamic graph building make research prototyping, debugging, and custom architecture creation intuitive.',
            'rules': [
                'Define custom models by inheriting from torch.nn.Module.',
                'Define layer instances in __init__ and data flow logic in forward(x).',
                'Call optimizer.zero_grad() before each training step to reset gradients.',
                'Execute loss.backward() for autograd gradient computation.',
                'Call optimizer.step() to update model weight parameters.',
            ],
            'examples': [
                'x = torch.tensor([2.0], requires_grad=True); y = x**2; y.backward()',
                'class Net(nn.Module): def __init__(self): super().__init__(); self.l = nn.Linear(5,1)',
                'opt.zero_grad(); loss.backward(); opt.step()',
            ],
        },
    },
    65: {
        'concept': 'Complete Tutorial on Data Science brings together the entire Python Data Science pipeline: Data Loading (CSV, Excel, JSON, SQL, MongoDB, Web Scraping), Data Preprocessing (missing values, scaling, Label/One-Hot encoding, outliers), Data Analysis & EDA (hypothesis tests, correlation), Visualization (Matplotlib, Seaborn, Plotly), and Machine Learning modeling.',
        'syntax': '# Comprehensive Data Science Pipeline Syntax\nimport pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import classification_report, accuracy_score\n\n# 1. Load data\ndf = pd.read_csv("dataset.csv")\n# 2. Preprocess & Clean\ndf = df.fillna(df.median(numeric_only=True))\n# 3. Split & Train\nX_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25)\nclf = RandomForestClassifier().fit(X_tr, y_tr)\n# 4. Evaluate\nprint(classification_report(y_te, clf.predict(X_te)))',
        'example': {
            'code': '# Complete Python Data Science Lifecycle simulation\nimport pandas as pd\nimport numpy as np\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import accuracy_score\n\n# Step 1: Load raw data into DataFrame\ndata = {\n    "feature1": [1.2, 2.3, 3.1, 4.5, 5.0, 6.2, 7.1, 8.4],\n    "feature2": [10, 20, 15, 25, 30, 42, 35, 50],\n    "target": [0, 0, 0, 0, 1, 1, 1, 1]\n}\ndf = pd.DataFrame(data)\n\n# Step 2: Preprocess & Feature Selection\nX = df[["feature1", "feature2"]]\ny = df["target"]\n\n# Step 3: Train-Test Split\nX_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)\n\n# Step 4: Model Training\nmodel = RandomForestClassifier(random_state=42)\nmodel.fit(X_tr, y_tr)\n\n# Step 5: Model Evaluation\nacc = accuracy_score(y_te, model.predict(X_te))\nprint("Data Science Pipeline Execution Successful!")\nprint(f"Dataset Rows: {len(df)}")\nprint(f"Model Accuracy: {acc * 100:.1f}%")',
            'output': 'Data Science Pipeline Execution Successful!\nDataset Rows: 8\nModel Accuracy: 100.0%',
            'explanation': 'The complete Data Science workflow combines data ingestion, cleaning, exploratory visualization, machine learning model fitting, and evaluation metrics.',
        },
        'fill_blanks': {
            'question': 'Complete the full Data Science pipeline loading, cleaning, splitting, and reporting snippet:',
            'answers': ['read_csv', 'fillna', 'train_test_split', 'classification_report'],
            'options': ['read_csv', 'fillna', 'train_test_split', 'classification_report', 'parse', 'plot'],
        },
        'compiler': {
            'title': 'End-to-End Data Science Pipeline Builder',
            'question': 'Arrange the lines to load a dataset, fill missing values, split training/testing sets, fit a classifier, and print the evaluation classification report.',
            'starter_code': 'import pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import classification_report\ndf = pd.DataFrame({"x1": [1, 2, 3, 4], "x2": [5, 6, 7, 8], "y": [0, 0, 1, 1]})\nX_tr, X_te, y_tr, y_te = train_test_split(df[["x1", "x2"]], df["y"], test_size=0.5, random_state=1)\nclf = RandomForestClassifier(random_state=1)\nclf.fit(X_tr, y_tr)\nprint(classification_report(y_te, clf.predict(X_te)))',
            'options': [
                'import pandas as pd',
                'from sklearn.model_selection import train_test_split',
                'from sklearn.ensemble import RandomForestClassifier',
                'from sklearn.metrics import classification_report',
                'df = pd.DataFrame({"x1": [1, 2, 3, 4], "x2": [5, 6, 7, 8], "y": [0, 0, 1, 1]})',
                'X_tr, X_te, y_tr, y_te = train_test_split(df[["x1", "x2"]], df["y"], test_size=0.5, random_state=1)',
                'clf = RandomForestClassifier(random_state=1)',
                'clf.fit(X_tr, y_tr)',
                'print(classification_report(y_te, clf.predict(X_te)))',
            ],
        },
        'skill_exa_test': [
            {
                'question': 'What is the correct sequential order of steps in a standard Data Science project lifecycle?',
                'options': ['Data Loading -> Data Preprocessing -> Exploratory Analysis -> Model Training -> Model Evaluation', 'Model Evaluation -> Data Loading -> Model Training -> Preprocessing', 'Model Training -> Data Preprocessing -> Data Loading -> Deployment', 'Exploratory Analysis -> Model Evaluation -> Data Loading -> Deployment'],
                'answer': 'Data Loading -> Data Preprocessing -> Exploratory Analysis -> Model Training -> Model Evaluation',
            },
            {
                'question': 'Which preprocessing technique normalizes features by removing the mean and scaling to unit variance?',
                'options': ['StandardScaler', 'LabelEncoder', 'OneHotEncoder', 'SimpleImputer'],
                'answer': 'StandardScaler',
            },
            {
                'question': 'Which statistical test is used to compare the means of three or more independent groups?',
                'options': ['ANOVA (Analysis of Variance)', 'T-Test', 'Z-Test', 'Chi-Square Test'],
                'answer': 'ANOVA (Analysis of Variance)',
            },
            {
                'question': 'Which metric evaluation function provides precision, recall, F1-score, and support for each class?',
                'options': ['classification_report()', 'accuracy_score()', 'r2_score()', 'mean_squared_error()'],
                'answer': 'classification_report()',
            },
            {
                'question': 'What method is used to detect outliers based on the distance from the median using 25th and 75th percentiles?',
                'options': ['Interquartile Range (IQR)', 'MinMax Scaling', 'Label Encoding', 'Cross Validation'],
                'answer': 'Interquartile Range (IQR)',
            },
        ],
        'theory': {
            'definition': 'Data Science with Python encompasses extracting actionable insights from data using numerical computing (NumPy), tabular manipulation (Pandas), statistical visualization (Matplotlib/Seaborn/Plotly), hypothesis testing (Statsmodels), and predictive modeling (Scikit-learn/XGBoost/TensorFlow/PyTorch).',
            'why': 'A unified Data Science pipeline ensures data quality, eliminates bias, surfaces statistical insights, and delivers reproducible ML models.',
            'rules': [
                'Phase 1 (Data Ingestion): Import data from CSV, SQL, JSON, Excel, MongoDB, or Web Scraping.',
                'Phase 2 (Preprocessing): Clean missing values, remove duplicates, detect outliers (IQR/Z-score), and encode categories.',
                'Phase 3 (EDA & Hypothesis Testing): Analyze distributions, compute correlations, and perform t-tests or ANOVA.',
                'Phase 4 (Modeling): Train classification or regression models using Scikit-learn, XGBoost, TensorFlow, or PyTorch.',
                'Phase 5 (Evaluation): Measure performance using classification reports, confusion matrices, and ROC-AUC curves.',
            ],
            'examples': [
                'df = pd.read_csv("data.csv"); df.fillna(0, inplace=True)',
                'X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2)',
                'clf.fit(X_tr, y_tr); print(classification_report(y_te, clf.predict(X_te)))',
            ],
        },
    },
}

def _build_programming_exercise(topic_id: int, title: str, example: dict, fill_data: dict, compiler_raw: dict) -> dict:
    starter_code = compiler_raw.get("starter_code")
    options = compiler_raw.get("options")
    if starter_code and options:
        return {
            "title": compiler_raw.get("title", f"Practice {title}"),
            "question": compiler_raw.get("question", "Click an option below to fill in the blanks in the example code, then click Run Code."),
            "starter_code": starter_code,
            "options": options,
        }
    return {
        "title": f"Practice {title}",
        "question": "Click an option below to fill in the blanks in the example code, then click Run Code.",
        "starter_code": f"# Complete code for {title}\n_____('{title} Sandbox')",
        "options": ["print", "input", "str", "len"],
    }

def _build_topic(topic_meta: dict[str, object]) -> dict[str, object]:
    topic_id = int(topic_meta["id"])
    title = str(topic_meta["title"])
    category = str(topic_meta.get("category", "General Python"))
    difficulty = str(topic_meta.get("difficulty", "Beginner"))
    duration = str(topic_meta.get("duration", "30 min"))

    core = TOPIC_CORE.get(topic_id, {})

    concept = str(core.get("concept") or f"{title} is an essential concept in Python development, providing foundational logic and execution rules.")
    syntax = str(core.get("syntax") or f"# {title} Syntax Specification\n# Example structure for {title}")

    example = core.get("example")
    if not isinstance(example, dict):
        example = {
            "code": f"# {title} Demonstration Code\nprint('Mastering {title} in Python')",
            "output": f"Mastering {title} in Python",
            "explanation": f"This code example demonstrates the usage and principles of {title} in Python.",
        }

    fill_blanks = core.get("fill_blanks")
    if not isinstance(fill_blanks, dict):
        fill_blanks = {
            "question": f"# Complete the code for {title}\n_____('{title} in Python')\n",
            "answers": ["print"],
            "options": ["print", "input", "str", "len"],
        }

    compiler_raw = core.get("compiler")
    if not isinstance(compiler_raw, dict):
        compiler_raw = {
            "title": f"Practice {title}",
            "question": f"Complete the code to execute {title}.",
            "starter_code": f"_____('Python: {title}')",
            "options": ["print", "input", "sys", "os"],
        }

    compiler = _build_programming_exercise(topic_id, title, example, fill_blanks, compiler_raw)

    skill_exa_test = core.get("skill_exa_test")
    if not isinstance(skill_exa_test, list) or len(skill_exa_test) < 5:
        skill_exa_test = [
            {
                "question": f"Which category does '{title}' belong to in the Python curriculum?",
                "options": [category, "Python Fundamentals", "Data Science", "Databases"],
                "answer": category,
            },
            {
                "question": f"What is the primary usage of {title} in Python?",
                "options": [
                    f"To implement {title.lower()} logic effectively in Python applications",
                    "To format HTML documents",
                    "To compile C binaries directly",
                    "To configure network IP addresses"
                ],
                "answer": f"To implement {title.lower()} logic effectively in Python applications",
            },
            {
                "question": f"Which module category covers {title} in SkillExa?",
                "options": [category, "GUI Libraries", "File Handling", "OOP Concepts"],
                "answer": category,
            },
            {
                "question": f"Which statement is TRUE regarding {title} in Python?",
                "options": [
                    f"{title} is part of the standard Python learning path",
                    f"{title} is deprecated in Python 3",
                    f"{title} cannot be used with functions",
                    f"{title} is available only on Linux OS"
                ],
                "answer": f"{title} is part of the standard Python learning path",
            },
            {
                "question": f"What is a best practice when working with {title} in Python?",
                "options": [
                    "Follow PEP 8 style guidelines and keep code readable and well-tested",
                    "Avoid writing unit tests",
                    "Never use comments or docstrings",
                    "Use hardcoded magic numbers"
                ],
                "answer": "Follow PEP 8 style guidelines and keep code readable and well-tested",
            },
        ]

    theory = core.get("theory")
    if not isinstance(theory, dict):
        theory = {
            "definition": concept,
            "why": f"{title} builds essential skills for professional Python programming.",
            "rules": [
                "Follow PEP 8 naming conventions and clean indentation.",
                "Verify variable types and return values.",
                "Handle edge cases and potential runtime exceptions."
            ],
            "examples": [example.get("code", "")],
        }

    return {
        "id": topic_id,
        "title": title,
        "difficulty": difficulty,
        "duration": duration,
        "category": category,
        "concept": concept,
        "syntax": syntax,
        "example": example,
        "output": example.get("output", ""),
        "theory": theory,
        "fill_blanks": fill_blanks,
        "compiler": compiler,
        "skill_exa_test": skill_exa_test,
        "completion": {
            "xp": 50,
            "badge": f"{title} Specialist",
            "unlock_next": topic_id + 1 if topic_id < 65 else None,
        },
    }

PYTHON_TOPICS = {item["id"]: _build_topic(item) for item in TOPIC_CATALOG}