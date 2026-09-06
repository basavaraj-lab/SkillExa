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
    {"id": 7, "title": "Operators", "difficulty": "Beginner", "duration": "30 min", "category": "Basics"},
    {"id": 8, "title": "Conditional Statements", "difficulty": "Beginner", "duration": "30 min", "category": "Basics"},
    {"id": 9, "title": "Loops", "difficulty": "Intermediate", "duration": "35 min", "category": "Basics"},

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
    "concept": "C++ is a powerful, general-purpose programming language created by Bjarne Stroustrup as an extension of C, supporting OOP, generic templates, and direct memory control.",
    "syntax": "#include <iostream>\n\nint main() {\n    std::cout << \"Hello, C++!\";\n    return 0;\n}",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Welcome to SkillExa C++ Track!\" << endl;\n    return 0;\n}",
        "output": "Welcome to SkillExa C++ Track!",
        "explanation": "#include <iostream> includes standard input-output stream library.",
    },
    "fill_blanks": {
        "question": "#include <_____\nusing namespace std;\n\nint main() {{\n    _____ << \"Hello C++!\";\n    return 0;\n}}",
        "answers": ["iostream>", "cout"],
        "options": ["iostream>", "cout", "stdio.h>", "cin"],
    },
    "compiler": {
        "title": "Hello C++ World",
        "question": "Complete the program to output greeting in C++.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    _____ << \"Welcome to SkillExa C++ Track!\\n\";\n    return 0;\n}",
        "options": ["cout", "cin", "printf", "print"],
    },
    "skill_exa_test": [
        {
            "question": "Who created the C++ programming language?",
            "options": ["Bjarne Stroustrup", "Dennis Ritchie", "Guido van Rossum", "James Gosling"],
            "answer": "Bjarne Stroustrup",
        }
    ],
}

CPP_TOPICS[2] = {
    "id": 2,
    "title": "Basic Input / Output",
    "category": "Basics",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "C++ uses stream objects std::cout (output stream) and std::cin (input stream) with insertion (<<) and extraction (>>) operators.",
    "syntax": "std::cin >> variable;\nstd::cout << variable << std::endl;",
    "example": {
        "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int age = 21;\n    cout << \"Age: \" << age << endl;\n    return 0;\n}",
        "output": "Age: 21",
        "explanation": "endl flushes the stream and prints a newline.",
    },
    "fill_blanks": {
        "question": "int x;\ncin _____ x;\ncout _____ x;",
        "answers": [">>", "<<"],
        "options": [">>", "<<", "->", "::"],
    },
    "compiler": {
        "title": "C++ Stream Practice",
        "question": "Fill in the insertion operator for std::cout.",
        "starter_code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout _____ \"C++ Stream Output\\n\";\n    return 0;\n}",
        "options": ["<<", ">>", "::", "->"],
    },
    "skill_exa_test": [
        {
            "question": "Which operator is used with std::cout for output insertion?",
            "options": ["<<", ">>", "::", "->"],
            "answer": "<<",
        }
    ],
}
