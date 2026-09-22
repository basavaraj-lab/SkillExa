"""C++ Programming Curriculum Catalog and Content Builder for 73 topics across 12 modules."""
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
    {"id": 16, "title": "Functions", "difficulty": "Intermediate", "duration": "30 min", "category": "Functions"},
    {"id": 17, "title": "Function Overloading", "difficulty": "Intermediate", "duration": "30 min", "category": "Functions"},
    {"id": 18, "title": "Parameter Passing", "difficulty": "Intermediate", "duration": "30 min", "category": "Functions"},
    {"id": 19, "title": "Default Arguments", "difficulty": "Intermediate", "duration": "20 min", "category": "Functions"},
    {"id": 20, "title": "Inline Functions", "difficulty": "Intermediate", "duration": "25 min", "category": "Functions"},
    {"id": 21, "title": "Recursion", "difficulty": "Intermediate", "duration": "35 min", "category": "Functions"},
    {"id": 22, "title": "Lambda Expressions", "difficulty": "Advanced", "duration": "35 min", "category": "Functions"},

    # 3. Arrays and Strings
    {"id": 23, "title": "Arrays", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays and Strings"},
    {"id": 24, "title": "Multidimensional Arrays", "difficulty": "Intermediate", "duration": "35 min", "category": "Arrays and Strings"},
    {"id": 25, "title": "Strings", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays and Strings"},
    {"id": 26, "title": "String Class", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays and Strings"},
    {"id": 27, "title": "String Functions", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays and Strings"},

    # 4. Pointers and References
    {"id": 28, "title": "Pointers", "difficulty": "Intermediate", "duration": "40 min", "category": "Pointers and References"},
    {"id": 29, "title": "References", "difficulty": "Intermediate", "duration": "30 min", "category": "Pointers and References"},
    {"id": 30, "title": "References vs Pointers", "difficulty": "Advanced", "duration": "35 min", "category": "Pointers and References"},

    # 5. User-Defined Data Types
    {"id": 31, "title": "Structures", "difficulty": "Intermediate", "duration": "35 min", "category": "User-Defined Data Types"},
    {"id": 32, "title": "Unions", "difficulty": "Intermediate", "duration": "30 min", "category": "User-Defined Data Types"},
    {"id": 33, "title": "Enumeration (enum)", "difficulty": "Intermediate", "duration": "25 min", "category": "User-Defined Data Types"},
    {"id": 34, "title": "typedef and using", "difficulty": "Intermediate", "duration": "25 min", "category": "User-Defined Data Types"},

    # 6. Dynamic Memory Management
    {"id": 35, "title": "Dynamic Memory Allocation", "difficulty": "Advanced", "duration": "35 min", "category": "Dynamic Memory Management"},
    {"id": 36, "title": "new and delete", "difficulty": "Advanced", "duration": "35 min", "category": "Dynamic Memory Management"},
    {"id": 37, "title": "Memory Leaks", "difficulty": "Advanced", "duration": "30 min", "category": "Dynamic Memory Management"},

    # 7. Object-Oriented Programming (OOP)
    {"id": 38, "title": "Object-Oriented Programming (OOP)", "difficulty": "Intermediate", "duration": "35 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 39, "title": "Classes and Objects", "difficulty": "Intermediate", "duration": "40 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 40, "title": "Constructors", "difficulty": "Intermediate", "duration": "35 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 41, "title": "Encapsulation", "difficulty": "Intermediate", "duration": "30 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 42, "title": "Polymorphism", "difficulty": "Advanced", "duration": "45 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 43, "title": "Inheritance", "difficulty": "Advanced", "duration": "40 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 44, "title": "Abstraction", "difficulty": "Advanced", "duration": "35 min", "category": "Object-Oriented Programming (OOP)"},

    # 8. Templates & Standard Template Library (STL)
    {"id": 45, "title": "Templates", "difficulty": "Advanced", "duration": "40 min", "category": "Templates & STL"},
    {"id": 46, "title": "Standard Template Library (STL)", "difficulty": "Advanced", "duration": "45 min", "category": "Templates & STL"},
    {"id": 47, "title": "Algorithms", "difficulty": "Advanced", "duration": "35 min", "category": "Templates & STL"},
    {"id": 48, "title": "Containers", "difficulty": "Advanced", "duration": "40 min", "category": "Templates & STL"},
    {"id": 49, "title": "Iterators", "difficulty": "Advanced", "duration": "30 min", "category": "Templates & STL"},
    {"id": 50, "title": "Vector", "difficulty": "Advanced", "duration": "35 min", "category": "Templates & STL"},
    {"id": 51, "title": "Stack", "difficulty": "Advanced", "duration": "30 min", "category": "Templates & STL"},
    {"id": 52, "title": "Queue", "difficulty": "Advanced", "duration": "30 min", "category": "Templates & STL"},
    {"id": 53, "title": "Map", "difficulty": "Advanced", "duration": "35 min", "category": "Templates & STL"},
    {"id": 54, "title": "Set", "difficulty": "Advanced", "duration": "30 min", "category": "Templates & STL"},

    # 9. Exception Handling
    {"id": 55, "title": "Exception Handling", "difficulty": "Intermediate", "duration": "30 min", "category": "Exception Handling"},
    {"id": 56, "title": "Exception Handling Using Classes", "difficulty": "Advanced", "duration": "35 min", "category": "Exception Handling"},
    {"id": 57, "title": "Stack Unwinding", "difficulty": "Advanced", "duration": "30 min", "category": "Exception Handling"},
    {"id": 58, "title": "User-Defined Exceptions", "difficulty": "Advanced", "duration": "35 min", "category": "Exception Handling"},

    # 10. File Handling
    {"id": 59, "title": "Files and Streams", "difficulty": "Intermediate", "duration": "35 min", "category": "File Handling"},
    {"id": 60, "title": "I/O Redirection", "difficulty": "Advanced", "duration": "30 min", "category": "File Handling"},

    # 11. Multithreading
    {"id": 61, "title": "Introduction to Multithreading", "difficulty": "Advanced", "duration": "30 min", "category": "Multithreading"},
    {"id": 62, "title": "Creating Threads", "difficulty": "Advanced", "duration": "35 min", "category": "Multithreading"},
    {"id": 63, "title": "std::thread::join()", "difficulty": "Advanced", "duration": "30 min", "category": "Multithreading"},
    {"id": 64, "title": "Detaching a Thread", "difficulty": "Advanced", "duration": "30 min", "category": "Multithreading"},
    {"id": 65, "title": "Mutex", "difficulty": "Advanced", "duration": "35 min", "category": "Multithreading"},
    {"id": 66, "title": "Lock Guard", "difficulty": "Advanced", "duration": "30 min", "category": "Multithreading"},
    {"id": 67, "title": "Race Conditions", "difficulty": "Advanced", "duration": "35 min", "category": "Multithreading"},
    {"id": 68, "title": "Thread Synchronization", "difficulty": "Advanced", "duration": "40 min", "category": "Multithreading"},

    # 12. Advanced Concepts
    {"id": 69, "title": "Preprocessor", "difficulty": "Intermediate", "duration": "25 min", "category": "Advanced Concepts"},
    {"id": 70, "title": "Namespaces", "difficulty": "Intermediate", "duration": "30 min", "category": "Advanced Concepts"},
    {"id": 71, "title": "Smart Pointers", "difficulty": "Advanced", "duration": "40 min", "category": "Advanced Concepts"},
    {"id": 72, "title": "Callbacks", "difficulty": "Advanced", "duration": "35 min", "category": "Advanced Concepts"},
    {"id": 73, "title": "Signal Handling", "difficulty": "Advanced", "duration": "30 min", "category": "Advanced Concepts"},


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

CPP_TOPICS[16] = {
    "id": 16,
    "title": "Functions",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "A function is a reusable block of code that performs a specific task, dividing programs into smaller logical units for readability, maintenance, and code reuse. C++ functions consist of a return type, function name, parameter list, and function body. Function declarations (prototypes) introduce signatures to the compiler, while definitions provide body implementations. Functions can be built-in library functions (e.g. sqrt(), abs(), getline()) or user-defined functions.",
    "syntax": "// Declaration prototype\nint square(int x);\n\n// Definition\nint square(int x) {\n    return x * x;\n}\n\n// Void parameterless function\nvoid greet() {\n    cout << \"Welcome!\" << endl;\n}",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\n// Function definition\nint square(int x) {\n    return x * x;\n}\n\nvoid greet() {\n    cout << \"Welcome to C++ Programming!\" << endl;\n}\n\nint multiply(int a, int b) {\n    return a * b;\n}\n\nint main() {\n    greet();\n    int sq = square(5);\n    cout << \"Square of 5 is: \" << sq << endl;\n    \n    int prod = multiply(4, 5);\n    cout << \"Multiplication result: \" << prod << endl;\n    return 0;\n}",
        "output": "Welcome to C++ Programming!\nSquare of 5 is: 25\nMultiplication result: 20",
        "explanation": "greet() is a void parameterless function. square(int) accepts one integer parameter and returns its square. multiply(int, int) accepts two parameters and returns their product.",
    },
    "fill_blanks": {
        "question": "Complete the C++ function definition and return statement:",
        "answers": ["int", "return", "void"],
        "options": ["int", "return", "void", "include", "cin"],
    },
    "compiler": {
        "title": "C++ Function Declaration and Execution",
        "question": "Arrange lines to declare, define, and call a function computing area of a rectangle.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint getArea(int width, int height) {\n    return width * height;\n}\n\nint main() {\n    int area = getArea(5, 10);\n    cout << \"Area: \" << area << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int getArea(int width, int height) {",
            "    return width * height;",
            "}",
            "int main() {",
            "    int area = getArea(5, 10);",
            "    cout << \"Area: \" << area << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What keyword is used as the return type for a C++ function that does not return any value?",
            "options": ["void", "int", "null", "empty"],
            "answer": "void",
        },
        {
            "question": "What is the primary distinction between a function declaration (prototype) and a function definition in C++?",
            "options": [
                "Declaration introduces function signature without body; definition contains the body implementation",
                "Declaration runs at runtime; definition runs at compile time",
                "Declaration is optional for all C++ functions; definition is never required",
                "Declaration can only exist inside the main() function"
            ],
            "answer": "Declaration introduces function signature without body; definition contains the body implementation",
        },
        {
            "question": "Why must a function be declared or defined before its first invocation in main()?",
            "options": [
                "So the compiler can recognize its identifier name, parameter types, and return type for type checking",
                "To allocate dynamic heap memory for variables",
                "To optimize CPU cache speed",
                "To export symbols to DLL files"
            ],
            "answer": "So the compiler can recognize its identifier name, parameter types, and return type for type checking",
        },
        {
            "question": "Which category of functions includes built-in functions like `sqrt()`, `abs()`, and `getline()`?",
            "options": ["Library functions", "User-defined functions", "Lambda functions", "Inline macros"],
            "answer": "Library functions",
        },
        {
            "question": "What happens if a function definition specifies a non-void return type but omits a return statement?",
            "options": [
                "Causes undefined behavior or compiler warning/error",
                "Automatically returns integer 0",
                "Automatically returns NULL string",
                "Converts function to void type"
            ],
            "answer": "Causes undefined behavior or compiler warning/error",
        },
    ],
    "theory": {
        "definition": "A function is a named block of code that performs a specific operation and optionally returns a value.",
        "why": "Functions promote code reusability, modular architecture, easy debugging, and eliminate code duplication.",
        "rules": [
            "Structure: return_type function_name(parameter_list) { body }.",
            "Use void return type when no value is returned.",
            "Function prototypes specify signature ending with a semicolon.",
            "Arguments passed in calls must match parameter types in definition.",
        ],
        "examples": [
            "int add(int a, int b) { return a + b; }",
            "void logMessage(string msg) { cout << msg; }",
        ],
    },
}

CPP_TOPICS[17] = {
    "id": 17,
    "title": "Function Overloading",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "Function overloading allows defining multiple functions with the same name but different parameter lists (different number of parameters, different data types of parameters, or both). The compiler resolves overloading at compile-time by matching argument signatures. Functions CANNOT be overloaded based on return type alone, nor can they differ only in pass-by-value vs pass-by-reference due to call ambiguity.",
    "syntax": "int add(int a, int b);\nint add(int a, int b, int c);\ndouble add(double a, double b);",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\n// 1. Overload by number of parameters\nint add(int a, int b) {\n    return a + b;\n}\nint add(int a, int b, int c) {\n    return a + b + c;\n}\n\n// 2. Overload by data type of parameters\ndouble add(double a, double b) {\n    return a + b;\n}\n\nint main() {\n    cout << \"Add 2 ints (5, 7): \" << add(5, 7) << endl;\n    cout << \"Add 3 ints (5, 7, 11): \" << add(5, 7, 11) << endl;\n    cout << \"Add 2 doubles (5.3, 6.2): \" << add(5.3, 6.2) << endl;\n    return 0;\n}",
        "output": "Add 2 ints (5, 7): 12\nAdd 3 ints (5, 7, 11): 23\nAdd 2 doubles (5.3, 6.2): 11.5",
        "explanation": "Compiler evaluates call signatures: add(5, 7) selects 2-int overload; add(5, 7, 11) selects 3-int overload; add(5.3, 6.2) selects double overload.",
    },
    "fill_blanks": {
        "question": "Complete the overloaded function headers snippet:",
        "answers": ["int", "double", "add"],
        "options": ["int", "double", "add", "void", "return"],
    },
    "compiler": {
        "title": "C++ Function Overloading Sandbox",
        "question": "Arrange lines to create overloaded multiply functions for 2 and 3 integer inputs.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint multiply(int a, int b) { return a * b; }\nint multiply(int a, int b, int c) { return a * b * c; }\n\nint main() {\n    cout << multiply(10, 2) << endl;\n    cout << multiply(5, 6, 4) << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int multiply(int a, int b) { return a * b; }",
            "int multiply(int a, int b, int c) { return a * b * c; }",
            "int main() {",
            "    cout << multiply(10, 2) << endl;",
            "    cout << multiply(5, 6, 4) << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "Can functions in C++ be overloaded solely by changing their return type?",
            "options": [
                "No, because return type is not included in function call resolution and causes compiler ambiguity",
                "Yes, return type is the main criteria for overloading",
                "Yes, but only for floating-point return types",
                "Yes, if used inside classes"
            ],
            "answer": "No, because return type is not included in function call resolution and causes compiler ambiguity",
        },
        {
            "question": "What are the 3 valid ways to overload a function in C++?",
            "options": [
                "Different number of parameters, different types of parameters, or different number and types of parameters",
                "Different return types, different access specifiers, or different inline keywords",
                "Different variable names, different file locations, or different header imports",
                "Different namespaces, different macro definitions, or different static storage"
            ],
            "answer": "Different number of parameters, different types of parameters, or different number and types of parameters",
        },
        {
            "question": "At what stage does C++ resolve which overloaded function to execute?",
            "options": ["Compile-time (Static binding)", "Runtime (Dynamic binding)", "Link-time only", "Pre-processor phase"],
            "answer": "Compile-time (Static binding)",
        },
        {
            "question": "Why are functions with `(int a)` and `(int &a)` parameters invalid for overloading?",
            "options": [
                "They cause call ambiguity during compiler resolution when passing an integer variable",
                "References are not supported in C++",
                "Integers cannot be passed by reference",
                "It violates pointer alignment"
            ],
            "answer": "They cause call ambiguity during compiler resolution when passing an integer variable",
        },
        {
            "question": "What is the key difference between Function Overloading and Function Overriding?",
            "options": [
                "Overloading uses same name with different parameters in same scope at compile-time; overriding redefines virtual methods in inherited derived classes at runtime",
                "Overloading works at runtime; overriding works at compile-time",
                "Overloading requires virtual keywords; overriding does not",
                "There is no difference between overloading and overriding"
            ],
            "answer": "Overloading uses same name with different parameters in same scope at compile-time; overriding redefines virtual methods in inherited derived classes at runtime",
        },
    ],
    "theory": {
        "definition": "Function overloading allows multiple functions in the same scope to share the same name with different parameter signatures.",
        "why": "Enhances readability and usability by allowing a single logical operation (e.g. add, print, sort) to work across different inputs.",
        "rules": [
            "Functions must differ in parameter count or parameter data types.",
            "Return type alone is NOT sufficient for overloading.",
            "Pass-by-value vs Pass-by-reference for same type creates ambiguity error.",
        ],
        "examples": [
            "int area(int side);",
            "int area(int l, int b);",
            "double area(double r);",
        ],
    },
}

CPP_TOPICS[18] = {
    "id": 18,
    "title": "Parameter Passing",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "Data passed into functions are called parameters or arguments. Formal Parameters act as placeholders in function headers, while Actual Parameters are values passed during function calls. C++ supports 3 parameter passing techniques: Pass by Value (copies argument value; local changes do not modify original variable), Pass by Reference (passes alias reference; modifies original variable directly without copy overhead), and Pass by Pointer (passes memory address; dereferences pointer * to modify original).",
    "syntax": "void byVal(int a);\nvoid byRef(int &a);\nvoid byPtr(int *a);\nbyPtr(&x);",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nvoid changeValue(int a) {\n    a = 99; // Modifies local copy only\n}\n\nvoid changeReference(int &a) {\n    a = 22; // Modifies original variable\n}\n\nvoid changePointer(int *a) {\n    *a = 55; // Modifies original variable via address\n}\n\nint main() {\n    int x = 5;\n    changeValue(x);\n    cout << \"After Pass by Value: x = \" << x << endl;\n    \n    changeReference(x);\n    cout << \"After Pass by Reference: x = \" << x << endl;\n    \n    changePointer(&x);\n    cout << \"After Pass by Pointer: x = \" << x << endl;\n    return 0;\n}",
        "output": "After Pass by Value: x = 5\nAfter Pass by Reference: x = 22\nAfter Pass by Pointer: x = 55",
        "explanation": "Pass by value keeps x unchanged at 5. Pass by reference &a modifies x to 22 directly. Pass by pointer *a dereferences &x to set x to 55.",
    },
    "fill_blanks": {
        "question": "Complete the parameter passing declarations for value, reference, and pointer:",
        "answers": ["int", "&", "*"],
        "options": ["int", "&", "*", "void", "return"],
    },
    "compiler": {
        "title": "C++ Parameter Passing Techniques Sandbox",
        "question": "Arrange lines to create a pass-by-reference function that doubles a number.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nvoid doubleNum(int &n) {\n    n = n * 2;\n}\n\nint main() {\n    int num = 10;\n    doubleNum(num);\n    cout << \"Doubled: \" << num << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "void doubleNum(int &n) {",
            "    n = n * 2;",
            "}",
            "int main() {",
            "    int num = 10;",
            "    doubleNum(num);",
            "    cout << \"Doubled: \" << num << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What is the difference between formal parameters and actual parameters?",
            "options": [
                "Formal parameters are placeholders defined in function header; actual parameters are values/arguments passed in call",
                "Formal parameters are constants; actual parameters are variables",
                "Formal parameters run at runtime; actual parameters run at compile-time",
                "There is no difference between formal and actual parameters"
            ],
            "answer": "Formal parameters are placeholders defined in function header; actual parameters are values/arguments passed in call",
        },
        {
            "question": "What happens to the original caller variable in Pass by Value when modified inside a function?",
            "options": [
                "Original variable remains unchanged because function operates on a local copy",
                "Original variable is modified in place",
                "Original variable is set to zero",
                "Compiler throws a syntax error"
            ],
            "answer": "Original variable remains unchanged because function operates on a local copy",
        },
        {
            "question": "Which parameter passing technique allows modifying original caller variables without using pointer addresses?",
            "options": [
                "Pass by Reference (`int &param`)",
                "Pass by Value (`int param`)",
                "Pass by Constant Value",
                "Pass by Macro"
            ],
            "answer": "Pass by Reference (`int &param`)",
        },
        {
            "question": "Why is Pass by Reference preferred over Pass by Value for large data structures or objects?",
            "options": [
                "Avoids memory and CPU copying overhead by passing an alias reference",
                "Makes code execute on GPU",
                "Automatically encrypts object data",
                "Prevents function calling overhead"
            ],
            "answer": "Avoids memory and CPU copying overhead by passing an alias reference",
        },
        {
            "question": "What syntax is used to pass the memory address of variable `x` to a Pass by Pointer parameter `int *p`?",
            "options": ["func(&x);", "func(*x);", "func(x&);", "func(->x);"],
            "answer": "func(&x);",
        },
    ],
    "theory": {
        "definition": "Parameter passing specifies how data arguments are transferred from caller functions into called function parameters.",
        "why": "Pass by value ensures data immutability; pass by reference/pointer allows output parameters and avoids large memory copies.",
        "rules": [
            "Pass by Value: void f(int a) (copies data).",
            "Pass by Reference: void f(int &a) (aliases original data).",
            "Pass by Pointer: void f(int *a) (passes raw memory address).",
        ],
        "examples": [
            "void swap(int &x, int &y) { int temp = x; x = y; y = temp; }",
        ],
    },
}

CPP_TOPICS[19] = {
    "id": 19,
    "title": "Default Arguments",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "A default argument is a fallback value provided for a parameter in a function declaration. If the caller omits that argument, the compiler automatically assigns the default value. Default arguments MUST be specified from right-to-left (once a parameter has a default, all parameters to its right must have defaults). They should be declared in function prototypes, cannot be modified in definitions, and must avoid ambiguity during function overloading.",
    "syntax": "double calcArea(double l, double h = 10.0);\nvoid f(int a = 10, int b = 20);",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\n// Default argument h = 10.0\ndouble calcArea(double l, double h = 10.0) {\n    return l * h;\n}\n\nvoid f(int a = 10) {\n    cout << \"Value of a: \" << a << endl;\n}\n\nint main() {\n    cout << \"Area 1 (length 5, default height 10): \" << calcArea(5) << endl;\n    cout << \"Area 2 (length 5, height 9): \" << calcArea(5, 9) << endl;\n    f();\n    f(221);\n    return 0;\n}",
        "output": "Area 1 (length 5, default height 10): 50\nArea 2 (length 5, height 9): 45\nValue of a: 10\nValue of a: 221",
        "explanation": "calcArea(5) omits height, so default h=10.0 is used (50). calcArea(5, 9) overrides height with 9 (45). f() defaults a to 10; f(221) overrides a with 221.",
    },
    "fill_blanks": {
        "question": "Complete the function prototype with default argument:",
        "answers": ["double", "10.0", "calcArea"],
        "options": ["double", "10.0", "calcArea", "void", "return"],
    },
    "compiler": {
        "title": "C++ Default Arguments Sandbox",
        "question": "Arrange lines to define a greet function with default name argument.",
        "starter_code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nvoid greetUser(string name = \"Guest\") {\n    cout << \"Hello, \" << name << \"!\" << endl;\n}\n\nint main() {\n    greetUser();\n    greetUser(\"Alex\");\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "#include <string>",
            "using namespace std;",
            "void greetUser(string name = \"Guest\") {",
            "    cout << \"Hello, \" << name << \"!\" << endl;",
            "}",
            "int main() {",
            "    greetUser();",
            "    greetUser(\"Alex\");",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "Where should default arguments be specified when a function is declared and defined separately?",
            "options": [
                "In the function declaration / prototype, not in the definition",
                "In the function definition only",
                "In both declaration and definition",
                "Inside the main() function"
            ],
            "answer": "In the function declaration / prototype, not in the definition",
        },
        {
            "question": "What rule governs the ordering of default parameters in a function declaration?",
            "options": [
                "Default arguments must be provided from rightmost parameter to left",
                "Default arguments must be provided from left to right",
                "Default arguments can be placed at any random position",
                "Only the first parameter can have a default argument"
            ],
            "answer": "Default arguments must be provided from rightmost parameter to left",
        },
        {
            "question": "Why is `void func(int x = 10, int y);` invalid in C++?",
            "options": [
                "Because parameter `y` to the right of default parameter `x` lacks a default value",
                "Because `x` cannot be an integer",
                "Because default values must be floats",
                "Because `func` must return a value"
            ],
            "answer": "Because parameter `y` to the right of default parameter `x` lacks a default value",
        },
        {
            "question": "What happens when a call `calcArea(5)` is made to `double calcArea(double l, double h = 10.0)`?",
            "options": [
                "Value 5 is passed for `l`, and default value 10.0 is automatically assigned to `h`",
                "Value 5 is passed for `h`, and `l` is set to zero",
                "The function call fails with missing parameter error",
                "The program loops infinitely"
            ],
            "answer": "Value 5 is passed for `l`, and default value 10.0 is automatically assigned to `h`",
        },
        {
            "question": "Can default argument values be redefined or modified in the function definition?",
            "options": [
                "No, redefining default values in the definition causes a compile error",
                "Yes, definitions take precedence over declarations",
                "Yes, if the values are numeric constants",
                "Yes, if using inline functions"
            ],
            "answer": "No, redefining default values in the definition causes a compile error",
        },
    ],
    "theory": {
        "definition": "Default arguments provide default parameter values used when arguments are omitted in function calls.",
        "why": "Reduces boilerplate function overloading code for optional parameters while simplifying function call interfaces.",
        "rules": [
            "Must be specified in declaration prototype.",
            "Must be supplied from rightmost parameter to left.",
            "Cannot be modified or duplicated in function definition.",
        ],
        "examples": [
            "void display(int a = 1, double b = 2.5);",
        ],
    },
}

CPP_TOPICS[20] = {
    "id": 20,
    "title": "Inline Functions",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "An `inline` function is a hint to the compiler to substitute function call sites with the function's body to eliminate function call overhead. Useful for small, frequently called functions. Inline specifiers relax the C++ One Definition Rule (ODR), allowing header definitions across multiple translation units. Compilers may ignore `inline` for complex functions with loops/recursion, or inline non-inline functions automatically.",
    "syntax": "inline int getSum(int a, int b) {\n    return a + b;\n}",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\ninline int getSum(int a, int b) {\n    return a + b;\n}\n\ninline void displayMessage() {\n    for (int i = 0; i < 3; i++) {\n        cout << \"Hello \" << i << endl;\n    }\n}\n\nint main() {\n    int result = getSum(5, 10);\n    cout << \"Sum: \" << result << endl;\n    displayMessage();\n    return 0;\n}",
        "output": "Sum: 15\nHello 0\nHello 1\nHello 2",
        "explanation": "getSum() is declared inline for small addition. displayMessage() contains a loop; although marked inline, compiler may choose whether to physically inline it.",
    },
    "fill_blanks": {
        "question": "Complete the inline function definition snippet:",
        "answers": ["inline", "int", "return"],
        "options": ["inline", "int", "return", "macro", "define"],
    },
    "compiler": {
        "title": "C++ Inline Functions Sandbox",
        "question": "Arrange lines to create an inline function calculating the square of a number.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\ninline int square(int n) {\n    return n * n;\n}\n\nint main() {\n    cout << \"Square of 4: \" << square(4) << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "inline int square(int n) {",
            "    return n * n;",
            "}",
            "int main() {",
            "    cout << \"Square of 4: \" << square(4) << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What is the primary purpose of the `inline` keyword in C++?",
            "options": [
                "To request the compiler to substitute function call site with function body to eliminate function call overhead",
                "To make function execution asynchronous on multiple CPU cores",
                "To force variables to store in GPU memory",
                "To prevent functions from returning values"
            ],
            "answer": "To request the compiler to substitute function call site with function body to eliminate function call overhead",
        },
        {
            "question": "Is the `inline` keyword a mandatory command or a suggestion to the compiler?",
            "options": [
                "It is a compiler request/suggestion; compiler may choose not to inline based on function complexity",
                "It is a mandatory command that always forces inlining",
                "It is evaluated at runtime by the OS kernel",
                "It is ignored completely by all modern compilers"
            ],
            "answer": "It is a compiler request/suggestion; compiler may choose not to inline based on function complexity",
        },
        {
            "question": "How do inline functions differ from `#define` preprocessor macros?",
            "options": [
                "Inline functions perform type checking, respect C++ scope rules, and evaluate arguments only once",
                "Macros perform compile-time type checking",
                "Inline functions are expanded by preprocessor",
                "Macros support function recursion"
            ],
            "answer": "Inline functions perform type checking, respect C++ scope rules, and evaluate arguments only once",
        },
        {
            "question": "What role does `inline` play regarding the C++ One Definition Rule (ODR)?",
            "options": [
                "Allows function definitions to appear in multiple translation units when included via header files",
                "Prohibits header files from containing function definitions",
                "Forces functions to be declared in single source files only",
                "Restricts function calls to same class scope"
            ],
            "answer": "Allows function definitions to appear in multiple translation units when included via header files",
        },
        {
            "question": "What is a potential disadvantage of excessive inlining in a large C++ codebase?",
            "options": [
                "Increases compiled binary executable size and may degrade CPU instruction cache performance",
                "Slows down runtime loop execution speed",
                "Causes memory leak errors on stack",
                "Prevents template specialization"
            ],
            "answer": "Increases compiled binary executable size and may degrade CPU instruction cache performance",
        },
    ],
    "theory": {
        "definition": "An inline function requests the compiler to expand code directly at the call site, eliminating function-call stack overhead.",
        "why": "Optimizes small, high-frequency functions and enables header function definitions adhering to One Definition Rule (ODR).",
        "rules": [
            "Use inline for small 1-3 line functions.",
            "Inline functions preserve scope and type safety (unlike macros).",
            "Compiler decides whether to honor inline request.",
        ],
        "examples": [
            "inline int max(int a, int b) { return (a > b) ? a : b; }",
        ],
    },
}

CPP_TOPICS[21] = {
    "id": 21,
    "title": "Recursion",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "35 min",
    "concept": "Recursion is a programming technique where a function calls itself repeatedly to solve sub-problems. Must contain a Base Condition (stops recursion to prevent stack overflow) and a Recursive Case (self-call with smaller inputs). Operates via Call Stack: Descending Phase (pushing stack frames deeper) and Ascending Phase (popping stack frames during unwinding). Applied in Divide & Conquer, Backtracking, Sorting (Merge/Quick), and Tree/Graph traversals.",
    "syntax": "void recursiveFunc(int n) {\n    if (n <= 0) return; // Base condition\n    // task\n    recursiveFunc(n - 1); // Recursive case\n}",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nvoid printHello(int n) {\n    if (n == 0) return; // Base Case\n    cout << \"Hello (n=\" << n << \")\" << endl;\n    printHello(n - 1);  // Recursive Case\n}\n\nint factorial(int n) {\n    if (n <= 1) return 1;\n    return n * factorial(n - 1);\n}\n\nint main() {\n    printHello(3);\n    cout << \"Factorial of 5: \" << factorial(5) << endl;\n    return 0;\n}",
        "output": "Hello (n=3)\nHello (n=2)\nHello (n=1)\nFactorial of 5: 120",
        "explanation": "printHello(3) calls printHello(2) -> printHello(1) -> printHello(0) which hits base condition n==0 and unwinds stack. factorial(5) computes 5 * 4 * 3 * 2 * 1 = 120.",
    },
    "fill_blanks": {
        "question": "Complete the recursive factorial base case and recursive call snippet:",
        "answers": ["if", "return", "factorial"],
        "options": ["if", "return", "factorial", "while", "for"],
    },
    "compiler": {
        "title": "C++ Recursion Sandbox",
        "question": "Arrange lines to create a recursive sum function from 1 to N.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint sum(int n) {\n    if (n <= 0) return 0;\n    return n + sum(n - 1);\n}\n\nint main() {\n    cout << \"Sum 1 to 5: \" << sum(5) << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int sum(int n) {",
            "    if (n <= 0) return 0;",
            "    return n + sum(n - 1);",
            "}",
            "int main() {",
            "    cout << \"Sum 1 to 5: \" << sum(5) << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What essential component must every recursive function contain to prevent infinite execution?",
            "options": [
                "A Base Condition",
                "A for loop header",
                "A break statement",
                "A global variable"
            ],
            "answer": "A Base Condition",
        },
        {
            "question": "What runtime error occurs when a recursive function lacks a base condition or exceeds available stack memory?",
            "options": ["Stack Overflow", "Null Pointer Exception", "Segmentation Fault", "Out of Bounds Error"],
            "answer": "Stack Overflow",
        },
        {
            "question": "What happens during the ascending phase of a recursive function call stack?",
            "options": [
                "Functions return values one by one and pop their stack frames off the call stack",
                "New stack frames are pushed onto call stack",
                "Memory is dynamically allocated on heap",
                "The compiler re-compiles function"
            ],
            "answer": "Functions return values one by one and pop their stack frames off the call stack",
        },
        {
            "question": "How does stack memory management operate during deep recursive calls?",
            "options": [
                "Each self-call pushes a new stack frame containing local variables onto the call stack until base case returns",
                "Memory is allocated in static global segment",
                "All recursive calls share 1 single stack frame",
                "Stack memory is freed before calling next function"
            ],
            "answer": "Each self-call pushes a new stack frame containing local variables onto the call stack until base case returns",
        },
        {
            "question": "Name two sorting algorithms that fundamentally rely on recursive divide-and-conquer strategies.",
            "options": [
                "Merge Sort and Quick Sort",
                "Bubble Sort and Selection Sort",
                "Insertion Sort and Counting Sort",
                "Radix Sort and Bucket Sort"
            ],
            "answer": "Merge Sort and Quick Sort",
        },
    ],
    "theory": {
        "definition": "Recursion is a technique where a function solves a problem by calling itself with reduced problem instances until reaching a base condition.",
        "why": "Simplifies complex algorithms like tree/graph traversals, Tower of Hanoi, and divide-and-conquer sorting.",
        "rules": [
            "Must define a valid base condition to terminate recursive calls.",
            "Each recursive step must move closer to the base condition.",
            "Stack memory footprint grows linearly with recursion depth.",
        ],
        "examples": [
            "int fib(int n) { if (n <= 1) return n; return fib(n-1) + fib(n-2); }",
        ],
    },
}

CPP_TOPICS[22] = {
    "id": 22,
    "title": "Lambda Expressions",
    "category": "Functions",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "Lambda expressions introduced in C++11 (`[capture](params) -> return_type { body }`) are anonymous inline functions written directly at call sites. Capture clauses access outer variables: `[&]` (all by ref), `[=]` (all by val), `[a, &b]` (mixed), `[]` (empty). Value captures are `const` by default unless marked `mutable`. Widely used in STL algorithms like `std::sort` and `std::find_if`.",
    "syntax": "auto sum = [](int a, int b) { return a + b; };\n[&] { v.push_back(10); };\n[=]() mutable { val++; };",
    "example": {
        "code": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    // 1. Basic Lambda\n    auto doubleVal = [](int x) { return x * 2; };\n    cout << \"Double 5: \" << doubleVal(5) << endl;\n\n    // 2. Lambda with STL sort\n    vector<int> v = {5, 1, 8, 3, 9, 2};\n    sort(v.begin(), v.end(), [](const int &a, const int &b) {\n        return a > b; // Descending\n    });\n    cout << \"Sorted Descending: \";\n    for (int x : v) cout << x << \" \";\n    cout << endl;\n\n    // 3. Lambda with find_if\n    auto it = find_if(v.begin(), v.end(), [](int x) {\n        return x % 3 == 0;\n    });\n    if (it != v.end()) cout << \"First div by 3: \" << *it << endl;\n    return 0;\n}",
        "output": "Double 5: 10\nSorted Descending: 9 8 5 3 2 1 \nFirst div by 3: 9",
        "explanation": "Basic lambda doubles 5. sort() uses lambda predicate (a > b) to arrange numbers in descending order. find_if() uses lambda predicate (x % 3 == 0) to locate first element divisible by 3.",
    },
    "fill_blanks": {
        "question": "Complete the lambda expression and capture clause snippet:",
        "answers": ["auto", "[&]", "sort"],
        "options": ["auto", "[&]", "sort", "while", "include"],
    },
    "compiler": {
        "title": "C++ Lambda Expression Sandbox",
        "question": "Arrange lines to write a lambda expression sorting a vector in ascending order.",
        "starter_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    vector<int> nums = {4, 2, 9, 1};\n    sort(nums.begin(), nums.end(), [](int a, int b) { return a < b; });\n    for (int n : nums) cout << n << \" \";\n    cout << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "#include <vector>",
            "#include <algorithm>",
            "using namespace std;",
            "int main() {",
            "    vector<int> nums = {4, 2, 9, 1};",
            "    sort(nums.begin(), nums.end(), [](int a, int b) { return a < b; });",
            "    for (int n : nums) cout << n << \" \";",
            "    cout << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What C++ standard introduced anonymous Lambda Expressions?",
            "options": ["C++11", "C++98", "C++03", "C++20"],
            "answer": "C++11",
        },
        {
            "question": "What capture clause syntax `[capture]` captures all external scope variables by reference?",
            "options": ["[&]", "[=]", "[*]", "[]"],
            "answer": "[&]",
        },
        {
            "question": "Why is the `mutable` keyword required when modifying a variable captured by value `[=]` inside a lambda body?",
            "options": [
                "Because value-captured variables are immutable `const` by default inside lambdas",
                "To make the lambda multi-threaded",
                "To extend variable lifetime after function exits",
                "To enable virtual dispatch"
            ],
            "answer": "Because value-captured variables are immutable `const` by default inside lambdas",
        },
        {
            "question": "What does an empty capture clause `[]` signify in a C++ lambda expression?",
            "options": [
                "The lambda cannot access variables from the outer enclosing scope, using only its parameters or globals",
                "The lambda takes no parameters",
                "The lambda returns void",
                "The lambda is inline"
            ],
            "answer": "The lambda cannot access variables from the outer enclosing scope, using only its parameters or globals",
        },
        {
            "question": "How are lambdas commonly utilized alongside C++ Standard Template Library (STL) algorithms like `std::sort` and `std::find_if`?",
            "options": [
                "As inline predicate comparison functions passed directly into algorithm arguments",
                "As replacements for headers",
                "To allocate vector capacity",
                "To catch exceptions"
            ],
            "answer": "As inline predicate comparison functions passed directly into algorithm arguments",
        },
    ],
    "theory": {
        "definition": "Lambda expressions are anonymous inline function objects defined at point of use with custom capture specifications.",
        "why": "Keeps code concise and localized, eliminating the need for standalone functor structs or global function definitions.",
        "rules": [
            "Syntax: [capture](parameters) mutable -> return_type { body }.",
            "[&] captures by reference; [=] captures by value.",
            "mutable permits modifying value-captured variables inside lambda body.",
        ],
        "examples": [
            "auto isEven = [](int x) { return x % 2 == 0; };",
            "sort(v.begin(), v.end(), [](int a, int b) { return a > b; });",
        ],
    },
}

CPP_TOPICS[23] = {
    "id": 23,
    "title": "Arrays",
    "category": "Arrays and Strings",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "An array in C++ is a fixed-size collection of elements of the same data type stored in contiguous memory locations. Each element is accessed using 0-based indexing (from index 0 to size - 1). Built-in arrays have fixed sizes after declaration, and their total size and length can be determined using the sizeof operator when in scope.",
    "syntax": "// Declaration\ndata_type array_name[size];\n\n// Initialization\nint arr[5] = {2, 4, 8, 12, 16};\nint arr[] = {2, 4, 8, 12, 16}; // Inferred size\nint arr[5] = {0}; // All elements initialized to 0\n\n// Accessing & Updating\narray_name[index] = value;\n\n// Length Calculation\nint n = sizeof(arr) / sizeof(arr[0]);",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // Declaring and initializing an array of size 5\n    int arr[5] = {2, 4, 8, 12, 16};\n\n    // Updating first element\n    arr[0] = 90;\n\n    // Accessing and printing array elements\n    cout << \"Array elements: \";\n    for (int i = 0; i < 5; i++) {\n        cout << arr[i] << \" \";\n    }\n    cout << endl;\n\n    // Length of array using sizeof\n    int length = sizeof(arr) / sizeof(arr[0]);\n    cout << \"Length of array: \" << length << endl;\n\n    return 0;\n}",
        "output": "Array elements: 90 4 8 12 16 \nLength of array: 5",
        "explanation": "int arr[5] declares an array of 5 integers in contiguous memory. arr[0] = 90 updates the first element. The for loop traverses indices 0 to 4. sizeof(arr)/sizeof(arr[0]) calculates the array length.",
    },
    "fill_blanks": {
        "question": "Complete the array declaration, update, traversal, and length calculation snippet:",
        "answers": ["arr", "0", "sizeof", "5"],
        "options": ["arr", "0", "sizeof", "5", "length", "vector"],
    },
    "compiler": {
        "title": "C++ Arrays Operations Sandbox",
        "question": "Arrange lines to declare an array of 5 integers, update the first element to 90, and traverse all elements using a for loop.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int arr[5] = {2, 4, 8, 12, 16};\n    arr[0] = 90;\n    for (int i = 0; i < 5; i++) {\n        cout << arr[i] << \" \";\n    }\n    cout << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int arr[5] = {2, 4, 8, 12, 16};",
            "    arr[0] = 90;",
            "    for (int i = 0; i < 5; i++) {",
            "        cout << arr[i] << \" \";",
            "    }",
            "    cout << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What is an array in C++?",
            "options": [
                "A fixed-size collection of elements of the same data type stored in contiguous memory locations",
                "A dynamically resizing collection of elements of different data types",
                "A pointer pointing strictly to string literals",
                "A key-value data structure mapping unique keys to values"
            ],
            "answer": "A fixed-size collection of elements of the same data type stored in contiguous memory locations",
        },
        {
            "question": "What is the starting index of an array in C++?",
            "options": ["0", "1", "-1", "Depends on array size"],
            "answer": "0",
        },
        {
            "question": "Given `int arr[5] = {2, 4, 8};`, what value is automatically assigned to `arr[3]` (partial initialization)?",
            "options": ["0", "8", "Indeterminate garbage value", "12"],
            "answer": "0",
        },
        {
            "question": "How can you calculate the length (number of elements) of a built-in C++ array `arr` in scope?",
            "options": [
                "sizeof(arr) / sizeof(arr[0])",
                "arr.length()",
                "arr.size()",
                "sizeof(arr[0]) / sizeof(arr)"
            ],
            "answer": "sizeof(arr) / sizeof(arr[0])",
        },
        {
            "question": "What does `int arr[5] = {0};` achieve in C++?",
            "options": [
                "Initializes all 5 array elements to zero (0)",
                "Initializes only the first element to 0 leaving remaining elements uninitialized",
                "Throws a compile-time syntax error",
                "Allocates a dynamic array of length 0"
            ],
            "answer": "Initializes all 5 array elements to zero (0)",
        },
    ],
    "theory": {
        "definition": "An array in C++ is a fixed-size collection of elements of the same data type stored in contiguous memory locations, indexed from 0 to size - 1.",
        "why": "Arrays provide O(1) constant-time element access by index and optimal memory layout without pointer overhead.",
        "rules": [
            "Declaration syntax: data_type array_name[size];",
            "Indexing starts at 0; last valid index is size - 1.",
            "Partial initialization (e.g. {2, 4}) automatically fills remaining elements with 0.",
            "{0} initializes all array elements to zero.",
            "Update elements using assignment: array_name[index] = value;",
            "Length of array in scope: sizeof(arr) / sizeof(arr[0]).",
        ],
        "examples": [
            "int arr[5] = {2, 4, 8, 12, 16}; cout << arr[0]; // Output: 2",
            "arr[0] = 90; // Updates first element",
            "int len = sizeof(arr) / sizeof(arr[0]); // Length calculation",
        ],
    },
}

CPP_TOPICS[24] = {
    "id": 24,
    "title": "Multidimensional Arrays",
    "category": "Arrays and Strings",
    "difficulty": "Intermediate",
    "duration": "35 min",
    "concept": "Multidimensional arrays in C++ are arrays with more than one dimension, storing elements in grid-like (2D: rows & columns) or layered cuboid structures (3D: layers, rows & columns). Total element capacity is the product of all dimension sizes, and memory allocation is contiguous. Function signatures receiving 2D/3D arrays must explicitly specify inner dimension bounds.",
    "syntax": "// 2D Array Declaration & Initialization\ndata_type array_name[rows][cols];\nint arr[2][4] = {{0, 1, 2, 3}, {4, 5, 6, 7}};\nint arr[2][4] = {0}; // All elements set to 0\n\n// 3D Array Declaration & Initialization\nint arr[2][2][3] = {{{0,1,2}, {3,4,5}}, {{6,7,8}, {9,10,11}}};\n\n// Accessing and Updating\narr[row][col] = new_value;\narr[layer][row][col] = new_value;\n\n// Functions\nvoid print2D(int arr[2][4]);",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\n// Function taking 2D array parameter\nvoid print2DArray(int arr[2][4]) {\n    for (int i = 0; i < 2; i++) {\n        for (int j = 0; j < 4; j++) {\n            cout << arr[i][j] << \" \";\n        }\n        cout << endl;\n    }\n}\n\nint main() {\n    // Initializing a 2D array (2 rows, 4 columns)\n    int arr[2][4] = {\n        {0, 1, 2, 3},\n        {4, 5, 6, 7}\n    };\n\n    // Updating elements\n    arr[0][2] = 22;\n    arr[1][0] = 99;\n\n    cout << \"Traversing 2D Array:\" << endl;\n    print2DArray(arr);\n\n    cout << \"Total Memory Size: \" << sizeof(arr) << \" bytes\" << endl;\n    return 0;\n}",
        "output": "Traversing 2D Array:\n0 1 22 3 \n99 5 6 7 \nTotal Memory Size: 32 bytes",
        "explanation": "int arr[2][4] allocates 8 integers (32 bytes). Nested loops access elements via arr[i][j]. Passing 2D arrays to functions requires specifying inner column dimensions.",
    },
    "fill_blanks": {
        "question": "Complete the 2D array declaration, update, traversal, and function parameter snippet:",
        "answers": ["arr", "22", "for", "4"],
        "options": ["arr", "22", "for", "4", "vector", "sizeof"],
    },
    "compiler": {
        "title": "C++ Multidimensional Array Sandbox",
        "question": "Arrange lines to create a 3x4 2D matrix and print all elements using nested for loops.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int matrix[3][4] = {\n        {1, 2, 3, 4},\n        {5, 6, 7, 8},\n        {9, 10, 11, 12}\n    };\n    for (int i = 0; i < 3; i++) {\n        for (int j = 0; j < 4; j++) {\n            cout << matrix[i][j] << \" \";\n        }\n        cout << endl;\n    }\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int matrix[3][4] = {",
            "        {1, 2, 3, 4},",
            "        {5, 6, 7, 8},",
            "        {9, 10, 11, 12}",
            "    };",
            "    for (int i = 0; i < 3; i++) {",
            "        for (int j = 0; j < 4; j++) {",
            "            cout << matrix[i][j] << \" \";",
            "        }",
            "        cout << endl;",
            "    }",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "How many total elements can a 2D array `int arr[3][4]` hold?",
            "options": ["12", "7", "16", "24"],
            "answer": "12",
        },
        {
            "question": "Which dimension MUST be explicitly specified in function signatures when passing a 2D array parameter in C++?",
            "options": [
                "The column dimension (inner dimension size)",
                "The row dimension (outermost dimension)",
                "None of the dimensions",
                "Both dimensions can always be omitted"
            ],
            "answer": "The column dimension (inner dimension size)",
        },
        {
            "question": "What is the memory size in bytes of `int arr[2][4]` assuming 4 bytes per integer?",
            "options": ["32 bytes", "8 bytes", "16 bytes", "64 bytes"],
            "answer": "32 bytes",
        },
        {
            "question": "How many nested loops are required to traverse a 3D array `int arr[2][2][3]`?",
            "options": ["3 nested loops", "2 nested loops", "1 loop", "4 nested loops"],
            "answer": "3 nested loops",
        },
        {
            "question": "What valid index ranges apply to accessing `arr[i][j]` in `int arr[2][4]`?",
            "options": [
                "0 <= i <= 1 and 0 <= j <= 3",
                "1 <= i <= 2 and 1 <= j <= 4",
                "0 <= i <= 2 and 0 <= j <= 4",
                "-1 <= i <= 1 and -1 <= j <= 3"
            ],
            "answer": "0 <= i <= 1 and 0 <= j <= 3",
        },
    ],
    "theory": {
        "definition": "A multidimensional array is an array of arrays organized across multiple dimensions (e.g. 2D grid of rows and columns, 3D cuboid).",
        "why": "Used to model matrices, game boards, image pixel data, and spatial coordinate systems efficiently in contiguous memory.",
        "rules": [
            "Syntax: data_type array_name[dim1][dim2]...[dimN];",
            "Element count = dim1 * dim2 * ... * dimN.",
            "Index range for dimension N is 0 to size_N - 1.",
            "When passing to functions, all dimensions except the first must be explicitly specified in parameters.",
            "Initialization with {0} clears all elements across all dimensions.",
        ],
        "examples": [
            "int matrix[3][4]; // 2D array",
            "int cube[2][2][3]; // 3D array",
            "void print(int arr[2][4]); // Column size required",
        ],
    },
}

CPP_TOPICS[25] = {
    "id": 25,
    "title": "Strings",
    "category": "Arrays and Strings",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "Strings in C++ are sequences of characters representing textual data. C++ supports C-style character arrays (`char str[]`) and the standard `std::string` class defined in `<string>`. `std::string` manages memory dynamically, avoids fixed buffer limits, and supports traversal using indices `[]`, range-based `for` loops, and iterators.",
    "syntax": "#include <string>\nusing namespace std;\n\nstring str = \"Hello Geeks\";\n\n// Traversals\nfor (int i = 0; i < str.size(); i++) cout << str[i];\nfor (char ch : str) cout << ch;\nfor (auto it = str.begin(); it != str.end(); it++) cout << *it;",
    "example": {
        "code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string str = \"Hello Geeks\";\n\n    // 1. Index-based traversal\n    cout << \"Using index: \";\n    for (int i = 0; i < str.size(); i++) {\n        cout << str[i];\n    }\n    cout << endl;\n\n    // 2. Range-based for loop traversal\n    cout << \"Using range-based loop: \";\n    for (char ch : str) {\n        cout << ch;\n    }\n    cout << endl;\n\n    // 3. Iterator traversal\n    cout << \"Using iterator: \";\n    for (auto it = str.begin(); it != str.end(); it++) {\n        cout << *it;\n    }\n    cout << endl;\n\n    return 0;\n}",
        "output": "Using index: Hello Geeks\nUsing range-based loop: Hello Geeks\nUsing iterator: Hello Geeks",
        "explanation": "std::string provides standard container behavior. Elements can be accessed sequentially using 0-based indices, range-based loops, or STL begin()/end() iterators.",
    },
    "fill_blanks": {
        "question": "Complete the std::string declaration and iterator traversal snippet:",
        "answers": ["string", "begin", "end", "*it"],
        "options": ["string", "begin", "end", "*it", "char", "vector"],
    },
    "compiler": {
        "title": "C++ Strings Traversal Sandbox",
        "question": "Arrange lines to declare a std::string and iterate through characters using a range-based for loop.",
        "starter_code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string text = \"SkillExa C++ Track\";\n    for (char c : text) {\n        cout << c;\n    }\n    cout << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "#include <string>",
            "using namespace std;",
            "int main() {",
            "    string text = \"SkillExa C++ Track\";",
            "    for (char c : text) {",
            "        cout << c;",
            "    }",
            "    cout << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "Which header file is required to use the std::string class in C++?",
            "options": ["<string>", "<cstring>", "<iostream>", "<stdlib.h>"],
            "answer": "<string>",
        },
        {
            "question": "What advantage does std::string offer over fixed C-style character arrays (char[])?",
            "options": [
                "Dynamic memory management that automatically expands and shrinks",
                "Fixed size decided at compile time",
                "Requires manual null-terminator ('\\0') management",
                "Does not support iterators"
            ],
            "answer": "Dynamic memory management that automatically expands and shrinks",
        },
        {
            "question": "Which method returns an iterator pointing to the first character of a std::string?",
            "options": ["str.begin()", "str.front()", "str.start()", "str.first()"],
            "answer": "str.begin()",
        },
        {
            "question": "How do you dereference an iterator `it` during std::string traversal to obtain the character value?",
            "options": ["*it", "&it", "it.val()", "it->char()"],
            "answer": "*it",
        },
        {
            "question": "What loop syntax provides concise read-only traversal over characters in a std::string `str`?",
            "options": [
                "for (char ch : str)",
                "for (str : char ch)",
                "while (str.hasNext())",
                "foreach (ch in str)"
            ],
            "answer": "for (char ch : str)",
        },
    ],
    "theory": {
        "definition": "A C++ string represents a sequence of characters managed as an object of std::string from the standard library.",
        "why": "Provides safety against buffer overflows, automatic memory lifecycle management, and standard STL iterator interfaces.",
        "rules": [
            "Always include <string>.",
            "std::string automatically manages capacity and memory reallocation.",
            "Traverse using indices, range-based for loops, or iterators.",
            "Characters are indexed starting from 0 to str.size() - 1.",
        ],
        "examples": [
            "string s = \"Hello\"; cout << s[0]; // Output: H",
            "for (char c : s) { cout << c; }",
        ],
    },
}

CPP_TOPICS[26] = {
    "id": 26,
    "title": "String Class",
    "category": "Arrays and Strings",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "The std::string class in C++ encapsulates character sequences and provides three core categories of member functions: Input Functions (getline(), push_back(), pop_back()), Capacity Functions (length(), size(), capacity(), resize(), shrink_to_fit()), and Iterator Functions (begin(), end(), rbegin(), rend(), cbegin(), cend(), crbegin(), crend()). Constant iterators enforce read-only semantics.",
    "syntax": "string str;\ngetline(cin, str);\nstr.push_back('A');\nstr.pop_back();\nstr.resize(10);\nstr.capacity();\nstr.shrink_to_fit();\n\n// Constant Iterators (Read-only)\nfor (auto it = str.cbegin(); it != str.cend(); ++it) cout << *it;",
    "example": {
        "code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string str = \"geeksforgeeks is for geeks\";\n    cout << \"Initial String: \" << str << endl;\n\n    // 1. Capacity & Resize\n    str.resize(13);\n    cout << \"After resize(13): \" << str << endl;\n    cout << \"Capacity: \" << str.capacity() << endl;\n    cout << \"Length: \" << str.length() << endl;\n\n    // 2. Memory optimization with shrink_to_fit\n    str.shrink_to_fit();\n    cout << \"Capacity after shrink_to_fit(): \" << str.capacity() << endl;\n\n    // 3. Modifying with forward iterators\n    for (auto it = str.begin(); it != str.end(); ++it) {\n        if (it == str.begin()) *it = 'G';\n    }\n    cout << \"After iterator edit: \" << str << endl;\n\n    return 0;\n}",
        "output": "Initial String: geeksforgeeks is for geeks\nAfter resize(13): geeksforgeeks\nCapacity: 26\nLength: 13\nCapacity after shrink_to_fit(): 13\nAfter iterator edit: Geeksforgeeks",
        "explanation": "resize(13) shortens text. capacity() shows allocated storage bytes. shrink_to_fit() shrinks memory buffer to match length 13. Forward iterators allow inline character updates.",
    },
    "fill_blanks": {
        "question": "Complete the std::string class capacity and iterator snippet:",
        "answers": ["getline", "resize", "capacity", "shrink_to_fit"],
        "options": ["getline", "resize", "capacity", "shrink_to_fit", "cin", "vector"],
    },
    "compiler": {
        "title": "C++ std::string Class Operations Sandbox",
        "question": "Arrange lines to create a string, append a char with push_back, resize to length 5, and call shrink_to_fit.",
        "starter_code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string str = \"Hello World\";\n    str.push_back('!');\n    str.resize(5);\n    str.shrink_to_fit();\n    cout << \"Result: \" << str << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "#include <string>",
            "using namespace std;",
            "int main() {",
            "    string str = \"Hello World\";",
            "    str.push_back('!');",
            "    str.resize(5);",
            "    str.shrink_to_fit();",
            "    cout << \"Result: \" << str << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "Which function reads an entire line including spaces from standard input into a std::string?",
            "options": ["getline(cin, str)", "cin >> str", "str.read()", "gets(str)"],
            "answer": "getline(cin, str)",
        },
        {
            "question": "What is the difference between str.length() and str.capacity()?",
            "options": [
                "length() returns character count; capacity() returns allocated memory buffer size",
                "length() returns bytes; capacity() returns bit count",
                "They are identical in all circumstances",
                "capacity() counts words instead of characters"
            ],
            "answer": "length() returns character count; capacity() returns allocated memory buffer size",
        },
        {
            "question": "Which member function reduces a std::string container's memory capacity to fit its current length?",
            "options": ["shrink_to_fit()", "resize()", "compact()", "clear()"],
            "answer": "shrink_to_fit()",
        },
        {
            "question": "What happens when trying to modify characters via a constant iterator (cbegin() / cend())?",
            "options": [
                "Causes a compile-time error because content is read-only",
                "Modifies the original string",
                "Creates a deep copy automatically",
                "Throws a runtime exception"
            ],
            "answer": "Causes a compile-time error because content is read-only",
        },
        {
            "question": "Which function appends a single character to the end of a std::string?",
            "options": ["push_back()", "append_char()", "add()", "insert_last()"],
            "answer": "push_back()",
        },
    ],
    "theory": {
        "definition": "The std::string class provides built-in member functions for stream input, capacity management, and bidirectional/constant iterator traversal.",
        "why": "Enables predictable memory footprints and clean object-oriented string operations.",
        "rules": [
            "Use getline(cin, str) to capture spaced sentences.",
            "push_back(ch) appends a char; pop_back() removes the last char.",
            "resize(n) alters length; shrink_to_fit() reclaims unneeded capacity.",
            "cbegin()/cend() return constant iterators preventing character modification.",
        ],
        "examples": [
            "string s = \"Test\"; s.push_back('!'); // Test!",
            "s.resize(2); // Te",
            "s.shrink_to_fit();",
        ],
    },
}

CPP_TOPICS[27] = {
    "id": 27,
    "title": "String Functions",
    "category": "Arrays and Strings",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "The std::string class in C++ provides standard manipulation functions: length()/size(), at() (bounds-checked access), append() / + (concatenation), compare() / == (lexicographical comparison), find()/rfind() (substring search returning index or string::npos), substr(pos, len) (substring extraction), insert(), replace(), erase(), c_str() (C-style const char* pointer conversion), and stringstream splitting.",
    "syntax": "str.length(); str.size();\nstr.at(index);\nstr1 + str2; str1.append(str2);\nstr1 == str2; str1.compare(str2);\nsize_t pos = str.find(\"target\"); // string::npos if missing\nstring sub = str.substr(pos, len);\nstr.insert(index, text);\nstr.replace(index, len, text);\nstr.erase(start, len);\nconst char* cstr = str.c_str();",
    "example": {
        "code": "#include <iostream>\n#include <string>\n#include <sstream>\nusing namespace std;\n\nint main() {\n    string text = \"C++ Programming Language\";\n\n    // 1. Searching & Substring\n    size_t pos = text.find(\"Programming\");\n    if (pos != string::npos) {\n        cout << \"Found 'Programming' at index: \" << pos << endl;\n    }\n    string sub = text.substr(pos, 11);\n    cout << \"Extracted Substring: \" << sub << endl;\n\n    // 2. Replacing substring\n    string str = \"Hello World\";\n    str.replace(6, 5, \"C++\");\n    cout << \"After replace: \" << str << endl;\n\n    // 3. String splitting with stringstream\n    string sentence = \"Learn C++ String Functions\";\n    stringstream ss(sentence);\n    string word;\n    cout << \"Split words: \";\n    while (ss >> word) {\n        cout << \"[\" << word << \"] \";\n    }\n    cout << endl;\n\n    // 4. C-style string conversion\n    const char* cstr = text.c_str();\n    cout << \"C-Style String: \" << cstr << endl;\n\n    return 0;\n}",
        "output": "Found 'Programming' at index: 4\nExtracted Substring: Programming\nAfter replace: Hello C++\nSplit words: [Learn] [C++] [String] [Functions] \nC-Style String: C++ Programming Language",
        "explanation": "text.find(\"Programming\") locates substring at index 4. substr(4, 11) extracts \"Programming\". replace(6, 5, \"C++\") replaces \"World\". stringstream splits tokens by space. c_str() converts std::string to const char*.",
    },
    "fill_blanks": {
        "question": "Complete the string search, substring extraction, replace, and stringstream split snippet:",
        "answers": ["find", "substr", "replace", "stringstream"],
        "options": ["find", "substr", "replace", "stringstream", "cin", "split"],
    },
    "compiler": {
        "title": "C++ String Functions Operations Sandbox",
        "question": "Arrange lines to search for a substring with find(), extract a substring with substr(), and convert to a C-style string using c_str().",
        "starter_code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string text = \"GeeksforGeeks Hello\";\n    size_t pos = text.find(\"Hello\");\n    string sub = text.substr(pos, 5);\n    const char* cstr = text.c_str();\n    cout << \"Sub: \" << sub << \", C-string: \" << cstr << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "#include <string>",
            "using namespace std;",
            "int main() {",
            "    string text = \"GeeksforGeeks Hello\";",
            "    size_t pos = text.find(\"Hello\");",
            "    string sub = text.substr(pos, 5);",
            "    const char* cstr = text.c_str();",
            "    cout << \"Sub: \" << sub << \", C-string: \" << cstr << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What value does `str.find(query)` return when the target substring is NOT found?",
            "options": ["std::string::npos", "-1", "0", "NULL"],
            "answer": "std::string::npos",
        },
        {
            "question": "What does `str1.compare(str2)` return when `str1` and `str2` are lexicographically equal?",
            "options": ["0", "1", "true", "-1"],
            "answer": "0",
        },
        {
            "question": "How does `str.at(index)` differ from `str[index]`?",
            "options": [
                "at() performs bounds checking and throws an out-of-range exception if index is invalid",
                "at() returns an integer ASCII code instead of char",
                "at() only works on uppercase strings",
                "There is no difference"
            ],
            "answer": "at() performs bounds checking and throws an out-of-range exception if index is invalid",
        },
        {
            "question": "Which C++ tool from `<sstream>` is commonly used with `while (ss >> word)` to split a space-delimited string?",
            "options": ["std::stringstream", "std::string_split", "std::strtok", "std::vector<string>"],
            "answer": "std::stringstream",
        },
        {
            "question": "Which member function converts a `std::string` into a null-terminated `const char*` C-style string pointer?",
            "options": ["c_str()", "to_char()", "c_string()", "data_ptr()"],
            "answer": "c_str()",
        },
    ],
    "theory": {
        "definition": "Member functions of std::string provide built-in text operations including search, slice, insertion, replacement, comparison, and C-API string conversion.",
        "why": "Eliminates low-level pointer arithmetic and manual memory management for text operations.",
        "rules": [
            "substr(start, length) returns a sub-portion of string.",
            "find(str) returns index or string::npos if missing.",
            "compare(str2) returns 0 (equal), < 0 (less), or > 0 (greater).",
            "c_str() returns a null-terminated const char* array.",
            "stringstream enables space-delimited string splitting.",
        ],
        "examples": [
            "string s = \"Hello World\"; size_t p = s.find(\"World\");",
            "string sub = s.substr(6, 5); // World",
            "const char* c = s.c_str();",
        ],
    },
}

CPP_TOPICS[28] = {
    "id": 28,
    "title": "Pointers",
    "category": "Pointers and References",
    "difficulty": "Intermediate",
    "duration": "40 min",
    "concept": "A pointer in C++ is a variable holding the memory address of another variable (&var). Pointers enable direct memory access, dynamic allocation (new/delete), and linked data structures. Accessing stored values is done via dereferencing (*ptr). Pointer sizes depend on host CPU architecture (8 bytes on 64-bit systems). Special pointer categories include Wild Pointers (uninitialized), NULL/nullptr (points to nothing), Void Pointers (void*, generic pointers requiring typecasting), Dangling Pointers (pointing to deallocated memory), Double Pointers (int**), Function Pointers, and Smart Pointers.",
    "syntax": "// Declaration & Address Assignment\ndata_type* ptr = &var;\n\n// Dereferencing & Re-assignment\n*ptr = 20; // Modify underlying value\nptr = &other_var; // Point to new address\n\n// Special Pointers\nint* p = nullptr; // Null pointer\nvoid* vptr = &var; // Generic void pointer\nint val = *(static_cast<int*>(vptr)); // Typecast void pointer\nint** dptr = &ptr; // Double pointer",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int var = 10;\n    int* ptr = &var;\n\n    cout << \"Value of var: \" << var << endl;\n    cout << \"Address of var (&var): \" << &var << endl;\n    cout << \"Address stored in ptr: \" << ptr << endl;\n    cout << \"Value pointed to (*ptr): \" << *ptr << endl;\n\n    // Dereferenced update\n    *ptr = 99;\n    cout << \"Value of var after *ptr = 99: \" << var << endl;\n\n    // Void pointer typecasting\n    void* vptr = &var;\n    cout << \"Dereferenced void pointer: \" << *(static_cast<int*>(vptr)) << endl;\n\n    // Pointer size\n    cout << \"Pointer size: \" << sizeof(ptr) << \" bytes\" << endl;\n    return 0;\n}",
        "output": "Value of var: 10\nAddress of var (&var): 0x7fffa0757dd4\nAddress stored in ptr: 0x7fffa0757dd4\nValue pointed to (*ptr): 10\nValue of var after *ptr = 99: 99\nDereferenced void pointer: 99\nPointer size: 8 bytes",
        "explanation": "int* ptr = &var stores the address of var. *ptr dereferences the memory address to access or modify value. void* holds any address type but requires explicit typecasting static_cast<int*> before dereferencing.",
    },
    "fill_blanks": {
        "question": "Complete the pointer declaration, address assignment, dereferencing, and void pointer typecasting snippet:",
        "answers": ["&var", "*ptr", "nullptr", "static_cast"],
        "options": ["&var", "*ptr", "nullptr", "static_cast", "sizeof", "new"],
    },
    "compiler": {
        "title": "C++ Pointers Sandbox",
        "question": "Arrange lines to declare integer var, store its address in pointer ptr, print value using dereferencing, and modify var using *ptr.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int var = 10;\n    int* ptr = &var;\n    cout << \"*ptr value: \" << *ptr << endl;\n    *ptr = 22;\n    cout << \"Updated var: \" << var << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int var = 10;",
            "    int* ptr = &var;",
            "    cout << \"*ptr value: \" << *ptr << endl;",
            "    *ptr = 22;",
            "    cout << \"Updated var: \" << var << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What operator is used to obtain the memory address of a variable in C++?",
            "options": ["& (Address-of operator)", "* (Dereference operator)", "-> (Arrow operator)", ":: (Scope operator)"],
            "answer": "& (Address-of operator)",
        },
        {
            "question": "What operator is used to dereference a pointer and access the value stored at its target address?",
            "options": ["* (Dereference operator)", "& (Address-of operator)", "% (Modulo operator)", ":: (Scope operator)"],
            "answer": "* (Dereference operator)",
        },
        {
            "question": "What is the size of any pointer variable on a 64-bit operating system architecture?",
            "options": ["8 bytes", "4 bytes", "2 bytes", "16 bytes"],
            "answer": "8 bytes",
        },
        {
            "question": "Why can a void* pointer NOT be directly dereferenced without explicit typecasting?",
            "options": [
                "Because void pointers have no associated data type, so the compiler does not know how many bytes to read",
                "Because void pointers are stored in GPU memory",
                "Because void pointers are read-only constants",
                "Because void pointers automatically delete data"
            ],
            "answer": "Because void pointers have no associated data type, so the compiler does not know how many bytes to read",
        },
        {
            "question": "What is a dangling pointer in C++?",
            "options": [
                "A pointer pointing to a memory location that has already been deallocated or gone out of scope",
                "An uninitialized pointer holding random garbage addresses",
                "A pointer initialized to nullptr",
                "A double pointer pointing to another pointer"
            ],
            "answer": "A pointer pointing to a memory location that has already been deallocated or gone out of scope",
        },
    ],
    "theory": {
        "definition": "A pointer is a variable storing the memory address of another variable, providing indirect access and dynamic memory management capability.",
        "why": "Crucial for hardware level memory manipulation, dynamic allocation (new/delete), function call-by-pointer, and linked structures.",
        "rules": [
            "Declare with data_type* ptr = &var;.",
            "Dereference with *ptr to get/set value.",
            "Use nullptr for unassigned pointers to avoid wild pointer errors.",
            "All pointers on 64-bit architecture consume 8 bytes.",
            "Void pointers require static_cast<T*> before dereferencing.",
        ],
        "examples": [
            "int x = 10; int* p = &x; cout << *p;",
            "void* v = &x; cout << *(static_cast<int*>(v));",
        ],
    },
}

CPP_TOPICS[29] = {
    "id": 29,
    "title": "References",
    "category": "Pointers and References",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "A reference in C++ acts as an alias or alternative name for an existing variable (T& ref = var;). Once initialized, any modification made through ref directly changes the original variable. References must be initialized at declaration, cannot be nullptr, and cannot be reassigned to refer to another variable. They are widely used for efficient parameter passing (pass-by-reference), returning references from functions, and modifying elements directly inside range-based for loops.",
    "syntax": "// Declaration & Binding\ndata_type& ref = var;\n\n// Pass-by-reference in functions\nvoid modifyValue(int& x) { x = 20; }\n\n// Returning reference from function\nint& getMax(int& a, int& b) { return (a > b) ? a : b; }\n\n// Range-based loop with reference\nfor (int& x : container) { x += 5; }",
    "example": {
        "code": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nvoid modifyValue(int& x) {\n    x = 99; // Modifies original caller variable\n}\n\nint main() {\n    int a = 10;\n    int& ref = a; // ref is alias for a\n\n    cout << \"Original a: \" << a << \", ref: \" << ref << endl;\n    ref = 22;\n    cout << \"After ref = 22 -> a: \" << a << endl;\n\n    modifyValue(a);\n    cout << \"After modifyValue(a) -> a: \" << a << endl;\n\n    // Modifying vector elements using reference in range loop\n    vector<int> vect = {10, 20, 30};\n    for (int& val : vect) {\n        val += 5;\n    }\n\n    cout << \"Updated vector elements: \";\n    for (int val : vect) {\n        cout << val << \" \";\n    }\n    cout << endl;\n    return 0;\n}",
        "output": "Original a: 10, ref: 10\nAfter ref = 22 -> a: 22\nAfter modifyValue(a) -> a: 99\nUpdated vector elements: 15 25 35",
        "explanation": "int& ref = a binds ref to variable a. Changes to ref update a directly. modifyValue(int& x) avoids copying. for (int& val : vect) mutates original elements in-place.",
    },
    "fill_blanks": {
        "question": "Complete the C++ reference declaration, pass-by-reference function parameter, and range loop reference snippet:",
        "answers": ["&", "modifyValue", "ref", "vect"],
        "options": ["&", "modifyValue", "ref", "vect", "*", "nullptr"],
    },
    "compiler": {
        "title": "C++ References Sandbox",
        "question": "Arrange lines to create variable x, bind reference ref to x, update ref to 22, and print updated x.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int x = 10;\n    int& ref = x;\n    ref = 22;\n    cout << \"x value: \" << x << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int x = 10;",
            "    int& ref = x;",
            "    ref = 22;",
            "    cout << \"x value: \" << x << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What symbol is used to declare a reference variable in C++?",
            "options": ["&", "*", "->", "::"],
            "answer": "&",
        },
        {
            "question": "Can a reference in C++ be initialized as nullptr or NULL?",
            "options": [
                "No, references must always refer to a valid object and cannot be null",
                "Yes, using nullptr keyword",
                "Yes, in modern C++20 standard only",
                "Only inside class definitions"
            ],
            "answer": "No, references must always refer to a valid object and cannot be null",
        },
        {
            "question": "What happens when you reassign a reference variable after initialization (e.g. ref = y)?",
            "options": [
                "It assigns the value of y to the original variable bound to ref, rather than rebinding ref to y",
                "It rebinds ref to point to y",
                "It causes a compile-time error",
                "It deletes the memory of y"
            ],
            "answer": "It assigns the value of y to the original variable bound to ref, rather than rebinding ref to y",
        },
        {
            "question": "Why should a function NEVER return a reference to a local variable?",
            "options": [
                "Because local variables are destroyed when function scope exits, resulting in a dangling reference",
                "Because local variables use 8 bytes",
                "Because references cannot return integer values",
                "Because compiler converts local variables to static"
            ],
            "answer": "Because local variables are destroyed when function scope exits, resulting in a dangling reference",
        },
        {
            "question": "What benefit does passing large structures/objects by const reference (const T&) to functions provide?",
            "options": [
                "Avoids expensive copying while preventing unintended modifications inside the function",
                "Enables dynamic memory allocation",
                "Allows the function to return void",
                "Makes the function multithreaded"
            ],
            "answer": "Avoids expensive copying while preventing unintended modifications inside the function",
        },
    ],
    "theory": {
        "definition": "A reference is an alias for an existing variable sharing the exact same memory address.",
        "why": "Provides cleaner syntax than pointers for pass-by-reference, operator overloading, and reference-based container mutation.",
        "rules": [
            "Must be initialized upon declaration (T& ref = var;).",
            "Cannot be reassigned to bind to another variable.",
            "Cannot be null (nullptr).",
            "Never return references to local stack-allocated variables.",
        ],
        "examples": [
            "int a = 10; int& ref = a; ref = 20; // a becomes 20",
            "void swap(int& a, int& b) { int temp = a; a = b; b = temp; }",
        ],
    },
}

CPP_TOPICS[30] = {
    "id": 30,
    "title": "References vs Pointers",
    "category": "Pointers and References",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "Pointers and references in C++ both enable indirect access to memory, but differ significantly in syntax, safety, rebindability, and nullability. A pointer (T*) is an independent variable storing a memory address, can be nullptr, can be reassigned to point to different variables, requires explicit dereferencing (*ptr), and can undergo pointer arithmetic. A reference (T&) is an alias for an existing variable, must be initialized at declaration, cannot be null, cannot be rebound, requires no dereferencing syntax, and shares the exact memory address of the bound variable.",
    "syntax": "// Pointers\nint* ptr = &x; // Stores address\n*ptr = 20; // Explicit dereference\nptr = nullptr; // Can be null\nptr = &y; // Can be reassigned\nptr++; // Pointer arithmetic allowed\n\n// References\nint& ref = x; // Alias (must initialize)\nref = 20; // Automatic dereference (updates x)\n// Cannot be null, cannot be rebound, no arithmetic",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int x = 10;\n    int y = 30;\n\n    // 1. Pointer Demonstrations\n    int* ptr = &x;\n    cout << \"Pointer *ptr: \" << *ptr << \", Address in ptr: \" << ptr << endl;\n    ptr = &y; // Reassigned pointer to point to y\n    cout << \"Reassigned *ptr: \" << *ptr << endl;\n    ptr = nullptr; // Nullable\n    cout << \"Null pointer check: \" << (ptr == nullptr ? \"Is nullptr\" : \"Valid\") << endl;\n\n    // 2. Reference Demonstrations\n    int& ref = x;\n    cout << \"Reference ref: \" << ref << \", Address of ref: \" << &ref << endl;\n    cout << \"Is &ref == &x? \" << (&ref == &x ? \"Yes, same address\" : \"No\") << endl;\n    ref = y; // Assigns y's value (30) to x, does NOT rebind ref\n    cout << \"After ref = y -> x: \" << x << endl;\n\n    return 0;\n}",
        "output": "Pointer *ptr: 10, Address in ptr: 0x7ffd2b32c7f4\nReassigned *ptr: 30\nNull pointer check: Is nullptr\nReference ref: 10, Address of ref: 0x7ffd2b32c7f4\nIs &ref == &x? Yes, same address\nAfter ref = y -> x: 30",
        "explanation": "ptr is an independent variable storing addresses, rebindable to &y and set to nullptr. ref shares x's address (&ref == &x). ref = y copies y's value into x without rebinding ref.",
    },
    "fill_blanks": {
        "question": "Complete the pointer vs reference comparative syntax snippet:",
        "answers": ["*", "&", "nullptr", "ref"],
        "options": ["*", "&", "nullptr", "ref", "delete", "new"],
    },
    "compiler": {
        "title": "C++ Pointers vs References Comparison Sandbox",
        "question": "Arrange lines to demonstrate a rebindable pointer and a non-rebindable reference bound to integer x.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int x = 10, y = 20;\n    int* ptr = &x;\n    int& ref = x;\n    ptr = &y;\n    ref = 50;\n    cout << \"*ptr: \" << *ptr << \", x: \" << x << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int x = 10, y = 20;",
            "    int* ptr = &x;",
            "    int& ref = x;",
            "    ptr = &y;",
            "    ref = 50;",
            "    cout << \"*ptr: \" << *ptr << \", x: \" << x << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "Which feature accurately describes a C++ pointer compared to a reference?",
            "options": [
                "A pointer has its own memory address, can be null, and can be reassigned to point to different variables",
                "A pointer cannot be null",
                "A pointer cannot be reassigned after declaration",
                "A pointer shares the exact memory address of its target variable without storing an address"
            ],
            "answer": "A pointer has its own memory address, can be null, and can be reassigned to point to different variables",
        },
        {
            "question": "Can a C++ reference be declared without being initialized?",
            "options": [
                "No, references must be initialized at the time of declaration",
                "Yes, references can be initialized later",
                "Yes, if declared inside a struct",
                "Yes, if initialized to nullptr"
            ],
            "answer": "No, references must be initialized at the time of declaration",
        },
        {
            "question": "What happens when executing `ref = y` on a reference `int& ref = x;`?",
            "options": [
                "The value of y is assigned to x, but ref remains permanently bound to x",
                "ref is rebound to refer to y",
                "A syntax compilation error occurs",
                "Both x and y are set to 0"
            ],
            "answer": "The value of y is assigned to x, but ref remains permanently bound to x",
        },
        {
            "question": "Which construct requires explicit dereferencing using `*` to read or write the underlying value?",
            "options": ["Pointer (T*)", "Reference (T&)", "Both Pointer and Reference", "Neither"],
            "answer": "Pointer (T*)",
        },
        {
            "question": "When should pointers be preferred over references in C++ program design?",
            "options": [
                "When optional/null parameters, dynamic memory management (new/delete), or pointer arithmetic/rebinding are required",
                "When passing read-only constant function parameters",
                "When overloading binary operators like +",
                "When creating simple variable aliases"
            ],
            "answer": "When optional/null parameters, dynamic memory management (new/delete), or pointer arithmetic/rebinding are required",
        },
    ],
    "theory": {
        "definition": "Pointers store variable memory addresses as independent objects; References act as non-null, non-rebindable aliases for existing variables.",
        "why": "Guides design decisions between nullable/rebindable low-level memory access (pointers) and safe, syntax-clean pass-by-reference (references).",
        "rules": [
            "Pointers: T* ptr, can be nullptr, rebindable, explicit *ptr dereference, supports pointer arithmetic.",
            "References: T& ref, must initialize, cannot be null, cannot rebind, implicit dereference.",
            "Use references by default for function parameters unless nullability or rebinding is required.",
        ],
        "examples": [
            "int x = 10, y = 20; int* p = &x; p = &y; // Pointer reassigned",
            "int& r = x; r = y; // Value of y copied into x",
        ],
    },
}

CPP_TOPICS[31] = {
    "id": 31,
    "title": "Structures",
    "category": "User-Defined Data Types",
    "difficulty": "Intermediate",
    "duration": "35 min",
    "concept": "A struct in C++ is a user-defined data type grouping related variables (data members) and functions (member functions) under a single name. Unlike C structures, C++ structs support member functions, constructors, destructors, and access specifiers (public, private, protected), behaving similarly to C++ classes except members are public by default. Members are accessed via the dot operator (.) or arrow operator (->) for structure pointers (ptr->member). Struct size includes compiler alignment padding, and empty structs consume 1 byte in C++.",
    "syntax": "struct Point {\n    int x = 0;\n    int y = 0;\n    int sum() { return x + y; }\n};\n\nPoint p = {10, 20};\ncout << p.x;\nPoint* ptr = &p;\nptr->sum();",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nstruct Point {\n    int x, y;\n\n    // Member function\n    int sum() {\n        return x + y;\n    }\n\n    void show() {\n        cout << \"Point(\" << x << \", \" << y << \")\" << endl;\n    }\n};\n\nint main() {\n    Point p1 = {10, 20};\n    p1.show();\n    cout << \"Sum: \" << p1.sum() << endl;\n\n    // Pointer to structure and arrow operator\n    Point* sptr = &p1;\n    sptr->x = 99;\n    cout << \"After arrow operator update: \";\n    sptr->show();\n\n    return 0;\n}",
        "output": "Point(10, 20)\nSum: 30\nAfter arrow operator update: Point(99, 20)",
        "explanation": "struct Point encapsulates data members x, y and member functions sum(), show(). Members are accessed with p1.x or via structure pointer sptr->x.",
    },
    "fill_blanks": {
        "question": "Complete the C++ struct definition, instantiation, member access, and pointer arrow operator snippet:",
        "answers": ["struct", "Point", ".", "->"],
        "options": ["struct", "Point", ".", "->", "class", "::"],
    },
    "compiler": {
        "title": "C++ Structures Sandbox",
        "question": "Arrange lines to define struct Point, instantiate p1 with {5, 15}, and call member function sum().",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nstruct Point {\n    int x, y;\n    int sum() { return x + y; }\n};\n\nint main() {\n    Point p = {5, 15};\n    cout << \"Sum: \" << p.sum() << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "struct Point {",
            "    int x, y;",
            "    int sum() { return x + y; }",
            "};",
            "int main() {",
            "    Point p = {5, 15};",
            "    cout << \"Sum: \" << p.sum() << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What is the default access specifier for members in a C++ struct?",
            "options": ["public", "private", "protected", "internal"],
            "answer": "public",
        },
        {
            "question": "Which operator is used to access structure members through a structure pointer (Point* ptr)?",
            "options": ["-> (Arrow operator)", ". (Dot operator)", ":: (Scope resolution operator)", "* (Dereference operator)"],
            "answer": "-> (Arrow operator)",
        },
        {
            "question": "Why does an empty struct in C++ consume 1 byte of memory instead of 0 bytes?",
            "options": [
                "To ensure every distinct structure instance object gets a unique memory address",
                "Because of virtual table pointers",
                "Due to string padding",
                "Empty structs are prohibited"
            ],
            "answer": "To ensure every distinct structure instance object gets a unique memory address",
        },
        {
            "question": "What causes the total sizeof(struct) in memory to potentially exceed the raw sum of its data member sizes?",
            "options": ["Compiler memory alignment padding", "Virtual inheritance", "Preprocessor directive expansion", "Name mangling"],
            "answer": "Compiler memory alignment padding",
        },
        {
            "question": "Can a C++ struct contain member functions, constructors, and destructors?",
            "options": [
                "Yes, C++ structures support member functions, constructors, destructors, and access specifiers",
                "No, structures can only contain primitive data variables",
                "Only if declared in C++20",
                "Only if using typedef"
            ],
            "answer": "Yes, C++ structures support member functions, constructors, destructors, and access specifiers",
        },
    ],
    "theory": {
        "definition": "A C++ struct is a user-defined compound data type grouping variables and member functions under a single name with default public access.",
        "why": "Provides object-oriented data aggregation for entities like student records, 2D/3D points, and node links in trees or linked lists.",
        "rules": [
            "Declare with struct Name { ... };.",
            "Members are public by default.",
            "Access with dot . for instance objects and arrow -> for pointers.",
            "C++ structs support default member initializers (C++11) and designated initializers (C++20).",
        ],
        "examples": [
            "struct Node { int data; Node* next; };",
            "Node n1 = {10, nullptr};",
        ],
    },
}

CPP_TOPICS[32] = {
    "id": 32,
    "title": "Unions",
    "category": "User-Defined Data Types",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "A union in C++ is a user-defined data type where all member variables share the exact same memory location. The total size of a union is at least the size of its largest data member. Only one member can hold a valid active value at any given time; writing to a new member overwrites the previously stored memory. Unions are widely used for memory optimization in embedded systems, register hardware mapping, and variant data representation. Anonymous unions lack a type name, allowing direct access to members within an enclosing struct.",
    "syntax": "union Data {\n    int i;\n    float f;\n    char str[20];\n};\n\nData d;\nd.i = 10; // active member\nd.f = 5.5; // overwrites d.i in shared memory",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nunion Data {\n    int intVal;\n    float floatVal;\n    char charVal;\n};\n\nstruct Employee {\n    int id;\n    // Anonymous union\n    union {\n        float hourlyRate;\n        float salary;\n    };\n};\n\nint main() {\n    Data d;\n    d.intVal = 42;\n    cout << \"Integer value: \" << d.intVal << endl;\n\n    // Writing to floatVal overwrites shared memory space\n    d.floatVal = 3.14f;\n    cout << \"Float value: \" << d.floatVal << endl;\n    cout << \"Union total size: \" << sizeof(Data) << \" bytes\" << endl;\n\n    // Anonymous union inside struct\n    Employee emp;\n    emp.id = 101;\n    emp.salary = 50000.0f;\n    cout << \"Employee ID: \" << emp.id << \", Salary: Rs \" << emp.salary << endl;\n\n    return 0;\n}",
        "output": "Integer value: 42\nFloat value: 3.14\nUnion total size: 4 bytes\nEmployee ID: 101, Salary: Rs 50000",
        "explanation": "union Data allocates memory equal to its largest member (4 bytes). All members intVal, floatVal share that address. Anonymous unions inside Employee allow direct field access emp.salary.",
    },
    "fill_blanks": {
        "question": "Complete the C++ union definition, shared memory allocation, and anonymous union snippet:",
        "answers": ["union", "sizeof", "shared", "hourlyRate"],
        "options": ["union", "sizeof", "shared", "hourlyRate", "struct", "class"],
    },
    "compiler": {
        "title": "C++ Unions Sandbox",
        "question": "Arrange lines to create union Data with int and float members, assign values, and print sizeof(Data).",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nunion Data {\n    int x;\n    float y;\n};\n\nint main() {\n    Data d;\n    d.x = 10;\n    cout << \"Sizeof union: \" << sizeof(Data) << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "union Data {",
            "    int x;",
            "    float y;",
            "};",
            "int main() {",
            "    Data d;",
            "    d.x = 10;",
            "    cout << \"Sizeof union: \" << sizeof(Data) << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "How is memory allocated for members of a C++ union compared to a struct?",
            "options": [
                "All members of a union share the exact same memory location, while struct members occupy separate memory offsets",
                "Union members get double memory allocation",
                "Union members are stored on heap; struct members on stack",
                "There is no difference in memory layout"
            ],
            "answer": "All members of a union share the exact same memory location, while struct members occupy separate memory offsets",
        },
        {
            "question": "What determines the overall sizeof() of a union in C++?",
            "options": [
                "It is at least the size of its largest member (plus alignment padding)",
                "The sum of all member sizes",
                "Always 4 bytes regardless of contents",
                "Always 8 bytes"
            ],
            "answer": "It is at least the size of its largest member (plus alignment padding)",
        },
        {
            "question": "What happens when a new member of a union is assigned a value?",
            "options": [
                "It overwrites the memory space, invalidating previous member values",
                "It creates a new memory buffer dynamically",
                "It causes a compile-time syntax error",
                "It shifts previous member values to the next memory offset"
            ],
            "answer": "It overwrites the memory space, invalidating previous member values",
        },
        {
            "question": "What is an anonymous union in C++?",
            "options": [
                "A union declared without a type name whose members can be accessed directly without a container object name",
                "A union declared inside a private namespace",
                "A union that cannot contain float variables",
                "A union declared in a C header"
            ],
            "answer": "A union declared without a type name whose members can be accessed directly without a container object name",
        },
        {
            "question": "What is a primary real-world application of unions in C++ software?",
            "options": [
                "Memory optimization in resource-constrained systems (e.g., embedded devices, hardware registers)",
                "Implementing polymorphic inheritance hierarchies",
                "Replacing STL vectors",
                "Exception handling stack unwinding"
            ],
            "answer": "Memory optimization in resource-constrained systems (e.g., embedded devices, hardware registers)",
        },
    ],
    "theory": {
        "definition": "A union is a user-defined data type where all data members overlap in the same memory storage location.",
        "why": "Saves memory when an entity only needs to store one variant data type at a time.",
        "rules": [
            "Declare with union Name { ... };.",
            "sizeof(union) equals largest member size + padding.",
            "Only one member is active at a time.",
            "Anonymous unions permit direct variable member access inside structs.",
        ],
        "examples": [
            "union Val { int i; float f; }; Val v; v.i = 5;",
        ],
    },
}

CPP_TOPICS[33] = {
    "id": 33,
    "title": "Enumeration (enum)",
    "category": "User-Defined Data Types",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "An enumeration (enum) in C++ is a user-defined data type consisting of a set of named integer constants, enhancing code clarity and safety for finite choices (e.g. days, directions, states). Unassigned enum values start at 0 and auto-increment by 1. C++11 introduced scoped enum class types, providing strict type safety, preventing implicit integer conversions, resolving scope name collisions, and requiring explicit scope resolution (Enum::Member) and typecasting (static_cast<int>(val)).",
    "syntax": "// Unscoped Enum\nenum Direction { EAST, NORTH = 5, WEST, SOUTH }; // 0, 5, 6, 7\nDirection dir = NORTH;\n\n// Scoped Enum Class (C++11)\nenum class Day { Sunday = 1, Monday, Tuesday };\nDay d = Day::Monday;\nint val = static_cast<int>(d);",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\n// Traditional Unscoped Enum\nenum Fruit { APPLE, BANANA = 5, ORANGE };\n\n// C++11 Scoped Enum Class\nenum class Day {\n    Sunday = 1,\n    Monday,\n    Tuesday,\n    Wednesday\n};\n\nint main() {\n    Fruit f = BANANA;\n    cout << \"Unscoped Enum (BANANA): \" << f << endl;\n    f = ORANGE;\n    cout << \"Unscoped Enum (ORANGE): \" << f << endl;\n\n    // Scoped Enum Class usage\n    Day today = Day::Tuesday;\n    cout << \"Scoped Enum (Day::Tuesday): \" << static_cast<int>(today) << endl;\n\n    return 0;\n}",
        "output": "Unscoped Enum (BANANA): 5\nUnscoped Enum (ORANGE): 6\nScoped Enum (Day::Tuesday): 3",
        "explanation": "Fruit enum assigns BANANA=5, auto-incrementing ORANGE to 6. Enum class Day prevents global scope leaks; Day::Tuesday evaluates to 3 via static_cast<int>.",
    },
    "fill_blanks": {
        "question": "Complete the unscoped enum and C++11 scoped enum class declaration snippet:",
        "answers": ["enum", "class", "Day::Monday", "static_cast"],
        "options": ["enum", "class", "Day::Monday", "static_cast", "struct", "typedef"],
    },
    "compiler": {
        "title": "C++ Enumeration Sandbox",
        "question": "Arrange lines to define an enum class Day, initialize today = Day::Monday, and print its integer value with static_cast.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nenum class Day { Sunday = 1, Monday, Tuesday };\n\nint main() {\n    Day today = Day::Monday;\n    cout << \"Day value: \" << static_cast<int>(today) << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "enum class Day { Sunday = 1, Monday, Tuesday };",
            "int main() {",
            "    Day today = Day::Monday;",
            "    cout << \"Day value: \" << static_cast<int>(today) << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What default integer value is assigned to the first enumerator in an unscoped enum if no value is explicitly set?",
            "options": ["0", "1", "-1", "Garbage value"],
            "answer": "0",
        },
        {
            "question": "If an enumerator BANANA is assigned value 5 in `enum Fruit { APPLE, BANANA = 5, ORANGE };`, what value does ORANGE take?",
            "options": ["6", "5", "0", "7"],
            "answer": "6",
        },
        {
            "question": "What key advantages does enum class (scoped enumeration introduced in C++11) provide over traditional enum?",
            "options": [
                "Strong type safety, elimination of global scope collisions, and prevention of implicit integer conversions",
                "Faster CPU execution speed",
                "Allows string values directly without integer mapping",
                "Allocates memory on dynamic heap"
            ],
            "answer": "Strong type safety, elimination of global scope collisions, and prevention of implicit integer conversions",
        },
        {
            "question": "How do you access an enumerator defined inside an `enum class Color { Red, Green, Blue };`?",
            "options": ["Color::Red", "Red", "Color.Red", "enum.Red"],
            "answer": "Color::Red",
        },
        {
            "question": "What explicit operator/cast is required to print or convert an enum class variable to an int?",
            "options": ["static_cast<int>(enum_var)", "dynamic_cast<int>(enum_var)", "int(enum_var)", "to_int(enum_var)"],
            "answer": "static_cast<int>(enum_var)",
        },
    ],
    "theory": {
        "definition": "An enumeration is a user-defined type comprising named integral constants representing discrete state values.",
        "why": "Replaces magic numbers with meaningful self-documenting identifiers.",
        "rules": [
            "Unscoped: enum Name { A, B }; (leaks names to outer scope).",
            "Scoped: enum class Name { A, B }; (requires Name::A).",
            "Auto-increment: Unassigned members increment previous value by +1.",
            "Scoped enums require explicit static_cast<int>() conversion.",
        ],
        "examples": [
            "enum Color { RED, GREEN, BLUE };",
            "enum class Status { OK = 200, NOT_FOUND = 404 };",
        ],
    },
}

CPP_TOPICS[34] = {
    "id": 34,
    "title": "typedef and using",
    "category": "User-Defined Data Types",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "The typedef keyword and modern using type aliases (C++11) create clean alternative names for complex data types (built-in types, STL containers, arrays, pointers, function pointers, and template aliases). The using keyword also serves as a directive for namespace access (using namespace std;), inheritance constructor inheriting (using Base::Base), and scope introduction (using std::cout). Modern C++ prefers using over typedef due to clearer template aliasing syntax.",
    "syntax": "// typedef syntax\ntypedef long long ulli;\ntypedef vector<int> vInt;\ntypedef int (*func_ptr)(int, int);\n\n// modern using syntax (C++11)\nusing ulli = long long;\nusing vInt = vector<int>;\ntemplate<typename T> using StringMap = map<string, T>; // template alias\n\n// using directives\nusing namespace std;\nusing std::cout;\nusing Base::Base; // inherit constructors",
    "example": {
        "code": "#include <iostream>\n#include <vector>\n#include <map>\nusing namespace std;\n\n// 1. typedef aliases\ntypedef long long ulli;\ntypedef vector<int> IntVector;\ntypedef int (*MathFunc)(int, int);\n\n// 2. Modern C++11 using type aliases\nusing StringMap = map<string, int>;\nusing Real = double;\n\nint add(int a, int b) { return a + b; }\n\nint main() {\n    ulli bigNum = 1234567890LL;\n    IntVector v = {10, 20, 30};\n    StringMap scores = {{\"Alice\", 95}, {\"Bob\", 88}};\n\n    MathFunc f = &add;\n    cout << \"bigNum: \" << bigNum << endl;\n    cout << \"Vector size: \" << v.size() << endl;\n    cout << \"Alice score: \" << scores[\"Alice\"] << endl;\n    cout << \"Function pointer result (2+3): \" << f(2, 3) << endl;\n\n    return 0;\n}",
        "output": "bigNum: 1234567890\nVector size: 3\nAlice score: 95\nFunction pointer result (2+3): 5",
        "explanation": "typedef long long ulli and using StringMap = map<string, int> simplify verbose type names. MathFunc aliases function pointers int (*)(int, int).",
    },
    "fill_blanks": {
        "question": "Complete the typedef and modern C++ using alias snippet:",
        "answers": ["typedef", "using", "vector", "long long"],
        "options": ["typedef", "using", "vector", "long long", "struct", "class"],
    },
    "compiler": {
        "title": "C++ typedef and using Aliases Sandbox",
        "question": "Arrange lines to create a typedef ulli for long long and a using alias vInt for vector<int>.",
        "starter_code": "#include <iostream>\n#include <vector>\nusing namespace std;\n\ntypedef long long ulli;\nusing vInt = vector<int>;\n\nint main() {\n    ulli num = 987654321;\n    vInt vec = {1, 2, 3};\n    cout << \"num: \" << num << \", vec size: \" << vec.size() << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "#include <vector>",
            "using namespace std;",
            "typedef long long ulli;",
            "using vInt = vector<int>;",
            "int main() {",
            "    ulli num = 987654321;",
            "    vInt vec = {1, 2, 3};",
            "    cout << \"num: \" << num << \", vec size: \" << vec.size() << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What is the primary purpose of typedef and using type aliases in C++?",
            "options": [
                "To create descriptive alternative names for complex or verbose data types",
                "To allocate memory dynamically on heap",
                "To declare virtual functions in abstract base classes",
                "To optimize compiler link times"
            ],
            "answer": "To create descriptive alternative names for complex or verbose data types",
        },
        {
            "question": "What syntax advantage does modern using (C++11) have over traditional typedef?",
            "options": [
                "using supports template aliases (template<typename T> using Alias = ...), whereas typedef does not directly support template aliasing",
                "using executes at runtime",
                "typedef can only be used with primitive integers",
                "There is no difference"
            ],
            "answer": "using supports template aliases (template<typename T> using Alias = ...), whereas typedef does not directly support template aliasing",
        },
        {
            "question": "What does `using Base::Base;` achieve in a derived class in C++11?",
            "options": [
                "Inherits all constructors from the base class into the derived class",
                "Deletes all base class constructors",
                "Overrides all base class member functions",
                "Makes the derived class abstract"
            ],
            "answer": "Inherits all constructors from the base class into the derived class",
        },
        {
            "question": "What is a potential risk of using `using namespace std;` in header files or large codebases?",
            "options": [
                "Name collisions and scope pollution across namespaces",
                "Increases executable file size by 50%",
                "Prevents template specialization",
                "Causes memory leak errors on exit"
            ],
            "answer": "Name collisions and scope pollution across namespaces",
        },
        {
            "question": "How do you declare a type alias for a function pointer returning int and taking two int params using typedef?",
            "options": [
                "typedef int (*func_ptr)(int, int);",
                "typedef func_ptr(int, int) -> int;",
                "typedef int func_ptr(int, int);",
                "typedef (int, int) -> int func_ptr;"
            ],
            "answer": "typedef int (*func_ptr)(int, int);",
        },
    ],
    "theory": {
        "definition": "typedef and using create readable aliases for primitive types, containers, pointers, function pointers, and template types.",
        "why": "Simplifies repetitive complex STL declarations, function pointers, and template syntax.",
        "rules": [
            "typedef: typedef current_type alias_name;",
            "using: using alias_name = current_type;",
            "Prefer using in modern C++ for template support and readable left-to-right syntax.",
            "Use using namespace with care to prevent name collisions.",
        ],
        "examples": [
            "typedef unsigned long long ulong;",
            "using StringVector = vector<string>;",
            "template<typename T> using Ptr = T*;",
        ],
    },
}

CPP_TOPICS[35] = {
    "id": 35,
    "title": "Dynamic Memory Allocation",
    "category": "Dynamic Memory Management",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "Dynamic Memory Allocation in C++ is the manual allocation and management of memory on the Heap (Free Store) during program execution, contrasting with automatic Stack allocation for local variables. It allows allocating objects or arrays whose sizes cannot be determined at compile time. Dynamic heap memory persists across function calls until explicitly released using delete/delete[]. Returning local stack variable addresses leads to undefined behavior, whereas returning heap pointers is safe provided caller deallocates memory.",
    "syntax": "// Allocation on Heap\nint* ptr = new int; // Single integer\nint* arr = new int[10]; // Array of 10 integers\n\n// Deallocation\ndelete ptr; ptr = nullptr;\ndelete[] arr; arr = nullptr;\n\n// Safe function returning heap memory\nint* createHeapVal() {\n    int* p = new int;\n    *p = 10;\n    return p;\n}",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint* createHeapInt() {\n    int* ptr = new int; // Memory allocated on Heap persists after function returns\n    *ptr = 42;\n    return ptr;\n}\n\nint main() {\n    int* p = createHeapInt();\n    cout << \"Dynamically allocated value on heap: \" << *p << endl;\n\n    // Modifying heap array\n    int* arr = new int[5];\n    *(arr + 2) = 10;\n    cout << \"Array 3rd element: \" << arr[2] << endl;\n\n    // Proper deallocation\n    delete p;\n    p = nullptr;\n\n    delete[] arr;\n    arr = nullptr;\n\n    return 0;\n}",
        "output": "Dynamically allocated value on heap: 42\nArray 3rd element: 10",
        "explanation": "createHeapInt() allocates an int on the Heap. The memory remains valid after function returns until explicit delete p; deallocates it. Array arr is freed with delete[].",
    },
    "fill_blanks": {
        "question": "Complete the dynamic heap memory allocation, element access, and deallocation snippet:",
        "answers": ["new", "Heap", "delete[]", "nullptr"],
        "options": ["new", "Heap", "delete[]", "nullptr", "Stack", "malloc"],
    },
    "compiler": {
        "title": "C++ Dynamic Memory Allocation Sandbox",
        "question": "Arrange lines to dynamically allocate an array of 5 integers on heap, assign element 2 to 10, print, and deallocate.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int* arr = new int[5];\n    *(arr + 2) = 10;\n    cout << \"Element 2: \" << arr[2] << endl;\n    delete[] arr;\n    arr = nullptr;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int* arr = new int[5];",
            "    *(arr + 2) = 10;",
            "    cout << \"Element 2: \" << arr[2] << endl;",
            "    delete[] arr;",
            "    arr = nullptr;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "Where is dynamically allocated memory stored in C++ runtime architecture?",
            "options": ["On the Heap (Free Store)", "On the Stack", "In CPU Registers", "In static data segment"],
            "answer": "On the Heap (Free Store)",
        },
        {
            "question": "What happens when a function returns the memory address of a local automatic variable defined on the Stack?",
            "options": [
                "Accessing it causes undefined behavior because local stack variables are destroyed when function scope ends",
                "It automatically moves to heap memory",
                "The compiler creates a global copy",
                "It compiles to a null pointer"
            ],
            "answer": "Accessing it causes undefined behavior because local stack variables are destroyed when function scope ends",
        },
        {
            "question": "How does heap memory allocated inside a function behave when the function returns?",
            "options": [
                "Heap memory persists across function calls until explicitly deallocated by the programmer",
                "Heap memory is destroyed automatically on function exit",
                "Heap memory converts to a reference",
                "Heap memory throws bad_alloc exception"
            ],
            "answer": "Heap memory persists across function calls until explicitly deallocated by the programmer",
        },
        {
            "question": "What is the consequence of forgetting to deallocate heap memory before losing all pointers pointing to it?",
            "options": [
                "A memory leak occurs, permanently consuming system RAM until program termination",
                "The program accelerates execution speed",
                "The OS automatically garbage collects the memory",
                "A segmentation fault occurs immediately"
            ],
            "answer": "A memory leak occurs, permanently consuming system RAM until program termination",
        },
        {
            "question": "Why should a pointer be set to nullptr immediately after calling delete or delete[]?",
            "options": [
                "To prevent dangling pointers and guard against accidental double deletion",
                "To increase pointer memory size to 16 bytes",
                "To force immediate OS garbage collection",
                "To allow pointer re-initialization with malloc"
            ],
            "answer": "To prevent dangling pointers and guard against accidental double deletion",
        },
    ],
    "theory": {
        "definition": "Dynamic memory allocation allocates memory on the Heap at runtime using new/delete rather than fixed Stack sizes.",
        "why": "Essential for runtime-sized arrays, dynamic data structures (linked lists, trees), and persistent objects spanning function lifetimes.",
        "rules": [
            "Stack memory is automatic; Heap memory is manual.",
            "Pair new with delete, and new[] with delete[].",
            "Always set pointers to nullptr after deallocation.",
        ],
        "examples": [
            "int* p = new int(10); delete p; p = nullptr;",
            "int* arr = new int[5]; delete[] arr; arr = nullptr;",
        ],
    },
}

CPP_TOPICS[36] = {
    "id": 36,
    "title": "new and delete",
    "category": "Dynamic Memory Management",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "The new operator in C++ requests memory allocation on the Heap, calls constructors for objects, and returns a typed pointer. The delete operator calls destructors and releases heap memory back to the operating system. Single object allocations (new T(val)) must be paired with delete ptr, while array allocations (new T[size]{...}) must be paired with delete[] arr. If allocation fails due to insufficient memory, new throws std::bad_alloc by default or returns nullptr when used with new (nothrow). Placement new constructs objects in pre-allocated memory buffers without allocating new heap storage.",
    "syntax": "// Single Object Allocation\nT* ptr = new T(init_value);\ndelete ptr; ptr = nullptr;\n\n// Array Allocation\nT* arr = new T[size]{val1, val2};\ndelete[] arr; arr = nullptr;\n\n// Nothrow Allocation\nint* p = new (nothrow) int;\nif (p == nullptr) { /* allocation failed */ }\n\n// Placement new\nchar buffer[sizeof(MyClass)];\nMyClass* obj = new (buffer) MyClass();",
    "example": {
        "code": "#include <iostream>\n#include <new>\nusing namespace std;\n\nint main() {\n    // 1. Single object allocation & initialization\n    int* nptr = new int(6);\n    cout << \"Single Heap Int: \" << *nptr << \" at address \" << nptr << endl;\n    delete nptr;\n    nptr = nullptr;\n\n    // 2. Dynamic Array allocation & initialization\n    int* arr = new int[5]{10, 20, 30, 40, 50};\n    cout << \"Array elements: \";\n    for (int i = 0; i < 5; i++) {\n        cout << arr[i] << \" \";\n    }\n    cout << endl;\n    delete[] arr;\n    arr = nullptr;\n\n    // 3. Handling allocation failure with nothrow\n    int* safePtr = new (nothrow) int[100];\n    if (safePtr != nullptr) {\n        cout << \"Nothrow allocation successful!\" << endl;\n        delete[] safePtr;\n        safePtr = nullptr;\n    }\n\n    return 0;\n}",
        "output": "Single Heap Int: 6 at address 0xb52dc20\nArray elements: 10 20 30 40 50 \nNothrow allocation successful!",
        "explanation": "new int(6) allocates a single int initialized to 6. new int[5]{...} allocates an array freed via delete[]. new (nothrow) returns nullptr instead of throwing std::bad_alloc on failure.",
    },
    "fill_blanks": {
        "question": "Complete the new operator, delete[], bad_alloc handling, and nothrow snippet:",
        "answers": ["new", "delete[]", "bad_alloc", "nothrow"],
        "options": ["new", "delete[]", "bad_alloc", "nothrow", "malloc", "free"],
    },
    "compiler": {
        "title": "C++ new and delete Operators Sandbox",
        "question": "Arrange lines to dynamically allocate a single integer initialized to 10 with new, print it, delete it, and nullify pointer.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int* ptr = new int(10);\n    cout << \"Value: \" << *ptr << endl;\n    delete ptr;\n    ptr = nullptr;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "int main() {",
            "    int* ptr = new int(10);",
            "    cout << \"Value: \" << *ptr << endl;",
            "    delete ptr;",
            "    ptr = nullptr;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What exception type does the new operator throw by default when dynamic memory allocation fails?",
            "options": ["std::bad_alloc", "std::out_of_range", "std::runtime_error", "std::invalid_argument"],
            "answer": "std::bad_alloc",
        },
        {
            "question": "How can you prevent new from throwing an exception on allocation failure and instead return nullptr?",
            "options": ["Use new (nothrow) from <new> header", "Use try-catch block only", "Use malloc()", "Use delete (nothrow)"],
            "answer": "Use new (nothrow) from <new> header",
        },
        {
            "question": "What happens if memory allocated with new[] (array allocation) is freed using scalar delete instead of delete[]?",
            "options": [
                "Causes undefined behavior and potential heap corruption because destructors/size metadata are not properly invoked",
                "It works identically without any issue",
                "It automatically converts to delete[]",
                "It throws a compile-time warning only"
            ],
            "answer": "Causes undefined behavior and potential heap corruption because destructors/size metadata are not properly invoked",
        },
        {
            "question": "What is Placement new in C++?",
            "options": [
                "Constructs an object in an already allocated memory block without requesting new heap memory",
                "Allocates memory on secondary hard drive storage",
                "Deallocates memory automatically after 5 seconds",
                "Translates C++ new to C malloc"
            ],
            "answer": "Constructs an object in an already allocated memory block without requesting new heap memory",
        },
        {
            "question": "Why is mixing C memory functions (malloc/free) with C++ memory operators (new/delete) considered dangerous?",
            "options": [
                "Because malloc does not call constructors and free does not call destructors, causing resource leaks and undefined behavior",
                "Because malloc allocates 8 bytes while new allocates 4 bytes",
                "Because free returns a pointer while delete returns void",
                "There is no danger"
            ],
            "answer": "Because malloc does not call constructors and free does not call destructors, causing resource leaks and undefined behavior",
        },
    ],
    "theory": {
        "definition": "new allocates heap memory and invokes constructors; delete invokes destructors and deallocates heap memory.",
        "why": "Provides object-oriented dynamic memory allocation integrated with class object lifecycles.",
        "rules": [
            "Match new with delete.",
            "Match new[] with delete[].",
            "Do not mix new/delete with malloc/free.",
            "Placement new constructs objects in pre-allocated buffers (new (buffer) Object()).",
        ],
        "examples": [
            "int* p = new int(5); delete p;",
            "int* a = new (nothrow) int[10]; if (a) delete[] a;",
        ],
    },
}

CPP_TOPICS[37] = {
    "id": 37,
    "title": "Memory Leaks",
    "category": "Dynamic Memory Management",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "A memory leak in C++ occurs when dynamically allocated heap memory (new/new[]) is never deallocated (delete/delete[]) before all pointers to it are lost or go out of scope. Because C++ lacks automatic garbage collection, leaked memory remains occupied until program termination, causing gradual RAM consumption, degraded performance, resource exhaustion, and system crashes. Common causes include missing delete, early function returns, pointer reassignment without freeing, and dangling pointers. Leaks are avoided using RAII, smart pointers (std::unique_ptr, std::shared_ptr), and detected via tools like Valgrind and AddressSanitizer (ASan).",
    "syntax": "// Memory Leak Example\nvoid leak() {\n    int* ptr = new int[100]; // Heap allocation\n    return; // ptr goes out of scope, 100 ints leaked!\n}\n\n// Prevention using RAII / Smart Pointers\n#include <memory>\nvoid safe() {\n    std::unique_ptr<int[]> ptr = std::make_unique<int[]>(100);\n    // Automatically deleted when ptr goes out of scope!\n}",
    "example": {
        "code": "#include <iostream>\n#include <memory>\nusing namespace std;\n\nvoid leakMemory() {\n    int* leakedPtr = new int[10];\n    // Missing delete[] leakedPtr causes memory leak!\n}\n\nvoid safeMemory() {\n    // Smart pointer automatically deallocates heap array on scope exit (RAII)\n    unique_ptr<int[]> safePtr(new int[10]);\n    safePtr[0] = 100;\n    cout << \"Safe smart pointer value: \" << safePtr[0] << endl;\n}\n\nint main() {\n    leakMemory();\n    cout << \"leakMemory() left 10 ints leaked on heap!\" << endl;\n\n    safeMemory();\n    cout << \"safeMemory() automatically deallocated memory on exit!\" << endl;\n    return 0;\n}",
        "output": "leakMemory() left 10 ints leaked on heap!\nSafe smart pointer value: 100\nsafeMemory() automatically deallocated memory on exit!",
        "explanation": "leakMemory() allocates heap memory without calling delete[]. When function scope exits, pointer is lost, leaking RAM. safeMemory() uses std::unique_ptr which automatically deletes memory on scope exit.",
    },
    "fill_blanks": {
        "question": "Complete the memory leak cause, RAII smart pointer prevention, and detection tool snippet:",
        "answers": ["new", "unique_ptr", "RAII", "Valgrind"],
        "options": ["new", "unique_ptr", "RAII", "Valgrind", "malloc", "Stack"],
    },
    "compiler": {
        "title": "C++ Memory Leaks Sandbox",
        "question": "Arrange lines to demonstrate safe dynamic memory management using std::unique_ptr.",
        "starter_code": "#include <iostream>\n#include <memory>\nusing namespace std;\n\nint main() {\n    unique_ptr<int> ptr(new int(50));\n    cout << \"Value: \" << *ptr << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "#include <memory>",
            "using namespace std;",
            "int main() {",
            "    unique_ptr<int> ptr(new int(50));",
            "    cout << \"Value: \" << *ptr << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What defines a memory leak in C++?",
            "options": [
                "Dynamically allocated heap memory is not deallocated before all pointers referencing it go out of scope or are overwritten",
                "Stack memory is deallocated prematurely",
                "A pointer is initialized to nullptr",
                "A function takes more than 3 arguments"
            ],
            "answer": "Dynamically allocated heap memory is not deallocated before all pointers referencing it go out of scope or are overwritten",
        },
        {
            "question": "Why are memory leaks especially dangerous in long-running software like web servers or operating system daemons?",
            "options": [
                "Because leaked memory continuously accumulates over time, eventually depleting system RAM and causing server crashes",
                "Because leaks increase CPU temperature",
                "Because leaks modify hard drive files",
                "Because leaks prevent compiler optimization"
            ],
            "answer": "Because leaked memory continuously accumulates over time, eventually depleting system RAM and causing server crashes",
        },
        {
            "question": "What modern C++ design idiom (RAII) and feature eliminate manual delete calls to prevent memory leaks?",
            "options": [
                "Resource Acquisition Is Initialization (RAII) using Smart Pointers (std::unique_ptr, std::shared_ptr)",
                "C-style malloc/free",
                "Global namespace directives",
                "Macro functions"
            ],
            "answer": "Resource Acquisition Is Initialization (RAII) using Smart Pointers (std::unique_ptr, std::shared_ptr)",
        },
        {
            "question": "What happens if a pointer holding dynamically allocated memory is reassigned (ptr = new_address) without freeing the old address first?",
            "options": [
                "The original memory block is orphaned and becomes a memory leak",
                "The OS frees the original memory automatically",
                "The pointer holds both memory addresses simultaneously",
                "The compiler throws a syntax error"
            ],
            "answer": "The original memory block is orphaned and becomes a memory leak",
        },
        {
            "question": "Which tools are commonly used by C++ developers to detect memory leaks and invalid memory accesses during execution?",
            "options": [
                "Valgrind and AddressSanitizer (ASan)",
                "GDB and Makefile",
                "GCC and Clang",
                "Doxygen and CMake"
            ],
            "answer": "Valgrind and AddressSanitizer (ASan)",
        },
    ],
    "theory": {
        "definition": "A memory leak is un-freed heap memory whose referencing pointer has been destroyed or overwritten.",
        "why": "Leads to RAM exhaustion, degraded system performance, and application crashes.",
        "rules": [
            "Every new must have a matching delete.",
            "Use smart pointers (unique_ptr, shared_ptr) for automatic memory cleanup.",
            "Assign nullptr after delete to avoid dangling pointers and double deletions.",
            "Use Valgrind or ASan to detect memory leaks.",
        ],
        "examples": [
            "int* p = new int[10]; delete[] p; // Prevents leak",
            "unique_ptr<int[]> p = make_unique<int[]>(10); // RAII safe",
        ],
    },
}

CPP_TOPICS[38] = {
    "id": 38,
    "title": "Object-Oriented Programming (OOP)",
    "category": "Object-Oriented Programming (OOP)",
    "difficulty": "Intermediate",
    "duration": "35 min",
    "concept": "Object-Oriented Programming (OOP) is a programming paradigm organizing code around classes (blueprints) and objects (instances). It models real-world entities through four core pillars: Abstraction (hiding implementation details), Encapsulation (binding data and functions while restricting direct access), Inheritance (reusing base class properties in derived classes), and Polymorphism ('many forms', early/late binding). Class relationships include Association (uses-a), Aggregation (weak has-a), and Composition (strong has-a ownership).",
    "syntax": "class Car {\nprivate:\n    string brand;\npublic:\n    Car(string b) : brand(b) {}\n    void drive() { cout << \"Driving \" << brand; }\n};\n\nCar c1(\"BMW\");\nc1.drive();",
    "example": {
        "code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nclass Car {\nprivate:\n    string brand;\n\npublic:\n    Car(string b) : brand(b) {}\n    void display() {\n        cout << \"Car Brand: \" << brand << endl;\n    }\n};\n\nint main() {\n    Car car1(\"Tesla\");\n    car1.display();\n    return 0;\n}",
        "output": "Car Brand: Tesla",
        "explanation": "Car represents a class blueprint. car1 is an object instance holding state (\"Tesla\") and executing member behavior display().",
    },
    "fill_blanks": {
        "question": "Complete the OOP core pillar definitions and class instance creation snippet:",
        "answers": ["class", "Car", "Encapsulation", "Polymorphism"],
        "options": ["class", "Car", "Encapsulation", "Polymorphism", "struct", "void"],
    },
    "compiler": {
        "title": "C++ OOP Overview Sandbox",
        "question": "Arrange lines to create class Car with brand property, instantiate car1, and display brand.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nclass Car {\npublic:\n    string brand;\n    void show() { cout << \"Brand: \" << brand << endl; }\n};\n\nint main() {\n    Car car1;\n    car1.brand = \"BMW\";\n    car1.show();\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "class Car {",
            "public:",
            "    string brand;",
            "    void show() { cout << \"Brand: \" << brand << endl; }",
            "};",
            "int main() {",
            "    Car car1;",
            "    car1.brand = \"BMW\";",
            "    car1.show();",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What are the 4 fundamental pillars of Object-Oriented Programming?",
            "options": [
                "Abstraction, Encapsulation, Inheritance, and Polymorphism",
                "Variables, Functions, Pointers, and Arrays",
                "Compilation, Linking, Execution, and Debugging",
                "Stack, Heap, Registers, and Cache"
            ],
            "answer": "Abstraction, Encapsulation, Inheritance, and Polymorphism",
        },
        {
            "question": "What distinguishes Composition from Aggregation class relationships?",
            "options": [
                "Composition represents a strong ownership relationship where child lifetime depends on parent, whereas Aggregation is weak ownership with independent lifetimes",
                "Aggregation requires virtual functions",
                "Composition can only be used with templates",
                "There is no difference"
            ],
            "answer": "Composition represents a strong ownership relationship where child lifetime depends on parent, whereas Aggregation is weak ownership with independent lifetimes",
        },
        {
            "question": "What feature of OOP protects internal object state from unauthorized external modification?",
            "options": [
                "Encapsulation using private access specifiers",
                "Dynamic polymorphism",
                "Template specialization",
                "Function overloading"
            ],
            "answer": "Encapsulation using private access specifiers",
        },
        {
            "question": "What defines a Class in C++ OOP?",
            "options": [
                "A user-defined data type serving as a blueprint for creating objects with data members and member functions",
                "An active process running in RAM",
                "A hardware CPU instruction",
                "A preprocessor macro directive"
            ],
            "answer": "A user-defined data type serving as a blueprint for creating objects with data members and member functions",
        },
        {
            "question": "What represents the State of an object in C++?",
            "options": [
                "The current values assigned to its data members in memory",
                "The member function execution speed",
                "The pointer address size",
                "The header include statements"
            ],
            "answer": "The current values assigned to its data members in memory",
        },
    ],
    "theory": {
        "definition": "OOP organizes programs around classes and objects modeling real-world entities with state, behavior, and identity.",
        "why": "Promotes modularity, code reusability, maintenance efficiency, and enterprise scalability.",
        "rules": [
            "4 Pillars: Abstraction, Encapsulation, Inheritance, Polymorphism.",
            "Objects have State (data), Behavior (functions), and Identity (unique address).",
            "Class relationships: Association (uses-a), Aggregation (weak has-a), Composition (strong has-a).",
        ],
        "examples": [
            "class Car { string model; }; Car c1;",
            "class Animal { public: virtual void sound() = 0; };",
        ],
    },
}

CPP_TOPICS[39] = {
    "id": 39,
    "title": "Classes and Objects",
    "category": "Object-Oriented Programming (OOP)",
    "difficulty": "Intermediate",
    "duration": "40 min",
    "concept": "A Class in C++ is a user-defined blueprint combining data members (state variables) and member functions (behavioral methods) into a single unit. An Object is an instantiated instance of a class allocated in memory. Class members are accessed using the dot operator (.) for objects (obj.func()) or arrow operator (->) for pointers. Member functions can be defined inside the class or outside using the scope resolution operator (::).",
    "syntax": "class ClassName {\npublic:\n    data_type member1;\n    void funcName(); // declaration\n};\n\nvoid ClassName::funcName() { /* definition */ }\n\nClassName obj;\nobj.member1 = val;\nobj.funcName();",
    "example": {
        "code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nclass Dog {\npublic:\n    string name;\n    string breed;\n\n    void display(); // Member function declared\n};\n\n// Definition outside class using scope resolution operator ::\nvoid Dog::display() {\n    cout << \"Dog Name: \" << name << \", Breed: \" << breed << endl;\n}\n\nint main() {\n    Dog tuffy;\n    tuffy.name = \"Tuffy\";\n    tuffy.breed = \"Papillon\";\n    tuffy.display();\n\n    Dog* ptr = &tuffy;\n    ptr->name = \"Max\";\n    ptr->display();\n    return 0;\n}",
        "output": "Dog Name: Tuffy, Breed: Papillon\nDog Name: Max, Breed: Papillon",
        "explanation": "Dog class declares data members and function display(). display() is defined outside with Dog::display(). tuffy.display() uses dot operator; ptr->display() uses arrow operator.",
    },
    "fill_blanks": {
        "question": "Complete the class definition, scope resolution operator, object instantiation, and arrow operator snippet:",
        "answers": ["class", "::", ".", "->"],
        "options": ["class", "::", ".", "->", "struct", "virtual"],
    },
    "compiler": {
        "title": "C++ Classes and Objects Sandbox",
        "question": "Arrange lines to define Dog class with display() function, create object tuffy, and print details.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nclass Dog {\npublic:\n    string name;\n    void show() { cout << \"Dog: \" << name << endl; }\n};\n\nint main() {\n    Dog tuffy;\n    tuffy.name = \"Tuffy\";\n    tuffy.show();\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "class Dog {",
            "public:",
            "    string name;",
            "    void show() { cout << \"Dog: \" << name << endl; }",
            "};",
            "int main() {",
            "    Dog tuffy;",
            "    tuffy.name = \"Tuffy\";",
            "    tuffy.show();",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What is the relationship between a Class and an Object in C++?",
            "options": [
                "A Class is a blueprint/template; an Object is an instantiated instance of that blueprint in memory",
                "An Object is a blueprint; a Class is an instance",
                "They are identical terms with no distinction",
                "A Class runs on GPU; an Object runs on CPU"
            ],
            "answer": "A Class is a blueprint/template; an Object is an instantiated instance of that blueprint in memory",
        },
        {
            "question": "Which operator is used to define member functions outside the class declaration?",
            "options": [":: (Scope resolution operator)", ". (Dot operator)", "-> (Arrow operator)", ": (Colon operator)"],
            "answer": ":: (Scope resolution operator)",
        },
        {
            "question": "How do multiple objects of the same class behave regarding memory allocation for data members?",
            "options": [
                "Each object gets its own separate memory allocation for data members",
                "All objects share the exact same memory for data members",
                "Data members are allocated on disk",
                "Objects consume 0 bytes of memory"
            ],
            "answer": "Each object gets its own separate memory allocation for data members",
        },
        {
            "question": "What operator is used to access class members using an object pointer (Dog* ptr)?",
            "options": ["-> (Arrow operator)", ". (Dot operator)", ":: (Scope resolution operator)", "* (Dereference operator)"],
            "answer": "-> (Arrow operator)",
        },
        {
            "question": "What default access specifier applies to members in a C++ class if none is specified?",
            "options": ["private", "public", "protected", "internal"],
            "answer": "private",
        },
    ],
    "theory": {
        "definition": "Classes are blueprints encapsulating state and behavior; Objects are instances allocated in memory.",
        "why": "Core foundation of C++ object-oriented design and abstraction.",
        "rules": [
            "Class members default to private.",
            "Define functions outside with ReturnType ClassName::func() {}.",
            "Access with . for objects and -> for pointers.",
        ],
        "examples": [
            "class Student { string name; }; Student s1;",
            "void Student::show() { cout << name; }",
        ],
    },
}

CPP_TOPICS[40] = {
    "id": 40,
    "title": "Constructors",
    "category": "Object-Oriented Programming (OOP)",
    "difficulty": "Intermediate",
    "duration": "35 min",
    "concept": "A Constructor is a special member function automatically invoked when an object of a class is created. It shares the exact name as the class, has no return type (not even void), and initializes data members. Types include: Default Constructor (no parameters; generated by compiler if no constructor is defined), Parameterized Constructor (takes arguments), Copy Constructor (Class(const Class& obj)), and Move Constructor (C++11: Class(Class&& obj) transferring resources via rvalue references). Destructors (~ClassName()) release resources on object destruction.",
    "syntax": "class Person {\npublic:\n    int age;\n    Person() : age(0) {} // Default\n    Person(int a) : age(a) {} // Parameterized\n    Person(const Person& p) : age(p.age) {} // Copy\n    Person(Person&& p) noexcept : age(p.age) {} // Move\n    ~Person() {} // Destructor\n};",
    "example": {
        "code": "#include <iostream>\n#include <utility>\nusing namespace std;\n\nclass Person {\npublic:\n    int age;\n\n    // 1. Default Constructor\n    Person() { age = 0; }\n\n    // 2. Parameterized Constructor\n    Person(int a) { age = a; }\n\n    // 3. Copy Constructor\n    Person(const Person& p) { age = p.age; }\n\n    // 4. Move Constructor (C++11)\n    Person(Person&& p) noexcept {\n        age = p.age;\n        p.age = 0;\n        cout << \"Move Constructor called!\" << endl;\n    }\n\n    // Destructor\n    ~Person() {\n        // Destructor cleanup\n    }\n};\n\nint main() {\n    Person p1(25); // Parameterized\n    Person p2(p1); // Copy\n    Person p3(move(p1)); // Move\n\n    cout << \"p2 age: \" << p2.age << \", p3 age: \" << p3.age << endl;\n    return 0;\n}",
        "output": "Move Constructor called!\np2 age: 25, p3 age: 25",
        "explanation": "Person defines default, parameterized, copy, and move constructors. p2(p1) invokes copy constructor. move(p1) invokes move constructor transferring state.",
    },
    "fill_blanks": {
        "question": "Complete constructor declarations for default, parameterized, copy, and destructor snippet:",
        "answers": ["Person", "const Person&", "~Person", "move"],
        "options": ["Person", "const Person&", "~Person", "move", "virtual", "void"],
    },
    "compiler": {
        "title": "C++ Constructors Sandbox",
        "question": "Arrange lines to define class A with parameterized constructor and create object a with value 10.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nclass A {\npublic:\n    int val;\n    A(int x) { val = x; }\n};\n\nint main() {\n    A a(10);\n    cout << \"Val: \" << a.val << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "class A {",
            "public:",
            "    int val;",
            "    A(int x) { val = x; }",
            "};",
            "int main() {",
            "    A a(10);",
            "    cout << \"Val: \" << a.val << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What is a distinguishing characteristic of a constructor in C++?",
            "options": [
                "It has the exact same name as the class and has no return type (not even void)",
                "It must always return int 0",
                "It must be declared static",
                "It requires virtual specifier"
            ],
            "answer": "It has the exact same name as the class and has no return type (not even void)",
        },
        {
            "question": "What happens if a developer defines a parameterized constructor in a class but does NOT define a default constructor?",
            "options": [
                "The compiler will NOT generate an automatic default constructor, requiring explicit arguments when instantiating objects",
                "The compiler generates default constructor anyway",
                "A syntax error occurs during compilation immediately",
                "The class becomes abstract"
            ],
            "answer": "The compiler will NOT generate an automatic default constructor, requiring explicit arguments when instantiating objects",
        },
        {
            "question": "What argument type is expected by a Copy Constructor Class(const Class& obj)?",
            "options": [
                "A constant reference to an object of the same class",
                "A pointer to integer",
                "An rvalue reference",
                "A void pointer"
            ],
            "answer": "A constant reference to an object of the same class",
        },
        {
            "question": "What feature introduced in C++11 uses rvalue references Class(Class&& obj) to transfer resources without deep copying?",
            "options": ["Move Constructor", "Copy Constructor", "Default Constructor", "Placement Constructor"],
            "answer": "Move Constructor",
        },
        {
            "question": "What is the primary function of a Destructor ~ClassName()?",
            "options": [
                "To automatically release resources (memory, file handles) when an object goes out of scope or is deleted",
                "To initialize member variables to 0",
                "To copy objects",
                "To create child classes"
            ],
            "answer": "To automatically release resources (memory, file handles) when an object goes out of scope or is deleted",
        },
    ],
    "theory": {
        "definition": "Constructors initialize object state on creation; Destructors clean up resources on destruction.",
        "why": "Guarantees proper object initialization and resource cleanup adhering to RAII.",
        "rules": [
            "Same name as class, no return type.",
            "4 types: Default, Parameterized, Copy, Move.",
            "Defining any constructor suppresses implicit default constructor.",
            "Destructor starts with tilde ~ClassName().",
        ],
        "examples": [
            "Class() {} // Default",
            "Class(int x) : val(x) {} // Parameterized",
            "~Class() {} // Destructor",
        ],
    },
}

CPP_TOPICS[41] = {
    "id": 41,
    "title": "Encapsulation",
    "category": "Object-Oriented Programming (OOP)",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "Encapsulation is the OOP principle of bundling data members and member functions into a single class while restricting direct access to internal state using access specifiers (private, protected). Controlled access is provided through public getter and setter functions, enabling input validation (e.g. setAge(int a) rejecting negative values) and data hiding to safeguard internal state integrity.",
    "syntax": "class Account {\nprivate:\n    double balance;\npublic:\n    double getBalance() const { return balance; }\n    void deposit(double amount) {\n        if (amount > 0) balance += amount;\n    }\n};",
    "example": {
        "code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nclass BankAccount {\nprivate:\n    string owner;\n    double balance;\n\npublic:\n    BankAccount(string o, double initialBalance) {\n        owner = o;\n        balance = (initialBalance >= 0) ? initialBalance : 0;\n    }\n\n    // Getter\n    double getBalance() const {\n        return balance;\n    }\n\n    // Setter with validation\n    void deposit(double amount) {\n        if (amount > 0) {\n            balance += amount;\n            cout << \"Deposited: $\" << amount << endl;\n        }\n    }\n};\n\nint main() {\n    BankAccount account(\"Alice\", 100.0);\n    cout << \"Balance: $\" << account.getBalance() << endl;\n\n    account.deposit(50.0);\n    cout << \"Updated Balance: $\" << account.getBalance() << endl;\n\n    return 0;\n}",
        "output": "Balance: $100\nDeposited: $50\nUpdated Balance: $150",
        "explanation": "balance is private. External access is strictly controlled via public getBalance() and deposit(). deposit() validates amount > 0.",
    },
    "fill_blanks": {
        "question": "Complete the encapsulation private data member and public getter/setter snippet:",
        "answers": ["private", "public", "getBalance", "setBalance"],
        "options": ["private", "public", "getBalance", "setBalance", "protected", "void"],
    },
    "compiler": {
        "title": "C++ Encapsulation Sandbox",
        "question": "Arrange lines to create class Programmer with private name field, setter setName(), and getter getName().",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nclass Programmer {\nprivate:\n    string name;\npublic:\n    void setName(string n) { name = n; }\n    string getName() { return name; }\n};\n\nint main() {\n    Programmer p;\n    p.setName(\"Geek\");\n    cout << \"Name: \" << p.getName() << endl;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "class Programmer {",
            "private:",
            "    string name;",
            "public:",
            "    void setName(string n) { name = n; }",
            "    string getName() { return name; }",
            "};",
            "int main() {",
            "    Programmer p;",
            "    p.setName(\"Geek\");",
            "    cout << \"Name: \" << p.getName() << endl;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "How is encapsulation primarily implemented in C++ classes?",
            "options": [
                "By marking data members as private and providing public getter and setter functions",
                "By defining all member variables as public global variables",
                "By using macro functions",
                "By declaring classes inside main()"
            ],
            "answer": "By marking data members as private and providing public getter and setter functions",
        },
        {
            "question": "What is the primary difference between Data Hiding and Encapsulation?",
            "options": [
                "Data Hiding restricts direct data access for security; Encapsulation is the broader wrapping of data and methods into a single class unit",
                "Data Hiding uses templates; Encapsulation uses macros",
                "They are opposite concepts",
                "Data Hiding executes at runtime; Encapsulation executes at compile time"
            ],
            "answer": "Data Hiding restricts direct data access for security; Encapsulation is the broader wrapping of data and methods into a single class unit",
        },
        {
            "question": "Why are setter functions advantageous over public member variables?",
            "options": [
                "Setters allow data validation before modifying object state",
                "Setters use less RAM",
                "Setters convert int to string automatically",
                "Setters eliminate constructors"
            ],
            "answer": "Setters allow data validation before modifying object state",
        },
        {
            "question": "What access specifier prevents external code from accessing class members while allowing access inside derived classes?",
            "options": ["protected", "private", "public", "internal"],
            "answer": "protected",
        },
        {
            "question": "What is a best practice for constant property values like ID numbers in encapsulated classes?",
            "options": [
                "Avoid providing setter functions for immutable fields",
                "Make setter functions return float",
                "Declare variables as public",
                "Use pointer arrays"
            ],
            "answer": "Avoid providing setter functions for immutable fields",
        },
    ],
    "theory": {
        "definition": "Encapsulation wraps data and methods into a class while controlling access via getters and setters.",
        "why": "Guarantees state integrity, hides implementation details, and enables input validation.",
        "rules": [
            "Data members should be private.",
            "Use public getters and setters.",
            "Validate inputs inside setters.",
        ],
        "examples": [
            "class Bank { private: double balance; public: double getBal() const { return balance; } };",
        ],
    },
}

CPP_TOPICS[42] = {
    "id": 42,
    "title": "Polymorphism",
    "category": "Object-Oriented Programming (OOP)",
    "difficulty": "Advanced",
    "duration": "45 min",
    "concept": "Polymorphism in C++ means 'many forms', enabling a single interface to behave differently depending on object context. Divided into Compile-Time Polymorphism (Static/Early Binding: Function Overloading and Operator Overloading) and Runtime Polymorphism (Dynamic/Late Binding: Function Overriding via virtual functions and vtables). Base class pointers (Base* ptr) invoke derived class overrides when pointed to derived objects.",
    "syntax": "// Compile-time: Function & Operator Overloading\nvoid add(int a, int b);\nvoid add(double a, double b);\nComplex operator+(const Complex& obj);\n\n// Runtime: Virtual Functions & Overriding\nclass Base {\npublic:\n    virtual void show() { cout << \"Base\"; }\n};\nclass Derived : public Base {\npublic:\n    void show() override { cout << \"Derived\"; }\n};\n\nBase* ptr = new Derived();\nptr->show(); // Prints \"Derived\" at runtime",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nclass Base {\npublic:\n    // Virtual function enables dynamic binding\n    virtual void display() {\n        cout << \"Base class display\" << endl;\n    }\n};\n\nclass Derived : public Base {\npublic:\n    void display() override {\n        cout << \"Derived class display\" << endl;\n    }\n};\n\nint main() {\n    Base* ptr;\n    Derived obj;\n    ptr = &obj;\n\n    // Dynamic dispatch calls Derived version at runtime\n    ptr->display();\n    return 0;\n}",
        "output": "Derived class display",
        "explanation": "display() is declared virtual in Base and overridden in Derived. Base* ptr = &obj resolves ptr->display() dynamically to Derived at runtime.",
    },
    "fill_blanks": {
        "question": "Complete the compile-time and runtime polymorphism snippet:",
        "answers": ["virtual", "override", "operator+", "Base*"],
        "options": ["virtual", "override", "operator+", "Base*", "struct", "static"],
    },
    "compiler": {
        "title": "C++ Polymorphism Sandbox",
        "question": "Arrange lines to implement virtual function display in Base, override it in Derived, and invoke via Base pointer.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nclass Base {\npublic:\n    virtual void show() { cout << \"Base\" << endl; }\n};\nclass Derived : public Base {\npublic:\n    void show() override { cout << \"Derived\" << endl; }\n};\n\nint main() {\n    Base* ptr = new Derived();\n    ptr->show();\n    delete ptr;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "class Base {",
            "public:",
            "    virtual void show() { cout << \"Base\" << endl; }",
            "};",
            "class Derived : public Base {",
            "public:",
            "    void show() override { cout << \"Derived\" << endl; }",
            "};",
            "int main() {",
            "    Base* ptr = new Derived();",
            "    ptr->show();",
            "    delete ptr;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "Which mechanisms implement Compile-Time (Static) Polymorphism in C++?",
            "options": [
                "Function Overloading and Operator Overloading",
                "Virtual functions and Function Overriding",
                "Multiple inheritance",
                "Abstract classes"
            ],
            "answer": "Function Overloading and Operator Overloading",
        },
        {
            "question": "What keyword must be used in the base class to enable Runtime (Dynamic) Polymorphism?",
            "options": ["virtual", "override", "static", "inline"],
            "answer": "virtual",
        },
        {
            "question": "Which C++ operators CANNOT be overloaded?",
            "options": ["::, ., .*, ?:, and sizeof", "+, -, *, /, and %", "==, !=, >, <, and >=", "[], (), ->, and ="],
            "answer": "::, ., .*, ?:, and sizeof",
        },
        {
            "question": "What mechanism does the compiler use under the hood to resolve virtual function calls at runtime?",
            "options": [
                "Virtual Tables (vtables) and Virtual Pointers (vptrs)",
                "Stack frames and registers",
                "Global hash maps",
                "Template instantiations"
            ],
            "answer": "Virtual Tables (vtables) and Virtual Pointers (vptrs)",
        },
        {
            "question": "What is Function Overriding in C++?",
            "options": [
                "A derived class providing its own implementation of a virtual function defined in the base class",
                "Defining two functions with same name but different parameters in same scope",
                "Overloading operator+",
                "Hiding private variables"
            ],
            "answer": "A derived class providing its own implementation of a virtual function defined in the base class",
        },
    ],
    "theory": {
        "definition": "Polymorphism allows a single interface to take multiple forms through static or dynamic binding.",
        "why": "Provides loose coupling, extensibility, and unified interfaces across class hierarchies.",
        "rules": [
            "Compile-time: Function/Operator overloading.",
            "Runtime: virtual functions + override in derived class.",
            "Requires Base class pointer/reference for dynamic dispatch.",
        ],
        "examples": [
            "virtual void sound(); // Base",
            "void sound() override; // Derived",
        ],
    },
}

CPP_TOPICS[43] = {
    "id": 43,
    "title": "Inheritance",
    "category": "Object-Oriented Programming (OOP)",
    "difficulty": "Advanced",
    "duration": "40 min",
    "concept": "Inheritance in C++ allows a derived class (child) to acquire data members and member functions from a base class (parent), creating an 'is-a' relationship and facilitating code reuse. C++ supports 5 types of inheritance: Single, Multiple (inheriting from 2+ base classes), Multilevel (chain of inheritance), Hierarchical (multiple children from 1 base), and Hybrid (combining types). Multiple inheritance can lead to the Diamond Problem, resolved using virtual inheritance (class Derived : virtual public Base).",
    "syntax": "// Base & Derived\nclass Base { public: void info(); };\nclass SingleDerived : public Base {};\n\n// Multiple Inheritance\nclass MultiDerived : public Base1, public Base2 {};\n\n// Virtual Inheritance (Resolves Diamond Problem)\nclass B1 : virtual public Base {};\nclass B2 : virtual public Base {};\nclass Diamond : public B1, public B2 {};",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nclass Base {\npublic:\n    void baseMsg() {\n        cout << \"Base class method\" << endl;\n    }\n};\n\nclass B1 : virtual public Base {};\nclass B2 : virtual public Base {};\n\n// Diamond Inheritance using Virtual Base Class\nclass Derived : public B1, public B2 {};\n\nint main() {\n    Derived d;\n    d.baseMsg(); // Resolved without ambiguity due to virtual inheritance\n    return 0;\n}",
        "output": "Base class method",
        "explanation": "B1 and B2 inherit Base using virtual public Base. Derived inherits B1 and B2, resolving the Diamond Problem without duplicate Base sub-objects.",
    },
    "fill_blanks": {
        "question": "Complete the single inheritance, multiple inheritance, and virtual inheritance snippet:",
        "answers": ["public", "virtual", "Derived", "Base"],
        "options": ["public", "virtual", "Derived", "Base", "protected", "private"],
    },
    "compiler": {
        "title": "C++ Inheritance Sandbox",
        "question": "Arrange lines to create base class Vehicle, derived class Car, and call inherited Vehicle constructor.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nclass Vehicle {\npublic:\n    Vehicle() { cout << \"Vehicle created\" << endl; }\n};\nclass Car : public Vehicle {\npublic:\n    Car() { cout << \"Car created\" << endl; }\n};\n\nint main() {\n    Car obj;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "class Vehicle {",
            "public:",
            "    Vehicle() { cout << \"Vehicle created\" << endl; }",
            "};",
            "class Car : public Vehicle {",
            "public:",
            "    Car() { cout << \"Car created\" << endl; }",
            "};",
            "int main() {",
            "    Car obj;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What are the 5 types of inheritance supported in C++?",
            "options": [
                "Single, Multiple, Multilevel, Hierarchical, and Hybrid Inheritance",
                "Primary, Secondary, Tertiary, Quaternary, and Pentary",
                "Public, Private, Protected, Virtual, and Abstract",
                "Static, Dynamic, Compilation, Execution, and Runtime"
            ],
            "answer": "Single, Multiple, Multilevel, Hierarchical, and Hybrid Inheritance",
        },
        {
            "question": "What is the Diamond Problem in C++ inheritance?",
            "options": [
                "Ambiguity occurring when a derived class inherits a base class through multiple paths in hybrid/multiple inheritance",
                "Allocating dynamic memory on 4 CPU cores",
                "Converting abstract classes to interfaces",
                "Multiple constructors called in reverse order"
            ],
            "answer": "Ambiguity occurring when a derived class inherits a base class through multiple paths in hybrid/multiple inheritance",
        },
        {
            "question": "How is the Diamond Problem resolved in C++?",
            "options": [
                "By using virtual inheritance (class B : virtual public Base)",
                "By deleting base constructors",
                "By using static casting",
                "By using typedef"
            ],
            "answer": "By using virtual inheritance (class B : virtual public Base)",
        },
        {
            "question": "What access specifier mode preserves public base members as public and protected base members as protected in derived classes?",
            "options": ["public inheritance mode", "private inheritance mode", "protected inheritance mode", "virtual inheritance mode"],
            "answer": "public inheritance mode",
        },
        {
            "question": "In what order are constructors executed during object creation in a derived class hierarchy?",
            "options": [
                "Base class constructor first, then derived class constructor",
                "Derived class constructor first, then base class constructor",
                "Constructors execute simultaneously in threads",
                "Destructors execute before constructors"
            ],
            "answer": "Base class constructor first, then derived class constructor",
        },
    ],
    "theory": {
        "definition": "Inheritance enables child classes to acquire features from parent classes promoting code reuse and hierarchy.",
        "why": "Models 'is-a' relationships (Dog is an Animal, Car is a Vehicle).",
        "rules": [
            "Syntax: class Derived : access_specifier Base {};.",
            "5 Types: Single, Multiple, Multilevel, Hierarchical, Hybrid.",
            "Use virtual public Base to fix Diamond Problem.",
        ],
        "examples": [
            "class Dog : public Animal {};",
            "class B : virtual public Base {};",
        ],
    },
}

CPP_TOPICS[44] = {
    "id": 44,
    "title": "Abstraction",
    "category": "Object-Oriented Programming (OOP)",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "Abstraction is the OOP principle of exposing only essential features while hiding internal implementation details. In C++, abstraction is achieved using Abstract Classes (classes containing at least one pure virtual function virtual void func() = 0) and Pure Abstract Classes / Interfaces (classes containing only pure virtual functions and a virtual destructor). Abstract classes cannot be instantiated directly (Shape* s = new Rectangle()); derived classes must override all pure virtual functions to become concrete instantiable classes.",
    "syntax": "// Abstract Base Class\nclass Shape {\npublic:\n    virtual double area() = 0; // Pure virtual function\n    virtual ~Shape() {} // Virtual destructor\n};\n\nclass Circle : public Shape {\n    double r;\npublic:\n    Circle(double radius) : r(radius) {}\n    double area() override { return 3.14159 * r * r; }\n};",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\n// Pure Abstract Class (Interface)\nclass Printable {\npublic:\n    virtual void print() = 0; // Pure virtual function\n    virtual ~Printable() {}\n};\n\nclass Document : public Printable {\npublic:\n    void print() override {\n        cout << \"Printing Document...\" << endl;\n    }\n};\n\nint main() {\n    Printable* p = new Document();\n    p->print();\n    delete p;\n    return 0;\n}",
        "output": "Printing Document...",
        "explanation": "Printable is a pure abstract class containing pure virtual function print() = 0. Document implements print(). Base pointer Printable* p invokes Document::print().",
    },
    "fill_blanks": {
        "question": "Complete the pure virtual function declaration, abstract class inheritance, and base pointer snippet:",
        "answers": ["virtual", "= 0", "override", "Printable*"],
        "options": ["virtual", "= 0", "override", "Printable*", "struct", "inline"],
    },
    "compiler": {
        "title": "C++ Abstraction Sandbox",
        "question": "Arrange lines to create abstract class Shape with pure virtual function area(), derive Rectangle, and calculate area.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nclass Shape {\npublic:\n    virtual double area() = 0;\n    virtual ~Shape() {}\n};\nclass Rectangle : public Shape {\n    double w, h;\npublic:\n    Rectangle(double w, double h) : w(w), h(h) {}\n    double area() override { return w * h; }\n};\n\nint main() {\n    Shape* s = new Rectangle(4, 5);\n    cout << \"Area: \" << s->area() << endl;\n    delete s;\n    return 0;\n}",
        "options": [
            "#include <iostream>",
            "using namespace std;",
            "class Shape {",
            "public:",
            "    virtual double area() = 0;",
            "    virtual ~Shape() {}",
            "};",
            "class Rectangle : public Shape {",
            "    double w, h;",
            "public:",
            "    Rectangle(double w, double h) : w(w), h(h) {}",
            "    double area() override { return w * h; }",
            "};",
            "int main() {",
            "    Shape* s = new Rectangle(4, 5);",
            "    cout << \"Area: \" << s->area() << endl;",
            "    delete s;",
            "    return 0;",
            "}"
        ],
    },
    "skill_exa_test": [
        {
            "question": "What makes a class an Abstract Class in C++?",
            "options": [
                "Containing at least one pure virtual function (virtual void func() = 0)",
                "Having all private constructors",
                "Inheriting from 3 base classes",
                "Containing static variables only"
            ],
            "answer": "Containing at least one pure virtual function (virtual void func() = 0)",
        },
        {
            "question": "Can an object of an Abstract Class be instantiated directly (e.g. Shape s;)?",
            "options": [
                "No, abstract classes cannot be instantiated directly",
                "Yes, using default constructor",
                "Yes, if declared in heap memory",
                "Yes, in C++20 standard"
            ],
            "answer": "No, abstract classes cannot be instantiated directly",
        },
        {
            "question": "What syntax is used to declare a Pure Virtual Function in a base class?",
            "options": [
                "virtual ReturnType funcName(params) = 0;",
                "pure virtual funcName();",
                "abstract funcName();",
                "virtual void funcName() = default;"
            ],
            "answer": "virtual ReturnType funcName(params) = 0;",
        },
        {
            "question": "What must a derived class do to become a concrete (instantiable) class when inheriting from an abstract base class?",
            "options": [
                "Implement/override all pure virtual functions inherited from the abstract base class",
                "Declare all data members as private",
                "Add static methods",
                "Use multiple inheritance"
            ],
            "answer": "Implement/override all pure virtual functions inherited from the abstract base class",
        },
        {
            "question": "Why is it important for an abstract base class to have a virtual destructor (virtual ~Base() {})?",
            "options": [
                "To ensure proper derived class destructor invocation when deleting objects via base pointers",
                "To initialize static data members",
                "To allow pure virtual functions",
                "To prevent inheritance"
            ],
            "answer": "To ensure proper derived class destructor invocation when deleting objects via base pointers",
        },
    ],
    "theory": {
        "definition": "Abstraction exposes essential interfaces while hiding internal implementation logic.",
        "why": "Simplifies system design, reduces coupling, and enforces consistent interface contracts.",
        "rules": [
            "Declare pure virtual functions with = 0.",
            "Classes with pure virtual functions are abstract and cannot be instantiated.",
            "Always provide virtual destructors in abstract base classes.",
        ],
        "examples": [
            "virtual void draw() = 0;",
            "Shape* s = new Circle(5.0);",
        ],
    },
}


CPP_TOPICS[45] = {
    "id": 45,
    "title": "Templates",
    "category": "Templates & STL",
    "difficulty": "Advanced",
    "duration": "40 min",
    "concept": "C++ templates enable writing generic, type-safe functions and classes that operate on multiple data types without code duplication. Form the foundation of STL. Supports function templates, class templates, variable templates (C++14), default template arguments, non-type template parameters (compile-time constants), argument deduction (CTAD in C++17), and template metaprogramming (compile-time computation).",
    "syntax": "template <typename T>\nT myMax(T x, T y) { return (x > y) ? x : y; }\n\ntemplate <typename T1, typename T2 = double>\nclass Pair { public: T1 first; T2 second; };",
    "example": {
        "code": "#include <iostream>\n#include <string>\nusing namespace std;\n\ntemplate <typename T>\nT myMax(T x, T y) {\n    return (x > y) ? x : y;\n}\n\ntemplate <typename T1, typename T2>\nclass Geek {\npublic:\n    T1 x; T2 y;\n    Geek(T1 val1, T2 val2) : x(val1), y(val2) {}\n    void getValues() { cout << x << \" \" << y << endl; }\n};\n\ntemplate <int N>\nstruct Factorial {\n    static const int value = N * Factorial<N - 1>::value;\n};\ntemplate <>\nstruct Factorial<0> {\n    static const int value = 1;\n};\n\nint main() {\n    cout << \"Max of 3 and 7 is: \" << myMax<int>(3, 7) << endl;\n    cout << \"Max of 3.5 and 7.5 is: \" << myMax<double>(3.5, 7.5) << endl;\n    cout << \"Max of 'g' and 'e' is: \" << myMax<char>('g', 'e') << endl;\n    Geek<int, string> obj(10, \"Hello\");\n    obj.getValues();\n    cout << \"Factorial of 5 is: \" << Factorial<5>::value << endl;\n    return 0;\n}",
        "output": "Max of 3 and 7 is: 7\nMax of 3.5 and 7.5 is: 7.5\nMax of 'g' and 'e' is: g\n10 Hello\nFactorial of 5 is: 120",
        "explanation": "myMax<T> compiles type-specific function versions for int, double, and char. Geek<T1, T2> stores values of two generic types. Factorial<N> computes factorials recursively at compile time."
    },
    "fill_blanks": {
        "question": "Complete the function template declaration and specialization call:",
        "answers": ["template", "typename", "myMax", "Factorial"],
        "options": ["template", "typename", "myMax", "Factorial", "class", "void"]
    },
    "compiler": {
        "title": "C++ Templates Practice",
        "starter_code": "#include <iostream>\nusing namespace std;\n\ntemplate <typename T>\nT multiply(T a, T b) {\n    return a * b;\n}\n\nint main() {\n    cout << multiply(4, 5) << endl;\n    cout << multiply(2.5, 3.0) << endl;\n    return 0;\n}",
        "question": "Arrange lines to define a template function multiply(T a, T b) and invoke it in main().",
        "options": [
            "template <typename T>",
            "T multiply(T a, T b) { return a * b; }",
            "int main() {",
            "    cout << multiply(4, 5) << endl;",
            "    return 0;",
            "}"
        ]
    },
    "skill_exa_test": [
        {
            "question": "Which keywords are interchangeable in standard C++ template declarations?",
            "options": [
                "typename and class",
                "struct and union",
                "template and inline",
                "const and constexpr"
            ],
            "answer": "typename and class"
        },
        {
            "question": "What is Class Template Argument Deduction (CTAD) introduced in C++17?",
            "options": [
                "The compiler automatically deduces class template parameters from constructor arguments without explicit type syntax",
                "The compiler converts templates into macros",
                "It restricts templates to primitive data types only",
                "It executes template constructors at runtime"
            ],
            "answer": "The compiler automatically deduces class template parameters from constructor arguments without explicit type syntax"
        },
        {
            "question": "What is Template Metaprogramming in C++?",
            "options": [
                "Performing computations at compile time using recursive template structures",
                "Executing C++ code inside a virtual machine at runtime",
                "Generating dynamic HTML templates in memory",
                "Debugging templates using standard GDB breakpoints"
            ],
            "answer": "Performing computations at compile time using recursive template structures"
        },
        {
            "question": "What requirement must non-type template parameters (e.g. template <typename T, int SIZE>) satisfy?",
            "options": [
                "They must be compile-time constant expressions",
                "They must be dynamic runtime heap pointers",
                "They must be float or double variables",
                "They must be initialized inside main()"
            ],
            "answer": "They must be compile-time constant expressions"
        },
        {
            "question": "Why are templates preferred over void* pointers and macros for generic C++ programming?",
            "options": [
                "Templates provide strict compile-time type safety and eliminate runtime casting overhead",
                "Templates make binaries smaller than macros",
                "void* pointers run faster than compiled code",
                "Macros support member functions whereas templates do not"
            ],
            "answer": "Templates provide strict compile-time type safety and eliminate runtime casting overhead"
        }
    ],
    "theory": {
        "definition": "Templates in C++ provide generic programming abstractions allowing functions and classes to work across arbitrary data types with compile-time type safety.",
        "why": "Eliminates code duplication, replaces unsafe macros and void* pointers, and powers the Standard Template Library (STL).",
        "rules": [
            "Use template <typename T> or template <class T> before function or class declarations.",
            "Default arguments can be provided for template parameters (e.g. template <typename T = int>).",
            "Non-type template parameters must be compile-time constants.",
            "C++17 CTAD permits class instantiation without specifying explicit type arguments when deducible."
        ],
        "examples": [
            "template <typename T> T add(T a, T b) { return a + b; }",
            "template <typename T, int N> class Array { T data[N]; };"
        ]
    }
}

CPP_TOPICS[46] = {
    "id": 46,
    "title": "Standard Template Library (STL)",
    "category": "Templates & STL",
    "difficulty": "Advanced",
    "duration": "45 min",
    "concept": "The Standard Template Library (STL) is a foundation of modern C++ providing reusable, generic, type-safe data structures and algorithms. STL comprises three core pillars: Containers (data storage structures), Iterators (pointer-like abstractions for container traversal), and Algorithms (functions for searching, sorting, manipulating container data).",
    "syntax": "#include <vector>\n#include <algorithm>\n#include <numeric>\n\nvector<int> v = {3, 1, 4};\nsort(v.begin(), v.end());",
    "example": {
        "code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <numeric>\nusing namespace std;\n\nint main() {\n    vector<int> numbers = {5, 2, 8, 1, 9};\n    sort(numbers.begin(), numbers.end());\n    cout << \"Sorted numbers: \";\n    for (int x : numbers) cout << x << \" \";\n    cout << endl;\n\n    int sum = accumulate(numbers.begin(), numbers.end(), 0);\n    cout << \"Sum of numbers: \" << sum << endl;\n    return 0;\n}",
        "output": "Sorted numbers: 1 2 5 8 9 \nSum of numbers: 25",
        "explanation": "Demonstrates the STL triad: std::vector (Container), .begin()/.end() (Iterators), and sort()/accumulate() (Algorithms)."
    },
    "fill_blanks": {
        "question": "Fill in the missing components of the STL triad:",
        "answers": ["Containers", "Iterators", "Algorithms"],
        "options": ["Containers", "Iterators", "Algorithms", "Pointers", "Macros", "Threads"]
    },
    "compiler": {
        "title": "STL Triad Sandbox",
        "starter_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    vector<int> v = {40, 10, 30, 20};\n    sort(v.begin(), v.end());\n    for (int n : v) cout << n << \" \";\n    cout << endl;\n    return 0;\n}",
        "question": "Arrange lines to sort vector elements in ascending order using STL algorithm.",
        "options": [
            "#include <vector>",
            "#include <algorithm>",
            "vector<int> v = {40, 10, 30, 20};",
            "sort(v.begin(), v.end());",
            "return 0;"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What are the three main components of the C++ Standard Template Library (STL)?",
            "options": [
                "Containers, Iterators, and Algorithms",
                "Classes, Objects, and Functions",
                "Headers, Libraries, and Preprocessors",
                "Stack, Heap, and Registers"
            ],
            "answer": "Containers, Iterators, and Algorithms"
        },
        {
            "question": "Which category of STL containers includes vector, deque, and list?",
            "options": [
                "Sequence Containers",
                "Associative Containers",
                "Unordered Associative Containers",
                "Container Adaptors"
            ],
            "answer": "Sequence Containers"
        },
        {
            "question": "What role do Iterators play in the STL architecture?",
            "options": [
                "They act as pointer-like interfaces connecting containers to generic algorithms",
                "They allocate dynamic heap memory for vectors",
                "They compile template classes into assembly instructions",
                "They handle file I/O operations"
            ],
            "answer": "They act as pointer-like interfaces connecting containers to generic algorithms"
        },
        {
            "question": "Which STL container adaptor provides a LIFO (Last In First Out) interface?",
            "options": [
                "std::stack",
                "std::queue",
                "std::vector",
                "std::set"
            ],
            "answer": "std::stack"
        },
        {
            "question": "What major advantage does STL offer to C++ software developers?",
            "options": [
                "Provides well-tested, highly optimized, type-safe data structures with performance guarantees",
                "Eliminates the need for a C++ compiler",
                "Replaces the main() entry point",
                "Automatically manages network connections"
            ],
            "answer": "Provides well-tested, highly optimized, type-safe data structures with performance guarantees"
        }
    ],
    "theory": {
        "definition": "The C++ Standard Template Library (STL) is a rich software library of generic data structures, algorithms, and iterators built using C++ templates.",
        "why": "Increases developer productivity by providing reliable, high-performance, ready-to-use software components.",
        "rules": [
            "Containers manage object collections.",
            "Iterators allow traversal across container elements regardless of underlying structure.",
            "Algorithms manipulate data via iterator ranges.",
            "STL components are defined within the std namespace."
        ],
        "examples": [
            "vector<int> v = {1, 2, 3};",
            "sort(v.begin(), v.end());"
        ]
    }
}

CPP_TOPICS[47] = {
    "id": 47,
    "title": "Algorithms",
    "category": "Templates & STL",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "The C++ STL Algorithm Library (<algorithm> and <numeric>) provides predefined functions for searching, sorting, counting, modifying, comparing, and numeric operations on container ranges via iterators. Decouples algorithmic logic from container implementation details.",
    "syntax": "#include <algorithm>\n#include <numeric>\n\nsort(v.begin(), v.end());\nauto it = find(v.begin(), v.end(), val);\nint total = accumulate(v.begin(), v.end(), 0);",
    "example": {
        "code": "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <numeric>\nusing namespace std;\n\nint main() {\n    vector<int> v = {10, 20, 30, 20, 40, 20};\n    int cnt = count(v.begin(), v.end(), 20);\n    cout << \"Count of 20: \" << cnt << endl;\n\n    bool found = binary_search(v.begin(), v.end(), 30);\n    cout << \"Binary search 30: \" << (found ? \"Found\" : \"Not Found\") << endl;\n\n    vector<int> seq(5);\n    iota(seq.begin(), seq.end(), 1); // Fills 1, 2, 3, 4, 5\n    cout << \"Sum of iota seq: \" << accumulate(seq.begin(), seq.end(), 0) << endl;\n    return 0;\n}",
        "output": "Count of 20: 3\nBinary search 30: Found\nSum of iota seq: 15",
        "explanation": "count() finds occurrences of 20. binary_search() checks element presence in O(log n). iota() populates sequential values, and accumulate() sums elements."
    },
    "fill_blanks": {
        "question": "Fill in the correct STL algorithm functions:",
        "answers": ["find", "sort", "accumulate", "iota"],
        "options": ["find", "sort", "accumulate", "iota", "search", "sum"]
    },
    "compiler": {
        "title": "STL Algorithms Practice",
        "starter_code": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    vector<int> v = {5, 3, 1, 4, 2};\n    reverse(v.begin(), v.end());\n    for (int x : v) cout << x << \" \";\n    cout << endl;\n    return 0;\n}",
        "question": "Arrange lines to reverse elements of a vector using std::reverse.",
        "options": [
            "#include <algorithm>",
            "vector<int> v = {5, 3, 1, 4, 2};",
            "reverse(v.begin(), v.end());",
            "for (int x : v) cout << x << \" \";",
            "return 0;"
        ]
    },
    "skill_exa_test": [
        {
            "question": "Which condition must be met before calling std::binary_search() on a container range?",
            "options": [
                "The element range must be sorted in ascending order",
                "The container must be a vector or raw array only",
                "The size of the container must be an even integer",
                "All elements must be positive"
            ],
            "answer": "The element range must be sorted in ascending order"
        },
        {
            "question": "Which STL header file defines mathematical functions like std::accumulate() and std::iota()?",
            "options": [
                "<numeric>",
                "<algorithm>",
                "<cmath>",
                "<memory>"
            ],
            "answer": "<numeric>"
        },
        {
            "question": "What does the std::iota() function do when executed over an iterator range?",
            "options": [
                "Fills the range with sequentially increasing values starting from a specified initial value",
                "Calculates the dot product of two vectors",
                "Removes duplicate adjacent elements",
                "Sorts the range in reverse descending order"
            ],
            "answer": "Fills the range with sequentially increasing values starting from a specified initial value"
        },
        {
            "question": "How does std::remove() behave when eliminating unwanted elements from an STL vector?",
            "options": [
                "It shifts non-removed elements to the front and returns the logical new end iterator, requiring vector::erase() to alter physical size",
                "It immediately frees heap memory allocated to deleted elements",
                "It sets deleted element indices to nullptr",
                "It throws std::out_of_range exception"
            ],
            "answer": "It shifts non-removed elements to the front and returns the logical new end iterator, requiring vector::erase() to alter physical size"
        },
        {
            "question": "What is the time complexity of std::sort() in modern standard C++ implementations?",
            "options": [
                "O(n log n) average and worst-case time complexity (Introsort)",
                "O(n^2) worst-case time complexity",
                "O(n) linear time complexity",
                "O(1) constant time complexity"
            ],
            "answer": "O(n log n) average and worst-case time complexity (Introsort)"
        }
    ],
    "theory": {
        "definition": "STL Algorithms are container-independent generic functions that operate on iterator ranges to search, sort, manipulate, count, and aggregate data.",
        "why": "Provides highly efficient, battle-tested algorithmic implementations with guaranteed performance complexity.",
        "rules": [
            "Include <algorithm> for general sorting/searching and <numeric> for mathematical aggregations.",
            "Binary search functions (binary_search, lower_bound, upper_bound) require sorted inputs.",
            "Algorithms use iterators (begin()/end()) to define operational bounds."
        ],
        "examples": [
            "sort(vec.begin(), vec.end());",
            "int s = accumulate(vec.begin(), vec.end(), 0);"
        ]
    }
}

CPP_TOPICS[48] = {
    "id": 48,
    "title": "Containers",
    "category": "Templates & STL",
    "difficulty": "Advanced",
    "duration": "40 min",
    "concept": "STL Containers are template classes that store and organize collections of data. Divided into 4 primary types: Sequence Containers (vector, list, deque, array), Associative Containers (set, map, multiset, multimap based on Red-Black Trees), Unordered Associative Containers (unordered_set, unordered_map based on Hash Tables), and Container Adaptors (stack, queue, priority_queue).",
    "syntax": "std::vector<int> seq;       // Sequence\nstd::set<string> unique;    // Associative (Red-Black Tree)\nstd::unordered_map<int, int> hash; // Unordered Hash Table\nstd::stack<int> st;         // Container Adaptor",
    "example": {
        "code": "#include <iostream>\n#include <vector>\n#include <set>\n#include <unordered_map>\nusing namespace std;\n\nint main() {\n    vector<int> vec = {10, 20, 30};\n    set<int> unique_set = {30, 10, 20, 10}; // Filtered & sorted: 10, 20, 30\n    unordered_map<string, int> ages = {{\"Alice\", 25}, {\"Bob\", 30}};\n\n    cout << \"Vector size: \" << vec.size() << endl;\n    cout << \"Unique set elements: \";\n    for (int x : unique_set) cout << x << \" \";\n    cout << endl;\n    cout << \"Bob's age: \" << ages[\"Bob\"] << endl;\n    return 0;\n}",
        "output": "Vector size: 3\nUnique set elements: 10 20 30 \nBob's age: 30",
        "explanation": "Illustrates key container categories: dynamic array (vector), self-balancing binary search tree (set), and hash table (unordered_map)."
    },
    "fill_blanks": {
        "question": "Fill in the container category classification:",
        "answers": ["Sequence", "Associative", "Unordered", "Adaptors"],
        "options": ["Sequence", "Associative", "Unordered", "Adaptors", "Global", "Local"]
    },
    "compiler": {
        "title": "Containers Overview Practice",
        "starter_code": "#include <iostream>\n#include <vector>\n#include <set>\nusing namespace std;\n\nint main() {\n    set<int> s = {3, 1, 2, 1};\n    for (int x : s) cout << x << \" \";\n    cout << endl;\n    return 0;\n}",
        "question": "Arrange lines to create std::set and print unique sorted elements.",
        "options": [
            "#include <set>",
            "set<int> s = {3, 1, 2, 1};",
            "for (int x : s) cout << x << \" \";",
            "cout << endl;",
            "return 0;"
        ]
    },
    "skill_exa_test": [
        {
            "question": "Which underlying data structure is typically used to implement C++ STL Associative Containers like std::map and std::set?",
            "options": [
                "Self-balancing Red-Black Search Trees",
                "Hash Tables with open addressing",
                "Doubly Linked Lists",
                "Fixed Contiguous Arrays"
            ],
            "answer": "Self-balancing Red-Black Search Trees"
        },
        {
            "question": "What is the average time complexity for element lookup in an Unordered Associative Container (e.g. std::unordered_map)?",
            "options": [
                "O(1) constant amortized time complexity",
                "O(log n) logarithmic time complexity",
                "O(n) linear time complexity",
                "O(n log n) logarithmic linear time complexity"
            ],
            "answer": "O(1) constant amortized time complexity"
        },
        {
            "question": "What distinguishes Container Adaptors (stack, queue, priority_queue) from standard containers?",
            "options": [
                "They wrap existing sequence containers to restrict member interfaces to specific behavioral models (e.g. LIFO/FIFO)",
                "They do not use templates",
                "They only store raw character pointers",
                "They cannot be allocated on the heap"
            ],
            "answer": "They wrap existing sequence containers to restrict member interfaces to specific behavioral models (e.g. LIFO/FIFO)"
        },
        {
            "question": "Which member function is common to virtually all C++ STL container classes to clear all stored elements?",
            "options": [
                "clear()",
                "erase_all()",
                "empty()",
                "destroy()"
            ],
            "answer": "clear()"
        },
        {
            "question": "Which sequence container supports fast O(1) time complexity insertions and deletions at both its front and back ends?",
            "options": [
                "std::deque (Double-ended Queue)",
                "std::vector",
                "std::array",
                "std::stack"
            ],
            "answer": "std::deque (Double-ended Queue)"
        }
    ],
    "theory": {
        "definition": "STL Containers are template classes that implement dynamic data structures for storing, accessing, and managing collections of objects.",
        "why": "Allows selecting optimized storage representations tailored to specific time and space complexity requirements.",
        "rules": [
            "Sequence containers maintain physical/logical linear ordering.",
            "Associative containers maintain elements sorted by key in O(log n) trees.",
            "Unordered associative containers maintain elements in O(1) hash tables.",
            "Adaptors restrict container interfaces for LIFO/FIFO algorithms."
        ],
        "examples": [
            "vector<int> v;",
            "map<string, int> m;",
            "unordered_set<int> us;"
        ]
    }
}

CPP_TOPICS[49] = {
    "id": 49,
    "title": "Iterators",
    "category": "Templates & STL",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "Iterators are pointer-like objects used to access, dereference (*it), and traverse elements in STL containers. Categories include Input, Output, Forward, Bidirectional, and Random Access iterators. Functions begin(), end(), cbegin(), cend(), rbegin(), rend(), std::advance(), std::next(), std::prev(), and std::distance() enable container-agnostic operations.",
    "syntax": "vector<int>::iterator it = vec.begin();\nfor (auto it = vec.cbegin(); it != vec.cend(); ++it) {\n    cout << *it;\n}",
    "example": {
        "code": "#include <iostream>\n#include <vector>\n#include <iterator>\nusing namespace std;\n\nint main() {\n    vector<int> vec = {10, 20, 30, 40, 50};\n\n    cout << \"Forward: \";\n    for (auto it = vec.begin(); it != vec.end(); ++it) cout << *it << \" \";\n    cout << endl;\n\n    cout << \"Reverse: \";\n    for (auto rit = vec.rbegin(); rit != vec.rend(); ++rit) cout << *rit << \" \";\n    cout << endl;\n\n    auto it2 = vec.begin() + 3;\n    cout << \"Element at offset 3: \" << *it2 << endl;\n    cout << \"Distance from begin: \" << distance(vec.begin(), it2) << endl;\n    return 0;\n}",
        "output": "Forward: 10 20 30 40 50 \nReverse: 50 40 30 20 10 \nElement at offset 3: 40\nDistance from begin: 3",
        "explanation": "Demonstrates forward iteration, reverse iteration via rbegin()/rend(), random-access arithmetic (+ 3), and std::distance calculation."
    },
    "fill_blanks": {
        "question": "Fill in the missing iterator functions:",
        "answers": ["begin", "end", "cbegin", "rbegin"],
        "options": ["begin", "end", "cbegin", "rbegin", "start", "finish"]
    },
    "compiler": {
        "title": "Iterators Practice Sandbox",
        "starter_code": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nint main() {\n    vector<int> v = {100, 200, 300};\n    for (auto it = v.cbegin(); it != v.cend(); ++it) {\n        cout << *it << \" \";\n    }\n    cout << endl;\n    return 0;\n}",
        "question": "Arrange lines to traverse a vector using constant iterators cbegin() and cend().",
        "options": [
            "#include <vector>",
            "vector<int> v = {100, 200, 300};",
            "for (auto it = v.cbegin(); it != v.cend(); ++it) {",
            "    cout << *it << \" \";",
            "}",
            "return 0;"
        ]
    },
    "skill_exa_test": [
        {
            "question": "Which iterator category offers the highest capability, supporting direct pointer arithmetic (it + n) and random indexing (it[n]) in O(1)?",
            "options": [
                "Random Access Iterator",
                "Bidirectional Iterator",
                "Forward Iterator",
                "Input Iterator"
            ],
            "answer": "Random Access Iterator"
        },
        {
            "question": "What is the difference between begin() and cbegin() member functions in STL containers?",
            "options": [
                "begin() returns a mutable iterator allowing value modifications; cbegin() returns a constant read-only iterator",
                "begin() starts from index 1; cbegin() starts from index 0",
                "cbegin() allocates heap memory for the container",
                "begin() works only for arrays while cbegin() works for lists"
            ],
            "answer": "begin() returns a mutable iterator allowing value modifications; cbegin() returns a constant read-only iterator"
        },
        {
            "question": "What does std::distance(it1, it2) compute?",
            "options": [
                "The number of elements between two iterators in a container",
                "The byte memory difference between two heap pointers",
                "The execution time taken to traverse between two elements",
                "The hash key difference in std::unordered_map"
            ],
            "answer": "The number of elements between two iterators in a container"
        },
        {
            "question": "Which iterator category is supported by std::list and std::set, allowing ++ and -- operations but NOT offset arithmetic (it + n)?",
            "options": [
                "Bidirectional Iterator",
                "Random Access Iterator",
                "Output Iterator",
                "Single-Pass Iterator"
            ],
            "answer": "Bidirectional Iterator"
        },
        {
            "question": "What is the purpose of std::back_inserter(container)?",
            "options": [
                "Creates an output iterator adaptor that appends assigned elements to the container by calling push_back()",
                "Reverses the array order in place",
                "Deletes elements from the back of the vector",
                "Returns a reference to the last element"
            ],
            "answer": "Creates an output iterator adaptor that appends assigned elements to the container by calling push_back()"
        }
    ],
    "theory": {
        "definition": "Iterators are generalized pointer abstractions used to navigate, access, and manipulate elements within standard containers.",
        "why": "Decouples container data storage models from generic algorithms, enabling unified algorithms across diverse data structures.",
        "rules": [
            "Use *it to access or modify referenced element values.",
            "Use cbegin()/cend() for read-only traversal.",
            "Random access iterators (vector, deque, array) support arithmetic offsets.",
            "Bidirectional iterators (list, set, map) support increment/decrement only."
        ],
        "examples": [
            "auto it = vec.begin();",
            "advance(it, 3);",
            "int len = distance(v.begin(), v.end());"
        ]
    }
}

CPP_TOPICS[50] = {
    "id": 50,
    "title": "Vector",
    "category": "Templates & STL",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "std::vector (<vector>) is a dynamic sequence container storing elements in contiguous memory. Provides constant O(1) random access via operator[] or at(), O(1) amortized push_back() and pop_back(), and O(n) insert()/erase() in middle positions. Automatically handles capacity expansion upon exceeding storage capacity.",
    "syntax": "#include <vector>\n\nstd::vector<int> v = {10, 20};\nv.push_back(30);\nv.at(1) = 50;\nv.pop_back();\nv.erase(v.begin() + 1);",
    "example": {
        "code": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    vector<int> v = {10, 20, 30};\n    v.push_back(40);\n    v.insert(v.begin() + 1, 15); // Insert 15 at index 1\n\n    cout << \"Elements: \";\n    for (int x : v) cout << x << \" \";\n    cout << endl;\n\n    cout << \"Size: \" << v.size() << \", Capacity: \" << v.capacity() << endl;\n    v.erase(v.begin() + 2); // Remove element at index 2 (20)\n\n    cout << \"After erase: \";\n    for (int i = 0; i < v.size(); i++) cout << v[i] << \" \";\n    cout << endl;\n    return 0;\n}",
        "output": "Elements: 10 15 20 30 40 \nSize: 5, Capacity: 6\nAfter erase: 10 15 30 40 ",
        "explanation": "Illustrates vector initialization, push_back(), insert(), capacity growth, erase(), and indexing using subscript operator[]."
    },
    "fill_blanks": {
        "question": "Fill in the missing std::vector member functions:",
        "answers": ["push_back", "pop_back", "insert", "erase"],
        "options": ["push_back", "pop_back", "insert", "erase", "append", "delete"]
    },
    "compiler": {
        "title": "Vector Operations Practice",
        "starter_code": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nint main() {\n    vector<string> fruits = {\"Apple\", \"Banana\"};\n    fruits.push_back(\"Cherry\");\n    cout << \"Front: \" << fruits.front() << \", Back: \" << fruits.back() << endl;\n    return 0;\n}",
        "question": "Arrange lines to create a string vector, push an element, and display front and back items.",
        "options": [
            "#include <vector>",
            "vector<string> fruits = {\"Apple\", \"Banana\"};",
            "fruits.push_back(\"Cherry\");",
            "cout << \"Front: \" << fruits.front() << \", Back: \" << fruits.back() << endl;",
            "return 0;"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What is the difference between vector element access using v[i] versus v.at(i)?",
            "options": [
                "v[i] performs direct fast access without bounds checking; v.at(i) performs bounds checking and throws std::out_of_range if index is invalid",
                "v[i] returns a pointer; v.at(i) returns a copy",
                "v.at(i) executes in O(n) time whereas v[i] is O(1)",
                "v[i] works only for integer vectors"
            ],
            "answer": "v[i] performs direct fast access without bounds checking; v.at(i) performs bounds checking and throws std::out_of_range if index is invalid"
        },
        {
            "question": "What is the time complexity of vector::push_back() under normal growth conditions?",
            "options": [
                "O(1) amortized constant time complexity",
                "O(n) linear time complexity always",
                "O(log n) logarithmic time complexity",
                "O(n^2) quadratic time complexity"
            ],
            "answer": "O(1) amortized constant time complexity"
        },
        {
            "question": "Why does calling vector::erase() or vector::insert() in the middle of a vector take O(n) time?",
            "options": [
                "Because subsequent elements must be shifted in contiguous memory to fill or make space",
                "Because the vector must be re-sorted",
                "Because it allocates a new heap matrix",
                "Because iterators become invalid permanently"
            ],
            "answer": "Because subsequent elements must be shifted in contiguous memory to fill or make space"
        },
        {
            "question": "What does vector::capacity() measure?",
            "options": [
                "The total number of elements the vector can store before needing memory re-allocation",
                "The current count of elements stored in the vector",
                "The max potential size limited by system RAM",
                "The byte size of a single element"
            ],
            "answer": "The total number of elements the vector can store before needing memory re-allocation"
        },
        {
            "question": "How is a 2D matrix represented using C++ STL vectors?",
            "options": [
                "vector<vector<T>> matrix;",
                "vector<matrix<T>> v;",
                "matrix<vector<T>> m;",
                "2D_vector<T> v;"
            ],
            "answer": "vector<vector<T>> matrix;"
        }
    ],
    "theory": {
        "definition": "std::vector is a standard sequence container representing a dynamic array with contiguous memory layout.",
        "why": "Optimal choice when fast random access is needed and insertions/deletions occur primarily at the end.",
        "rules": [
            "Use push_back() / pop_back() for O(1) trailing element operations.",
            "Use v.at(i) for safe, bounds-checked element retrieval.",
            "Capacity automatically expands (typically doubling) when size exceeds capacity.",
            "Contiguous memory guarantees compatibility with raw C-style array pointers (&v[0])."
        ],
        "examples": [
            "vector<int> v = {1, 2, 3};",
            "v.push_back(4);",
            "v.erase(v.begin());"
        ]
    }
}

CPP_TOPICS[51] = {
    "id": 51,
    "title": "Stack",
    "category": "Templates & STL",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "std::stack (<stack>) is a container adaptor implementing Last-In-First-Out (LIFO) context. Restricts access to the top element only. Provides O(1) push(), pop(), top(), empty(), and size() operations. Uses std::deque as default underlying container.",
    "syntax": "#include <stack>\n\nstd::stack<int> st;\nst.push(10);\nst.push(20);\nint topVal = st.top(); // 20\nst.pop();              // Removes 20",
    "example": {
        "code": "#include <iostream>\n#include <stack>\nusing namespace std;\n\nint main() {\n    stack<int> st;\n    st.push(10);\n    st.push(20);\n    st.push(30);\n\n    cout << \"Top element: \" << st.top() << endl;\n    cout << \"Stack size: \" << st.size() << endl;\n\n    cout << \"Popping elements: \";\n    while (!st.empty()) {\n        cout << st.top() << \" \";\n        st.pop();\n    }\n    cout << endl;\n    return 0;\n}",
        "output": "Top element: 30\nStack size: 3\nPopping elements: 30 20 10 ",
        "explanation": "Elements are pushed onto the stack in order 10, 20, 30. top() accesses 30. Popping elements prints them in reverse LIFO order: 30 20 10."
    },
    "fill_blanks": {
        "question": "Fill in the missing std::stack functions:",
        "answers": ["push", "top", "pop", "empty"],
        "options": ["push", "top", "pop", "empty", "insert", "remove"]
    },
    "compiler": {
        "title": "Stack Practice Sandbox",
        "starter_code": "#include <iostream>\n#include <stack>\nusing namespace std;\n\nint main() {\n    stack<string> st;\n    st.push(\"First\");\n    st.push(\"Second\");\n    cout << st.top() << endl;\n    st.pop();\n    cout << st.top() << endl;\n    return 0;\n}",
        "question": "Arrange lines to create a stack, push strings, display top, and pop.",
        "options": [
            "#include <stack>",
            "stack<string> st;",
            "st.push(\"First\");",
            "st.push(\"Second\");",
            "st.pop();",
            "return 0;"
        ]
    },
    "skill_exa_test": [
        {
            "question": "Which principle governs element ordering in std::stack?",
            "options": [
                "LIFO (Last In, First Out)",
                "FIFO (First In, First Out)",
                "Priority Order",
                "Random Access Order"
            ],
            "answer": "LIFO (Last In, First Out)"
        },
        {
            "question": "What happens if stack::top() or stack::pop() is called on an empty std::stack?",
            "options": [
                "Undefined Behavior (segmentation fault or memory crash)",
                "Returns 0 automatically",
                "Returns nullptr",
                "Throws std::stack_empty exception"
            ],
            "answer": "Undefined Behavior (segmentation fault or memory crash)"
        },
        {
            "question": "What is the return type of stack::pop() in C++ STL?",
            "options": [
                "void (it removes the top element without returning its value)",
                "The element type T",
                "bool (true if successful)",
                "An iterator to top"
            ],
            "answer": "void (it removes the top element without returning its value)"
        },
        {
            "question": "How can you safely traverse and print all elements of std::stack without modifying the original stack?",
            "options": [
                "By creating a copy of the stack (stack<T> temp = st;) and popping elements from the copy in a while loop",
                "By using for (auto it = st.begin(); it != st.end(); ++it)",
                "By calling st.display()",
                "By using operator[] indexing"
            ],
            "answer": "By creating a copy of the stack (stack<T> temp = st;) and popping elements from the copy in a while loop"
        },
        {
            "question": "What is the default underlying sequence container used by std::stack?",
            "options": [
                "std::deque",
                "std::vector",
                "std::list",
                "std::array"
            ],
            "answer": "std::deque"
        }
    ],
    "theory": {
        "definition": "std::stack is a LIFO container adaptor that restricts element access, insertion, and deletion strictly to the top element.",
        "why": "Provides clean, enforced LIFO data management for function call stacks, expression evaluation, matching parentheses, and backtracking algorithms.",
        "rules": [
            "push(val) adds element to top of stack in O(1).",
            "top() returns reference to top element in O(1).",
            "pop() removes top element in O(1) without returning it.",
            "Always check !st.empty() before calling top() or pop()."
        ],
        "examples": [
            "stack<int> st;",
            "st.push(5);",
            "int x = st.top(); st.pop();"
        ]
    }
}

CPP_TOPICS[52] = {
    "id": 52,
    "title": "Queue",
    "category": "Templates & STL",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "std::queue (<queue>) is a container adaptor implementing First-In-First-Out (FIFO) ordering. Insertions (enqueue) occur at the back via push(), and deletions (dequeue) occur at the front via pop(). Front and back elements are accessed using front() and back() in O(1) time.",
    "syntax": "#include <queue>\n\nstd::queue<int> q;\nq.push(10);  // Enqueue at back\nq.push(20);\nint f = q.front(); // 10\nint b = q.back();  // 20\nq.pop();     // Dequeue 10 from front",
    "example": {
        "code": "#include <iostream>\n#include <queue>\nusing namespace std;\n\nint main() {\n    queue<int> q;\n    q.push(100);\n    q.push(200);\n    q.push(300);\n\n    cout << \"Front: \" << q.front() << \", Back: \" << q.back() << endl;\n    cout << \"Queue size: \" << q.size() << endl;\n\n    q.pop(); // Removes front (100)\n    cout << \"New Front after pop: \" << q.front() << endl;\n\n    cout << \"Traversing remaining: \";\n    queue<int> temp(q);\n    while (!temp.empty()) {\n        cout << temp.front() << \" \";\n        temp.pop();\n    }\n    cout << endl;\n    return 0;\n}",
        "output": "Front: 100, Back: 300\nQueue size: 3\nNew Front after pop: 200\nTraversing remaining: 200 300 ",
        "explanation": "pushed 100, 200, 300. front() is 100, back() is 300. pop() removes 100 in FIFO order, leaving 200 as new front."
    },
    "fill_blanks": {
        "question": "Fill in the missing std::queue functions:",
        "answers": ["push", "pop", "front", "back"],
        "options": ["push", "pop", "front", "back", "top", "insert"]
    },
    "compiler": {
        "title": "Queue Practice Sandbox",
        "starter_code": "#include <iostream>\n#include <queue>\nusing namespace std;\n\nint main() {\n    queue<string> q;\n    q.push(\"Task1\");\n    q.push(\"Task2\");\n    cout << \"Processing: \" << q.front() << endl;\n    q.pop();\n    cout << \"Next task: \" << q.front() << endl;\n    return 0;\n}",
        "question": "Arrange lines to create a queue, push tasks, and process in FIFO order.",
        "options": [
            "#include <queue>",
            "queue<string> q;",
            "q.push(\"Task1\");",
            "q.push(\"Task2\");",
            "q.pop();",
            "return 0;"
        ]
    },
    "skill_exa_test": [
        {
            "question": "Which principle governs element processing in std::queue?",
            "options": [
                "FIFO (First In, First Out)",
                "LIFO (Last In, First Out)",
                "Sorted Order",
                "Random Access"
            ],
            "answer": "FIFO (First In, First Out)"
        },
        {
            "question": "Which member function accesses the oldest inserted element in a std::queue?",
            "options": [
                "front()",
                "back()",
                "top()",
                "begin()"
            ],
            "answer": "front()"
        },
        {
            "question": "What is the operation of queue::pop()?",
            "options": [
                "Removes the element from the front of the queue",
                "Removes the element from the back of the queue",
                "Returns the front element without deleting it",
                "Clears all elements in the queue"
            ],
            "answer": "Removes the element from the front of the queue"
        },
        {
            "question": "What common computer science applications utilize queue structures?",
            "options": [
                "Process scheduling, task buffering, and Breadth-First Search (BFS)",
                "Depth-First Search (DFS) graph traversal",
                "Compulsory memory garbage collection",
                "Binary search tree balancing"
            ],
            "answer": "Process scheduling, task buffering, and Breadth-First Search (BFS)"
        },
        {
            "question": "What is the time complexity of queue::push(), queue::pop(), and queue::front() operations?",
            "options": [
                "O(1) constant time complexity for all three operations",
                "O(n) linear time complexity",
                "O(log n) logarithmic time complexity",
                "O(n log n) time complexity"
            ],
            "answer": "O(1) constant time complexity for all three operations"
        }
    ],
    "theory": {
        "definition": "std::queue is a FIFO container adaptor restricting element addition to the back and element removal to the front.",
        "why": "Essential for managing ordered work queues, message buffers, and level-order tree/graph traversals.",
        "rules": [
            "push(val) appends element to the back.",
            "pop() removes element from the front.",
            "front() accesses the next element to be dequeued.",
            "back() accesses the most recently enqueued element."
        ],
        "examples": [
            "queue<int> q;",
            "q.push(1); q.push(2);",
            "q.pop();"
        ]
    }
}

CPP_TOPICS[53] = {
    "id": 53,
    "title": "Map",
    "category": "Templates & STL",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "std::map (<map>) is an associative container that stores key-value pairs sorted by unique keys using a self-balancing Red-Black Tree. Searching, insertion, value update, and deletion operate in logarithmic O(log n) time. Accessing keys via operator[] automatically inserts non-existent keys with default values.",
    "syntax": "#include <map>\n\nstd::map<int, string> m;\nm[1] = \"Geeks\";\nm.insert({2, \"SkillExa\"});\nauto it = m.find(1);\nm.erase(2);",
    "example": {
        "code": "#include <iostream>\n#include <map>\nusing namespace std;\n\nint main() {\n    map<int, string> m = {{1, \"Geeks\"}, {2, \"For\"}, {3, \"Geeks\"}};\n    m.insert({4, \"SkillExa\"});\n    m[1] = \"UpdatedGeek\";\n\n    cout << \"Map key-value pairs:\" << endl;\n    for (const auto& pair : m) {\n        cout << pair.first << \" -> \" << pair.second << endl;\n    }\n\n    auto it = m.find(3);\n    if (it != m.end()) {\n        cout << \"Found key 3: \" << it->second << endl;\n    }\n    return 0;\n}",
        "output": "Map key-value pairs:\n1 -> UpdatedGeek\n2 -> For\n3 -> Geeks\n4 -> SkillExa\nFound key 3: Geeks",
        "explanation": "Illustrates std::map creation, insert(), subscript operator updates, range-based traversal in key-sorted order, and find() key search."
    },
    "fill_blanks": {
        "question": "Fill in the missing std::map member functions:",
        "answers": ["insert", "erase", "find", "at"],
        "options": ["insert", "erase", "find", "at", "append", "push"]
    },
    "compiler": {
        "title": "Map Operations Practice",
        "starter_code": "#include <iostream>\n#include <map>\nusing namespace std;\n\nint main() {\n    map<string, int> scores;\n    scores[\"Alice\"] = 95;\n    scores[\"Bob\"] = 88;\n    cout << \"Alice score: \" << scores[\"Alice\"] << endl;\n    return 0;\n}",
        "question": "Arrange lines to create map<string, int>, assign key-value pairs, and access score.",
        "options": [
            "#include <map>",
            "map<string, int> scores;",
            "scores[\"Alice\"] = 95;",
            "cout << \"Alice score: \" << scores[\"Alice\"] << endl;",
            "return 0;"
        ]
    },
    "skill_exa_test": [
        {
            "question": "Which underlying data structure is utilized by std::map in standard C++ implementations?",
            "options": [
                "Self-balancing Red-Black Search Tree",
                "Dynamic array with linear probing",
                "Unordered Hash Table",
                "Singly Linked List"
            ],
            "answer": "Self-balancing Red-Black Search Tree"
        },
        {
            "question": "What side effect occurs when accessing a non-existent key using the map subscript operator m[key]?",
            "options": [
                "It automatically inserts the key into the map with a default-constructed value and returns reference to it",
                "It throws std::out_of_range exception",
                "It returns nullptr without modifying the map",
                "It triggers compile-time syntax error"
            ],
            "answer": "It automatically inserts the key into the map with a default-constructed value and returns reference to it"
        },
        {
            "question": "What is the time complexity of map::find(key) and map::erase(key)?",
            "options": [
                "O(log n) logarithmic time complexity",
                "O(1) constant time complexity",
                "O(n) linear time complexity",
                "O(n log n) time complexity"
            ],
            "answer": "O(log n) logarithmic time complexity"
        },
        {
            "question": "How does map::insert({key, val}) handle attempts to insert a duplicate key that already exists in the map?",
            "options": [
                "It ignores the insertion and leaves the existing key-value pair unchanged",
                "It overwrites the existing value with the new value",
                "It throws std::invalid_argument exception",
                "It appends a duplicate entry to the end"
            ],
            "answer": "It ignores the insertion and leaves the existing key-value pair unchanged"
        },
        {
            "question": "In what order are key-value pairs visited during iterator traversal of std::map?",
            "options": [
                "Strict ascending order of their keys",
                "The exact insertion sequence order",
                "Random hash bucket order",
                "Strict descending order of their values"
            ],
            "answer": "Strict ascending order of their keys"
        }
    ],
    "theory": {
        "definition": "std::map is an associative container storing unique key-value pairs sorted in ascending key order using a Red-Black Tree.",
        "why": "Ideal for dictionary lookups, associative counting, symbol tables, and range queries requiring ordered keys.",
        "rules": [
            "Keys must be unique and support operator< comparison.",
            "m[key] inserts key with default value if missing; m.at(key) throws out_of_range if missing.",
            "m.insert() does not overwrite existing key values.",
            "Search, insertion, and erasure operate in guaranteed O(log n) time."
        ],
        "examples": [
            "map<int, string> m;",
            "m[10] = \"Ten\";",
            "if (m.find(10) != m.end()) { ... }"
        ]
    }
}

CPP_TOPICS[54] = {
    "id": 54,
    "title": "Set",
    "category": "Templates & STL",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "std::set (<set>) is an associative container storing unique elements in sorted order using a self-balancing Red-Black Tree. Duplicate insertions are automatically ignored. Insertion, search (find, count), and erasure operate in O(log n) logarithmic time. Supports upper_bound() and lower_bound() range queries.",
    "syntax": "#include <set>\n\nstd::set<int> s = {3, 1, 2, 1}; // Sorted unique: 1, 2, 3\ns.insert(4);\nbool exists = s.count(2); // returns 1\ns.erase(3);",
    "example": {
        "code": "#include <iostream>\n#include <set>\nusing namespace std;\n\nint main() {\n    set<int> s = {5, 2, 8, 2, 1}; // Duplicates auto-filtered: {1, 2, 5, 8}\n    s.insert(3);\n\n    cout << \"Sorted unique elements: \";\n    for (int x : s) cout << x << \" \";\n    cout << endl;\n\n    auto it = s.find(5);\n    if (it != s.end()) cout << \"Found 5 in set!\" << endl;\n\n    s.erase(2);\n    cout << \"After erasing 2: \";\n    for (int x : s) cout << x << \" \";\n    cout << endl;\n    return 0;\n}",
        "output": "Sorted unique elements: 1 2 3 5 8 \nFound 5 in set!\nAfter erasing 2: 1 3 5 8 ",
        "explanation": "Demonstrates automatic duplicate filtering, sorted element traversal, logarithmic search via find(), and element removal via erase()."
    },
    "fill_blanks": {
        "question": "Fill in the missing std::set member functions:",
        "answers": ["insert", "erase", "find", "count"],
        "options": ["insert", "erase", "find", "count", "push", "remove"]
    },
    "compiler": {
        "title": "Set Operations Practice",
        "starter_code": "#include <iostream>\n#include <set>\nusing namespace std;\n\nint main() {\n    set<int> numbers = {40, 10, 20, 10, 30};\n    for (int num : numbers) cout << num << \" \";\n    cout << endl;\n    return 0;\n}",
        "question": "Arrange lines to create a set, initialize with duplicates, and display sorted unique elements.",
        "options": [
            "#include <set>",
            "set<int> numbers = {40, 10, 20, 10, 30};",
            "for (int num : numbers) cout << num << \" \";",
            "cout << endl;",
            "return 0;"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What happens when a duplicate value is inserted into a std::set?",
            "options": [
                "The duplicate value is automatically ignored and the set remains unchanged",
                "It overwrites the existing value and moves it to the back",
                "It throws std::duplicate_error exception",
                "It creates a secondary bucket for duplicates"
            ],
            "answer": "The duplicate value is automatically ignored and the set remains unchanged"
        },
        {
            "question": "What key difference distinguishes std::set from std::unordered_set in C++ STL?",
            "options": [
                "std::set maintains elements in sorted order via Red-Black Tree (O(log n)); std::unordered_set uses Hash Table (O(1) avg) without sorting guarantees",
                "std::set allows duplicate elements whereas std::unordered_set does not",
                "std::set requires C++20 standard compiler flags",
                "std::unordered_set can only store integers"
            ],
            "answer": "std::set maintains elements in sorted order via Red-Black Tree (O(log n)); std::unordered_set uses Hash Table (O(1) avg) without sorting guarantees"
        },
        {
            "question": "What is the return value of set::count(val) in std::set?",
            "options": [
                "1 if the element exists in the set, or 0 if it does not",
                "The total count of all elements in the set",
                "The iterator index of val",
                "The memory address of val"
            ],
            "answer": "1 if the element exists in the set, or 0 if it does not"
        },
        {
            "question": "Why are elements stored in a std::set immutable (read-only) via iterators?",
            "options": [
                "Directly modifying an element value in-place would violate the binary search tree ordering invariant",
                "Because sets are allocated in read-only memory segments",
                "Because set iterators are pointers to const static variables",
                "To optimize thread synchronization locks"
            ],
            "answer": "Directly modifying an element value in-place would violate the binary search tree ordering invariant"
        },
        {
            "question": "Which member function returns an iterator to the first element in std::set that is NOT LESS than a specified value?",
            "options": [
                "lower_bound()",
                "upper_bound()",
                "find()",
                "binary_search()"
            ],
            "answer": "lower_bound()"
        }
    ],
    "theory": {
        "definition": "std::set is an associative container containing a sorted set of unique objects of type Key.",
        "why": "Guarantees uniqueness of stored data and maintains sorted order with O(log n) search and range query capabilities.",
        "rules": [
            "All elements must be unique.",
            "Elements are stored in sorted order according to strict weak ordering (operator<).",
            "Set elements cannot be modified in-place (must erase and re-insert).",
            "Insertion, deletion, and lookup execute in O(log n) time."
        ],
        "examples": [
            "set<int> s = {3, 1, 2};",
            "s.insert(4);",
            "if (s.count(2)) { ... }"
        ]
    }
}


CPP_TOPICS[55] = {
    "id": 55,
    "title": "Exception Handling",
    "category": "Exception Handling",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "Exception handling in C++ provides a structured mechanism to manage runtime errors using try, throw, and catch keywords. Code that may throw errors is enclosed in a try block; exceptions are signaled via throw; and catch blocks process matching exception types. Supports nested try-catch blocks and catch-all handlers catch(...). Prevents unexpected program termination.",
    "syntax": "try {\n    if (denom == 0) throw \"Division by zero!\";\n    int res = num / denom;\n} catch (const char* msg) {\n    cout << \"Error: \" << msg;\n} catch (...) {\n    cout << \"Unknown exception occurred!\";\n}",
    "example": {
        "code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nvoid checkAge(int age) {\n    if (age < 18)\n        throw \"Age must be 18 or above!\";\n}\n\nint main() {\n    int n = 10, m = 0;\n    try {\n        if (m == 0)\n            throw \"Division by zero error!\";\n        cout << n / m << endl;\n    } catch (const char* msg) {\n        cout << \"Caught: \" << msg << endl;\n    }\n\n    try {\n        checkAge(15);\n    } catch (const char* msg) {\n        cout << \"Age Check Exception: \" << msg << endl;\n    }\n\n    try {\n        try {\n            throw 10;\n        } catch (int e) {\n            cout << \"Nested inner catch: \" << e << endl;\n            throw \"Outer rethrow error\";\n        }\n    } catch (const char* msg) {\n        cout << \"Outer catch: \" << msg << endl;\n    }\n    return 0;\n}",
        "output": "Caught: Division by zero error!\nAge Check Exception: Age must be 18 or above!\nNested inner catch: 10\nOuter catch: Outer rethrow error",
        "explanation": "Demonstrates basic try-catch for division by zero, throw keyword in checkAge(), and nested try-catch with inner exception handling and rethrowing."
    },
    "fill_blanks": {
        "question": "Fill in the missing C++ exception keywords:",
        "answers": ["try", "throw", "catch", "..."],
        "options": ["try", "throw", "catch", "...", "finally", "except"]
    },
    "compiler": {
        "title": "Exception Handling Practice",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    try {\n        int val = -1;\n        if (val < 0) throw \"Negative value not allowed!\";\n    } catch (const char* msg) {\n        cout << \"Error: \" << msg << endl;\n    }\n    return 0;\n}",
        "question": "Arrange lines to create a try-catch block throwing a const char* exception string.",
        "options": [
            "try {",
            "    if (val < 0) throw \"Negative value not allowed!\";",
            "} catch (const char* msg) {",
            "    cout << \"Error: \" << msg << endl;",
            "}"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What happens when an exception is thrown in a try block and no matching catch handler is found in the call stack?",
            "options": [
                "std::terminate() is called, abruptly ending program execution",
                "The exception is ignored and execution resumes on the next line",
                "The compiler re-runs the try block automatically",
                "The operating system prints a stack dump and continues"
            ],
            "answer": "std::terminate() is called, abruptly ending program execution"
        },
        {
            "question": "What is the purpose of the catch(...) handler syntax in C++?",
            "options": [
                "It acts as a catch-all handler that catches any unhandled exception of any data type",
                "It catches only floating point exceptions",
                "It converts standard exceptions into string messages",
                "It disables stack unwinding"
            ],
            "answer": "It acts as a catch-all handler that catches any unhandled exception of any data type"
        },
        {
            "question": "What role does the throw keyword perform in C++ exception handling?",
            "options": [
                "Explicitly triggers an exception and transfers control to a matching catch block",
                "Declares dynamic stack memory allocations",
                "Frees memory allocated by new",
                "Defines function prototypes"
            ],
            "answer": "Explicitly triggers an exception and transfers control to a matching catch block"
        },
        {
            "question": "What occurs to lines of code remaining inside a try block after a throw statement executes?",
            "options": [
                "They are skipped and control immediately jumps to the matching catch block",
                "They are executed after the catch block completes",
                "They are compiled into inline instructions",
                "They cause a syntax error"
            ],
            "answer": "They are skipped and control immediately jumps to the matching catch block"
        },
        {
            "question": "Which primitive data types can be thrown as built-in exceptions in C++?",
            "options": [
                "Any valid C++ type, including int, char, float, and string literals",
                "Only std::exception objects",
                "Only positive integers",
                "Only void pointers"
            ],
            "answer": "Any valid C++ type, including int, char, float, and string literals"
        }
    ],
    "theory": {
        "definition": "Exception Handling is a language mechanism using try, throw, and catch to handle runtime errors without corrupting execution flow.",
        "why": "Separates error detection from error resolution logic, improving code maintainability and program stability.",
        "rules": [
            "Enclose error-prone code inside a try block.",
            "Use throw to signal error states.",
            "Match thrown types with specific catch parameter types.",
            "Use catch(...) as a fallback handler at the end of handler lists."
        ],
        "examples": [
            "try { if (x == 0) throw -1; } catch (int e) { ... }",
            "catch (...) { cout << \"Unknown error\"; }"
        ]
    }
}

CPP_TOPICS[56] = {
    "id": 56,
    "title": "Exception Handling Using Classes",
    "category": "Exception Handling",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "Class-based exception handling utilizes standard exception classes (<exception>, <stdexcept>) derived from std::exception. Provides the virtual const char* what() const noexcept member function for retrieving descriptive error messages. Common built-in exceptions include std::out_of_range, std::bad_alloc, std::invalid_argument, and std::runtime_error. Custom exception classes inherit from std::exception or std::runtime_error.",
    "syntax": "#include <exception>\n#include <stdexcept>\n\nclass CustomExcept : public std::exception {\npublic:\n    const char* what() const noexcept override {\n        return \"Custom class error message!\";\n    }\n};",
    "example": {
        "code": "#include <iostream>\n#include <exception>\n#include <stdexcept>\n#include <vector>\nusing namespace std;\n\nclass NegativeValueException : public exception {\nprivate:\n    int value;\npublic:\n    NegativeValueException(int val) : value(val) {}\n    const char* what() const noexcept override {\n        return \"Negative value error occurred!\";\n    }\n    int getValue() const { return value; }\n};\n\nint main() {\n    try {\n        vector<int> v = {10, 20};\n        v.at(5); // Throws std::out_of_range\n    } catch (const out_of_range& e) {\n        cout << \"Standard Exception Caught: \" << e.what() << endl;\n    }\n\n    try {\n        throw NegativeValueException(-5);\n    } catch (const NegativeValueException& e) {\n        cout << \"Custom Exception: \" << e.what() << \" Value: \" << e.getValue() << endl;\n    }\n\n    try {\n        throw runtime_error(\"Custom runtime message\");\n    } catch (const runtime_error& e) {\n        cout << \"Runtime Error Caught: \" << e.what() << endl;\n    }\n    return 0;\n}",
        "output": "Standard Exception Caught: vector::_M_range_check: __n (which is 5) >= this->size() (which is 2)\nCustom Exception: Negative value error occurred! Value: -5\nRuntime Error Caught: Custom runtime message",
        "explanation": "Illustrates handling std::out_of_range, creating custom exception classes inheriting from std::exception, and overriding what() const noexcept."
    },
    "fill_blanks": {
        "question": "Fill in the missing standard exception keywords:",
        "answers": ["exception", "what", "override", "noexcept"],
        "options": ["exception", "what", "override", "noexcept", "virtual", "delete"]
    },
    "compiler": {
        "title": "Exception Classes Practice",
        "starter_code": "#include <iostream>\n#include <stdexcept>\nusing namespace std;\n\nint main() {\n    try {\n        throw runtime_error(\"Invalid configuration file!\");\n    } catch (const runtime_error& e) {\n        cout << \"Caught: \" << e.what() << endl;\n    }\n    return 0;\n}",
        "question": "Arrange lines to throw and catch a std::runtime_error standard exception object.",
        "options": [
            "#include <stdexcept>",
            "try {",
            "    throw runtime_error(\"Invalid configuration file!\");",
            "} catch (const runtime_error& e) {",
            "    cout << \"Caught: \" << e.what() << endl;",
            "}"
        ]
    },
    "skill_exa_test": [
        {
            "question": "Which virtual member function declared in std::exception returns an explanatory string describing the exception?",
            "options": [
                "const char* what() const noexcept",
                "string getMessage()",
                "void printError()",
                "char* details()"
            ],
            "answer": "const char* what() const noexcept"
        },
        {
            "question": "Which standard C++ exception is thrown when dynamic memory allocation via operator new fails?",
            "options": [
                "std::bad_alloc",
                "std::out_of_range",
                "std::bad_cast",
                "std::overflow_error"
            ],
            "answer": "std::bad_alloc"
        },
        {
            "question": "Why is it best practice to catch exception objects by const reference (catch (const exception& e))?",
            "options": [
                "Prevents object slicing, avoids unnecessary object copying, and preserves polymorphic behavior",
                "Increases stack memory size",
                "Allows modifying the thrown exception object",
                "Enables inline assembly compilation"
            ],
            "answer": "Prevents object slicing, avoids unnecessary object copying, and preserves polymorphic behavior"
        },
        {
            "question": "Which standard exception class is derived from std::exception to represent index out of bounds errors?",
            "options": [
                "std::out_of_range",
                "std::domain_error",
                "std::bad_typeid",
                "std::invalid_argument"
            ],
            "answer": "std::out_of_range"
        },
        {
            "question": "What is the benefit of inheriting custom exception classes from std::runtime_error instead of raw std::exception?",
            "options": [
                "std::runtime_error includes a constructor accepting custom std::string error messages, reducing boilerplate",
                "std::runtime_error runs faster at compile time",
                "std::runtime_error prevents stack unwinding",
                "std::runtime_error does not require virtual destructors"
            ],
            "answer": "std::runtime_error includes a constructor accepting custom std::string error messages, reducing boilerplate"
        }
    ],
    "theory": {
        "definition": "Exception Handling Using Classes uses object-oriented exception hierarchies derived from std::exception for error encapsulation.",
        "why": "Provides structured, polymorphic error data and standardized error messages via the what() interface.",
        "rules": [
            "Derive custom exception classes from std::exception or std::runtime_error.",
            "Override virtual const char* what() const noexcept.",
            "Catch exception objects by const reference.",
            "Standard exceptions are defined in <exception> and <stdexcept>."
        ],
        "examples": [
            "class MyError : public std::exception { const char* what() const noexcept override { return \"Err\"; } };",
            "catch (const std::exception& e) { cout << e.what(); }"
        ]
    }
}

CPP_TOPICS[57] = {
    "id": 57,
    "title": "Stack Unwinding",
    "category": "Exception Handling",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "Stack unwinding is the runtime mechanism where call stack frames are removed step-by-step when an exception is thrown until a matching catch handler is located. Local (automatic) stack objects are destroyed in exact reverse order of construction. Heap allocations (new) are NOT automatically freed unless managed by RAII objects or smart pointers (std::unique_ptr).",
    "syntax": "void func() {\n    std::unique_ptr<int> data(new int(10));\n    throw std::runtime_error(\"Runtime failure!\");\n    // data destructor automatically frees memory during stack unwinding!\n}",
    "example": {
        "code": "#include <iostream>\n#include <memory>\n#include <stdexcept>\nusing namespace std;\n\nclass Demo {\n    string name;\npublic:\n    Demo(string n) : name(n) { cout << \"Constructed: \" << name << endl; }\n    ~Demo() { cout << \"Destroyed: \" << name << endl; }\n};\n\nvoid f1() {\n    Demo d1(\"f1_local\");\n    cout << \"f1() throwing exception...\" << endl;\n    throw runtime_error(\"Exception from f1()\");\n}\n\nvoid f2() {\n    Demo d2(\"f2_local\");\n    f1();\n}\n\nint main() {\n    try {\n        f2();\n    } catch (const exception& e) {\n        cout << \"Caught in main(): \" << e.what() << endl;\n    }\n    return 0;\n}",
        "output": "Constructed: f2_local\nConstructed: f1_local\nf1() throwing exception...\nDestroyed: f1_local\nDestroyed: f2_local\nCaught in main(): Exception from f1()",
        "explanation": "Constructors execute for f2_local then f1_local. When f1() throws an exception, stack unwinding destroys f1_local, pops f1 frame, destroys f2_local, pops f2 frame, and transfers control to catch in main()."
    },
    "fill_blanks": {
        "question": "Fill in the missing Stack Unwinding & RAII concepts:",
        "answers": ["unwinding", "reverse", "RAII", "unique_ptr"],
        "options": ["unwinding", "reverse", "RAII", "unique_ptr", "forward", "malloc"]
    },
    "compiler": {
        "title": "Stack Unwinding Practice",
        "starter_code": "#include <iostream>\n#include <memory>\n#include <stdexcept>\nusing namespace std;\n\nvoid func() {\n    unique_ptr<int> num(new int(42));\n    throw runtime_error(\"Error occurred!\");\n}\n\nint main() {\n    try {\n        func();\n    } catch (const exception& e) {\n        cout << \"Caught: \" << e.what() << endl;\n    }\n    return 0;\n}",
        "question": "Arrange lines to demonstrate safe dynamic resource management using unique_ptr during stack unwinding.",
        "options": [
            "#include <memory>",
            "void func() {",
            "    unique_ptr<int> num(new int(42));",
            "    throw runtime_error(\"Error occurred!\");",
            "}"
        ]
    },
    "skill_exa_test": [
        {
            "question": "In what order are local automatic objects destroyed during stack unwinding?",
            "options": [
                "In exact reverse order of their construction",
                "In the exact same order as their construction",
                "In arbitrary alphabetical order",
                "Local objects are not destroyed during stack unwinding"
            ],
            "answer": "In exact reverse order of their construction"
        },
        {
            "question": "What happens to raw dynamic heap memory allocated with operator new if an exception is thrown before calling delete?",
            "options": [
                "A memory leak occurs unless managed by an RAII object or smart pointer (e.g. std::unique_ptr)",
                "The garbage collector automatically reclaims the heap memory",
                "The compiler automatically adds delete statements during unwinding",
                "The heap pointer is reset to nullptr"
            ],
            "answer": "A memory leak occurs unless managed by an RAII object or smart pointer (e.g. std::unique_ptr)"
        },
        {
            "question": "What happens if a destructor throws another exception while stack unwinding is ALREADY in progress?",
            "options": [
                "std::terminate() is called immediately, crashing the application",
                "The second exception is queued until the first handler finishes",
                "The second exception overrides the first exception",
                "The program ignores the destructor exception"
            ],
            "answer": "std::terminate() is called immediately, crashing the application"
        },
        {
            "question": "What design pattern prevents memory and resource leaks during stack unwinding?",
            "options": [
                "RAII (Resource Acquisition Is Initialization)",
                "Singleton Pattern",
                "Factory Method Pattern",
                "Observer Pattern"
            ],
            "answer": "RAII (Resource Acquisition Is Initialization)"
        },
        {
            "question": "What occurs to function code statements located AFTER a throw statement during stack unwinding?",
            "options": [
                "They are never executed; control exits the function immediately",
                "They execute after the catch block completes",
                "They run asynchronously in a background thread",
                "They are logged to std::clog"
            ],
            "answer": "They are never executed; control exits the function immediately"
        }
    ],
    "theory": {
        "definition": "Stack Unwinding is the process of removing function stack frames and invoking destructors for local automatic objects when an exception propagates up the call stack.",
        "why": "Ensures stack-allocated resources (file handles, stack objects, smart pointers) are cleaned up safely during runtime errors.",
        "rules": [
            "Destructors for local objects execute in reverse order of construction.",
            "Raw heap allocations (new) require RAII smart pointers (unique_ptr) to prevent leaks.",
            "Destructors should be declared noexcept and NEVER throw exceptions during unwinding."
        ],
        "examples": [
            "void f() { Demo d; throw 1; } // d.~Demo() called automatically",
            "unique_ptr<int> p(new int(5)); // memory freed on unwind"
        ]
    }
}

CPP_TOPICS[58] = {
    "id": 58,
    "title": "User-Defined Exceptions",
    "category": "Exception Handling",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "User-defined exceptions allow programmers to define application-specific error types using classes (throw ClassName();). Enables fine-grained error dispatching. In inheritance hierarchies, catch block ordering is critical: derived-class catch blocks MUST be placed before base-class catch blocks. Constructors can throw exceptions to signal initialization failure.",
    "syntax": "class BaseErr {};\nclass DerivedErr : public BaseErr {};\n\ntry {\n    throw DerivedErr();\n} catch (const DerivedErr& d) { /* Derived handler FIRST */ }\ncatch (const BaseErr& b) { /* Base handler SECOND */ }",
    "example": {
        "code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nclass InvalidInputException {};\nclass OutOfBoundsException : public InvalidInputException {};\n\nclass DemoAccount {\n    int balance;\npublic:\n    DemoAccount(int initial) {\n        if (initial < 0) throw \"Negative initial balance!\";\n        balance = initial;\n        cout << \"Account created with balance: \" << balance << endl;\n    }\n};\n\nint main() {\n    for (int i = 1; i <= 2; i++) {\n        try {\n            if (i == 1) throw InvalidInputException();\n            else throw OutOfBoundsException();\n        } catch (const OutOfBoundsException& e) {\n            cout << \"Caught Derived OutOfBoundsException\" << endl;\n        } catch (const InvalidInputException& e) {\n            cout << \"Caught Base InvalidInputException\" << endl;\n        }\n    }\n\n    try {\n        DemoAccount acc(-50);\n    } catch (const char* msg) {\n        cout << \"Constructor Exception Caught: \" << msg << endl;\n    }\n    return 0;\n}",
        "output": "Caught Base InvalidInputException\nCaught Derived OutOfBoundsException\nConstructor Exception Caught: Negative initial balance!",
        "explanation": "Demonstrates user-defined exception classes, inheritance catch order (derived before base), and throwing/handling exceptions inside constructors."
    },
    "fill_blanks": {
        "question": "Fill in the missing User-Defined Exception concepts:",
        "answers": ["throw", "derived", "base", "constructor"],
        "options": ["throw", "derived", "base", "constructor", "virtual", "destructor"]
    },
    "compiler": {
        "title": "User-Defined Exceptions Practice",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nclass CustomAppError {};\n\nint main() {\n    try {\n        throw CustomAppError();\n    } catch (const CustomAppError& e) {\n        cout << \"Caught custom application error!\" << endl;\n    }\n    return 0;\n}",
        "question": "Arrange lines to define an empty user-defined exception class and catch its instance.",
        "options": [
            "class CustomAppError {};",
            "try {",
            "    throw CustomAppError();",
            "} catch (const CustomAppError& e) {",
            "    cout << \"Caught custom application error!\" << endl;",
            "}"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What critical rule must be followed when placing catch blocks for exception classes related by inheritance?",
            "options": [
                "Derived-class catch handlers MUST be placed BEFORE base-class catch handlers",
                "Base-class catch handlers MUST be placed BEFORE derived-class catch handlers",
                "Inherited exception classes cannot be caught in try-catch blocks",
                "Only the catch(...) handler can catch inherited exceptions"
            ],
            "answer": "Derived-class catch handlers MUST be placed BEFORE base-class catch handlers"
        },
        {
            "question": "What occurs if a base-class catch block (catch (Base b)) is placed BEFORE a derived-class catch block (catch (Derived d))?",
            "options": [
                "The base-class catch handler intercepts both base and derived exceptions, rendering the derived handler unreachable",
                "The compiler reorders the catch blocks automatically",
                "The derived handler executes twice",
                "A runtime bad_cast exception is thrown"
            ],
            "answer": "The base-class catch handler intercepts both base and derived exceptions, rendering the derived handler unreachable"
        },
        {
            "question": "Why are exceptions useful inside class constructors?",
            "options": [
                "Constructors cannot return status values, so throwing an exception signals object initialization failure safely",
                "Exceptions make constructor execution run twice as fast",
                "Exceptions allow constructors to allocate dynamic memory without new",
                "Exceptions override virtual functions"
            ],
            "answer": "Constructors cannot return status values, so throwing an exception signals object initialization failure safely"
        },
        {
            "question": "How is a user-defined class object thrown as an exception in C++?",
            "options": [
                "throw ClassName();",
                "raise ClassName();",
                "return exception ClassName();",
                "catch ClassName();"
            ],
            "answer": "throw ClassName();"
        },
        {
            "question": "What is an advantage of user-defined exception classes over throwing primitive types like int or const char*?",
            "options": [
                "Allows encapsulating custom domain metadata (e.g. error codes, failing input values, timestamps) in type-safe objects",
                "Eliminates the need for try blocks",
                "Bypasses compiler type checking",
                "Prevents destructors from running"
            ],
            "answer": "Allows encapsulating custom domain metadata (e.g. error codes, failing input values, timestamps) in type-safe objects"
        }
    ],
    "theory": {
        "definition": "User-Defined Exceptions are custom application-specific class types thrown using throw ClassName() to signal specific runtime errors.",
        "why": "Provides type-safe, domain-tailored error reporting with diagnostic fields.",
        "rules": [
            "Order catch blocks from most-derived exception type to most-base exception type.",
            "Throw exceptions inside constructors when object invariants fail.",
            "Objects thrown as exceptions are copied into exception storage during propagation."
        ],
        "examples": [
            "class InsufficientFundsError {};",
            "if (amt > bal) throw InsufficientFundsError();"
        ]
    }
}


CPP_TOPICS[59] = {
    "id": 59,
    "title": "Files and Streams",
    "category": "File Handling",
    "difficulty": "Advanced",
    "duration": "40 min",
    "concept": "File handling in C++ persists data to secondary storage using stream classes from <fstream> (ifstream for reading, ofstream for writing, fstream for both). Opening modes (ios::in, ios::out, ios::binary, ios::app, ios::trunc, ios::ate) control file interaction and can be combined via bitwise OR (|). Supports line-by-line reading (getline), status verification (is_open, eof, fail), raw byte binary I/O (read, write), and fixed-size chunk buffering for large files.",
    "syntax": "#include <fstream>\n\nofstream outFile(\"output.txt\", ios::out | ios::app);\nif (outFile.is_open()) {\n    outFile << \"Data line\\n\";\n    outFile.close();\n}",
    "example": {
        "code": "#include <iostream>\n#include <fstream>\n#include <string>\nusing namespace std;\n\nint main() {\n    // 1. Write text file\n    ofstream outFile(\"example.txt\");\n    if (outFile.is_open()) {\n        outFile << \"Welcome to SkillExa C++ File Handling!\\nLine 2\";\n        outFile.close();\n    }\n\n    // 2. Read text file line by line\n    ifstream inFile(\"example.txt\");\n    if (inFile.is_open()) {\n        string line;\n        while (getline(inFile, line)) {\n            cout << \"Read: \" << line << endl;\n        }\n        if (inFile.eof()) cout << \"Reached end of file.\" << endl;\n        inFile.close();\n    }\n\n    // 3. Binary file write and read\n    int number = 12345;\n    ofstream binOut(\"data.bin\", ios::binary);\n    binOut.write(reinterpret_cast<const char*>(&number), sizeof(number));\n    binOut.close();\n\n    int readNumber = 0;\n    ifstream binIn(\"data.bin\", ios::binary);\n    binIn.read(reinterpret_cast<char*>(&readNumber), sizeof(readNumber));\n    binIn.close();\n    cout << \"Binary Read Value: \" << readNumber << endl;\n    return 0;\n}",
        "output": "Read: Welcome to SkillExa C++ File Handling!\nRead: Line 2\nReached end of file.\nBinary Read Value: 12345",
        "explanation": "Demonstrates writing text with ofstream, reading line-by-line with ifstream and getline(), checking eof(), and handling raw binary integers with reinterpret_cast."
    },
    "fill_blanks": {
        "question": "Fill in the missing C++ File Handling stream classes and modes:",
        "answers": ["ifstream", "ofstream", "ios::binary", "getline"],
        "options": ["ifstream", "ofstream", "ios::binary", "getline", "cin", "cout"]
    },
    "compiler": {
        "title": "File Stream Practice",
        "starter_code": "#include <iostream>\n#include <fstream>\nusing namespace std;\n\nint main() {\n    ofstream file(\"sample.txt\");\n    if (file.is_open()) {\n        file << \"File Handling in C++\" << endl;\n        file.close();\n    }\n    return 0;\n}",
        "question": "Arrange lines to create an ofstream, write text, and close the file stream.",
        "options": [
            "#include <fstream>",
            "ofstream file(\"sample.txt\");",
            "if (file.is_open()) {",
            "    file << \"File Handling in C++\" << endl;",
            "    file.close();",
            "}"
        ]
    },
    "skill_exa_test": [
        {
            "question": "Which header file provides standard file stream classes (ifstream, ofstream, fstream) in C++?",
            "options": [
                "<fstream>",
                "<iostream>",
                "<sstream>",
                "<fileio>"
            ],
            "answer": "<fstream>"
        },
        {
            "question": "What is the behavior of opening a file in ios::app (append) mode?",
            "options": [
                "All output operations write data exclusively at the end of the file, preserving existing content",
                "It discards all existing file contents prior to writing",
                "It sets the file mode to binary input",
                "It throws std::bad_alloc if the file exists"
            ],
            "answer": "All output operations write data exclusively at the end of the file, preserving existing content"
        },
        {
            "question": "Which member function is used to verify whether a file stream was successfully opened?",
            "options": [
                "is_open()",
                "good_file()",
                "check_stream()",
                "exists()"
            ],
            "answer": "is_open()"
        },
        {
            "question": "How should binary data (e.g. raw integer buffers) be written to a binary file opened with ios::binary?",
            "options": [
                "file.write(reinterpret_cast<const char*>(&buffer), sizeof(buffer));",
                "file << buffer;",
                "file.print(buffer);",
                "file.put_binary(buffer);"
            ],
            "answer": "file.write(reinterpret_cast<const char*>(&buffer), sizeof(buffer));"
        },
        {
            "question": "Why is std::getline(file, str) preferred over file >> str when reading lines of text from a file?",
            "options": [
                "getline() reads the entire line including spaces, whereas operator>> stops at the first whitespace character",
                "operator>> cannot read characters",
                "getline() automatically converts text to uppercase",
                "operator>> only works for binary files"
            ],
            "answer": "getline() reads the entire line including spaces, whereas operator>> stops at the first whitespace character"
        }
    ],
    "theory": {
        "definition": "Files and Streams in C++ use <fstream> classes (ifstream, ofstream, fstream) to read and write persistent data on disk.",
        "why": "Enables data persistence across application restarts for configuration, logs, databases, and media files.",
        "rules": [
            "Use ifstream for reading, ofstream for writing, and fstream for dual I/O.",
            "Combine opening modes using bitwise OR (e.g. ios::in | ios::out | ios::binary).",
            "Always check file.is_open() before performing I/O operations.",
            "Always call file.close() when finished to flush buffers and release system handles."
        ],
        "examples": [
            "ofstream out(\"log.txt\", ios::app); out << \"log\";",
            "ifstream in(\"data.bin\", ios::binary); in.read(buf, size);"
        ]
    }
}

CPP_TOPICS[60] = {
    "id": 60,
    "title": "I/O Redirection",
    "category": "File Handling",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "I/O Redirection alters standard input (cin) and output (cout) streams from the console to files or secondary streams. C++ stream buffer redirection uses ios::rdbuf() to swap streambuf* pointers (saving original buffers for later restoration). Inherited C-style redirection uses freopen(\"file\", \"w\", stdout). Essential for automated batch testing, data pipelines, error logging, and clean console output.",
    "syntax": "#include <iostream>\n#include <fstream>\n\nofstream file(\"output.txt\");\nstreambuf* original_cout = cout.rdbuf();\ncout.rdbuf(file.rdbuf()); // Redirect cout -> file\ncout << \"Written to file!\";\ncout.rdbuf(original_cout); // Restore console",
    "example": {
        "code": "#include <iostream>\n#include <fstream>\n#include <string>\n#include <cstdio>\nusing namespace std;\n\nint main() {\n    // 1. C++ streambuf Redirection (cout)\n    ofstream outFile(\"redirected_out.txt\");\n    streambuf* orig_cout_buf = cout.rdbuf();\n    cout.rdbuf(outFile.rdbuf()); // Redirect cout -> file\n\n    cout << \"This line is written to redirected_out.txt via cout!\" << endl;\n    cout.flush();\n\n    cout.rdbuf(orig_cout_buf); // Restore console cout\n    cout << \"Console output restored successfully!\" << endl;\n    outFile.close();\n\n    // 2. C-style Redirection using freopen\n    if (freopen(\"freopen_log.txt\", \"w\", stdout) != NULL) {\n        cout << \"Logged via freopen redirect!\" << endl;\n    }\n    return 0;\n}",
        "output": "Console output restored successfully!",
        "explanation": "Illustrates manipulating cout's stream buffer via cout.rdbuf(), writing cout statements into a file, restoring the original console buffer, and C-style freopen() redirection."
    },
    "fill_blanks": {
        "question": "Fill in the missing I/O redirection member functions and streams:",
        "answers": ["rdbuf", "streambuf", "freopen", "stdout"],
        "options": ["rdbuf", "streambuf", "freopen", "stdout", "buffer", "stdin"]
    },
    "compiler": {
        "title": "I/O Redirection Practice",
        "starter_code": "#include <iostream>\n#include <fstream>\nusing namespace std;\n\nint main() {\n    ofstream file(\"out.txt\");\n    streambuf* backup = cout.rdbuf();\n    cout.rdbuf(file.rdbuf());\n    cout << \"Redirected text\" << endl;\n    cout.rdbuf(backup);\n    return 0;\n}",
        "question": "Arrange lines to back up cout buffer, redirect cout to a file, print text, and restore cout.",
        "options": [
            "streambuf* backup = cout.rdbuf();",
            "cout.rdbuf(file.rdbuf());",
            "cout << \"Redirected text\" << endl;",
            "cout.rdbuf(backup);"
        ]
    },
    "skill_exa_test": [
        {
            "question": "Which C++ member function is used to access or swap internal stream buffers for I/O redirection?",
            "options": [
                "ios::rdbuf()",
                "ios::redirect()",
                "ios::swap_buffer()",
                "ios::set_stream()"
            ],
            "answer": "ios::rdbuf()"
        },
        {
            "question": "Why is it important to save the original streambuf* pointer before redirecting cout.rdbuf()?",
            "options": [
                "To restore standard console output capability after file redirection completes",
                "To prevent the compiler from generating warning flags",
                "To increase heap memory size",
                "To clear the file contents"
            ],
            "answer": "To restore standard console output capability after file redirection completes"
        },
        {
            "question": "What is the function signature of C-style file stream redirection inherited from C?",
            "options": [
                "freopen(fileName, mode, stream)",
                "redirect_stream(fileName, mode)",
                "rdbuf_open(fileName, stream)",
                "fopen_redirect(fileName, mode)"
            ],
            "answer": "freopen(fileName, mode, stream)"
        },
        {
            "question": "What key distinction exists between ios::rdbuf() and freopen()?",
            "options": [
                "ios::rdbuf() operates at C++ stream buffer level allowing temporary restoration; freopen() redirects file descriptors at C-level",
                "freopen() only works on Windows operating systems",
                "ios::rdbuf() cannot redirect cin",
                "freopen() does not support text files"
            ],
            "answer": "ios::rdbuf() operates at C++ stream buffer level allowing temporary restoration; freopen() redirects file descriptors at C-level"
        },
        {
            "question": "What is a major practical use case of I/O redirection in software development?",
            "options": [
                "Automating test suites by feeding input files to cin and logging cout output to files",
                "Accelerating binary compilation speed",
                "Encrypting source code files",
                "Replacing main() entry points"
            ],
            "answer": "Automating test suites by feeding input files to cin and logging cout output to files"
        }
    ],
    "theory": {
        "definition": "I/O Redirection changes default stream sources (cin) and destinations (cout) to read/write external file streams.",
        "why": "Enables automated testing, data pipelines, error logging, and competitive programming input/output automation.",
        "rules": [
            "Backup original streambuf* pointers (cout_buf = cout.rdbuf()) before redirecting.",
            "Assign file streambuf* to console stream (cout.rdbuf(file_buf)).",
            "Flush output streams (cout.flush()) before restoring buffers.",
            "Restore original streambuf* (cout.rdbuf(cout_buf)) when redirection completes."
        ],
        "examples": [
            "streambuf* old = cout.rdbuf(file.rdbuf());",
            "freopen(\"input.txt\", \"r\", stdin);"
        ]
    }
}


CPP_TOPICS[61] = {
    "id": 61,
    "title": "Introduction to Multithreading",
    "category": "Multithreading",
    "difficulty": "Advanced",
    "duration": "40 min",
    "concept": "Multithreading in C++ (C++11 <thread>) enables concurrent execution of multiple threads within a single process sharing memory space. Maximizes CPU multi-core utilization and system responsiveness. Management features include this_thread::get_id(), this_thread::sleep_for(), and thread::hardware_concurrency(). Multithreading problems include deadlocks, race conditions, starvation, and context switching overhead.",
    "syntax": "#include <thread>\n#include <chrono>\n\nstd::thread t(taskFunc);\nunsigned int cores = std::thread::hardware_concurrency();\nstd::this_thread::sleep_for(std::chrono::milliseconds(100));",
    "example": {
        "code": "#include <iostream>\n#include <thread>\n#include <chrono>\nusing namespace std;\n\nvoid task1() {\n    cout << \"Task 1 running on thread ID: \" << this_thread::get_id() << endl;\n}\n\nvoid task2() {\n    cout << \"Task 2 running on thread ID: \" << this_thread::get_id() << endl;\n}\n\nint main() {\n    cout << \"Hardware Concurrency: \" << thread::hardware_concurrency() << \" cores\" << endl;\n    thread t1(task1);\n    thread t2(task2);\n\n    cout << \"Main thread ID: \" << this_thread::get_id() << endl;\n    if (t1.joinable()) t1.join();\n    if (t2.joinable()) t2.join();\n    cout << \"Multithreading execution completed.\" << endl;\n    return 0;\n}",
        "output": "Hardware Concurrency: 8 cores\nTask 1 running on thread ID: 140737347512000\nTask 2 running on thread ID: 140737213290176\nMain thread ID: 140737110000000\nMultithreading execution completed.",
        "explanation": "Demonstrates hardware_concurrency(), thread creation, retrieving unique IDs via this_thread::get_id(), and checking joinable() state before joining."
    },
    "fill_blanks": {
        "question": "Fill in the missing C++ multithreading functions:",
        "answers": ["hardware_concurrency", "get_id", "sleep_for", "thread"],
        "options": ["hardware_concurrency", "get_id", "sleep_for", "thread", "process", "fork"]
    },
    "compiler": {
        "title": "Multithreading Basics Practice",
        "starter_code": "#include <iostream>\n#include <thread>\nusing namespace std;\n\nvoid printHello() {\n    cout << \"Hello from thread!\" << endl;\n}\n\nint main() {\n    thread t(printHello);\n    t.join();\n    return 0;\n}",
        "question": "Arrange lines to create a std::thread executing printHello and join it.",
        "options": [
            "#include <thread>",
            "void printHello() { cout << \"Hello from thread!\" << endl; }",
            "thread t(printHello);",
            "t.join();"
        ]
    },
    "skill_exa_test": [
        {
            "question": "Which C++ standard library header file introduced native multithreading support in C++11?",
            "options": [
                "<thread>",
                "<pthread.h>",
                "<process>",
                "<concurrent>"
            ],
            "answer": "<thread>"
        },
        {
            "question": "Which static member function of std::thread returns the number of concurrent hardware execution cores?",
            "options": [
                "std::thread::hardware_concurrency()",
                "std::thread::cpu_count()",
                "std::thread::core_capacity()",
                "std::thread::max_threads()"
            ],
            "answer": "std::thread::hardware_concurrency()"
        },
        {
            "question": "What is a CPU Context Switch in multithreading?",
            "options": [
                "Saving the state of the current running thread and loading the state of another thread to share CPU time",
                "Converting C++ code to machine assembly",
                "Switching between RAM and disk memory",
                "Freeing heap allocation"
            ],
            "answer": "Saving the state of the current running thread and loading the state of another thread to share CPU time"
        },
        {
            "question": "What problem occurs when two threads wait indefinitely for resources held by each other?",
            "options": [
                "Deadlock",
                "Race Condition",
                "Memory Leak",
                "Stack Overflow"
            ],
            "answer": "Deadlock"
        },
        {
            "question": "Which function retrieves the unique ID of the currently executing thread?",
            "options": [
                "std::this_thread::get_id()",
                "std::thread::id()",
                "std::get_process_id()",
                "std::current_thread()"
            ],
            "answer": "std::this_thread::get_id()"
        }
    ],
    "theory": {
        "definition": "Multithreading enables concurrent execution of multiple threads sharing the same memory address space within a process.",
        "why": "Improves performance, CPU multi-core utilization, and application responsiveness.",
        "rules": [
            "Native multithreading is defined in <thread> since C++11.",
            "Threads share process memory but maintain independent call stacks.",
            "Always synchronize shared mutable data to avoid race conditions and deadlocks."
        ],
        "examples": [
            "thread t(func); t.join();",
            "this_thread::sleep_for(chrono::milliseconds(100));"
        ]
    }
}

CPP_TOPICS[62] = {
    "id": 62,
    "title": "Creating Threads",
    "category": "Multithreading",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "std::thread objects execute callable targets passed to their constructors. Supported callables include Function Pointers, Lambda Expressions ([](args){}), Functors (classes overloading operator()), and Non-Static/Static Member Functions. Member functions require passing member pointers (&Class::func) and object instances (&obj).",
    "syntax": "thread t1(funcPtr, arg1);                // Function Pointer\nthread t2([](int a){ cout << a; }, 10);  // Lambda\nthread t3(FunctorObj(5));               // Functor\nthread t4(&MyClass::memFunc, &obj, 10);  // Member Function",
    "example": {
        "code": "#include <iostream>\n#include <thread>\nusing namespace std;\n\nvoid printNum(int n) { cout << \"Function Pointer: \" << n << endl; }\n\nclass SumFunctor {\npublic:\n    void operator()(int a, int b) const { cout << \"Functor Sum: \" << (a + b) << endl; }\n};\n\nclass MyWorker {\npublic:\n    void memberTask(string msg) { cout << \"Member Function: \" << msg << endl; }\n    static void staticTask(int val) { cout << \"Static Member: \" << val << endl; }\n};\n\nint main() {\n    thread t1(printNum, 42);\n    thread t2([](string s) { cout << \"Lambda Expression: \" << s << endl; }, \"SkillExa\");\n    thread t3(SumFunctor(), 10, 20);\n    MyWorker worker;\n    thread t4(&MyWorker::memberTask, &worker, \"Running...\");\n    thread t5(&MyWorker::staticTask, 99);\n\n    t1.join(); t2.join(); t3.join(); t4.join(); t5.join();\n    return 0;\n}",
        "output": "Function Pointer: 42\nLambda Expression: SkillExa\nFunctor Sum: 30\nMember Function: Running...\nStatic Member: 99",
        "explanation": "Illustrates 5 ways to create threads: regular function pointer, inline lambda, functor object, class member function with object pointer, and static member function."
    },
    "fill_blanks": {
        "question": "Fill in the missing C++ thread callable forms:",
        "answers": ["Lambda", "Functor", "Member", "pointer"],
        "options": ["Lambda", "Functor", "Member", "pointer", "Macro", "Template"]
    },
    "compiler": {
        "title": "Thread Creation Practice",
        "starter_code": "#include <iostream>\n#include <thread>\nusing namespace std;\n\nint main() {\n    thread t([](int val) {\n        cout << \"Lambda value: \" << val << endl;\n    }, 100);\n    t.join();\n    return 0;\n}",
        "question": "Arrange lines to launch a thread with a lambda taking an integer parameter.",
        "options": [
            "#include <thread>",
            "thread t([](int val) {",
            "    cout << \"Lambda value: \" << val << endl;",
            "}, 100);",
            "t.join();"
        ]
    },
    "skill_exa_test": [
        {
            "question": "Which parameter must be supplied when initializing a std::thread with a non-static class member function?",
            "options": [
                "The address of the member function (&Class::func) AND a pointer to the class instance (&obj)",
                "Only the function name",
                "A nullptr reference",
                "The virtual table index"
            ],
            "answer": "The address of the member function (&Class::func) AND a pointer to the class instance (&obj)"
        },
        {
            "question": "What operator must a class overload to qualify as a callable Functor object for std::thread?",
            "options": [
                "operator()",
                "operator*",
                "operator->",
                "operator[]"
            ],
            "answer": "operator()"
        },
        {
            "question": "When does execution of a thread's callable target begin?",
            "options": [
                "Immediately upon construction of the std::thread object",
                "Only after calling std::thread::start()",
                "When main() finishes",
                "When join() is called"
            ],
            "answer": "Immediately upon construction of the std::thread object"
        },
        {
            "question": "How can arguments be passed by reference to a thread callable?",
            "options": [
                "Wrap the argument using std::ref(var)",
                "Pass by value automatically converts to reference",
                "Use raw C pointers only",
                "Use const_cast"
            ],
            "answer": "Wrap the argument using std::ref(var)"
        },
        {
            "question": "Why is passing an object pointer NOT required when launching a thread with a static member function?",
            "options": [
                "Static member functions belong to the class type itself and do not operate on an implicit 'this' instance",
                "Static functions run on the main stack frame",
                "Static functions do not accept arguments",
                "Static functions run inside the compiler"
            ],
            "answer": "Static member functions belong to the class type itself and do not operate on an implicit 'this' instance"
        }
    ],
    "theory": {
        "definition": "Creating Threads constructs a std::thread object bound to a callable (function pointer, lambda, functor, or member function).",
        "why": "Provides flexible invocation patterns for concurrent background tasks.",
        "rules": [
            "Construct std::thread with callable and arguments.",
            "Non-static member functions require passing object instance pointer (&obj).",
            "Always join or detach before destructor runs."
        ],
        "examples": [
            "thread t([](){ cout << \"hi\"; });",
            "thread t(&Class::mem, &obj, arg);"
        ]
    }
}

CPP_TOPICS[63] = {
    "id": 63,
    "title": "std::thread::join()",
    "category": "Multithreading",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "std::thread::join() is a member function of std::thread that blocks the calling thread until the target thread completes execution. A thread can be joined only once while in a joinable() state. Destroying a joinable std::thread object without calling join() or detach() invokes std::terminate(), crashing the program.",
    "syntax": "std::thread t(task);\nif (t.joinable()) {\n    t.join(); // Blocks calling thread until t finishes\n}",
    "example": {
        "code": "#include <iostream>\n#include <thread>\n#include <chrono>\nusing namespace std;\n\nvoid workerTask() {\n    cout << \"Worker thread starting work...\" << endl;\n    this_thread::sleep_for(chrono::milliseconds(200));\n    cout << \"Worker thread completed work.\" << endl;\n}\n\nint main() {\n    thread t(workerTask);\n\n    if (t.joinable()) {\n        cout << \"Main thread waiting at join()...\" << endl;\n        t.join();\n        cout << \"Worker thread successfully joined!\" << endl;\n    }\n    cout << \"Is thread still joinable? \" << (t.joinable() ? \"Yes\" : \"No\") << endl;\n    return 0;\n}",
        "output": "Worker thread starting work...\nMain thread waiting at join()...\nWorker thread completed work.\nWorker thread successfully joined!\nIs thread still joinable? No",
        "explanation": "Main thread creates worker thread, checks joinable(), blocks at join() until workerTask finishes, and verifies joinable() returns false post-join."
    },
    "fill_blanks": {
        "question": "Fill in the missing std::thread::join() concepts:",
        "answers": ["join", "joinable", "blocks", "terminate"],
        "options": ["join", "joinable", "blocks", "terminate", "detach", "pause"]
    },
    "compiler": {
        "title": "Thread Join Practice",
        "starter_code": "#include <iostream>\n#include <thread>\nusing namespace std;\n\nvoid task() { cout << \"Running...\" << endl; }\n\nint main() {\n    thread t(task);\n    if (t.joinable()) t.join();\n    return 0;\n}",
        "question": "Arrange lines to check if a thread is joinable before calling join().",
        "options": [
            "thread t(task);",
            "if (t.joinable()) {",
            "    t.join();",
            "}"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What is the primary execution behavior of std::thread::join()?",
            "options": [
                "It blocks the calling thread until the target thread finishes execution",
                "It terminates the target thread immediately",
                "It pauses the target thread temporarily",
                "It moves the target thread to a background process"
            ],
            "answer": "It blocks the calling thread until the target thread finishes execution"
        },
        {
            "question": "What happens if a joinable std::thread object goes out of scope without calling join() or detach()?",
            "options": [
                "The std::thread destructor invokes std::terminate(), crashing the application",
                "The thread joins automatically",
                "The thread is detached automatically",
                "The compiler logs a runtime warning"
            ],
            "answer": "The std::thread destructor invokes std::terminate(), crashing the application"
        },
        {
            "question": "How many times can join() be successfully invoked on a single std::thread object?",
            "options": [
                "Exactly once (after which joinable() returns false)",
                "Multiple times without restriction",
                "Twice",
                "Unlimited times"
            ],
            "answer": "Exactly once (after which joinable() returns false)"
        },
        {
            "question": "What exception is thrown if join() is called on a non-joinable thread object?",
            "options": [
                "std::system_error",
                "std::out_of_range",
                "std::bad_alloc",
                "std::runtime_error"
            ],
            "answer": "std::system_error"
        },
        {
            "question": "What value does t.joinable() return after t.join() has executed?",
            "options": [
                "false",
                "true",
                "nullptr",
                "1"
            ],
            "answer": "false"
        }
    ],
    "theory": {
        "definition": "std::thread::join() synchronizes thread execution by forcing the calling thread to wait for target thread completion.",
        "why": "Guarantees thread work finishes before accessing results or exiting program.",
        "rules": [
            "join() blocks calling thread execution.",
            "Check joinable() before calling join().",
            "A thread can only be joined once.",
            "Destroying a joinable thread without join/detach calls std::terminate()."
        ],
        "examples": [
            "thread t(work); t.join();",
            "if (t.joinable()) t.join();"
        ]
    }
}

CPP_TOPICS[64] = {
    "id": 64,
    "title": "Detaching a Thread",
    "category": "Multithreading",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "std::thread::detach() separates a thread from its std::thread handle, permitting independent background execution. Ownership is transferred to the operating system, which automatically reclaims thread resources upon completion. After calling detach(), joinable() returns false, and the thread cannot be joined.",
    "syntax": "std::thread t(backgroundTask);\nt.detach(); // Separates thread for independent execution",
    "example": {
        "code": "#include <iostream>\n#include <thread>\n#include <chrono>\nusing namespace std;\n\nvoid backgroundWorker() {\n    cout << \"Background detached worker running...\" << endl;\n    this_thread::sleep_for(chrono::milliseconds(50));\n    cout << \"Background detached worker finished.\" << endl;\n}\n\nint main() {\n    thread t(backgroundWorker);\n    t.detach();\n\n    cout << \"Main thread continues without waiting...\" << endl;\n    cout << \"Is t joinable after detach? \" << (t.joinable() ? \"Yes\" : \"No\") << endl;\n\n    this_thread::sleep_for(chrono::milliseconds(100));\n    cout << \"Main thread exiting.\" << endl;\n    return 0;\n}",
        "output": "Main thread continues without waiting...\nIs t joinable after detach? No\nBackground detached worker running...\nBackground detached worker finished.\nMain thread exiting.",
        "explanation": "Main thread creates and detaches worker thread, verifies t.joinable() is false, and continues execution independently while OS manages detached thread."
    },
    "fill_blanks": {
        "question": "Fill in the missing C++ thread detachment concepts:",
        "answers": ["detach", "independent", "false", "system"],
        "options": ["detach", "independent", "false", "system", "join", "true"]
    },
    "compiler": {
        "title": "Thread Detach Practice",
        "starter_code": "#include <iostream>\n#include <thread>\nusing namespace std;\n\nvoid bgTask() { cout << \"Background task\" << endl; }\n\nint main() {\n    thread t(bgTask);\n    t.detach();\n    return 0;\n}",
        "question": "Arrange lines to detach a thread for background execution.",
        "options": [
            "#include <thread>",
            "thread t(bgTask);",
            "t.detach();",
            "return 0;"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What happens to ownership and resource management of a thread after calling std::thread::detach()?",
            "options": [
                "Ownership is transferred to the OS, which executes it independently and frees resources upon completion",
                "The thread is deleted immediately",
                "The thread is paused until join() is called",
                "The main thread is terminated"
            ],
            "answer": "Ownership is transferred to the OS, which executes it independently and frees resources upon completion"
        },
        {
            "question": "What does std::thread::joinable() return after detach() has been called on a thread object?",
            "options": [
                "false",
                "true",
                "nullptr",
                "std::system_error"
            ],
            "answer": "false"
        },
        {
            "question": "Can a detached thread be joined later using join()?",
            "options": [
                "No, calling join() on a detached (non-joinable) thread throws std::system_error",
                "Yes, anytime",
                "Yes, if called within 5 seconds",
                "Yes, using force_join()"
            ],
            "answer": "No, calling join() on a detached (non-joinable) thread throws std::system_error"
        },
        {
            "question": "What risk must developers manage when detaching a thread that accesses local variables or shared resources?",
            "options": [
                "Dangling reference/pointer errors if the creator thread exits and destroys local variables while detached thread is still running",
                "Compiler syntax error",
                "Hardware overheating",
                "Stack overflow on main thread"
            ],
            "answer": "Dangling reference/pointer errors if the creator thread exits and destroys local variables while detached thread is still running"
        },
        {
            "question": "Which scenarios are best suited for detaching threads?",
            "options": [
                "Long-running background tasks (e.g. logging, background monitoring) where the caller does not require return values",
                "Tasks where return values are needed immediately",
                "Synchronous mathematical calculations",
                "Destructor invocations"
            ],
            "answer": "Long-running background tasks (e.g. logging, background monitoring) where the caller does not require return values"
        }
    ],
    "theory": {
        "definition": "std::thread::detach() separates a thread handle from its execution context, allowing autonomous background processing.",
        "why": "Useful for background daemons, loggers, and task handlers that do not require return synchronization.",
        "rules": [
            "detach() makes joinable() return false.",
            "Detached threads cannot be joined.",
            "Ensure shared resources accessed by detached threads remain valid throughout execution."
        ],
        "examples": [
            "thread t(logger); t.detach();",
            "if (t.joinable()) t.detach();"
        ]
    }
}

CPP_TOPICS[65] = {
    "id": 65,
    "title": "Mutex",
    "category": "Multithreading",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "std::mutex (<mutex>) is a mutual exclusion synchronization primitive protecting shared resources from concurrent multi-thread access. Critical sections are guarded by lock() (acquires exclusive lock) and unlock() (releases lock). Prevents race conditions and guarantees thread-safe execution.",
    "syntax": "#include <mutex>\n\nstd::mutex mtx;\nmtx.lock();\n// Critical section modifying shared resource\nmtx.unlock();",
    "example": {
        "code": "#include <iostream>\n#include <thread>\n#include <mutex>\nusing namespace std;\n\nmutex mtx;\nint sharedCounter = 0;\n\nvoid incrementTask() {\n    for (int i = 0; i < 100000; i++) {\n        mtx.lock();\n        sharedCounter++;\n        mtx.unlock();\n    }\n}\n\nint main() {\n    thread t1(incrementTask);\n    thread t2(incrementTask);\n\n    t1.join(); t2.join();\n    cout << \"Synchronized Counter with Mutex: \" << sharedCounter << endl;\n    return 0;\n}",
        "output": "Synchronized Counter with Mutex: 200000",
        "explanation": "Two threads increment sharedCounter 100,000 times each. mtx.lock() and mtx.unlock() ensure exclusive access, producing exact count 200,000 without race condition losses."
    },
    "fill_blanks": {
        "question": "Fill in the missing C++ Mutex concepts:",
        "answers": ["mutex", "lock", "unlock", "critical"],
        "options": ["mutex", "lock", "unlock", "critical", "semaphore", "signal"]
    },
    "compiler": {
        "title": "Mutex Practice Sandbox",
        "starter_code": "#include <iostream>\n#include <thread>\n#include <mutex>\nusing namespace std;\n\nmutex mtx;\nint val = 0;\n\nvoid add() {\n    mtx.lock();\n    val += 5;\n    mtx.unlock();\n}\n\nint main() {\n    thread t1(add);\n    thread t2(add);\n    t1.join(); t2.join();\n    cout << val << endl;\n    return 0;\n}",
        "question": "Arrange lines to protect variable addition inside a mutex lock/unlock critical section.",
        "options": [
            "mutex mtx;",
            "mtx.lock();",
            "val += 5;",
            "mtx.unlock();"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What is the primary function of std::mutex in multithreaded C++ programming?",
            "options": [
                "Protects shared resources from concurrent access by allowing only one thread inside a critical section at a time",
                "Allocates heap memory for threads",
                "Accelerates thread creation speed",
                "Compiles lambda expressions"
            ],
            "answer": "Protects shared resources from concurrent access by allowing only one thread inside a critical section at a time"
        },
        {
            "question": "What happens if a second thread calls mtx.lock() while another thread currently holds the lock?",
            "options": [
                "The second thread blocks and waits until the first thread calls mtx.unlock()",
                "The second thread throws std::bad_alloc",
                "The second thread terminates immediately",
                "The program crashes with a syntax error"
            ],
            "answer": "The second thread blocks and waits until the first thread calls mtx.unlock()"
        },
        {
            "question": "What major risk occurs if a function returns or throws an exception after calling mtx.lock() without calling mtx.unlock()?",
            "options": [
                "A Deadlock occurs because the mutex remains permanently locked",
                "The mutex unlocks automatically",
                "The thread re-runs from main()",
                "The operating system resets the mutex"
            ],
            "answer": "A Deadlock occurs because the mutex remains permanently locked"
        },
        {
            "question": "Which C++ header file defines std::mutex?",
            "options": [
                "<mutex>",
                "<thread>",
                "<condition_variable>",
                "<future>"
            ],
            "answer": "<mutex>"
        },
        {
            "question": "Why are RAII lock wrappers (lock_guard, unique_lock) preferred over manual lock()/unlock() calls?",
            "options": [
                "They automatically release the mutex upon scope exit or exception propagation, eliminating deadlock bugs",
                "They make code execute faster",
                "They bypass operating system locks",
                "They allow multiple threads to enter simultaneously"
            ],
            "answer": "They automatically release the mutex upon scope exit or exception propagation, eliminating deadlock bugs"
        }
    ],
    "theory": {
        "definition": "std::mutex is a mutual exclusion primitive used to serialize access to shared critical section resources across concurrent threads.",
        "why": "Eliminates data corruption and race conditions during simultaneous read/write access.",
        "rules": [
            "Acquire lock via lock() before accessing shared data.",
            "Release lock via unlock() immediately after completing operations.",
            "Never leave mutexes locked when exiting functions or throwing exceptions."
        ],
        "examples": [
            "mutex m; m.lock(); shared++; m.unlock();",
            "lock_guard<mutex> lock(m);"
        ]
    }
}

CPP_TOPICS[66] = {
    "id": 66,
    "title": "Lock Guard",
    "category": "Multithreading",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "std::lock_guard and std::unique_lock are RAII-based mutex wrappers. std::lock_guard locks a mutex upon construction and unlocks upon scope exit (lightweight, minimal overhead). std::unique_lock offers advanced capabilities: manual lock/unlock, deferred locking (std::defer_lock), timed locking, lock movement, and compatibility with std::condition_variable.",
    "syntax": "std::mutex mtx;\n{\n    std::lock_guard<std::mutex> lock(mtx); // Automatic RAII lock/unlock\n    // Critical section\n}\n{\n    std::unique_lock<std::mutex> ulock(mtx, std::defer_lock); // Flexible\n    ulock.lock();\n}",
    "example": {
        "code": "#include <iostream>\n#include <thread>\n#include <mutex>\nusing namespace std;\n\nmutex mtx;\nint sharedVal = 0;\n\nvoid safeIncrementGuard() {\n    lock_guard<mutex> lock(mtx); // RAII auto lock/unlock\n    sharedVal += 10;\n}\n\nvoid flexibleIncrementUnique() {\n    unique_lock<mutex> ulock(mtx, defer_lock);\n    ulock.lock();\n    sharedVal += 20;\n    ulock.unlock();\n}\n\nint main() {\n    thread t1(safeIncrementGuard);\n    thread t2(flexibleIncrementUnique);\n    t1.join(); t2.join();\n    cout << \"Final Shared Value: \" << sharedVal << endl;\n    return 0;\n}",
        "output": "Final Shared Value: 30",
        "explanation": "Illustrates lock_guard for automatic scope-bound locking and unique_lock with defer_lock for manual explicit locking control."
    },
    "fill_blanks": {
        "question": "Fill in the missing Mutex Wrapper keywords:",
        "answers": ["lock_guard", "unique_lock", "defer_lock", "RAII"],
        "options": ["lock_guard", "unique_lock", "defer_lock", "RAII", "static_lock", "auto_lock"]
    },
    "compiler": {
        "title": "Lock Wrappers Practice",
        "starter_code": "#include <iostream>\n#include <thread>\n#include <mutex>\nusing namespace std;\n\nmutex mtx;\n\nvoid task() {\n    lock_guard<mutex> lock(mtx);\n    cout << \"Thread-safe task execution\" << endl;\n}\n\nint main() {\n    thread t(task);\n    t.join();\n    return 0;\n}",
        "question": "Arrange lines to implement thread-safe execution using std::lock_guard.",
        "options": [
            "mutex mtx;",
            "void task() {",
            "    lock_guard<mutex> lock(mtx);",
            "    cout << \"Thread-safe task execution\" << endl;",
            "}"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What primary design pattern is utilized by std::lock_guard and std::unique_lock?",
            "options": [
                "RAII (Resource Acquisition Is Initialization)",
                "Factory Pattern",
                "Singleton Pattern",
                "Observer Pattern"
            ],
            "answer": "RAII (Resource Acquisition Is Initialization)"
        },
        {
            "question": "What advantage does std::unique_lock offer over std::lock_guard?",
            "options": [
                "Supports manual locking/unlocking, deferred locking (std::defer_lock), timed locking, and std::condition_variable integration",
                "Runs faster with less memory",
                "Does not require a mutex reference",
                "Can be copied across threads"
            ],
            "answer": "Supports manual locking/unlocking, deferred locking (std::defer_lock), timed locking, and std::condition_variable integration"
        },
        {
            "question": "Why is std::lock_guard preferred when simple scope-bound locking is sufficient?",
            "options": [
                "It has lower performance overhead and a simpler API than std::unique_lock",
                "It allows multiple threads inside critical section",
                "It converts mutexes to atomic variables",
                "It prevents deadlocks across processes"
            ],
            "answer": "It has lower performance overhead and a simpler API than std::unique_lock"
        },
        {
            "question": "What does passing std::defer_lock to std::unique_lock's constructor accomplish?",
            "options": [
                "Constructs the wrapper associated with the mutex WITHOUT immediately locking it",
                "Unlocks the mutex immediately",
                "Deletes the mutex",
                "Throws std::system_error"
            ],
            "answer": "Constructs the wrapper associated with the mutex WITHOUT immediately locking it"
        },
        {
            "question": "Which mutex wrapper is strictly required when working with std::condition_variable::wait()?",
            "options": [
                "std::unique_lock<std::mutex>",
                "std::lock_guard<std::mutex>",
                "std::atomic<std::mutex>",
                "std::shared_ptr<std::mutex>"
            ],
            "answer": "std::unique_lock<std::mutex>"
        }
    ],
    "theory": {
        "definition": "std::lock_guard and std::unique_lock are RAII wrappers that acquire mutexes on construction and release them on scope destruction.",
        "why": "Guarantees exception-safe mutex release without manual unlock calls.",
        "rules": [
            "Use lock_guard for simple scope-bound critical sections.",
            "Use unique_lock for deferred locking, manual unlocking, and condition variables.",
            "Lock wrappers cannot be copied (non-copyable)."
        ],
        "examples": [
            "lock_guard<mutex> lock(mtx);",
            "unique_lock<mutex> lock(mtx, defer_lock);"
        ]
    }
}

CPP_TOPICS[67] = {
    "id": 67,
    "title": "Race Conditions",
    "category": "Multithreading",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "A race condition occurs when multiple threads access and modify shared data concurrently without proper synchronization. The execution outcome depends unpredictably on CPU thread scheduling. Prevented using std::mutex, RAII lock guards, or lock-free atomic operations (std::atomic).",
    "syntax": "#include <mutex>\n#include <atomic>\n\nstd::atomic<int> atomicCount(0); // Thread-safe atomic variable\natomicCount++;",
    "example": {
        "code": "#include <iostream>\n#include <thread>\n#include <mutex>\n#include <atomic>\nusing namespace std;\n\nint unsafeCounter = 0;\nmutex mtx;\nint safeCounter = 0;\natomic<int> atomicCounter(0);\n\nvoid runUnsafe() { for (int i = 0; i < 50000; i++) unsafeCounter++; }\nvoid runSafe() {\n    for (int i = 0; i < 50000; i++) {\n        lock_guard<mutex> lock(mtx);\n        safeCounter++;\n    }\n}\nvoid runAtomic() { for (int i = 0; i < 50000; i++) atomicCounter++; }\n\nint main() {\n    thread t1(runSafe); thread t2(runSafe);\n    t1.join(); t2.join();\n\n    thread t3(runAtomic); thread t4(runAtomic);\n    t3.join(); t4.join();\n\n    cout << \"Safe Counter (Mutex): \" << safeCounter << endl;\n    cout << \"Atomic Counter (std::atomic): \" << atomicCounter << endl;\n    return 0;\n}",
        "output": "Safe Counter (Mutex): 100000\nAtomic Counter (std::atomic): 100000",
        "explanation": "Demonstrates eliminating race conditions using std::mutex synchronization and std::atomic atomic operations."
    },
    "fill_blanks": {
        "question": "Fill in the missing Race Condition concepts:",
        "answers": ["race", "unsynchronized", "atomic", "mutex"],
        "options": ["race", "unsynchronized", "atomic", "mutex", "sequential", "virtual"]
    },
    "compiler": {
        "title": "Race Condition Prevention Practice",
        "starter_code": "#include <iostream>\n#include <atomic>\n#include <thread>\nusing namespace std;\n\natomic<int> counter(0);\n\nvoid add() { counter++; }\n\nint main() {\n    thread t1(add);\n    thread t2(add);\n    t1.join(); t2.join();\n    cout << counter << endl;\n    return 0;\n}",
        "question": "Arrange lines to create a thread-safe atomic counter modified by two threads.",
        "options": [
            "#include <atomic>",
            "atomic<int> counter(0);",
            "void add() { counter++; }",
            "thread t1(add); thread t2(add);"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What conditions must be present for a Race Condition to occur in a C++ application?",
            "options": [
                "Two or more threads access shared data concurrently AND at least one thread modifies/writes the data without synchronization",
                "A single thread calls sleep_for()",
                "A file stream is opened in binary mode",
                "An abstract class is instantiated"
            ],
            "answer": "Two or more threads access shared data concurrently AND at least one thread modifies/writes the data without synchronization"
        },
        {
            "question": "Why do race conditions lead to unpredictable output across different program runs?",
            "options": [
                "Because thread execution order depends on OS CPU scheduling, causing overlapping read-modify-write operations to lose updates",
                "Because compilers generate random numbers",
                "Because RAM memory addresses shift dynamically",
                "Because templates recompile every run"
            ],
            "answer": "Because thread execution order depends on OS CPU scheduling, causing overlapping read-modify-write operations to lose updates"
        },
        {
            "question": "Which header file provides lock-free atomic types like std::atomic<int> to eliminate race conditions?",
            "options": [
                "<atomic>",
                "<mutex>",
                "<future>",
                "<thread>"
            ],
            "answer": "<atomic>"
        },
        {
            "question": "How do atomic operations (std::atomic) prevent race conditions?",
            "options": [
                "They execute read-modify-write instructions as indivisible single hardware operations without lock overhead",
                "They pause all background threads for 1 second",
                "They convert variables into pointers",
                "They allocate data on virtual disk storage"
            ],
            "answer": "They execute read-modify-write instructions as indivisible single hardware operations without lock overhead"
        },
        {
            "question": "What strategy helps avoid race conditions when designing multithreaded systems?",
            "options": [
                "Protecting critical sections with mutexes, using std::atomic, and minimizing shared mutable data across threads",
                "Increasing total CPU clock speed",
                "Using global variables everywhere",
                "Calling detach() on all threads"
            ],
            "answer": "Protecting critical sections with mutexes, using std::atomic, and minimizing shared mutable data across threads"
        }
    ],
    "theory": {
        "definition": "A Race Condition is an unsynchronized concurrent access flaw where program outcome varies based on thread scheduling.",
        "why": "Understanding race conditions is fundamental to writing correct, deterministic multithreaded software.",
        "rules": [
            "Occurs when multiple threads access shared memory and >=1 thread writes.",
            "Prevent using std::mutex lock guards.",
            "Use std::atomic for simple scalar counters and flags."
        ],
        "examples": [
            "atomic<int> counter(0); counter++;",
            "lock_guard<mutex> lock(mtx); shared_data++;"
        ]
    }
}

CPP_TOPICS[68] = {
    "id": 68,
    "title": "Thread Synchronization",
    "category": "Multithreading",
    "difficulty": "Advanced",
    "duration": "40 min",
    "concept": "Thread Synchronization coordinates execution across concurrent threads to ensure safe shared resource access and clear communication. Primitives include std::mutex, std::condition_variable (wait, notify_one, notify_all), and asynchronous thread communication via <future> (std::promise and std::future).",
    "syntax": "#include <condition_variable>\n#include <future>\n\nstd::condition_variable cv;\ncv.wait(ulock, []{ return ready; });\ncv.notify_one();\n\nstd::promise<int> p;\nstd::future<int> f = p.get_future();",
    "example": {
        "code": "#include <iostream>\n#include <thread>\n#include <mutex>\n#include <condition_variable>\n#include <future>\nusing namespace std;\n\ncondition_variable cv;\nmutex mtx;\nbool ready = false;\n\nvoid workerCV() {\n    unique_lock<mutex> ulock(mtx);\n    cv.wait(ulock, [] { return ready; });\n    cout << \"Worker CV activated!\" << endl;\n}\n\nvoid computePromise(promise<int>&& p) {\n    p.set_value(42);\n}\n\nint main() {\n    thread t1(workerCV);\n    {\n        lock_guard<mutex> lock(mtx);\n        ready = true;\n    }\n    cv.notify_one();\n    t1.join();\n\n    promise<int> p;\n    future<int> f = p.get_future();\n    thread t2(computePromise, move(p));\n    cout << \"Future value from thread: \" << f.get() << endl;\n    t2.join();\n    return 0;\n}",
        "output": "Worker CV activated!\nFuture value from thread: 42",
        "explanation": "Demonstrates condition_variable signaling with wait() & notify_one(), and thread value communication using std::promise and std::future."
    },
    "fill_blanks": {
        "question": "Fill in the missing Thread Synchronization components:",
        "answers": ["condition_variable", "notify_one", "promise", "future"],
        "options": ["condition_variable", "notify_one", "promise", "future", "signal", "event"]
    },
    "compiler": {
        "title": "Synchronization Practice",
        "starter_code": "#include <iostream>\n#include <future>\n#include <thread>\nusing namespace std;\n\nvoid compute(promise<int>&& p) { p.set_value(100); }\n\nint main() {\n    promise<int> p;\n    future<int> f = p.get_future();\n    thread t(compute, move(p));\n    cout << f.get() << endl;\n    t.join();\n    return 0;\n}",
        "question": "Arrange lines to pass data from a worker thread to main thread using promise and future.",
        "options": [
            "promise<int> p;",
            "future<int> f = p.get_future();",
            "thread t(compute, move(p));",
            "cout << f.get() << endl;"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What is the role of std::condition_variable in multithreaded synchronization?",
            "options": [
                "Allows threads to block efficiently until another thread notifies that a predicate condition is met",
                "Allocates heap memory for threads",
                "Generates random numbers across threads",
                "Compiles thread code"
            ],
            "answer": "Allows threads to block efficiently until another thread notifies that a predicate condition is met"
        },
        {
            "question": "Which member function of std::condition_variable unblocks a single waiting thread?",
            "options": [
                "notify_one()",
                "notify_all()",
                "signal_single()",
                "wake_up()"
            ],
            "answer": "notify_one()"
        },
        {
            "question": "How do std::promise and std::future coordinate one-time data transfer between threads?",
            "options": [
                "The producing thread sets a value into std::promise; the receiving thread retrieves it from std::future via get()",
                "They share raw pointer addresses",
                "They write data to a temporary disk file",
                "They use global static integers"
            ],
            "answer": "The producing thread sets a value into std::promise; the receiving thread retrieves it from std::future via get()"
        },
        {
            "question": "What happens when future::get() is called before the producing thread sets a value in the promise?",
            "options": [
                "get() blocks the receiving thread until the value becomes available",
                "get() returns 0 immediately",
                "get() throws std::out_of_range",
                "get() cancels the worker thread"
            ],
            "answer": "get() blocks the receiving thread until the value becomes available"
        },
        {
            "question": "Which mutex wrapper type MUST be used when calling cv.wait(ulock, predicate)?",
            "options": [
                "std::unique_lock<std::mutex>",
                "std::lock_guard<std::mutex>",
                "std::atomic<std::mutex>",
                "std::shared_ptr<std::mutex>"
            ],
            "answer": "std::unique_lock<std::mutex>"
        }
    ],
    "theory": {
        "definition": "Thread Synchronization coordinates thread execution timing to prevent race conditions, deadlocks, and enable data transfer.",
        "why": "Ensures deterministic execution and safe data exchange between concurrent threads.",
        "rules": [
            "Use mutexes/lock guards to protect critical sections.",
            "Use condition_variable with unique_lock for conditional thread signaling.",
            "Use promise/future from <future> for one-time thread communication."
        ],
        "examples": [
            "cv.wait(ulock, []{ return ready; });",
            "promise.set_value(val); future.get();"
        ]
    }
}


CPP_TOPICS[69] = {
    "id": 69,
    "title": "Preprocessor",
    "category": "Advanced Concepts",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "The C++ Preprocessor modifies source code before compilation begins. Directives begin with # (no ending semicolon). Features include #include (<header> vs \"header\"), #define macros and constants, #undef macro deletion, conditional compilation (#if, #elif, #else, #endif, #ifdef, #ifndef), compilation errors/warnings (#error, #warning), and compiler pragmas (#pragma once, #pragma message).",
    "syntax": "#define PI 3.14159\n#define SQUARE(x) ((x) * (x))\n#pragma once\n#ifndef DEBUG\n#warning \"Debug mode disabled\"\n#endif",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\n#define PI 3.14159\n#define findSquare(x) ((x) * (x))\n\n#ifdef PI\n#pragma message(\"PI macro is defined!\")\n#endif\n\nint main() {\n    double r = 5.0;\n    double area = PI * findSquare(r);\n    cout << \"Area of circle: \" << area << endl;\n\n    #undef PI\n    #define PI 3.14\n    cout << \"Redefined PI: \" << PI << endl;\n    return 0;\n}",
        "output": "Area of circle: 78.5397\nRedefined PI: 3.14",
        "explanation": "Demonstrates #define constants and macro functions, #ifdef checks, #pragma message compilation notes, and undefining/redefining macros with #undef."
    },
    "fill_blanks": {
        "question": "Fill in the missing Preprocessor directives:",
        "answers": ["define", "undef", "ifdef", "pragma"],
        "options": ["define", "undef", "ifdef", "pragma", "import", "include"]
    },
    "compiler": {
        "title": "Preprocessor Practice",
        "starter_code": "#include <iostream>\nusing namespace std;\n\n#define MAX_VAL 100\n\nint main() {\n    cout << \"Max: \" << MAX_VAL << endl;\n    return 0;\n}",
        "question": "Arrange lines to define a preprocessor macro constant MAX_VAL and output it.",
        "options": [
            "#define MAX_VAL 100",
            "int main() {",
            "    cout << \"Max: \" << MAX_VAL << endl;",
            "    return 0;",
            "}"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What is the difference between #include <header> and #include \"header\" in C++?",
            "options": [
                "#include <header> searches system library paths; #include \"header\" searches current project directory first",
                "#include \"header\" compiles header files faster",
                "#include <header> works only for C files",
                "There is no difference"
            ],
            "answer": "#include <header> searches system library paths; #include \"header\" searches current project directory first"
        },
        {
            "question": "Which directive cancels a previously defined macro?",
            "options": [
                "#undef",
                "#delete",
                "#remove",
                "#clear"
            ],
            "answer": "#undef"
        },
        {
            "question": "What is the purpose of #pragma once in C++ header files?",
            "options": [
                "Serves as an efficient include guard preventing multiple inclusions of the header file",
                "Compiles code only once per system restart",
                "Optimizes loops for single execution",
                "Restricts function parameters to 1"
            ],
            "answer": "Serves as an efficient include guard preventing multiple inclusions of the header file"
        },
        {
            "question": "Which directive causes compilation to halt immediately with a custom user error message?",
            "options": [
                "#error",
                "#warning",
                "#stop",
                "#exit"
            ],
            "answer": "#error"
        },
        {
            "question": "Why do preprocessor directives NOT end with a semicolon (;)?",
            "options": [
                "They are processed before lexical parsing by the compiler preprocessor phase",
                "Semicolons cause heap memory corruption",
                "Directives are written in C language syntax",
                "Preprocessor directives require colons instead"
            ],
            "answer": "They are processed before lexical parsing by the compiler preprocessor phase"
        }
    ],
    "theory": {
        "definition": "The Preprocessor processes source code prior to compilation, handling macro expansions, header inclusions, and conditional directives.",
        "why": "Enables code reuse, platform-specific conditional compilation, and header inclusion guards.",
        "rules": [
            "Directives begin with # and lack semicolons.",
            "Include system headers with <> and local headers with \"\".",
            "Use include guards (#pragma once or #ifndef) to avoid double inclusion errors."
        ],
        "examples": [
            "#define SIZE 100",
            "#pragma once"
        ]
    }
}

CPP_TOPICS[70] = {
    "id": 70,
    "title": "Namespaces",
    "category": "Advanced Concepts",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "A namespace in C++ (namespace Name { ... }) groups identifiers (variables, functions, classes) to prevent naming collisions in modular code. Accessed via scope resolution ::, using directives (using namespace std;), or specific using declarations (using std::cout). Supports Nested, Anonymous (internal linkage), Inline (versioning), Global (::var), and Namespace Aliases.",
    "syntax": "namespace Geometry {\n    double area(double r) { return 3.14 * r * r; }\n}\nnamespace Geo = Geometry; // Alias",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint globalVal = 100;\n\nnamespace Room1 {\n    void greet() { cout << \"Hello from Room 1!\" << endl; }\n}\n\nnamespace outer {\n    namespace inner {\n        void display() { cout << \"Inside nested outer::inner!\" << endl; }\n    }\n}\n\nnamespace { // Anonymous namespace\n    int secretVal = 42;\n}\n\nint main() {\n    Room1::greet();\n    outer::inner::display();\n\n    int globalVal = 5;\n    cout << \"Local globalVal: \" << globalVal << \", Global ::globalVal: \" << ::globalVal << endl;\n    cout << \"Anonymous secretVal: \" << secretVal << endl;\n    return 0;\n}",
        "output": "Hello from Room 1!\nInside nested outer::inner!\nLocal globalVal: 5, Global ::globalVal: 100\nAnonymous secretVal: 42",
        "explanation": "Illustrates namespace definition, nested scope resolution outer::inner::display(), global namespace operator ::globalVal, and anonymous namespaces."
    },
    "fill_blanks": {
        "question": "Fill in the missing Namespace keywords:",
        "answers": ["namespace", "using", "inline", "alias"],
        "options": ["namespace", "using", "inline", "alias", "package", "module"]
    },
    "compiler": {
        "title": "Namespace Practice",
        "starter_code": "#include <iostream>\n\nnamespace App {\n    void run() { std::cout << \"App running...\" << std::endl; }\n}\n\nint main() {\n    App::run();\n    return 0;\n}",
        "question": "Arrange lines to create a custom namespace App and invoke its member function using scope resolution.",
        "options": [
            "namespace App {",
            "    void run() { std::cout << \"App running...\" << std::endl; }",
            "}",
            "int main() { App::run(); return 0; }"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What is the primary purpose of namespaces in C++?",
            "options": [
                "To organize code identifiers (functions, variables, classes) and prevent naming collisions across libraries",
                "To allocate heap memory for global variables",
                "To speed up loop iterations",
                "To enable multithreaded locks"
            ],
            "answer": "To organize code identifiers (functions, variables, classes) and prevent naming collisions across libraries"
        },
        {
            "question": "What does an Anonymous (unnamed) Namespace achieve in C++?",
            "options": [
                "Restricts identifier accessibility strictly to the current source file (translation unit), providing internal linkage",
                "Allows global access across all project files",
                "Deletes variables when main() completes",
                "Disables type checking"
            ],
            "answer": "Restricts identifier accessibility strictly to the current source file (translation unit), providing internal linkage"
        },
        {
            "question": "How is a global variable accessed when a local variable in the same scope shares the exact same identifier name?",
            "options": [
                "By prefixing the variable with the global scope resolution operator ::var",
                "By using using namespace global;",
                "By prefixing with std::var",
                "It cannot be accessed"
            ],
            "answer": "By prefixing the variable with the global scope resolution operator ::var"
        },
        {
            "question": "What is the benefit of a using declaration (using std::cout;) over a using directive (using namespace std;)?",
            "options": [
                "It imports only specific necessary identifiers into scope, reducing risks of namespace pollution and ambiguity",
                "It makes the binary smaller",
                "It automatically includes header files",
                "It converts cout to a pointer"
            ],
            "answer": "It imports only specific necessary identifiers into scope, reducing risks of namespace pollution and ambiguity"
        },
        {
            "question": "What is the behavior of an Inline Namespace in C++?",
            "options": [
                "Members of nested inline namespaces are automatically accessible as if declared in the parent enclosing namespace",
                "It physically inlines all function code into call sites",
                "It makes functions private",
                "It prevents namespace extending"
            ],
            "answer": "Members of nested inline namespaces are automatically accessible as if declared in the parent enclosing namespace"
        }
    ],
    "theory": {
        "definition": "Namespaces provide declarative scopes for organizing code and avoiding naming conflicts.",
        "why": "Crucial for modular software development and library integration.",
        "rules": [
            "Access members using Scope Resolution Operator (::).",
            "Anonymous namespaces grant internal linkage.",
            "Inline namespaces expose nested declarations to enclosing scopes."
        ],
        "examples": [
            "namespace Math { int sq(int x) { return x*x; } }",
            "namespace M = Math;"
        ]
    }
}

CPP_TOPICS[71] = {
    "id": 71,
    "title": "Smart Pointers",
    "category": "Advanced Concepts",
    "difficulty": "Advanced",
    "duration": "40 min",
    "concept": "Smart pointers (<memory>) are RAII-based class templates managing dynamic heap memory automatically. Eliminates memory leaks, dangling pointers, and wild pointers. Types: std::unique_ptr (exclusive single owner, move-only, make_unique), std::shared_ptr (shared ownership with reference counting .use_count(), make_shared), and std::weak_ptr (non-owning observer breaking cyclic references).",
    "syntax": "#include <memory>\n\nstd::unique_ptr<int> u = std::make_unique<int>(10);\nstd::shared_ptr<int> s1 = std::make_shared<int>(20);\nstd::shared_ptr<int> s2 = s1; // count = 2\nstd::weak_ptr<int> w = s1;   // observer",
    "example": {
        "code": "#include <iostream>\n#include <memory>\nusing namespace std;\n\nclass Rectangle {\n    int w, h;\npublic:\n    Rectangle(int width, int height) : w(width), h(height) {}\n    int area() const { return w * h; }\n};\n\nint main() {\n    // 1. unique_ptr\n    unique_ptr<Rectangle> u1 = make_unique<Rectangle>(10, 5);\n    cout << \"Unique_ptr Area: \" << u1->area() << endl;\n    unique_ptr<Rectangle> u2 = move(u1); // Ownership transferred\n\n    // 2. shared_ptr & weak_ptr\n    shared_ptr<Rectangle> s1 = make_shared<Rectangle>(4, 5);\n    shared_ptr<Rectangle> s2 = s1;\n    weak_ptr<Rectangle> w1 = s1;\n\n    cout << \"Shared_ptr Area: \" << s2->area() << endl;\n    cout << \"Shared Use Count: \" << s1.use_count() << endl;\n    cout << \"Weak Use Count: \" << w1.use_count() << endl;\n    return 0;\n}",
        "output": "Unique_ptr Area: 50\nShared_ptr Area: 20\nShared Use Count: 2\nWeak Use Count: 2",
        "explanation": "Demonstrates unique_ptr exclusive ownership & std::move(), shared_ptr reference counting via .use_count(), and non-owning weak_ptr observers."
    },
    "fill_blanks": {
        "question": "Fill in the missing Smart Pointer types:",
        "answers": ["unique_ptr", "shared_ptr", "weak_ptr", "make_unique"],
        "options": ["unique_ptr", "shared_ptr", "weak_ptr", "make_unique", "auto_ptr", "raw_ptr"]
    },
    "compiler": {
        "title": "Smart Pointers Practice",
        "starter_code": "#include <iostream>\n#include <memory>\nusing namespace std;\n\nint main() {\n    unique_ptr<int> p = make_unique<int>(42);\n    cout << *p << endl;\n    return 0;\n}",
        "question": "Arrange lines to create a unique_ptr using make_unique and print dereferenced value.",
        "options": [
            "#include <memory>",
            "unique_ptr<int> p = make_unique<int>(42);",
            "cout << *p << endl;",
            "return 0;"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What is the primary ownership behavior of std::unique_ptr?",
            "options": [
                "Exclusive single ownership; cannot be copied, only moved via std::move()",
                "Shared ownership using reference counting",
                "Non-owning observer reference",
                "Global static ownership"
            ],
            "answer": "Exclusive single ownership; cannot be copied, only moved via std::move()"
        },
        {
            "question": "How does std::shared_ptr determine when to deallocate the managed heap object?",
            "options": [
                "It maintains a reference counter; when the reference count drops to 0, memory is freed automatically",
                "When main() completes",
                "When delete is explicitly invoked by the developer",
                "Using an OS timer interrupt"
            ],
            "answer": "It maintains a reference counter; when the reference count drops to 0, memory is freed automatically"
        },
        {
            "question": "Why is std::weak_ptr used alongside std::shared_ptr?",
            "options": [
                "To observe shared objects without incrementing reference counts, resolving cyclic reference memory leaks",
                "To speed up pointer arithmetic",
                "To allow copying unique_ptr objects",
                "To manage raw stack arrays"
            ],
            "answer": "To observe shared objects without incrementing reference counts, resolving cyclic reference memory leaks"
        },
        {
            "question": "Why was std::auto_ptr deprecated in C++11 and removed in C++17?",
            "options": [
                "Its copy syntax secretly transferred ownership, causing dangerous null pointer dereferences",
                "It consumed double memory space",
                "It could not store integers",
                "It was replaced by raw pointers"
            ],
            "answer": "Its copy syntax secretly transferred ownership, causing dangerous null pointer dereferences"
        },
        {
            "question": "Which factory function is recommended for exception-safe creation of std::shared_ptr objects?",
            "options": [
                "std::make_shared<T>()",
                "new shared_ptr<T>()",
                "create_shared<T>()",
                "allocate_ptr<T>()"
            ],
            "answer": "std::make_shared<T>()"
        }
    ],
    "theory": {
        "definition": "Smart Pointers (<memory>) are RAII object wrappers managing dynamic memory lifetimes to prevent memory leaks and dangling pointers.",
        "why": "Eliminates manual delete management and ensures automatic memory deallocation.",
        "rules": [
            "Use unique_ptr for single ownership (transfer via move).",
            "Use shared_ptr for shared ownership.",
            "Use weak_ptr to break circular dependencies."
        ],
        "examples": [
            "auto u = make_unique<int>(10);",
            "auto s = make_shared<int>(20);"
        ]
    }
}

CPP_TOPICS[72] = {
    "id": 72,
    "title": "Callbacks",
    "category": "Advanced Concepts",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "Passing functions as parameters (callbacks) permits dynamic runtime behavior modification. Achieved via raw Function Pointers (return_type (*ptr)(args)), std::function<R(Args)> from <functional>, Lambda Expressions ([](args){}), and Member Functions bound via std::bind(&Class::func, &obj, _1, _2).",
    "syntax": "#include <functional>\n\nvoid process(int val, std::function<int(int)> callback) {\n    cout << callback(val);\n}",
    "example": {
        "code": "#include <iostream>\n#include <functional>\nusing namespace std;\n\nint square(int x) { return x * x; }\nint add(int a, int b) { return a + b; }\n\nclass Multiplier {\npublic:\n    int multiply(int a, int b) { return a * b; }\n};\n\nvoid execute(int a, int b, function<int(int, int)> op) {\n    cout << \"Result: \" << op(a, b) << endl;\n}\n\nint main() {\n    // 1. Function Pointer & std::function\n    execute(10, 20, add);\n\n    // 2. Lambda Callback\n    execute(10, 20, [](int x, int y) { return x - y; });\n\n    // 3. Member Function via std::bind\n    Multiplier m;\n    auto boundFunc = bind(&Multiplier::multiply, &m, placeholders::_1, placeholders::_2);\n    execute(10, 20, boundFunc);\n    return 0;\n}",
        "output": "Result: 30\nResult: -10\nResult: 200",
        "explanation": "Demonstrates callbacks using function pointers, inline lambdas, and class member functions wrapped with std::bind and std::function."
    },
    "fill_blanks": {
        "question": "Fill in the missing Callback wrapper concepts:",
        "answers": ["function", "bind", "lambda", "pointer"],
        "options": ["function", "bind", "lambda", "pointer", "virtual", "delegate"]
    },
    "compiler": {
        "title": "Callbacks Practice",
        "starter_code": "#include <iostream>\n#include <functional>\nusing namespace std;\n\nvoid compute(int x, function<void(int)> cb) {\n    cb(x * 2);\n}\n\nint main() {\n    compute(5, [](int res) { cout << \"Result: \" << res << endl; });\n    return 0;\n}",
        "question": "Arrange lines to define a function accepting a std::function callback parameter.",
        "options": [
            "#include <functional>",
            "void compute(int x, function<void(int)> cb) {",
            "    cb(x * 2);",
            "}"
        ]
    },
    "skill_exa_test": [
        {
            "question": "What is the role of std::function from <functional> in modern C++?",
            "options": [
                "Polymorphic type-safe wrapper storing any callable target (functions, lambdas, functors, bound member functions)",
                "Compiles C++ code to byte array",
                "Measures execution time of functions",
                "Deletes memory allocated by new"
            ],
            "answer": "Polymorphic type-safe wrapper storing any callable target (functions, lambdas, functors, bound member functions)"
        },
        {
            "question": "How is a raw function pointer parameter declared for a function taking two ints and returning an int?",
            "options": [
                "int (*func_ptr)(int, int)",
                "int func_ptr(int, int)*",
                "void* func_ptr(int, int)",
                "pointer<int(int, int)> func_ptr"
            ],
            "answer": "int (*func_ptr)(int, int)"
        },
        {
            "question": "Why are Lambda Expressions widely used as callbacks in C++ algorithms like std::sort?",
            "options": [
                "They provide inline anonymous callables, keeping callback logic readable and localized",
                "They run on background threads automatically",
                "They bypass compiler optimizations",
                "They do not consume stack space"
            ],
            "answer": "They provide inline anonymous callables, keeping callback logic readable and localized"
        },
        {
            "question": "What utility function binds a class member function with an object instance for callback passing?",
            "options": [
                "std::bind()",
                "std::connect()",
                "std::attach()",
                "std::pair()"
            ],
            "answer": "std::bind()"
        },
        {
            "question": "What advantage does std::function offer over raw function pointers?",
            "options": [
                "Can store callables with captured state (e.g. stateful lambdas and functors)",
                "Runs faster than assembly code",
                "Eliminates header include requirements",
                "Does not use stack memory"
            ],
            "answer": "Can store callables with captured state (e.g. stateful lambdas and functors)"
        }
    ],
    "theory": {
        "definition": "Callbacks pass function callables as parameters to customize program execution dynamically at runtime.",
        "why": "Enables flexible event handling, custom sorting comparators, and decoupled software architectures.",
        "rules": [
            "Use std::function<R(Args)> for general callable parameters.",
            "Use inline lambdas for short one-time callbacks.",
            "Use std::bind to pass class member functions with object references."
        ],
        "examples": [
            "void run(function<void()> cb) { cb(); }",
            "run([](){ cout << \"callback\"; });"
        ]
    }
}

CPP_TOPICS[73] = {
    "id": 73,
    "title": "Signal Handling",
    "category": "Advanced Concepts",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "Signal handling (<csignal>) catches operating system event notifications sent to a process (e.g. SIGINT user interrupt, SIGABRT abort, SIGFPE math error, SIGSEGV invalid memory access). Custom handlers are registered via signal(SIG_TYPE, handler). Signals can be raised programmatically using raise(SIG_TYPE) or POSIX kill(pid, SIG_TYPE).",
    "syntax": "#include <csignal>\n\nvoid handleSignal(int sig) {\n    cout << \"Caught signal: \" << sig << endl;\n    exit(sig);\n}\nsignal(SIGINT, handleSignal);\nraise(SIGINT);",
    "example": {
        "code": "#include <iostream>\n#include <csignal>\nusing namespace std;\n\nvoid customSignalHandler(int signalNum) {\n    cout << \"Signal Handler Executed for Signal #\" << signalNum << endl;\n}\n\nint main() {\n    // Register custom handler for SIGINT (Ctrl + C)\n    signal(SIGINT, customSignalHandler);\n\n    cout << \"Raising SIGINT programmatically...\" << endl;\n    raise(SIGINT);\n\n    cout << \"Program execution resumed safely after signal handling!\" << endl;\n    return 0;\n}",
        "output": "Raising SIGINT programmatically...\nSignal Handler Executed for Signal #2\nProgram execution resumed safely after signal handling!",
        "explanation": "Registers customSignalHandler for SIGINT (Signal #2), raises SIGINT via raise(), executes handler, and resumes program execution."
    },
    "fill_blanks": {
        "question": "Fill in the missing Signal Handling functions and types:",
        "answers": ["csignal", "signal", "raise", "SIGINT"],
        "options": ["csignal", "signal", "raise", "SIGINT", "throw", "interrupt"]
    },
    "compiler": {
        "title": "Signal Handling Practice",
        "starter_code": "#include <iostream>\n#include <csignal>\nusing namespace std;\n\nvoid handler(int sig) { cout << \"Signal: \" << sig << endl; }\n\nint main() {\n    signal(SIGINT, handler);\n    raise(SIGINT);\n    return 0;\n}",
        "question": "Arrange lines to register a signal handler for SIGINT and trigger it with raise().",
        "options": [
            "#include <csignal>",
            "signal(SIGINT, handler);",
            "raise(SIGINT);"
        ]
    },
    "skill_exa_test": [
        {
            "question": "Which C++ standard header provides signal handling functions and macros?",
            "options": [
                "<csignal>",
                "<signal.h>",
                "<sys/signal>",
                "<os_signal>"
            ],
            "answer": "<csignal>"
        },
        {
            "question": "Which signal is generated when a user presses Ctrl + C in the terminal?",
            "options": [
                "SIGINT",
                "SIGABRT",
                "SIGSEGV",
                "SIGKILL"
            ],
            "answer": "SIGINT"
        },
        {
            "question": "Which signals CANNOT be caught, blocked, or ignored by a C++ signal handler?",
            "options": [
                "SIGKILL and SIGSTOP",
                "SIGINT and SIGTERM",
                "SIGFPE and SIGSEGV",
                "SIGABRT and SIGUSR1"
            ],
            "answer": "SIGKILL and SIGSTOP"
        },
        {
            "question": "Which function raises a signal programmatically for the current process?",
            "options": [
                "raise(signal_type)",
                "send_signal(signal_type)",
                "throw_signal(signal_type)",
                "dispatch(signal_type)"
            ],
            "answer": "raise(signal_type)"
        },
        {
            "question": "What rule should be followed when writing code inside a C++ signal handler?",
            "options": [
                "Keep handlers short and perform ONLY async-signal-safe operations (avoid complex I/O or heap allocation)",
                "Allocate large dynamic vectors",
                "Use std::sort on global arrays",
                "Launch multiple std::thread objects"
            ],
            "answer": "Keep handlers short and perform ONLY async-signal-safe operations (avoid complex I/O or heap allocation)"
        }
    ],
    "theory": {
        "definition": "Signal Handling intercepts operating system notifications (signals) sent to a process when hardware/software events occur.",
        "why": "Enables graceful shutdown, resource cleanup, and crash diagnosis.",
        "rules": [
            "Register handlers with signal(SIG_NAME, handler).",
            "Use raise(SIG) or kill(pid, SIG) to send signals.",
            "Only execute async-signal-safe code inside signal handlers.",
            "SIGKILL and SIGSTOP cannot be handled."
        ],
        "examples": [
            "signal(SIGINT, handler);",
            "raise(SIGINT);"
        ]
    }
}


