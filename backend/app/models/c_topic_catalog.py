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
    {"id": 8, "title": "Arithmetic & Relational Operators", "difficulty": "Beginner", "duration": "25 min", "category": "Introduction"},
    {"id": 9, "title": "Logical & Bitwise Operators", "difficulty": "Intermediate", "duration": "25 min", "category": "Introduction"},
    {"id": 10, "title": "Assignment & Special Operators", "difficulty": "Intermediate", "duration": "25 min", "category": "Introduction"},

    # 2. Control Flow
    {"id": 11, "title": "Conditional Statements (if, if-else, Nested if, Ladder)", "difficulty": "Beginner", "duration": "30 min", "category": "Control Flow"},
    {"id": 12, "title": "Switch Statement & Conditional Operator", "difficulty": "Intermediate", "duration": "25 min", "category": "Control Flow"},
    {"id": 13, "title": "Loops", "difficulty": "Intermediate", "duration": "35 min", "category": "Control Flow"},

    # 3. Functions
    {"id": 14, "title": "Functions", "difficulty": "Intermediate", "duration": "30 min", "category": "Functions"},
    {"id": 15, "title": "Parameter Passing Techniques", "difficulty": "Intermediate", "duration": "30 min", "category": "Functions"},
    {"id": 16, "title": "Main Function", "difficulty": "Intermediate", "duration": "20 min", "category": "Functions"},
    {"id": 17, "title": "Recursion", "difficulty": "Intermediate", "duration": "35 min", "category": "Functions"},
    {"id": 18, "title": "Inline Function", "difficulty": "Intermediate", "duration": "25 min", "category": "Functions"},
    {"id": 19, "title": "Nested Functions", "difficulty": "Intermediate", "duration": "25 min", "category": "Functions"},

    # 4. Arrays and Strings
    {"id": 20, "title": "Arrays", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays and Strings"},
    {"id": 21, "title": "Multidimensional Arrays", "difficulty": "Intermediate", "duration": "35 min", "category": "Arrays and Strings"},
    {"id": 22, "title": "Strings", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays and Strings"},
    {"id": 23, "title": "String Functions", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays and Strings"},

    # 5. Pointers
    {"id": 24, "title": "Pointers", "difficulty": "Intermediate", "duration": "40 min", "category": "Pointers"},
    {"id": 25, "title": "Pointer Arithmetic", "difficulty": "Advanced", "duration": "35 min", "category": "Pointers"},
    {"id": 26, "title": "Pointer to Pointer", "difficulty": "Advanced", "duration": "35 min", "category": "Pointers"},
    {"id": 27, "title": "Function Pointers", "difficulty": "Advanced", "duration": "40 min", "category": "Pointers"},

    # 6. User-Defined Data Types
    {"id": 28, "title": "Structures", "difficulty": "Intermediate", "duration": "35 min", "category": "User-Defined Data Types"},
    {"id": 29, "title": "Unions", "difficulty": "Intermediate", "duration": "30 min", "category": "User-Defined Data Types"},
    {"id": 30, "title": "Enumeration (enum)", "difficulty": "Intermediate", "duration": "25 min", "category": "User-Defined Data Types"},

    # 7. File Handling
    {"id": 31, "title": "Basics of File Handling", "difficulty": "Intermediate", "duration": "35 min", "category": "File Handling"},
    {"id": 32, "title": "Reading a File", "difficulty": "Intermediate", "duration": "30 min", "category": "File Handling"},
    {"id": 33, "title": "Reading/Writing Structures From/To a File", "difficulty": "Advanced", "duration": "40 min", "category": "File Handling"},
    {"id": 34, "title": "EOF, getc() and feof()", "difficulty": "Advanced", "duration": "30 min", "category": "File Handling"},
    {"id": 35, "title": "Deleting a File", "difficulty": "Intermediate", "duration": "25 min", "category": "File Handling"},

    # 8. Error Handling
    {"id": 36, "title": "Error Handling", "difficulty": "Intermediate", "duration": "30 min", "category": "Error Handling"},
    {"id": 37, "title": "Exception Handling Using goto", "difficulty": "Advanced", "duration": "30 min", "category": "Error Handling"},
    {"id": 38, "title": "File Error Handling", "difficulty": "Advanced", "duration": "30 min", "category": "Error Handling"},
    {"id": 39, "title": "Divide-by-Zero Exception", "difficulty": "Intermediate", "duration": "25 min", "category": "Error Handling"},

    # 9. Miscellaneous Concepts
    {"id": 40, "title": "Preprocessors", "difficulty": "Intermediate", "duration": "30 min", "category": "Miscellaneous Concepts"},
    {"id": 41, "title": "Macros", "difficulty": "Intermediate", "duration": "30 min", "category": "Miscellaneous Concepts"},
    {"id": 42, "title": "Header Files", "difficulty": "Intermediate", "duration": "25 min", "category": "Miscellaneous Concepts"},
    {"id": 43, "title": "Date and Time", "difficulty": "Intermediate", "duration": "30 min", "category": "Miscellaneous Concepts"},
    {"id": 44, "title": "Linkage", "difficulty": "Advanced", "duration": "35 min", "category": "Miscellaneous Concepts"},
    {"id": 45, "title": "Storage Classes", "difficulty": "Advanced", "duration": "35 min", "category": "Miscellaneous Concepts"},

    # 10. Advanced Concepts
    {"id": 46, "title": "Variadic Functions", "difficulty": "Advanced", "duration": "40 min", "category": "Advanced Concepts"},
    {"id": 47, "title": "Input-Output System Calls", "difficulty": "Advanced", "duration": "45 min", "category": "Advanced Concepts"},
    {"id": 48, "title": "Signals", "difficulty": "Advanced", "duration": "40 min", "category": "Advanced Concepts"},
    {"id": 49, "title": "Socket Programming", "difficulty": "Advanced", "duration": "50 min", "category": "Advanced Concepts"},
    {"id": 50, "title": "_Generic Keyword", "difficulty": "Advanced", "duration": "35 min", "category": "Advanced Concepts"},
    {"id": 51, "title": "Multithreading", "difficulty": "Advanced", "duration": "50 min", "category": "Advanced Concepts"},
]

C_TOPIC_CORE = {
    1: {
        "concept": "C is a procedural, general-purpose programming language developed by Dennis Ritchie at Bell Labs in 1972. It offers fast execution speed, low-level memory access, and structured control flow, serving as the foundational building block for operating systems, compilers, database engines, embedded systems, and modern software development.",
        "syntax": "#include <stdio.h>\n\nint main(void) {\n    // Print message to screen\n    printf(\"Hello World\");\n    return 0;\n}",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    // This prints \"Hello World\"\n    printf(\"Hello World\\n\");\n    return 0;\n}",
            "output": "Hello World",
            "explanation": "#include <stdio.h> includes the standard input/output library for printf(). int main(void) serves as the entry point of execution, returning 0 to signal successful program termination.",
        },
        "fill_blanks": {
            "question": "#include <_____.h>\n\nint main(void) {\n    _____\(\"Hello World\\n\");\n    return 0;\n}",
            "answers": ["stdio", "printf"],
            "options": ["stdio", "printf", "stdlib", "scanf", "math"],
        },
        "compiler": {
            "title": "First C Program Sandbox",
            "question": "Complete the C program using printf to display 'Hello World'.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    _____\(\"Hello World\\n\");\n    return 0;\n}",
            "options": ["printf", "scanf", "puts", "print"],
        },
        "skill_exa_test": [
            {
                "question": "Who developed the C programming language at Bell Labs in 1972?",
                "options": ["Dennis Ritchie", "Bjarne Stroustrup", "James Gosling", "Guido van Rossum"],
                "answer": "Dennis Ritchie",
            },
            {
                "question": "Which standard header file is required for printf() and scanf() functions in C?",
                "options": ["<stdio.h>", "<stdlib.h>", "<string.h>", "<math.h>"],
                "answer": "<stdio.h>",
            },
            {
                "question": "What does a return value of 0 in main() indicate to the operating system?",
                "options": [
                    "Successful execution of the program",
                    "Compilation warning",
                    "Stack overflow exception",
                    "Memory leak error"
                ],
                "answer": "Successful execution of the program",
            },
            {
                "question": "Which step in execution converts C source code into an executable file?",
                "options": [
                    "Compilation via GCC/Clang",
                    "Direct interpretation in browser",
                    "Just-in-Time JIT bytecode transformation",
                    "HTML DOM rendering"
                ],
                "answer": "Compilation via GCC/Clang",
            },
            {
                "question": "Which of the following is a primary application area of C programming?",
                "options": [
                    "Operating Systems & Kernel Development (e.g., Linux)",
                    "CSS Layout Animations",
                    "Web Browser CSS Flexbox",
                    "Static HTML Page Parsing"
                ],
                "answer": "Operating Systems & Kernel Development (e.g., Linux)",
            },
        ],
        "theory": {
            "definition": "C is a procedural, compiled, high-performance general-purpose programming language developed by Dennis Ritchie at Bell Labs in 1972.",
            "why": "C provides raw hardware-level memory access, high execution speed, and direct compilation into native machine instructions, making it essential for operating systems, microcontrollers, database engines, and compilers.",
            "rules": [
                "Every executable C program must contain an entry point function named main().",
                "Header files (such as <stdio.h>) must be included at the top of the file to use standard library functions.",
                "Single-line comments begin with // and multi-line comments are wrapped in /* ... */.",
                "C code is compiled into native machine code binary before execution.",
                "Statement execution terminates with a return statement (return 0; signals clean exit)."
            ],
            "examples": [
                "#include <stdio.h>\n\nint main(void) {\n    printf(\"Hello World\\n\");\n    return 0;\n}"
            ],
        },
    },
    2: {
        "concept": "The C compilation process transforms human-readable source code (.c) into machine-executable binary across 4 distinct phases: Preprocessing (.i), Compilation (.s), Assembly (.o), and Linking (executable). Understanding these phases helps developers debug build errors, inspect macros, and optimize performance.",
        "syntax": "gcc -Wall -save-temps filename.c -o filename",
        "example": {
            "code": "#include <stdio.h>\n#define PLATFORM \"Linux GCC\"\n\nint main(void) {\n    // Preprocessor replaces PLATFORM before compilation\n    printf(\"Compiled output for %s\\n\", PLATFORM);\n    return 0;\n}",
            "output": "Compiled output for Linux GCC",
            "explanation": "Preprocessing strips comments and expands #define PLATFORM into \"Linux GCC\". The compiler generates assembly (.s), the assembler produces machine object code (.o), and the linker connects printf() dynamically to produce the final executable binary.",
        },
        "fill_blanks": {
            "question": "gcc -Wall -save-temps filename.c -_____ filename\n// Phases: Preprocessing (.i) -> Compiling (.s) -> Assembling (.o) -> _____",
            "answers": ["o", "Linking"],
            "options": ["o", "Linking", "Parsing", "Executing", "c"],
        },
        "compiler": {
            "title": "C Compilation Sandbox",
            "question": "Fill in the output flag -o to specify the executable name during GCC compilation.",
            "starter_code": "#include <stdio.h>\n#define APP_NAME \"SkillExa C Engine\"\n\nint main(void) {\n    printf(\"Target: %s\\n\", APP_NAME);\n    return 0;\n}",
            "options": ["-o", "-Wall", "-c", "-E"],
        },
        "skill_exa_test": [
            {
                "question": "Which phase of C compilation expands #define macros, strips comments, and includes header files?",
                "options": ["Preprocessing (.i)", "Compilation (.s)", "Assembly (.o)", "Linking"],
                "answer": "Preprocessing (.i)",
            },
            {
                "question": "What type of code is stored inside the intermediate .s file during GCC compilation?",
                "options": [
                    "Assembly-level CPU instructions",
                    "High-level Python code",
                    "Unresolved C preprocessor directives",
                    "Final executable machine binary"
                ],
                "answer": "Assembly-level CPU instructions",
            },
            {
                "question": "What is the default executable file name created by GCC if the -o flag is omitted?",
                "options": ["a.out", "main.exe", "output.bin", "program.o"],
                "answer": "a.out",
            },
            {
                "question": "Which phase connects unresolved library functions like printf() and appends environment startup code?",
                "options": ["Linking", "Preprocessing", "Lexical Analysis", "Assembly"],
                "answer": "Linking",
            },
            {
                "question": "What is the key difference between Static Linking and Dynamic Linking in C?",
                "options": [
                    "Static copies library code into executable; Dynamic references shared libraries at runtime",
                    "Static compiles faster; Dynamic produces larger executable files",
                    "Dynamic linking strips comments; Static preserves comments",
                    "Static linking runs only in browser environment"
                ],
                "answer": "Static copies library code into executable; Dynamic references shared libraries at runtime",
            },
        ],
        "theory": {
            "definition": "Compilation is the multi-stage process of converting high-level C source code into low-level machine binary instructions executable by the CPU.",
            "why": "Knowledge of the 4 compilation phases (Preprocessing, Compiling, Assembling, Linking) helps developers troubleshoot macro expansion bugs, missing symbol linker errors, and binary optimization.",
            "rules": [
                "1. Preprocessing: Expands #include headers, resolves #define macros, and removes comments (.i file).",
                "2. Compilation: Translates preprocessed code into CPU assembly instructions (.s file).",
                "3. Assembly: Converts assembly code into machine-level object file (.o file).",
                "4. Linking: Connects object files with C standard library definitions to produce executable binary.",
                "Use gcc -Wall to display all compiler warnings for robust code hygiene."
            ],
            "examples": [
                "gcc -Wall -save-temps main.c -o main\n./main"
            ],
        },
    },
    3: {
        "concept": "Identifiers in C are user-defined names given to variables, functions, arrays, structures, unions, and labels. They uniquely identify program elements. Naming rules mandate starting with a letter or underscore, strict case-sensitivity, and avoiding reserved C keywords.",
        "syntax": "int studentAge = 20;\nvoid calculateSum(int a, int b) { ... }",
        "example": {
            "code": "#include <stdio.h>\n\nint sumValues(int num1, int num2) {\n    return num1 + num2;\n}\n\nint main(void) {\n    int totalSum = sumValues(10, 20);\n    printf(\"Total: %d\\n\", totalSum);\n    return 0;\n}",
            "output": "Total: 30",
            "explanation": "sumValues, num1, num2, totalSum, and main are identifiers. They follow camelCase naming conventions and start with letters.",
        },
        "fill_blanks": {
            "question": "int _____ = 100;\n// Attempting identifier starting with digit: int _____ = 50; (Invalid)",
            "answers": ["totalScore", "1score"],
            "options": ["totalScore", "1score", "int", "return", "_score"],
        },
        "compiler": {
            "title": "C Identifiers Sandbox",
            "question": "Complete the C program with a valid variable identifier totalScore.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int _____ = 95;\n    printf(\"Score: %d\\n\", totalScore);\n    return 0;\n}",
            "options": ["totalScore", "95score", "return", "int"],
        },
        "skill_exa_test": [
            {
                "question": "Which of the following is a valid C identifier name?",
                "options": ["_studentScore", "99score", "float", "total-sum"],
                "answer": "_studentScore",
            },
            {
                "question": "What occurs if a reserved keyword like 'const' or 'return' is used as a variable identifier?",
                "options": [
                    "Compilation error: expected identifier",
                    "Warning message, but program runs fine",
                    "Keyword is automatically renamed",
                    "Program compiles into a DLL"
                ],
                "answer": "Compilation error: expected identifier",
            },
            {
                "question": "Which rule correctly describes starting characters for C identifiers?",
                "options": [
                    "Must start with a letter (A-Z, a-z) or an underscore (_)",
                    "Can start with any digit 0-9",
                    "Must start with a dollar sign $",
                    "Can start with hyphen - or dot ."
                ],
                "answer": "Must start with a letter (A-Z, a-z) or an underscore (_)",
            },
            {
                "question": "Are identifiers case-sensitive in C (e.g. value vs Value)?",
                "options": [
                    "Yes, C is strictly case-sensitive",
                    "No, C ignores character casing",
                    "Only inside main() function",
                    "Only when using static storage"
                ],
                "answer": "Yes, C is strictly case-sensitive",
            },
            {
                "question": "Which naming convention is standard for structure names in C?",
                "options": ["PascalCase", "camelCase", "UPPER_SNAKE_CASE", "kebab-case"],
                "answer": "PascalCase",
            },
        ],
        "theory": {
            "definition": "An identifier in C is a symbolic user-defined name assigned to variables, functions, arrays, structures, or labels.",
            "why": "Identifiers uniquely reference memory addresses and executable routines in program source code, improving readability and code organization.",
            "rules": [
                "1. Can contain uppercase/lowercase letters (A-Z, a-z), digits (0-9), and underscores (_).",
                "2. First character MUST be a letter or an underscore (_); digits are strictly prohibited at start.",
                "3. Identifiers are case-sensitive (e.g. item_count and Item_Count are separate variables).",
                "4. Reserved C keywords (e.g. int, double, return, if) cannot be used as identifiers.",
                "5. Common conventions: camelCase for variables/functions, UPPER_SNAKE_CASE for constants, PascalCase for structures."
            ],
            "examples": [
                "int studentAge = 20; // Valid variable identifier\nvoid computeTotal() {} // Valid function identifier"
            ],
        },
    },
    4: {
        "concept": "C keywords are reserved words that have predefined structural meanings recognized by the compiler parser. They form the core language constructs (e.g., int, return, if, struct) and cannot be used as user identifiers. Standard ANSI C (C89) defines 32 core keywords.",
        "syntax": "const int MAX_LIMIT = 100;\nif (x == 10) { ... } else { ... }",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    const int limit = 100;\n    int val = 10;\n    \n    if (val < limit) {\n        printf(\"Value %d is within limit %d\\n\", val, limit);\n    }\n    return 0;\n}",
            "output": "Value 10 is within limit 100",
            "explanation": "const, int, if, and return are reserved C keywords. const makes limit read-only.",
        },
        "fill_blanks": {
            "question": "_____ int MAX_SIZE = 500;\n// Attempting int return = 10; fails because _____ is reserved.",
            "answers": ["const", "return"],
            "options": ["const", "return", "var", "let", "define"],
        },
        "compiler": {
            "title": "C Keywords Practice Sandbox",
            "question": "Fill in the const keyword to declare a read-only integer variable.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    _____ int MAX_USERS = 100;\n    printf(\"Max users allowed: %d\\n\", MAX_USERS);\n    return 0;\n}",
            "options": ["const", "final", "static", "auto"],
        },
        "skill_exa_test": [
            {
                "question": "How many standard reserved keywords exist in ANSI C (C89/C90)?",
                "options": ["32", "48", "64", "28"],
                "answer": "32",
            },
            {
                "question": "Why does writing 'int return = 10;' cause a compilation error in C?",
                "options": [
                    "return is a reserved C keyword and cannot be used as an identifier",
                    "10 is not a valid integer value",
                    "return must always be written in uppercase",
                    "Variable names must begin with underscores"
                ],
                "answer": "return is a reserved C keyword and cannot be used as an identifier",
            },
            {
                "question": "Which of the following keywords is used to query the size of a data type in bytes?",
                "options": ["sizeof", "length", "size", "bytesof"],
                "answer": "sizeof",
            },
            {
                "question": "Because C is case-sensitive, how does the compiler treat 'if' vs 'IF'?",
                "options": [
                    "if is a reserved keyword; IF is treated as a normal user identifier",
                    "Both are treated as reserved keywords",
                    "Both cause compilation syntax errors",
                    "IF is a macro alias for if"
                ],
                "answer": "if is a reserved keyword; IF is treated as a normal user identifier",
            },
            {
                "question": "Which keyword makes a variable read-only after initialization?",
                "options": ["const", "static", "volatile", "extern"],
                "answer": "const",
            },
        ],
        "theory": {
            "definition": "Keywords in C are predefined, reserved words that carry fixed structural meaning to the compiler parser.",
            "why": "Keywords form essential control structures, data declarations, type definitions, and memory qualifiers in C programs.",
            "rules": [
                "1. Keywords cannot be redefined or used as identifier names (variables, functions, structs).",
                "2. Keywords must be typed in lowercase letters (e.g. while, return, struct).",
                "3. ANSI C (C89) defines 32 core keywords across data types, control flow, storage classes, and qualifiers.",
                "4. Data Type Keywords: char, int, float, double, void, short, long, signed, unsigned.",
                "5. Control Flow Keywords: if, else, switch, case, default, for, while, do, break, continue, goto, return.",
                "6. Type Qualifiers & Operators: const, volatile, restrict, sizeof."
            ],
            "examples": [
                "const double PI = 3.14159;\nsizeof(int);"
            ],
        },
    },
    5: {
        "concept": "Input and Output (I/O) operations in C allow programs to interact with users via <stdio.h>. Output uses formatted printf() or string-based fputs(). Input uses formatted scanf() (requiring & address-of operator) or safer multi-word line reading via fgets(buffer, size, stdin).",
        "syntax": "printf(\"Age: %d\\n\", age);\nscanf(\"%d\", &age);\nfgets(name, sizeof(name), stdin);",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    int age = 22;\n    char name[30] = \"SkillExa\";\n    \n    printf(\"Name: %s\\n\", name);\n    printf(\"Age: %d\\n\", age);\n    fputs(\"I/O Demonstration Complete\\n\", stdout);\n    return 0;\n}",
            "output": "Name: SkillExa\nAge: 22\nI/O Demonstration Complete",
            "explanation": "%s and %d are format specifiers in printf(). fputs() prints raw string text directly to stdout.",
        },
        "fill_blanks": {
            "question": "int age;\nscanf(\"%_____\", &age);\nfgets(name, sizeof(name), _____);",
            "answers": ["d", "stdin"],
            "options": ["d", "stdin", "stdout", "c", "s"],
        },
        "compiler": {
            "title": "C Input/Output Sandbox",
            "question": "Complete the printf statement using the %d format specifier.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int score = 100;\n    _____\(\"Score: %d\\n\", score);\n    return 0;\n}",
            "options": ["printf", "scanf", "fputs", "puts"],
        },
        "skill_exa_test": [
            {
                "question": "Which operator MUST be passed before a variable in scanf() to store entered input?",
                "options": [
                    "& (Address-of operator)",
                    "* (Dereference operator)",
                    "% (Modulus operator)",
                    "-> (Arrow operator)"
                ],
                "answer": "& (Address-of operator)",
            },
            {
                "question": "Why is fgets() preferred over scanf(\"%s\", str) when reading string input containing spaces?",
                "options": [
                    "fgets() reads spaces and limits buffer size to prevent buffer overflow",
                    "fgets() automatically converts text to uppercase",
                    "scanf() cannot read string characters",
                    "fgets() executes directly in GPU memory"
                ],
                "answer": "fgets() reads spaces and limits buffer size to prevent buffer overflow",
            },
            {
                "question": "Which header file provides standard C input/output functions like printf(), scanf(), and fgets()?",
                "options": ["<stdio.h>", "<stdlib.h>", "<string.h>", "<conio.h>"],
                "answer": "<stdio.h>",
            },
            {
                "question": "Which function outputs a plain string directly to stdout or a file stream without format specifiers?",
                "options": ["fputs()", "scanf()", "getchar()", "malloc()"],
                "answer": "fputs()",
            },
            {
                "question": "What happens when scanf(\"%s\", str) encounters a whitespace space character?",
                "options": [
                    "It stops reading further characters for that string",
                    "It replaces the space with an underscore _",
                    "It causes a segmentation fault",
                    "It converts the space to '\\0' and continues reading"
                ],
                "answer": "It stops reading further characters for that string",
            },
        ],
        "theory": {
            "definition": "Input and Output operations in C handle reading user data into memory and writing processed information onto standard output streams.",
            "why": "I/O forms the bridge between user input devices (keyboard/files) and display output monitors/terminal screens.",
            "rules": [
                "1. Always include <stdio.h> header file for I/O routines.",
                "2. scanf() requires & symbol for non-pointer primitive variables to pass memory address.",
                "3. Format specifiers must match data types: %d for int, %f for float, %lf for double, %c for char, %s for string.",
                "4. Use fgets(buffer, sizeof(buffer), stdin) for multi-word input containing spaces.",
                "5. Unformatted output functions like fputs() write raw string data directly to stdout."
            ],
            "examples": [
                "printf(\"Score: %d\\n\", score);\nscanf(\"%d\", &score);"
            ],
        },
    },
    6: {
        "concept": "A variable in C is a named memory location that holds a typed value. Variables must be declared before use. Initializing variables is critical because uninitialized local variables contain unpredictable garbage values in memory.",
        "syntax": "int age = 20;\nfloat height = 5.7;\nchar grade = 'A';",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    int num = 10;                         // [TRUE: Variable 'num' allocated on Stack & Initialized to 10]\n    printf(\"Initial num: %d\\n\", num);     // [EXECUTED: Outputting Initial State num = 10]\n    \n    num = 25;                             // [TRUE: Reassigned 'num' from 10 -> 25]\n    num = num + 5;                        // [TRUE: Mutated 'num' (25 + 5) -> 30]\n    printf(\"Final num: %d\\n\", num);       // [EXECUTED: Outputting Final State num = 30]\n    return 0;                             // [EXECUTED: Clean Exit 0]\n}",
            "output": "Initial num: 10\nFinal num: 30",
            "explanation": "Step-by-Step Variable State & Execution Flow:\n1. Line 4: 'int num = 10;' -> Allocates integer variable 'num' on stack memory, initialized to 10 (Blue Line).\n2. Line 5: Executing 'printf(...)' -> Outputs 'Initial num: 10' to standard console (Blue Line).\n3. Line 7: Reassignment 'num = 25;' -> Replaces 10 with 25 at memory address &num (Blue Line).\n4. Line 8: Mutation 'num = num + 5;' -> Evaluates expression (25 + 5) = 30 and updates 'num' to 30 (Blue Line).\n5. Line 9: Executing 'printf(...)' -> Outputs 'Final num: 30' to console (Blue Line).\n6. Line 10: Process completes and returns exit code 0.",
        },
        "fill_blanks": {
            "question": "int age = 20;\n// Update variable value\nage = age _____ 5;\nprintf(\"%d\", age);",
            "answers": ["+"],
            "options": ["+", "=", "int", "char", "var"],
        },
        "compiler": {
            "title": "C Variables Sandbox",
            "question": "Declare and initialize integer variable score to 100, then print its value.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    _____ score = 100;\n    printf(\"Score: %d\\n\", score);\n    return 0;\n}",
            "options": ["int", "float", "char", "void"],
        },
        "skill_exa_test": [
            {
                "question": "What does an uninitialized local variable in C contain prior to assignment?",
                "options": [
                    "Unpredictable garbage value",
                    "Guaranteed zero 0",
                    "NULL pointer",
                    "Empty string ''"
                ],
                "answer": "Unpredictable garbage value",
            },
            {
                "question": "Which operator is used to assign or update the value of a variable in C?",
                "options": [
                    "= (Assignment operator)",
                    "== (Equality operator)",
                    "& (Address operator)",
                    "-> (Arrow operator)"
                ],
                "answer": "= (Assignment operator)",
            },
            {
                "question": "Where are local variables typically stored in C memory layout?",
                "options": ["Stack Memory", "Heap Memory", "Text Segment", "Data Segment"],
                "answer": "Stack Memory",
            },
            {
                "question": "Which of the following is a valid C variable declaration and initialization?",
                "options": [
                    "float height = 5.7f;",
                    "int 1stScore = 90;",
                    "char grade = \"A\";",
                    "double return = 3.14;"
                ],
                "answer": "float height = 5.7f;",
            },
            {
                "question": "How can you query the exact memory size occupied by a variable in bytes?",
                "options": [
                    "Using sizeof(var) operator",
                    "Using length(var) function",
                    "Using address &var operator",
                    "Using typeof(var) macro"
                ],
                "answer": "Using sizeof(var) operator",
            },
        ],
        "theory": {
            "definition": "A variable is an abstraction for a location in RAM that holds typed binary data.",
            "why": "Variables allow programs to store, retrieve, and dynamically mutate state during runtime execution.",
            "rules": [
                "1. Variables must be declared with a specific data type before referencing them.",
                "2. Always initialize variables before reading them to avoid garbage values.",
                "3. Variable names must follow identifier rules (letters, digits, underscores, no digit start).",
                "4. Variable memory size depends on the data type and CPU architecture.",
                "5. Values can be updated anytime using assignment = or compound operators."
            ],
            "examples": [
                "int count = 0;\ncount += 1;"
            ],
        },
    },
    7: {
        "concept": "Data types in C classify variables into Primitive (int, char, float, double, void), Derived (Arrays, Pointers, Functions), and User-Defined (struct, union, enum). Data type modifiers (short, long, signed, unsigned) alter size and value range.",
        "syntax": "int a = 10;\nchar c = 'A';\nfloat f = 12.45f;\ndouble d = 1.4521;\nsizeof(int);",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    int i = 22;\n    char ch = 'A';\n    float fl = 12.45f;\n    double db = 1.4521;\n    \n    printf(\"int: %d (%lu bytes)\\n\", i, sizeof(i));\n    printf(\"char: %c (%lu bytes)\\n\", ch, sizeof(ch));\n    printf(\"float: %.2f (%lu bytes)\\n\", fl, sizeof(fl));\n    printf(\"double: %.4lf (%lu bytes)\\n\", db, sizeof(db));\n    return 0;\n}",
            "output": "int: 22 (4 bytes)\nchar: A (1 bytes)\nfloat: 12.45 (4 bytes)\ndouble: 1.4521 (8 bytes)",
            "explanation": "Demonstrates primitive data types, their respective format specifiers (%d, %c, %f, %lf), and memory sizes using sizeof().",
        },
        "fill_blanks": {
            "question": "char grade = 'A'; // Format specifier: %_____\ndouble price = 99.99; // Format specifier: %_____",
            "answers": ["c", "lf"],
            "options": ["c", "lf", "d", "f", "s"],
        },
        "compiler": {
            "title": "C Data Types Sandbox",
            "question": "Fill in the char data type to store character letter 'A'.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    _____ symbol = 'A';\n    printf(\"Symbol: %c, Size: %lu byte\\n\", symbol, sizeof(symbol));\n    return 0;\n}",
            "options": ["char", "int", "float", "double"],
        },
        "skill_exa_test": [
            {
                "question": "What is the guaranteed size of a char data type in C across all platforms?",
                "options": ["1 byte", "2 bytes", "4 bytes", "8 bytes"],
                "answer": "1 byte",
            },
            {
                "question": "Which format specifier is used for double precision floating-point numbers in printf()?",
                "options": ["%lf", "%f", "%d", "%c"],
                "answer": "%lf",
            },
            {
                "question": "Which category of data types includes struct, union, and enum in C?",
                "options": [
                    "User-Defined Data Types",
                    "Primitive Data Types",
                    "System Kernels",
                    "Preprocessors"
                ],
                "answer": "User-Defined Data Types",
            },
            {
                "question": "What does the void data type signify when used as a function return type?",
                "options": [
                    "The function returns no value to the caller",
                    "The function returns an integer 0",
                    "The function returns a generic pointer",
                    "The function execution is skipped"
                ],
                "answer": "The function returns no value to the caller",
            },
            {
                "question": "Which data type modifier can be applied to int to allow only positive numbers and zero?",
                "options": ["unsigned", "signed", "short", "static"],
                "answer": "unsigned",
            },
        ],
        "theory": {
            "definition": "Data types specify memory allocation, representation layout, format specifiers, and permissible operations on variables.",
            "why": "Proper data type selection ensures numerical accuracy, prevents arithmetic overflow, and optimizes RAM utilization.",
            "rules": [
                "1. Primitive Data Types: int (%d), char (%c), float (%f), double (%lf), void.",
                "2. Derived Data Types: Arrays, Pointers, Functions.",
                "3. User-Defined Data Types: Structures (struct), Unions (union), Enumerations (enum).",
                "4. Type Modifiers: short, long, signed, unsigned modify size and range.",
                "5. Use sizeof() operator to check platform-specific byte sizes."
            ],
            "examples": [
                "char letter = 'Z';\nsizeof(double);"
            ],
        },
    },
    8: {
        "concept": "Arithmetic operators (+, -, *, /, %, ++, --) perform numeric calculations. Relational operators (==, !=, >, <, >=, <=) compare values and return boolean-like results: 1 for True and 0 for False.",
        "syntax": "int sum = a + b;\nint rem = a % b;\nint isGreater = (a > b);",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    int a = 25, b = 5;\n    printf(\"a + b = %d\\n\", a + b);\n    printf(\"a %% b = %d\\n\", a % b);\n    printf(\"a > b : %d\\n\", a > b);\n    printf(\"a == b: %d\\n\", a == b);\n    return 0;\n}",
            "output": "a + b = 30\na % b = 0\na > b : 1\na == b: 0",
            "explanation": "Calculates addition, remainder via modulus operator %, and evaluates relational comparisons returning 1 (True) or 0 (False).",
        },
        "fill_blanks": {
            "question": "int rem = 25 _____ 5;\nint isGreater = (25 _____ 5);",
            "answers": ["%", ">"],
            "options": ["%", ">", "/", "==", "&&"],
        },
        "compiler": {
            "title": "Arithmetic & Relational Operators Sandbox",
            "question": "Fill in the modulus operator % and relational operator >.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int a = 25, b = 5;\n    printf(\"Remainder: %d\\n\", a _____ b);\n    printf(\"Is Greater: %d\\n\", a _____ b);\n    return 0;\n}",
            "options": ["%", ">", "/", "=="],
        },
        "skill_exa_test": [
            {
                "question": "Which operator returns the remainder of integer division in C?",
                "options": ["%", "/", "*", "&"],
                "answer": "%",
            },
            {
                "question": "What is the return value of a relational expression like (25 > 5) in C?",
                "options": ["1 (True)", "0 (False)", "25", "Compilation Error"],
                "answer": "1 (True)",
            },
            {
                "question": "What is the key difference between prefix ++x and postfix x++?",
                "options": [
                    "Prefix ++x increments before evaluating value; Postfix x++ increments after evaluating value",
                    "Prefix ++x adds 2; Postfix x++ adds 1",
                    "Postfix x++ works only with pointers",
                    "There is no difference between them"
                ],
                "answer": "Prefix ++x increments before evaluating value; Postfix x++ increments after evaluating value",
            },
            {
                "question": "Which relational operator checks for inequality between two expressions?",
                "options": ["!=", "==", "=", "<>"],
                "answer": "!=",
            },
            {
                "question": "Can the modulus operator % be applied directly to float or double operands in C?",
                "options": [
                    "No, % requires integer operands in C",
                    "Yes, % works identically on float and double",
                    "Only when using GCC compiler flags",
                    "Only inside switch statements"
                ],
                "answer": "No, % requires integer operands in C",
            },
        ],
        "theory": {
            "definition": "Arithmetic operators perform mathematical calculations, while relational operators compare values and evaluate truth conditions.",
            "why": "Form the foundational math and conditional comparison building blocks for algorithm logic.",
            "rules": [
                "1. Arithmetic: +, -, *, /, % (modulus works only on integer types).",
                "2. Increment/Decrement: ++a (prefix) vs a++ (postfix).",
                "3. Relational: ==, !=, >, <, >=, <= evaluate to 1 (True) or 0 (False)."
            ],
            "examples": [
                "int rem = 17 % 5;\nint check = (a >= b);"
            ],
        },
    },
    9: {
        "concept": "Logical operators (&& AND, || OR, ! NOT) combine or invert conditions with short-circuit evaluation. Bitwise operators (& AND, | OR, ^ XOR, ~ NOT, << Left Shift, >> Right Shift) manipulate binary bits directly for hardware and high-performance operations.",
        "syntax": "int res = (a > 0) && (b > 0);\nint bitAnd = a & b;\nint shifted = a << 2;",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    int a = 25, b = 5;\n    printf(\"a && b : %d\\n\", a && b);\n    printf(\"!a    : %d\\n\", !a);\n    printf(\"a & b  : %d\\n\", a & b);\n    printf(\"a | b  : %d\\n\", a | b);\n    printf(\"a << 1 : %d\\n\", a << 1);\n    return 0;\n}",
            "output": "a && b : 1\n!a    : 0\na & b  : 1\na | b  : 29\na << 1 : 50",
            "explanation": "Logical AND && checks boolean truth. Bitwise & performs bitwise AND, | performs bitwise OR, and << shifts bits left (multiplying by 2).",
        },
        "fill_blanks": {
            "question": "int cond = (x > 0) _____ (y > 0);\nint leftShift = val _____ 1;",
            "answers": ["&&", "<<"],
            "options": ["&&", "<<", "||", ">>", "&"],
        },
        "compiler": {
            "title": "Logical & Bitwise Operators Sandbox",
            "question": "Fill in the logical AND operator && and bitwise left shift << operator.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int x = 25, y = 5;\n    printf(\"Logical AND: %d\\n\", (x > 0) _____ (y > 0));\n    printf(\"Left Shift: %d\\n\", x _____ 1);\n    return 0;\n}",
            "options": ["&&", "<<", "||", "&"],
        },
        "skill_exa_test": [
            {
                "question": "Which logical operator evaluates to True (1) only when BOTH operands are non-zero/True?",
                "options": ["&& (Logical AND)", "|| (Logical OR)", "! (Logical NOT)", "^ (XOR)"],
                "answer": "&& (Logical AND)",
            },
            {
                "question": "What does shifting an integer x to the left by 1 bit (x << 1) effectively do mathematically?",
                "options": [
                    "Multiplies x by 2",
                    "Divides x by 2",
                    "Adds 1 to x",
                    "Subtracts 1 from x"
                ],
                "answer": "Multiplies x by 2",
            },
            {
                "question": "Which bitwise operator flips all 0 bits to 1 and all 1 bits to 0?",
                "options": [
                    "~ (Bitwise NOT / One's Complement)",
                    "& (Bitwise AND)",
                    "| (Bitwise OR)",
                    "^ (Bitwise XOR)"
                ],
                "answer": "~ (Bitwise NOT / One's Complement)",
            },
            {
                "question": "What is short-circuit evaluation in logical expressions?",
                "options": [
                    "Skipping second operand evaluation if the result is determined by the first",
                    "Executing bitwise operations in hardware registers",
                    "Truncating floating point decimals",
                    "Catching division by zero exceptions"
                ],
                "answer": "Skipping second operand evaluation if the result is determined by the first",
            },
            {
                "question": "Which bitwise operator evaluates to 1 when corresponding bits differ and 0 when they match?",
                "options": ["^ (Bitwise XOR)", "& (Bitwise AND)", "| (Bitwise OR)", "~ (Bitwise NOT)"],
                "answer": "^ (Bitwise XOR)",
            },
        ],
        "theory": {
            "definition": "Logical operators perform boolean decision logic, whereas bitwise operators operate directly on binary bits of integer data.",
            "why": "Essential for flag manipulation, bit masking, boolean logic circuits, and low-level system programming.",
            "rules": [
                "1. Logical: && (AND), || (OR), ! (NOT). Supports short-circuiting.",
                "2. Bitwise: & (AND), | (OR), ^ (XOR), ~ (NOT), << (Left Shift), >> (Right Shift).",
                "3. x << n multiplies x by 2^n; x >> n divides x by 2^n."
            ],
            "examples": [
                "int mask = flag & 0x0F;\nint shifted = val << 2;"
            ],
        },
    },
    10: {
        "concept": "Assignment operators (=, +=, -=, *=, /=, %=, &=, |=, ^=, <<=, >>=) assign or modify variable values. Special operators include sizeof (byte query), comma , (sequential execution), ternary ?: (conditional choice), dot . & arrow -> (struct access), cast (type conversion), and pointer address & / dereference *.",
        "syntax": "a += 5;\nint max = (a > b) ? a : b;\nint *ptr = &num;\nfloat f = (float)integerVal;",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    int num = 10;\n    int *ptr = &num;\n    \n    num += 15; // num = num + 15\n    printf(\"num after += 15: %d\\n\", num);\n    printf(\"Dereferenced *ptr: %d\\n\", *ptr);\n    printf(\"Ternary max: %d\\n\", (num > 20) ? 100 : 200);\n    printf(\"Float cast: %.2f\\n\", (float)num);\n    return 0;\n}",
            "output": "num after += 15: 25\nDereferenced *ptr: 25\nTernary max: 100\nFloat cast: 25.00",
            "explanation": "+= modifies num in place. & gets address, * dereferences pointer, ?: performs conditional choice, and (float) performs explicit type casting.",
        },
        "fill_blanks": {
            "question": "num _____ 5; // num = num + 5\nint max = (x > y) _____ x : y;",
            "answers": ["+=", "?"],
            "options": ["+=", "?", "=", ":", "->"],
        },
        "compiler": {
            "title": "Assignment & Special Operators Sandbox",
            "question": "Fill in the compound assignment operator += and ternary conditional operator ?.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int val = 10;\n    val _____ 5;\n    int result = (val > 10) _____ 100 : 0;\n    printf(\"Val: %d, Result: %d\\n\", val, result);\n    return 0;\n}",
            "options": ["+=", "?", "=", ":"],
        },
        "skill_exa_test": [
            {
                "question": "What is the compound assignment expression 'x += 10;' equivalent to?",
                "options": ["x = x + 10;", "x = 10;", "x + 10;", "x == 10;"],
                "answer": "x = x + 10;",
            },
            {
                "question": "Which operator is used to access structure members through a structure pointer?",
                "options": [
                    "-> (Arrow operator)",
                    ". (Dot operator)",
                    "* (Dereference operator)",
                    "& (Address operator)"
                ],
                "answer": "-> (Arrow operator)",
            },
            {
                "question": "Which is the only ternary operator in C?",
                "options": [
                    "?: (Conditional operator)",
                    "&& (Logical AND)",
                    "sizeof operator",
                    "-> (Arrow operator)"
                ],
                "answer": "?: (Conditional operator)",
            },
            {
                "question": "Which operator returns the memory address of a variable?",
                "options": [
                    "& (Address-of operator)",
                    "* (Dereference operator)",
                    "sizeof operator",
                    "% (Modulus operator)"
                ],
                "answer": "& (Address-of operator)",
            },
            {
                "question": "What does the expression '(float)5' perform in C?",
                "options": [
                    "Explicit type casting of 5 to a float",
                    "Declaration of float variable named 5",
                    "Division of 5 by float max",
                    "Memory allocation of 5 floats"
                ],
                "answer": "Explicit type casting of 5 to a float",
            },
        ],
        "theory": {
            "definition": "Assignment operators update variable storage, while special operators handle memory addresses, type casting, member access, and conditional evaluation.",
            "why": "Provides concise code syntax, memory manipulation capabilities, and type conversion tools.",
            "rules": [
                "1. Compound Assignment: +=, -=, *=, /=, %=, &=, |=, ^=, <<=, >>=.",
                "2. Ternary Operator ?: (expr1 ? expr2 : expr3).",
                "3. Member Access: . (dot for objects), -> (arrow for pointers).",
                "4. Pointers & Memory: & (address-of), * (dereference).",
                "5. Cast Operator: (type)operand."
            ],
            "examples": [
                "a += 10;\nint *p = &a;\nfloat f = (float)a;"
            ],
        },
    },
    11: {
        "concept": "Conditional statements in C allow programs to make decisions and branch execution flow based on condition evaluations. Constructs include simple if, if-else, nested if-else (for hierarchical checks), and if-else-if ladders (for testing multiple sequential conditions).",
        "syntax": "if (condition1) {\n    // Code if condition1 is true\n} else if (condition2) {\n    // Code if condition2 is true\n} else {\n    // Code if all conditions are false\n}",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    int age = 20;\n    \n    if (age >= 18) {                       // [TRUE: 20 >= 18 Evaluates to 1]\n        if (age >= 60) {                   // [FALSE: 20 >= 60 Evaluates to 0]\n            printf(\"Senior Citizen\\n\");    // [SKIPPED]\n        } else {\n            printf(\"Eligible for vote\\n\");  // [EXECUTED: Inner Else Branch]\n        }\n    } else {                                // [SKIPPED]\n        printf(\"Not eligible\\n\");          // [SKIPPED: Outer Else Branch]\n    }\n    return 0;\n}",
            "output": "Eligible for vote",
            "explanation": "1. Outer Condition: (20 >= 18) evaluates to TRUE (1) -> Blue Highlighted Line.\n2. Inner Condition: (20 >= 60) evaluates to FALSE (0) -> Red Highlighted Line.\n3. Inner Else Branch: Executes printf('Eligible for vote') -> Blue Executed Line.",
        },
        "fill_blanks": {
            "question": "int age = 20;\n_____ (age >= 18) {\n    printf(\"Eligible\");\n} _____ {\n    printf(\"Not Eligible\");\n}",
            "answers": ["if", "else"],
            "options": ["if", "else", "else if", "switch", "while"],
        },
        "compiler": {
            "title": "C Conditional Statements Sandbox",
            "question": "Complete the if-else conditional statement for voting eligibility.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int age = 20;\n    _____ (age >= 18) {\n        printf(\"Eligible to vote\\n\");\n    } _____ {\n        printf(\"Not eligible\\n\");\n    }\n    return 0;\n}",
            "options": ["if", "else", "else if", "switch"],
        },
        "skill_exa_test": [
            {
                "question": "What happens when an if condition evaluates to false in a simple if statement without an else block?",
                "options": [
                    "The if body block is skipped and program execution continues after it",
                    "A runtime exception is thrown",
                    "The program terminates immediately with error code 1",
                    "The compiler generates a syntax error"
                ],
                "answer": "The if body block is skipped and program execution continues after it",
            },
            {
                "question": "In an if-else-if ladder statement, when is the final else block executed?",
                "options": [
                    "Only when all preceding if and else-if conditions evaluate to false",
                    "Before any of the if conditions are evaluated",
                    "Always executed regardless of previous condition results",
                    "Only when a segmentation fault occurs"
                ],
                "answer": "Only when all preceding if and else-if conditions evaluate to false",
            },
            {
                "question": "When are curly braces {} optional around an if statement body in C?",
                "options": [
                    "When the if body contains only a single statement",
                    "Curly braces are always mandatory in C",
                    "When using integer variables only",
                    "Inside main() function only"
                ],
                "answer": "When the if body contains only a single statement",
            },
            {
                "question": "In a nested if-else structure, when is the inner if condition evaluated?",
                "options": [
                    "Only if the enclosing outer condition evaluates to true",
                    "Simultaneously alongside the outer condition",
                    "Before the outer condition is checked",
                    "Only if the enclosing outer condition evaluates to false"
                ],
                "answer": "Only if the enclosing outer condition evaluates to true",
            },
            {
                "question": "In what order are conditions evaluated in an if-else-if ladder?",
                "options": [
                    "Top to bottom, stopping at the first condition that evaluates to true",
                    "Bottom to top in reverse order",
                    "All conditions are evaluated concurrently",
                    "In order of numerical variable magnitude"
                ],
                "answer": "Top to bottom, stopping at the first condition that evaluates to true",
            },
        ],
        "theory": {
            "definition": "Conditional statements test logical expressions and direct runtime program execution along specific branching paths.",
            "why": "Enables dynamic decision-making based on user input, calculations, or system status.",
            "rules": [
                "1. Simple if: Executes body only when condition is non-zero (True).",
                "2. if-else: Selects between two mutually exclusive execution paths.",
                "3. Nested if: Evaluates hierarchical conditions (inner if requires outer if True).",
                "4. if-else-if ladder: Evaluates multiple conditions sequentially from top to bottom."
            ],
            "examples": [
                "if (score >= 90) printf(\"A\"); else if (score >= 80) printf(\"B\"); else printf(\"C\");"
            ],
        },
    },
    12: {
        "concept": "The switch statement selects one execution case from multiple constant integral values (int or char). break statements prevent fall-through into subsequent cases, and default executes when no case matches. The conditional operator (?:) provides a ternary shorthand for simple if-else assignments.",
        "syntax": "switch (var) {\n    case 1: printf(\"One\"); break;\n    case 2: printf(\"Two\"); break;\n    default: printf(\"Other\"); break;\n}\nval = (flag == 0) ? 25 : -25;",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    int var = 18;\n    int flag = 0;\n    \n    switch (var) {\n        case 15:\n            printf(\"You are a kid\\n\");\n            break;\n        case 18:\n            printf(\"Eligible for vote\\n\");\n            break;\n        default:\n            printf(\"Default Case\\n\");\n            break;\n    }\n    \n    int value = (flag == 0) ? 25 : -25;\n    printf(\"Value when flag is 0: %d\\n\", value);\n    return 0;\n}",
            "output": "Eligible for vote\nValue when flag is 0: 25",
            "explanation": "var matches case 18, printing 'Eligible for vote' and breaking. Ternary operator assigns 25 to value because flag == 0 is True.",
        },
        "fill_blanks": {
            "question": "switch (choice) {\n    case 18:\n        printf(\"Vote\");\n        _____;\n    _____:\n        printf(\"Default\");\n}",
            "answers": ["break", "default"],
            "options": ["break", "default", "continue", "return", "case"],
        },
        "compiler": {
            "title": "Switch Statement & Ternary Sandbox",
            "question": "Fill in the break keyword to exit switch case 18 and default keyword for fallback.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int var = 18;\n    switch (var) {\n        case 18:\n            printf(\"Eligible for vote\\n\");\n            _____;\n        _____:\n            printf(\"Default executed\\n\");\n            break;\n    }\n    return 0;\n}",
            "options": ["break", "default", "continue", "case"],
        },
        "skill_exa_test": [
            {
                "question": "What types of expressions are allowed as the control expression inside a C switch statement?",
                "options": [
                    "Only integral types (int or char)",
                    "Floating-point types (float or double)",
                    "Strings and C-arrays",
                    "Any struct or pointer type"
                ],
                "answer": "Only integral types (int or char)",
            },
            {
                "question": "What happens if a break statement is omitted at the end of a matching case in a switch block?",
                "options": [
                    "Execution falls through into the next case statement body",
                    "The program crashes immediately",
                    "The switch statement restarts from the beginning",
                    "A runtime memory overflow exception occurs"
                ],
                "answer": "Execution falls through into the next case statement body",
            },
            {
                "question": "When is the default case block executed inside a switch statement?",
                "options": [
                    "When none of the defined case constant values match the switch expression",
                    "Always before any case statement is evaluated",
                    "Only when an unhandled exception occurs",
                    "At the beginning of every loop iteration"
                ],
                "answer": "When none of the defined case constant values match the switch expression",
            },
            {
                "question": "Which operator acts as a compact ternary alternative to an if-else assignment?",
                "options": [
                    "?: (Conditional / Ternary Operator)",
                    "&& (Logical AND Operator)",
                    "sizeof Operator",
                    "-> (Arrow Operator)"
                ],
                "answer": "?: (Conditional / Ternary Operator)",
            },
            {
                "question": "Can float or double variables be used as case labels in a switch statement?",
                "options": [
                    "No, case labels must be constant integer or character expressions",
                    "Yes, float variables are allowed as case labels",
                    "Only when compiled with GCC -Wall flags",
                    "Only if cast to string"
                ],
                "answer": "No, case labels must be constant integer or character expressions",
            },
        ],
        "theory": {
            "definition": "The switch statement provides multi-way constant value branching, while the conditional operator (?:) offers inline ternary decision assignment.",
            "why": "Optimizes multi-choice menu selections and provides clean ternary conditional expressions.",
            "rules": [
                "1. switch expressions must evaluate to int or char.",
                "2. Each case label must be a constant integral expression.",
                "3. break prevents fall-through to subsequent cases.",
                "4. default handles unmatched values.",
                "5. Conditional operator: condition ? true_expr : false_expr."
            ],
            "examples": [
                "switch(val) { case 1: break; default: break; }\nint x = (a > b) ? a : b;"
            ],
        },
    },
    13: {
        "concept": "Loops (for, while, do-while) repeat code execution while a condition evaluates to true.",
        "syntax": "for (int i = 0; i < n; i++) { ... }",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    for (int i = 1; i <= 3; i++) {         // [TRUE: Loop Iterations i = 1, 2, 3]\n        printf(\"Iteration %d: i = %d\\n\", i, i); // [EXECUTED: Body Executed on Iteration]\n    }\n    // Loop condition (4 <= 3) evaluates to 0  // [FALSE: Loop Exit Condition (4 <= 3)]\n    return 0;\n}",
            "output": "Iteration 1: i = 1\nIteration 2: i = 2\nIteration 3: i = 3",
            "explanation": "Step-by-Step Loop Iteration & Variable State Trace:\n1. Initialization: 'int i = 1' sets loop control variable i to 1 (runs once at start).\n2. Iteration 1: Evaluates condition (1 <= 3) -> TRUE (Blue Line) -> Executes body (prints i=1) -> Increments i to 2.\n3. Iteration 2: Evaluates condition (2 <= 3) -> TRUE (Blue Line) -> Executes body (prints i=2) -> Increments i to 3.\n4. Iteration 3: Evaluates condition (3 <= 3) -> TRUE (Blue Line) -> Executes body (prints i=3) -> Increments i to 4.\n5. Loop Termination: Evaluates condition (4 <= 3) -> FALSE (Red Line) -> Exits for loop and returns 0.",
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
    14: {
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
    15: {
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

    24: {
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

    28: {
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
            "unlock_next": topic_id + 1 if topic_id < len(C_TOPIC_CATALOG) else None,
        },
    }


C_TOPICS = {item["id"]: _build_c_topic(item) for item in C_TOPIC_CATALOG}
