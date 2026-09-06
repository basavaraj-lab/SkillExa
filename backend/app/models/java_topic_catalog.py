"""Java Enterprise Curriculum Catalog and Content Builder for 120 topics across 18 modules."""
from __future__ import annotations

JAVA_TOPIC_CATALOG = [
    # 1. Basics
    {"id": 1, "title": "Introduction to Java", "difficulty": "Beginner", "duration": "20 min", "category": "Basics"},
    {"id": 2, "title": "Creating First Java Application in IntelliJ IDEA", "difficulty": "Beginner", "duration": "20 min", "category": "Basics"},
    {"id": 3, "title": "JDK vs JRE vs JVM", "difficulty": "Beginner", "duration": "20 min", "category": "Basics"},
    {"id": 4, "title": "Print Output", "difficulty": "Beginner", "duration": "15 min", "category": "Basics"},
    {"id": 5, "title": "Taking Input", "difficulty": "Beginner", "duration": "25 min", "category": "Basics"},
    {"id": 6, "title": "Identifiers", "difficulty": "Beginner", "duration": "15 min", "category": "Basics"},
    {"id": 7, "title": "Keywords", "difficulty": "Beginner", "duration": "15 min", "category": "Basics"},
    {"id": 8, "title": "Variables and Data Types", "difficulty": "Beginner", "duration": "25 min", "category": "Basics"},
    {"id": 9, "title": "Wrapper Classes", "difficulty": "Beginner", "duration": "25 min", "category": "Basics"},
    {"id": 10, "title": "Operators", "difficulty": "Beginner", "duration": "30 min", "category": "Basics"},

    # 2. Decision Making and Loops
    {"id": 11, "title": "Decision Making", "difficulty": "Beginner", "duration": "30 min", "category": "Decision Making and Loops"},
    {"id": 12, "title": "Loops and Jump Statements", "difficulty": "Intermediate", "duration": "35 min", "category": "Decision Making and Loops"},

    # 3. Methods
    {"id": 13, "title": "Methods – Introduction", "difficulty": "Intermediate", "duration": "30 min", "category": "Methods"},
    {"id": 14, "title": "Static Methods vs Instance Methods", "difficulty": "Intermediate", "duration": "30 min", "category": "Methods"},
    {"id": 15, "title": "Access Modifiers", "difficulty": "Intermediate", "duration": "25 min", "category": "Methods"},
    {"id": 16, "title": "Command Line Arguments", "difficulty": "Intermediate", "duration": "20 min", "category": "Methods"},
    {"id": 17, "title": "Variable Arguments (Varargs)", "difficulty": "Intermediate", "duration": "25 min", "category": "Methods"},

    # 4. Arrays
    {"id": 18, "title": "Arrays – Introduction", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays"},
    {"id": 19, "title": "Multi-Dimensional Arrays", "difficulty": "Intermediate", "duration": "35 min", "category": "Arrays"},
    {"id": 20, "title": "Jagged Arrays", "difficulty": "Intermediate", "duration": "30 min", "category": "Arrays"},
    {"id": 21, "title": "Arrays Class", "difficulty": "Intermediate", "duration": "25 min", "category": "Arrays"},
    {"id": 22, "title": "Final Arrays", "difficulty": "Intermediate", "duration": "20 min", "category": "Arrays"},

    # 5. Strings
    {"id": 23, "title": "Strings – Introduction", "difficulty": "Intermediate", "duration": "30 min", "category": "Strings"},
    {"id": 24, "title": ".equals() vs ==", "difficulty": "Intermediate", "duration": "25 min", "category": "Strings"},
    {"id": 25, "title": "String Methods", "difficulty": "Intermediate", "duration": "30 min", "category": "Strings"},
    {"id": 26, "title": "String Class", "difficulty": "Intermediate", "duration": "25 min", "category": "Strings"},
    {"id": 27, "title": "StringBuffer Class", "difficulty": "Intermediate", "duration": "30 min", "category": "Strings"},
    {"id": 28, "title": "StringBuilder Class", "difficulty": "Intermediate", "duration": "30 min", "category": "Strings"},
    {"id": 29, "title": "Strings vs StringBuffer vs StringBuilder", "difficulty": "Advanced", "duration": "35 min", "category": "Strings"},

    # 6. Object-Oriented Programming (OOP)
    {"id": 30, "title": "OOP Concepts – Introduction", "difficulty": "Intermediate", "duration": "35 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 31, "title": "this Keyword", "difficulty": "Intermediate", "duration": "25 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 32, "title": "super Keyword", "difficulty": "Intermediate", "duration": "25 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 33, "title": "Encapsulation", "difficulty": "Intermediate", "duration": "30 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 34, "title": "Inheritance", "difficulty": "Advanced", "duration": "40 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 35, "title": "Polymorphism", "difficulty": "Advanced", "duration": "40 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 36, "title": "Abstraction", "difficulty": "Advanced", "duration": "35 min", "category": "Object-Oriented Programming (OOP)"},
    {"id": 37, "title": "Object Class", "difficulty": "Intermediate", "duration": "25 min", "category": "Object-Oriented Programming (OOP)"},

    # 7. Packages and Interfaces
    {"id": 38, "title": "Packages", "difficulty": "Intermediate", "duration": "25 min", "category": "Packages and Interfaces"},
    {"id": 39, "title": "Interfaces", "difficulty": "Intermediate", "duration": "35 min", "category": "Packages and Interfaces"},
    {"id": 40, "title": "Class vs Interface", "difficulty": "Intermediate", "duration": "25 min", "category": "Packages and Interfaces"},
    {"id": 41, "title": "Functional Interface", "difficulty": "Advanced", "duration": "30 min", "category": "Packages and Interfaces"},
    {"id": 42, "title": "Nested Interface", "difficulty": "Advanced", "duration": "25 min", "category": "Packages and Interfaces"},
    {"id": 43, "title": "Marker Interface", "difficulty": "Advanced", "duration": "25 min", "category": "Packages and Interfaces"},

    # 8. Exception Handling
    {"id": 44, "title": "Exception Handling – Introduction", "difficulty": "Intermediate", "duration": "30 min", "category": "Exception Handling"},
    {"id": 45, "title": "Try-Catch Block", "difficulty": "Intermediate", "duration": "30 min", "category": "Exception Handling"},
    {"id": 46, "title": "final, finally and finalize", "difficulty": "Intermediate", "duration": "30 min", "category": "Exception Handling"},
    {"id": 47, "title": "throw and throws", "difficulty": "Advanced", "duration": "30 min", "category": "Exception Handling"},
    {"id": 48, "title": "Customized Exception Handling", "difficulty": "Advanced", "duration": "35 min", "category": "Exception Handling"},
    {"id": 49, "title": "Chained Exceptions", "difficulty": "Advanced", "duration": "30 min", "category": "Exception Handling"},
    {"id": 50, "title": "Null Pointer Exceptions", "difficulty": "Intermediate", "duration": "25 min", "category": "Exception Handling"},
    {"id": 51, "title": "Exception Handling with Method Overriding", "difficulty": "Advanced", "duration": "35 min", "category": "Exception Handling"},

    # 9. Regular Expressions (Regex)
    {"id": 52, "title": "Regex – Introduction", "difficulty": "Intermediate", "duration": "30 min", "category": "Regular Expressions (Regex)"},
    {"id": 53, "title": "Matcher Class", "difficulty": "Advanced", "duration": "30 min", "category": "Regular Expressions (Regex)"},
    {"id": 54, "title": "Character Class", "difficulty": "Intermediate", "duration": "25 min", "category": "Regular Expressions (Regex)"},
    {"id": 55, "title": "Quantifiers", "difficulty": "Intermediate", "duration": "25 min", "category": "Regular Expressions (Regex)"},

    # 10. Memory Allocation
    {"id": 56, "title": "Java Memory Management", "difficulty": "Advanced", "duration": "35 min", "category": "Memory Allocation"},
    {"id": 57, "title": "How Java Objects Are Stored in Memory", "difficulty": "Advanced", "duration": "35 min", "category": "Memory Allocation"},
    {"id": 58, "title": "Types of Memory Areas Allocated by JVM", "difficulty": "Advanced", "duration": "40 min", "category": "Memory Allocation"},
    {"id": 59, "title": "Stack vs Heap Memory Allocation", "difficulty": "Advanced", "duration": "35 min", "category": "Memory Allocation"},
    {"id": 60, "title": "Garbage Collection", "difficulty": "Advanced", "duration": "40 min", "category": "Memory Allocation"},
    {"id": 61, "title": "Types of JVM Garbage Collectors", "difficulty": "Advanced", "duration": "40 min", "category": "Memory Allocation"},
    {"id": 62, "title": "Memory Leaks", "difficulty": "Advanced", "duration": "30 min", "category": "Memory Allocation"},

    # 11. Generics
    {"id": 63, "title": "Generic Classes", "difficulty": "Advanced", "duration": "35 min", "category": "Generics"},
    {"id": 64, "title": "Wildcards", "difficulty": "Advanced", "duration": "35 min", "category": "Generics"},
    {"id": 65, "title": "Bounded Types", "difficulty": "Advanced", "duration": "30 min", "category": "Generics"},
    {"id": 66, "title": "Type Erasure", "difficulty": "Advanced", "duration": "30 min", "category": "Generics"},

    # 12. Collections
    {"id": 67, "title": "Collections Class", "difficulty": "Intermediate", "duration": "30 min", "category": "Collections"},
    {"id": 68, "title": "Collection Interface", "difficulty": "Intermediate", "duration": "30 min", "category": "Collections"},
    {"id": 69, "title": "List Interface", "difficulty": "Intermediate", "duration": "35 min", "category": "Collections"},
    {"id": 70, "title": "Set Interface", "difficulty": "Intermediate", "duration": "35 min", "category": "Collections"},
    {"id": 71, "title": "Queue Interface", "difficulty": "Intermediate", "duration": "30 min", "category": "Collections"},
    {"id": 72, "title": "Map Interface", "difficulty": "Intermediate", "duration": "40 min", "category": "Collections"},
    {"id": 73, "title": "Iterator", "difficulty": "Intermediate", "duration": "25 min", "category": "Collections"},
    {"id": 74, "title": "Comparator Interface", "difficulty": "Advanced", "duration": "35 min", "category": "Collections"},
    {"id": 75, "title": "Comparable Interface", "difficulty": "Advanced", "duration": "35 min", "category": "Collections"},
    {"id": 76, "title": "Collection Framework – Complete Tutorial", "difficulty": "Advanced", "duration": "60 min", "category": "Collections"},

    # 13. Java 8+ Features
    {"id": 77, "title": "Lambda Expressions", "difficulty": "Advanced", "duration": "40 min", "category": "Java 8+ Features"},
    {"id": 78, "title": "Predicate", "difficulty": "Advanced", "duration": "30 min", "category": "Java 8+ Features"},
    {"id": 79, "title": "Consumer", "difficulty": "Advanced", "duration": "30 min", "category": "Java 8+ Features"},
    {"id": 80, "title": "Supplier", "difficulty": "Advanced", "duration": "30 min", "category": "Java 8+ Features"},
    {"id": 81, "title": "Method References", "difficulty": "Advanced", "duration": "35 min", "category": "Java 8+ Features"},
    {"id": 82, "title": "Streams", "difficulty": "Advanced", "duration": "45 min", "category": "Java 8+ Features"},
    {"id": 83, "title": "Optional", "difficulty": "Advanced", "duration": "30 min", "category": "Java 8+ Features"},
    {"id": 84, "title": "Collectors", "difficulty": "Advanced", "duration": "35 min", "category": "Java 8+ Features"},

    # 14. Date and Time API
    {"id": 85, "title": "Date and Time API – Introduction", "difficulty": "Intermediate", "duration": "25 min", "category": "Date and Time API"},
    {"id": 86, "title": "LocalDate", "difficulty": "Intermediate", "duration": "25 min", "category": "Date and Time API"},
    {"id": 87, "title": "LocalTime", "difficulty": "Intermediate", "duration": "25 min", "category": "Date and Time API"},
    {"id": 88, "title": "LocalDateTime", "difficulty": "Intermediate", "duration": "25 min", "category": "Date and Time API"},
    {"id": 89, "title": "Duration", "difficulty": "Intermediate", "duration": "25 min", "category": "Date and Time API"},
    {"id": 90, "title": "Period", "difficulty": "Intermediate", "duration": "25 min", "category": "Date and Time API"},
    {"id": 91, "title": "DateTimeFormatter", "difficulty": "Intermediate", "duration": "30 min", "category": "Date and Time API"},

    # 15. Multithreading and Synchronization
    {"id": 92, "title": "Multithreading and Synchronization – Introduction", "difficulty": "Advanced", "duration": "35 min", "category": "Multithreading and Synchronization"},
    {"id": 93, "title": "Thread.start() vs Thread.run()", "difficulty": "Advanced", "duration": "30 min", "category": "Multithreading and Synchronization"},
    {"id": 94, "title": "Main Thread", "difficulty": "Advanced", "duration": "25 min", "category": "Multithreading and Synchronization"},
    {"id": 95, "title": "Thread Priority", "difficulty": "Advanced", "duration": "25 min", "category": "Multithreading and Synchronization"},
    {"id": 96, "title": "Synchronization and Thread Safety", "difficulty": "Advanced", "duration": "40 min", "category": "Multithreading and Synchronization"},
    {"id": 97, "title": "Locks and Reentrant Lock", "difficulty": "Advanced", "duration": "40 min", "category": "Multithreading and Synchronization"},
    {"id": 98, "title": "Deadlock", "difficulty": "Advanced", "duration": "35 min", "category": "Multithreading and Synchronization"},
    {"id": 99, "title": "Thread Pools", "difficulty": "Advanced", "duration": "40 min", "category": "Multithreading and Synchronization"},
    {"id": 100, "title": "Multithreading – Complete Tutorial", "difficulty": "Advanced", "duration": "60 min", "category": "Multithreading and Synchronization"},

    # 16. File Handling
    {"id": 101, "title": "Introduction to Java I/O", "difficulty": "Intermediate", "duration": "30 min", "category": "File Handling"},
    {"id": 102, "title": "Reader Class", "difficulty": "Intermediate", "duration": "25 min", "category": "File Handling"},
    {"id": 103, "title": "Writer Class", "difficulty": "Intermediate", "duration": "25 min", "category": "File Handling"},
    {"id": 104, "title": "File Handling", "difficulty": "Intermediate", "duration": "35 min", "category": "File Handling"},
    {"id": 105, "title": "BufferedReader Input Stream", "difficulty": "Intermediate", "duration": "30 min", "category": "File Handling"},
    {"id": 106, "title": "BufferedReader Output Stream", "difficulty": "Intermediate", "duration": "30 min", "category": "File Handling"},
    {"id": 107, "title": "FilePermission Class", "difficulty": "Advanced", "duration": "25 min", "category": "File Handling"},
    {"id": 108, "title": "FileDescriptor Class", "difficulty": "Advanced", "duration": "25 min", "category": "File Handling"},

    # 17. Networking
    {"id": 109, "title": "Networking – Introduction", "difficulty": "Intermediate", "duration": "30 min", "category": "Networking"},
    {"id": 110, "title": "Socket Programming", "difficulty": "Advanced", "duration": "45 min", "category": "Networking"},
    {"id": 111, "title": "ServerSocket Class", "difficulty": "Advanced", "duration": "40 min", "category": "Networking"},
    {"id": 112, "title": "URL Class and Methods", "difficulty": "Intermediate", "duration": "30 min", "category": "Networking"},

    # 18. Java Database Connectivity (JDBC)
    {"id": 113, "title": "JDBC – Introduction", "difficulty": "Intermediate", "duration": "35 min", "category": "Java Database Connectivity (JDBC)"},
    {"id": 114, "title": "JDBC Driver", "difficulty": "Intermediate", "duration": "30 min", "category": "Java Database Connectivity (JDBC)"},
    {"id": 115, "title": "JDBC Connection", "difficulty": "Intermediate", "duration": "35 min", "category": "Java Database Connectivity (JDBC)"},
    {"id": 116, "title": "Types of Statements in JDBC", "difficulty": "Advanced", "duration": "40 min", "category": "Java Database Connectivity (JDBC)"},
    {"id": 117, "title": "Transactions", "difficulty": "Advanced", "duration": "35 min", "category": "Java Database Connectivity (JDBC)"},
    {"id": 118, "title": "ResultSet", "difficulty": "Intermediate", "duration": "30 min", "category": "Java Database Connectivity (JDBC)"},
    {"id": 119, "title": "Metadata", "difficulty": "Advanced", "duration": "30 min", "category": "Java Database Connectivity (JDBC)"},
    {"id": 120, "title": "Connection Pooling", "difficulty": "Advanced", "duration": "40 min", "category": "Java Database Connectivity (JDBC)"},
]


def _build_java_topic(meta: dict[str, str | int]) -> dict[str, object]:
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
        "concept": f"Mastering {title} in Java provides enterprise-grade object-oriented system stability and JVM memory management.",
        "syntax": f"// Java {title} syntax\npublic class Main {{\n    public static void main(String[] args) {{\n        System.out.println(\"{title} in Java\");\n    }}\n}}",
        "example": {
            "code": f"public class Main {{\n    public static void main(String[] args) {{\n        System.out.println(\"SkillExa Java Track: {title}\");\n    }}\n}}",
            "output": f"SkillExa Java Track: {title}",
            "explanation": f"Demonstrates core usage of {title} in standard Java 17 enterprise execution.",
        },
        "fill_blanks": {
            "question": f"public class Main {{\n    public static void main(String[] args) {{\n        System.out.____(\"{title}\");\n    }}\n}}",
            "answers": ["println"],
            "options": ["println", "print", "out", "log"],
        },
        "compiler": {
            "title": f"Java Practice - {title}",
            "question": f"Complete the Java class to print output using System.out.println.",
            "starter_code": f"public class Main {{\n    public static void main(String[] args) {{\n        System.out.____(\"Learning {title} on SkillExa!\");\n    }}\n}}",
            "options": ["println", "print", "write", "display"],
        },
        "skill_exa_test": [
            {
                "question": f"Which standard method is the entry point for executing a Java application for {title}?",
                "options": ["public static void main(String[] args)", "public void main()", "public static int main()", "void start()"],
                "answer": "public static void main(String[] args)",
            }
        ],
    }


JAVA_TOPICS: dict[int, dict[str, object]] = {
    meta["id"]: _build_java_topic(meta) for meta in JAVA_TOPIC_CATALOG
}

# Specific overrides for Topic 1 & 3
JAVA_TOPICS[1] = {
    "id": 1,
    "title": "Introduction to Java",
    "category": "Basics",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "Java is a class-based, object-oriented programming language designed by James Gosling at Sun Microsystems to 'Write Once, Run Anywhere' (WORA) via JVM bytecode.",
    "syntax": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, Java!\");\n    }\n}",
    "example": {
        "code": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Welcome to SkillExa Java Track!\");\n    }\n}",
        "output": "Welcome to SkillExa Java Track!",
        "explanation": "public class Main defines the primary class containing main entry method.",
    },
    "fill_blanks": {
        "question": "public class Main {{\n    public _____ void main(String[] args) {{\n        System.out.println(\"Hello Java!\");\n    }}\n}}",
        "answers": ["static"],
        "options": ["static", "final", "abstract", "native"],
    },
    "compiler": {
        "title": "Hello Java World",
        "question": "Complete the program to output greeting in Java.",
        "starter_code": "public class Main {\n    public static void main(String[] args) {\n        System.out.____(\"Welcome to SkillExa Java Track!\\n\");\n    }\n}",
        "options": ["println", "print", "printf", "write"],
    },
    "skill_exa_test": [
        {
            "question": "Which philosophy describes Java's cross-platform portability?",
            "options": ["Write Once, Run Anywhere (WORA)", "Compile Once, Run Never", "Write Everywhere, Test Nowhere", "Run Once, Write Many"],
            "answer": "Write Once, Run Anywhere (WORA)",
        }
    ],
}

JAVA_TOPICS[3] = {
    "id": 3,
    "title": "JDK vs JRE vs JVM",
    "category": "Basics",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "JVM (Java Virtual Machine) executes bytecode; JRE (Java Runtime Environment) provides JVM + core libraries; JDK (Java Development Kit) includes JRE + development tools like javac.",
    "syntax": "javac Main.java  // Compile to bytecode\njava Main        // Execute on JVM",
    "example": {
        "code": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"JDK contains JRE and javac compiler.\");\n    }\n}",
        "output": "JDK contains JRE and javac compiler.",
        "explanation": "javac compiles Java source code (.java) into JVM bytecode (.class).",
    },
    "fill_blanks": {
        "question": "The _____ compiler converts Java code into bytecode.",
        "answers": ["javac"],
        "options": ["javac", "gcc", "g++", "python"],
    },
    "compiler": {
        "title": "JVM Concept Practice",
        "question": "Complete the Java code to print JVM execution concept.",
        "starter_code": "public class Main {\n    public static void main(String[] args) {\n        System.out.____(\"JVM executes bytecode!\");\n    }\n}",
        "options": ["println", "print", "log", "out"],
    },
    "skill_exa_test": [
        {
            "question": "Which component of Java is responsible for compiling .java files into bytecode?",
            "options": ["JDK (javac)", "JVM", "JRE", "JAR"],
            "answer": "JDK (javac)",
        }
    ],
}
