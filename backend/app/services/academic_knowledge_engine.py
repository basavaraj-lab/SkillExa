import re
from typing import Any, Dict, List, Optional, Tuple

# Common student spelling mistakes and phonetic variants
TYPO_CORRECTIONS = {
    "pyhton": "python",
    "pythn": "python",
    "pyton": "python",
    "javascrip": "javascript",
    "javscript": "javascript",
    "js": "javascript",
    "c++": "cpp",
    "cplusplus": "cpp",
    "recurtion": "recursion",
    "recursiv": "recursion",
    "pointr": "pointer",
    "pointes": "pointers",
    "inheritence": "inheritance",
    "inheretence": "inheritance",
    "polymorphysm": "polymorphism",
    "encapsulaton": "encapsulation",
    "microprossesor": "microprocessor",
    "microprocesor": "microprocessor",
    "8085": "8085 microprocessor",
    "8086": "8086 microprocessor",
    "linklist": "linked list",
    "linkelist": "linked list",
    "datastructure": "data structures",
    "algoritm": "algorithm",
    "algortihm": "algorithm",
    "binarytree": "binary tree",
    "varible": "variable",
    "varables": "variables",
    "functon": "function",
    "functons": "functions",
}


def normalize_query(query: str) -> str:
    """Normalize whitespace, lower-case, and correct common student typos."""
    clean = re.sub(r"[^\w\s+#.-]", " ", query.lower()).strip()
    words = clean.split()
    corrected = [TYPO_CORRECTIONS.get(w, w) for w in words]
    return " ".join(corrected)


# Comprehensive Educational Knowledge Base
ACADEMIC_TOPICS: Dict[str, Dict[str, Any]] = {
    "css": {
        "title": "Cascading Style Sheets (CSS)",
        "badge": "🎨 CSS",
        "definition": (
            "CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation, "
            "formatting, layout, and visual appearance of a document written in HTML or XML."
        ),
        "explanation": (
            "If HTML is the skeleton and structure of a house (walls, doors, windows), CSS is the interior "
            "design, paint colors, wallpapers, lighting, and layout arrangement that make it look attractive."
        ),
        "features": [
            "**Separation of Concerns**: Separates website design and styling from HTML content structure.",
            "**Responsive Web Design**: Uses Flexbox, CSS Grid, and Media Queries for mobile and desktop screens.",
            "**Cascade & Specificity**: Rules cascade based on importance, specificity, and source order.",
            "**Animations & Transitions**: Enables smooth visual effects without requiring heavy JavaScript.",
        ],
        "applications": [
            "Styling modern responsive web apps across phones, tablets, and desktops.",
            "Building consistent design systems and UI component libraries (Tailwind, Bootstrap).",
        ],
        "example_code": (
            "/* Basic CSS Styling Example */\n"
            ".skillexa-card {\n"
            "    background-color: #4F46E5;\n"
            "    color: #FFFFFF;\n"
            "    padding: 16px;\n"
            "    border-radius: 8px;\n"
            "    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);\n"
            "    transition: transform 0.2s ease;\n"
            "}\n"
            ".skillexa-card:hover {\n"
            "    transform: translateY(-4px);\n"
            "}\n"
        ),
        "example_output": (
            "/* Renders an indigo card with white text, rounded corners, soft shadow, and hover elevation */\n"
        ),
        "line_by_line": [
            "`.skillexa-card`: Class selector that applies styles to matching HTML elements.",
            "`background-color: #4F46E5`: Sets the background to indigo.",
            "`border-radius: 8px`: Rounds the corners of the card.",
            "`.skillexa-card:hover`: Pseudo-class that elevates the card when the user hovers over it.",
        ],
        "summary": (
            "CSS controls colors, fonts, layouts, and responsive behavior for all modern websites."
        ),
        "spoken": (
            "CSS stands for Cascading Style Sheets. It is used to design and format the layout, colors, "
            "and visual styling of web pages written in HTML."
        ),
    },

    "html": {
        "title": "HyperText Markup Language (HTML)",
        "badge": "🌐 HTML",
        "definition": (
            "HTML (HyperText Markup Language) is the standard markup language used to create and structure "
            "web pages and web applications."
        ),
        "explanation": (
            "HTML serves as the architectural skeleton of every website. It organizes content into headings, "
            "paragraphs, images, links, forms, and lists using tags and semantic elements."
        ),
        "features": [
            "**Semantic Elements**: `<header>`, `<nav>`, `<main>`, `<article>`, `<footer>` improve accessibility and SEO.",
            "**Hyperlinks**: Uses `<a>` tags to connect documents across the World Wide Web.",
            "**Multimedia Support**: Native audio, video (`<audio>`, `<video>`), and SVG graphics.",
            "**Forms & User Input**: Inputs, buttons, selects, and textareas for collecting user submissions.",
        ],
        "applications": [
            "Foundation of every website, web application, email template, and hybrid mobile view.",
        ],
        "example_code": (
            "<!DOCTYPE html>\n"
            "<html lang=\"en\">\n"
            "<head>\n"
            "    <meta charset=\"UTF-8\">\n"
            "    <title>SkillExa Learn</title>\n"
            "</head>\n"
            "<body>\n"
            "    <h1>Welcome to SkillExa</h1>\n"
            "    <p>Empowering students with AI-driven learning.</p>\n"
            "    <a href=\"https://skillexa.onrender.com\">Start Practicing</a>\n"
            "</body>\n"
            "</html>\n"
        ),
        "example_output": (
            "SkillExa Learn - Heading, paragraph, and interactive practice link displayed.\n"
        ),
        "line_by_line": [
            "`<!DOCTYPE html>`: Declares that the document follows HTML5 specifications.",
            "`<head>`: Contains metadata, character encoding, and the page title.",
            "`<body>`: Holds all visible page content such as headings and links.",
            "`<a href=...>`: Creates a hyperlink to navigate to another page or URL.",
        ],
        "summary": (
            "HTML provides the structural skeleton of the web, organizing content into tags and elements."
        ),
        "spoken": (
            "HTML stands for HyperText Markup Language. It provides the core structure and skeleton of web pages, "
            "organizing content into headings, paragraphs, and links."
        ),
    },

    "html vs css": {
        "title": "HTML vs CSS: Differences & Comparison",
        "badge": "⚖️ HTML vs CSS",
        "definition": (
            "HTML (HyperText Markup Language) defines the structure and content of a web page, while CSS (Cascading Style Sheets) "
            "defines the visual styling, presentation, and layout."
        ),
        "explanation": (
            "A great analogy is building a car: HTML is the engine, chassis, and body panels (structure); "
            "CSS is the paint job, leather seat upholstery, and sleek aesthetic design (styling)."
        ),
        "features": [
            "**Role**: HTML organizes content (text, images, forms); CSS formats content (colors, sizes, grids).",
            "**Syntax**: HTML uses angle bracket tags `<p>text</p>`; CSS uses selector-rule blocks `p { color: blue; }`.",
            "**File Extension**: HTML uses `.html`; CSS uses `.css`.",
            "**Interdependence**: CSS requires HTML elements to style; HTML without CSS looks plain and unstyled.",
        ],
        "applications": [
            "Front-end web development, responsive user interfaces, and cross-platform UI design.",
        ],
        "example_code": (
            "<!-- index.html -->\n"
            "<button class=\"cta-btn\">Click Me</button>\n"
            "\n"
            "/* styles.css */\n"
            ".cta-btn {\n"
            "    background-color: #2563EB;\n"
            "    color: white;\n"
            "    padding: 10px 20px;\n"
            "    border: none;\n"
            "    border-radius: 5px;\n"
            "}\n"
        ),
        "example_output": (
            "HTML creates the clickable button element, and CSS styles it with blue background and rounded corners.\n"
        ),
        "line_by_line": [
            "`<button class=\"cta-btn\">`: HTML defines the functional interactive element.",
            "`.cta-btn`: CSS selects the element to set color, padding, and border radius.",
        ],
        "summary": (
            "HTML builds the content structure; CSS makes it beautiful and responsive."
        ),
        "spoken": (
            "HTML defines the structure and content of a web page, while CSS controls the visual layout, "
            "colors, and styling. HTML is the skeleton, and CSS is the design."
        ),
    },

    "java": {
        "title": "Java Programming Language",
        "badge": "☕ Java",
        "definition": (
            "Java is a high-level, class-based, object-oriented, platform-independent programming language "
            "designed by James Gosling at Sun Microsystems in 1995. Its core principle is 'Write Once, Run Anywhere' (WORA)."
        ),
        "explanation": (
            "Java source code compiles into platform-neutral bytecode (`.class` files), which executes inside the "
            "Java Virtual Machine (JVM) on any operating system, with automatic garbage collection managing memory."
        ),
        "features": [
            "**Platform Independent (JVM)**: Runs on Windows, Linux, macOS, and Android without recompilation.",
            "**Strongly Typed & Object-Oriented**: Strictly enforces classes, encapsulation, inheritance, and polymorphism.",
            "**Automatic Memory Management**: Garbage Collector reclaims unused heap memory automatically.",
            "**Robust Security & Multithreading**: Built-in support for concurrent execution and byte-code verification.",
        ],
        "applications": [
            "Enterprise backend systems (Spring Boot, Jakarta EE).",
            "Android mobile applications and high-frequency financial trading systems.",
        ],
        "example_code": (
            "public class SkillExaStudent {\n"
            "    private String name;\n"
            "\n"
            "    public SkillExaStudent(String name) {\n"
            "        this.name = name;\n"
            "    }\n"
            "\n"
            "    public void display() {\n"
            "        System.out.println(\"Student: \" + this.name);\n"
            "    }\n"
            "\n"
            "    public static void main(String[] args) {\n"
            "        SkillExaStudent s = new SkillExaStudent(\"Ganesh\");\n"
            "        s.display();\n"
            "    }\n"
            "}\n"
        ),
        "example_output": (
            "Student: Ganesh\n"
        ),
        "line_by_line": [
            "`public class SkillExaStudent`: Declares a blueprint class.",
            "`private String name`: Encapsulated instance variable.",
            "`public static void main(String[] args)`: Program entry point executed by the JVM.",
            "`s.display()`: Calls the instance method on the allocated object.",
        ],
        "summary": (
            "Java is a bedrock language for enterprise backends, cloud microservices, and Android development."
        ),
        "spoken": (
            "Java is a widely used object-oriented programming language designed for platform independence. "
            "Code compiles to bytecode that runs on the Java Virtual Machine across all operating systems."
        ),
    },

    "stack": {
        "title": "Stack Data Structure (LIFO)",
        "badge": "📚 DSA Stack",
        "definition": (
            "A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle, where "
            "elements are added (pushed) and removed (popped) exclusively from one end, called the top."
        ),
        "explanation": (
            "Think of a physical stack of plates in a cafeteria: the plate placed on top last is always "
            "the first plate you pick up. You cannot remove bottom plates without removing top ones first."
        ),
        "features": [
            "**LIFO Principle**: The most recently inserted element is removed first.",
            "**Core Operations**: `push()` (insert), `pop()` (remove top), `peek()`/`top()` (view top element), `isEmpty()`.",
            "**Constant Time Complexity**: `push`, `pop`, and `peek` all operate in $O(1)$ constant time.",
            "**Memory**: Can be implemented using contiguous dynamic arrays or singly linked lists.",
        ],
        "applications": [
            "Function call call-stack management and recursion handling in CPUs and programming language runtimes.",
            "Undo/Redo functionality in text editors (like VS Code).",
            "Expression parsing, syntax matching (balanced parentheses `({[]})`), and backtracking algorithms (DFS).",
        ],
        "example_code": (
            "# Stack implementation in Python using a list\n"
            "class Stack:\n"
            "    def __init__(self):\n"
            "        self.items = []\n"
            "\n"
            "    def push(self, item):\n"
            "        self.items.append(item)\n"
            "\n"
            "    def pop(self):\n"
            "        if not self.is_empty():\n"
            "            return self.items.pop()\n"
            "        raise IndexError(\"Pop from empty stack\")\n"
            "\n"
            "    def peek(self):\n"
            "        return self.items[-1] if not self.is_empty() else None\n"
            "\n"
            "    def is_empty(self):\n"
            "        return len(self.items) == 0\n"
            "\n"
            "s = Stack()\n"
            "s.push(10)\n"
            "s.push(20)\n"
            "print(\"Popped:\", s.pop())  # 20\n"
            "print(\"Top:\", s.peek())      # 10\n"
        ),
        "example_output": (
            "Popped: 20\n"
            "Top: 10\n"
        ),
        "line_by_line": [
            "`self.items.append(item)`: Adds element to the top of the stack in $O(1)$ time.",
            "`self.items.pop()`: Removes and returns the top element in $O(1)$ time.",
            "`self.items[-1]`: Inspects the top item without removing it.",
        ],
        "summary": (
            "Stacks are fundamental LIFO structures essential for function calls, expression evaluation, and algorithm backtracking."
        ),
        "spoken": (
            "A stack is a linear data structure that follows the Last In, First Out principle. "
            "Elements are inserted with push and removed with pop, both operating in O of 1 time."
        ),
    },

    "aptitude": {
        "title": "Quantitative & Logical Aptitude",
        "badge": "🎯 Aptitude Practice",
        "definition": (
            "Aptitude tests evaluate numerical reasoning, logical deduction, data interpretation, and problem-solving "
            "speed, which are core requirements for campus placements, GATE, SSC, UPSC, and banking examinations."
        ),
        "explanation": (
            "Aptitude tests do not just test mathematical formulas; they test analytical thinking under time pressure. "
            "Mastering shortcuts for percentages, ratios, time & work, and speed makes complex problems solvable in seconds."
        ),
        "features": [
            "**Quantitative Aptitude**: Arithmetic (Percentages, Profit & Loss, Simple & Compound Interest, Ratios).",
            "**Time & Work**: Work done formula $W = \\text{Rate} \\times \\text{Time}$; reciprocal trick for combined work.",
            "**Time, Speed & Distance**: Relative speed, trains, and boats & streams.",
            "**Logical Reasoning**: Syllogisms, blood relations, series completion, and coding-decoding.",
        ],
        "applications": [
            "Technical placement tests (TCS, Infosys, Wipro, Cognizant, Accenture, FAANG).",
            "Government exams (SSC CGL, UPSC CSAT, RRB NTPC, Banking PO/Clerk).",
        ],
        "example_code": (
            "# Aptitude Example: Time & Work Calculation\n"
            "# A completes a task in 12 days; B in 15 days. How many days together?\n"
            "rate_a = 1 / 12\n"
            "rate_b = 1 / 15\n"
            "combined_rate = rate_a + rate_b\n"
            "total_days = 1 / combined_rate\n"
            "\n"
            "print(f\"Combined Work Duration: {total_days:.2f} days\")  # 6.67 days\n"
        ),
        "example_output": (
            "Combined Work Duration: 6.67 days\n"
        ),
        "line_by_line": [
            "`rate_a = 1 / 12`: Fraction of work A accomplishes in 1 day.",
            "`combined_rate = rate_a + rate_b`: Sum of daily contributions.",
            "`total_days = 1 / combined_rate`: Total days required when working simultaneously.",
        ],
        "summary": (
            "Practicing daily aptitude questions is critical for clearing first-round screening tests in tech and government exams."
        ),
        "spoken": (
            "Aptitude tests measure your quantitative, logical, and analytical problem-solving abilities. "
            "They are key for campus placements and competitive examinations like GATE and SSC."
        ),
    },

    "python": {
        "title": "Python Programming Language",
        "badge": "🐍 Python",
        "definition": (
            "Python is a high-level, interpreted, general-purpose programming language known for its "
            "simple syntax, code readability, and developer productivity. Created by Guido van Rossum "
            "and released in 1991, Python emphasizes clear and concise code with structured whitespace indentation."
        ),
        "explanation": (
            "Think of Python like plain English for computers. Instead of writing verbose boilerplate code "
            "with manual memory management (like in C) or strict class definitions (like in Java), "
            "Python lets you express complex algorithms and solutions in very few lines of code."
        ),
        "features": [
            "**Interpreted**: Code runs line-by-line via the Python virtual machine without explicit compilation steps.",
            "**Dynamically Typed**: You do not need to declare variable types (e.g. `x = 10` automatically becomes an integer).",
            "**Extensive Standard Library**: Offers 'batteries included' support for file I/O, networking, regular expressions, and mathematics.",
            "**Multi-Paradigm**: Supports Object-Oriented Programming (OOP), Procedural programming, and Functional patterns.",
            "**Cross-Platform**: Executes consistently on Windows, macOS, Linux, and embedded microcontrollers (MicroPython).",
        ],
        "applications": [
            "**Web Development**: Backend frameworks including FastAPI, Django, and Flask.",
            "**Artificial Intelligence & Data Science**: PyTorch, TensorFlow, Scikit-learn, and Pandas.",
            "**Automation & Scripting**: Automating spreadsheets, web scraping (BeautifulSoup), and cloud pipelines.",
            "**Academic & Engineering Computing**: Scientific simulations, DSP, and algorithm prototyping.",
        ],
        "example_code": (
            "# Basic Python variables, lists, and functions\n"
            "def welcome_student(name: str, topics: list):\n"
            "    print(f\"Welcome to SkillExa, {name}!\")\n"
            "    print(f\"You are studying: {', '.join(topics)}\")\n"
            "\n"
            "student_name = \"SkillExa Student\"\n"
            "study_list = [\"Python\", \"DSA\", \"AI\"]\n"
            "welcome_student(student_name, study_list)\n"
        ),
        "example_output": (
            "Welcome to SkillExa, SkillExa Student!\n"
            "You are studying: Python, DSA, AI\n"
        ),
        "line_by_line": [
            "`def welcome_student(...)`: Defines a reusable function taking a student name and topic list.",
            "`f\"Welcome to SkillExa, {name}!\"`: Uses Python 3 f-strings for clear, readable string interpolation.",
            "`', '.join(topics)`: Concatenates list elements with commas into a clean output string.",
            "`welcome_student(...)`: Calls the function with our defined variables.",
        ],
        "summary": (
            "Python is the foundational language for modern software engineering, AI, and data science, "
            "making it the ideal first programming language for university and competitive exam students."
        ),
        "spoken": (
            "Python is a high-level, interpreted, general-purpose programming language known for its simple syntax "
            "and readability. It is widely used in web development, automation, data science, artificial intelligence, "
            "and machine learning."
        ),
    },

    "c": {
        "title": "C Programming Language",
        "badge": "⚡ C Language",
        "definition": (
            "C is a general-purpose, procedural, compiled computer programming language developed in 1972 by "
            "Dennis Ritchie at Bell Labs. It provides low-level memory access and maps efficiently to machine "
            "instructions, making it the foundational language of modern computer operating systems and embedded firmware."
        ),
        "explanation": (
            "C is often described as 'portable assembly'. It gives programmers direct control over computer memory "
            "and hardware through pointers, arrays, and bitwise manipulation, while maintaining a readable procedural syntax."
        ),
        "features": [
            "**Procedural & Structured**: Organized into functions and modules with top-down execution.",
            "**Direct Memory Management**: Uses pointers, `malloc()`, and `free()` for fine-grained memory control.",
            "**Fast & Efficient**: Compiles directly to native processor machine code with near-zero runtime overhead.",
            "**Rich Standard Library**: Defined by ANSI/ISO C with standard headers like `<stdio.h>`, `<stdlib.h>`, and `<string.h>`.",
        ],
        "applications": [
            "**Operating Systems**: Core kernels of Linux, macOS (Darwin), and Microsoft Windows.",
            "**Embedded Systems & Microcontrollers**: Firmware for ARM, PIC, AVR, and automotive ECUs.",
            "**Compilers & Virtual Machines**: The official Python runtime (CPython) and JVM are written in C/C++.",
            "**High-Performance Engines**: Databases like SQLite and graphics rendering engines.",
        ],
        "example_code": (
            "#include <stdio.h>\n"
            "\n"
            "int main() {\n"
            "    int score = 95;\n"
            "    printf(\"SkillExa Competitive Score: %d\\n\", score);\n"
            "    return 0;\n"
            "}\n"
        ),
        "example_output": (
            "SkillExa Competitive Score: 95\n"
        ),
        "line_by_line": [
            "`#include <stdio.h>`: Imports the standard input/output header for `printf()`.",
            "`int main()`: Entry point function where program execution begins.",
            "`int score = 95;`: Allocates a signed integer on the stack and initializes it to 95.",
            "`return 0;`: Returns status code 0 indicating successful program termination.",
        ],
        "summary": (
            "Mastering C gives you a deep, rigorous understanding of how computer memory, CPUs, and operating systems function."
        ),
        "spoken": (
            "C is a powerful procedural programming language developed by Dennis Ritchie. It provides low-level memory control "
            "through pointers and is the foundation for operating systems like Linux and Windows."
        ),
    },

    "pointers": {
        "title": "Pointers in C/C++",
        "badge": "📌 Pointers",
        "definition": (
            "A pointer is a variable that stores the hexadecimal memory address of another variable rather than "
            "a direct value. It is declared using the asterisk (`*`) syntax and initialized using the address-of (`&`) operator."
        ),
        "explanation": (
            "Imagine a house has a home address. A normal variable holds what is inside the house (e.g. 42). "
            "A pointer holds the GPS address that tells you where that house is located in computer memory."
        ),
        "features": [
            "**Address-of Operator (`&`)**: Retrieves the RAM memory address where a variable is stored.",
            "**Dereference Operator (`*`)**: Accesses or modifies the actual value located at the stored memory address.",
            "**Pass by Reference**: Allows functions to modify caller variables directly without making slow data copies.",
            "**Dynamic Data Structures**: Pointers form the building blocks of linked lists, binary trees, and graphs.",
        ],
        "applications": [
            "Passing large arrays or structs to functions efficiently.",
            "Dynamic memory allocation using `malloc()`, `calloc()`, and `free()`.",
            "Low-level driver programming, DMA buffers, and hardware register mapping.",
        ],
        "example_code": (
            "#include <stdio.h>\n"
            "\n"
            "void swap(int *a, int *b) {\n"
            "    int temp = *a;\n"
            "    *a = *b;\n"
            "    *b = temp;\n"
            "}\n"
            "\n"
            "int main() {\n"
            "    int x = 10, y = 20;\n"
            "    swap(&x, &y);\n"
            "    printf(\"Swapped values: x = %d, y = %d\\n\", x, y);\n"
            "    return 0;\n"
            "}\n"
        ),
        "example_output": (
            "Swapped values: x = 20, y = 10\n"
        ),
        "line_by_line": [
            "`void swap(int *a, int *b)`: Function receives the memory addresses of two integers.",
            "`int temp = *a;`: Dereferences `a` to copy the value at that address into temporary storage.",
            "`*a = *b;`: Writes the value stored at `b` directly into the memory location pointed to by `a`.",
            "`swap(&x, &y);`: In `main`, passes memory addresses using the `&` operator.",
        ],
        "summary": (
            "Pointers provide direct memory access, enable pass-by-reference, and form the basis for dynamic data structures."
        ),
        "spoken": (
            "A pointer in C is a variable that stores the memory address of another variable. "
            "You use the ampersand operator to get an address, and the asterisk operator to access "
            "the value at that address."
        ),
    },

    "variable": {
        "title": "Variables in Programming",
        "badge": "📦 Variables",
        "definition": (
            "A variable is a named storage location in a computer's memory that holds a value which can be inspected "
            "and modified during program execution."
        ),
        "explanation": (
            "Think of a variable as a labeled cardboard box. The label is the variable's name (e.g. `age`), "
            "and what you put inside the box is the value (e.g. `21`). Whenever you need that number, you refer to the box's name."
        ),
        "features": [
            "**Data Types**: Specifies what kind of information can be stored (integers, floats, strings, booleans).",
            "**Scope & Lifetime**: Determines where in the code the variable is accessible (local vs global).",
            "**Naming Conventions**: In Python: `snake_case` (e.g. `user_count`); in Java/C++: `camelCase` (e.g. `userCount`).",
        ],
        "applications": [
            "Tracking loop counters, scores, student details, database records, and mathematical constants.",
        ],
        "example_code": (
            "# Python Variables Example\n"
            "student_name = \"Ganesh\"\n"
            "roll_number = \"4KV22EC018\"\n"
            "cgpa = 8.75\n"
            "is_enrolled = True\n"
            "\n"
            "print(f\"Student: {student_name} | Roll: {roll_number} | CGPA: {cgpa}\")\n"
        ),
        "example_output": (
            "Student: Ganesh | Roll: 4KV22EC018 | CGPA: 8.75\n"
        ),
        "line_by_line": [
            "`student_name = 'Ganesh'`: Stores a text string in memory.",
            "`cgpa = 8.75`: Stores a floating-point decimal number.",
            "`is_enrolled = True`: Stores a boolean flag.",
        ],
        "summary": (
            "Variables are the fundamental storage containers in all programming languages."
        ),
        "spoken": (
            "A variable is a named container in computer memory used to store and manipulate data throughout a program."
        ),
    },

    "inheritance": {
        "title": "Inheritance in Object-Oriented Programming",
        "badge": "🧬 OOP Inheritance",
        "definition": (
            "Inheritance is an Object-Oriented Programming (OOP) mechanism where a child (derived) class acquires "
            "the attributes and methods of an existing parent (base) class, promoting code reusability and hierarchical design."
        ),
        "explanation": (
            "Just like a child inherits traits (eye color, height) from their parents, an `EngineeringStudent` class "
            "inherits universal traits (name, email) from a general `Student` class and adds its own specific properties (branch, lab practicals)."
        ),
        "features": [
            "**Code Reusability**: Eliminates duplicate code across related classes.",
            "**Method Overriding**: Child classes can provide specialized implementations of inherited methods.",
            "**`super()` Keyword**: Allows the child class to invoke the parent class's constructor or methods.",
            "**Inheritance Types**: Single, Multiple, Multilevel, Hierarchical, and Hybrid.",
        ],
        "applications": [
            "Building GUI frameworks (where buttons and checkboxes inherit from a general `Widget` class).",
            "Game development (where `Player` and `Enemy` inherit from a base `Character` class).",
        ],
        "example_code": (
            "class Student:\n"
            "    def __init__(self, name: str, roll_no: str):\n"
            "        self.name = name\n"
            "        self.roll_no = roll_no\n"
            "\n"
            "    def display(self):\n"
            "        return f\"{self.name} (Roll: {self.roll_no})\"\n"
            "\n"
            "class EngineeringStudent(Student):\n"
            "    def __init__(self, name: str, roll_no: str, branch: str):\n"
            "        super().__init__(name, roll_no)\n"
            "        self.branch = branch\n"
            "\n"
            "# Instantiate derived class\n"
            "s = EngineeringStudent(\"Ganesh\", \"4KV22EC018\", \"ECE\")\n"
            "print(s.display())  # Inherited from Student\n"
            "print(f\"Branch: {s.branch}\")\n"
        ),
        "example_output": (
            "Ganesh (Roll: 4KV22EC018)\n"
            "Branch: ECE\n"
        ),
        "line_by_line": [
            "`class EngineeringStudent(Student)`: Declares that `EngineeringStudent` inherits from `Student`.",
            "`super().__init__(name, roll_no)`: Calls the parent class constructor to initialize common fields.",
            "`s.display()`: Executes the inherited method defined in the parent class.",
        ],
        "summary": (
            "Inheritance allows you to build clean, maintainable software architectures without redundant code."
        ),
        "spoken": (
            "Inheritance in Python and OOP allows a child class to inherit methods and properties from a parent class. "
            "It promotes code reuse and cleaner architecture."
        ),
    },

    "dsa": {
        "title": "Data Structures & Algorithms (DSA)",
        "badge": "📊 DSA",
        "definition": (
            "A data structure is a specialized format for organizing, processing, retrieving, and storing data in computer memory, "
            "while an algorithm is a finite sequence of unambiguous instructions for solving a specific computational problem."
        ),
        "explanation": (
            "Data structures are like shelves, drawers, and folders in an office; algorithms are the step-by-step procedures "
            "you follow to organize, find, and update documents inside them."
        ),
        "features": [
            "**Linear Data Structures**: Arrays, Linked Lists, Stacks (LIFO), and Queues (FIFO).",
            "**Non-Linear Data Structures**: Trees (Binary Search Trees, Heaps) and Graphs.",
            "**Asymptotic Notation**: Big-O notation measures time and space complexity ($O(1)$, $O(\\log n)$, $O(n)$, $O(n^2)$).",
        ],
        "applications": [
            "Technical coding rounds for top tier tech placements.",
            "Search engines, GPS route navigation (Dijkstra's), and database indexing (B+ Trees).",
        ],
        "example_code": (
            "# Binary Search Algorithm in Python (O(log n))\n"
            "def binary_search(arr, target):\n"
            "    low = 0\n"
            "    high = len(arr) - 1\n"
            "    while low <= high:\n"
            "        mid = (low + high) // 2\n"
            "        if arr[mid] == target:\n"
            "            return mid\n"
            "        elif arr[mid] < target:\n"
            "            low = mid + 1\n"
            "        else:\n"
            "            high = mid - 1\n"
            "    return -1\n"
            "\n"
            "nums = [10, 20, 30, 40, 50, 60, 70]\n"
            "print(\"Index of 40:\", binary_search(nums, 40))\n"
        ),
        "example_output": (
            "Index of 40: 3\n"
        ),
        "line_by_line": [
            "`low = 0, high = len(arr) - 1`: Initializes the search boundary pointers.",
            "`mid = (low + high) // 2`: Finds the middle index.",
            "`arr[mid] == target`: Compares target and halves search space in $O(\\log n)$ time.",
        ],
        "summary": (
            "DSA is the core foundation evaluated in technical interviews and competitive programming."
        ),
        "spoken": (
            "Data structures and algorithms are the fundamental tools of computer science. "
            "They determine how efficiently data is organized and how fast computational problems are solved."
        ),
    },

    "microprocessor": {
        "title": "8085 Microprocessor Architecture",
        "badge": "⚡ ECE Microprocessor",
        "definition": (
            "The Intel 8085 is an 8-bit general-purpose microprocessor introduced in 1976. It operates on 8-bit data, "
            "has a 16-bit address bus capable of addressing up to 64 KB of memory, and operates with a 3 MHz clock frequency."
        ),
        "explanation": (
            "The microprocessor is the CPU of an embedded system. It fetches instructions from memory, decodes them, "
            "and executes arithmetic, logical, and I/O operations through its internal registers and ALU."
        ),
        "features": [
            "**Bus Width**: 8-bit multiplexed address/data bus (AD0-AD7) and 8-bit higher-order address bus (A8-A15).",
            "**Registers**: Accumulator (A), Flag Register (S, Z, AC, P, CY), General Purpose pairs (B-C, D-E, H-L), Stack Pointer (SP), Program Counter (PC).",
            "**Interrupts**: TRAP (non-maskable, highest priority), RST 7.5, RST 6.5, RST 5.5, and INTR.",
            "**Power Supply**: Requires a single +5V DC power supply.",
        ],
        "applications": [
            "Foundational academic topic in ECE/EEE university curricula.",
            "Industrial controllers, traffic light management, washing machine control units, and instrumentation.",
        ],
        "example_code": (
            "; 8085 Assembly Code: Add two 8-bit numbers\n"
            "MVI A, 25H     ; Load 25H into Accumulator\n"
            "MVI B, 15H     ; Load 15H into Register B\n"
            "ADD B          ; Add contents of B to Accumulator (A = A + B)\n"
            "STA 2050H      ; Store result into memory location 2050H\n"
            "HLT            ; Halt execution\n"
        ),
        "example_output": (
            "Memory [2050H] = 3AH (25H + 15H = 3AH)\n"
        ),
        "line_by_line": [
            "`MVI A, 25H`: Moves immediate 8-bit data into the accumulator.",
            "`ADD B`: Arithmetic logic unit performs binary addition.",
            "`STA 2050H`: Direct addressing mode writes 8-bit result to memory.",
            "`HLT`: Stops machine cycle clock.",
        ],
        "summary": (
            "The 8085 microprocessor forms the bedrock for learning computer architecture, assembly language, and embedded systems."
        ),
        "spoken": (
            "The 8085 is an 8-bit microprocessor with a 16-bit address bus capable of accessing 64 kilobytes of memory. "
            "It features registers including the accumulator, flag register, program counter, and stack pointer."
        ),
    },
    "string in python": {
        "title": "Python Strings (str)",
        "badge": "🧵 Python String",
        "definition": (
            "In Python, a string is a built-in immutable sequence of Unicode characters. "
            "Strings are enclosed in single quotes ('...'), double quotes (\"...\"), or triple quotes ('''...''' / \"\"\"...\"\"\") "
            "for multi-line text and docstrings."
        ),
        "explanation": (
            "Think of a string as an ordered chain of letters, symbols, or numbers. "
            "Because Python strings are immutable, once created their contents cannot be altered in-place. "
            "Python provides zero-based indexing and slicing to access individual characters or substrings effortlessly."
        ),
        "features": [
            "**Immutable**: String contents cannot be modified in-place; modifications return a new string instance.",
            "**Indexed & Slicable**: Individual characters can be accessed via `s[0]` and slices via `s[start:stop:step]`.",
            "**Unicode Standard**: Python 3 strings natively support international characters, symbols, and emojis.",
            "**Built-in Methods**: Provides rich transformation methods such as `.upper()`, `.lower()`, `.strip()`, `.split()`, and `.replace()`.",
            "**F-Strings Support**: Allows formatted string literals via `f\"{variable}\"` for clean string interpolation.",
        ],
        "applications": [
            "User input validation, text processing, and natural language formatting.",
            "Parsing JSON, CSV, API payloads, and database query parameters.",
            "Pattern matching and tokenization in compilers and search algorithms.",
        ],
        "example_code": (
            "# Creating and manipulating strings in Python\n"
            "text = \"SkillExa AI\"\n"
            "greeting = f\"Welcome to {text}!\"\n\n"
            "# Indexing and slicing\n"
            "first_char = text[0]        # 'S'\n"
            "sliced_word = text[0:8]     # 'SkillExa'\n"
            "reversed_text = text[::-1]  # 'IA axEllikS'\n\n"
            "print(greeting)\n"
            "print(f\"First char: {first_char}, Sliced: {sliced_word}\")\n"
            "print(f\"Reversed: {reversed_text}\")\n"
        ),
        "example_output": (
            "Welcome to SkillExa AI!\n"
            "First char: S, Sliced: SkillExa\n"
            "Reversed: IA axEllikS\n"
        ),
        "line_by_line": [
            "`text = \"SkillExa AI\"`: Instantiates a string literal assigned to variable `text`.",
            "`f\"Welcome to {text}!\"`: Formatted f-string interpolates the value of `text` dynamically.",
            "`text[0:8]`: Slices the string from index 0 up to (not including) index 8.",
            "`text[::-1]`: Pythonic extended slice with a step of -1 to reverse the string.",
            "`print(...)`: Standard output displaying the formatted results to console.",
        ],
        "summary": (
            "Strings in Python are fundamental immutable sequences used for representing textual data, "
            "featuring powerful slicing, built-in string methods, and f-string interpolation."
        ),
        "spoken": (
            "In Python, a string is an immutable sequence of characters enclosed in single, double, or triple quotes. "
            "Strings support zero-based indexing, slicing, and built-in methods like split and replace."
        ),
    },
    "string": {
        "title": "String Data Type",
        "badge": "🧵 String Data Type",
        "definition": (
            "A string is a fundamental computer science data type representing a contiguous sequence of characters, "
            "such as letters, numbers, symbols, and spaces, used to store and manipulate text."
        ),
        "explanation": (
            "In programming, strings are typically implemented as an array of characters encoded in ASCII or UTF-8 Unicode. "
            "They allow human-readable text to be stored in computer memory, compared, concatenated, and searched."
        ),
        "features": [
            "**Sequence Structure**: Characters are stored in a sequential, indexed order.",
            "**Encoding Compatibility**: Encoded into binary memory using standards like ASCII (8-bit) or UTF-8 / UTF-16 Unicode.",
            "**Common Operations**: Concatenation, substring search, length calculation, and case transformations.",
            "**Null-Terminated vs Object-Oriented**: In C, strings are null-terminated (`\\0`) character arrays, while modern languages treat them as managed objects.",
        ],
        "applications": [
            "Text rendering and user interface labels across web, mobile, and desktop applications.",
            "Network protocols (HTTP headers, JSON, XML, REST API requests).",
            "Data persistence in file systems and relational database tables (VARCHAR / TEXT).",
        ],
        "example_code": (
            "// String declaration in C and Python\n"
            "// Python: text = \"Hello World\"\n"
            "// C: char text[] = \"Hello World\";\n"
            "#include <stdio.h>\n"
            "#include <string.h>\n\n"
            "int main() {\n"
            "    char greeting[] = \"SkillExa\";\n"
            "    printf(\"String: %s\\n\", greeting);\n"
            "    printf(\"Length: %lu\\n\", strlen(greeting));\n"
            "    return 0;\n"
            "}\n"
        ),
        "example_output": (
            "String: SkillExa\n"
            "Length: 8\n"
        ),
        "line_by_line": [
            "`char greeting[] = \"SkillExa\"`: Allocates 9 bytes in memory (8 characters + 1 null terminator `\\0`).",
            "`strlen(greeting)`: Computes character count excluding the null terminator.",
            "`printf(...)`: Prints the string using the `%s` format specifier.",
        ],
        "summary": (
            "A string is an indexed sequence of characters used for representing human-readable text across all programming languages."
        ),
        "spoken": (
            "A string is a sequence of characters used in programming to store and manipulate text, typically encoded in ASCII or Unicode."
        ),
    },
}

# Specific computer science concept keywords that prevent naive matching of generic language names
SPECIFIC_CONCEPTS = {
    "string", "strings", "list", "lists", "dict", "dictionary", "dictionaries",
    "tuple", "tuples", "set", "sets", "array", "arrays", "pointer", "pointers",
    "loop", "loops", "function", "functions", "class", "classes", "object", "objects",
    "recursion", "sorting", "tree", "graph", "stack", "queue", "inheritance",
    "polymorphism", "encapsulation", "abstraction", "exception", "lambda", "decorator"
}


class AcademicKnowledgeEngine:
    """
    High-Intelligence Academic & Concept Engine.
    Resolves definitions, programming concepts, engineering formulas, and follow-up questions
    with structured, pedagogical answers conforming strictly to user requirements.
    """

    @classmethod
    def answer(
        cls,
        user_query: str,
        past_messages: List[Any] = None,
        project_name: str = "General Chats",
    ) -> Optional[Tuple[str, str]]:
        clean_q = normalize_query(user_query)
        query_words = set(re.findall(r"\b[a-z0-9_+#.-]+\b", clean_q))

        # 1. Check for Definition Queries (longest & most specific match first)
        matched_topic = None
        for key in sorted(ACADEMIC_TOPICS.keys(), key=len, reverse=True):
            pattern = r"\b" + re.escape(key) + r"\b"
            if re.search(pattern, clean_q):
                # If key is a generic language name ("python", "c", etc.) but query contains
                # a specific concept not in the key (e.g. "define string in python"), skip this broad key
                if key in ("python", "c", "cpp", "javascript"):
                    concept_overlap = query_words.intersection(SPECIFIC_CONCEPTS)
                    if concept_overlap:
                        continue
                matched_topic = key
                break

        # Check multi-turn context ONLY if user's current query is an explicit follow-up
        FOLLOW_UP_INDICATORS = [
            "give me an example", "example", "code example", "show code",
            "features", "applications", "syntax", "explain more",
            "tell me more", "how does it work", "why use it", "summary",
            "more details", "what is it used for", "explain further"
        ]
        is_follow_up = any(re.search(r"\b" + re.escape(p) + r"\b", clean_q) for p in FOLLOW_UP_INDICATORS)

        if not matched_topic and is_follow_up and past_messages:
            last_user_msgs = [
                m for m in past_messages if getattr(m, "sender_type", "") == "user" and getattr(m, "message_text", "") != user_query
            ]
            if last_user_msgs:
                prev_text = normalize_query(last_user_msgs[-1].message_text)
                for key in sorted(ACADEMIC_TOPICS.keys(), key=len, reverse=True):
                    # Never loosely match single-letter topics like 'c' from past context
                    if len(key) <= 1:
                        continue
                    if re.search(r"\b" + re.escape(key) + r"\b", prev_text):
                        matched_topic = key
                        break

        # If a known academic topic is found, generate the requested structured response
        if matched_topic and matched_topic in ACADEMIC_TOPICS:
            info = ACADEMIC_TOPICS[matched_topic]
            return cls._build_structured_topic_response(user_query, info)

        return None

    @classmethod
    def _build_structured_topic_response(cls, user_query: str, info: Dict[str, Any]) -> Tuple[str, str]:
        """Format strictly according to requested definition structure."""
        title = info.get("title", "Core Concept")
        badge = info.get("badge", "📘 Concept")
        definition = info["definition"]
        explanation = info["explanation"]
        features = info.get("features", [])
        applications = info.get("applications", [])
        code = info.get("example_code", "")
        output = info.get("example_output", "")
        line_by_line = info.get("line_by_line", [])
        summary = info["summary"]

        features_md = "\n".join([f"- {f}" for f in features])
        apps_md = "\n".join([f"- {a}" for f in applications for a in [f]])

        md_parts = [
            f"### {badge}: Definition & Overview",
            "",
            "#### 1. Definition",
            definition,
            "",
            "#### 2. Simple Explanation",
            explanation,
            "",
            "#### 3. Important Features",
            features_md,
            "",
            "#### 4. Real-World Applications",
            apps_md,
        ]

        if code:
            md_parts.extend([
                "",
                "#### 5. Working Example",
                f"```python\n{code.strip()}\n```" if "python" in badge.lower() else f"```c\n{code.strip()}\n```",
            ])
            if output:
                md_parts.extend([
                    "**Expected Output:**",
                    f"```text\n{output.strip()}\n```",
                ])
            if line_by_line:
                md_parts.extend([
                    "**Line-by-Line Breakdown:**",
                    "\n".join([f"- {line}" for line in line_by_line]),
                ])

        md_parts.extend([
            "",
            "#### 6. Summary",
            f"> [!NOTE]\n> {summary}",
        ])

        full_reply = "\n".join(md_parts)
        speech_text = info.get("spoken", definition)

        return full_reply, speech_text

