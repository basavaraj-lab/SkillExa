"""C++ Programming Curriculum Catalog and Content Builder for 70 topics across 13 modules."""
from __future__ import annotations

CPP_TOPIC_CATALOG = [
    # 1. Basics
    {"id": 1, "title": "Introduction to C++", "difficulty": "Beginner", "duration": "20 min", "category": "Basics"},
    {"id": 2, "title": "Basic Input / Output", "difficulty": "Beginner", "duration": "20 min", "category": "Basics"},
    {"id": 3, "title": "Identifiers", "difficulty": "Beginner", "duration": "15 min", "category": "Basics"},
    {"id": 4, "title": "Keywords", "difficulty": "Beginner", "duration": "15 min", "category": "Basics"},
    {"id": 5, "title": "Variables", "difficulty": "Beginner", "duration": "20 min", "category": "Basics"},
    {"id": 6, "title": "Data Types", "difficulty": "Beginner", "duration": "25 min", "category": "Basics"},
    {"id": 7, "title": "Arithmetic & Relational Operators", "difficulty": "Beginner", "duration": "25 min", "category": "Basics"},
    {"id": 8, "title": "Logical & Bitwise Operators", "difficulty": "Beginner", "duration": "25 min", "category": "Basics"},
    {"id": 9, "title": "Assignment, Ternary & Misc Operators", "difficulty": "Beginner", "duration": "25 min", "category": "Basics"},
    {"id": 10, "title": "If, If-Else & If-Else-If Statements", "difficulty": "Beginner", "duration": "25 min", "category": "Basics"},
    {"id": 11, "title": "Switch Statement & Ternary Decisioning", "difficulty": "Beginner", "duration": "25 min", "category": "Basics"},
    {"id": 12, "title": "For Loop", "difficulty": "Intermediate", "duration": "25 min", "category": "Basics"},
    {"id": 13, "title": "While Loop", "difficulty": "Intermediate", "duration": "25 min", "category": "Basics"},
    {"id": 14, "title": "Do-While Loop", "difficulty": "Intermediate", "duration": "25 min", "category": "Basics"},
    {"id": 15, "title": "Range-Based For Loop & Loop Control", "difficulty": "Intermediate", "duration": "30 min", "category": "Basics"},


    # 2. Functions
    {"id": 10, "title": "Functions", "difficulty": "Intermediate", "duration": "30 min", "category": "Functions"},
    {"id": 11, "title": "Function Overloading", "difficulty": "Intermediate", "duration": "30 min", "category": "Functions"},
    {"id": 12, "title": "Parameter Passing", "difficulty": "Intermediate", "duration": "30 min", "category": "Functions"},
    {"id": 13, "title": "Default Arguments", "difficulty": "Intermediate", "duration": "20 min", "category": "Functions"},
    {"id": 14, "title": "Inline Functions", "difficulty": "Intermediate", "duration": "25 min", "category": "Functions"},
    {"id": 15, "title": "Recursion", "difficulty": "Intermediate", "duration": "35 min", "category": "Functions"},
    {"id": 16, "title": "Lambda Expressions", "difficulty": "Advanced", "duration": "35 min", "category": "Functions"},

    # 3. Arrays and Strings
    {"id": 17, "title": "Arrays", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays and Strings"},
    {"id": 18, "title": "Multidimensional Arrays", "difficulty": "Intermediate", "duration": "35 min", "category": "Arrays and Strings"},
    {"id": 19, "title": "Strings", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays and Strings"},
    {"id": 20, "title": "String Class", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays and Strings"},
    {"id": 21, "title": "String Functions", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays and Strings"},

    # 4. Pointers and References
    {"id": 22, "title": "Pointers", "difficulty": "Intermediate", "duration": "40 min", "category": "Pointers and References"},
    {"id": 23, "title": "References", "difficulty": "Intermediate", "duration": "30 min", "category": "Pointers and References"},
    {"id": 24, "title": "References vs Pointers", "difficulty": "Advanced", "duration": "35 min", "category": "Pointers and References"},

    # 5. User-Defined Data Types
    {"id": 25, "title": "Structures", "difficulty": "Intermediate", "duration": "35 min", "category": "User-Defined Data Types"},
    {"id": 26, "title": "Unions", "difficulty": "Intermediate", "duration": "30 min", "category": "User-Defined Data Types"},
    {"id": 27, "title": "Enumeration (enum)", "difficulty": "Intermediate", "duration": "25 min", "category": "User-Defined Data Types"},
    {"id": 28, "title": "typedef and using", "difficulty": "Intermediate", "duration": "25 min", "category": "User-Defined Data Types"},

    # 6. Dynamic Memory Management
    {"id": 29, "title": "Dynamic Memory Allocation", "difficulty": "Advanced", "duration": "35 min", "category": "Dynamic Memory Management"},
    {"id": 30, "title": "new and delete", "difficulty": "Advanced", "duration": "35 min", "category": "Dynamic Memory Management"},
    {"id": 31, "title": "Memory Leaks", "difficulty": "Advanced", "duration": "30 min", "category": "Dynamic Memory Management"},

    # 7. Object-Oriented Programming (OOP)
    {"id": 32, "title": "Object-Oriented Programming (OOP)", "difficulty": "Intermediate", "duration": "35 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 33, "title": "Classes and Objects", "difficulty": "Intermediate", "duration": "40 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 34, "title": "Constructors", "difficulty": "Intermediate", "duration": "35 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 35, "title": "Encapsulation", "difficulty": "Intermediate", "duration": "30 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 36, "title": "Polymorphism", "difficulty": "Advanced", "duration": "45 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 37, "title": "Inheritance", "difficulty": "Advanced", "duration": "40 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 38, "title": "Abstraction", "difficulty": "Advanced", "duration": "35 min", "category": "Object-Oriented Programming (OOP)"},

    # 8. Templates & Standard Template Library (STL)
    {"id": 39, "title": "Templates", "difficulty": "Advanced", "duration": "40 min", "category": "Templates & STL"},
    {"id": 40, "title": "Standard Template Library (STL)", "difficulty": "Advanced", "duration": "45 min", "category": "Templates & STL"},
    {"id": 41, "title": "Algorithms", "difficulty": "Advanced", "duration": "35 min", "category": "Templates & STL"},
    {"id": 42, "title": "Containers", "difficulty": "Advanced", "duration": "40 min", "category": "Templates & STL"},
    {"id": 43, "title": "Iterators", "difficulty": "Advanced", "duration": "30 min", "category": "Templates & STL"},
    {"id": 44, "title": "Vector", "difficulty": "Advanced", "duration": "35 min", "category": "Templates & STL"},
    {"id": 45, "title": "Stack", "difficulty": "Advanced", "duration": "30 min", "category": "Templates & STL"},
    {"id": 46, "title": "Queue", "difficulty": "Advanced", "duration": "30 min", "category": "Templates & STL"},
    {"id": 47, "title": "Map", "difficulty": "Advanced", "duration": "35 min", "category": "Templates & STL"},
    {"id": 48, "title": "Set", "difficulty": "Advanced", "duration": "30 min", "category": "Templates & STL"},

    # 9. Exception Handling
    {"id": 49, "title": "Exception Handling", "difficulty": "Intermediate", "duration": "30 min", "category": "Exception Handling"},
    {"id": 50, "title": "Exception Handling Using Classes", "difficulty": "Advanced", "duration": "35 min", "category": "Exception Handling"},
    {"id": 51, "title": "Stack Unwinding", "difficulty": "Advanced", "duration": "30 min", "category": "Exception Handling"},
    {"id": 52, "title": "User-Defined Exceptions", "difficulty": "Advanced", "duration": "35 min", "category": "Exception Handling"},

    # 10. File Handling
    {"id": 53, "title": "Files and Streams", "difficulty": "Intermediate", "duration": "35 min", "category": "File Handling"},
    {"id": 54, "title": "I/O Redirection", "difficulty": "Advanced", "duration": "30 min", "category": "File Handling"},

    # 11. Multithreading
    {"id": 55, "title": "Introduction to Multithreading", "difficulty": "Advanced", "duration": "30 min", "category": "Multithreading"},
    {"id": 56, "title": "Creating Threads", "difficulty": "Advanced", "duration": "35 min", "category": "Multithreading"},
    {"id": 57, "title": "std::thread::join()", "difficulty": "Advanced", "duration": "30 min", "category": "Multithreading"},
    {"id": 58, "title": "Detaching a Thread", "difficulty": "Advanced", "duration": "30 min", "category": "Multithreading"},
    {"id": 59, "title": "Mutex", "difficulty": "Advanced", "duration": "35 min", "category": "Multithreading"},
    {"id": 60, "title": "Lock Guard", "difficulty": "Advanced", "duration": "30 min", "category": "Multithreading"},
    {"id": 61, "title": "Race Conditions", "difficulty": "Advanced", "duration": "35 min", "category": "Multithreading"},
    {"id": 62, "title": "Thread Synchronization", "difficulty": "Advanced", "duration": "40 min", "category": "Multithreading"},

    # 12. Advanced Concepts
    {"id": 63, "title": "Preprocessor", "difficulty": "Intermediate", "duration": "25 min", "category": "Advanced Concepts"},
    {"id": 64, "title": "Namespaces", "difficulty": "Intermediate", "duration": "30 min", "category": "Advanced Concepts"},
    {"id": 65, "title": "Smart Pointers", "difficulty": "Advanced", "duration": "40 min", "category": "Advanced Concepts"},
    {"id": 66, "title": "Callbacks", "difficulty": "Advanced", "duration": "35 min", "category": "Advanced Concepts"},
    {"id": 67, "title": "Signal Handling", "difficulty": "Advanced", "duration": "30 min", "category": "Advanced Concepts"},

    # 13. Skill Assessments
    {"id": 68, "title": "Beginner Skill Assessment Practice Test", "difficulty": "Beginner", "duration": "45 min", "category": "Skill Assessments"},
    {"id": 69, "title": "Intermediate Skill Assessment Practice Test", "difficulty": "Intermediate", "duration": "50 min", "category": "Skill Assessments"},
    {"id": 70, "title": "Advanced Skill Assessment Practice Test", "difficulty": "Advanced", "duration": "60 min", "category": "Skill Assessments"},
]


def _build_cpp_topic(meta: dict[str, str | int]) -> dict[str, object]:
    t_id = meta["id"]
    title = meta["title"]
    cat = meta["category"]
    diff = meta["difficulty"]
    dur = meta["duration"]

    return {
        "id": t_id,
        "title": title,
        "category": cat,
        "difficulty": diff,
        "duration": dur,
        "concept": f"Mastering {title} in C++ provides high-performance memory control and object-oriented abstractions.",
        "syntax": f"// C++ {title} syntax\n#include <iostream>\nusing namespace std;\n\nint main() {{\n    cout << \"{title} in C++\" << endl;\n    return 0;\n}}",
        "example": {
            "code": f"#include <iostream>\nusing namespace std;\n\nint main() {{\n    cout << \"SkillExa C++ Track: {title}\" << endl;\n    return 0;\n}}",
            "output": f"SkillExa C++ Track: {title}",
            "explanation": f"Demonstrates core usage of {title} in standard C++17.",
        },
        "fill_blanks": {
            "question": f"#include <iostream>\nusing namespace std;\n\nint main() {{\n    _____ << \"{title}\" << endl;\n    return 0;\n}}",
            "answers": ["cout"],
            "options": ["cout", "cin", "printf", "std"],
        },
        "compiler": {
            "title": f"C++ Practice - {title}",
            "question": f"Complete the C++ code to print output using std::cout.",
            "starter_code": f"#include <iostream>\nusing namespace std;\n\nint main() {{\n    _____ << \"Learning {title} on SkillExa!\" << endl;\n    return 0;\n}}",
            "options": ["cout", "cin", "print", "printf"],
        },
        "skill_exa_test": [
            {
                "question": f"Which standard stream object is used for outputting text in C++ for {title}?",
                "options": ["std::cout", "std::cin", "std::cerr", "printf"],
                "answer": "std::cout",
            }
        ],
    }


CPP_TOPICS: dict[int, dict[str, object]] = {
    meta["id"]: _build_cpp_topic(meta) for meta in CPP_TOPIC_CATALOG
}

# Override Topic 1 & 2 for specific detailed C++ intro
CPP_TOPICS[1] = {
    "id": 1,
    "title": "Introduction to C++",
    "category": "Basics",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "C++ is a general-purpose programming language developed by Bjarne Stroustrup as an extension of C. It supports procedural and object-oriented paradigms, fast execution, and direct memory management for system software, game engines, and competitive programming.",
    "syntax": "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Hello, World!\";\n    return 0;\n}",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\n// Basic C++ Program Structure\nint main() {\n    cout << \"Hello, World!\";\n    return 0;\n}",
        "output": "Hello, World!",
        "explanation": "#include <iostream> provides stream I/O. using namespace std enables std symbols. main() is the program entry point returning 0 upon successful execution.",
    },
    "fill_blanks": {
        "question": "Complete the basic C++ program structure:",
        "answers": ["iostream", "main", "cout", "return"],
        "options": ["iostream", "main", "cout", "return", "stdio.h", "print"],
    },
    "compiler": {
        "title": "First C++ Hello World Program",
        "question": "Arrange the lines to build a complete working C++ main program that prints Hello World.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Hello, World!\";\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    cout << \"Hello, World!\";",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "Who developed the C++ programming language as an extension of C?",
            "options": ["Bjarne Stroustrup", "Dennis Ritchie", "Guido van Rossum", "James Gosling"],
            "answer": "Bjarne Stroustrup",
        },
        {
            "question": "Which header file is required to include standard input/output stream objects like cin and cout?",
            "options": ["<iostream>", "<stdio.h>", "<fstream>", "<stdlib.h>"],
            "answer": "<iostream>",
        },
        {
            "question": "What is the entry point function where C++ program execution begins?",
            "options": ["start()", "main()", "init()", "run()"],
            "answer": "main()",
        },
        {
            "question": "What does the `return 0;` statement at the end of the main() function indicate?",
            "options": ["Program terminated with a runtime error", "Program executed successfully", "Compiler should re-run the loop", "Memory was freed"],
            "answer": "Program executed successfully",
        },
        {
            "question": "Which C++ operator is used with std::cout to send text to the output stream?",
            "options": ["<< (insertion operator)", ">> (extraction operator)", ":: (scope resolution)", "-> (arrow operator)"],
            "answer": "<< (insertion operator)",
        },
    ],
    "theory": {
        "definition": "C++ is a high-performance general-purpose language combining low-level memory access with high-level object-oriented abstractions.",
        "why": "Widely used in operating systems, game engines, embedded systems, and competitive programming due to near-hardware execution speed.",
        "rules": [
            "Header files (#include <iostream>) specify preprocessor directive dependencies.",
            "using namespace std allows referencing cout and cin without std:: prefix.",
            "int main() is mandatory as the primary entry point function.",
            "Statements must end with semicolons (;).",
            "return 0 indicates clean exit to the operating system.",
        ],
        "examples": [
            "#include <iostream>\nusing namespace std;\nint main() { cout << \"Hi\"; return 0; }",
        ],
    },
}

CPP_TOPICS[2] = {
    "id": 2,
    "title": "Basic Input / Output",
    "category": "Basics",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "C++ performs I/O through byte streams defined in <iostream>. Standard streams include std::cout (output), std::cin (input), std::cerr (unbuffered error stream for immediate display), and std::clog (buffered logging stream).",
    "syntax": "cin >> variable;\ncout << variable << endl;\ncerr << \"Immediate error\";\nclog << \"Buffered log\";",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int age = 18;\n    cout << \"Age entered: \" << age << endl;\n    cerr << \"Error log: Immediate unbuffered warning!\" << endl;\n    clog << \"System log: Buffered logging message.\" << endl;\n    return 0;\n}",
        "output": "Age entered: 18\nError log: Immediate unbuffered warning!\nSystem log: Buffered logging message.",
        "explanation": "cin reads input with >>, cout prints output with <<, cerr displays unbuffered errors instantly, and clog stores log messages in a buffer.",
    },
    "fill_blanks": {
        "question": "Complete the standard C++ stream objects:",
        "answers": ["cin", "cout", "cerr", "clog"],
        "options": ["cin", "cout", "cerr", "clog", "scanf", "printf"],
    },
    "compiler": {
        "title": "C++ Input and Output Streams",
        "question": "Arrange the lines to read integer input via cin and display output via cout and cerr.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int num = 42;\n    cout << \"Value: \" << num << endl;\n    cerr << \"Status: Execution OK\\n\";\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int num = 42;",
            "    cout << \"Value: \" << num << endl;",
            "    cerr << \"Status: Execution OK\\n\";",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "Which stream object is used to read input from the keyboard in C++?",
            "options": ["cin", "cout", "cerr", "clog"],
            "answer": "cin",
        },
        {
            "question": "Which operator is used with `cin` to extract data from the input stream?",
            "options": [">> (extraction operator)", "<< (insertion operator)", "::", "->"],
            "answer": ">> (extraction operator)",
        },
        {
            "question": "What is the key difference between std::cerr and std::clog?",
            "options": ["cerr is unbuffered for immediate display; clog is buffered", "cerr is for input; clog is for output", "clog cannot output to console", "cerr only works with floating point numbers"],
            "answer": "cerr is unbuffered for immediate display; clog is buffered",
        },
        {
            "question": "Which class instance does std::cout belong to in the <iostream> library?",
            "options": ["ostream", "istream", "fstream", "stringstream"],
            "answer": "ostream",
        },
        {
            "question": "What does `std::endl` do in an output statement?",
            "options": ["Inserts a newline character and flushes the output stream buffer", "Deletes the variable from memory", "Converts text to uppercase", "Terminates the program execution"],
            "answer": "Inserts a newline character and flushes the output stream buffer",
        },
    ],
    "theory": {
        "definition": "Basic I/O in C++ is managed via stream objects defined in <iostream> representing sequences of bytes flowing into or out of memory.",
        "why": "Streams provide type-safe, extensible input reading (cin) and output rendering (cout, cerr, clog).",
        "rules": [
            "Use cin >> var to read user input into a variable.",
            "Use cout << var to display formatted values.",
            "Use cerr for unbuffered error messages that must display immediately.",
            "Use clog for buffered diagnostic logging.",
            "Use endl or '\\n' to format multiline output.",
        ],
        "examples": [
            "int x; cin >> x; cout << \"x: \" << x;",
            "cerr << \"File error!\"; clog << \"Log update\";",
        ],
    },
}

CPP_TOPICS[3] = {
    "id": 3,
    "title": "Identifiers",
    "category": "Basics",
    "difficulty": "Beginner",
    "duration": "15 min",
    "concept": "Identifiers are user-defined names given to variables, functions, classes, methods, and objects in C++. They must follow strict naming rules: start with a letter or underscore, contain letters/digits/underscores, avoid reserved keywords, and remain case-sensitive.",
    "syntax": "class Student {\npublic:\n    void show() {\n        int marks = 90;\n        cout << marks;\n    }\n};\nStudent s1; // s1 is an object identifier",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nclass Student {\npublic:\n    void show() {\n        int marks = 90;\n        cout << \"Marks: \" << marks;\n    }\n};\n\nint main() {\n    Student s1; // Object identifier\n    s1.show(); // Method identifier call\n    return 0;\n}",
        "output": "Marks: 90",
        "explanation": "Student (class), show (method), marks (variable), s1 (object), and main (function) are all valid C++ identifiers.",
    },
    "fill_blanks": {
        "question": "Complete the valid identifier declaration and class definition:",
        "answers": ["Student", "_count", "totalSum", "show"],
        "options": ["Student", "_count", "totalSum", "show", "2count", "class"],
    },
    "compiler": {
        "title": "C++ Identifier Naming Verification",
        "question": "Arrange the lines to define a class Car, method getSum, and valid variable identifiers.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nclass Car {\n    string Brand;\n    int year;\n};\n\nint main() {\n    int age = 20;\n    int _count = 5;\n    cout << \"Total: \" << (age + _count);\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "class Car {",
            "    string Brand;",
            "    int year;",
            "};",
            "int main() {",
            "    int age = 20;",
            "    int _count = 5;",
            "    cout << \"Total: \" << (age + _count);",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "Which of the following is a valid starting character for a C++ identifier?",
            "options": ["A letter (a-z, A-Z) or an underscore (_)", "Any digit (0-9)", "A dollar sign ($) or hash (#)", "A space character"],
            "answer": "A letter (a-z, A-Z) or an underscore (_)",
        },
        {
            "question": "Why is `int 2value = 10;` an invalid C++ identifier?",
            "options": ["Because an identifier cannot start with a digit", "Because int requires double quotes", "Because 2value is a keyword", "Because 10 is an integer"],
            "answer": "Because an identifier cannot start with a digit",
        },
        {
            "question": "Is C++ a case-sensitive language regarding identifiers (e.g. `Num` vs `num`)?",
            "options": ["Yes, Num and num are treated as two distinct identifiers", "No, case is completely ignored", "Only when declaring classes", "Only when using standard libraries"],
            "answer": "Yes, Num and num are treated as two distinct identifiers",
        },
        {
            "question": "Can reserved keywords like `int`, `class`, or `return` be used as custom variable identifiers?",
            "options": ["No, attempting to use keywords as identifiers causes compilation errors", "Yes, as long as they are in uppercase", "Yes, without restrictions", "Only inside loops"],
            "answer": "No, attempting to use keywords as identifiers causes compilation errors",
        },
        {
            "question": "Which of the following is a VALID C++ identifier?",
            "options": ["_student_score_2", "2score", "student score", "float"],
            "answer": "_student_score_2",
        },
    ],
    "theory": {
        "definition": "An identifier is a user-defined sequence of characters used to name program entities such as variables, functions, structures, classes, and objects.",
        "why": "Identifiers give descriptive names to memory locations and code routines, enabling readable and maintainable programs.",
        "rules": [
            "Can only contain letters (A-Z, a-z), digits (0-9), and underscores (_).",
            "Must start with a letter or an underscore only (cannot start with a digit).",
            "C++ keywords (e.g., int, return, class) cannot be used as identifiers.",
            "Identifiers are case-sensitive (Score and score are different).",
            "No spaces or special symbols ($, #, %, @) are allowed.",
        ],
        "examples": [
            "int age = 20; // Valid",
            "int _total_sum = 100; // Valid",
            "// int 2sum = 50; // Invalid (starts with digit)",
        ],
    },
}

CPP_TOPICS[4] = {
    "id": 4,
    "title": "Keywords",
    "category": "Basics",
    "difficulty": "Beginner",
    "duration": "15 min",
    "concept": "Keywords are predefined, reserved words in C++ with fixed meanings to the compiler. Categorized across Data Types (int, bool, char, double, void), Control Flow (if, else, switch, for, while, do, break, continue), Memory (new, delete, sizeof), Classes (class, struct, friend, this), and Exceptions (try, catch, throw).",
    "syntax": "int age = 20;\nif (age > 18) {\n    cout << \"Adult\";\n}\nreturn 0;",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\n// Demonstrating keywords: int, main, if, return\nint main() {\n    int age = 20; // 'int' is a data type keyword\n    if (age >= 18) { // 'if' is a control flow keyword\n        cout << \"Adult\";\n    }\n    return 0; // 'return' is a function exit keyword\n}",
        "output": "Adult",
        "explanation": "int, main, if, and return are reserved words recognized by the C++ compiler and cannot be redefined.",
    },
    "fill_blanks": {
        "question": "Complete the C++ keyword usage in variable definition and control flow:",
        "answers": ["int", "if", "return", "class"],
        "options": ["int", "if", "return", "class", "variable", "include"],
    },
    "compiler": {
        "title": "C++ Keyword Syntax Verification",
        "question": "Arrange the lines to use reserved C++ keywords int, if, and return correctly.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int val = 15;\n    if (val > 10) {\n        cout << \"Value exceeds 10\\n\";\n    }\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int val = 15;",
            "    if (val > 10) {",
            "        cout << \"Value exceeds 10\\n\";",
            "    }",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What is a C++ keyword?",
            "options": ["A predefined reserved word with special meaning to the compiler", "A user-defined variable name", "A standard library header file", "A comment tag ignored by the compiler"],
            "answer": "A predefined reserved word with special meaning to the compiler",
        },
        {
            "question": "Which of the following is a C++ keyword used for pointer nullability introduced in C++11?",
            "options": ["nullptr", "NULL", "zero_ptr", "void_ptr"],
            "answer": "nullptr",
        },
        {
            "question": "What happens if a developer attempts to declare `int return = 10;` in C++?",
            "options": ["The compiler throws a syntax error because 'return' is a reserved keyword", "The program compiles normally", "The return value of main becomes 10", "The variable is renamed automatically"],
            "answer": "The compiler throws a syntax error because 'return' is a reserved keyword",
        },
        {
            "question": "Which keyword category includes `if`, `else`, `switch`, `for`, `while`, and `break`?",
            "options": ["Control Flow", "Data Types", "Memory Management", "Casting"],
            "answer": "Control Flow",
        },
        {
            "question": "How do keywords differ from identifiers?",
            "options": ["Keywords are predefined by the language; Identifiers are user-defined names", "Keywords can be in uppercase; Identifiers cannot", "Keywords store memory values; Identifiers do not", "There is no difference"],
            "answer": "Keywords are predefined by the language; Identifiers are user-defined names",
        },
    ],
    "theory": {
        "definition": "Keywords are reserved words that serve as fundamental building blocks of C++ syntax and cannot be used as identifier names.",
        "why": "Preserved keywords inform the compiler about control flow, data types, class structures, memory allocation, and access specifiers.",
        "rules": [
            "Keywords must always be written in lowercase (e.g. int, if, while).",
            "Keywords cannot be redefined or used as variable/function/class names.",
            "Syntax highlighters in IDEs render keywords in distinct colors.",
            "C++ standard evolution adds new keywords (e.g., nullptr, constexpr in C++11; co_await in C++20).",
        ],
        "examples": [
            "int age = 20; // 'int' is a keyword",
            "if (true) { } // 'if' and 'true' are keywords",
        ],
    },
}

CPP_TOPICS[5] = {
    "id": 5,
    "title": "Variables",
    "category": "Basics",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "Variables in C++ are named memory locations used to store data. A variable comprises 3 components: Data Type (e.g. int, float, string), Variable Name (identifier), and Value. Supports declaration, initialization, updating, and variable assignment.",
    "syntax": "type name;\nname = value;\ntype name = value;\nnum2 = num1;",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // Definition and initialization\n    int num1 = 10, num2;\n    // Assigning num1's value to num2\n    num2 = num1;\n    cout << \"num1: \" << num1 << \", num2: \" << num2 << endl;\n    \n    // Updating value\n    num1 = 7;\n    cout << \"Updated num1: \" << num1 << endl;\n    cout << \"Sum: \" << (num1 + num2) << endl;\n    return 0;\n}",
        "output": "num1: 10, num2: 10\nUpdated num1: 7\nSum: 17",
        "explanation": "Variables store values in allocated memory locations. Values can be retrieved, assigned between variables, or updated using the assignment operator (=).",
    },
    "fill_blanks": {
        "question": "Complete the variable declaration, initialization, and update snippet:",
        "answers": ["int", "num", "endl", "num1"],
        "options": ["int", "num", "endl", "num1", "float", "cin"],
    },
    "compiler": {
        "title": "C++ Variable Operations and Assignment",
        "question": "Arrange the lines to declare variables num1 and num2, perform assignment, update values, and compute addition.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int num1 = 10, num2 = 20;\n    int sum = num1 + num2;\n    cout << \"Sum: \" << sum << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int num1 = 10, num2 = 20;",
            "    int sum = num1 + num2;",
            "    cout << \"Sum: \" << sum << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What are the three essential components of a C++ variable?",
            "options": ["Data Type, Variable Name, and Value", "Header, Namespace, and Function", "Class, Pointer, and Reference", "Scope, Preprocessor, and Macro"],
            "answer": "Data Type, Variable Name, and Value",
        },
        {
            "question": "What happens when a decimal value like `3.14` is assigned to an `int` variable?",
            "options": ["The value is implicitly converted and truncated to integer 3", "A runtime error crashes the system", "The variable automatically becomes a float", "The compiler throws a fatal error"],
            "answer": "The value is implicitly converted and truncated to integer 3",
        },
        {
            "question": "What value do uninitialized local (automatic) variables contain in C++?",
            "options": ["Indeterminate garbage values", "Always zero (0)", "Always NULL", "Compiler default string"],
            "answer": "Indeterminate garbage values",
        },
        {
            "question": "What default initial value is automatically assigned to uninitialized global or static variables in C++?",
            "options": ["Zero (0)", "Garbage value", "100", "-1"],
            "answer": "Zero (0)",
        },
        {
            "question": "Which operator is used to assign or update a variable's value in C++?",
            "options": ["= (assignment operator)", "== (equality operator)", ":: (scope resolution)", "-> (arrow operator)"],
            "answer": "= (assignment operator)",
        },
    ],
    "theory": {
        "definition": "A variable is a symbolic name given to a specific block of memory that holds data during program execution.",
        "why": "Variables allow programs to dynamically store, manipulate, retrieve, and pass state values across functions.",
        "rules": [
            "Declaration specifies the data type and identifier name (e.g. int age;).",
            "Initialization assigns an initial value (e.g. age = 20;).",
            "Local variables should always be initialized before access to prevent garbage values.",
            "Updating replaces the stored value using the assignment operator =.",
            "Variables are allocated in distinct memory segments (Stack for local, Data/BSS for global/static).",
        ],
        "examples": [
            "int num = 3; num = 7; // Update",
            "int a = 10, b = 20; int sum = a + b;",
        ],
    },
}

CPP_TOPICS[6] = {
    "id": 6,
    "title": "Data Types",
    "category": "Basics",
    "difficulty": "Beginner",
    "duration": "25 min",
    "concept": "Data types in C++ define the type of data a variable can hold, determining memory allocation size and valid operations. C++ categorizes data types into Primitive/Built-in (int, char, bool, float, double, void), Derived (arrays, pointers, references, functions), User-Defined (struct, union, enum, class), and Standard Library types (std::string). Modifiers like short, long, signed, and unsigned alter size and range. The sizeof operator measures memory footprint in bytes.",
    "syntax": "int x = 10;\nchar ch = 'A';\nbool flag = true;\nfloat f = 3.14f;\ndouble d = 9.9999;\nunsigned long long big = 1234567890ULL;\nsizeof(int);",
    "example": {
        "code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    int integerVar = 100;\n    char charVar = 'Z';\n    bool boolVar = true;\n    float floatVar = 5.75f;\n    double doubleVar = 19.9999;\n    string stringVar = \"SkillExa C++\";\n\n    cout << \"int: \" << integerVar << \" (size: \" << sizeof(int) << \" bytes)\" << endl;\n    cout << \"char: \" << charVar << \" (size: \" << sizeof(char) << \" byte)\" << endl;\n    cout << \"bool: \" << boolVar << \" (size: \" << sizeof(bool) << \" byte)\" << endl;\n    cout << \"float: \" << floatVar << \" (size: \" << sizeof(float) << \" bytes)\" << endl;\n    cout << \"double: \" << doubleVar << \" (size: \" << sizeof(double) << \" bytes)\" << endl;\n    cout << \"string: \" << stringVar << endl;\n    return 0;\n}",
        "output": "int: 100 (size: 4 bytes)\nchar: Z (size: 1 byte)\nbool: 1 (size: 1 byte)\nfloat: 5.75 (size: 4 bytes)\ndouble: 19.9999 (size: 8 bytes)\nstring: SkillExa C++",
        "explanation": "Different data types allocate distinct memory sizes (e.g. 4 bytes for int/float, 8 bytes for double, 1 byte for char/bool). The sizeof operator calculates memory footprint at compile-time.",
    },
    "fill_blanks": {
        "question": "Complete the data type declaration and sizeof print statement:",
        "answers": ["double", "char", "sizeof", "bool"],
        "options": ["double", "char", "sizeof", "bool", "void", "unsigned"],
    },
    "compiler": {
        "title": "C++ Primitive Data Types and Memory Sizing",
        "question": "Arrange lines to declare int, char, and double variables and print their sizes using sizeof operator.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a = 42;\n    double b = 3.14159;\n    cout << \"sizeof int: \" << sizeof(a) << endl;\n    cout << \"sizeof double: \" << sizeof(b) << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int a = 42;",
            "    double b = 3.14159;",
            "    cout << \"sizeof int: \" << sizeof(a) << endl;",
            "    cout << \"sizeof double: \" << sizeof(b) << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "Which of the following is a primitive (built-in) data type in C++?",
            "options": ["int", "std::vector", "class", "std::string"],
            "answer": "int",
        },
        {
            "question": "What compile-time operator is used in C++ to find the memory footprint of a data type or variable in bytes?",
            "options": ["sizeof", "len()", "size()", "typeof"],
            "answer": "sizeof",
        },
        {
            "question": "Which modifier doubles the range of positive integers by preventing negative representation?",
            "options": ["unsigned", "signed", "short", "long"],
            "answer": "unsigned",
        },
        {
            "question": "What is the standard memory size allocated for a standard `char` data type in C++?",
            "options": ["1 byte", "2 bytes", "4 bytes", "8 bytes"],
            "answer": "1 byte",
        },
        {
            "question": "What output does printing a `bool` variable holding `true` produce when using `cout` without `boolalpha`?",
            "options": ["1", "true", "TRUE", "0"],
            "answer": "1",
        },
    ],
    "theory": {
        "definition": "Data types declare the nature, storage requirement, and set of operations permissible for variables.",
        "why": "Data types enable compiler memory layout optimization, type safety, and efficient hardware execution.",
        "rules": [
            "Primitive types: int (4B), char (1B), bool (1B), float (4B), double (8B), void.",
            "Type modifiers: signed, unsigned, short, long, long long.",
            "Derived types: Arrays, Pointers, References, Functions.",
            "User-defined types: struct, union, enum, class.",
            "Standard library types: std::string, std::vector, etc.",
            "sizeof returns size in bytes as type size_t.",
        ],
        "examples": [
            "unsigned int count = 500;",
            "long long distance = 9876543210LL;",
            "char letter = 'A';",
        ],
    },
}

CPP_TOPICS[7] = {
    "id": 7,
    "title": "Arithmetic & Relational Operators",
    "category": "Basics",
    "difficulty": "Beginner",
    "duration": "25 min",
    "concept": "Arithmetic operators (+, -, *, /, %, ++, --) and Relational operators (==, !=, >, <, >=, <=) perform mathematical calculations and value comparison in C++. Modulo (%) operates on integers yielding remainder. Pre-increment (++a) updates before expression evaluation while post-increment (a++) updates after.",
    "syntax": "int sum = a + b;\nint rem = a % b;\n++a;\nb--;\nbool isGreater = (a > b);\nbool isEqual = (a == b);",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a = 10, b = 3;\n    cout << \"Addition (a + b): \" << (a + b) << endl;\n    cout << \"Division (a / b): \" << (a / b) << endl;\n    cout << \"Modulo (a % b): \" << (a % b) << endl;\n    \n    int x = 5;\n    cout << \"Pre-increment (++x): \" << ++x << endl;\n    cout << \"Post-increment (x++): \" << x++ << endl;\n    cout << \"Value after post-increment: \" << x << endl;\n    \n    cout << \"Is a > b? \" << (a > b) << endl;\n    cout << \"Is a == b? \" << (a == b) << endl;\n    return 0;\n}",
        "output": "Addition (a + b): 13\nDivision (a / b): 3\nModulo (a % b): 1\nPre-increment (++x): 6\nPost-increment (x++): 6\nValue after post-increment: 7\nIs a > b? 1\nIs a == b? 0",
        "explanation": "Arithmetic division of integers truncates fractional parts; modulo computes remainder. Pre-increment updates variable prior to statement evaluation; relational operators return 1 for true and 0 for false.",
    },
    "fill_blanks": {
        "question": "Complete the arithmetic modulo and relational equality snippet:",
        "answers": ["%", "==", "++"],
        "options": ["%", "==", "++", "&&", "cout"],
    },
    "compiler": {
        "title": "C++ Arithmetic and Relational Expressions",
        "question": "Arrange lines to compute modulo, pre-increment, and relational comparison.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int num1 = 17, num2 = 5;\n    int remainder = num1 % num2;\n    bool check = (num1 >= num2);\n    cout << \"Remainder: \" << remainder << \", Check: \" << check << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int num1 = 17, num2 = 5;",
            "    int remainder = num1 % num2;",
            "    bool check = (num1 >= num2);",
            "    cout << \"Remainder: \" << remainder << \", Check: \" << check << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What operator in C++ yields the remainder of integer division?",
            "options": ["% (modulo operator)", "/ (division operator)", "* (multiplication operator)", "^ (bitwise XOR operator)"],
            "answer": "% (modulo operator)",
        },
        {
            "question": "What is the key difference between pre-increment (`++a`) and post-increment (`a++`)?",
            "options": [
                "Pre-increment modifies value before evaluation; post-increment modifies value after evaluation in expression",
                "Post-increment works on floats, pre-increment works only on integers",
                "Pre-increment uses 2 bytes, post-increment uses 4 bytes",
                "There is no difference in any context"
            ],
            "answer": "Pre-increment modifies value before evaluation; post-increment modifies value after evaluation in expression",
        },
        {
            "question": "What is the result of integer division `7 / 2` in C++?",
            "options": ["3", "3.5", "4", "0"],
            "answer": "3",
        },
        {
            "question": "What value does printing a true relational statement like `(10 > 5)` produce with `cout`?",
            "options": ["1", "true", "TRUE", "0"],
            "answer": "1",
        },
        {
            "question": "Which operator tests if two variables are NOT equal in C++?",
            "options": ["!=", "==", "!", "<>"],
            "answer": "!=",
        },
    ],
    "theory": {
        "definition": "Arithmetic and Relational operators perform numerical calculation and comparison evaluation.",
        "why": "Form the basis of all mathematical calculations, loop counters, and condition evaluations.",
        "rules": [
            "Modulo (%) requires integer operands.",
            "Pre-increment (++a) increments first, then yields value.",
            "Post-increment (a++) yields value first, then increments.",
            "Relational operators (==, !=, >, <, >=, <=) evaluate to bool (true/false).",
        ],
        "examples": [
            "int rem = 15 % 4; // 3",
            "bool pass = (marks >= 40);",
        ],
    },
}

CPP_TOPICS[8] = {
    "id": 8,
    "title": "Logical & Bitwise Operators",
    "category": "Basics",
    "difficulty": "Beginner",
    "duration": "25 min",
    "concept": "Logical operators (&&, ||, !) evaluate boolean conditions using short-circuiting logic. Bitwise operators (&, |, ^, ~, <<, >>) perform direct binary bit manipulations on integral types at hardware speed.",
    "syntax": "bool pass = (cond1 && cond2);\nbool flag = !isReady;\nint res = a & b;\nint shifted = a << 2;",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a = 12, b = 5; // Binary: a = 1100, b = 0101\n    bool cond = (a > 10) && (b < 10);\n    cout << \"Logical AND (a > 10 && b < 10): \" << cond << endl;\n    \n    cout << \"Bitwise AND (a & b): \" << (a & b) << endl;  // 1100 & 0101 = 0100 (4)\n    cout << \"Bitwise OR (a | b): \" << (a | b) << endl;   // 1100 | 0101 = 1101 (13)\n    cout << \"Bitwise XOR (a ^ b): \" << (a ^ b) << endl;  // 1100 ^ 0101 = 1001 (9)\n    cout << \"Left Shift (b << 1): \" << (b << 1) << endl; // 5 << 1 = 10\n    return 0;\n}",
        "output": "Logical AND (a > 10 && b < 10): 1\nBitwise AND (a & b): 4\nBitwise OR (a | b): 13\nBitwise XOR (a ^ b): 9\nLeft Shift (b << 1): 10",
        "explanation": "Logical AND short-circuits if left expression is false. Bitwise operators execute bitwise binary calculations directly on integer bit patterns.",
    },
    "fill_blanks": {
        "question": "Complete the logical AND and bitwise left shift snippet:",
        "answers": ["&&", "<<", "^"],
        "options": ["&&", "<<", "^", "||", "int"],
    },
    "compiler": {
        "title": "C++ Logical & Bitwise Evaluation",
        "question": "Arrange lines to evaluate logical AND and bitwise XOR.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int x = 6, y = 3;\n    bool logicalRes = (x > 0 && y > 0);\n    int bitwiseXor = x ^ y;\n    cout << \"Logical: \" << logicalRes << \", Bitwise XOR: \" << bitwiseXor << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int x = 6, y = 3;",
            "    bool logicalRes = (x > 0 && y > 0);",
            "    int bitwiseXor = x ^ y;",
            "    cout << \"Logical: \" << logicalRes << \", Bitwise XOR: \" << bitwiseXor << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "Which logical operator returns true only if BOTH operands evaluate to non-zero/true?",
            "options": ["&& (Logical AND)", "|| (Logical OR)", "! (Logical NOT)", "^ (Bitwise XOR)"],
            "answer": "&& (Logical AND)",
        },
        {
            "question": "What is short-circuit evaluation in logical `&&`?",
            "options": [
                "If the left operand is false, the right operand is not evaluated",
                "If the left operand is true, the right operand is skipped",
                "Both operands are always evaluated regardless of values",
                "It causes a compilation error for non-boolean values"
            ],
            "answer": "If the left operand is false, the right operand is not evaluated",
        },
        {
            "question": "Which operator represents Bitwise XOR in C++?",
            "options": ["^", "&", "|", "~"],
            "answer": "^",
        },
        {
            "question": "What effect does the bitwise left shift operation `x << 1` have on an integer `x`?",
            "options": ["Multiplies x by 2", "Divides x by 2", "Subtracts 1 from x", "Inverts all bits of x"],
            "answer": "Multiplies x by 2",
        },
        {
            "question": "Which bitwise operator flips all binary bits of an integer operand (1 to 0, 0 to 1)?",
            "options": ["~ (Bitwise NOT)", "& (Bitwise AND)", "| (Bitwise OR)", "^ (Bitwise XOR)"],
            "answer": "~ (Bitwise NOT)",
        },
    ],
    "theory": {
        "definition": "Logical operators combine boolean statements; bitwise operators manipulate individual binary bit representations.",
        "why": "Logical operators drive control flow decisions; bitwise operators enable high-performance low-level bit flag manipulation and binary protocols.",
        "rules": [
            "Logical && and || feature short-circuit evaluation.",
            "Bitwise operators (&, |, ^, ~, <<, >>) apply only to integral types.",
            "Left shift x << n equals x * (2^n).",
            "Right shift x >> n equals x / (2^n).",
        ],
        "examples": [
            "bool ok = (age >= 18) && (hasId == true);",
            "int flags = 1 << 3; // 8",
        ],
    },
}

CPP_TOPICS[9] = {
    "id": 9,
    "title": "Assignment, Ternary & Misc Operators",
    "category": "Basics",
    "difficulty": "Beginner",
    "duration": "25 min",
    "concept": "Assignment operators (=, +=, -=, *=, /=, %=) update variable values. The Ternary operator (? :) provides a compact 3-operand conditional expression. Miscellaneous operators include sizeof, comma (,), address-of (&), dereference (*), and static_cast.",
    "syntax": "x += 10;\nmaxVal = (a > b) ? a : b;\nsizeof(double);\nstatic_cast<float>(total);",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a = 20;\n    a += 10; // Compound assignment (a = a + 10)\n    cout << \"Compound Assignment (a += 10): \" << a << endl;\n    \n    int b = 15;\n    int minVal = (a < b) ? a : b;\n    cout << \"Ternary Min Value: \" << minVal << endl;\n    \n    double pi = 3.14159;\n    int intPi = static_cast<int>(pi);\n    cout << \"static_cast double to int: \" << intPi << endl;\n    return 0;\n}",
        "output": "Compound Assignment (a += 10): 30\nTernary Min Value: 15\nstatic_cast double to int: 3",
        "explanation": "Compound assignment modifies variable value in place. Ternary operator evaluates condition returning one of two expressions. static_cast provides safe explicit type conversion.",
    },
    "fill_blanks": {
        "question": "Complete the compound assignment, ternary operator, and static_cast snippet:",
        "answers": ["+=", "?", "static_cast"],
        "options": ["+=", "?", "static_cast", "==", "cout"],
    },
    "compiler": {
        "title": "C++ Assignment & Miscellaneous Operators",
        "question": "Arrange lines to execute compound assignment, ternary operator, and static_cast.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int score = 50;\n    score += 25;\n    int finalVal = (score >= 70) ? 1 : 0;\n    cout << \"Score: \" << score << \", Pass: \" << finalVal << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int score = 50;",
            "    score += 25;",
            "    int finalVal = (score >= 70) ? 1 : 0;",
            "    cout << \"Score: \" << score << \", Pass: \" << finalVal << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What is the equivalent expanded expression of `x += 5`?",
            "options": ["x = x + 5", "x = 5", "x + 5 = x", "x == 5"],
            "answer": "x = x + 5",
        },
        {
            "question": "What is the correct syntax structure of the ternary conditional operator?",
            "options": ["condition ? expression_if_true : expression_if_false", "if ? true : false", "condition : true ? false", "switch ? case : default"],
            "answer": "condition ? expression_if_true : expression_if_false",
        },
        {
            "question": "Which operator retrieves the memory address of a variable in C++?",
            "options": ["& (address-of operator)", "* (dereference operator)", ":: (scope resolution)", "sizeof"],
            "answer": "& (address-of operator)",
        },
        {
            "question": "Which operator performs safe explicit type conversion in modern C++?",
            "options": ["static_cast<type>(expression)", "(type)expression", "convert<type>()", "type.cast()"],
            "answer": "static_cast<type>(expression)",
        },
        {
            "question": "How does the comma operator `,` evaluate expressions separated by commas?",
            "options": [
                "Evaluates left-to-right and yields the value of the rightmost expression",
                "Evaluates right-to-left and yields the value of the leftmost expression",
                "Causes a compiler syntax error",
                "Combines all values into an array"
            ],
            "answer": "Evaluates left-to-right and yields the value of the rightmost expression",
        },
    ],
    "theory": {
        "definition": "Assignment operators update memory variables; ternary operator simplifies inline conditionals; misc operators perform casting and address retrieval.",
        "why": "Compound assignment reduces code verbosity; ternary operator streamlines assignments; static_cast ensures type safety.",
        "rules": [
            "Compound assignment: =, +=, -=, *=, /=, %=.",
            "Ternary operator: condition ? val1 : val2.",
            "Address-of operator & returns memory address.",
            "static_cast<target_type>(var) performs compile-time checked type casting.",
        ],
        "examples": [
            "num *= 2; // num = num * 2",
            "int max = (a > b) ? a : b;",
            "float f = static_cast<float>(total) / count;",
        ],
    },
}

CPP_TOPICS[10] = {
    "id": 10,
    "title": "If, If-Else & If-Else-If Statements",
    "category": "Basics",
    "difficulty": "Beginner",
    "duration": "25 min",
    "concept": "Conditional branching in C++ controls execution paths based on truth evaluation of expressions: single 'if', two-way 'if-else', multi-condition 'if-else-if' ladder, and hierarchical nested 'if-else' statements.",
    "syntax": "if (condition) {\n    // code\n} else if (cond2) {\n    // code\n} else {\n    // fallback\n}",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int marks = 82;\n    if (marks >= 90) {\n        cout << \"Grade: A+\" << endl;\n    } else if (marks >= 80) {\n        cout << \"Grade: A\" << endl;\n    } else if (marks >= 70) {\n        cout << \"Grade: B\" << endl;\n    } else {\n        cout << \"Grade: C\" << endl;\n    }\n    return 0;\n}",
        "output": "Grade: A",
        "explanation": "Evaluates conditions sequentially. Since marks >= 80 is true (82), Grade A prints and subsequent conditions are bypassed.",
    },
    "fill_blanks": {
        "question": "Complete the if-else-if ladder snippet:",
        "answers": ["if", "else if", "else"],
        "options": ["if", "else if", "else", "switch", "case"],
    },
    "compiler": {
        "title": "C++ Conditional Branching with If-Else-If",
        "question": "Arrange lines to create an if-else-if condition check for number positivity.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int n = 0;\n    if (n > 0) {\n        cout << \"Positive\" << endl;\n    } else if (n < 0) {\n        cout << \"Negative\" << endl;\n    } else {\n        cout << \"Zero\" << endl;\n    }\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int n = 0;",
            "    if (n > 0) {",
            "        cout << \"Positive\" << endl;",
            "    } else if (n < 0) {",
            "        cout << \"Negative\" << endl;",
            "    } else {",
            "        cout << \"Zero\" << endl;",
            "    }",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What condition evaluation triggers execution of an `if` block in C++?",
            "options": ["Any non-zero or true value", "Only integer 1", "Only boolean true keyword", "Negative values only"],
            "answer": "Any non-zero or true value",
        },
        {
            "question": "When does the `else` block execute in an `if-else` statement?",
            "options": [
                "When the `if` condition evaluates to false (zero)",
                "Always after the `if` block finishes",
                "Before the `if` condition is tested",
                "Only when an exception occurs"
            ],
            "answer": "When the `if` condition evaluates to false (zero)",
        },
        {
            "question": "How does an `if-else-if` ladder evaluate multiple conditions?",
            "options": [
                "Sequentially from top to bottom until the first true condition is found",
                "Evaluates all conditions simultaneously in parallel",
                "Evaluates from bottom to top",
                "Randomly selects one true condition block"
            ],
            "answer": "Sequentially from top to bottom until the first true condition is found",
        },
        {
            "question": "What is a nested `if-else` statement?",
            "options": [
                "An `if` or `else` block placed inside another `if` or `else` block",
                "An `if` statement placed inside a class definition",
                "An `if` statement compiled on multiple threads",
                "An `if` statement inside a macro"
            ],
            "answer": "An `if` or `else` block placed inside another `if` or `else` block",
        },
        {
            "question": "What happens if curly braces `{}` are omitted after an `if` condition?",
            "options": [
                "Only the single immediately following statement belongs to the `if` block",
                "The compiler throws a fatal syntax error",
                "The entire file is treated as the `if` block",
                "The `if` condition is ignored"
            ],
            "answer": "Only the single immediately following statement belongs to the `if` block",
        },
    ],
    "theory": {
        "definition": "If, if-else, and if-else-if ladder statements branch program execution along alternate code paths based on expression truth values.",
        "why": "Enables dynamic decision making, input validation, and business logic execution paths.",
        "rules": [
            "if condition evaluates non-zero as true, 0 as false.",
            "else block is optional.",
            "if-else-if ladder executes first matching true block and skips the rest.",
        ],
        "examples": [
            "if (age >= 18) { cout << \"Eligible\"; }",
            "if (num % 2 == 0) { cout << \"Even\"; } else { cout << \"Odd\"; }",
        ],
    },
}

CPP_TOPICS[11] = {
    "id": 11,
    "title": "Switch Statement & Ternary Decisioning",
    "category": "Basics",
    "difficulty": "Beginner",
    "duration": "25 min",
    "concept": "The `switch` statement performs multi-way discrete value equality checks against integral or enumeration case labels. `break` prevents fallthrough, and `default` handles unmatched cases. Ternary decisioning provides concise inline branching.",
    "syntax": "switch (expression) {\n    case const1:\n        // code\n        break;\n    case const2:\n        // code\n        break;\n    default:\n        // fallback\n        break;\n}",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    char code = 'B';\n    switch (code) {\n        case 'A':\n            cout << \"Option A selected\" << endl;\n            break;\n        case 'B':\n            cout << \"Option B selected\" << endl;\n            break;\n        default:\n            cout << \"Invalid selection\" << endl;\n            break;\n    }\n    return 0;\n}",
        "output": "Option B selected",
        "explanation": "Switch tests expression 'code' against case constants. Matches 'B', executes cout, and break terminates switch execution preventing fallthrough.",
    },
    "fill_blanks": {
        "question": "Complete the switch statement with break and default:",
        "answers": ["switch", "case", "break", "default"],
        "options": ["switch", "case", "break", "default", "if", "else"],
    },
    "compiler": {
        "title": "C++ Switch Case Execution Sandbox",
        "question": "Arrange lines to create a switch statement selecting day names.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int day = 1;\n    switch (day) {\n        case 1: cout << \"Monday\" << endl; break;\n        default: cout << \"Other\" << endl; break;\n    }\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int day = 1;",
            "    switch (day) {",
            "        case 1: cout << \"Monday\" << endl; break;",
            "        default: cout << \"Other\" << endl; break;",
            "    }",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What occurs if a `break` statement is omitted from a `case` block in a `switch` statement?",
            "options": [
                "Execution falls through into subsequent case blocks regardless of case labels",
                "The program crashes immediately",
                "The compiler outputs a mandatory syntax error",
                "The switch statement loops infinitely"
            ],
            "answer": "Execution falls through into subsequent case blocks regardless of case labels",
        },
        {
            "question": "Which data types are valid expression types for a C++ `switch` statement?",
            "options": ["Integral types (int, char, enum)", "Floating-point types (float, double)", "Strings (std::string)", "Pointers to functions"],
            "answer": "Integral types (int, char, enum)",
        },
        {
            "question": "When does the `default` block inside a `switch` statement execute?",
            "options": [
                "When none of the defined `case` values match the switch expression",
                "Always before any `case` statements",
                "Only when an unhandled exception is thrown",
                "When the switch expression evaluates to true"
            ],
            "answer": "When none of the defined `case` values match the switch expression",
        },
        {
            "question": "What restriction applies to `case` label values in a C++ `switch` statement?",
            "options": [
                "Case values must be compile-time constant integral expressions",
                "Case values must be dynamic variables",
                "Case values can be floating-point numbers",
                "Case values must be string literals"
            ],
            "answer": "Case values must be compile-time constant integral expressions",
        },
        {
            "question": "Why can `switch` statements execute faster than long `if-else-if` ladders?",
            "options": [
                "Compilers can optimize `switch` statements into efficient jump tables",
                "`switch` statements run on GPU hardware",
                "`switch` statements skip syntax validation",
                "`switch` statements inline all function calls"
            ],
            "answer": "Compilers can optimize `switch` statements into efficient jump tables",
        },
    ],
    "theory": {
        "definition": "A switch statement evaluates an integral expression against discrete constant case values for efficient multi-way branching.",
        "why": "Provides clean readability and optimal compiler jump-table execution for menu selection and dispatching discrete states.",
        "rules": [
            "Switch condition must evaluate to integral type (int, char, enum).",
            "Case values must be compile-time constant literals.",
            "break statement exits switch; without break execution falls through.",
            "default handles unmatched fallback options.",
        ],
        "examples": [
            "switch (op) { case '+': res = a+b; break; case '-': res = a-b; break; }",
        ],
    },
}

CPP_TOPICS[12] = {
    "id": 12,
    "title": "For Loop",
    "category": "Basics",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "The `for` loop is an entry-controlled loop used when the number of iterations is known prior to execution. Consists of 3 header expressions: Initialization, Condition, and Update step.",
    "syntax": "for (initialization; condition; update) {\n    // loop body\n}",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int sum = 0;\n    for (int i = 1; i <= 5; i++) {\n        sum += i;\n        cout << \"Iteration \" << i << \", sum = \" << sum << endl;\n    }\n    cout << \"Final Sum: \" << sum << endl;\n    return 0;\n}",
        "output": "Iteration 1, sum = 1\nIteration 2, sum = 3\nIteration 3, sum = 6\nIteration 4, sum = 10\nIteration 5, sum = 15\nFinal Sum: 15",
        "explanation": "Initializes i = 1. Evaluates i <= 5. Executes body adding i to sum, then increments i. Terminates when i = 6.",
    },
    "fill_blanks": {
        "question": "Complete the for loop header and increment step:",
        "answers": ["for", "int", "++"],
        "options": ["for", "int", "++", "while", "do"],
    },
    "compiler": {
        "title": "C++ For Loop Iteration Sandbox",
        "question": "Arrange lines to write a for loop printing even numbers from 2 to 6.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    for (int i = 2; i <= 6; i += 2) {\n        cout << \"i = \" << i << endl;\n    }\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    for (int i = 2; i <= 6; i += 2) {",
            "        cout << \"i = \" << i << endl;",
            "    }",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "Is the `for` loop an entry-controlled or exit-controlled loop in C++?",
            "options": [
                "Entry-controlled loop (condition is evaluated before executing body)",
                "Exit-controlled loop (condition is evaluated after body executes)",
                "Non-controlled loop",
                "Asynchronous loop"
            ],
            "answer": "Entry-controlled loop (condition is evaluated before executing body)",
        },
        {
            "question": "What is the order of execution of components in a `for (init; cond; update)` loop?",
            "options": [
                "1. Init -> 2. Condition -> 3. Loop Body -> 4. Update",
                "1. Condition -> 2. Init -> 3. Update -> 4. Body",
                "1. Body -> 2. Init -> 3. Update -> 4. Condition",
                "1. Update -> 2. Condition -> 3. Init -> 4. Body"
            ],
            "answer": "1. Init -> 2. Condition -> 3. Loop Body -> 4. Update",
        },
        {
            "question": "How many iterations does `for (int i = 0; i < 5; i++)` perform?",
            "options": ["5 iterations (i = 0, 1, 2, 3, 4)", "6 iterations", "4 iterations", "0 iterations"],
            "answer": "5 iterations (i = 0, 1, 2, 3, 4)",
        },
        {
            "question": "Which construct creates a valid infinite `for` loop in C++?",
            "options": ["for (;;)", "for (0; 0; 0)", "for (while)", "for (int i = 0)"],
            "answer": "for (;;)",
        },
        {
            "question": "What happens if the condition in a `for` loop evaluates to false on the initial check?",
            "options": [
                "The loop body never executes (0 iterations)",
                "The loop body executes exactly once",
                "A compile runtime error occurs",
                "The compiler throws a warning"
            ],
            "answer": "The loop body never executes (0 iterations)",
        },
    ],
    "theory": {
        "definition": "A for loop is an entry-controlled loop executing a code block repeatedly based on initialization, condition, and update expressions.",
        "why": "Ideal when the exact number of iterations is known in advance (counting loops, array indexing).",
        "rules": [
            "Header format: for (init; condition; update).",
            "Initialization runs once at the beginning.",
            "Condition is evaluated before each iteration.",
            "Update step executes after each body completion.",
        ],
        "examples": [
            "for (int i = 0; i < 10; ++i) { cout << i; }",
        ],
    },
}

CPP_TOPICS[13] = {
    "id": 13,
    "title": "While Loop",
    "category": "Basics",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "The `while` loop is an entry-controlled loop that executes as long as a specified condition remains true. Suited for condition-driven iterations where iteration count is indeterminate.",
    "syntax": "while (condition) {\n    // loop body\n    // update state\n}",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int num = 1234, reverse = 0;\n    while (num > 0) {\n        int digit = num % 10;\n        reverse = reverse * 10 + digit;\n        num /= 10;\n    }\n    cout << \"Reversed Number: \" << reverse << endl;\n    return 0;\n}",
        "output": "Reversed Number: 4321",
        "explanation": "Executes while num > 0. Extracts last digit using modulo %, appends to reverse, and divides num by 10 until num becomes 0.",
    },
    "fill_blanks": {
        "question": "Complete the while loop condition and division update snippet:",
        "answers": ["while", ">", "/="],
        "options": ["while", ">", "/=", "for", "do"],
    },
    "compiler": {
        "title": "C++ While Loop Execution Sandbox",
        "question": "Arrange lines to create a while loop counting down from 3 to 1.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int count = 3;\n    while (count > 0) {\n        cout << \"Count: \" << count << endl;\n        count--;\n    }\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int count = 3;",
            "    while (count > 0) {",
            "        cout << \"Count: \" << count << endl;",
            "        count--;",
            "    }",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "When is a `while` loop preferred over a `for` loop?",
            "options": [
                "When the number of iterations is unknown in advance and depends on a dynamic condition",
                "When counting from 1 to 100",
                "When iterating over fixed-size arrays",
                "When defining class member functions"
            ],
            "answer": "When the number of iterations is unknown in advance and depends on a dynamic condition",
        },
        {
            "question": "Where is the condition evaluated in a standard `while` loop?",
            "options": [
                "At the top of the loop before executing the body",
                "At the bottom after executing the body",
                "In a separate thread",
                "Only when the loop terminates"
            ],
            "answer": "At the top of the loop before executing the body",
        },
        {
            "question": "What happens if the condition variable inside a `while` loop is never modified?",
            "options": [
                "The loop becomes an infinite loop",
                "The loop automatically terminates after 100 iterations",
                "The compiler converts it to a for loop",
                "The program throws a compile error"
            ],
            "answer": "The loop becomes an infinite loop",
        },
        {
            "question": "How many times does `int x = 10; while (x < 5) { x++; }` run?",
            "options": ["0 times", "10 times", "5 times", "1 time"],
            "answer": "0 times",
        },
        {
            "question": "Which idiom creates a standard infinite `while` loop in C++?",
            "options": ["while (true)", "while (0)", "while (false)", "while ()"],
            "answer": "while (true)",
        },
    ],
    "theory": {
        "definition": "A while loop is an entry-controlled loop that continues executing as long as its condition evaluates to true.",
        "why": "Essential for processing data streams, event handling, and algorithm loops with unknown termination criteria.",
        "rules": [
            "Condition is evaluated before each iteration.",
            "Body must update state to avoid infinite looping.",
            "If condition is initially false, body executes 0 times.",
        ],
        "examples": [
            "while (cin >> value) { process(value); }",
        ],
    },
}

CPP_TOPICS[14] = {
    "id": 14,
    "title": "Do-While Loop",
    "category": "Basics",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "The `do-while` loop is an exit-controlled loop that evaluates its condition after executing the loop body. Guarantees that the loop body will execute **at least once**. Requires a ending semicolon `;` after the `while(condition)` expression.",
    "syntax": "do {\n    // loop body\n} while (condition);",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int option = 0;\n    do {\n        cout << \"Menu: [1] Start, [0] Exit\" << endl;\n        // Simulating user choosing 0 to exit\n        option = 0;\n    } while (option != 0);\n    cout << \"Program Exited Successfully.\" << endl;\n    return 0;\n}",
        "output": "Menu: [1] Start, [0] Exit\nProgram Exited Successfully.",
        "explanation": "Executes menu body first. Checks condition (option != 0). Since option is 0, condition is false and loop exits after running once.",
    },
    "fill_blanks": {
        "question": "Complete the do-while loop syntax with ending semicolon:",
        "answers": ["do", "while", ";"],
        "options": ["do", "while", ";", ":", "for"],
    },
    "compiler": {
        "title": "C++ Do-While Loop Sandbox",
        "question": "Arrange lines to create a do-while loop that executes once.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int val = 100;\n    do {\n        cout << \"Running at least once, val = \" << val << endl;\n    } while (val < 10);\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int val = 100;",
            "    do {",
            "        cout << \"Running at least once, val = \" << val << endl;",
            "    } while (val < 10);",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What is the key distinguishing property of a `do-while` loop?",
            "options": [
                "It is exit-controlled and guarantees at least one execution of the body",
                "It runs faster than a standard for loop",
                "It does not support break or continue statements",
                "It can only run with integer conditions"
            ],
            "answer": "It is exit-controlled and guarantees at least one execution of the body",
        },
        {
            "question": "What mandatory syntax character must follow `while(condition)` at the end of a `do-while` loop?",
            "options": ["; (semicolon)", ": (colon)", "} (closing brace)", "no character required"],
            "answer": "; (semicolon)",
        },
        {
            "question": "How many times does `int x = 50; do { x++; } while (x < 10);` execute?",
            "options": ["1 time", "0 times", "50 times", "Infinitely"],
            "answer": "1 time",
        },
        {
            "question": "Why is a `do-while` loop commonly used for menu-driven CLI applications?",
            "options": [
                "Because the menu must display at least once before checking user exit input",
                "Because `do-while` loops automatically handle user keyboard inputs",
                "Because it consumes zero RAM memory",
                "Because it prevents invalid user input"
            ],
            "answer": "Because the menu must display at least once before checking user exit input",
        },
        {
            "question": "If the condition in a `do-while` loop evaluates to false on the first check, how many times does the body run?",
            "options": ["1 time", "0 times", "2 times", "Compiler error"],
            "answer": "1 time",
        },
    ],
    "theory": {
        "definition": "A do-while loop is an exit-controlled loop that executes its body first before evaluating the truth condition.",
        "why": "Ensures initial execution pass for interactive menus, user prompts, and retry mechanisms.",
        "rules": [
            "Exit-controlled flow guarantees body runs >= 1 time.",
            "Syntax requirement: MUST terminate with semicolon after while(cond);.",
        ],
        "examples": [
            "do { promptUser(); } while (!validInput());",
        ],
    },
}

CPP_TOPICS[15] = {
    "id": 15,
    "title": "Range-Based For Loop & Loop Control",
    "category": "Basics",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "Modern C++11 Range-based `for` loop (`for (auto &x : collection)`) simplifies iterating over elements in arrays or containers without manual indexing. Loop control statements `break` (terminates loop immediately) and `continue` (skips remainder of current iteration).",
    "syntax": "for (auto &elem : collection) {\n    if (skipCond) continue;\n    if (stopCond) break;\n}",
    "example": {
        "code": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nint main() {\n    vector<int> nums = {1, 2, 3, 4, 5, 6};\n    cout << \"Range-based loop with break/continue: \";\n    for (int val : nums) {\n        if (val == 3) continue; // Skip 3\n        if (val == 5) break;    // Stop at 5\n        cout << val << \" \";\n    }\n    cout << endl;\n    return 0;\n}",
        "output": "Range-based loop with break/continue: 1 2 4 ",
        "explanation": "Iterates through nums vector. When val == 3, continue skips printing. When val == 5, break exits loop immediately.",
    },
    "fill_blanks": {
        "question": "Complete the range-based for loop with reference and break/continue statements:",
        "answers": ["for", "auto", "continue", "break"],
        "options": ["for", "auto", "continue", "break", "while", "do"],
    },
    "compiler": {
        "title": "C++ Range-Based For Loop & Loop Control Sandbox",
        "question": "Arrange lines to write a range-based for loop over an array with break.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int arr[] = {10, 20, 30, 40};\n    for (int x : arr) {\n        if (x == 30) break;\n        cout << \"x = \" << x << endl;\n    }\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int arr[] = {10, 20, 30, 40};",
            "    for (int x : arr) {",
            "        if (x == 30) break;",
            "        cout << \"x = \" << x << endl;",
            "    }",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What feature was introduced in C++11 to iterate over collections without explicit index counters?",
            "options": [
                "Range-based `for` loop",
                "Pointer arithmetic loop",
                "Thread iteration loop",
                "Lambda loop"
            ],
            "answer": "Range-based `for` loop",
        },
        {
            "question": "What is the benefit of passing elements by reference `for (auto &x : collection)` in a range-based for loop?",
            "options": [
                "Allows modifying collection elements directly and avoids element copying overhead",
                "Makes the loop run in parallel",
                "Prevents modifying element values",
                "Forces elements to become constant"
            ],
            "answer": "Allows modifying collection elements directly and avoids element copying overhead",
        },
        {
            "question": "What action does the `break` statement perform inside a loop?",
            "options": [
                "Immediately terminates the loop and transfers execution to statement following loop",
                "Skips current iteration and moves to next element",
                "Restarts the loop from index 0",
                "Pauses execution for 1 second"
            ],
            "answer": "Immediately terminates the loop and transfers execution to statement following loop",
        },
        {
            "question": "What action does the `continue` statement perform inside a loop?",
            "options": [
                "Skips the remainder of current iteration and jumps directly to next iteration / condition check",
                "Terminates the loop entirely",
                "Exits the current function",
                "Throws a runtime exception"
            ],
            "answer": "Skips the remainder of current iteration and jumps directly to next iteration / condition check",
        },
        {
            "question": "What is the correct syntax for a range-based `for` loop over array `int arr[] = {5, 10, 15}`?",
            "options": ["for (int x : arr)", "for (int x in arr)", "foreach (arr as x)", "for (x -> arr)"],
            "answer": "for (int x : arr)",
        },
    ],
    "theory": {
        "definition": "Range-based for loop iterates over sequence containers; break and continue control loop execution flow.",
        "why": "Eliminates index out-of-bound errors, simplifies code syntax, and enables precise control over iteration logic.",
        "rules": [
            "Syntax: for (range_declaration : range_expression).",
            "Use reference auto &x to modify elements or prevent copy overhead.",
            "break exits loop immediately.",
            "continue skips remaining statements in current iteration.",
        ],
        "examples": [
            "for (const auto &item : vec) { cout << item << endl; }",
            "for (int x : arr) { if (x < 0) continue; process(x); }",
        ],
    },
}


