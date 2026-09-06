"""C Programming Curriculum Catalog and Content Builder for 48 topics across 10 modules."""
from __future__ import annotations

C_TOPIC_CATALOG = [
    # 1. Introduction
    {"id": 1, "title": "Introduction to C", "difficulty": "Beginner", "duration": "20 min", "category": "Introduction"},
    {"id": 2, "title": "Compilation Process", "difficulty": "Beginner", "duration": "20 min", "category": "Introduction"},
    {"id": 3, "title": "Identifiers", "difficulty": "Beginner", "duration": "15 min", "category": "Introduction"},
    {"id": 4, "title": "Keywords", "difficulty": "Beginner", "duration": "15 min", "category": "Introduction"},
    {"id": 5, "title": "Input and Output", "difficulty": "Beginner", "duration": "25 min", "category": "Introduction"},
    {"id": 6, "title": "Variables", "difficulty": "Beginner", "duration": "20 min", "category": "Introduction"},
    {"id": 7, "title": "Data Types", "difficulty": "Beginner", "duration": "25 min", "category": "Introduction"},
    {"id": 8, "title": "Operators", "difficulty": "Beginner", "duration": "30 min", "category": "Introduction"},

    # 2. Control Flow
    {"id": 9, "title": "Conditional Statements", "difficulty": "Beginner", "duration": "30 min", "category": "Control Flow"},
    {"id": 10, "title": "Loops", "difficulty": "Intermediate", "duration": "35 min", "category": "Control Flow"},

    # 3. Functions
    {"id": 11, "title": "Functions", "difficulty": "Intermediate", "duration": "30 min", "category": "Functions"},
    {"id": 12, "title": "Parameter Passing Techniques", "difficulty": "Intermediate", "duration": "30 min", "category": "Functions"},
    {"id": 13, "title": "Main Function", "difficulty": "Intermediate", "duration": "20 min", "category": "Functions"},
    {"id": 14, "title": "Recursion", "difficulty": "Intermediate", "duration": "35 min", "category": "Functions"},
    {"id": 15, "title": "Inline Function", "difficulty": "Intermediate", "duration": "25 min", "category": "Functions"},
    {"id": 16, "title": "Nested Functions", "difficulty": "Intermediate", "duration": "25 min", "category": "Functions"},

    # 4. Arrays and Strings
    {"id": 17, "title": "Arrays", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays and Strings"},
    {"id": 18, "title": "Multidimensional Arrays", "difficulty": "Intermediate", "duration": "35 min", "category": "Arrays and Strings"},
    {"id": 19, "title": "Strings", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays and Strings"},
    {"id": 20, "title": "String Functions", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays and Strings"},

    # 5. Pointers
    {"id": 21, "title": "Pointers", "difficulty": "Intermediate", "duration": "40 min", "category": "Pointers"},
    {"id": 22, "title": "Pointer Arithmetic", "difficulty": "Advanced", "duration": "35 min", "category": "Pointers"},
    {"id": 23, "title": "Pointer to Pointer", "difficulty": "Advanced", "duration": "35 min", "category": "Pointers"},
    {"id": 24, "title": "Function Pointers", "difficulty": "Advanced", "duration": "40 min", "category": "Pointers"},

    # 6. User-Defined Data Types
    {"id": 25, "title": "Structures", "difficulty": "Intermediate", "duration": "35 min", "category": "User-Defined Data Types"},
    {"id": 26, "title": "Unions", "difficulty": "Intermediate", "duration": "30 min", "category": "User-Defined Data Types"},
    {"id": 27, "title": "Enumeration (enum)", "difficulty": "Intermediate", "duration": "25 min", "category": "User-Defined Data Types"},

    # 7. File Handling
    {"id": 28, "title": "Basics of File Handling", "difficulty": "Intermediate", "duration": "35 min", "category": "File Handling"},
    {"id": 29, "title": "Reading a File", "difficulty": "Intermediate", "duration": "30 min", "category": "File Handling"},
    {"id": 30, "title": "Reading/Writing Structures From/To a File", "difficulty": "Advanced", "duration": "40 min", "category": "File Handling"},
    {"id": 31, "title": "EOF, getc() and feof()", "difficulty": "Advanced", "duration": "30 min", "category": "File Handling"},
    {"id": 32, "title": "Deleting a File", "difficulty": "Intermediate", "duration": "25 min", "category": "File Handling"},

    # 8. Error Handling
    {"id": 33, "title": "Error Handling", "difficulty": "Intermediate", "duration": "30 min", "category": "Error Handling"},
    {"id": 34, "title": "Exception Handling Using goto", "difficulty": "Advanced", "duration": "30 min", "category": "Error Handling"},
    {"id": 35, "title": "File Error Handling", "difficulty": "Advanced", "duration": "30 min", "category": "Error Handling"},
    {"id": 36, "title": "Divide-by-Zero Exception", "difficulty": "Intermediate", "duration": "25 min", "category": "Error Handling"},

    # 9. Miscellaneous Concepts
    {"id": 37, "title": "Preprocessors", "difficulty": "Intermediate", "duration": "30 min", "category": "Miscellaneous Concepts"},
    {"id": 38, "title": "Macros", "difficulty": "Intermediate", "duration": "30 min", "category": "Miscellaneous Concepts"},
    {"id": 39, "title": "Header Files", "difficulty": "Intermediate", "duration": "25 min", "category": "Miscellaneous Concepts"},
    {"id": 40, "title": "Date and Time", "difficulty": "Intermediate", "duration": "30 min", "category": "Miscellaneous Concepts"},
    {"id": 41, "title": "Linkage", "difficulty": "Advanced", "duration": "35 min", "category": "Miscellaneous Concepts"},
    {"id": 42, "title": "Storage Classes", "difficulty": "Advanced", "duration": "35 min", "category": "Miscellaneous Concepts"},

    # 10. Advanced Concepts
    {"id": 43, "title": "Variadic Functions", "difficulty": "Advanced", "duration": "40 min", "category": "Advanced Concepts"},
    {"id": 44, "title": "Input-Output System Calls", "difficulty": "Advanced", "duration": "45 min", "category": "Advanced Concepts"},
    {"id": 45, "title": "Signals", "difficulty": "Advanced", "duration": "40 min", "category": "Advanced Concepts"},
    {"id": 46, "title": "Socket Programming", "difficulty": "Advanced", "duration": "50 min", "category": "Advanced Concepts"},
    {"id": 47, "title": "_Generic Keyword", "difficulty": "Advanced", "duration": "35 min", "category": "Advanced Concepts"},
    {"id": 48, "title": "Multithreading", "difficulty": "Advanced", "duration": "50 min", "category": "Advanced Concepts"},
]

C_TOPIC_CORE = {
    1: {
        "concept": "C is a procedural, general-purpose programming language developed by Dennis Ritchie at Bell Labs in 1972.",
        "syntax": "#include <stdio.h>\n\nint main() {\n    printf(\"Hello, World!\\n\");\n    return 0;\n}",
        "example": {
            "code": "#include <stdio.h>\n\nint main() {\n    printf(\"Welcome to SkillExa C Track!\\n\");\n    return 0;\n}",
            "output": "Welcome to SkillExa C Track!",
            "explanation": "#include <stdio.h> includes the standard input/output library. main() is the entry point.",
        },
        "fill_blanks": {
            "question": "#include <_____.h>\n\nint main() {\n    _____\(\"Hello, C!\\n\");\n    return 0;\n}",
            "answers": ["stdio", "printf"],
            "options": ["stdio", "printf", "stdlib", "scanf"],
        },
        "compiler": {
            "title": "Hello World in C",
            "question": "Complete the C program to print 'Welcome to SkillExa C Track!'.",
            "starter_code": "#include <stdio.h>\n\nint main() {\n    _____(\"Welcome to SkillExa C Track!\\n\");\n    return 0;\n}",
            "options": ["printf", "scanf", "cout", "print"],
        },
        "skill_exa_test": [
            {
                "question": "Which header file is required for printf() and scanf() in C?",
                "options": ["<stdio.h>", "<stdlib.h>", "<string.h>", "<conio.h>"],
                "answer": "<stdio.h>",
            },
            {
                "question": "What is the return type of the standard main() function in C?",
                "options": ["int", "void", "float", "char"],
                "answer": "int",
            },
        ],
    },
    2: {
        "concept": "The C compilation process consists of 4 main stages: Preprocessing, Compiling, Assembling, and Linking.",
        "syntax": "gcc -Wall main.c -o main",
        "example": {
            "code": "#include <stdio.h>\n#define PLATFORM \"C Engine\"\n\nint main() {\n    printf(\"Compiled on %s\\n\", PLATFORM);\n    return 0;\n}",
            "output": "Compiled on C Engine",
            "explanation": "Preprocessor expands #define PLATFORM before compilation.",
        },
        "fill_blanks": {
            "question": "#define STAGE \"____\"\nint main() {\n    printf(\"%s\\n\", STAGE);\n    return 0;\n}",
            "answers": ["Linking"],
            "options": ["Linking", "Parsing", "Running", "Writing"],
        },
        "compiler": {
            "title": "Preprocessing & Compilation",
            "question": "Fill in the blank to print the macro macro expansion.",
            "starter_code": "#include <stdio.h>\n#define SYSTEM \"SkillExa C\"\n\nint main() {\n    _____\(\"System: %s\\n\", SYSTEM);\n    return 0;\n}",
            "options": ["printf", "scanf", "puts", "syslog"],
        },
        "skill_exa_test": [
            {
                "question": "Which stage of C compilation expands macros and includes header files?",
                "options": ["Preprocessing", "Compiling", "Assembling", "Linking"],
                "answer": "Preprocessing",
            },
        ],
    },
    3: {
        "concept": "Identifiers are user-defined names given to variables, functions, arrays, structures, and labels in C.",
        "syntax": "int student_age = 20;",
        "example": {
            "code": "#include <stdio.h>\n\nint main() {\n    int student_score = 95;\n    printf(\"Score: %d\\n\", student_score);\n    return 0;\n}",
            "output": "Score: 95",
            "explanation": "student_score is a valid C identifier starting with a letter.",
        },
        "fill_blanks": {
            "question": "int _____ = 100;\nprintf(\"%d\", total_count);",
            "answers": ["total_count"],
            "options": ["total_count", "100count", "int", "float"],
        },
        "compiler": {
            "title": "Declare C Identifiers",
            "question": "Fill in the correct identifier to print the count.",
            "starter_code": "#include <stdio.h>\n\nint main() {\n    int _____ = 50;\n    printf(\"%d\\n\", items_count);\n    return 0;\n}",
            "options": ["items_count", "50items", "default", "class"],
        },
        "skill_exa_test": [
            {
                "question": "Which of the following is a valid C identifier?",
                "options": ["_score", "1score", "score-val", "return"],
                "answer": "_score",
            },
        ],
    },
    4: {
        "concept": "Keywords are reserved words in C with predefined meanings that cannot be used as identifiers (e.g., int, return, if, for, struct).",
        "syntax": "const int MAX_LIMIT = 100;",
        "example": {
            "code": "#include <stdio.h>\n\nint main() {\n    const double PI = 3.14159;\n    printf(\"PI: %.2f\\n\", PI);\n    return 0;\n}",
            "output": "PI: 3.14",
            "explanation": "const and double are reserved C keywords.",
        },
        "fill_blanks": {
            "question": "_____ float price = 19.99f;",
            "answers": ["const"],
            "options": ["const", "var", "let", "define"],
        },
        "compiler": {
            "title": "C Keywords Practice",
            "question": "Fill in the C keyword to declare a constant float variable.",
            "starter_code": "#include <stdio.h>\n\nint main() {\n    _____ float rate = 7.5f;\n    printf(\"Rate: %.1f\\n\", rate);\n    return 0;\n}",
            "options": ["const", "final", "static", "auto"],
        },
        "skill_exa_test": [
            {
                "question": "How many standard reserved keywords exist in ANSI C (C89)?",
                "options": ["32", "48", "64", "28"],
                "answer": "32",
            },
        ],
    },
    5: {
        "concept": "Input and Output in C is handled using printf() for output and scanf() for formatted input.",
        "syntax": "scanf(\"%d\", &variable);",
        "example": {
            "code": "#include <stdio.h>\n\nint main() {\n    int val = 42;\n    printf(\"Value: %d\\n\", val);\n    return 0;\n}",
            "output": "Value: 42",
            "explanation": "%d format specifier prints signed decimal integers.",
        },
        "fill_blanks": {
            "question": "int age = 20;\nprintf(\"Age: %_\", ____);",
            "answers": ["d", "age"],
            "options": ["d", "age", "f", "s"],
        },
        "compiler": {
            "title": "Formatted I/O in C",
            "question": "Complete the printf statement to print integer x.",
            "starter_code": "#include <stdio.h>\n\nint main() {\n    int x = 15;\n    _____\(\"x = %d\\n\", x);\n    return 0;\n}",
            "options": ["printf", "scanf", "puts", "print"],
        },
        "skill_exa_test": [
            {
                "question": "Which format specifier is used to print a double in printf()?",
                "options": ["%f", "%d", "%c", "%s"],
                "answer": "%f",
            },
        ],
    },
    6: {
        "concept": "Variables in C are named memory locations storing values of a specific data type.",
        "syntax": "int age = 25;",
        "example": {
            "code": "#include <stdio.h>\n\nint main() {\n    int a = 10, b = 20;\n    int sum = a + b;\n    printf(\"Sum: %d\\n\", sum);\n    return 0;\n}",
            "output": "Sum: 30",
            "explanation": "Variables a and b store integer values.",
        },
        "fill_blanks": {
            "question": "_____ num = 100;\nnum = num + 50;\nprintf(\"%d\", num);",
            "answers": ["int"],
            "options": ["int", "char", "void", "double"],
        },
        "compiler": {
            "title": "Declare C Variables",
            "question": "Fill in the type to declare integer variable score.",
            "starter_code": "#include <stdio.h>\n\nint main() {\n    _____ score = 88;\n    printf(\"Score: %d\\n\", score);\n    return 0;\n}",
            "options": ["int", "float", "char", "void"],
        },
        "skill_exa_test": [
            {
                "question": "Where are local variables stored in C memory layout?",
                "options": ["Stack", "Heap", "Data Segment", "BSS"],
                "answer": "Stack",
            },
        ],
    },
    7: {
        "concept": "C supports basic data types: int, float, double, char, and void, along with modifiers signed, unsigned, short, and long.",
        "syntax": "long long big_num = 1234567890LL;",
        "example": {
            "code": "#include <stdio.h>\n\nint main() {\n    char letter = 'A';\n    printf(\"Character: %c, ASCII: %d\\n\", letter, letter);\n    return 0;\n}",
            "output": "Character: A, ASCII: 65",
            "explanation": "char stores single byte text or ASCII codes.",
        },
        "fill_blanks": {
            "question": "_____ grade = 'A';\nprintf(\"%c\", grade);",
            "answers": ["char"],
            "options": ["char", "int", "double", "string"],
        },
        "compiler": {
            "title": "Data Types in C",
            "question": "Fill in the char data type to store character 'C'.",
            "starter_code": "#include <stdio.h>\n\nint main() {\n    _____ symbol = 'C';\n    printf(\"Symbol: %c\\n\", symbol);\n    return 0;\n}",
            "options": ["char", "int", "float", "double"],
        },
        "skill_exa_test": [
            {
                "question": "What is the typical size of a standard char in C?",
                "options": ["1 byte", "2 bytes", "4 bytes", "8 bytes"],
                "answer": "1 byte",
            },
        ],
    },
    8: {
        "concept": "Operators in C include Arithmetic, Relational, Logical, Bitwise, Assignment, and Ternary operators.",
        "syntax": "int result = (a > b) ? a : b;",
        "example": {
            "code": "#include <stdio.h>\n\nint main() {\n    int a = 7, b = 3;\n    printf(\"Remainder: %d\\n\", a % b);\n    return 0;\n}",
            "output": "Remainder: 1",
            "explanation": "% modulus operator computes remainder of integer division.",
        },
        "fill_blanks": {
            "question": "int rem = 10 _____ 3;\nprintf(\"%d\", rem);",
            "answers": ["%"],
            "options": ["%", "/", "*", "&&"],
        },
        "compiler": {
            "title": "C Operators",
            "question": "Fill in the modulus operator to get remainder.",
            "starter_code": "#include <stdio.h>\n\nint main() {\n    int x = 17, y = 5;\n    printf(\"Remainder: %d\\n\", x _____ y);\n    return 0;\n}",
            "options": ["%", "/", "*", "&&"],
        },
        "skill_exa_test": [
            {
                "question": "Which operator returns the remainder of integer division in C?",
                "options": ["%", "/", "*", "&"],
                "answer": "%",
            },
        ],
    },
    9: {
        "concept": "Conditional statements (if, if-else, nested if, switch) branch code execution based on boolean conditions.",
        "syntax": "switch(choice) {\n    case 1: break;\n    default: break;\n}",
        "example": {
            "code": "#include <stdio.h>\n\nint main() {\n    int marks = 85;\n    if (marks >= 80) {\n        printf(\"Grade: A\\n\");\n    } else {\n        printf(\"Grade: B\\n\");\n    }\n    return 0;\n}",
            "output": "Grade: A",
            "explanation": "if-else evaluates marks >= 80 to true.",
        },
        "fill_blanks": {
            "question": "_____ (val > 0) {\n    printf(\"Positive\");\n}",
            "answers": ["if"],
            "options": ["if", "else", "switch", "while"],
        },
        "compiler": {
            "title": "C Control Flow - if statement",
            "question": "Fill in the if keyword to test condition.",
            "starter_code": "#include <stdio.h>\n\nint main() {\n    int n = 10;\n    _____ (n > 0) {\n        printf(\"Positive\\n\");\n    }\n    return 0;\n}",
            "options": ["if", "else", "for", "switch"],
        },
        "skill_exa_test": [
            {
                "question": "Which keyword ends a case block inside a switch statement?",
                "options": ["break", "stop", "exit", "continue"],
                "answer": "break",
            },
        ],
    },
    10: {
        "concept": "Loops (for, while, do-while) repeat code execution while a condition evaluates to true.",
        "syntax": "for (int i = 0; i < n; i++) { ... }",
        "example": {
            "code": "#include <stdio.h>\n\nint main() {\n    for (int i = 1; i <= 3; i++) {\n        printf(\"%d \", i);\n    }\n    printf(\"\\n\");\n    return 0;\n}",
            "output": "1 2 3 ",
            "explanation": "for loop iterates from i = 1 up to i = 3.",
        },
        "fill_blanks": {
            "question": "_____ (int i = 0; i < 5; i++) {\n    printf(\"%d\", i);\n}",
            "answers": ["for"],
            "options": ["for", "while", "do", "if"],
        },
        "compiler": {
            "title": "C Loops - for loop",
            "question": "Fill in the for keyword to start loop.",
            "starter_code": "#include <stdio.h>\n\nint main() {\n    _____ (int i = 1; i <= 3; i++) {\n        printf(\"%d\\n\", i);\n    }\n    return 0;\n}",
            "options": ["for", "while", "do", "repeat"],
        },
        "skill_exa_test": [
            {
                "question": "Which loop guarantees at least one execution of its loop body?",
                "options": ["do-while", "for", "while", "foreach"],
                "answer": "do-while",
            },
        ],
    },

    # Topics 11 through 48
    11: {
        "concept": "Functions break C code into reusable, modular blocks of statements.",
        "syntax": "int add(int a, int b) {\n    return a + b;\n}",
        "example": {
            "code": "#include <stdio.h>\n\nint square(int n) {\n    return n * n;\n}\n\nint main() {\n    printf(\"Square: %d\\n\", square(5));\n    return 0;\n}",
            "output": "Square: 25",
            "explanation": "square() function takes parameter n and returns n * n.",
        },
        "fill_blanks": {
            "question": "_____ add(int a, int b) {\n    return a + b;\n}",
            "answers": ["int"],
            "options": ["int", "void", "char", "double"],
        },
        "compiler": {
            "title": "C Functions",
            "question": "Fill in return keyword to return calculated square value.",
            "starter_code": "#include <stdio.h>\n\nint square(int n) {\n    _____ n * n;\n}\n\nint main() {\n    printf(\"%d\\n\", square(4));\n    return 0;\n}",
            "options": ["return", "output", "yield", "send"],
        },
        "skill_exa_test": [
            {
                "question": "What is the default return type of a function in C if omitted?",
                "options": ["int", "void", "float", "char"],
                "answer": "int",
            },
        ],
    },
    12: {
        "concept": "Parameters in C are passed by Value (creates a copy) or by Reference (passes memory address using pointers).",
        "syntax": "void swap(int *a, int *b);",
        "example": {
            "code": "#include <stdio.h>\n\nvoid increment(int *p) {\n    (*p)++;\n}\n\nint main() {\n    int val = 10;\n    increment(&val);\n    printf(\"Val: %d\\n\", val);\n    return 0;\n}",
            "output": "Val: 11",
            "explanation": "Passing &val (reference) allows function to modify main variable.",
        },
        "fill_blanks": {
            "question": "void update(int *p) {\n    _____ = 50;\n}",
            "answers": ["*p"],
            "options": ["*p", "p", "&p", "int"],
        },
        "compiler": {
            "title": "Pass by Reference in C",
            "question": "Pass address of variable x using & operator.",
            "starter_code": "#include <stdio.h>\n\nvoid modify(int *ptr) {\n    *ptr = 99;\n}\n\nint main() {\n    int x = 10;\n    modify(_____);\n    printf(\"%d\\n\", x);\n    return 0;\n}",
            "options": ["&x", "x", "*x", "ptr"],
        },
        "skill_exa_test": [
            {
                "question": "Which mechanism allows a C function to modify caller variables directly?",
                "options": ["Pass by Reference using Pointers", "Pass by Value", "Global variables only", "Recursion"],
                "answer": "Pass by Reference using Pointers",
            },
        ],
    },

    21: {
        "concept": "A pointer is a variable that stores the memory address of another variable.",
        "syntax": "int *ptr = &num;",
        "example": {
            "code": "#include <stdio.h>\n\nint main() {\n    int num = 42;\n    int *ptr = &num;\n    printf(\"Value: %d, Address: %p\\n\", *ptr, (void*)ptr);\n    return 0;\n}",
            "output": "Value: 42",
            "explanation": "*ptr dereferences the memory address stored in ptr.",
        },
        "fill_blanks": {
            "question": "int val = 10;\nint *ptr = ____val;\nprintf(\"%d\", *ptr);",
            "answers": ["&"],
            "options": ["&", "*", "->", "."],
        },
        "compiler": {
            "title": "C Pointers",
            "question": "Use address-of operator & to point ptr to variable a.",
            "starter_code": "#include <stdio.h>\n\nint main() {\n    int a = 100;\n    int *ptr = ____a;\n    printf(\"%d\\n\", *ptr);\n    return 0;\n}",
            "options": ["&", "*", "->", "%"],
        },
        "skill_exa_test": [
            {
                "question": "Which operator is used to get the memory address of a variable in C?",
                "options": ["&", "*", "->", "."],
                "answer": "&",
            },
        ],
    },

    25: {
        "concept": "A structure (struct) is a user-defined data type that groups related variables of different data types together.",
        "syntax": "struct Student {\n    char name[50];\n    int age;\n};",
        "example": {
            "code": "#include <stdio.h>\n\nstruct Point {\n    int x;\n    int y;\n};\n\nint main() {\n    struct Point p1 = {10, 20};\n    printf(\"Point: (%d, %d)\\n\", p1.x, p1.y);\n    return 0;\n}",
            "output": "Point: (10, 20)",
            "explanation": "p1.x and p1.y access member variables of struct Point.",
        },
        "fill_blanks": {
            "question": "_____ Book {\n    char title[30];\n    float price;\n};",
            "answers": ["struct"],
            "options": ["struct", "union", "typedef", "class"],
        },
        "compiler": {
            "title": "C Structures",
            "question": "Fill in struct keyword to define Point structure.",
            "starter_code": "#include <stdio.h>\n\n_____ Point {\n    int x;\n    int y;\n};\n\nint main() {\n    struct Point p = {5, 15};\n    printf(\"x=%d\\n\", p.x);\n    return 0;\n}",
            "options": ["struct", "union", "enum", "typedef"],
        },
        "skill_exa_test": [
            {
                "question": "Which operator is used to access members of a structure variable?",
                "options": [".", "->", "*", "&"],
                "answer": ".",
            },
        ],
    },
}


def _build_c_topic(topic_meta: dict[str, object]) -> dict[str, object]:
    topic_id = int(topic_meta["id"])
    core = C_TOPIC_CORE.get(topic_id, {})
    title = str(topic_meta["title"])
    category = str(topic_meta.get("category", "General"))

    concept = core.get("concept", f"{title} is a fundamental concept in C programming.")
    syntax = core.get("syntax", f"// {title} syntax example\n// Review syntax rules carefully.")
    
    example = core.get("example")
    if not isinstance(example, dict):
        example = {
            "code": f"#include <stdio.h>\n\nint main() {{\n    printf(\"Demonstrating {title}\\n\");\n    return 0;\n}}",
            "output": f"Demonstrating {title}",
            "explanation": f"This program demonstrates {title} in C.",
        }

    fill_blanks = core.get("fill_blanks")
    if not isinstance(fill_blanks, dict):
        fill_blanks = {
            "question": f"#include <stdio.h>\n\nint main() {{\n    _____(\"{title}\\n\");\n    return 0;\n}}",
            "answers": ["printf"],
            "options": ["printf", "scanf", "puts", "int"],
        }

    compiler = core.get("compiler")
    if not isinstance(compiler, dict):
        compiler = {
            "title": f"Practice {title}",
            "question": f"Fill in the blanks to complete the C program for {title}, then run it.",
            "starter_code": f"#include <stdio.h>\n\nint main() {{\n    _____(\"{title} C Sandbox\\n\");\n    return 0;\n}}",
            "options": ["printf", "scanf", "return", "int", "include"],
        }

    skill_exa_test = core.get("skill_exa_test")
    if not isinstance(skill_exa_test, list):
        skill_exa_test = [
            {
                "question": f"Which module category does '{title}' belong to in C?",
                "options": [category, "Introduction", "Pointers", "Advanced Concepts"],
                "answer": category,
            }
        ]

    return {
        "id": topic_id,
        "title": title,
        "category": category,
        "difficulty": topic_meta["difficulty"],
        "duration": topic_meta["duration"],
        "concept": concept,
        "syntax": syntax,
        "example": example,
        "output": example.get("output", ""),
        "theory": {
            "definition": concept,
            "why": f"{title} builds essential foundational skills in C software development.",
            "rules": [
                "Always include required standard header files like <stdio.h>.",
                "Ensure variables are declared before use.",
                "Verify format specifiers match variable data types.",
            ],
            "examples": [example.get("code", "")],
        },
        "fill_blanks": fill_blanks,
        "compiler": compiler,
        "skill_exa_test": skill_exa_test,
        "completion": {
            "xp": 50,
            "badge": f"{title} C Specialist",
            "unlock_next": topic_id + 1 if topic_id < 48 else None,
        },
    }


C_TOPICS = {item["id"]: _build_c_topic(item) for item in C_TOPIC_CATALOG}
