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

    # 11. Memory Management
    {"id": 52, "title": "Memory Layout of C Programs", "difficulty": "Intermediate", "duration": "35 min", "category": "Memory Management"},
    {"id": 53, "title": "Dynamic Memory Allocation", "difficulty": "Intermediate", "duration": "40 min", "category": "Memory Management"},
    {"id": 54, "title": "Memory Leak in C", "difficulty": "Intermediate", "duration": "30 min", "category": "Memory Management"},
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
            "question": "#include <_____.h>\n\nint main(void) {\n    _____(\"Hello World\\n\");\n    return 0;\n}",
            "answers": ["stdio", "printf"],
            "options": ["stdio", "printf", "stdlib", "scanf", "math"],
        },
        "compiler": {
            "title": "First C Program Sandbox",
            "question": "Complete the C program using printf to display 'Hello World'.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    _____(\"Hello World\\n\");\n    return 0;\n}",
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
            "title": "C Compilation & Macro Preprocessing Sandbox",
            "question": "Fill in the macro definition to set APP_NAME before compilation.",
            "starter_code": "#include <stdio.h>\n#define APP_NAME _____\n\nint main(void) {\n    printf(\"Target: %s\\n\", APP_NAME);\n    return 0;\n}",
            "options": ["\"SkillExa C Engine\"", "\"Linux GCC Binary\"", "\"GCC Compiler\"", "\"C Native Executable\""],
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
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int score = 100;\n    _____(\"Score: %d\\n\", score);\n    return 0;\n}",
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
            {
                "question": "What is the primary difference between entry-controlled loops (for, while) and exit-controlled loops (do-while)?",
                "options": [
                    "Entry-controlled loops evaluate condition before executing body; exit-controlled loops evaluate after executing body at least once",
                    "Entry-controlled loops run infinitely by default; exit-controlled loops run once",
                    "Exit-controlled loops cannot use break or continue statements",
                    "Entry-controlled loops do not allow variable initialization in C"
                ],
                "answer": "Entry-controlled loops evaluate condition before executing body; exit-controlled loops evaluate after executing body at least once",
            },
            {
                "question": "Which statement immediately terminates a loop and transfers control to the statement following the loop?",
                "options": ["break", "continue", "return", "goto"],
                "answer": "break",
            },
            {
                "question": "What does the continue statement do when executed inside a loop body in C?",
                "options": [
                    "Skips the remainder of the current iteration body and jumps to loop condition evaluation / increment step",
                    "Terminates the loop entirely and exits the function",
                    "Restarts the loop from the initial counter value",
                    "Pauses execution of the loop for 1 second"
                ],
                "answer": "Skips the remainder of the current iteration body and jumps to loop condition evaluation / increment step",
            },
            {
                "question": "In a standard C for (expr1; expr2; expr3) loop header, which expression is executed only once before loop execution begins?",
                "options": [
                    "expr1 (Initialization)",
                    "expr2 (Condition)",
                    "expr3 (Increment/Decrement)",
                    "None of the above"
                ],
                "answer": "expr1 (Initialization)",
            },
        ],
    },

    # Topics 11 through 48
    14: {
        "concept": "A function is a named block of code that performs a specific task. A function can take inputs (called parameters), execute a block of statements, and optionally return a result. Functions allow you to write logic once and reuse it wherever needed, keeping your code clean, modular, organized, and easy to debug.",
        "syntax": "// Function Declaration (Prototype)\nreturn_type function_name(parameter_list);\n\n// Function Definition\nreturn_type function_name(parameter_type parameter_name) {\n    // Function body\n    return result;\n}",
        "example": {
            "code": "#include <stdio.h>\n\n// Function definition\nint square(int x) {\n    return x * x;\n}\n\nint main(void) {\n    // Calling the function\n    int result = square(5);\n    printf(\"Square of 5 is: %d\\n\", result);\n    return 0;\n}",
            "output": "Square of 5 is: 25",
            "explanation": "The square() function takes an integer input x (5), computes 5 * 5, and returns 25. main() receives this value, stores it in result, and prints it.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\n// Function definition\nint add(int a, int b) {\n    _____ a + b;\n}\n\nint main(void) {\n    // Function call\n    int result = _____(5, 3);\n    printf(\"The sum is: %d\\n\", result);\n    return 0;\n}",
            "answers": ["return", "add"],
            "options": ["return", "add", "void", "printf", "square"],
        },
        "compiler": {
            "title": "C Functions Sandbox",
            "question": "Complete the C function definition and function call to calculate the sum of 5 and 3.",
            "starter_code": "#include <stdio.h>\n\n// Function definition\nint add(int a, int b) {\n    _____ a + b;\n}\n\nint main(void) {\n    int result = _____(5, 3);\n    printf(\"The sum is: %d\\n\", result);\n    return 0;\n}",
            "options": ["return", "add", "square", "output", "void"],
        },
        "skill_exa_test": [
            {
                "question": "What is the primary difference between a function declaration and a function definition in C?",
                "options": [
                    "Declaration specifies return type and prototype without a body; definition includes the full implementation code.",
                    "Declaration allocates memory for local variables; definition specifies the return type.",
                    "Declaration is written inside main(); definition is written in header files.",
                    "Declaration creates stack frames; definition runs the C preprocessor."
                ],
                "answer": "Declaration specifies return type and prototype without a body; definition includes the full implementation code.",
            },
            {
                "question": "What happens in memory when a C function is executed?",
                "options": [
                    "A stack frame is allocated automatically for parameters/local variables and freed upon function return.",
                    "Memory is allocated in heap storage permanently until free() is called.",
                    "Local variables are stored in CPU cache registers permanently.",
                    "The program creates a new thread process for every function call."
                ],
                "answer": "A stack frame is allocated automatically for parameters/local variables and freed upon function return.",
            },
            {
                "question": "Which type of C function takes inputs but does not return any value back to the caller?",
                "options": [
                    "Arguments, no return value (void return type with parameters)",
                    "No arguments, no return value",
                    "No arguments, return value",
                    "Arguments and return value"
                ],
                "answer": "Arguments, no return value (void return type with parameters)",
            },
            {
                "question": "Which of the following built-in C library functions requires including <math.h>?",
                "options": ["sqrt()", "printf()", "scanf()", "puts()"],
                "answer": "sqrt()",
            },
            {
                "question": "Which keyword specifies that a function does not return any value in C?",
                "options": ["void", "null", "none", "empty"],
                "answer": "void",
            },
        ],
        "theory": {
            "definition": "A function in C is a self-contained, named block of statements designed to perform a specific task, take inputs (parameters), and return a calculated result.",
            "why": "Functions eliminate code duplication, enforce modular code design, simplify debugging, and enable reusability across programs.",
            "rules": [
                "Return Type: Specifies the data type returned by the function (use void if no value is returned).",
                "Function Prototype: Functions must be declared before use if defined after main().",
                "Parameters: Input values passed into function parentheses during a call.",
                "Call Stack: Local variables and parameters exist only within the function's stack frame life cycle."
            ],
            "examples": [
                "int add(int a, int b) {\n    return a + b;\n}",
                "void greet(void) {\n    printf(\"Hello from C Function!\\n\");\n}"
            ],
        },
    },
    15: {
        "concept": "In C, parameter passing provides data to functions upon invocation via two primary techniques: Pass by Value (passing a copy of the argument) and Pass by Pointers (passing the memory address using pointers). Formal parameters act as placeholders in function definitions, while actual parameters are real values or expressions passed during function calls.",
        "syntax": "// Formal Parameters (placeholders) & Actual Parameters (arguments)\nvoid funcValue(int val);    // Pass by Value\nvoid funcPointer(int *val);  // Pass by Pointer\n\nfuncValue(x);               // Pass copy of x\nfuncPointer(&x);            // Pass address of x",
        "example": {
            "code": "#include <stdio.h>\n\n// Function that takes parameters by value\nvoid funcValue(int val) {\n    // Changing local copy\n    val = 123;\n}\n\n// Function that takes parameters by pointer\nvoid funcPointer(int* val) {\n    // Changing value at memory address\n    *val = 123;\n}\n\nint main(void) {\n    int x1 = 1;\n    funcValue(x1);\n    printf(\"Pass by Value: %d\\n\", x1);\n\n    int x2 = 1;\n    funcPointer(&x2);\n    printf(\"Pass by Pointer: %d\\n\", x2);\n    return 0;\n}",
            "output": "Pass by Value: 1\nPass by Pointer: 123",
            "explanation": "funcValue(x1) passes a copy of x1, so x1 remains 1 in main(). funcPointer(&x2) receives the memory address of x2; dereferencing *val = 123 directly modifies x2 in main() to 123.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nvoid funcPointer(int *val) {\n    _____ = 123; // Dereference pointer to modify original variable\n}\n\nint main(void) {\n    int x = 1;\n    funcPointer(_____); // Pass address of x\n    printf(\"%d\", x);\n    return 0;\n}",
            "answers": ["*val", "&x"],
            "options": ["*val", "&x", "val", "x", "*x", "&val"],
        },
        "compiler": {
            "title": "Parameter Passing: Pass by Value vs Pass by Pointer",
            "question": "Complete the C code using pointer dereferencing and address-of operator so that x is modified to 123.",
            "starter_code": "#include <stdio.h>\n\nvoid func(int *val) {\n    _____ = 123;\n}\n\nint main(void) {\n    int x = 1;\n    func(_____);\n    printf(\"%d\\n\", x);\n    return 0;\n}",
            "options": ["*val", "&x", "val", "x"],
        },
        "skill_exa_test": [
            {
                "question": "What are variables declared in a function definition called versus the real values passed during a function call?",
                "options": [
                    "Formal Parameters (placeholders) and Actual Parameters (arguments)",
                    "Actual Parameters (placeholders) and Formal Parameters (arguments)",
                    "Local Variables and Global Variables",
                    "Pointer Parameters and Value Parameters"
                ],
                "answer": "Formal Parameters (placeholders) and Actual Parameters (arguments)",
            },
            {
                "question": "Given the C code: `void func(int val) { val = 123; } int main() { int x = 1; func(x); printf(\"%d\", x); return 0; }`, what is the output?",
                "options": ["1", "123", "0", "Garbage value"],
                "answer": "1",
            },
            {
                "question": "Given the C code: `void func(int* val) { *val = 123; } int main() { int x = 1; func(&x); printf(\"%d\", x); return 0; }`, what is the output?",
                "options": ["123", "1", "Address of x", "Compilation Error"],
                "answer": "123",
            },
            {
                "question": "Why is Pass by Value inefficient when passing large C structures or arrays to functions?",
                "options": [
                    "Making copies of large structures in memory is computationally costly",
                    "The C compiler rejects passing structures by value",
                    "Pass by value causes stack overflow for primitive variables",
                    "Pass by value prevents functions from using return statements"
                ],
                "answer": "Making copies of large structures in memory is computationally costly",
            },
            {
                "question": "Does the C programming language have native references like C++ (e.g., `int &val` in parameters)?",
                "options": [
                    "No, C does not have references; pointers themselves are passed by value to achieve call-by-reference effect",
                    "Yes, C supports parameter declarations like `int &val`",
                    "Yes, C references are identical to C++ references in syntax and semantics",
                    "No, C functions cannot modify variables defined in main under any circumstances"
                ],
                "answer": "No, C does not have references; pointers themselves are passed by value to achieve call-by-reference effect",
            },
        ],
        "theory": {
            "definition": "Parameter passing in C provides input data to functions when called. Formal parameters are placeholders declared in function definitions, whereas actual parameters (arguments) are the values passed during invocation.",
            "why": "Understanding parameter passing techniques allows developers to control variable mutability, avoid unnecessary memory copying for large data structures, and safely modify caller data across scopes.",
            "rules": [
                "Formal Parameters: Variables declared in the function definition acting as local placeholders.",
                "Actual Parameters: The real values or expressions passed during function calls.",
                "Pass By Value: Passes a copy of the argument. Modifications inside the function alter only the copy, leaving original data unchanged.",
                "Pass By Pointer (Call by Pointer): Passes the memory address (&x). Dereferencing (*val) modifies the original data directly in memory.",
                "Performance: Pass by pointer avoids memory copying overhead for large structures and arrays.",
                "No True References in C: C does not possess native reference parameters (like C++ int &x). Pointers are passed by value to simulate reference behavior."
            ],
            "examples": [
                "#include <stdio.h>\n\n// Pass by Value example\nvoid func(int val) {\n    val = 123;\n}\n\nint main(void) {\n    int x = 1;\n    func(x);\n    printf(\"%d\\n\", x); // Output: 1\n    return 0;\n}",
                "#include <stdio.h>\n\n// Pass by Pointer example\nvoid func(int* val) {\n    *val = 123;\n}\n\nint main(void) {\n    int x = 1;\n    func(&x);\n    printf(\"%d\\n\", x); // Output: 123\n    return 0;\n}"
            ],
        },
    },

    16: {
        "concept": "The main() function serves as the mandatory entry point for execution in C programs. When a C program starts, the operating system kernel transfers execution control to main(). It returns an integer status code (0 for success, non-zero for error) back to the OS environment.",
        "syntax": "int main(void) {\n    // Code statements\n    return 0;\n}\n\n// Command-line arguments signature\nint main(int argc, char *argv[]) {\n    // argc: argument count, argv: argument values\n    return 0;\n}",
        "example": {
            "code": "#include <stdio.h>\n\nint main(int argc, char *argv[]) {\n    printf(\"Program Name: %s\\n\", argv[0]);\n    printf(\"Total Arguments Passed: %d\\n\", argc);\n    return 0;\n}",
            "output": "Program Name: ./program\nTotal Arguments Passed: 1",
            "explanation": "The main() function receives argc (number of arguments) and argv (array of argument strings). argv[0] contains the executable program name.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\n_____ main(int argc, char *_____[]) {\n    printf(\"Arguments count: %d\\n\", argc);\n    _____ 0;\n}",
            "answers": ["int", "argv", "return"],
            "options": ["int", "argv", "return", "void", "char", "main"],
        },
        "compiler": {
            "title": "C Main Function Sandbox",
            "question": "Complete the main function signature and return statement.",
            "starter_code": "#include <stdio.h>\n\n_____ main(void) {\n    printf(\"Execution starts in main()\\n\");\n    _____ 0;\n}",
            "options": ["int", "return", "void", "main", "exit"],
        },
        "skill_exa_test": [
            {
                "question": "What is the return type of the main() function as mandated by standard C specs (C99/C11/C17)?",
                "options": ["int", "void", "float", "char*"],
                "answer": "int",
            },
            {
                "question": "What does returning 0 from the main() function indicate to the operating system?",
                "options": [
                    "Successful execution of the program without errors",
                    "A runtime error occurred",
                    "The program requires command line input",
                    "Memory stack overflow"
                ],
                "answer": "Successful execution of the program without errors",
            },
            {
                "question": "What does argv[0] contain when command-line arguments are passed to int main(int argc, char *argv[])?",
                "options": [
                    "The name or invocation path of the program executable",
                    "The first user-passed command line argument",
                    "The total number of arguments passed",
                    "A NULL pointer"
                ],
                "answer": "The name or invocation path of the program executable",
            },
            {
                "question": "In int main(int argc, char *argv[]), what is the minimum value of argc when executing a C program?",
                "options": [
                    "1 (at least the program executable name itself)",
                    "0",
                    "2",
                    "Undefined"
                ],
                "answer": "1 (at least the program executable name itself)",
            },
            {
                "question": "Which array element in argv is always guaranteed to be a NULL pointer according to C standards?",
                "options": ["argv[argc]", "argv[0]", "argv[1]", "argv[-1]"],
                "answer": "argv[argc]",
            },
        ],
        "theory": {
            "definition": "The main() function is the mandatory entry point for C program execution, where the operating system transfers control to start program execution.",
            "why": "Standardizing main() allows the OS runtime loader to pass startup parameters (argc, argv) and capture process exit codes to determine program success or failure status.",
            "rules": [
                "Return Type: According to C standards, main() should return an int (0 for success, non-zero for error status).",
                "Signatures: Allowed standard signatures are int main(void) and int main(int argc, char *argv[]).",
                "argc: Holds the count of command-line arguments, including the program binary path.",
                "argv: Array of null-terminated C strings containing the argument values. argv[argc] is always NULL."
            ],
            "examples": [
                "int main(void) {\n    return 0;\n}",
                "int main(int argc, char *argv[]) {\n    for (int i = 0; i < argc; i++) {\n        printf(\"argv[%d] = %s\\n\", i, argv[i]);\n    }\n    return 0;\n}"
            ],
        },
    },

    17: {
        "concept": "Recursion is a programming technique where a function calls itself repeatedly until a specific base condition is met. A function performing self-calling behavior is known as a recursive function, and each instance of the function calling itself is called a recursive call.",
        "syntax": "void rec(int n) {\n    // Base Case\n    if (n == 6) return;\n    \n    printf(\"Level %d\\n\", n);\n    rec(n + 1); // Recursive Call\n}",
        "example": {
            "code": "#include <stdio.h>\n\nvoid rec(int n) {\n    // Base Case\n    if (n == 6) return;\n\n    printf(\"Recursion Level %d\\n\", n);\n    rec(n + 1);\n}\n\nint main(void) {\n    rec(1);\n    return 0;\n}",
            "output": "Recursion Level 1\nRecursion Level 2\nRecursion Level 3\nRecursion Level 4\nRecursion Level 5",
            "explanation": "The function rec(n) calls itself with n + 1 until it reaches the base case n == 6, at which point recursion stops and stack frames unwind.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nvoid rec(int n) {\n    if (n == 6) _____; // Base Case\n    printf(\"Recursion Level %d\\n\", n);\n    rec(n _____ 1); // Recursive step\n}",
            "answers": ["return", "+"],
            "options": ["return", "+", "break", "*", "-", "continue"],
        },
        "compiler": {
            "title": "C Recursion Sandbox",
            "question": "Complete the base case condition and recursive call to print levels 1 to 5.",
            "starter_code": "#include <stdio.h>\n\nvoid rec(int n) {\n    if (n == _____) return;\n    printf(\"Recursion Level %d\\n\", n);\n    rec(_____);\n}\n\nint main(void) {\n    rec(1);\n    return 0;\n}",
            "options": ["6", "n + 1", "5", "n - 1", "0"],
        },
        "skill_exa_test": [
            {
                "question": "What is the condition called that stops a recursive function from calling itself infinitely?",
                "options": ["Base Case", "Terminating Frame", "Break Condition", "Default Case"],
                "answer": "Base Case",
            },
            {
                "question": "What error occurs when a recursive function lacks a base case or has excessively deep recursive calls?",
                "options": [
                    "Stack Overflow occurs due to call stack memory exhaustion",
                    "The compiler converts it to an infinite loop",
                    "Heap memory grows dynamically without bounds",
                    "The program exits cleanly with code 0"
                ],
                "answer": "Stack Overflow occurs due to call stack memory exhaustion",
            },
            {
                "question": "What type of recursion occurs when a function makes multiple recursive calls (e.g. f(n-1) twice), generating a branching call structure?",
                "options": ["Tree Recursion", "Tail Recursion", "Linear Recursion", "Nested Recursion"],
                "answer": "Tree Recursion",
            },
            {
                "question": "Where are the local variables and state of each recursive function call stored in memory?",
                "options": [
                    "Stack Memory (in distinct Stack Frames)",
                    "Heap Memory",
                    "Data Segment",
                    "Code/Text Segment"
                ],
                "answer": "Stack Memory (in distinct Stack Frames)",
            },
            {
                "question": "Which of the following is an advantage of using recursion in programming?",
                "options": [
                    "Reduces code length and easily solves problems on recursive data structures like Trees and Graphs",
                    "Uses less memory and runs faster than simple iterative loops",
                    "Eliminates function call overhead",
                    "Avoids allocating stack frames altogether"
                ],
                "answer": "Reduces code length and easily solves problems on recursive data structures like Trees and Graphs",
            },
        ],
        "theory": {
            "definition": "Recursion is a programming technique where a function calls itself repeatedly until a specific base condition is met. Each self-calling instance is a recursive call.",
            "why": "Recursion allows developers to write concise, elegant code for complex algorithms like tree traversal, divide and conquer, dynamic programming, and Tower of Hanoi.",
            "rules": [
                "Base Case: Every recursive function must contain a base case to terminate execution.",
                "Recursive Step: The function calls itself with modified arguments moving toward the base condition.",
                "Stack Frames: Each recursive invocation allocates a new stack frame on the call stack.",
                "Tree Recursion: Occurs when multiple recursive calls are made inside a single invocation (e.g., branching calls).",
                "Stack Overflow: Occurs when recursive depth exceeds fixed call stack memory limits.",
                "Trade-offs: Recursion offers cleaner code for recursive structures but introduces function call overhead and stack memory cost."
            ],
            "examples": [
                "#include <stdio.h>\n\n// Linear Recursion Example\nvoid rec(int n) {\n    if (n == 6) return;\n    printf(\"Recursion Level %d\\n\", n);\n    rec(n + 1);\n}\n\nint main(void) {\n    rec(1);\n    return 0;\n}",
                "#include <stdio.h>\n\n// Tree Recursion Example\nvoid f(int n) {\n    printf(\"F(%d)'s Stack Frame Pushed\\n\", n);\n    if (n > 1) {\n        f(n - 1);\n        f(n - 1);\n    }\n    printf(\"F(%d)'s Stack Frame Removed\\n\", n);\n}\n\nint main(void) {\n    f(3);\n    return 0;\n}"
            ],
        },
    },

    18: {
        "concept": "An inline function is a function declared with the inline keyword that suggests to the compiler to replace the function call directly with the actual function code. It reduces function call overhead (stack frame push/pop) for small, frequently called functions. Inlining is only a request; the compiler may ignore it for large or complex functions.",
        "syntax": "inline return_type function_name(parameters) {\n    // function body\n}",
        "example": {
            "code": "#include <stdio.h>\n\ninline int add(int a, int b) {\n    return a + b;\n}\n\nint main(void) {\n    int result = add(5, 3);\n    printf(\"Sum = %d\\n\", result);\n    return 0;\n}",
            "output": "Sum = 8",
            "explanation": "The inline keyword suggests replacing add(5, 3) with 5 + 3 directly at the call site during compilation, eliminating function call overhead.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\n_____ int add(int a, int b) {\n    return a + b;\n}\n\nint main(void) {\n    int result = add(5, 3);\n    printf(\"Sum = %d\", result);\n    return 0;\n}",
            "answers": ["inline"],
            "options": ["inline", "static", "extern", "macro", "register"],
        },
        "compiler": {
            "title": "C Inline Function Sandbox",
            "question": "Complete the inline function declaration to calculate the sum of two numbers.",
            "starter_code": "#include <stdio.h>\n\n_____ int add(int a, int b) {\n    return a + b;\n}\n\nint main(void) {\n    int result = add(5, 3);\n    printf(\"Sum = %d\\n\", result);\n    return 0;\n}",
            "options": ["inline", "define", "typedef", "extern"],
        },
        "skill_exa_test": [
            {
                "question": "What does the inline keyword in C suggest to the compiler?",
                "options": [
                    "Suggests replacing the function call with the actual function code to eliminate call overhead",
                    "Forces the compiler to execute the function on a background thread",
                    "Prevents the compiler from optimizing variable assignments",
                    "Defines a preprocessor macro without parameter checking"
                ],
                "answer": "Suggests replacing the function call with the actual function code to eliminate call overhead",
            },
            {
                "question": "Is the inline keyword a strict mandate or a suggestion to the C compiler?",
                "options": [
                    "It is only a suggestion; the compiler may choose not to inline large or complex functions",
                    "It is a mandatory compiler directive enforced in 100% of cases",
                    "It is a linker flag evaluated during execution",
                    "It is restricted only to main() function calls"
                ],
                "answer": "It is only a suggestion; the compiler may choose not to inline large or complex functions",
            },
            {
                "question": "What is a key advantage of an inline function over a #define macro in C?",
                "options": [
                    "Inline functions provide strict type-checking, scoping, and safer parameter evaluation",
                    "Inline functions cannot accept parameters",
                    "Macros execute faster than inline functions in all instances",
                    "Inline functions bypass compiler type-checking completely"
                ],
                "answer": "Inline functions provide strict type-checking, scoping, and safer parameter evaluation",
            },
            {
                "question": "What potential drawback can occur if inline functions are overused for large functions?",
                "options": [
                    "Executable binary size increases due to repeated code duplication",
                    "Variable scope errors occur in standard header files",
                    "Stack frames leak continuously during runtime",
                    "Function pointers lose access to global memory"
                ],
                "answer": "Executable binary size increases due to repeated code duplication",
            },
            {
                "question": "How are parameters evaluated in inline functions versus macros in C?",
                "options": [
                    "Inline function parameters are evaluated once, whereas macro parameters may be evaluated multiple times",
                    "Macro parameters are evaluated once, whereas inline function parameters are evaluated multiple times",
                    "Both macros and inline functions evaluate parameters twice",
                    "Neither macros nor inline functions evaluate function arguments"
                ],
                "answer": "Inline function parameters are evaluated once, whereas macro parameters may be evaluated multiple times",
            },
        ],
        "theory": {
            "definition": "An inline function is declared with the inline keyword to suggest compiler-level function substitution at the call site, eliminating function call stack overhead for small, performance-critical code.",
            "why": "Inline functions improve execution speed in performance-sensitive applications (embedded systems, real-time software) while providing type checking and debugging superior to preprocessor macros.",
            "rules": [
                "Syntax: Place inline before return type in function definition: inline int add(int a, int b) { ... }.",
                "Compiler Suggestion: inline is a hint; compilers may ignore it if functions are large, recursive, or complex.",
                "Vs Macros: Inline functions perform strict type-checking, evaluate arguments once, and respect scoping rules.",
                "Code Size Trade-off: Overusing inline on large functions increases executable binary size due to code duplication.",
                "Best Use Case: Ideal for small, frequently called helper functions."
            ],
            "examples": [
                "#include <stdio.h>\n\ninline int add(int a, int b) {\n    return a + b;\n}\n\nint main(void) {\n    int result = add(5, 3);\n    printf(\"Sum = %d\\n\", result);\n    return 0;\n}"
            ],
        },
    },

    19: {
        "concept": "Nesting of functions means defining one function inside another function body. Standard ISO C forbids nested function definitions (all functions must be defined at global scope). However, GCC supports nested functions as a compiler-specific extension featuring lexical scoping and runtime trampolines.",
        "syntax": "// Standard C: INVALID\n// GCC Extension: VALID\nvoid outer(void) {\n    void inner(void) {\n        printf(\"Nested Function\\n\");\n    }\n    inner();\n}",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    printf(\"Outer Function\\n\");\n    \n    // Defining inner function (GCC Extension)\n    void inner(void) {\n        printf(\"Inner Function\\n\");\n    }\n    \n    // Calling nested function\n    inner();\n    return 0;\n}",
            "output": "Outer Function\nInner Function",
            "explanation": "GCC allows defining inner() inside main(). Standard C compilers (like MSVC or strict Clang) produce compilation errors because standard C requires all functions to be defined at global file scope.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nint main(void) {\n    void inner(void) {\n        printf(\"Inner Function\\n\");\n    }\n    _____(); // Call nested function\n    return 0;\n}",
            "answers": ["inner"],
            "options": ["inner", "main", "outer", "printf"],
        },
        "compiler": {
            "title": "GCC Nested Functions Sandbox",
            "question": "Complete the C code to define and call a nested inner function within main using GCC extensions.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    printf(\"Outer\\n\");\n    void inner(void) {\n        printf(\"Inner\\n\");\n    }\n    _____();\n    return 0;\n}",
            "options": ["inner", "main", "outer", "return"],
        },
        "skill_exa_test": [
            {
                "question": "Are nested function definitions allowed in ISO Standard C?",
                "options": [
                    "No, ISO Standard C forbids defining functions inside other functions",
                    "Yes, ISO Standard C mandates nested functions for local helpers",
                    "Yes, nested functions are supported in C99 standard",
                    "No, functions can only be defined inside structure definitions"
                ],
                "answer": "No, ISO Standard C forbids defining functions inside other functions",
            },
            {
                "question": "Which C compiler natively supports nested functions as a non-standard compiler extension?",
                "options": [
                    "GNU Compiler Collection (GCC)",
                    "Microsoft Visual C++ (MSVC)",
                    "Standard C Preprocessor",
                    "Turbo C 1.0"
                ],
                "answer": "GNU Compiler Collection (GCC)",
            },
            {
                "question": "What runtime code structure does GCC generate when taking the memory address of a nested function?",
                "options": [
                    "Trampoline (runtime code linking nested function with outer stack frame)",
                    "Heap Allocation Table",
                    "Just-In-Time Bytecode Wrapper",
                    "Global Variable Proxy"
                ],
                "answer": "Trampoline (runtime code linking nested function with outer stack frame)",
            },
            {
                "question": "What is lexical scoping in the context of GCC nested functions?",
                "options": [
                    "The inner nested function can directly access local variables of its enclosing outer function",
                    "Nested functions inherit global scope visibility only",
                    "Variables declared inside inner functions become global static variables",
                    "Parameters passed to nested functions are restricted to floating point values"
                ],
                "answer": "The inner nested function can directly access local variables of its enclosing outer function",
            },
            {
                "question": "What is the effective lifetime of a GCC nested function that accesses outer local variables?",
                "options": [
                    "It remains valid only while the enclosing outer function's stack frame is active",
                    "It persists throughout the entire execution of the program",
                    "It expires immediately after the inner function's first line of code",
                    "It is managed by automatic heap garbage collection"
                ],
                "answer": "It remains valid only while the enclosing outer function's stack frame is active",
            },
        ],
        "theory": {
            "definition": "Nested functions refer to defining one function inside another. Standard C mandates all function definitions exist at global scope, making nested functions non-standard, though supported as a GCC compiler extension.",
            "why": "Understanding nested functions clarifies compiler extensions, lexical scoping, trampolines, and portability limitations when building cross-platform C software.",
            "rules": [
                "Standard C Limitation: ISO C requires all functions to be defined at global file scope.",
                "GCC Extension: GCC permits nested functions for localized helper utility functions.",
                "Lexical Scoping: Nested functions in GCC can access local variables of their enclosing outer function.",
                "Trampolines: When taking the address of a nested function, GCC creates a runtime trampoline linking to the outer stack frame.",
                "Lifetime Constraint: Accessing outer variables via a nested function pointer after the outer function returns causes undefined behavior (destroyed stack frame).",
                "Portability: Avoid nested functions in standard C projects to maintain compatibility across non-GCC compilers (MSVC, Clang)."
            ],
            "examples": [
                "#include <stdio.h>\n\n// GCC Nested Function Extension Example\nint main(void) {\n    printf(\"Outer Function\\n\");\n    void inner(void) {\n        printf(\"Inner Function\\n\");\n    }\n    inner();\n    return 0;\n}",
                "#include <stdio.h>\n\n// Lexical Scoping & Trampoline Example\nvoid print(void (*fp)()) {\n    fp();\n}\n\nvoid outer(int x) {\n    int y = 10;\n    void inner(void) {\n        printf(\"Sum: %d\\n\", x + y);\n    }\n    void (*fp)() = &inner;\n    print(fp);\n}\n\nint main(void) {\n    outer(5); // Outputs: 15\n    return 0;\n}"
            ],
        },
    },

    20: {
        "concept": "An array in C is a fixed-size collection of elements of the same data type stored in contiguous memory locations. Indexing starts at 0 (0 to n - 1). Arrays allow direct element access using the subscript operator [], element updates, traversal using loops, and size calculation using sizeof(arr) / sizeof(arr[0]).",
        "syntax": "data_type array_name[size];              // Declaration\nint arr[5] = {2, 4, 8, 12, 16};           // Initialization\nint n = sizeof(arr) / sizeof(arr[0]);     // Size calculation",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    int arr[] = {2, 4, 8, 12, 16, 18};\n    int n = sizeof(arr) / sizeof(arr[0]);\n\n    // Printing array elements\n    for (int i = 0; i < n; i++) {\n        printf(\"%d \", arr[i]);\n    }\n    return 0;\n}",
            "output": "2 4 8 12 16 18",
            "explanation": "arr is an array of integers stored in contiguous memory locations. sizeof(arr)/sizeof(arr[0]) calculates element count (6), and a loop traverses each element by its 0-based index.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nint main(void) {\n    int arr[5] = {2, 4, 8, 12, 16};\n    int size = sizeof(arr) / sizeof(_____);\n    printf(\"%d\", arr[_____]); // Print last element\n    return 0;\n}",
            "answers": ["arr[0]", "4"],
            "options": ["arr[0]", "4", "5", "arr", "size", "1"],
        },
        "compiler": {
            "title": "C Arrays Sandbox",
            "question": "Complete the C code to calculate array size using sizeof and traverse elements.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int arr[5] = {2, 4, 8, 12, 16};\n    int n = sizeof(arr) / sizeof(_____);\n\n    for (int i = 0; i < n; i++) {\n        printf(\"%d \", arr[i]);\n    }\n    return 0;\n}",
            "options": ["arr[0]", "arr", "5", "int"],
        },
        "skill_exa_test": [
            {
                "question": "What is the starting index of an array in C?",
                "options": ["0", "1", "-1", "Memory base offset"],
                "answer": "0",
            },
            {
                "question": "How are array elements stored in computer memory in C?",
                "options": [
                    "In contiguous memory locations",
                    "In non-contiguous heap blocks",
                    "In linked list pointers",
                    "In random stack registers"
                ],
                "answer": "In contiguous memory locations",
            },
            {
                "question": "How do you calculate the total number of elements in an array `int arr[10]`?",
                "options": [
                    "sizeof(arr) / sizeof(arr[0])",
                    "sizeof(arr) * 10",
                    "arr.length()",
                    "count(arr)"
                ],
                "answer": "sizeof(arr) / sizeof(arr[0])",
            },
            {
                "question": "What happens if a local array `int arr[5];` is declared without an initializer and read before assignment?",
                "options": [
                    "It results in undefined behavior due to garbage/indeterminate values",
                    "Elements are automatically initialized to zero",
                    "The compiler throws a syntax error",
                    "The program terminates with code 1"
                ],
                "answer": "It results in undefined behavior due to garbage/indeterminate values",
            },
            {
                "question": "What happens when you attempt to access an array element outside its valid index range (0 to n - 1)?",
                "options": [
                    "Undefined behavior occurs",
                    "An ArrayIndexOutOfBoundsException is thrown",
                    "The array automatically expands",
                    "The index wraps around to 0"
                ],
                "answer": "Undefined behavior occurs",
            },
        ],
        "theory": {
            "definition": "An array is a fixed-size collection of elements of the same data type stored in contiguous memory locations in C.",
            "why": "Arrays enable storing multiple values under a single variable name and support random access in O(1) time complexity.",
            "rules": [
                "Fixed Size: Array size must be specified at declaration or inferred from initialization list.",
                "Contiguous Memory: Elements are stored sequentially in adjacent memory addresses.",
                "0-Based Indexing: Index ranges from 0 to n - 1 for an array of size n.",
                "Uninitialized Local Arrays: Local arrays contain indeterminate garbage values unless explicitly initialized.",
                "Size Formula: sizeof(arr) / sizeof(arr[0]) calculates total element count.",
                "Bounds Checking: C does not perform automatic array bound checks; out-of-bounds access causes undefined behavior."
            ],
            "examples": [
                "#include <stdio.h>\n\nint main(void) {\n    int arr[5] = {2, 4, 8, 12, 16};\n    for (int i = 0; i < 5; i++) {\n        printf(\"%d \", arr[i]);\n    }\n    return 0;\n}"
            ],
        },
    },

    21: {
        "concept": "A multidimensional array in C organizes data in multiple dimensions (2D arrays with rows/columns, 3D arrays with depth/rows/columns). Multidimensional arrays are stored in contiguous memory locations in row-major order. The first dimension size can be omitted during array initialization, but subsequent dimension sizes are mandatory.",
        "syntax": "// 2D Array: type arr[rows][cols];\nint arr2D[3][4] = {{0,1,2,3}, {4,5,6,7}, {8,9,10,11}};\n\n// 3D Array: type arr[depth][rows][cols];\nint arr3D[2][3][2] = { {{{1,1},{2,3},{4,5}}}, {{{6,7},{8,9},{10,11}}} };",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    int arr[2][2] = { {10, 20}, {30, 40} };\n\n    printf(\"2D Array Elements:\\n\");\n    for (int i = 0; i < 2; i++) {\n        for (int j = 0; j < 2; j++) {\n            printf(\"%d \", arr[i][j]);\n        }\n        printf(\"\\n\");\n    }\n    return 0;\n}",
            "output": "2D Array Elements:\n10 20 \n30 40 ",
            "explanation": "arr[2][2] creates a 2D integer array with 2 rows and 2 columns. Nested loops traverse rows (outer loop i) and columns (inner loop j).",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nvoid print2D(int arr[][_____], int rows) {\n    for (int i = 0; i < rows; i++) {\n        for (int j = 0; j < 3; j++) {\n            printf(\"%d \", arr[i][j]);\n        }\n    }\n}",
            "answers": ["3"],
            "options": ["3", "rows", "i", "*"],
        },
        "compiler": {
            "title": "C Multidimensional Array Sandbox",
            "question": "Complete the nested loop indices to print a 2x2 2D array row by row.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int arr[2][2] = { {10, 20}, {30, 40} };\n\n    for (int i = 0; i < 2; i++) {\n        for (int j = 0; j < 2; j++) {\n            printf(\"%d \", arr[_____][_____]);\n        }\n        printf(\"\\n\");\n    }\n    return 0;\n}",
            "options": ["i", "j", "2", "0"],
        },
        "skill_exa_test": [
            {
                "question": "How does the C language store multidimensional arrays in linear computer memory?",
                "options": [
                    "Row-major order",
                    "Column-major order",
                    "Diagonal-major order",
                    "Random sparse blocks"
                ],
                "answer": "Row-major order",
            },
            {
                "question": "For a 2D array `int arr[10][20]`, how many total bytes are occupied if `sizeof(int) == 4`?",
                "options": [
                    "800 bytes (10 * 20 * 4)",
                    "200 bytes",
                    "400 bytes",
                    "80 bytes"
                ],
                "answer": "800 bytes (10 * 20 * 4)",
            },
            {
                "question": "When initializing a 2D array `int arr[][4] = { {1,2,3,4}, {5,6,7,8} };`, which dimension can be omitted?",
                "options": [
                    "Row dimension size can be omitted, but column dimension is mandatory",
                    "Column dimension size can be omitted",
                    "Both row and column dimensions can be omitted",
                    "Neither dimension can ever be omitted"
                ],
                "answer": "Row dimension size can be omitted, but column dimension is mandatory",
            },
            {
                "question": "How many indices are required to access an element in a 3D array `arr[depth][row][column]`?",
                "options": ["3 indices", "2 indices", "1 index", "4 indices"],
                "answer": "3 indices",
            },
            {
                "question": "When passing a 2D array `int arr[][3]` to a C function parameter, why must the column size 3 be specified in the function signature?",
                "options": [
                    "So the compiler can calculate memory offset addresses for row-major order indexing",
                    "Because standard C requires all array dimensions to be 100",
                    "To prevent stack frame overflow",
                    "To automatically initialize unallocated memory"
                ],
                "answer": "So the compiler can calculate memory offset addresses for row-major order indexing",
            },
        ],
        "theory": {
            "definition": "A multidimensional array in C is an array of arrays used to store data in tabular (2D) or volumetric/layered (3D) form.",
            "why": "Multidimensional arrays model matrices, grid maps, graphics tables, and multi-layered data structures.",
            "rules": [
                "2D Array Syntax: type arr[rows][cols];.",
                "3D Array Syntax: type arr[depth][rows][cols];.",
                "Row-Major Storage: Elements of row 0 are stored sequentially, followed by row 1, etc.",
                "Omitted Dimensions: In array initializers, only the outermost (first) dimension size may be left blank.",
                "Function Parameter Rule: When passing 2D/3D arrays, all dimension sizes except the first must be explicitly declared."
            ],
            "examples": [
                "#include <stdio.h>\n\nint main(void) {\n    int arr[2][2] = { {10, 20}, {30, 40} };\n    for (int i = 0; i < 2; i++) {\n        for (int j = 0; j < 2; j++) {\n            printf(\"%d \", arr[i][j]);\n        }\n        printf(\"\\n\");\n    }\n    return 0;\n}"
            ],
        },
    },

    22: {
        "concept": "A string in C is a sequence of characters stored in a char array and terminated by the null character '\\0'. C has no built-in string primitive type; strings are managed via null-terminated char arrays or const char * string literals. scanf(\"%s\", str) reads single words, while fgets(str, size, stdin) reads entire lines including spaces.",
        "syntax": "char str[] = \"Geeks\";            // Character array with '\\0'\nconst char *lit = \"Hello World\";   // String literal (read-only)\nfgets(str, sizeof(str), stdin);    // Safe line input",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    char str[] = \"Geeks\";\n    printf(\"The string is: %s\\n\", str);\n    return 0;\n}",
            "output": "The string is: Geeks",
            "explanation": "char str[] = \"Geeks\" creates a 6-element character array containing 'G', 'e', 'e', 'k', 's', '\\0'. %s prints characters until encountering '\\0'.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nint main(void) {\n    char str[20];\n    _____(str, sizeof(str), stdin); // Read line including spaces safely\n    printf(\"%s\", str);\n    return 0;\n}",
            "answers": ["fgets"],
            "options": ["fgets", "scanf", "gets", "puts", "strcpy"],
        },
        "compiler": {
            "title": "C Strings Sandbox",
            "question": "Complete the character pointer traversal loop until reaching the null character '\\0'.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    char str[20] = \"GeeksforGeeks\";\n    char *ptr = str;\n    while (*ptr != '_____') {\n        printf(\"%c\", *ptr);\n        ptr++;\n    }\n    return 0;\n}",
            "options": ["\\0", "0", "\\n", "EOF"],
        },
        "skill_exa_test": [
            {
                "question": "What special character marks the end of a string in C?",
                "options": [
                    "The null character '\\0'",
                    "The newline character '\\n'",
                    "The space character ' '",
                    "EOF marker"
                ],
                "answer": "The null character '\\0'",
            },
            {
                "question": "What is the array size allocated for `char str[] = \"Geeks\";`?",
                "options": [
                    "6 bytes (5 characters + 1 null terminator '\\0')",
                    "5 bytes",
                    "4 bytes",
                    "20 bytes"
                ],
                "answer": "6 bytes (5 characters + 1 null terminator '\\0')",
            },
            {
                "question": "Which C input function reads an entire line including whitespace until encountering a newline?",
                "options": ["fgets()", "scanf(\"%s\")", "getchar()", "strlen()"],
                "answer": "fgets()",
            },
            {
                "question": "Why does modifying a string literal `const char *str = \"Hello\"; str[0] = 'h';` cause undefined behavior?",
                "options": [
                    "String literals are stored in read-only memory",
                    "String literals do not contain null terminators",
                    "The compiler converts string literals to integers",
                    "Pointers cannot access character memory"
                ],
                "answer": "String literals are stored in read-only memory",
            },
            {
                "question": "How does `scanf(\"%s\", str)` handle whitespace (spaces, tabs, newlines)?",
                "options": [
                    "It stops reading input as soon as it encounters any whitespace",
                    "It reads spaces as regular characters",
                    "It converts whitespace to null terminators",
                    "It throws an input format exception"
                ],
                "answer": "It stops reading input as soon as it encounters any whitespace",
            },
        ],
        "theory": {
            "definition": "A string in C is a contiguous sequence of characters stored in a character array and terminated by the null character '\\0'.",
            "why": "Strings enable processing text data, user input, sentences, and messages in C applications.",
            "rules": [
                "Null Termination: All C string functions depend on '\\0' to identify the end of a string.",
                "Memory Allocation: Always allocate 1 extra byte for '\\0' (e.g. 5-char string needs 6-byte array).",
                "Input Handling: scanf(\"%s\") stops at space; fgets(str, size, stdin) reads full lines with spaces.",
                "String Literals: Enclosed in double quotes and stored in read-only memory. Use const char *.",
                "Modifiability: Array-based strings char str[] = \"Hello\" can be updated; string literals const char *str = \"Hello\" cannot."
            ],
            "examples": [
                "#include <stdio.h>\n\nint main(void) {\n    char str[] = \"Geeks\";\n    printf(\"%s\\n\", str);\n    return 0;\n}"
            ],
        },
    },

    23: {
        "concept": """String functions in <string.h> perform essential text operations organized into 6 key categories:

1. Length & Copying: strlen, strcpy, strncpy
2. Concatenation: strcat, strncat
3. Comparison: strcmp, strncmp
4. Character Search: strchr, strrchr
5. Substring & Formatting: strstr, sprintf
6. Tokenization: strtok

All functions operate on null-terminated strings.""",
        "syntax": "#include <string.h>\n\nstrlen(str);               // String length\nstrcpy(dest, src);         // Copy string\nstrcat(dest, src);         // Concatenate strings\nstrcmp(s1, s2);            // Compare strings (0 if equal)\nstrchr(str, 'c');          // Search first character\nstrstr(str, \"sub\");        // Search substring\nsprintf(buf, \"fmt\", ...);  // Format string buffer\nstrtok(str, \"delim\");      // Tokenize string",
        "example": {
            "code": "#include <stdio.h>\n#include <string.h>\n\nint main(void) {\n    char src[] = \"Hello, \";\n    char dest[30] = \"World\";\n\n    // Pair 1: Length & Copy\n    printf(\"Length: %lu\\n\", strlen(src));\n    \n    // Pair 2: Concatenation\n    strcat(src, dest);\n    printf(\"Concatenated: %s\\n\", src);\n\n    // Pair 3: Comparison\n    if (strcmp(\"Apple\", \"Apple\") == 0) {\n        printf(\"Strings are equal\\n\");\n    }\n    return 0;\n}",
            "output": "Length: 7\nConcatenated: Hello, World\nStrings are equal",
            "explanation": "Demonstrates <string.h> library functions. strlen() calculates character length excluding '\\0'. strcat() appends dest to src. strcmp() compares strings lexicographically, returning 0 when identical.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n#include <string.h>\n\nint main(void) {\n    char s1[30] = \"Hello, \";\n    char s2[] = \"Geeks!\";\n    _____(s1, s2); // Append s2 to s1\n    printf(\"%s\", s1);\n    return 0;\n}",
            "answers": ["strcat"],
            "options": ["strcat", "strcpy", "strcmp", "strlen", "sprintf"],
        },
        "compiler": {
            "title": "C String Functions Sandbox",
            "question": "Complete the string functions to copy src to dest and calculate its length.",
            "starter_code": "#include <stdio.h>\n#include <string.h>\n\nint main(void) {\n    char src[] = \"SkillExa\";\n    char dest[20];\n    _____(dest, src);\n    printf(\"%s (Len: %lu)\\n\", dest, _____(dest));\n    return 0;\n}",
            "options": ["strcpy", "strlen", "strcat", "strcmp"],
        },
        "skill_exa_test": [
            {
                "question": "What header file must be included to use C standard string functions like strcpy(), strcat(), and strcmp()?",
                "options": ["<string.h>", "<stdio.h>", "<stdlib.h>", "<math.h>"],
                "answer": "<string.h>",
            },
            {
                "question": "Does strlen(\"Geeks\") include the null terminator '\\0' in its returned count?",
                "options": [
                    "No, strlen() excludes the null terminator '\\0' (returns 5)",
                    "Yes, strlen() includes '\\0' (returns 6)",
                    "It returns the array memory size in bytes",
                    "It returns 0 for all string arrays"
                ],
                "answer": "No, strlen() excludes the null terminator '\\0' (returns 5)",
            },
            {
                "question": "What value does strcmp(s1, s2) return when both strings s1 and s2 are lexicographically identical?",
                "options": ["0", "1", "-1", "NULL pointer"],
                "answer": "0",
            },
            {
                "question": "What is the primary difference between strchr() and strrchr() in <string.h>?",
                "options": [
                    "strchr() finds the first occurrence of a character, while strrchr() finds the last occurrence",
                    "strchr() searches strings, while strrchr() searches numbers",
                    "strchr() compares strings, while strrchr() copies strings",
                    "They perform identical forward searches"
                ],
                "answer": "strchr() finds the first occurrence of a character, while strrchr() finds the last occurrence",
            },
            {
                "question": "How does strtok(str, delim) tokenize a string, and what is passed as the first argument in subsequent calls?",
                "options": [
                    "It replaces delimiters with '\\0'; subsequent calls pass NULL as the first argument",
                    "It creates new heap copies; subsequent calls pass the original string",
                    "It deletes matching characters; subsequent calls pass '0'",
                    "It parses string length; subsequent calls pass EOF"
                ],
                "answer": "It replaces delimiters with '\\0'; subsequent calls pass NULL as the first argument",
            },
        ],
        "theory": {
            "definition": "String functions in C are pre-compiled library functions in <string.h> used to manipulate, search, compare, copy, and tokenize null-terminated character arrays.",
            "why": "Using standard string library functions eliminates the need to manually implement character-by-character loops for text processing.",
            "rules": [
                "Pair 1 (Length & Copy): strlen(str) returns character count. strcpy(dest, src) copies characters including \\0. strncpy(dest, src, n) limits copy to n bytes.",
                "Pair 2 (Concatenation): strcat(dest, src) appends src to dest. strncat(dest, src, n) appends at most n characters.",
                "Pair 3 (Comparison): strcmp(s1, s2) compares strings (0 if equal, <0 if s1 < s2, >0 if s1 > s2). strncmp(s1, s2, n) compares first n chars.",
                "Pair 4 (Search Chars): strchr(s, 'c') returns pointer to first occurrence. strrchr(s, 'c') returns pointer to last occurrence.",
                "Pair 5 (Search Substrings & Format): strstr(s, \"sub\") searches substring. sprintf(buf, fmt, ...) formats output to string buffer.",
                "Pair 6 (Tokenization): strtok(s, delim) splits strings into tokens by replacing delimiters with \\0."
            ],
            "examples": [
                "#include <stdio.h>\n#include <string.h>\n\nint main(void) {\n    char s1[20] = \"Hello \";\n    char s2[] = \"C\";\n    strcat(s1, s2);\n    printf(\"%s (Len: %lu)\\n\", s1, strlen(s1));\n    return 0;\n}"
            ],
        },
    },

    24: {
        "concept": "A pointer in C is a variable that stores the memory address of another variable rather than a direct value. The address operator (&) obtains the memory location, while the dereference operator (*) accesses the value stored at that address. Pointer size is uniform across data types on a given machine (typically 4 bytes on 32-bit systems, 8 bytes on 64-bit systems). Special pointer types include NULL pointers, Void (generic) pointers, Wild pointers, and Dangling pointers.",
        "syntax": "data_type *pointer_name;          // Declaration\npointer_name = &variable;          // Initialization with address\n*pointer_name = 100;              // Dereferencing (access/modify)\nint *ptr = NULL;                  // NULL pointer\nvoid *vptr;                       // Generic void pointer",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    int var = 10;\n    int *ptr = &var;\n\n    printf(\"Memory Address: %p\\n\", (void*)ptr);\n    printf(\"Dereferenced Value: %d\\n\", *ptr);\n    return 0;\n}",
            "output": "Memory Address: 0x7fffffffe9cc\nDereferenced Value: 10",
            "explanation": "int *ptr = &var assigns the memory address of var to ptr. Format specifier %p prints hexadecimal memory addresses, while *ptr dereferences ptr to retrieve the value 10.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nint main(void) {\n    int var = 10;\n    int *ptr = _____var; // Store address of var\n    printf(\"%d\", _____ptr); // Dereference ptr\n    return 0;\n}",
            "answers": ["&", "*"],
            "options": ["&", "*", "->", "%", "var", "int"],
        },
        "compiler": {
            "title": "C Pointers Sandbox",
            "question": "Complete the code using address-of (&) and dereference (*) operators to print 10.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int val = 10;\n    int *ptr = _____val;\n    printf(\"Val: %d\\n\", _____ptr);\n    return 0;\n}",
            "options": ["&", "*", "->", "val"],
        },
        "skill_exa_test": [
            {
                "question": "What is the primary purpose of a pointer variable in C?",
                "options": [
                    "To store the memory address of another variable",
                    "To store high-precision floating point numbers",
                    "To replace all standard library functions",
                    "To allocate stack memory automatically"
                ],
                "answer": "To store the memory address of another variable",
            },
            {
                "question": "What is the size of a pointer (int*, char*, float*) on a 64-bit operating system architecture?",
                "options": [
                    "8 bytes for all pointer types",
                    "4 bytes for int* and 1 byte for char*",
                    "Varies depending on data type size",
                    "16 bytes"
                ],
                "answer": "8 bytes for all pointer types",
            },
            {
                "question": "Which pointer type is defined as an uninitialized pointer storing an arbitrary/invalid memory address?",
                "options": [
                    "Wild Pointer",
                    "NULL Pointer",
                    "Dangling Pointer",
                    "Void Pointer"
                ],
                "answer": "Wild Pointer",
            },
            {
                "question": "What is a Dangling Pointer in C programming?",
                "options": [
                    "A pointer pointing to a memory location that has been deallocated or freed",
                    "A pointer initialized to 0 or NULL",
                    "A generic void pointer before typecasting",
                    "A constant pointer defined at file scope"
                ],
                "answer": "A pointer pointing to a memory location that has been deallocated or freed",
            },
            {
                "question": "Why must a void * (generic) pointer be typecast before dereferencing in C?",
                "options": [
                    "Because void has no associated data type, so the compiler doesn't know how many bytes to read",
                    "Because void pointers are automatically converted to float",
                    "Because void pointers are read-only memory literals",
                    "Because typecasting converts stack memory to heap memory"
                ],
                "answer": "Because void has no associated data type, so the compiler doesn't know how many bytes to read",
            },
        ],
        "theory": {
            "definition": "A pointer is a variable that stores the memory address of another variable in C.",
            "why": "Pointers enable low-level memory access, dynamic memory allocation, efficient array/structure passing, and complex data structures (linked lists, trees, graphs).",
            "rules": [
                "Address Operator (&): Returns the memory address of a variable.",
                "Dereference Operator (*): Accesses the value stored at the memory address pointed to.",
                "Format Specifiers: Use %p for printing memory addresses, %d for integer values.",
                "Uniform Size: Pointer size depends on OS architecture (4 bytes on 32-bit, 8 bytes on 64-bit), not data type.",
                "Pointer Types: NULL (points to nothing), Void (generic pointer), Wild (uninitialized), Dangling (points to freed memory).",
                "Safety Rule: Always initialize pointers with a valid address or NULL before use."
            ],
            "examples": [
                "#include <stdio.h>\n\nint main(void) {\n    int val = 10;\n    int *ptr = &val;\n    printf(\"Address: %p, Value: %d\\n\", (void*)ptr, *ptr);\n    return 0;\n}"
            ],
        },
    },

    25: {
        "concept": "Pointer arithmetic in C refers to valid mathematical operations on memory addresses. Unlike integer arithmetic, incrementing/decrementing a pointer moves the address by sizeof(data_type) bytes, not 1 byte. Formula: New Address = Current Address ± (N × sizeof(data_type)). Allowed operations include increment (ptr++), decrement (ptr--), adding/subtracting integers (ptr + N), subtracting two pointers of the same type (returns element count difference), and pointer comparisons (==, !=, <, >). Adding two pointers is invalid.",
        "syntax": "int *ptr = arr;\nptr++;                        // Moves by sizeof(int) bytes (+4)\nptr = ptr + 3;                // Moves by 3 * sizeof(int) bytes (+12)\nint diff = ptr2 - ptr1;       // Number of elements between ptr1 and ptr2\nif (ptr1 == ptr2) { ... }      // Pointer comparison",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    int arr[] = {10, 20, 30, 40, 50};\n    int *ptr = arr;\n\n    printf(\"First element: %d\\n\", *ptr);\n    ptr++; // Moves by 4 bytes (sizeof(int))\n    printf(\"Second element: %d\\n\", *ptr);\n\n    ptr = ptr + 2; // Moves forward by 2 elements\n    printf(\"Fourth element: %d\\n\", *ptr);\n    return 0;\n}",
            "output": "First element: 10\nSecond element: 20\nFourth element: 40",
            "explanation": "ptr initially points to arr[0]. ptr++ increments the memory address by sizeof(int) (4 bytes), advancing to arr[1]. ptr + 2 moves 2 more elements forward to arr[3].",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nint main(void) {\n    int arr[] = {1, 2, 3, 4, 5};\n    int *ptr1 = &arr[0];\n    int *ptr2 = &arr[4];\n    int diff = ptr2 _____ ptr1; // Element count difference\n    printf(\"%d\", diff);\n    return 0;\n}",
            "answers": ["-"],
            "options": ["-", "+", "*", "/", "&"],
        },
        "compiler": {
            "title": "C Pointer Arithmetic Sandbox",
            "question": "Complete the code using pointer arithmetic to traverse array elements.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int arr[] = {10, 20, 30};\n    int *ptr = arr;\n\n    for (int i = 0; i < 3; i++) {\n        printf(\"%d \", *ptr);\n        _____; // Increment pointer\n    }\n    return 0;\n}",
            "options": ["ptr++", "ptr = ptr + 1", "*ptr++", "i++"],
        },
        "skill_exa_test": [
            {
                "question": "If an integer pointer `int *ptr` stores memory address 1000 on a machine where sizeof(int) == 4, what address is stored after evaluating ptr + 2?",
                "options": ["1008", "1002", "1004", "1016"],
                "answer": "1008",
            },
            {
                "question": "What does subtracting two pointers of the same type `ptr2 - ptr1` produce in C?",
                "options": [
                    "The number of elements between the two memory locations",
                    "The total difference in bytes divided by 100",
                    "A new pointer pointing to address 0",
                    "A syntax compilation error"
                ],
                "answer": "The number of elements between the two memory locations",
            },
            {
                "question": "Which of the following pointer arithmetic operations is ILLEGAL in C?",
                "options": [
                    "Adding two pointers together (ptr1 + ptr2)",
                    "Subtracting an integer from a pointer (ptr - 3)",
                    "Subtracting two pointers of the same type (ptr2 - ptr1)",
                    "Comparing two pointers using relational operators (ptr1 < ptr2)"
                ],
                "answer": "Adding two pointers together (ptr1 + ptr2)",
            },
            {
                "question": "If `char *r` (where sizeof(char) == 1) points to address 2000, what address will `r++` point to?",
                "options": ["2001", "2004", "2008", "2000"],
                "answer": "2001",
            },
            {
                "question": "Why do memory addresses of pointers change between different execution runs of the same program?",
                "options": [
                    "Due to Address Space Layout Randomization (ASLR) used by modern operating systems",
                    "Because compiler optimizes pointers into garbage registers",
                    "Because arrays are non-contiguous in RAM",
                    "Due to hardware clock cycle desynchronization"
                ],
                "answer": "Due to Address Space Layout Randomization (ASLR) used by modern operating systems",
            },
        ],
        "theory": {
            "definition": "Pointer arithmetic refers to performing valid operations (increment, decrement, integer addition/subtraction, pointer subtraction, and pointer comparison) on memory addresses.",
            "why": "Pointer arithmetic enables efficient array traversal, buffer manipulation, and dynamic memory offset calculations without index bounds overhead.",
            "rules": [
                "Scaling Rule: New Address = Current Address ± (N × sizeof(type)).",
                "Increment/Decrement: ptr++ adds sizeof(type) bytes; ptr-- subtracts sizeof(type) bytes.",
                "Pointer Subtraction: ptr2 - ptr1 returns element distance between two pointers of matching data types.",
                "Prohibited Operation: Adding two pointers (ptr1 + ptr2) is invalid.",
                "Array Relationship: arr acts as a constant pointer to &arr[0].",
                "Pointer Comparison: Relational operators (==, !=, <, >) compare memory addresses."
            ],
            "examples": [
                "#include <stdio.h>\n\nint main(void) {\n    int arr[3] = {1, 2, 3};\n    int *p = arr;\n    printf(\"%d %d %d\\n\", *p, *(p+1), *(p+2));\n    return 0;\n}"
            ],
        },
    },

    26: {
        "concept": "A double pointer (pointer to pointer, declared as **) is a pointer variable that stores the memory address of another pointer. Single pointer ptr1 points to a data variable, while double pointer ptr2 points to ptr1. Double pointers are used for dynamic 2D array allocation (malloc), passing pointers to functions for modification, array of string handling (char **), and multi-level data structures.",
        "syntax": "int var = 10;\nint *ptr1 = &var;       // Single pointer\nint **ptr2 = &ptr1;     // Double pointer\n\n// Dynamic 2D Array:\nint **arr = (int **)malloc(m * sizeof(int *));\nfor(int i = 0; i < m; i++) arr[i] = (int *)malloc(n * sizeof(int));",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    int var = 10;\n    int *ptr1 = &var;\n    int **ptr2 = &ptr1;\n\n    printf(\"var: %d\\n\", var);\n    printf(\"*ptr1: %d\\n\", *ptr1);\n    printf(\"**ptr2: %d\\n\", **ptr2);\n    return 0;\n}",
            "output": "var: 10\n*ptr1: 10\n**ptr2: 10",
            "explanation": "ptr1 holds the address of var. ptr2 holds the address of ptr1. Dereferencing *ptr1 gives 10. Double dereferencing **ptr2 first accesses ptr1 and then retrieves var (10).",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nint main(void) {\n    int num = 50;\n    int *p = &num;\n    int _____ dp = &p; // Double pointer declaration\n    printf(\"%d\", _____dp); // Double dereference\n    return 0;\n}",
            "answers": ["**", "**"],
            "options": ["**", "*", "&", "int", "->", "dp"],
        },
        "compiler": {
            "title": "C Double Pointer Sandbox",
            "question": "Complete the double pointer declaration and dereferencing to print num value.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int a = 100;\n    int *ptr = &a;\n    int _____ dptr = &ptr;\n    printf(\"Val: %d\\n\", _____dptr);\n    return 0;\n}",
            "options": ["**", "*", "&", "a"],
        },
        "skill_exa_test": [
            {
                "question": "What does a double pointer (`int **ptr`) store in C?",
                "options": [
                    "The memory address of another pointer",
                    "Directly two integer values",
                    "The address of a float variable",
                    "A 64-bit floating point exponent"
                ],
                "answer": "The memory address of another pointer",
            },
            {
                "question": "Given `int x = 5; int *p = &x; int **dp = &p;`, what does `**dp` evaluate to?",
                "options": ["5", "Address of x", "Address of p", "Garbage value"],
                "answer": "5",
            },
            {
                "question": "What is the memory size of a double pointer (`int **d_ptr`) on a 64-bit architecture?",
                "options": [
                    "8 bytes (same size as any other pointer)",
                    "16 bytes",
                    "4 bytes",
                    "32 bytes"
                ],
                "answer": "8 bytes (same size as any other pointer)",
            },
            {
                "question": "Why are double pointers commonly used when allocating dynamic 2D arrays with malloc()?",
                "options": [
                    "To create an array of row pointers, where each row is allocated dynamically",
                    "Because single pointers cannot hold integer arrays",
                    "To bypass stack memory limits",
                    "Because C compiler requires ** for all malloc calls"
                ],
                "answer": "To create an array of row pointers, where each row is allocated dynamically",
            },
            {
                "question": "How can an array of string literals `char *arr[] = {\"Geek\", \"Geeks\"};` be passed as a parameter to a function signature?",
                "options": [
                    "void print(char **arr, int n)",
                    "void print(char arr, int n)",
                    "void print(int **arr, int n)",
                    "void print(char *arr[], float n)"
                ],
                "answer": "void print(char **arr, int n)",
            },
        ],
        "theory": {
            "definition": "A double pointer in C is a pointer variable that stores the memory address of another pointer variable.",
            "why": "Double pointers allow dynamic allocation of multidimensional arrays, passing pointer addresses to functions to modify caller pointers, and managing complex data structures (linked lists, trees).",
            "rules": [
                "Declaration Syntax: type **d_ptr;.",
                "Initialization: d_ptr = &s_ptr; (where s_ptr is a single pointer).",
                "Double Dereferencing: **d_ptr retrieves the final target value.",
                "Memory Size: The size of int ** is identical to int * (4 bytes on 32-bit, 8 bytes on 64-bit).",
                "Multi-level Pointers: C supports triple pointers (***), quadruple pointers (****), etc."
            ],
            "examples": [
                "#include <stdio.h>\n\nint main(void) {\n    int val = 10;\n    int *p = &val;\n    int **dp = &p;\n    printf(\"%d %d %d\\n\", val, *p, **dp);\n    return 0;\n}"
            ],
        },
    },

    27: {
        "concept": "A function pointer in C is a pointer that stores the memory address of executable code (a function) in the code segment rather than data in stack/heap. It enables indirect/dynamic function calls, passing functions as arguments (callbacks), emulating object member functions inside structures, and building array function lookup tables. Pointer arithmetic cannot be performed on function pointers.",
        "syntax": "// Syntax: return_type (*pointer_name)(parameter_types);\nint (*fptr)(int, int);      // Declaration matching int func(int, int)\nfptr = &add;                // Initialization (& is optional)\nint res = fptr(10, 5);      // Execution call via pointer",
        "example": {
            "code": "#include <stdio.h>\n\nint add(int a, int b) {\n    return a + b;\n}\n\nint main(void) {\n    // Declare function pointer matching add() signature\n    int (*fptr)(int, int) = &add;\n\n    // Call function indirectly via pointer\n    printf(\"Result: %d\\n\", fptr(10, 5));\n    return 0;\n}",
            "output": "Result: 15",
            "explanation": "int (*fptr)(int, int) declares a function pointer taking two integers and returning an integer. fptr = &add assigns the entry point address of add(). fptr(10, 5) invokes add(10, 5) dynamically.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nint multiply(int a, int b) { return a * b; }\n\nint main(void) {\n    int (_____fptr)(int, int) = multiply; // Function pointer declaration\n    printf(\"%d\", fptr(3, 4));\n    return 0;\n}",
            "answers": ["*"],
            "options": ["*", "&", "**", "->", "int"],
        },
        "compiler": {
            "title": "C Function Pointer Sandbox",
            "question": "Complete the function pointer declaration and invocation to execute add(10, 5).",
            "starter_code": "#include <stdio.h>\n\nint add(int a, int b) { return a + b; }\n\nint main(void) {\n    int (_____fptr)(int, int) = add;\n    printf(\"Sum: %d\\n\", fptr(10, 5));\n    return 0;\n}",
            "options": ["*", "&", "**", "add"],
        },
        "skill_exa_test": [
            {
                "question": "What does a function pointer store in C?",
                "options": [
                    "The memory address of executable function code in the code segment",
                    "The return value of a function stored on stack",
                    "The local variables of main()",
                    "A heap allocation pointer"
                ],
                "answer": "The memory address of executable function code in the code segment",
            },
            {
                "question": "Which declaration correctly defines a function pointer `fptr` for a function `int square(int x)`?",
                "options": [
                    "int (*fptr)(int);",
                    "int *fptr(int);",
                    "int fptr(*int);",
                    "void (*fptr)(int);"
                ],
                "answer": "int (*fptr)(int);",
            },
            {
                "question": "Why are parentheses mandatory around `(*fptr)` in `int (*fptr)(int, int)`?",
                "options": [
                    "Without parentheses, it would be treated as a function declaration returning an int* pointer",
                    "Without parentheses, the C preprocessor deletes the variable",
                    "Parentheses are needed to allocate heap memory",
                    "Without parentheses, parameters are converted to float"
                ],
                "answer": "Without parentheses, it would be treated as a function declaration returning an int* pointer",
            },
            {
                "question": "Which of the following operations CANNOT be performed on a function pointer in C?",
                "options": [
                    "Pointer arithmetic (e.g. fptr++)",
                    "Passing as callback argument to another function",
                    "Storing inside an array of function pointers",
                    "Assigning the address of a matching function signature"
                ],
                "answer": "Pointer arithmetic (e.g. fptr++)",
            },
            {
                "question": "What is a major application of function pointers in C programming?",
                "options": [
                    "Implementing callback functions and event-driven programming",
                    "Increasing stack frame memory capacity",
                    "Automatically fixing memory leak errors",
                    "Compiling C source code into HTML"
                ],
                "answer": "Implementing callback functions and event-driven programming",
            },
        ],
        "theory": {
            "definition": "A function pointer is a pointer that stores the address of an executable function in the code segment, allowing indirect and dynamic function calls.",
            "why": "Function pointers enable callback functions, event-driven programming, structure-based member function emulation, and dispatch tables.",
            "rules": [
                "Syntax: return_type (*pointer_name)(parameter_types);.",
                "Signature Matching: Function pointer signature (return type and parameter list) must match the target function.",
                "Initialization: fptr = &add; or fptr = add; (function name acts as constant function pointer).",
                "No Pointer Arithmetic: Function pointers cannot be incremented (fptr++) or decremented.",
                "Array of Function Pointers: int (*farr[])(int, int) = {add, sub, mul}; creates a function dispatch table.",
                "Callbacks: Passing function pointers as function arguments enables runtime operation selection."
            ],
            "examples": [
                "#include <stdio.h>\n\nint add(int a, int b) { return a + b; }\nint main(void) {\n    int (*fp)(int, int) = add;\n    printf(\"%d\\n\", fp(10, 5));\n    return 0;\n}"
            ],
        },
    },

    28: {
        "concept": "A structure (struct) in C is a user-defined data type that groups related variables of different data types under a single name. Members are accessed via the dot operator (.) for variables or the arrow operator (->) for structure pointers. Initialization forms include initializer lists, designated initializers (.member = val), and copying (s2 = s1 shallow copy). Structure size includes compiler padding bytes for alignment requirements unless #pragma pack or __attribute__((packed)) is used. Concepts include nested structures, self-referential structures (linked lists/trees), and bit fields.",
        "syntax": "struct Student {\n    char name[50];\n    int age;\n    float grade;\n};\nstruct Student s1 = {\"Rahul\", 20, 18.5};          // Initializer list\nstruct Student s2 = {.age = 18, .name = \"Vikas\"}; // Designated initializer (C99)\nstruct Student *ptr = &s1;\nprintf(\"%s\", ptr->name);                         // Arrow operator for pointers",
        "example": {
            "code": "#include <stdio.h>\n\nstruct Student {\n    int id;\n    float grade;\n};\n\nint main(void) {\n    struct Student s1 = {1, 92.5};\n    struct Student *ptr = &s1;\n\n    printf(\"Dot access - ID: %d, Grade: %.1f\\n\", s1.id, s1.grade);\n    printf(\"Arrow access - ID: %d, Grade: %.1f\\n\", ptr->id, ptr->grade);\n    return 0;\n}",
            "output": "Dot access - ID: 1, Grade: 92.5\nArrow access - ID: 1, Grade: 92.5",
            "explanation": "struct Student groups id and grade. Members are accessed directly using s1.id (dot operator) or via pointer using ptr->id (arrow operator).",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nstruct Point { int x, y; };\n\nint main(void) {\n    struct Point p = {10, 20};\n    struct Point *ptr = &p;\n    printf(\"%d %d\", p._____, ptr_____y);\n    return 0;\n}",
            "answers": ["x", "->"],
            "options": ["x", "->", ".", "*", "y", "&"],
        },
        "compiler": {
            "title": "C Structures Sandbox",
            "question": "Complete the structure declaration and arrow operator pointer access.",
            "starter_code": "#include <stdio.h>\n\n_____ Student {\n    int age;\n    float marks;\n};\n\nint main(void) {\n    struct Student s = {20, 85.5};\n    struct Student *ptr = &s;\n    printf(\"Age: %d\\n\", ptr_____age);\n    return 0;\n}",
            "options": ["struct", "->", ".", "union"],
        },
        "skill_exa_test": [
            {
                "question": "Which operator is used to access structure members through a structure pointer (`struct Node *ptr`)?",
                "options": [
                    "Arrow operator (->)",
                    "Dot operator (.)",
                    "Dereference asterisk (*)",
                    "Address operator (&)"
                ],
                "answer": "Arrow operator (->)",
            },
            {
                "question": "Introduced in the C99 standard, what is the syntax feature called that allows initializing structure members out of order by member name (e.g. `struct Student s = {.age = 18, .name = \"Vikas\"};`)?",
                "options": [
                    "Designated Initializers",
                    "Anonymous Initializers",
                    "Typedef Initializers",
                    "Static Parameter Binding"
                ],
                "answer": "Designated Initializers",
            },
            {
                "question": "Why is `sizeof(struct S)` often larger than the sum of the byte sizes of its individual members?",
                "options": [
                    "The compiler inserts padding bytes between or after members for memory alignment requirements",
                    "Structures automatically allocate dynamic heap headers",
                    "Member arrays double in size inside structures",
                    "Pointers inside structures take 32 bytes each"
                ],
                "answer": "The compiler inserts padding bytes between or after members for memory alignment requirements",
            },
            {
                "question": "What is a self-referential structure in C?",
                "options": [
                    "A structure that contains a pointer member pointing to an object of the same structure type",
                    "A structure that recursively embeds a copy of itself as a direct variable member",
                    "A structure that can only be declared inside main()",
                    "A structure that cannot contain integer variables"
                ],
                "answer": "A structure that contains a pointer member pointing to an object of the same structure type",
            },
            {
                "question": "What type of copy is performed when assigning one structure variable to another (`s2 = s1;`) if `s1` contains dynamic memory pointers allocated via malloc()?",
                "options": [
                    "Shallow copy (only the pointer address is copied, sharing the dynamic resource)",
                    "Deep copy (dynamic memory resources are duplicated)",
                    "Compiler error",
                    "Automatic garbage collection copy"
                ],
                "answer": "Shallow copy (only the pointer address is copied, sharing the dynamic resource)",
            },
        ],
        "theory": {
            "definition": "A structure in C is a user-defined data type that groups related variables of different data types under a single name.",
            "why": "Structures model real-world entities (students, employees, dates) and form the foundation for data structures like linked lists, trees, and graphs.",
            "rules": [
                "Member Access: Use . for structure variables, -> for structure pointers.",
                "Initialization: Initializer lists {v1, v2}, designated initializers {.member = val}, or assignment s2 = s1.",
                "Memory Padding: Compilers insert alignment padding; use #pragma pack(1) or __attribute__((packed)) to remove padding.",
                "Pass to Functions: Pass by pointer void func(struct A *ptr) to avoid copying large data blocks.",
                "typedef Alias: typedef struct { int x; } Point; creates a concise type name.",
                "Bit Fields: Specify exact bit lengths for members (e.g. unsigned int flag : 1;)."
            ],
            "examples": [
                "#include <stdio.h>\n\nstruct Student { int age; float marks; };\nint main(void) {\n    struct Student s = {20, 85.5};\n    struct Student *p = &s;\n    printf(\"%d %.1f\\n\", p->age, p->marks);\n    return 0;\n}"
            ],
        },
    },

    29: {
        "concept": "A union in C is a user-defined data type that allows storing different data types in the same memory location. Unlike structures, all union members share the exact same memory space. The total size of a union is determined by the size of its largest member. Writing to one union member overwrites the value of previously written members. Unions save memory in hardware registers, variant data records, anonymous nested unions, and resource-constrained environments.",
        "syntax": "union Student {\n    int rollNo;\n    float height;\n    char firstLetter;\n};\nunion Student data;\ndata.rollNo = 21;    // Valid\ndata.height = 5.2;   // Overwrites rollNo in shared memory!",
        "example": {
            "code": "#include <stdio.h>\n\nunion Data {\n    int i;\n    float f;\n    char str[20];\n};\n\nint main(void) {\n    union Data data;\n    printf(\"Size of union Data: %lu bytes\\n\", sizeof(data));\n\n    data.i = 10;\n    printf(\"data.i: %d\\n\", data.i);\n\n    data.f = 220.5;\n    printf(\"data.f: %.1f\\n\", data.f);\n    return 0;\n}",
            "output": "Size of union Data: 20 bytes\ndata.i: 10\ndata.f: 220.5",
            "explanation": "union Data contains int, float, and char str[20]. Total size is 20 bytes (size of largest member str[20]). Updating data.f overwrites data.i because all members share the same memory location.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\n_____ Item {\n    int id;\n    float price;\n};\n\nint main(void) {\n    union Item it;\n    printf(\"Size: %lu\", sizeof(it)); // Size equals sizeof(float) i.e. 4\n    return 0;\n}",
            "answers": ["union"],
            "options": ["union", "struct", "enum", "typedef"],
        },
        "compiler": {
            "title": "C Unions Sandbox",
            "question": "Complete the union declaration to verify shared memory allocation.",
            "starter_code": "#include <stdio.h>\n\n_____ Student {\n    int rollNo;\n    float height;\n};\n\nint main(void) {\n    union Student s;\n    s.rollNo = 21;\n    printf(\"Roll: %d\\n\", s.rollNo);\n    return 0;\n}",
            "options": ["union", "struct", "enum", "class"],
        },
        "skill_exa_test": [
            {
                "question": "What is the fundamental difference between a `struct` and a `union` in C?",
                "options": [
                    "In a struct, each member has its own distinct memory location; in a union, all members share the same memory location",
                    "Unions cannot contain integer members",
                    "Structures share memory space while unions allocate individual member blocks",
                    "Unions can only be used with function pointers"
                ],
                "answer": "In a struct, each member has its own distinct memory location; in a union, all members share the same memory location",
            },
            {
                "question": "How is the total memory size of a `union` variable calculated?",
                "options": [
                    "It is equal to the size of its largest member",
                    "It is equal to the sum of the sizes of all its members",
                    "It is always fixed at 8 bytes regardless of members",
                    "It is calculated as the average size of its members"
                ],
                "answer": "It is equal to the size of its largest member",
            },
            {
                "question": "Given `union Test { int x; char arr[8]; int y; };` (assuming sizeof(int) == 4, sizeof(char) == 1), what is sizeof(union Test)?",
                "options": ["8 bytes", "16 bytes", "4 bytes", "12 bytes"],
                "answer": "8 bytes",
            },
            {
                "question": "What happens when a value is assigned to a union member after another member was previously set?",
                "options": [
                    "The new assignment overwrites the shared memory space, invalidating the previous member's value",
                    "The previous member's value is stored in a backup stack frame",
                    "The compiler throws a type mismatch error",
                    "Both values are concatenated in memory"
                ],
                "answer": "The new assignment overwrites the shared memory space, invalidating the previous member's value",
            },
            {
                "question": "What is an anonymous union in C?",
                "options": [
                    "A union declared without a type name inside a structure, allowing direct access to its members without a union variable name",
                    "A union that cannot be initialized",
                    "A union defined in external assembly files",
                    "A union with zero members"
                ],
                "answer": "A union declared without a type name inside a structure, allowing direct access to its members without a union variable name",
            },
        ],
        "theory": {
            "definition": "A union in C is a user-defined data type that enables storing different data types in the same shared memory location.",
            "why": "Unions minimize memory footprint in memory-constrained systems, hardware register modeling, and variant data structures.",
            "rules": [
                "Shared Memory: All members start at the same base memory address.",
                "Single Active Member: Only one member holds a valid value at any given time.",
                "Size Calculation: sizeof(union) equals the size of its largest member.",
                "Syntax: union UnionName { data_type member1; ... };.",
                "Anonymous Unions: Nested unions without variable names grant direct member access."
            ],
            "examples": [
                "#include <stdio.h>\n\nunion Data { int i; float f; };\nint main(void) {\n    union Data d;\n    d.i = 100;\n    printf(\"Int: %d, Size: %lu\\n\", d.i, sizeof(d));\n    return 0;\n}"
            ],
        },
    },

    30: {
        "concept": "An enumeration (enum) in C is a user-defined data type that assigns user-friendly named identifiers to integer constants. By default, the first constant is assigned 0 and each subsequent constant increments by 1. Values can also be assigned manually (enum enm { a = 3, b = 2, c } where c becomes 2 + 1 = 3). Enums enhance code readability, maintainability, and safety over raw magic numbers in state machines, error codes, menu options, and permission flags. Typedef can create concise enum type aliases.",
        "syntax": "enum direction { EAST, NORTH, WEST, SOUTH }; // EAST=0, NORTH=1, WEST=2, SOUTH=3\nenum direction dir = NORTH;\ntypedef enum { READ = 1, WRITE = 2, EXEC = 4 } Permission;",
        "example": {
            "code": "#include <stdio.h>\n\nenum Day { SUN, MON, TUE, WED, THU, FRI, SAT };\n\nint main(void) {\n    enum Day today = WED;\n    printf(\"Day integer value: %d\\n\", today);\n    return 0;\n}",
            "output": "Day integer value: 3",
            "explanation": "enum Day defines 7 constants. SUN is automatically 0, MON is 1, TUE is 2, and WED is 3.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\n_____ Status { SUCCESS, ERROR, PENDING };\n\nint main(void) {\n    enum Status s = SUCCESS;\n    printf(\"%d\", s);\n    return 0;\n}",
            "answers": ["enum"],
            "options": ["enum", "struct", "union", "typedef"],
        },
        "compiler": {
            "title": "C Enum Sandbox",
            "question": "Complete the enum declaration and variable assignment to print 1 for NORTH.",
            "starter_code": "#include <stdio.h>\n\n_____ direction { EAST, NORTH, WEST, SOUTH };\n\nint main(void) {\n    enum direction dir = NORTH;\n    printf(\"Dir: %d\\n\", dir);\n    return 0;\n}",
            "options": ["enum", "struct", "union", "int"],
        },
        "skill_exa_test": [
            {
                "question": "What default integer value is assigned to the first identifier in a C enum definition if no manual value is specified?",
                "options": ["0", "1", "-1", "Garbage value"],
                "answer": "0",
            },
            {
                "question": "Given `enum Alpha { A = 3, B = 2, C };`, what integer value is automatically assigned to C?",
                "options": [
                    "3 (previous value 2 + 1)",
                    "2",
                    "4",
                    "0"
                ],
                "answer": "3 (previous value 2 + 1)",
            },
            {
                "question": "What is the typical memory size of an enum variable in C?",
                "options": [
                    "Same as integer size (typically 4 bytes)",
                    "1 byte",
                    "Depends on the number of letters in enum constant names",
                    "Enums do not occupy memory"
                ],
                "answer": "Same as integer size (typically 4 bytes)",
            },
            {
                "question": "Why are enums preferred over raw numeric magic constants in programming?",
                "options": [
                    "Enums improve code readability, maintainability, and self-documentation",
                    "Enums execute twice as fast as integer variables",
                    "Enums automatically allocate heap memory",
                    "Enums prevent preprocessor macro compilation"
                ],
                "answer": "Enums improve code readability, maintainability, and self-documentation",
            },
            {
                "question": "How can typedef be combined with enum to simplify variable declarations?",
                "options": [
                    "By defining a type alias so the 'enum' keyword does not need to be repeated (e.g., `typedef enum { EAST, NORTH } Direction; Direction d = NORTH;`)",
                    "By converting enum values to string literals automatically",
                    "By forcing enums to use 1-byte storage",
                    "By hiding enum constant names from global scope"
                ],
                "answer": "By defining a type alias so the 'enum' keyword does not need to be repeated (e.g., `typedef enum { EAST, NORTH } Direction; Direction d = NORTH;`)",
            },
        ],
        "theory": {
            "definition": "An enumeration (enum) is a user-defined data type in C that assigns user-friendly named identifiers to integer constants.",
            "why": "Enums replace magic numbers with descriptive names in state machines, error codes, flags, user choices, and file permissions.",
            "rules": [
                "Default Auto-Increment: First constant is 0; subsequent constants increment by 1.",
                "Manual Values: enum { A = 10, B = 20, C } sets C = 21.",
                "Uniqueness Scope: Enum constant names must be unique within the same global/local scope.",
                "Memory Size: Usually stored as int (4 bytes).",
                "Typedef Usage: typedef enum { ... } AliasName; enables concise declarations."
            ],
            "examples": [
                "#include <stdio.h>\n\ntypedef enum { LOW, MED, HIGH } Level;\nint main(void) {\n    Level l = HIGH;\n    printf(\"Level: %d\\n\", l);\n    return 0;\n}"
            ],
        },
    },

    31: {
        "concept": "File handling in C enables creating, opening, reading, writing, seeking, and closing files using FILE stream pointers provided by <stdio.h>. Functions like fopen(), fclose(), fputs(), fprintf(), and fseek() handle persistent disk I/O.",
        "syntax": "FILE *fptr = fopen(\"filename.txt\", \"mode\");\nif (fptr == NULL) { /* handle error */ }\nfputs(\"text\", fptr);\nfseek(fptr, offset, SEEK_SET);\nfclose(fptr);",
        "example": {
            "code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    FILE *fptr = fopen(\"file.txt\", \"w+\");\n    if (fptr == NULL) {\n        printf(\"The file is not opened.\\n\");\n        return 1;\n    }\n    printf(\"The file is created Successfully.\\n\");\n    fputs(\"GeeksforGeeks-A Computer Science Portal for Geeks\\n\", fptr);\n    \n    fseek(fptr, -6, SEEK_END);\n    fputs(\"Geeks\", fptr);\n    \n    fclose(fptr);\n    printf(\"Data successfully written in file file.txt\\n\");\n    printf(\"The file is now closed.\\n\");\n    return 0;\n}",
            "output": "The file is created Successfully.\nData successfully written in file file.txt\nThe file is now closed.",
            "explanation": "Opens file.txt in 'w+' mode, writes text, positions file pointer 6 bytes before the end with fseek(), overwrites text, and closes stream with fclose().",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nint main(void) {\n    FILE *fptr = _____(\"data.txt\", \"w\");\n    if (fptr == _____) {\n        printf(\"Error opening file\\n\");\n    }\n    _____(fptr);\n    return 0;\n}",
            "answers": ["fopen", "NULL", "fclose"],
            "options": ["fopen", "NULL", "fclose", "open", "EOF", "close"],
        },
        "compiler": {
            "title": "File Creation and Access Mode Sandbox",
            "question": "Select the correct mode for fopen to write text to a file, creating it if it does not exist.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    FILE *fp = fopen(\"output.txt\", _____);\n    if (fp != NULL) {\n        fputs(\"Writing data to file\\n\", fp);\n        fclose(fp);\n        printf(\"Success\\n\");\n    }\n    return 0;\n}",
            "options": ["\"w\"", "\"r\"", "\"rb\"", "\"read\""],
        },
        "skill_exa_test": [
            {
                "question": "What is returned by fopen() if a file cannot be opened due to an invalid path or missing access permissions?",
                "options": ["NULL", "EOF", "-1", "0"],
                "answer": "NULL",
            },
            {
                "question": "Which access mode opens a text file for writing, overwriting existing contents or creating a new file if it does not exist?",
                "options": ["\"w\"", "\"r\"", "\"a\"", "\"r+\""],
                "answer": "\"w\"",
            },
            {
                "question": "What is the primary difference between file opening access modes \"a\" and \"w\"?",
                "options": [
                    "\"a\" appends data to the end of the file without deleting existing contents, whereas \"w\" overwrites existing contents",
                    "\"a\" opens the file in read-only mode, whereas \"w\" opens it in binary mode",
                    "\"a\" deletes the file, whereas \"w\" creates a directory",
                    "\"a\" requires root permissions, whereas \"w\" does not"
                ],
                "answer": "\"a\" appends data to the end of the file without deleting existing contents, whereas \"w\" overwrites existing contents",
            },
            {
                "question": "Which standard function is used to manually position the file pointer to a specific location in an open file?",
                "options": ["fseek()", "ftell()", "rewind()", "fgetc()"],
                "answer": "fseek()",
            },
            {
                "question": "What effect does calling rewind(fptr) have on an open file stream?",
                "options": [
                    "Resets the file pointer to the beginning of the file (equivalent to fseek(fptr, 0, SEEK_SET))",
                    "Closes and deletes the file from disk",
                    "Flushes the input buffer into memory",
                    "Returns the current byte position in file"
                ],
                "answer": "Resets the file pointer to the beginning of the file (equivalent to fseek(fptr, 0, SEEK_SET))",
            },
        ],
        "theory": {
            "definition": "File handling in C is the process of creating, opening, reading, writing, seeking, and closing persistent files stored on secondary storage.",
            "why": "Variables in RAM are lost when a program terminates; files provide persistent data storage across program executions.",
            "rules": [
                "Always check if fopen() returned NULL before performing file operations.",
                "Access modes: \"r\" (read), \"w\" (write/overwrite), \"a\" (append), \"r+\" (read/write existing), \"w+\" (read/write overwrite), \"a+\" (read/append).",
                "Binary modes append 'b' to the mode string (e.g. \"rb\", \"wb\", \"ab\").",
                "Always close files with fclose(fptr) to flush memory buffers and release OS file handles.",
                "Function fseek(fptr, offset, pos) positions pointer using SEEK_SET, SEEK_CUR, or SEEK_END."
            ],
            "examples": [
                "#include <stdio.h>\nint main(void) {\n    FILE *fp = fopen(\"notes.txt\", \"w\");\n    if (fp) { fputs(\"Hello C File Handling\\n\", fp); fclose(fp); }\n    return 0;\n}"
            ],
        },
    },

    32: {
        "concept": "Reading a file in C involves opening a file stream in read mode (\"r\" or \"rb\") and using functions suited to the data format: fgetc() for character-by-character, fgets() for line-by-line, fscanf() for formatted text parsing, and fread() for raw binary memory block reading.",
        "syntax": "FILE *fp = fopen(\"file.txt\", \"r\");\nchar buffer[100];\nwhile (fgets(buffer, sizeof(buffer), fp) != NULL) {\n    printf(\"%s\", buffer);\n}\nfclose(fp);",
        "example": {
            "code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    FILE *fp = fopen(\"file.txt\", \"w+\");\n    if (fp == NULL) {\n        printf(\"Unable to open file.\\n\");\n        return 1;\n    }\n    fputs(\"Raman 12\\nKunal 25\\nVikas 6\\n\", fp);\n    rewind(fp);\n\n    char name[50];\n    int age;\n\n    printf(\"Reading structured records using fscanf:\\n\");\n    while (fscanf(fp, \"%s %d\", name, &age) == 2) {\n        printf(\"Name: %s, Age: %d\\n\", name, age);\n    }\n\n    fclose(fp);\n    return 0;\n}",
            "output": "Reading structured records using fscanf:\nName: Raman, Age: 12\nName: Kunal, Age: 25\nName: Vikas, Age: 6",
            "explanation": "Writes formatted text lines into file.txt, rewinds stream to beginning, and reads formatted string and integer variables line-by-line using fscanf() until EOF.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nint main(void) {\n    FILE *fp = fopen(\"input.txt\", \"r\");\n    char buffer[100];\n    while (_____(buffer, sizeof(buffer), fp) != _____) {\n        printf(\"%s\", buffer);\n    }\n    fclose(fp);\n    return 0;\n}",
            "answers": ["fgets", "NULL"],
            "options": ["fgets", "NULL", "fputs", "EOF", "fscanf", "0"],
        },
        "compiler": {
            "title": "Reading File Line by Line Sandbox",
            "question": "Choose the function best suited for reading text lines including spaces into a string buffer safely.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    FILE *fp = fopen(\"sample.txt\", \"r\");\n    char line[100];\n    if (fp != NULL) {\n        while (_____(line, sizeof(line), fp)) {\n            printf(\"%s\", line);\n        }\n        fclose(fp);\n    }\n    return 0;\n}",
            "options": ["fgets", "fgetc", "fwrite", "fputw"],
        },
        "skill_exa_test": [
            {
                "question": "Which C file reading function inputs an entire text line up to a newline character or buffer size limit into a character array?",
                "options": ["fgets()", "fgetc()", "fread()", "fputc()"],
                "answer": "fgets()",
            },
            {
                "question": "What does fscanf(fp, \"%s %d\", name, &age) return when it successfully matches and reads both a string and an integer?",
                "options": ["2", "1", "EOF", "0"],
                "answer": "2",
            },
            {
                "question": "Why is fgets() preferred over fscanf() with %s when reading standard text lines?",
                "options": [
                    "fgets() reads spaces within a line and prevents buffer overflows via buffer size parameters",
                    "fgets() automatically parses integers into double floats",
                    "fscanf() deletes the file after reading",
                    "fgets() only works on binary files"
                ],
                "answer": "fgets() reads spaces within a line and prevents buffer overflows via buffer size parameters",
            },
            {
                "question": "Which reading function reads raw byte blocks from binary files directly into memory addresses?",
                "options": ["fread()", "fgets()", "fscanf()", "fgetc()"],
                "answer": "fread()",
            },
            {
                "question": "What does fgetc(fp) return when the end of the file is reached or a read error occurs?",
                "options": ["EOF", "NULL", "0", "\\0"],
                "answer": "EOF",
            },
        ],
        "theory": {
            "definition": "Reading a file in C is retrieving stored textual or binary data from secondary memory into program RAM variables using standard library input stream functions.",
            "why": "Enables reading persistent configuration settings, logs, structured databases, text documents, and user inputs saved across sessions.",
            "rules": [
                "File must be opened in \"r\" (text read) or \"rb\" (binary read) mode before calling read functions.",
                "fgetc(fp) reads 1 character at a time; returns int (character byte or EOF).",
                "fgets(buffer, size, fp) reads up to size-1 characters including newline \\n, appending null terminator \\0. Returns NULL on EOF/error.",
                "fscanf(fp, format, ...) reads formatted tokens; returns number of successfully converted arguments.",
                "fread(ptr, size, count, fp) reads count items of size bytes each into memory pointed by ptr."
            ],
            "examples": [
                "#include <stdio.h>\nint main(void) {\n    FILE *fp = fopen(\"log.txt\", \"r\");\n    char buf[256];\n    if (fp) { while (fgets(buf, 256, fp)) printf(\"%s\", buf); fclose(fp); }\n    return 0;\n}"
            ],
        },
    },

    33: {
        "concept": "fwrite() and fread() allow saving entire C struct instances directly to binary files (.dat, .bin) and reading them back into memory without manual field-by-field conversion. Structures are stored in raw binary memory representation preserving field alignment.",
        "syntax": "// Write struct\nFILE *fp = fopen(\"student.dat\", \"wb\");\nfwrite(&s1, sizeof(struct Student), 1, fp);\nfclose(fp);\n\n// Read struct\nfp = fopen(\"student.dat\", \"rb\");\nfread(&s2, sizeof(struct Student), 1, fp);\nfclose(fp);",
        "example": {
            "code": "#include <stdio.h>\n#include <stdlib.h>\n\nstruct Student {\n    int id;\n    char name[20];\n    float marks;\n};\n\nint main(void) {\n    struct Student s1 = {101, \"Rahul\", 89.5f};\n    struct Student s2;\n\n    FILE *fp = fopen(\"student.dat\", \"wb\");\n    if (fp == NULL) {\n        printf(\"Error opening file for writing.\\n\");\n        return 1;\n    }\n    fwrite(&s1, sizeof(struct Student), 1, fp);\n    fclose(fp);\n\n    fp = fopen(\"student.dat\", \"rb\");\n    if (fp == NULL) {\n        printf(\"Error opening file for reading.\\n\");\n        return 1;\n    }\n    fread(&s2, sizeof(struct Student), 1, fp);\n    fclose(fp);\n\n    printf(\"ID: %d\\n\", s2.id);\n    printf(\"Name: %s\\n\", s2.name);\n    printf(\"Marks: %.1f\\n\", s2.marks);\n    return 0;\n}",
            "output": "ID: 101\nName: Rahul\nMarks: 89.5",
            "explanation": "Serializes structure s1 to student.dat using fwrite() in binary write mode ('wb'), then deserializes bytes back into s2 using fread() in binary read mode ('rb').",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nstruct Student { int id; char name[20]; };\n\nint main(void) {\n    struct Student s1 = {1, \"Alice\"};\n    FILE *fp = fopen(\"data.bin\", \"_____\");\n    _____( &s1, sizeof(struct Student), 1, fp);\n    fclose(fp);\n    return 0;\n}",
            "answers": ["wb", "fwrite"],
            "options": ["wb", "fwrite", "r", "fread", "fputs", "ab"],
        },
        "compiler": {
            "title": "Binary Structure Serialization Sandbox",
            "question": "Select the correct mode and function to read a binary struct block from a file stream.",
            "starter_code": "#include <stdio.h>\n\nstruct Item { int code; float price; };\n\nint main(void) {\n    struct Item item;\n    FILE *fp = fopen(\"items.bin\", _____ );\n    if (fp != NULL) {\n        _____(&item, sizeof(struct Item), 1, fp);\n        fclose(fp);\n    }\n    return 0;\n}",
            "options": ["\"rb\", fread", "\"w\", fwrite", "\"r\", fgets", "\"wb\", fputs"],
        },
        "skill_exa_test": [
            {
                "question": "What parameters are passed in order to fwrite(&s, sizeof(struct Student), 1, fp)?",
                "options": [
                    "Address of struct memory, size of struct in bytes, number of elements, FILE pointer",
                    "FILE pointer, total bytes, format string, struct pointer",
                    "Struct pointer, line count, delimiter string, mode",
                    "Filename string, memory offset, buffer length, flags"
                ],
                "answer": "Address of struct memory, size of struct in bytes, number of elements, FILE pointer",
            },
            {
                "question": "Why must files be opened in binary modes (\"wb\", \"rb\", \"ab\") when reading or writing C structs using fwrite()/fread()?",
                "options": [
                    "To prevent special text translation of newline characters from corrupting raw struct byte data",
                    "Because text modes only allow integer numbers",
                    "Binary modes compress struct memory by 50%",
                    "Text modes do not support struct pointers"
                ],
                "answer": "To prevent special text translation of newline characters from corrupting raw struct byte data",
            },
            {
                "question": "What is returned by fread(&s, sizeof(struct Student), 1, fp) upon successful read of 1 struct object?",
                "options": ["1", "sizeof(struct Student)", "EOF", "0"],
                "answer": "1",
            },
            {
                "question": "How can an array of struct records be written to a binary file in a single fwrite() call?",
                "options": [
                    "fwrite(people, sizeof(struct person), count, fp);",
                    "fwrite(&people, count, sizeof(struct person), \"wb\");",
                    "fputs(people, fp);",
                    "fprintf(fp, \"%struct\", people);"
                ],
                "answer": "fwrite(people, sizeof(struct person), count, fp);",
            },
            {
                "question": "What happens if a struct containing raw dynamic pointers (e.g. char *name) is written directly using fwrite()?",
                "options": [
                    "Only pointer address numbers are written, rendering the saved file unusable in future runs when virtual addresses change",
                    "The pointer target string is automatically deeply serialized into the file",
                    "The compiler raises a static syntax error",
                    "The file is deleted automatically"
                ],
                "answer": "Only pointer address numbers are written, rendering the saved file unusable in future runs when virtual addresses change",
            },
        ],
        "theory": {
            "definition": "Binary structure serialization in C writes or reads exact struct memory blocks directly to/from disk using fwrite() and fread().",
            "why": "Provides high-speed file I/O for complex records, preserving raw binary layout without manual text formatting/parsing conversions.",
            "rules": [
                "Files must be opened in binary modes (\"wb\", \"rb\", \"ab\", \"wb+\", \"rb+\").",
                "fwrite(ptr, size, count, fp) writes count elements of size bytes each from RAM address ptr.",
                "fread(ptr, size, count, fp) reads count elements of size bytes each into RAM address ptr.",
                "Struct padding depends on compiler architecture; binary struct files may differ across architectures.",
                "Avoid writing structs containing raw pointer members directly; save pointed-to data instead."
            ],
            "examples": [
                "#include <stdio.h>\nstruct User { int id; char name[20]; };\nint main(void) {\n    struct User u = {1, \"Alice\"};\n    FILE *fp = fopen(\"user.dat\", \"wb\");\n    fwrite(&u, sizeof(u), 1, fp);\n    fclose(fp);\n    return 0;\n}"
            ],
        },
    },

    34: {
        "concept": "EOF is a macro constant (typically -1) returned by stream functions when reaching end-of-file or experiencing a read error. The getc() function reads single characters. Because getc() returns EOF for BOTH actual end-of-file AND errors, feof(fptr) and ferror(fptr) distinguish true end-of-file from file I/O failure.",
        "syntax": "int ch = getc(fp);\nif (ch == EOF) {\n    if (feof(fp)) {\n        printf(\"End of file reached.\\n\");\n    } else if (ferror(fp)) {\n        printf(\"File read error occurred.\\n\");\n    }\n}",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    FILE *fptr = fopen(\"sample.txt\", \"w\");\n    if (fptr == NULL) {\n        printf(\"Error opening file.\\n\");\n        return 1;\n    }\n\n    int ch = getc(fptr);\n\n    if (ch == EOF) {\n        if (feof(fptr)) {\n            printf(\"End of File reached.\\n\");\n        } else {\n            printf(\"Unable to Read (File error or invalid mode).\\n\");\n        }\n    } else {\n        printf(\"Read Character: %c\\n\", (char)ch);\n    }\n\n    fclose(fptr);\n    return 0;\n}",
            "output": "Unable to Read (File error or invalid mode).",
            "explanation": "Opens a file in write-only mode ('w'). Calling getc() returns EOF. feof(fptr) returns 0 because it was a read error on a write-only stream rather than genuine end-of-file.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nint main(void) {\n    FILE *fp = fopen(\"data.txt\", \"r\");\n    int ch = fgetc(fp);\n    if (ch == _____) {\n        if (_____(fp)) printf(\"End of file reached\\n\");\n    }\n    fclose(fp);\n    return 0;\n}",
            "answers": ["EOF", "feof"],
            "options": ["EOF", "feof", "NULL", "ferror", "0", "SEEK_END"],
        },
        "compiler": {
            "title": "EOF and feof Distinction Sandbox",
            "question": "Check for true End-of-File condition when getc returns EOF.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    FILE *fp = fopen(\"data.txt\", \"r\");\n    if (fp != NULL) {\n        while (getc(fp) != EOF);\n        if (_____(fp)) {\n            printf(\"Reached EOF successfully\\n\");\n        }\n        fclose(fp);\n    }\n    return 0;\n}",
            "options": ["feof", "ferror", "fclose", "remove"],
        },
        "skill_exa_test": [
            {
                "question": "What integer constant macro defined in <stdio.h> indicates end-of-file or input failure?",
                "options": ["EOF (commonly -1)", "NULL", "ZERO", "END_OF_FILE"],
                "answer": "EOF (commonly -1)",
            },
            {
                "question": "Why should the variable storing the return value of getc() or fgetc() be declared as int rather than char?",
                "options": [
                    "Because EOF is an integer constant (-1), which may not fit or compare correctly if char is unsigned",
                    "Because char uses 4 bytes of stack space",
                    "Because getc() converts characters into double precision floats",
                    "Because C requires all loop variables to be int"
                ],
                "answer": "Because EOF is an integer constant (-1), which may not fit or compare correctly if char is unsigned",
            },
            {
                "question": "Why is comparing getc() == EOF alone insufficient to confirm end-of-file?",
                "options": [
                    "getc() also returns EOF when a file read error occurs (e.g. corrupt media, write-only mode)",
                    "EOF changes value dynamically every millisecond",
                    "getc() deletes the file stream on EOF",
                    "feof() automatically fixes file errors"
                ],
                "answer": "getc() also returns EOF when a file read error occurs (e.g. corrupt media, write-only mode)",
            },
            {
                "question": "What does feof(fptr) return when the end-of-file indicator for the stream has been set?",
                "options": ["A non-zero integer value (true)", "0 (false)", "EOF (-1)", "NULL"],
                "answer": "A non-zero integer value (true)",
            },
            {
                "question": "Which standard C function explicitly checks if an I/O read/write error occurred on a file stream?",
                "options": ["ferror()", "feof()", "fseek()", "ftell()"],
                "answer": "ferror()",
            },
        ],
        "theory": {
            "definition": "EOF, getc(), and feof() are C stdio facilities used to read characters from file streams and test stream termination status.",
            "why": "Prevents infinite loops, prevents reading past valid file limits, and distinguishes genuine end-of-file from read error conditions.",
            "rules": [
                "EOF is defined in <stdio.h> (usually -1).",
                "Store getc() / fgetc() return values in an int variable to preserve EOF value.",
                "feof(fptr) returns non-zero if end-of-file indicator was set by prior read beyond file boundary.",
                "ferror(fptr) returns non-zero if an I/O error occurred on the file stream.",
                "clearerr(fptr) clears both EOF and error flags."
            ],
            "examples": [
                "#include <stdio.h>\nint main(void) {\n    FILE *fp = fopen(\"file.txt\", \"r\");\n    int c;\n    while ((c = fgetc(fp)) != EOF) putchar(c);\n    if (feof(fp)) printf(\"\\nEnd of file.\\n\");\n    fclose(fp);\n    return 0;\n}"
            ],
        },
    },

    35: {
        "concept": "In C, files on disk can be permanently deleted using the standard library function remove() declared in <stdio.h>. It takes a file path string argument and returns 0 on success, or a non-zero integer if the file cannot be deleted.",
        "syntax": "const char *filename = \"temp.txt\";\nif (remove(filename) == 0) {\n    printf(\"File deleted successfully.\\n\");\n} else {\n    printf(\"Error deleting file.\\n\");\n}",
        "example": {
            "code": "#include <stdio.h>\n\nint main(void) {\n    FILE *fp = fopen(\"temp_test.txt\", \"w\");\n    if (fp != NULL) {\n        fputs(\"Temporary data\", fp);\n        fclose(fp); // Close before removing!\n    }\n\n    const char *file = \"temp_test.txt\";\n    if (remove(file) == 0) {\n        printf(\"File deleted successfully.\\n\");\n    } else {\n        printf(\"Error: Unable to delete the file.\\n\");\n    }\n    return 0;\n}",
            "output": "File deleted successfully.",
            "explanation": "Creates a temporary file, closes it with fclose(), and calls remove() to delete the file, checking the return value 0 for success.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nint main(void) {\n    const char *fname = \"log.txt\";\n    if (_____(fname) == _____) {\n        printf(\"File deleted\\n\");\n    }\n    return 0;\n}",
            "answers": ["remove", "0"],
            "options": ["remove", "0", "delete", "EOF", "fclose", "-1"],
        },
        "compiler": {
            "title": "File Removal Sandbox",
            "question": "Select the function to delete a file by path in C.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    if (_____(\"old_data.txt\") == 0) {\n        printf(\"File removed successfully\\n\");\n    }\n    return 0;\n}",
            "options": ["remove", "delete", "unlink_file", "destroy"],
        },
        "skill_exa_test": [
            {
                "question": "Which standard C library function in <stdio.h> is used to delete a file from storage?",
                "options": ["remove()", "delete()", "erase()", "unlink_file()"],
                "answer": "remove()",
            },
            {
                "question": "What is the return value of remove(\"data.txt\") upon successful file deletion?",
                "options": ["0", "1", "EOF", "-1"],
                "answer": "0",
            },
            {
                "question": "What prerequisite MUST be fulfilled before calling remove() on an active file stream in C?",
                "options": [
                    "The file must be closed using fclose() before attempting deletion",
                    "The file must be converted to binary format",
                    "The file pointer must be set to NULL",
                    "The file contents must be zeroed out"
                ],
                "answer": "The file must be closed using fclose() before attempting deletion",
            },
            {
                "question": "Why might remove(\"file.txt\") fail and return a non-zero value?",
                "options": [
                    "The specified file does not exist, path is invalid, or permissions are insufficient",
                    "The file contains integers",
                    "The file extension is .txt",
                    "The file size is less than 1KB"
                ],
                "answer": "The specified file does not exist, path is invalid, or permissions are insufficient",
            },
            {
                "question": "Besides deleting files, what else can remove() delete on POSIX-compliant operating systems if given an empty directory path?",
                "options": [
                    "An empty directory",
                    "System processes",
                    "CPU caches",
                    "RAM swap partitions"
                ],
                "answer": "An empty directory",
            },
        ],
        "theory": {
            "definition": "Deleting a file in C is permanently removing a specified file entry and disk resources from the filesystem using remove().",
            "why": "Essential for cleaning up temporary files, cache buffers, outdated logs, and managing storage space.",
            "rules": [
                "Function prototype: int remove(const char *filename); declared in <stdio.h>.",
                "Returns 0 on success; non-zero integer on failure.",
                "Always close open file pointers with fclose(fptr) prior to calling remove().",
                "Requires appropriate file system permissions."
            ],
            "examples": [
                "#include <stdio.h>\nint main(void) {\n    if (remove(\"cache.tmp\") == 0) {\n        printf(\"Cache cleared.\\n\");\n    }\n    return 0;\n}"
            ],
        },
    },

    36: {
        "concept": "Error handling in C relies on function return values (-1, NULL), return status checks, global variable errno from <errno.h>, diagnostic printing with perror(), string formatting with strerror(), and signaling exit status via exit(EXIT_FAILURE) or exit(EXIT_SUCCESS) from <stdlib.h>.",
        "syntax": "#include <errno.h>\n#include <string.h>\n#include <stdlib.h>\n\nFILE *fp = fopen(\"missing.txt\", \"r\");\nif (fp == NULL) {\n    printf(\"Errno: %d (%s)\\n\", errno, strerror(errno));\n    perror(\"fopen failed\");\n    exit(EXIT_FAILURE);\n}",
        "example": {
            "code": "#include <stdio.h>\n#include <errno.h>\n#include <string.h>\n#include <stdlib.h>\n\nint main(void) {\n    FILE *fp = fopen(\"non_existent_file.txt\", \"r\");\n\n    if (fp == NULL) {\n        printf(\"Value of errno: %d\\n\", errno);\n        printf(\"Error message: %s\\n\", strerror(errno));\n        perror(\"Message from perror\");\n        return EXIT_FAILURE;\n    }\n\n    fclose(fp);\n    return EXIT_SUCCESS;\n}",
            "output": "Value of errno: 2\nError message: No such file or directory\nMessage from perror: No such file or directory",
            "explanation": "Attempts to open a missing file, which returns NULL and sets errno to 2 (ENOENT). Displays numeric errno, human-readable description via strerror(), prints error to stderr via perror(), and returns EXIT_FAILURE.",
        },
        "fill_blanks": {
            "question": "#include <_____.h>\n#include <stdlib.h>\n\nFILE *fp = fopen(\"test.txt\", \"r\");\nif (fp == NULL) {\n    _____(\"fopen failed\");\n    exit(_____);\n}",
            "answers": ["errno", "perror", "EXIT_FAILURE"],
            "options": ["errno", "perror", "EXIT_FAILURE", "stdio", "strerror", "EXIT_SUCCESS"],
        },
        "compiler": {
            "title": "C Error Handling & errno Sandbox",
            "question": "Select the function to convert an integer errno into a descriptive error string.",
            "starter_code": "#include <stdio.h>\n#include <errno.h>\n#include <string.h>\n\nint main(void) {\n    FILE *fp = fopen(\"nonexistent.txt\", \"r\");\n    if (fp == NULL) {\n        printf(\"Error: %s\\n\", _____(errno));\n    }\n    return 0;\n}",
            "options": ["strerror", "perror", "ferror", "clearerr"],
        },
        "skill_exa_test": [
            {
                "question": "Which standard C header file defines the global variable errno and system error constants?",
                "options": ["<errno.h>", "<stdio.h>", "<stdlib.h>", "<string.h>"],
                "answer": "<errno.h>",
            },
            {
                "question": "What does calling perror(\"File Open\") do when a system call fails?",
                "options": [
                    "Prints the user string \"File Open\", followed by a colon and the system error description matching errno to stderr",
                    "Terminates the operating system kernel immediately",
                    "Resets errno back to 0",
                    "Clears the output buffer of stdout"
                ],
                "answer": "Prints the user string \"File Open\", followed by a colon and the system error description matching errno to stderr",
            },
            {
                "question": "What string is returned by strerror(2) on standard POSIX C platforms?",
                "options": [
                    "\"No such file or directory\"",
                    "\"Permission denied\"",
                    "\"Out of memory\"",
                    "\"Division by zero\""
                ],
                "answer": "\"No such file or directory\"",
            },
            {
                "question": "Which standard header file defines the program exit constants EXIT_SUCCESS and EXIT_FAILURE?",
                "options": ["<stdlib.h>", "<errno.h>", "<stdio.h>", "<signal.h>"],
                "answer": "<stdlib.h>",
            },
            {
                "question": "How does standard C signal an error from functions since it lacks built-in try-catch syntax?",
                "options": [
                    "By returning special values (such as NULL, -1, or non-zero status codes) and setting global errno",
                    "By raising C++ throw exceptions automatically",
                    "By stopping CPU clock cycles",
                    "By deleting the output binary file"
                ],
                "answer": "By returning special values (such as NULL, -1, or non-zero status codes) and setting global errno",
            },
        ],
        "theory": {
            "definition": "Error handling in C is detecting, diagnosing, and reacting to runtime failure conditions using function return codes, if-else guards, errno, perror(), strerror(), and program exit status codes.",
            "why": "Prevents undefined behavior, program crashes, resource leaks, and data corruption when hardware I/O, memory allocations, or OS calls fail.",
            "rules": [
                "C lacks try-catch; error checking relies on validating return values after system/library calls.",
                "Header <errno.h> declares extern int errno; which stores error codes (e.g. ENOENT, EACCES, ENOMEM).",
                "perror(const char *s) prints s followed by ': ' and system error text corresponding to errno to stderr.",
                "strerror(int errnum) from <string.h> returns a string pointer describing error number errnum.",
                "<stdlib.h> provides exit(int status) with macros EXIT_SUCCESS (0) and EXIT_FAILURE (non-zero)."
            ],
            "examples": [
                "#include <stdio.h>\n#include <errno.h>\n#include <string.h>\nint main(void) {\n    FILE *fp = fopen(\"invalid.path\", \"r\");\n    if (!fp) printf(\"Err %d: %s\\n\", errno, strerror(errno));\n    return 0;\n}"
            ],
        },
    },

    37: {
        "concept": "The goto error_label pattern is a widely accepted idiom in low-level C programming (such as Linux kernel development and systems software) for single-point resource cleanup and simulating try-catch blocks. Advanced non-local jumps across function boundaries are achieved using setjmp() and longjmp() from <setjmp.h>.",
        "syntax": "int process_file(const char *filename) {\n    FILE *file = fopen(filename, \"r\");\n    if (file == NULL) goto error;\n    // Read & process file data...\n    fclose(file);\n    return 0;\nerror:\n    if (file != NULL) fclose(file);\n    return -1;\n}",
        "example": {
            "code": "#include <stdio.h>\n#include <stdlib.h>\n\nint process_file(const char *path) {\n    FILE *file = fopen(path, \"r\");\n    if (file == NULL) {\n        printf(\"Error opening file\\n\");\n        goto error;\n    }\n\n    char buffer[100];\n    if (fgets(buffer, sizeof(buffer), file) == NULL) {\n        printf(\"Error reading file\\n\");\n        goto error;\n    }\n\n    printf(\"Read data: %s\\n\", buffer);\n    fclose(file);\n    return 0;\n\nerror:\n    if (file != NULL) {\n        fclose(file);\n    }\n    return -1;\n}\n\nint main(void) {\n    process_file(\"nonexistent.txt\");\n    return 0;\n}",
            "output": "Error opening file",
            "explanation": "Simulates a try-catch block using goto error. If fopen() or fgets() fails, execution jumps directly to the error: cleanup block to close file resources safely.",
        },
        "fill_blanks": {
            "question": "FILE *file = fopen(\"data.txt\", \"r\");\nif (file == NULL) {\n    printf(\"Error opening file\\n\");\n    _____ error;\n}\n// Process file...\nerror:\nif (file != NULL) fclose(file);",
            "answers": ["goto"],
            "options": ["goto", "return", "break", "continue", "throw"],
        },
        "compiler": {
            "title": "goto Error Unwinding Sandbox",
            "question": "Select the keyword used in systems C programming to jump directly to a central cleanup block on failure.",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    FILE *fp = fopen(\"input.txt\", \"r\");\n    if (fp == NULL) _____ err_handler;\n    \n    fclose(fp);\n    return 0;\n\nerr_handler:\n    printf(\"Cleanup and exit\\n\");\n    return 1;\n}",
            "options": ["goto", "catch", "raise", "break"],
        },
        "skill_exa_test": [
            {
                "question": "Why is the goto cleanup pattern widely adopted in C systems software like the Linux kernel despite goto being discouraged for general loops?",
                "options": [
                    "It provides a clean, single-point resource unwinding mechanism to prevent code duplication and memory leaks when multiple consecutive allocations fail",
                    "It compiles into multithreaded assembly code automatically",
                    "It replaces the need for header files",
                    "It converts C code into object-oriented C++ classes"
                ],
                "answer": "It provides a clean, single-point resource unwinding mechanism to prevent code duplication and memory leaks when multiple consecutive allocations fail",
            },
            {
                "question": "Which standard C header provides setjmp() and longjmp() for non-local jumps across function boundaries?",
                "options": ["<setjmp.h>", "<errno.h>", "<signal.h>", "<stdlib.h>"],
                "answer": "<setjmp.h>",
            },
            {
                "question": "In a stacked goto cleanup handler block, in what order should resources generally be freed?",
                "options": [
                    "In reverse order of allocation (Last-Allocated, First-Freed)",
                    "In random order",
                    "In alphabetical order by variable name",
                    "All at once without individual labels"
                ],
                "answer": "In reverse order of allocation (Last-Allocated, First-Freed)",
            },
            {
                "question": "What restriction applies to local goto jumps in C?",
                "options": [
                    "A goto statement can only jump to a label within the exact same function body",
                    "A goto statement can jump across different source files",
                    "A goto statement can only jump backward in code",
                    "A goto statement requires root system privileges"
                ],
                "answer": "A goto statement can only jump to a label within the exact same function body",
            },
            {
                "question": "Which of the following is a major risk when using goto without careful design?",
                "options": [
                    "Creating unstructured \"spaghetti code\" that makes program logic difficult to trace and maintain",
                    "Causing hardware CPU clock acceleration",
                    "Forcing the compiler to switch to 16-bit real mode",
                    "Deleting global variable declarations"
                ],
                "answer": "Creating unstructured \"spaghetti code\" that makes program logic difficult to trace and maintain",
            },
        ],
        "theory": {
            "definition": "goto exception handling in C uses forward jumps to specific cleanup labels at the bottom of a function to centralize error recovery, simulate try-catch blocks, and deallocate resources.",
            "why": "Simplifies error handling when acquiring multiple resources (files, sockets, memory blocks) by eliminating nested if-else cascades and duplicate cleanup blocks.",
            "rules": [
                "A goto label must be defined within the same function scope followed by a colon (label:).",
                "Stack cleanup labels in reverse order of allocation so that failure at step N unwinds steps N-1 down to 1.",
                "Always ensure normal non-error execution paths bypass cleanup labels (e.g. using return 0; before labels).",
                "For non-local jumps across function calls, use setjmp() and longjmp() from <setjmp.h>.",
                "Avoid overuse to prevent unmaintainable spaghetti code."
            ],
            "examples": [
                "#include <stdio.h>\n#include <stdlib.h>\nint work(void) {\n    FILE *f = fopen(\"in.txt\", \"r\"); if (!f) goto err_f;\n    void *b = malloc(100); if (!b) goto err_b;\n    free(b); fclose(f); return 0;\nerr_b: fclose(f);\nerr_f: return -1;\n}"
            ],
        },
    },

    38: {
        "concept": "File I/O operations in C can encounter runtime errors such as missing files (ENOENT), permission denied (EACCES), file already exists in 'wx' mode (EEXIST), disk full (ferror), invalid NULL file pointers, or closing failures (fclose returning -1). Standard functions ferror(), feof(), clearerr(), and errno inspect and manage these stream error conditions.",
        "syntax": "FILE *fp = fopen(\"test.txt\", \"wx\"); // Exclusive mode fails if file exists\nif (fp == NULL && errno == EEXIST) {\n    printf(\"File already exists\\n\");\n}\nif (fclose(fp) == -1) {\n    printf(\"File closing error\\n\");\n}",
        "example": {
            "code": "#include <stdio.h>\n#include <stdlib.h>\n#include <errno.h>\n\nint main(void) {\n    FILE *fptr = fopen(\"test.txt\", \"wx\");\n    if (fptr == NULL) {\n        if (errno == EEXIST) {\n            printf(\"File already exists\\n\");\n        } else {\n            perror(\"Error opening file\");\n        }\n        return 1;\n    }\n\n    fprintf(fptr, \"This is a new file.\");\n\n    if (ferror(fptr)) {\n        perror(\"Error writing to file\");\n    }\n\n    if (fclose(fptr) == -1) {\n        printf(\"File closing error\\n\");\n    } else {\n        printf(\"File closed successfully\\n\");\n    }\n    return 0;\n}",
            "output": "File closed successfully",
            "explanation": "Demonstrates opening a file in exclusive write mode ('wx') which sets errno to EEXIST if the file already exists, checks write errors via ferror(), and verifies fclose() return value.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n#include <errno.h>\n\nFILE *fp = fopen(\"data.txt\", \"wx\");\nif (fp == NULL && errno == _____) {\n    printf(\"File already exists\\n\");\n}\nif (fclose(fp) == _____) {\n    printf(\"File closing error\\n\");\n}",
            "answers": ["EEXIST", "-1"],
            "options": ["EEXIST", "-1", "ENOENT", "0", "EOF", "NULL"],
        },
        "compiler": {
            "title": "File Stream Flags & clearerr Sandbox",
            "question": "Select the function used to reset error and EOF indicators for an open FILE pointer.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    FILE *fp = fopen(\"sample.txt\", \"r\");\n    if (fp != NULL) {\n        while (fgetc(fp) != EOF);\n        _____(fp); // Clear EOF indicator\n        if (!feof(fp)) printf(\"EOF flag cleared\\n\");\n        fclose(fp);\n    }\n    return 0;\n}",
            "options": ["clearerr", "ferror", "rewind", "fflush"],
        },
        "skill_exa_test": [
            {
                "question": "What access mode string passed to fopen() creates a new file only if it does not already exist, setting errno to EEXIST on conflict?",
                "options": ["\"wx\"", "\"w\"", "\"a+\"", "\"wb\""],
                "answer": "\"wx\"",
            },
            {
                "question": "What value is returned by fclose() if a file stream fails to close properly?",
                "options": ["-1 (EOF)", "0", "NULL", "1"],
                "answer": "-1 (EOF)",
            },
            {
                "question": "Which standard function checks if an I/O error indicator has been set for a given FILE stream?",
                "options": ["ferror()", "feof()", "clearerr()", "perror()"],
                "answer": "ferror()",
            },
            {
                "question": "What is the purpose of clearerr(FILE *stream) in C?",
                "options": [
                    "It resets both the error indicator and end-of-file (EOF) indicator for the specified stream to zero",
                    "It deletes the file from disk",
                    "It closes and reopens the file in append mode",
                    "It flushes stdout memory"
                ],
                "answer": "It resets both the error indicator and end-of-file (EOF) indicator for the specified stream to zero",
            },
            {
                "question": "Which errno macro indicates that a file opening operation failed because the user lacks read/write permissions?",
                "options": ["EACCES", "ENOENT", "EEXIST", "ENOSPC"],
                "answer": "EACCES",
            },
        ],
        "theory": {
            "definition": "File error handling in C manages file system runtime errors (missing files, permission errors, disk full, existing files) using errno, perror(), ferror(), feof(), clearerr(), and fclose() status checks.",
            "why": "Ensures robust file operations, permitting programs to detect write failures, handle end-of-file boundaries gracefully, and clear error conditions without crashing.",
            "rules": [
                "Always check if fopen() returned NULL before reading/writing.",
                "Mode 'wx' enables exclusive file creation, returning NULL and setting errno = EEXIST if file exists.",
                "Check ferror(fp) after write operations to detect full disks or I/O failure.",
                "Verify fclose(fp) == 0 (returns -1 / EOF on failure).",
                "Use feof(fp) and ferror(fp) separately to distinguish end-of-file from stream errors."
            ],
            "examples": [
                "#include <stdio.h>\n#include <errno.h>\nint main(void) {\n    FILE *fp = fopen(\"out.txt\", \"w\");\n    if (fp) {\n        fputs(\"data\", fp);\n        if (ferror(fp)) perror(\"Write error\");\n        if (fclose(fp) == -1) printf(\"Close err\\n\");\n    }\n    return 0;\n}"
            ],
        },
    },

    39: {
        "concept": "In C, dividing an integer by zero is undefined behavior causing a runtime SIGFPE signal crash. Division by zero can be handled manually via defensive guard clauses (if (b == 0)) or advanced signal handling using signal(SIGFPE, handler), setjmp(), longjmp(), and <fenv.h> exception testing.",
        "syntax": "// Method 1: Defensive check\nif (b == 0) { printf(\"Error: Division by zero\\n\"); }\nelse { res = a / b; }\n\n// Method 2: Signal Handling with <signal.h> & <setjmp.h>\nsignal(SIGFPE, handle_sigfpe);\nif (setjmp(recovery) == 0) { res = a / b; }",
        "example": {
            "code": "#include <stdio.h>\n#include <stdlib.h>\n#include <signal.h>\n#include <setjmp.h>\n\njmp_buf recovery;\n\nvoid handle_divide_by_zero(int sig) {\n    printf(\"Error: Division by zero caught via SIGFPE signal handler!\\n\");\n    signal(SIGFPE, handle_divide_by_zero);\n    longjmp(recovery, 1);\n}\n\nint main(void) {\n    double a = 10, b = 0, res;\n\n    signal(SIGFPE, handle_divide_by_zero);\n\n    if (setjmp(recovery) == 0) {\n        if (b == 0) {\n            raise(SIGFPE); // Trigger floating point exception signal\n        } else {\n            res = a / b;\n            printf(\"Result: %f\\n\", res);\n        }\n    } else {\n        printf(\"Program recovered cleanly from divide-by-zero exception.\\n\");\n    }\n\n    return 0;\n}",
            "output": "Error: Division by zero caught via SIGFPE signal handler!\nProgram recovered cleanly from divide-by-zero exception.",
            "explanation": "Demonstrates catching floating-point exceptions (SIGFPE) using signal() and restoring program execution context using setjmp() and longjmp().",
        },
        "fill_blanks": {
            "question": "#include <signal.h>\n#include <setjmp.h>\n\njmp_buf env;\nvoid handle_sig(int sig) {\n    printf(\"Caught SIGFPE\\n\");\n    _____(env, 1);\n}\n\nint main(void) {\n    signal(_____, handle_sig);\n    if (_____(env) == 0) { /* code */ }\n    return 0;\n}",
            "answers": ["longjmp", "SIGFPE", "setjmp"],
            "options": ["longjmp", "SIGFPE", "setjmp", "raise", "SIGINT", "catch"],
        },
        "compiler": {
            "title": "Divide-by-Zero Defensive Guard Sandbox",
            "question": "Complete the defensive guard clause to prevent division by zero in integer arithmetic.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int num = 50, den = 0;\n    if (den _____ 0) {\n        printf(\"Error: Cannot divide by zero!\\n\");\n    } else {\n        printf(\"Quotient: %d\\n\", num / den);\n    }\n    return 0;\n}",
            "options": ["==", "!=", ">", "<"],
        },
        "skill_exa_test": [
            {
                "question": "Which operating system signal is raised when a program encounters a floating-point error or integer division by zero?",
                "options": ["SIGFPE", "SIGSEGV", "SIGINT", "SIGABRT"],
                "answer": "SIGFPE",
            },
            {
                "question": "Which pair of standard C library functions allows saving and jumping back to a program execution state during signal recovery?",
                "options": [
                    "setjmp() and longjmp()",
                    "fopen() and fclose()",
                    "malloc() and free()",
                    "raise() and kill()"
                ],
                "answer": "setjmp() and longjmp()",
            },
            {
                "question": "How should division-by-zero errors be handled in general user-level C programs?",
                "options": [
                    "By checking if the divisor is equal to 0 (defensive guard clause) before performing division or modulo",
                    "By wrapping division in a try-catch block",
                    "By casting all integers to signed char",
                    "By ignoring zero values"
                ],
                "answer": "By checking if the divisor is equal to 0 (defensive guard clause) before performing division or modulo",
            },
            {
                "question": "Besides division (/), which arithmetic operator in C also causes a crash if the right operand is 0?",
                "options": ["Modulo operator (%)", "Bitwise AND (&)", "Addition (+)", "Bitwise Left Shift (<<)"],
                "answer": "Modulo operator (%)",
            },
            {
                "question": "Which standard C header file provides floating-point exception status functions such as fetestexcept() and feclearexcept()?",
                "options": ["<fenv.h>", "<float.h>", "<math.h>", "<signal.h>"],
                "answer": "<fenv.h>",
            },
        ],
        "theory": {
            "definition": "Divide-by-zero handling in C is preventing or intercepting division by zero using defensive guard clauses (if (b == 0)) or OS signal handlers (SIGFPE) with setjmp/longjmp context restoration.",
            "why": "Integer division by zero causes undefined behavior and SIGFPE process crashes; defensive checks guarantee application stability.",
            "rules": [
                "Integer division (x / 0) and modulo (x % 0) cause immediate process crashes if unchecked.",
                "Always prefer manual guard checks (if (b == 0)) over signal handling for standard user code.",
                "Signal handling for SIGFPE via signal(SIGFPE, handler) and setjmp()/longjmp() provides low-level crash recovery.",
                "Header <fenv.h> provides floating-point exception functions fetestexcept(FE_DIVBYZERO) and feclearexcept(FE_DIVBYZERO)."
            ],
            "examples": [
                "#include <stdio.h>\n#include <signal.h>\nint main(void) {\n    int a = 10, b = 0;\n    if (b == 0) printf(\"Div by zero prevented\\n\");\n    else printf(\"%d\\n\", a / b);\n    return 0;\n}"
            ],
        },
    },

    40: {
        "concept": "Preprocessor directives in C are instructions starting with # that process source code before compilation. They perform text substitution (#define, #undef), header file inclusion (#include), conditional compilation (#if, #ifdef, #ifndef, #elif, #else, #endif), custom errors (#error), line renumbering (#line), compiler pragmas (#pragma), and predefined macros (__FILE__, __LINE__, __DATE__, __TIME__).",
        "syntax": "#define PI 3.14159\n#undef LIMIT\n#include <stdio.h>\n#include \"custom.h\"\n\n#ifdef DEBUG\n    printf(\"Debug build\\n\");\n#else\n    printf(\"Release build\\n\");\n#endif",
        "example": {
            "code": "#include <stdio.h>\n\n#define MAX_SIZE 100\n#define FEATURE_ENABLED\n\nint main(void) {\n#ifdef FEATURE_ENABLED\n    printf(\"Feature is ENABLED with limit %d\\n\", MAX_SIZE);\n#else\n    printf(\"Feature is DISABLED\\n\");\n#endif\n\n    printf(\"Compiled file: %s, line: %d\\n\", __FILE__, __LINE__);\n    return 0;\n}",
            "output": "Feature is ENABLED with limit 100\nCompiled file: solution.c, line: 14",
            "explanation": "Preprocessor replaces MAX_SIZE with 100, evaluates #ifdef FEATURE_ENABLED to include the first printf, and replaces predefined macros __FILE__ and __LINE__ with source file metadata.",
        },
        "fill_blanks": {
            "question": "#define LIMIT 50\n#_____(LIMIT) // Undefine macro\n// Compiling now fails if LIMIT is referenced",
            "answers": ["undef"],
            "options": ["undef", "define", "ifdef", "error"],
        },
        "compiler": {
            "title": "C Preprocessor Sandbox",
            "question": "Select the directive used to check if a macro identifier is defined before compilation.",
            "starter_code": "#include <stdio.h>\n\n#define VERBOSE\n\nint main(void) {\n#_____ VERBOSE\n    printf(\"Verbose logging active\\n\");\n#endif\n    return 0;\n}",
            "options": ["ifdef", "include", "pragma", "error"],
        },
        "skill_exa_test": [
            {
                "question": "At which stage of the C compilation pipeline are # directives (such as #define and #include) executed?",
                "options": [
                    "Preprocessing stage (before actual C source code compilation)",
                    "Assembly generation stage",
                    "Linker object symbol binding stage",
                    "CPU runtime execution stage"
                ],
                "answer": "Preprocessing stage (before actual C source code compilation)",
            },
            {
                "question": "What is the difference between #include <file.h> and #include \"file.h\"?",
                "options": [
                    "<file.h> searches standard system directories first, whereas \"file.h\" searches the current source file directory first",
                    "<file.h> is for C++ files, whereas \"file.h\" is for C files",
                    "<file.h> compiles in binary mode, whereas \"file.h\" compiles in text mode",
                    "There is no difference"
                ],
                "answer": "<file.h> searches standard system directories first, whereas \"file.h\" searches the current source file directory first",
            },
            {
                "question": "Which directive removes a previously created macro definition, causing any subsequent usage to result in an undeclared identifier error?",
                "options": ["#undef", "#delete", "#remove", "#clear"],
                "answer": "#undef",
            },
            {
                "question": "Which directive generates a custom compile-time error message and halts compilation when a required condition is not met?",
                "options": ["#error", "#warning", "#pragma", "#abort"],
                "answer": "#error",
            },
            {
                "question": "Which predefined macro automatically expands to the current source code line number integer during preprocessing?",
                "options": ["__LINE__", "__FILE__", "__DATE__", "__TIME__"],
                "answer": "__LINE__",
            },
        ],
        "theory": {
            "definition": "Preprocessor directives in C perform text manipulation, macro expansion, conditional compilation, and header inclusion before source code is compiled into assembly.",
            "why": "Enables platform portability, configurable feature builds, constant definitions without RAM overhead, and modular multi-file header organization.",
            "rules": [
                "Preprocessor directives begin with # and must not end with a semicolon ;.",
                "#define creates object-like or function-like text substitutions.",
                "#include <h> searches system paths; #include \"h\" searches local directory first.",
                "#ifdef, #ifndef, #if, #elif, #else, #endif control code inclusion conditionally.",
                "#pragma provides compiler-specific options; #error halts build with a message."
            ],
            "examples": [
                "#include <stdio.h>\n#define PI 3.14\n#ifdef PI\nint main(void) { printf(\"%f\\n\", PI); return 0; }\n#endif"
            ],
        },
    },

    41: {
        "concept": "Macros in C are preprocessor substitutions categorized into: (1) Object-Like Macros (replace identifiers with values), (2) Chain Macros (macros expanding into other macros), (3) Multi-Line Macros (using backslash \\ to extend definition), and (4) Function-Like Macros (accept parameters and evaluate without function call overhead). Arguments must be parenthesized for precedence safety.",
        "syntax": "#define MAX_USERS 50                        // Object-like\n#define ADMIN_LIMIT MAX_USERS              // Chain macro\n#define MULTI_ARR 1, \\\n                  2, \\\n                  3                         // Multi-line\n#define SQUARE(x) ((x) * (x))              // Function-like",
        "example": {
            "code": "#include <stdio.h>\n\n#define MIN(a, b) (((a) < (b)) ? (a) : (b))\n#define CHAIN_VAL BASE_VAL\n#define BASE_VAL 100\n#define MATRIX_ROW 1, \\\n                   2, \\\n                   3\n\nint main(void) {\n    int x = 15, y = 42;\n    printf(\"Min of %d and %d is: %d\\n\", x, y, MIN(x, y));\n    printf(\"Chain macro value: %d\\n\", CHAIN_VAL);\n\n    int arr[] = { MATRIX_ROW };\n    printf(\"Array first element: %d\\n\", arr[0]);\n    return 0;\n}",
            "output": "Min of 15 and 42 is: 15\nChain macro value: 100\nArray first element: 1",
            "explanation": "Demonstrates function-like macro MIN(a, b), chain macro CHAIN_VAL expanding to BASE_VAL (100), and multi-line macro MATRIX_ROW using backslashes \\.",
        },
        "fill_blanks": {
            "question": "#define MULTI_LINE 10, \\\n                   20, \\\n                   30\nint nums[] = { _____ };",
            "answers": ["MULTI_LINE"],
            "options": ["MULTI_LINE", "MULTI_LINE()", "ARRAY", "LIST"],
        },
        "compiler": {
            "title": "C Function-Like Macro Parentheses Sandbox",
            "question": "Fill in the function-like macro definition to safely multiply expressions with parentheses.",
            "starter_code": "#include <stdio.h>\n\n#define SAFE_MULT(a, b) _____\n\nint main(void) {\n    int res = SAFE_MULT(2 + 3, 4 + 1);\n    printf(\"Result: %d\\n\", res);\n    return 0;\n}",
            "options": ["((a) * (b))", "(a * b)", "a * b", "((a) + (b))"],
        },
        "skill_exa_test": [
            {
                "question": "What character is used at the end of a line to extend a multi-line macro definition across multiple physical lines?",
                "options": ["Backslash (\\)", "Forward slash (/)", "Semicolon (;)", "Tilde (~)"],
                "answer": "Backslash (\\)",
            },
            {
                "question": "What is a \"Chain Macro\" in C?",
                "options": [
                    "A macro whose definition references another macro name, causing sequential expansion by the preprocessor",
                    "A macro connected to a database socket",
                    "A loop containing 100 macros",
                    "A macro that only works in header files"
                ],
                "answer": "A macro whose definition references another macro name, causing sequential expansion by the preprocessor",
            },
            {
                "question": "What potential bug occurs if a function-like macro is written as #define SQUARE(x) x * x and invoked as SQUARE(2 + 3)?",
                "options": [
                    "It expands to 2 + 3 * 2 + 3 which evaluates incorrectly to 11 instead of 25 due to operator precedence",
                    "It causes a segmentation fault at runtime",
                    "It creates an infinite loop",
                    "It returns 0"
                ],
                "answer": "It expands to 2 + 3 * 2 + 3 which evaluates incorrectly to 11 instead of 25 due to operator precedence",
            },
            {
                "question": "Unlike standard C functions, what is a primary execution advantage of function-like macros?",
                "options": [
                    "They eliminate function call overhead (stack frame creation and return jumps) via inline text substitution",
                    "They automatically allocate heap memory",
                    "They support private member variables",
                    "They compile into separate dynamic library DLLs"
                ],
                "answer": "They eliminate function call overhead (stack frame creation and return jumps) via inline text substitution",
            },
            {
                "question": "What naming convention is standard in C for macro identifiers?",
                "options": ["UPPER_SNAKE_CASE", "camelCase", "PascalCase", "kebab-case"],
                "answer": "UPPER_SNAKE_CASE",
            },
        ],
        "theory": {
            "definition": "Macros in C are symbolic names or parameterized templates expanded by the preprocessor before compilation into equivalent code snippets.",
            "why": "Replaces magic numbers with readable constants, avoids function call overhead for tiny operations, and enables reusable code templates.",
            "rules": [
                "Object-like macros: #define NAME value.",
                "Multi-line macros use \\ at line ends; do not place spaces after \\.",
                "Function-like macros: #define MACRO(a, b) ((a) + (b)) — always parenthesize parameters and entire expression.",
                "Avoid side effects in arguments passed to macros (e.g. MIN(x++, y) expands x++ twice).",
                "Macro chaining allows parent macro expansion followed by child macro expansion."
            ],
            "examples": [
                "#include <stdio.h>\n#define ABS(x) (((x) < 0) ? -(x) : (x))\nint main(void) { printf(\"%d\\n\", ABS(-5)); return 0; }"
            ],
        },
    },

    42: {
        "concept": "A header file (.h) contains reusable function prototypes, structure definitions, enum types, macro constants, and external variable declarations. C divides headers into Standard Headers (<stdio.h>, <stdlib.h>, <string.h>, <math.h>, <time.h>, <limits.h>, <float.h>, <ctype.h>) and User-Defined Headers (\"my_header.h\"). Include guards prevent duplicate definitions.",
        "syntax": "// math_utils.h (Include Guard Pattern)\n#ifndef MATH_UTILS_H\n#define MATH_UTILS_H\n\nint add(int a, int b);\nint multiply(int a, int b);\n\n#endif",
        "example": {
            "code": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <math.h>\n\nint main(void) {\n    double root = sqrt(49.0);\n    char str[20] = \"12345\";\n    long val = atol(str);\n\n    printf(\"Square root from <math.h>: %.1f\\n\", root);\n    printf(\"Converted long from <stdlib.h>: %ld\\n\", val);\n    printf(\"String length from <string.h>: %zu\\n\", strlen(str));\n    return 0;\n}",
            "output": "Square root from <math.h>: 7.0\nConverted long from <stdlib.h>: 12345\nString length from <string.h>: 5",
            "explanation": "Uses standard header files <math.h>, <stdlib.h>, and <string.h> for mathematical calculations, string conversions, and character array utility functions.",
        },
        "fill_blanks": {
            "question": "// Guard header against multiple inclusion\n#_____ MY_HEADER_H\n#define MY_HEADER_H\n// Declarations...\n#endif",
            "answers": ["ifndef"],
            "options": ["ifndef", "ifdef", "include", "pragma"],
        },
        "compiler": {
            "title": "C Custom Header File Sandbox",
            "question": "Select the syntax to include a user-defined header file located in the same directory as the source file.",
            "starter_code": "#include <stdio.h>\n#include _____\n\nint main(void) {\n    printf(\"Included user header\\n\");\n    return 0;\n}",
            "options": ["\"my_utils.h\"", "<my_utils.h>", "my_utils.h", "#my_utils.h"],
        },
        "skill_exa_test": [
            {
                "question": "What is the primary purpose of an Include Guard (#ifndef HEADER_H / #define HEADER_H / #endif) in header files?",
                "options": [
                    "To prevent duplicate definition errors caused by including the same header file multiple times across nested inclusions",
                    "To password-protect header file contents",
                    "To encrypt C source code before compilation",
                    "To disable function prototypes"
                ],
                "answer": "To prevent duplicate definition errors caused by including the same header file multiple times across nested inclusions",
            },
            {
                "question": "Which standard C header file contains character testing and conversion prototypes such as isalpha(), isdigit(), toupper(), and tolower()?",
                "options": ["<ctype.h>", "<string.h>", "<stdlib.h>", "<limits.h>"],
                "answer": "<ctype.h>",
            },
            {
                "question": "Which standard C header file specifies data type value limits (such as INT_MAX, CHAR_BIT, LONG_MIN)?",
                "options": ["<limits.h>", "<float.h>", "<stddef.h>", "<math.h>"],
                "answer": "<limits.h>",
            },
            {
                "question": "Which header file contains platform-dependent floating-point constants such as FLT_MAX and DBL_EPSILON?",
                "options": ["<float.h>", "<limits.h>", "<math.h>", "<errno.h>"],
                "answer": "<float.h>",
            },
            {
                "question": "What modern non-standard preprocessor directive is widely supported by compilers as a single-line alternative to traditional #ifndef include guards?",
                "options": ["#pragma once", "#include once", "#guard once", "#define once"],
                "answer": "#pragma once",
            },
        ],
        "theory": {
            "definition": "Header files (.h) in C store reusable function declarations, macro definitions, data type aliases (typedef), and constants shared across multiple .c translation units.",
            "why": "Promotes modularity, prevents code duplication, and enforces consistent interface contracts between separate implementation files.",
            "rules": [
                "Header files should contain function declarations (prototypes), not function definitions (bodies).",
                "Standard headers use angle brackets #include <stdio.h>; user headers use quotes #include \"utils.h\".",
                "Always protect custom header files with include guards (#ifndef HEADER_H ... #endif) or #pragma once.",
                "Header <limits.h> defines integer type boundaries; <float.h> defines floating-point boundaries.",
                "Header <stdarg.h> provides va_start and va_arg for variadic functions."
            ],
            "examples": [
                "#ifndef UTILS_H\n#define UTILS_H\nvoid print_msg(const char *msg);\n#endif"
            ],
        },
    },

    43: {
        "concept": "The <time.h> header in C provides types and functions to measure time, manipulate dates, and format calendar information. Key types: clock_t (CPU clock cycles), time_t (seconds since Unix Epoch Jan 1, 1970), and struct tm (decomposed date/time components). Key functions: time(), localtime(), gmtime(), asctime(), difftime(), clock(), strftime().",
        "syntax": "#include <time.h>\n\ntime_t now = time(NULL);\nstruct tm *local = localtime(&now);\nprintf(\"%s\", asctime(local));\n\nclock_t start = clock();\n// Work...\ndouble cpu_time = (double)(clock() - start) / CLOCKS_PER_SEC;",
        "example": {
            "code": "#include <stdio.h>\n#include <time.h>\n\nint main(void) {\n    time_t t = time(NULL);\n    struct tm *local = localtime(&t);\n\n    char buf[80];\n    strftime(buf, sizeof(buf), \"Current Time: %Y-%m-%d %H:%M:%S\", local);\n    puts(buf);\n\n    clock_t start = clock();\n    for (volatile long i = 0; i < 10000000; i++);\n    clock_t end = clock();\n\n    double elapsed = (double)(end - start) / CLOCKS_PER_SEC;\n    printf(\"CPU time consumed: %.4f seconds\\n\", elapsed);\n    return 0;\n}",
            "output": "Current Time: 2026-04-15 07:22:42\nCPU time consumed: 0.0028 seconds",
            "explanation": "Uses time() and localtime() to retrieve calendar time, formats it using strftime(), and calculates CPU execution time using clock() and CLOCKS_PER_SEC.",
        },
        "fill_blanks": {
            "question": "clock_t t = clock();\n// Run workload...\ndouble sec = (double)(clock() - t) / _____ ;",
            "answers": ["CLOCKS_PER_SEC"],
            "options": ["CLOCKS_PER_SEC", "TIME_PER_SEC", "CPU_TICKS", "HZ"],
        },
        "compiler": {
            "title": "C Date and Time Formatting Sandbox",
            "question": "Select the function used to format struct tm date/time components into a customized string buffer using format specifiers like %Y and %H.",
            "starter_code": "#include <stdio.h>\n#include <time.h>\n\nint main(void) {\n    time_t now = time(NULL);\n    struct tm *info = localtime(&now);\n    char buf[50];\n    _____(buf, 50, \"%I:%M %p\", info);\n    printf(\"%s\\n\", buf);\n    return 0;\n}",
            "options": ["strftime", "asctime", "ctime", "difftime"],
        },
        "skill_exa_test": [
            {
                "question": "What starting epoch date is represented by a time_t integer value of 0 in standard C calendar time?",
                "options": [
                    "00:00:00 UTC, January 1, 1970 (Unix Epoch)",
                    "00:00:00 UTC, January 1, 1900",
                    "00:00:00 UTC, January 1, 2000",
                    "00:00:00 UTC, December 31, 1899"
                ],
                "answer": "00:00:00 UTC, January 1, 1970 (Unix Epoch)",
            },
            {
                "question": "How is the tm_mon (month) member field represented inside C's struct tm structure?",
                "options": [
                    "An integer from 0 to 11 (0 = January, 11 = December)",
                    "An integer from 1 to 12",
                    "A 3-letter string code",
                    "An enum value"
                ],
                "answer": "An integer from 0 to 11 (0 = January, 11 = December)",
            },
            {
                "question": "How is the tm_year member field represented inside struct tm?",
                "options": [
                    "Number of years elapsed since 1900 (e.g. year 2026 is stored as 126)",
                    "The full 4-digit year (e.g. 2026)",
                    "Number of years elapsed since 2000",
                    "Number of leap years"
                ],
                "answer": "Number of years elapsed since 1900 (e.g. year 2026 is stored as 126)",
            },
            {
                "question": "Which macro in <time.h> is used to convert CPU clock ticks returned by clock() into seconds?",
                "options": ["CLOCKS_PER_SEC", "SEC_PER_CLOCK", "TICKS_PER_SEC", "CLK_TCK"],
                "answer": "CLOCKS_PER_SEC",
            },
            {
                "question": "What is the difference between localtime() and gmtime() in <time.h>?",
                "options": [
                    "localtime() adjusts for local system timezone/DST, whereas gmtime() returns Coordinated Universal Time (UTC)",
                    "localtime() returns float, whereas gmtime() returns int",
                    "localtime() measures CPU clock, whereas gmtime() measures disk speed",
                    "There is no difference"
                ],
                "answer": "localtime() adjusts for local system timezone/DST, whereas gmtime() returns Coordinated Universal Time (UTC)",
            },
        ],
        "theory": {
            "definition": "Date and time management in C utilizes <time.h> types (time_t, clock_t, struct tm) and functions to track calendar time, measure CPU performance, and format timestamps.",
            "why": "Essential for logging events, performance profiling, calculating elapsed execution times, and scheduling date/time operations.",
            "rules": [
                "time_t holds total seconds since Jan 1, 1970.",
                "struct tm contains tm_sec (0-59), tm_min (0-59), tm_hour (0-23), tm_mday (1-31), tm_mon (0-11), tm_year (years since 1900), tm_wday (0-6, Sun=0), tm_yday (0-365).",
                "difftime(time2, time1) returns time difference in seconds as a double.",
                "clock() measures CPU clock ticks; elapsed CPU time in seconds is (double)ticks / CLOCKS_PER_SEC.",
                "asctime(struct tm*) formats time as Day Mon DD HH:MM:SS YYYY\\n."
            ],
            "examples": [
                "#include <stdio.h>\n#include <time.h>\nint main(void) {\n    time_t t = time(NULL);\n    printf(\"%s\", ctime(&t));\n    return 0;\n}"
            ],
        },
    },

    44: {
        "concept": """Linkage determines whether an identifier can be referenced across multiple translation units (source files) or is restricted to a single file. C defines three types of linkage:

1. Internal Linkage: Declared with static at file scope; visible only within the current source file
2. External Linkage: Default for global variables and functions (or extern); shared across multiple files
3. No Linkage: Local variables and function parameters; accessible within block scope only""",
        "syntax": "// Translation Unit 1 (file1.c)\nstatic int local_counter = 0; // Internal linkage\nint global_count = 100;      // External linkage (default)\n\n// Translation Unit 2 (file2.c)\nextern int global_count;     // External linkage reference",
        "example": {
            "code": "#include <stdio.h>\n\nstatic int file_private_var = 50; // Internal Linkage\nint global_shared_var = 100;      // External Linkage\n\nvoid demo(void) {\n    int local_var = 10; // No Linkage\n    printf(\"Local: %d, Private: %d, Shared: %d\\n\", local_var, file_private_var, global_shared_var);\n}\n\nint main(void) {\n    demo();\n    return 0;\n}",
            "output": "Local: 10, Private: 50, Shared: 100",
            "explanation": "file_private_var has internal linkage via static, global_shared_var has default external linkage, and local_var has no linkage.",
        },
        "fill_blanks": {
            "question": "// Limit variable visibility strictly to current source file\n_____ int file_local_config = 1;",
            "answers": ["static"],
            "options": ["static", "extern", "auto", "register"],
        },
        "compiler": {
            "title": "C Linkage Keyword Sandbox",
            "question": "Select the keyword used to declare a global variable defined in another translation unit file.",
            "starter_code": "#include <stdio.h>\n\n_____ int external_global_counter;\n\nint main(void) {\n    printf(\"Count: %d\\n\", external_global_counter);\n    return 0;\n}",
            "options": ["extern", "static", "auto", "volatile"],
        },
        "skill_exa_test": [
            {
                "question": "What is a \"Translation Unit\" in C?",
                "options": [
                    "A single C source file (.c) along with all header files (.h) included via #include directives",
                    "The executable file produced after linking",
                    "A CPU register block",
                    "A line of code inside main()"
                ],
                "answer": "A single C source file (.c) along with all header files (.h) included via #include directives",
            },
            {
                "question": "What type of linkage does a global variable declared with the static keyword possess?",
                "options": [
                    "Internal Linkage (accessible only within its own translation unit)",
                    "External Linkage",
                    "No Linkage",
                    "Dynamic Linkage"
                ],
                "answer": "Internal Linkage (accessible only within its own translation unit)",
            },
            {
                "question": "What is the default linkage for global functions and file-scope variables declared without static or extern in C?",
                "options": [
                    "External Linkage",
                    "Internal Linkage",
                    "No Linkage",
                    "Block Linkage"
                ],
                "answer": "External Linkage",
            },
            {
                "question": "What type of linkage do local variables declared inside a function body possess?",
                "options": [
                    "No Linkage",
                    "Internal Linkage",
                    "External Linkage",
                    "Global Linkage"
                ],
                "answer": "No Linkage",
            },
            {
                "question": "What error occurs at link time if two separate .c translation units define global variables with the exact same name and default external linkage?",
                "options": [
                    "Multiple definition / Duplicate symbol linker error",
                    "Stack overflow error",
                    "Segmentation fault",
                    "Preprocessor directive error"
                ],
                "answer": "Multiple definition / Duplicate symbol linker error",
            },
        ],
        "theory": {
            "definition": "Linkage determines whether an identifier can be bound across different translation units during linking or is private to a single file or block.",
            "why": "Prevents naming conflicts in multi-file projects, encapsulates module-private variables/functions, and enables global symbol sharing across modules.",
            "rules": [
                "Internal Linkage: static at global file scope. Visible only within declaring source file.",
                "External Linkage: Default for global variables and functions. Accessible across object files using extern.",
                "No Linkage: Local variables, parameters, struct tags, and typedef aliases.",
                "Functions marked static cannot be invoked from other .c files.",
                "Combining static and extern on the same symbol in the same scope is invalid."
            ],
            "examples": [
                "#include <stdio.h>\nstatic void private_func(void) {} // Internal linkage\nextern int shared_count;          // External linkage\nint main(void) { private_func(); return 0; }"
            ],
        },
    },

    45: {
        "concept": """Storage classes in C define scope, visibility, memory location, default value, and lifetime of variables. C features four primary storage classes:

1. auto: Default for local variables, allocated on stack with garbage initial values
2. static: Preserves value between function calls, allocated in data segment with zero initial value
3. register: Requests CPU register storage for fast access; address-of (&) operator is disallowed
4. extern: Refers to a global variable defined in another source file or translation unit""",
        "syntax": "void demo(void) {\n    auto int a = 10;        // Automatic (stack)\n    static int count = 0;   // Static (retains value across calls)\n    register int i;         // Register (CPU register suggestion)\n}\nextern int global_var;      // External (defined elsewhere)",
        "example": {
            "code": "#include <stdio.h>\n\nvoid counter_func(void) {\n    auto int auto_val = 0;\n    static int static_val = 0;\n\n    auto_val++;\n    static_val++;\n\n    printf(\"Auto: %d, Static: %d\\n\", auto_val, static_val);\n}\n\nint main(void) {\n    printf(\"Call 1: \"); counter_func();\n    printf(\"Call 2: \"); counter_func();\n    printf(\"Call 3: \"); counter_func();\n    return 0;\n}",
            "output": "Call 1: Auto: 1, Static: 1\nCall 2: Auto: 1, Static: 2\nCall 3: Auto: 1, Static: 3",
            "explanation": "auto_val is re-created and re-initialized on every function call (Auto: 1), whereas static_val retains its value between function calls (Static: 1, 2, 3).",
        },
        "fill_blanks": {
            "question": "void increment(void) {\n    _____ int count = 0; // Retains value across calls\n    count++;\n}",
            "answers": ["static"],
            "options": ["static", "auto", "register", "extern"],
        },
        "compiler": {
            "title": "C Storage Class Properties Sandbox",
            "question": "Which storage class keyword attempts to store a local loop variable inside a CPU register for high-speed execution?",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    _____ int i;\n    for (i = 0; i < 5; i++) {\n        printf(\"%d \", i);\n    }\n    return 0;\n}",
            "options": ["register", "auto", "static", "extern"],
        },
        "skill_exa_test": [
            {
                "question": "What is the lifetime of a variable declared with the static storage class inside a local function body?",
                "options": [
                    "Entire duration of program execution (retaining its value between function calls)",
                    "Until the function returns",
                    "1 second",
                    "Until CPU cache flushes"
                ],
                "answer": "Entire duration of program execution (retaining its value between function calls)",
            },
            {
                "question": "What is the default initial value of uninitialized auto and register variables in C?",
                "options": [
                    "Garbage value (undefined memory contents)",
                    "Zero (0)",
                    "NULL",
                    "-1"
                ],
                "answer": "Garbage value (undefined memory contents)",
            },
            {
                "question": "Why does trying to use the address-of operator & on a register variable (e.g. &reg_var) result in a compilation error?",
                "options": [
                    "Because register variables are stored in CPU hardware registers which do not have RAM memory addresses",
                    "Because register variables are read-only",
                    "Because register variables are stored on disk",
                    "Because & operator is reserved for pointers"
                ],
                "answer": "Because register variables are stored in CPU hardware registers which do not have RAM memory addresses",
            },
            {
                "question": "What is the default initial value of uninitialized static and extern global variables in C?",
                "options": [
                    "Zero (0)",
                    "Garbage value",
                    "1",
                    "EOF"
                ],
                "answer": "Zero (0)",
            },
            {
                "question": "What terminal command is used with GCC to compile multiple source files containing extern declarations into a single executable?",
                "options": [
                    "gcc main.c printVar.c -o main",
                    "gcc run main.c",
                    "cat main.c printVar.c",
                    "make link main.c"
                ],
                "answer": "gcc main.c printVar.c -o main",
            },
        ],
        "theory": {
            "definition": "Storage classes in C specify the scope (visibility), lifetime (duration in memory), location (RAM or CPU register), and default initial value of variables.",
            "why": "Provides fine-grained control over variable memory retention, global symbol visibility, and execution speed optimizations.",
            "rules": [
                "auto: Default local storage class. Stack RAM, local scope, garbage initial value.",
                "static: Retains value across calls. Data segment RAM, zero initial value, program lifetime.",
                "register: CPU register (if available). Local scope, garbage initial value, cannot take address &var.",
                "extern: References global variable defined in another file. Data segment RAM, zero initial value, program lifetime."
            ],
            "examples": [
                "#include <stdio.h>\nvoid count(void) {\n    static int n = 0;\n    printf(\"%d\\n\", ++n);\n}\nint main(void) { count(); count(); return 0; }"
            ],
        },
    },

    46: {
        "concept": "Variadic functions in C accept a variable number of arguments using an ellipsis (...) in the function signature following at least one fixed parameter. Variable arguments are accessed using <stdarg.h> macros: va_list (argument list pointer), va_start() (initializes traversal), va_arg() (retrieves next argument), and va_end() (cleans up argument list).",
        "syntax": "#include <stdarg.h>\n\nreturn_type func_name(int count, ...) {\n    va_list args;\n    va_start(args, count);\n    for (int i = 0; i < count; i++) {\n        int val = va_arg(args, int);\n    }\n    va_end(args);\n}",
        "example": {
            "code": "#include <stdio.h>\n#include <stdarg.h>\n\nint getSum(int n, ...) {\n    int sum = 0;\n    va_list list;\n    va_start(list, n);\n\n    for (int i = 0; i < n; i++) {\n        sum += va_arg(list, int);\n    }\n\n    va_end(list);\n    return sum;\n}\n\nint main(void) {\n    printf(\"1 + 2 = %d\\n\", getSum(2, 1, 2));\n    printf(\"3 + 4 + 5 = %d\\n\", getSum(3, 3, 4, 5));\n    printf(\"6 + 7 + 8 + 9 = %d\\n\", getSum(4, 6, 7, 8, 9));\n    return 0;\n}",
            "output": "1 + 2 = 3\n3 + 4 + 5 = 12\n6 + 7 + 8 + 9 = 30",
            "explanation": "getSum() takes count n followed by n variable integer arguments, traversing the argument list with va_start(), va_arg(), and va_end().",
        },
        "fill_blanks": {
            "question": "#include <stdarg.h>\n\nvoid print_nums(int count, ...) {\n    va_list args;\n    _____(args, count);\n    int first = _____(args, int);\n    _____(args);\n}",
            "answers": ["va_start", "va_arg", "va_end"],
            "options": ["va_start", "va_arg", "va_end", "va_list", "printf", "va_init"],
        },
        "compiler": {
            "title": "Variadic Function Sandbox",
            "question": "Select the macro used to step to the next argument and extract it with a specific type from va_list.",
            "starter_code": "#include <stdio.h>\n#include <stdarg.h>\n\ndouble average(int count, ...) {\n    va_list args;\n    va_start(args, count);\n    double sum = 0;\n    for (int i = 0; i < count; i++) {\n        sum += _____(args, double);\n    }\n    va_end(args);\n    return sum / count;\n}\n\nint main(void) {\n    printf(\"Avg: %.1f\\n\", average(3, 10.0, 20.0, 30.0));\n    return 0;\n}",
            "options": ["va_arg", "va_start", "va_next", "va_get"],
        },
        "skill_exa_test": [
            {
                "question": "Which standard C header file must be included to define va_list, va_start(), va_arg(), and va_end() for variadic functions?",
                "options": ["<stdarg.h>", "<stdlib.h>", "<stdio.h>", "<varargs.h>"],
                "answer": "<stdarg.h>",
            },
            {
                "question": "What parameter requirement is imposed on variadic functions in C?",
                "options": [
                    "They must have at least one named fixed argument preceding the ellipsis (...)",
                    "They cannot return any value (must be void)",
                    "They require all parameters to be floats",
                    "They can only be called from main()"
                ],
                "answer": "They must have at least one named fixed argument preceding the ellipsis (...)",
            },
            {
                "question": "What is the role of va_start(args, last_fixed_arg) in a variadic function?",
                "options": [
                    "Initializes the va_list argument pointer to reference the first variable argument following last_fixed_arg",
                    "Allocates memory on the heap for arguments",
                    "Prints arguments to stdout",
                    "Resets global errno"
                ],
                "answer": "Initializes the va_list argument pointer to reference the first variable argument following last_fixed_arg",
            },
            {
                "question": "What happens if va_arg(args, int) is called more times than the number of variable arguments passed to the function?",
                "options": [
                    "Undefined behavior occurs, reading invalid memory beyond the function stack frame",
                    "It returns 0 automatically",
                    "The program pauses for input",
                    "It throws a C++ exception"
                ],
                "answer": "Undefined behavior occurs, reading invalid memory beyond the function stack frame",
            },
            {
                "question": "Which standard C library functions are famous real-world examples of variadic functions?",
                "options": ["printf() and scanf()", "malloc() and free()", "fopen() and fclose()", "strcpy() and strcmp()"],
                "answer": "printf() and scanf()",
            },
        ],
        "theory": {
            "definition": "Variadic functions in C are functions that accept a variable number of positional arguments using an ellipsis ... in their parameter signature.",
            "why": "Enables building flexible formatting or aggregation APIs (like printf, scanf, or mathematical sum functions) where argument counts vary per call site.",
            "rules": [
                "Must feature at least one named parameter before ... (e.g. int count, ...).",
                "va_list: Special type representing argument list state.",
                "va_start(list, last_fixed): Initializes list pointer.",
                "va_arg(list, type): Yields current argument of type and advances pointer. Floating point arguments promote to double.",
                "va_end(list): Cleans up list before function return."
            ],
            "examples": [
                "#include <stdio.h>\n#include <stdarg.h>\nvoid log_vals(int n, ...) {\n    va_list a; va_start(a, n);\n    for(int i=0;i<n;i++) printf(\"%d \", va_arg(a, int));\n    va_end(a);\n}\nint main(void) { log_vals(2, 10, 20); return 0; }"
            ],
        },
    },

    47: {
        "concept": "Low-level Input-Output system calls provide direct interfaces to the operating system kernel for unbuffered file and device operations using integer File Descriptors (fd). Standard process descriptors: 0 (stdin), 1 (stdout), 2 (stderr). Primary unbuffered system calls from <unistd.h> and <fcntl.h>: creat(), open(), read(), write(), and close().",
        "syntax": "#include <fcntl.h>\n#include <unistd.h>\n\nint fd = open(\"foo.txt\", O_WRONLY | O_CREAT | O_TRUNC, 0644);\nif (fd < 0) { /* handle error */ }\nwrite(fd, \"hello\\n\", 6);\nclose(fd);",
        "example": {
            "code": "#include <stdio.h>\n#include <stdlib.h>\n#include <fcntl.h>\n#include <unistd.h>\n#include <string.h>\n\nint main(void) {\n    int fd = creat(\"sys_demo.txt\", 0644);\n    if (fd == -1) {\n        perror(\"Error creating file\");\n        return 1;\n    }\n    printf(\"File created with File Descriptor: %d\\n\", fd);\n\n    const char *text = \"Hello System Calls!\\n\";\n    ssize_t bytes_written = write(fd, text, strlen(text));\n    printf(\"Wrote %zd bytes to fd %d\\n\", bytes_written, fd);\n    close(fd);\n\n    fd = open(\"sys_demo.txt\", O_RDONLY);\n    char buffer[100];\n    ssize_t bytes_read = read(fd, buffer, sizeof(buffer) - 1);\n    if (bytes_read > 0) {\n        buffer[bytes_read] = '\\0';\n        printf(\"Read %zd bytes: %s\", bytes_read, buffer);\n    }\n    close(fd);\n    return 0;\n}",
            "output": "File created with File Descriptor: 3\nWrote 20 bytes to fd 3\nRead 20 bytes: Hello System Calls!",
            "explanation": "Uses creat() to create a file returning file descriptor 3, writes data using write(), closes descriptor, and reads unbuffered bytes back using open(), read(), and close().",
        },
        "fill_blanks": {
            "question": "int fd = open(\"test.txt\", O_RDONLY);\nchar buf[50];\nssize_t n = _____(fd, buf, sizeof(buf));\n_____(fd);",
            "answers": ["read", "close"],
            "options": ["read", "close", "write", "creat", "fopen", "fclose"],
        },
        "compiler": {
            "title": "Unbuffered I/O System Calls Sandbox",
            "question": "Select the standard file descriptor integer reserved for stdout (Standard Output) when a process starts.",
            "starter_code": "#include <unistd.h>\n\nint main(void) {\n    const char msg[] = \"Direct kernel write\\n\";\n    write(_____, msg, sizeof(msg) - 1);\n    return 0;\n}",
            "options": ["1", "0", "2", "3"],
        },
        "skill_exa_test": [
            {
                "question": "What integer file descriptor number is assigned by default to standard input (stdin) when any C process starts?",
                "options": ["0", "1", "2", "3"],
                "answer": "0",
            },
            {
                "question": "Which header file declares low-level POSIX file I/O system call prototypes like read(), write(), and close()?",
                "options": ["<unistd.h>", "<stdio.h>", "<fcntl.h>", "<sys/types.h>"],
                "answer": "<unistd.h>",
            },
            {
                "question": "Which file open flag passed to open() creates the target file if it does not already exist on disk?",
                "options": ["O_CREAT", "O_RDONLY", "O_APPEND", "O_EXCL"],
                "answer": "O_CREAT",
            },
            {
                "question": "What value is returned by read(fd, buf, count) when the end of file (EOF) is reached?",
                "options": ["0", "-1", "EOF", "NULL"],
                "answer": "0",
            },
            {
                "question": "What does the OS kernel do when close(fd) is called on a valid open file descriptor?",
                "options": [
                    "Destroys the file table entry association for fd and frees fd in the process descriptor table for future open calls",
                    "Deletes the file from disk secondary storage",
                    "Flushes stdout screen buffers",
                    "Terminates the calling process"
                ],
                "answer": "Destroys the file table entry association for fd and frees fd in the process descriptor table for future open calls",
            },
        ],
        "theory": {
            "definition": "Input-Output system calls (creat, open, read, write, close) provide direct, unbuffered communication between C programs and the operating system kernel via integer file descriptors.",
            "why": "High-performance, unbuffered control over files, pipes, sockets, and hardware devices without stdio buffer layer overhead.",
            "rules": [
                "Standard File Descriptors: 0 = stdin, 1 = stdout, 2 = stderr.",
                "Newly opened files get lowest unused integer descriptor (typically 3).",
                "open(path, flags, mode) flags in <fcntl.h>: O_RDONLY, O_WRONLY, O_RDWR, O_CREAT, O_EXCL, O_APPEND, O_TRUNC.",
                "read() returns bytes read (0 on EOF, -1 on error).",
                "write() returns bytes written (-1 on error)."
            ],
            "examples": [
                "#include <fcntl.h>\n#include <unistd.h>\nint main(void) {\n    int fd = open(\"log.txt\", O_WRONLY | O_CREAT | O_APPEND, 0644);\n    write(fd, \"Log\\n\", 4);\n    close(fd);\n    return 0;\n}"
            ],
        },
    },

    48: {
        "concept": "A signal in C is an asynchronous software-generated interrupt sent by the OS kernel or another process to notify a program of an event (e.g. SIGINT for Ctrl+C, SIGSEGV for invalid memory access, SIGFPE for division by zero, SIGKILL for forced termination). Header <signal.h> provides signal(), raise(), and kill().",
        "syntax": "#include <signal.h>\n#include <stdio.h>\n#include <stdlib.h>\n\nvoid handle_sigint(int sig) {\n    printf(\"Caught signal %d\\n\", sig);\n    exit(0);\n}\n\nint main(void) {\n    signal(SIGINT, handle_sigint);\n    raise(SIGINT);\n    return 0;\n}",
        "example": {
            "code": "#include <stdio.h>\n#include <stdlib.h>\n#include <signal.h>\n#include <unistd.h>\n\nvoid handle_signal(int sig) {\n    printf(\"Signal Handler caught signal number: %d\\n\", sig);\n}\n\nint main(void) {\n    signal(SIGINT, handle_signal);\n    pid_t pid = getpid();\n    printf(\"Current Process PID: %d. Raising SIGINT...\\n\", pid);\n    kill(pid, SIGINT);\n    printf(\"Process resumed after signal handling.\\n\");\n    return 0;\n}",
            "output": "Current Process PID: 4210. Raising SIGINT...\nSignal Handler caught signal number: 2\nProcess resumed after signal handling.",
            "explanation": "Registers handle_signal() for SIGINT (signal 2), gets process PID via getpid(), and triggers signal manually using kill(pid, SIGINT).",
        },
        "fill_blanks": {
            "question": "#include <signal.h>\n\nvoid handler(int sig) { printf(\"Signal %d\", sig); }\nint main(void) {\n    _____(SIGINT, handler);\n    _____(SIGINT);\n}",
            "answers": ["signal", "raise"],
            "options": ["signal", "raise", "kill", "catch", "throw", "exit"],
        },
        "compiler": {
            "title": "C Signal Handling Sandbox",
            "question": "Select the function used to send a signal to a specific process ID (PID) in POSIX C.",
            "starter_code": "#include <signal.h>\n#include <unistd.h>\n\nint main(void) {\n    pid_t pid = getpid();\n    _____(pid, SIGTERM);\n    return 0;\n}",
            "options": ["kill", "raise", "signal", "alarm"],
        },
        "skill_exa_test": [
            {
                "question": "What integer signal number is assigned to SIGINT (Keyboard Interrupt) on standard POSIX systems?",
                "options": ["2", "9", "11", "15"],
                "answer": "2",
            },
            {
                "question": "Which of the following signals CANNOT be caught, blocked, or customized with a user-defined signal handler?",
                "options": ["SIGKILL", "SIGINT", "SIGTERM", "SIGSEGV"],
                "answer": "SIGKILL",
            },
            {
                "question": "What signal is generated by the OS when a C program attempts to dereference an invalid or unmapped memory address (Segmentation Fault)?",
                "options": ["SIGSEGV", "SIGFPE", "SIGILL", "SIGBUS"],
                "answer": "SIGSEGV",
            },
            {
                "question": "What function in <signal.h> sends a specified signal to the currently executing process itself?",
                "options": ["raise()", "kill()", "signal()", "alarm()"],
                "answer": "raise()",
            },
            {
                "question": "What signature must a user-defined signal handler function possess in C?",
                "options": [
                    "void handler_name(int sig)",
                    "int handler_name(void)",
                    "void* handler_name(char *msg)",
                    "int handler_name(int sig, double val)"
                ],
                "answer": "void handler_name(int sig)",
            },
        ],
        "theory": {
            "definition": "Signals in C are software-generated asynchronous notifications delivered by the OS kernel to a process to handle hardware/software events or inter-process interrupts.",
            "why": "Permits graceful cleanup on interrupt (Ctrl+C), handling crashes (SIGSEGV), setting timer alarms (SIGALRM), and managing child processes (SIGCHLD).",
            "rules": [
                "<signal.h> defines signal constants: SIGINT, SIGILL, SIGFPE, SIGSEGV, SIGTERM, SIGABRT, SIGKILL, SIGBUS.",
                "Default actions: Term (Terminate), Ign (Ignore), Stop (Block), Cont (Continue).",
                "signal(sig, handler) registers custom handler void handler(int).",
                "SIGKILL (9) and SIGSTOP cannot be caught or ignored.",
                "raise(sig) sends sig to current process; kill(pid, sig) sends sig to target pid."
            ],
            "examples": [
                "#include <stdio.h>\n#include <signal.h>\nvoid on_int(int s) { printf(\"Caught %d\\n\", s); }\nint main(void) { signal(SIGINT, on_int); raise(SIGINT); return 0; }"
            ],
        },
    },

    49: {
        "concept": "Socket programming in C enables network communication between client and server processes over IPv4/IPv6 networks using TCP (stream sockets) or UDP (datagram sockets). Server workflow: socket() -> setsockopt() -> bind() -> listen() -> accept() -> read()/write() -> close(). Client workflow: socket() -> connect() -> write()/read() -> close().",
        "syntax": "#include <sys/socket.h>\n#include <netinet/in.h>\n#include <unistd.h>\n\nint server_fd = socket(AF_INET, SOCK_STREAM, 0);\nstruct sockaddr_in addr;\naddr.sin_family = AF_INET;\naddr.sin_addr.s_addr = INADDR_ANY;\naddr.sin_port = htons(8080);\n\nbind(server_fd, (struct sockaddr*)&addr, sizeof(addr));\nlisten(server_fd, 5);\nint client_sock = accept(server_fd, NULL, NULL);",
        "example": {
            "code": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <sys/socket.h>\n#include <netinet/in.h>\n#include <unistd.h>\n\nint main(void) {\n    int server_fd = socket(AF_INET, SOCK_STREAM, 0);\n    if (server_fd < 0) {\n        perror(\"Socket creation failed\");\n        return 1;\n    }\n\n    int opt = 1;\n    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));\n\n    struct sockaddr_in address;\n    address.sin_family = AF_INET;\n    address.sin_addr.s_addr = INADDR_ANY;\n    address.sin_port = htons(8080);\n\n    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {\n        perror(\"Bind failed\");\n        close(server_fd);\n        return 1;\n    }\n\n    printf(\"Server bound successfully to port 8080 (AF_INET, SOCK_STREAM).\\n\");\n    close(server_fd);\n    return 0;\n}",
            "output": "Server bound successfully to port 8080 (AF_INET, SOCK_STREAM).",
            "explanation": "Demonstrates server TCP socket initialization using socket(AF_INET, SOCK_STREAM, 0), setting SO_REUSEADDR, and binding to port 8080 via bind().",
        },
        "fill_blanks": {
            "question": "int fd = _____(AF_INET, SOCK_STREAM, 0);\n_____(fd, (struct sockaddr*)&addr, sizeof(addr));\n_____(fd, 5);",
            "answers": ["socket", "bind", "listen"],
            "options": ["socket", "bind", "listen", "accept", "connect", "recv"],
        },
        "compiler": {
            "title": "C Socket Creation Sandbox",
            "question": "Select the socket type constant used for reliable, connection-oriented TCP stream sockets.",
            "starter_code": "#include <sys/socket.h>\n\nint main(void) {\n    int sockfd = socket(AF_INET, _____, 0);\n    return 0;\n}",
            "options": ["SOCK_STREAM", "SOCK_DGRAM", "SOCK_RAW", "SOCK_SEQPACKET"],
        },
        "skill_exa_test": [
            {
                "question": "Which domain constant is passed to socket() to specify IPv4 Internet protocol communication?",
                "options": ["AF_INET", "AF_UNIX", "AF_INET6", "AF_LOCAL"],
                "answer": "AF_INET",
            },
            {
                "question": "What is the correct sequence of system calls executed on the SERVER side to accept incoming TCP client connections?",
                "options": [
                    "socket() -> bind() -> listen() -> accept()",
                    "socket() -> connect() -> read() -> close()",
                    "bind() -> socket() -> connect() -> accept()",
                    "listen() -> bind() -> socket() -> accept()"
                ],
                "answer": "socket() -> bind() -> listen() -> accept()",
            },
            {
                "question": "Which function puts a server socket into passive listening mode to wait for incoming client connection requests?",
                "options": ["listen()", "bind()", "accept()", "connect()"],
                "answer": "listen()",
            },
            {
                "question": "Which helper function converts a port number from host byte order to network byte order (uint16_t) in C?",
                "options": ["htons()", "ntohs()", "htonl()", "inet_pton()"],
                "answer": "htons()",
            },
            {
                "question": "What error occurs when a server attempts to bind to a port that is already in use by another running application?",
                "options": [
                    "Port binding error / Address already in use (EADDRINUSE)",
                    "Segmentation fault",
                    "Stack overflow",
                    "SIGFPE exception"
                ],
                "answer": "Port binding error / Address already in use (EADDRINUSE)",
            },
        ],
        "theory": {
            "definition": "Socket programming in C uses network APIs (<sys/socket.h>, <netinet/in.h>) to enable client-server data exchange across local or remote networks via TCP or UDP sockets.",
            "why": "Essential for web servers, chat applications, streaming services, distributed systems, and IPC networking.",
            "rules": [
                "Socket Types: SOCK_STREAM (TCP, reliable stream), SOCK_DGRAM (UDP, connectionless datagrams).",
                "Address Structure: struct sockaddr_in with sin_family, sin_addr.s_addr, sin_port.",
                "Use htons(port) for port byte order conversion to network big-endian.",
                "setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &opt, len) avoids 'address already in use' errors.",
                "accept() blocks until a client connects, returning a new socket file descriptor for client I/O."
            ],
            "examples": [
                "#include <sys/socket.h>\n#include <netinet/in.h>\n#include <unistd.h>\nint main(void) {\n    int s = socket(AF_INET, SOCK_STREAM, 0);\n    close(s);\n    return 0;\n}"
            ],
        },
    },

    50: {
        "concept": "Introduced in C11, the _Generic keyword provides compile-time type selection based on the data type of a controlling expression. Combined with macros, _Generic simulates function overloading in C by dispatching different functions or expressions based on argument types in a type-safe manner.",
        "syntax": "#define print_type(x) _Generic((x), \\\n    int: \"Integer\", \\\n    double: \"Double\", \\\n    char*: \"String\", \\\n    default: \"Other\")",
        "example": {
            "code": "#include <stdio.h>\n\nvoid print_int(int val) { printf(\"Int: %d\\n\", val); }\nvoid print_double(double val) { printf(\"Double: %.2f\\n\", val); }\nvoid print_str(char* val) { printf(\"String: %s\\n\", val); }\n\n#define print_val(x) _Generic((x), \\\n    int: print_int, \\\n    double: print_double, \\\n    char*: print_str \\\n)(x)\n\nint main(void) {\n    print_val(42);\n    print_val(3.14159);\n    print_val(\"SkillExa C11\");\n    return 0;\n}",
            "output": "Int: 42\nDouble: 3.14\nString: SkillExa C11",
            "explanation": "Uses C11 _Generic inside print_val(x) macro to select the correct type-specific print function (print_int, print_double, or print_str) at compile time.",
        },
        "fill_blanks": {
            "question": "#define TYPE_NAME(x) _____((x), \\\n    int: \"Integer\", \\\n    double: \"Double\", \\\n    default: \"Unknown\")",
            "answers": ["_Generic"],
            "options": ["_Generic", "typeof", "decltype", "switch_type"],
        },
        "compiler": {
            "title": "C11 _Generic Overloading Sandbox",
            "question": "Select the keyword introduced in C11 standard to perform compile-time type selection.",
            "starter_code": "#include <stdio.h>\n\nint main(void) {\n    int code = _____(100L, int: 1, long: 2, default: 0);\n    printf(\"Code: %d\\n\", code);\n    return 0;\n}",
            "options": ["_Generic", "typeof", "alignof", "auto"],
        },
        "skill_exa_test": [
            {
                "question": "In which C language ISO standard was the _Generic keyword officially introduced?",
                "options": ["C11 standard", "C89 standard", "C99 standard", "C23 standard"],
                "answer": "C11 standard",
            },
            {
                "question": "What feature of C++ is simulated in C by combining _Generic with preprocessor macros?",
                "options": [
                    "Function Overloading (executing different code based on argument types)",
                    "Class Inheritance",
                    "Try-Catch exception handling",
                    "Template Metaprogramming"
                ],
                "answer": "Function Overloading (executing different code based on argument types)",
            },
            {
                "question": "At what stage of execution is the type selection in _Generic evaluated?",
                "options": [
                    "Compile time (zero runtime performance penalty)",
                    "Runtime during function execution",
                    "Preprocessing textual macro expansion",
                    "Linker symbol binding time"
                ],
                "answer": "Compile time (zero runtime performance penalty)",
            },
            {
                "question": "What happens if an argument type passed to _Generic does not match any listed type association and no default: association is provided?",
                "options": [
                    "A compilation error occurs at build time",
                    "It returns 0 at runtime",
                    "It converts to void* automatically",
                    "It calls exit(1)"
                ],
                "answer": "A compilation error occurs at build time",
            },
            {
                "question": "What is a primary advantage of _Generic macros over traditional C macros?",
                "options": [
                    "Provides compile-time type safety and prevents unexpected type conversions",
                    "Generates self-documenting HTML files",
                    "Allocates dynamic stack frames",
                    "Enables multi-threading automatically"
                ],
                "answer": "Provides compile-time type safety and prevents unexpected type conversions",
            },
        ],
        "theory": {
            "definition": "_Generic is a C11 keyword that chooses an expression at compile time based on the data type of a controlling expression.",
            "why": "Enables type-safe generic macros and function overloading simulation in C without runtime type inspection overhead.",
            "rules": [
                "Syntax: _Generic(expression, type1: expr1, type2: expr2, ..., default: default_expr).",
                "Controlling expression is evaluated only for its type, not its runtime value.",
                "Type associations must be unique (no duplicate types in same _Generic selection).",
                "Compile error occurs if no type matches and default: is omitted.",
                "Fully evaluated at compile time."
            ],
            "examples": [
                "#include <stdio.h>\n#define typename(x) _Generic((x), int: \"int\", float: \"float\", default: \"other\")\nint main(void) { printf(\"%s\\n\", typename(10)); return 0; }"
            ],
        },
    },

    51: {
        "concept": "Multithreading in C using POSIX Threads (<pthread.h>) allows concurrent execution of multiple lightweight thread units sharing process RAM space (code, data, heap, descriptors) while maintaining independent stacks and program counters. APIs: pthread_create(), pthread_join(), pthread_exit(), pthread_cancel(), pthread_self(), and pthread_mutex_t.",
        "syntax": "#include <pthread.h>\n\nvoid* worker(void* arg) {\n    printf(\"Thread running\\n\");\n    return NULL;\n}\n\npthread_t thread;\npthread_create(&thread, NULL, worker, NULL);\npthread_join(thread, NULL);",
        "example": {
            "code": "#include <stdio.h>\n#include <stdlib.h>\n#include <pthread.h>\n\npthread_mutex_t lock;\nint counter = 0;\n\nvoid* count_up(void* arg) {\n    pthread_mutex_lock(&lock);\n    counter++;\n    printf(\"Thread %lu updated counter to %d\\n\", (unsigned long)pthread_self(), counter);\n    pthread_mutex_unlock(&lock);\n    return NULL;\n}\n\nint main(void) {\n    pthread_t t1, t2;\n    pthread_mutex_init(&lock, NULL);\n\n    pthread_create(&t1, NULL, count_up, NULL);\n    pthread_create(&t2, NULL, count_up, NULL);\n\n    pthread_join(t1, NULL);\n    pthread_join(t2, NULL);\n\n    pthread_mutex_destroy(&lock);\n    printf(\"Final counter: %d\\n\", counter);\n    return 0;\n}",
            "output": "Thread 139847120 updated counter to 1\nThread 139847952 updated counter to 2\nFinal counter: 2",
            "explanation": "Creates two threads executing count_up(), synchronized using a pthread_mutex_t lock to prevent race conditions on shared counter memory.",
        },
        "fill_blanks": {
            "question": "pthread_t tid;\n_____( &tid, NULL, task, NULL);\n_____(tid, NULL); // Wait for thread completion",
            "answers": ["pthread_create", "pthread_join"],
            "options": ["pthread_create", "pthread_join", "pthread_exit", "pthread_cancel", "fork", "wait"],
        },
        "compiler": {
            "title": "POSIX Threads (pthreads) Creation Sandbox",
            "question": "Select the GCC compiler flag required to link the POSIX threads library when compiling multi-threaded C applications.",
            "starter_code": "#include <pthread.h>\n#include <stdio.h>\n\nint main(void) {\n    // Build with: gcc main.c _____ -o main\n    printf(\"Pthreads ready\\n\");\n    return 0;\n}",
            "options": ["-lpthread", "-lmath", "-lstd", "-lposix"],
        },
        "skill_exa_test": [
            {
                "question": "Which standard C POSIX function creates and launches a new concurrent thread?",
                "options": ["pthread_create()", "pthread_start()", "thread_new()", "fork()"],
                "answer": "pthread_create()",
            },
            {
                "question": "What function is used by a parent thread to block execution until a target thread completes execution?",
                "options": ["pthread_join()", "pthread_wait()", "pthread_exit()", "pthread_sleep()"],
                "answer": "pthread_join()",
            },
            {
                "question": "What shared resource is accessible by all threads within the same C process?",
                "options": [
                    "Global variables, heap memory, and open file descriptors",
                    "Independent CPU registers and stack frames",
                    "Private program counters",
                    "Isolated kernel process tables"
                ],
                "answer": "Global variables, heap memory, and open file descriptors",
            },
            {
                "question": "What concurrency bug occurs when two or more threads attempt to read and write shared data simultaneously without synchronization, leading to unpredictable results?",
                "options": ["Race Condition", "Deadlock", "Starvation", "Segmentation Fault"],
                "answer": "Race Condition",
            },
            {
                "question": "Which synchronization primitive in <pthread.h> ensures mutual exclusion so that only one thread can access a critical section at a time?",
                "options": ["Mutex (pthread_mutex_t)", "Barrier", "Spinlock", "Condition Variable"],
                "answer": "Mutex (pthread_mutex_t)",
            },
        ],
        "theory": {
            "definition": "Multithreading in C via POSIX Threads (<pthread.h>) allows concurrent execution paths within a single process sharing the same address space.",
            "why": "Improves application performance, responsiveness, and multi-core CPU utilization for parallel tasks.",
            "rules": [
                "Threads share code, global/static data, heap memory, and file descriptors; each thread has its own stack and registers.",
                "Function signature for thread routine: void* thread_func(void* arg).",
                "pthread_create(&tid, attr, func, arg) launches thread.",
                "pthread_join(tid, &retval) waits for thread termination.",
                "Synchronize shared state mutations using pthread_mutex_lock() and pthread_mutex_unlock()."
            ],
            "examples": [
                "#include <pthread.h>\n#include <stdio.h>\nvoid* run(void* a) { printf(\"Thread\\n\"); return NULL; }\nint main(void) { pthread_t t; pthread_create(&t, NULL, run, NULL); pthread_join(t, NULL); return 0; }"
            ],
        },
    },

    52: {
        "concept": """The memory layout of a C program divides process memory into 5 distinct segments:/n

1. Text Segment: Stores compiled executable machine instructions (read-only)/n
2. Initialized Data Segment: Stores global and static variables initialized by programmer/n
3. Uninitialized Data Segment (BSS): Stores uninitialized global/static variables, set to 0 at runtime/n
4. Heap Segment: Dynamic memory allocated via malloc/calloc/realloc, grows upward/n
5. Stack Segment: Stores local variables, function arguments, and stack frames, grows downward""",
        "syntax": "// Memory Layout Segments:\n// Text Segment: Executable instructions (read-only)\n// Initialized Data: int gvar = 10; static int svar = 20;\n// BSS Segment: int ugvar; static int usvar; (zero-initialized)\n// Heap Segment: int *hvar = malloc(sizeof(int)); (grows up)\n// Stack Segment: int lvar = 5; (grows down, stack frames)",
        "example": {
            "code": "#include <stdio.h>\n#include <stdlib.h>\n\nint gvar = 10;            // Initialized Data Segment\nint ugvar;                // BSS Segment (uninitialized global)\nconst int cgvar = 100;    // Text/Read-Only Segment\n\nvoid foo(void) {\n    int lvar = 5;         // Stack Segment\n    printf(\"Stack (lvar): %p\\n\", (void*)&lvar);\n}\n\nint main(void) {\n    int *hvar = (int*)malloc(sizeof(int)); // Heap Segment\n    printf(\"Text (cgvar):  %p\\n\", (void*)&cgvar);\n    printf(\"Data (gvar):   %p\\n\", (void*)&gvar);\n    printf(\"BSS (ugvar):   %p\\n\", (void*)&ugvar);\n    printf(\"Heap (hvar):   %p\\n\", (void*)hvar);\n    foo();\n    free(hvar);\n    return 0;\n}",
            "output": "Text (cgvar): 0x402084\nData (gvar): 0x404020\nBSS (ugvar): 0x404028\nHeap (hvar): 0x119592a0\nStack (lvar): 0x7ffe8289c66c",
            "explanation": "Demonstrates memory addresses across all 5 segments. cgvar is in read-only text, gvar in initialized data segment, ugvar in BSS segment (auto-zeroed), hvar points to heap memory, and lvar resides on the stack.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n\nint global_init = 10; // Stored in _____ Data Segment\nint global_uninit;    // Stored in _____ Segment (auto zeroed)\n\nint main(void) {\n    return 0;\n}",
            "answers": ["Initialized", "BSS"],
            "options": ["Initialized", "BSS", "Stack", "Heap", "Text", "Code"],
        },
        "compiler": {
            "title": "C Memory Layout Sandbox",
            "question": "Complete the initialization of the global data segment variable.",
            "starter_code": "#include <stdio.h>\n\nint g_init = _____; // Initialized Data Segment\nint g_uninit;     // BSS Segment\n\nint main(void) {\n    int l_var = 5; // Stack\n    printf(\"G_Init: %d, G_Uninit: %d, L_Var: %d\\n\", g_init, g_uninit, l_var);\n    return 0;\n}",
            "options": ["100", "200", "50", "0"],
        },
        "skill_exa_test": [
            {
                "question": "Which segment of C memory stores the executable machine instructions and functions of a program in read-only memory?",
                "options": [
                    "Text Segment (Code Segment)",
                    "BSS Segment",
                    "Heap Segment",
                    "Stack Segment"
                ],
                "answer": "Text Segment (Code Segment)",
            },
            {
                "question": "What is the BSS (Uninitialized Data Segment) in C memory layout?",
                "options": [
                    "Segment storing global and static variables not explicitly initialized, which are automatically set to zero at runtime",
                    "Segment storing local variables declared inside function bodies",
                    "Segment storing dynamically allocated memory returned by malloc()",
                    "Segment storing command-line arguments passed to main()"
                ],
                "answer": "Segment storing global and static variables not explicitly initialized, which are automatically set to zero at runtime",
            },
            {
                "question": "In which directions do the Heap and Stack segments grow in memory during execution?",
                "options": [
                    "Heap grows upward toward higher addresses; Stack grows downward toward lower addresses",
                    "Heap grows downward toward lower addresses; Stack grows upward toward higher addresses",
                    "Both Heap and Stack grow upward toward higher addresses",
                    "Neither Heap nor Stack changes size during program execution"
                ],
                "answer": "Heap grows upward toward higher addresses; Stack grows downward toward lower addresses",
            },
            {
                "question": "What command line tool in GCC/MinGW reports byte sizes of text, data, and bss segments of a compiled executable binary file?",
                "options": [
                    "size command (size filename)",
                    "gdb command",
                    "valgrind command",
                    "objdump -d"
                ],
                "answer": "size command (size filename)",
            },
            {
                "question": "What memory segment stores a `static int count = 5;` variable declared inside a function?",
                "options": [
                    "Initialized Data Segment",
                    "BSS Segment",
                    "Stack Segment",
                    "Heap Segment"
                ],
                "answer": "Initialized Data Segment",
            },
        ],
        "theory": {
            "definition": "The memory layout of a C program organizes process memory into 5 distinct regions during execution: Text, Initialized Data, Uninitialized Data (BSS), Heap, and Stack.",
            "why": "Understanding memory layout prevents segmentation faults, stack overflow, memory leaks, and enables performance optimization.",
            "rules": [
                "Text Segment: Stores executable instructions in read-only memory.",
                "Initialized Data Segment: Stores initialized global and static variables.",
                "BSS Segment: Stores uninitialized global and static variables (zero-initialized at runtime).",
                "Heap Segment: Dynamic memory allocation (malloc, calloc, realloc, free), grows upward.",
                "Stack Segment: Function calls, stack frames, local variables, parameters, grows downward.",
                "Memory Boundary: When Heap and Stack meet, available free system memory is exhausted."
            ],
            "examples": [
                "#include <stdio.h>\nint g_var = 10; // Initialized Data\nint u_var;     // BSS\nint main(void) {\n    int l_var = 5; // Stack\n    printf(\"%d %d %d\\n\", g_var, u_var, l_var);\n    return 0;\n}"
            ],
        },
    },

    53: {
        "concept": """Dynamic memory allocation manages heap memory at runtime using 4 standard functions in <stdlib.h>:

1. malloc(size): Allocates uninitialized heap memory bytes
2. calloc(n, size): Allocates contiguous heap memory for n elements and initializes all bytes to 0
3. realloc(ptr, new_size): Resizes a previously allocated memory block
4. free(ptr): Deallocates memory and returns it to the heap
5. Return Value: Allocation functions return a void* pointer or NULL if allocation fails.""",
        "syntax": "#include <stdlib.h>\n\nint *ptr = malloc(5 * sizeof(int));           // Allocates uninitialized memory\nint *cptr = calloc(5, sizeof(int));          // Allocates zero-initialized memory\nint *temp = realloc(ptr, 10 * sizeof(int));  // Resizes memory block\nif (temp != NULL) ptr = temp;                // Safe reallocation pattern\nfree(ptr); ptr = NULL;                        // Deallocates & prevents dangling pointer",
        "example": {
            "code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    int *ptr = calloc(5, sizeof(int));\n\n    if (ptr == NULL) {\n        printf(\"Memory allocation failed\\n\");\n        return 1;\n    }\n\n    printf(\"Zero-initialized values: \");\n    for (int i = 0; i < 5; i++) {\n        printf(\"%d \", ptr[i]);\n    }\n    printf(\"\\n\");\n\n    free(ptr);\n    ptr = NULL;\n    return 0;\n}",
            "output": "Zero-initialized values: 0 0 0 0 0",
            "explanation": "calloc(5, sizeof(int)) allocates memory for 5 integers and initializes all bytes to zero. ptr is checked against NULL for safety, used like an array, and deallocated with free(ptr).",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    int *ptr = _____(5 * sizeof(int)); // Allocate uninitialized heap memory\n    if (ptr != NULL) {\n        _____(ptr); // Deallocate heap memory\n        ptr = NULL;\n    }\n    return 0;\n}",
            "answers": ["malloc", "free"],
            "options": ["malloc", "free", "calloc", "realloc", "sizeof", "exit"],
        },
        "compiler": {
            "title": "C Dynamic Memory Sandbox",
            "question": "Complete the calloc allocation and free deallocation code.",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    int *arr = _____(5, sizeof(int));\n    if (arr == NULL) return 1;\n\n    for (int i = 0; i < 5; i++) arr[i] = (i + 1) * 10;\n    for (int i = 0; i < 5; i++) printf(\"%d \", arr[i]);\n\n    _____(arr);\n    return 0;\n}",
            "options": ["calloc", "free", "malloc", "realloc"],
        },
        "skill_exa_test": [
            {
                "question": "What is the main difference between malloc() and calloc() in C?",
                "options": [
                    "calloc() initializes allocated memory bytes to zero, whereas malloc() leaves memory uninitialized with garbage values",
                    "malloc() allocates memory from heap while calloc() allocates from stack",
                    "malloc() requires 2 parameters while calloc() requires 1 parameter",
                    "calloc() can only allocate character array memory"
                ],
                "answer": "calloc() initializes allocated memory bytes to zero, whereas malloc() leaves memory uninitialized with garbage values",
            },
            {
                "question": "What value do malloc(), calloc(), and realloc() return if heap memory allocation fails?",
                "options": ["NULL pointer", "-1 integer", "0 integer", "EOF marker"],
                "answer": "NULL pointer",
            },
            {
                "question": "Why is it recommended to use a temporary pointer `int *temp = realloc(ptr, new_size);` when resizing memory?",
                "options": [
                    "If realloc() fails and returns NULL, assigning directly to ptr (`ptr = realloc(ptr, new_size)`) would overwrite ptr with NULL and cause a memory leak",
                    "Because realloc() deletes the original pointer variable",
                    "Because C compiler forbids reallocating the same pointer",
                    "To automatically convert void* to float*"
                ],
                "answer": "If realloc() fails and returns NULL, assigning directly to ptr (`ptr = realloc(ptr, new_size)`) would overwrite ptr with NULL and cause a memory leak",
            },
            {
                "question": "Is an explicit cast like `(int *)malloc(...)` mandatory in standard C?",
                "options": [
                    "No, malloc() returns void* which is implicitly converted to any object pointer type in C",
                    "Yes, standard C requires explicit casting for all memory allocations",
                    "Yes, without explicit casting malloc() causes compilation error in C",
                    "No, malloc() returns int* by default"
                ],
                "answer": "No, malloc() returns void* which is implicitly converted to any object pointer type in C",
            },
            {
                "question": "What good programming practice should be performed immediately after calling free(ptr)?",
                "options": [
                    "Set ptr to NULL (`ptr = NULL;`) to prevent dangling pointer errors",
                    "Call malloc() to reassign ptr",
                    "Cast ptr to void pointer",
                    "Increment ptr by sizeof(int)"
                ],
                "answer": "Set ptr to NULL (`ptr = NULL;`) to prevent dangling pointer errors",
            },
        ],
        "theory": {
            "definition": "Dynamic memory allocation manages heap memory at runtime using <stdlib.h> functions (malloc, calloc, realloc, free).",
            "why": "Allows programs to allocate memory dynamically when data sizes are unknown at compile time.",
            "rules": [
                "malloc(size): Allocates uninitialized heap bytes.",
                "calloc(n, size): Allocates heap memory for n elements and zeroes all bytes.",
                "realloc(ptr, new_size): Resizes previously allocated block.",
                "free(ptr): Releases allocated heap memory back to system.",
                "NULL Checking: Always verify returned pointer is not NULL before dereferencing.",
                "Set to NULL: Assign ptr = NULL after freeing to avoid dangling pointers."
            ],
            "examples": [
                "#include <stdio.h>\n#include <stdlib.h>\nint main(void) {\n    int *p = malloc(sizeof(int));\n    if (p) { *p = 42; printf(\"%d\\n\", *p); free(p); p = NULL; }\n    return 0;\n}"
            ],
        },
    },

    54: {
        "concept": "A memory leak occurs when dynamically allocated heap memory (malloc/calloc/realloc) is not released using free() after it is no longer needed. Leaked memory remains occupied until program termination. Causes include missing free() calls, overwriting pointers before freeing (ptr = new_ptr), and letting pointers go out of scope. Consequences include system performance degradation, RAM exhaustion, and Out of Memory crashes in long-running servers. Tools like Valgrind detect memory leaks.",
        "syntax": "// Memory Leak Scenario:\nint *ptr = malloc(100 * sizeof(int));\n// ... used ptr ...\nptr = malloc(200 * sizeof(int)); // LEAK! Original block address lost!\n\n// Corrected Code:\nfree(ptr);\nptr = malloc(200 * sizeof(int));\nfree(ptr); ptr = NULL;",
        "example": {
            "code": "#include <stdio.h>\n#include <stdlib.h>\n\nvoid leaking_function(void) {\n    int *ptr = (int *)malloc(5 * sizeof(int));\n    if (ptr == NULL) return;\n    ptr[0] = 10;\n    ptr[1] = 20;\n    printf(\"Values: %d %d\\n\", ptr[0], ptr[1]);\n    // free(ptr); // Added to prevent leak\n    free(ptr);\n}\n\nint main(void) {\n    leaking_function();\n    return 0;\n}",
            "output": "Values: 10 20",
            "explanation": "malloc() allocates heap memory for 5 integers. If free(ptr) is omitted before leaking_function() returns, the local variable ptr is popped off the stack while the heap memory remains allocated and unreachable—causing a memory leak.",
        },
        "fill_blanks": {
            "question": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    int *ptr = malloc(10 * sizeof(int));\n    // ... perform operations ...\n    _____(ptr); // Prevent memory leak by releasing heap memory\n    ptr = _____; // Prevent dangling pointer\n    return 0;\n}",
            "answers": ["free", "NULL"],
            "options": ["free", "NULL", "malloc", "realloc", "0", "exit"],
        },
        "compiler": {
            "title": "C Memory Leak Prevention Sandbox",
            "question": "Add free() and NULL assignment to prevent memory leaks.",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    int *data = malloc(100 * sizeof(int));\n    if (data == NULL) return 1;\n\n    printf(\"Memory allocated safely\\n\");\n    _____(data);\n    data = _____;\n    return 0;\n}",
            "options": ["free", "NULL", "malloc", "0"],
        },
        "skill_exa_test": [
            {
                "question": "What is a Memory Leak in C programming?",
                "options": [
                    "Occurs when dynamically allocated heap memory is not released using free() after it is no longer needed",
                    "Occurs when a local stack variable exceeds 4 bytes",
                    "Occurs when a global variable is initialized to 0",
                    "Occurs when a pointer is assigned a NULL value"
                ],
                "answer": "Occurs when dynamically allocated heap memory is not released using free() after it is no longer needed",
            },
            {
                "question": "What happens if a pointer variable holding a heap memory address is overwritten (`ptr = new_address`) before freeing the original memory block?",
                "options": [
                    "The original heap memory address is lost, making it unreachable and causing a memory leak",
                    "The compiler automatically frees the original memory block",
                    "The program throws an automatic Garbage Collection exception",
                    "The two memory blocks are merged into one"
                ],
                "answer": "The original heap memory address is lost, making it unreachable and causing a memory leak",
            },
            {
                "question": "Which command-line memory analysis tool is widely used on Linux systems to detect memory leaks and invalid memory accesses in C programs?",
                "options": ["Valgrind", "GDB", "GCC", "Make"],
                "answer": "Valgrind",
            },
            {
                "question": "What is the main danger of memory leaks in long-running applications like web servers or daemon services?",
                "options": [
                    "Accumulated leaked memory gradually exhausts system RAM, eventually causing application crashes or Out of Memory (OOM) errors",
                    "The C preprocessor deletes the executable binary file",
                    "The CPU clock speed drops to zero",
                    "Floating point calculations lose precision"
                ],
                "answer": "Accumulated leaked memory gradually exhausts system RAM, eventually causing application crashes or Out of Memory (OOM) errors",
            },
            {
                "question": "Which of the following is a recommended best practice to prevent memory leaks in C?",
                "options": [
                    "Ensure every call to malloc(), calloc(), or realloc() has a corresponding free() call when memory is no longer needed",
                    "Avoid using pointers anywhere in C programs",
                    "Use global static variables for all temporary data allocations",
                    "Call malloc() inside an infinite loop without free()"
                ],
                "answer": "Ensure every call to malloc(), calloc(), or realloc() has a corresponding free() call when memory is no longer needed",
            },
        ],
        "theory": {
            "definition": "A memory leak occurs when dynamically allocated heap memory is not released back to the system after use, wasting memory resources.",
            "why": "Preventing memory leaks is essential for application stability, performance, and preventing Out of Memory crashes in long-running software.",
            "rules": [
                "Pair Allocation and Deallocation: Every malloc/calloc/realloc must be matched with free().",
                "Pointer Overwrites: Never reassign a pointer before freeing its existing memory address.",
                "Scope Rules: Free dynamically allocated memory before pointer variables go out of scope.",
                "Long-Running Applications: Unfreed memory accumulates over time in servers/daemons.",
                "Detection Tools: Use tools like Valgrind or AddressSanitizer (ASan) to audit memory leaks."
            ],
            "examples": [
                "#include <stdio.h>\n#include <stdlib.h>\nint main(void) {\n    int *p = malloc(10 * sizeof(int));\n    if (p) { free(p); p = NULL; }\n    return 0;\n}"
            ],
        },
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

    theory = core.get("theory")
    if not isinstance(theory, dict):
        theory = {
            "definition": concept,
            "why": f"{title} builds essential foundational skills in C software development.",
            "rules": [
                "Always include required standard header files like <stdio.h>.",
                "Ensure variables are declared before use.",
                "Verify format specifiers match variable data types.",
            ],
            "examples": [example.get("code", "")],
        }

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
        "theory": theory,
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
