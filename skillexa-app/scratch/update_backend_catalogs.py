import os
import re
import json

# 1. Update cpp_topic_catalog.py
cpp_catalog_path = "backend/app/models/cpp_topic_catalog.py"
with open(cpp_catalog_path, "r", encoding="utf-8") as f:
    cpp_code = f.read()

# Add CPP_TOPIC_CORE alias at the bottom if not present
if "CPP_TOPIC_CORE =" not in cpp_code:
    cpp_code += "\n\nCPP_TOPIC_CORE = CPP_TOPICS\n"

# Enhance _build_cpp_topic skill_exa_test to generate 5 questions
old_cpp_build = """        "skill_exa_test": [
            {
                "question": f"Which standard stream object is used for outputting text in C++ for {title}?",
                "options": ["std::cout", "std::cin", "std::cerr", "printf"],
                "answer": "std::cout",
            }
        ],"""

new_cpp_build = """        "skill_exa_test": [
            {
                "question": f"What is the primary role of '{title}' in C++ programming?",
                "options": [f"A core programming concept in {cat} for {title}", "An unused CSS styling directive", "A hardware driver protocol only used in firmware", "A database table locking rule"],
                "answer": f"A core programming concept in {cat} for {title}",
            },
            {
                "question": f"Which standard header file or stream object is fundamental to '{title}' in C++?",
                "options": ["std::cout / <iostream>", "Direct raw disk sector formatting", "Unbounded buffer overflow execution", "Operating system power cycle reset"],
                "answer": "std::cout / <iostream>",
            },
            {
                "question": f"What is the recommended best practice when working with '{title}' in C++?",
                "options": ["Write structured, maintainable code following C++ standards", "Hardcode magic numbers without comments or error checks", "Ignore compiler warnings and memory safety guidelines", "Bypass function scope and use global state everywhere"],
                "answer": "Write structured, maintainable code following C++ standards",
            },
            {
                "question": f"What potential error or bug can happen if '{title}' is implemented incorrectly?",
                "options": ["Syntax or runtime execution errors in C++", "Physical GPU fan speed reduction", "Static HTML layout shift", "Automatic database deletion"],
                "answer": "Syntax or runtime execution errors in C++",
            },
            {
                "question": f"How does mastering '{title}' benefit software development in C++?",
                "options": ["Improves program modularity, execution safety, and readability", "Slows down program compilation by 10x", "Prevents the program from running on modern operating systems", "Removes the need for variable type definitions"],
                "answer": "Improves program modularity, execution safety, and readability",
            }
        ],"""

if old_cpp_build in cpp_code:
    cpp_code = cpp_code.replace(old_cpp_build, new_cpp_build)

with open(cpp_catalog_path, "w", encoding="utf-8") as f:
    f.write(cpp_code)
print("Updated cpp_topic_catalog.py")


# 2. Update java_topic_catalog.py
java_catalog_path = "backend/app/models/java_topic_catalog.py"
with open(java_catalog_path, "r", encoding="utf-8") as f:
    java_code = f.read()

if "JAVA_TOPIC_CORE =" not in java_code:
    java_code += "\n\nJAVA_TOPIC_CORE = JAVA_TOPICS\n"

old_java_build = """        "skill_exa_test": [
            {
                "question": f"Which standard method is the entry point for executing a Java application for {title}?",
                "options": ["public static void main(String[] args)", "public void main()", "public static int main()", "void start()"],
                "answer": "public static void main(String[] args)",
            }
        ],"""

new_java_build = """        "skill_exa_test": [
            {
                "question": f"What is the primary role of '{title}' in Java enterprise programming?",
                "options": [f"A core object-oriented concept in {cat} for {title}", "An unused CSS styling directive", "A hardware driver protocol only used in firmware", "A database table locking rule"],
                "answer": f"A core object-oriented concept in {cat} for {title}",
            },
            {
                "question": f"Which standard entry method or concept is fundamental to '{title}' in Java?",
                "options": ["public static void main(String[] args)", "Direct raw disk sector formatting", "Unbounded buffer overflow execution", "Operating system power cycle reset"],
                "answer": "public static void main(String[] args)",
            },
            {
                "question": f"What is the recommended best practice when working with '{title}' in Java?",
                "options": ["Write structured, object-oriented code following Java clean code conventions", "Hardcode magic numbers without comments or error checks", "Ignore compiler warnings and memory safety guidelines", "Bypass package encapsulation and use global state everywhere"],
                "answer": "Write structured, object-oriented code following Java clean code conventions",
            },
            {
                "question": f"What potential exception or error can happen if '{title}' is implemented incorrectly?",
                "options": ["NullPointerException or runtime execution error in Java", "Physical GPU fan speed reduction", "Static HTML layout shift", "Automatic database deletion"],
                "answer": "NullPointerException or runtime execution error in Java",
            },
            {
                "question": f"How does mastering '{title}' benefit Java application development?",
                "options": ["Improves program encapsulation, JVM memory safety, and readability", "Slows down program compilation by 10x", "Prevents the program from running on JVM", "Removes the need for class declarations"],
                "answer": "Improves program encapsulation, JVM memory safety, and readability",
            }
        ],"""

if old_java_build in java_code:
    java_code = java_code.replace(old_java_build, new_java_build)

with open(java_catalog_path, "w", encoding="utf-8") as f:
    f.write(java_code)
print("Updated java_topic_catalog.py")


# 3. Update js_topic_catalog.py
js_catalog_path = "backend/app/models/js_topic_catalog.py"
with open(js_catalog_path, "r", encoding="utf-8") as f:
    js_code = f.read()

if "JS_TOPIC_CORE =" not in js_code:
    js_code += "\n\nJS_TOPIC_CORE = JS_TOPICS\n"

old_js_build = """        "skill_exa_test": [
            {
                "question": f"Which standard console method is used for logging information in JavaScript for {title}?",
                "options": ["console.log()", "print()", "System.out.println()", "cout <<"],
                "answer": "console.log()",
            }
        ],"""

new_js_build = """        "skill_exa_test": [
            {
                "question": f"What is the primary role of '{title}' in JavaScript web and Node.js development?",
                "options": [f"A core ECMAScript concept in {category} for {title}", "An unused CSS styling directive", "A hardware driver protocol only used in firmware", "A database table locking rule"],
                "answer": f"A core ECMAScript concept in {category} for {title}",
            },
            {
                "question": f"Which standard method or keyword is fundamental to '{title}' in JavaScript?",
                "options": ["console.log() / let & const", "Direct raw disk sector formatting", "Unbounded buffer overflow execution", "Operating system power cycle reset"],
                "answer": "console.log() / let & const",
            },
            {
                "question": f"What is the recommended best practice when working with '{title}' in JavaScript?",
                "options": ["Write clean, non-blocking asynchronous code following JS best practices", "Hardcode magic numbers without comments or error checks", "Ignore console warnings and scope rules", "Poll globally in infinite loops"],
                "answer": "Write clean, non-blocking asynchronous code following JS best practices",
            },
            {
                "question": f"What potential error can happen if '{title}' is implemented incorrectly in JavaScript?",
                "options": ["TypeError, ReferenceError or runtime error in JS engine", "Physical GPU fan speed reduction", "Static HTML layout shift", "Automatic database deletion"],
                "answer": "TypeError, ReferenceError or runtime error in JS engine",
            },
            {
                "question": f"How does mastering '{title}' benefit frontend and backend JavaScript applications?",
                "options": ["Enhances code responsiveness, Event Loop execution, and maintainability", "Slows down execution speed by 100x", "Prevents JavaScript from executing in browsers", "Disables DOM manipulation capability"],
                "answer": "Enhances code responsiveness, Event Loop execution, and maintainability",
            }
        ],"""

if old_js_build in js_code:
    js_code = js_code.replace(old_js_build, new_js_build)

with open(js_catalog_path, "w", encoding="utf-8") as f:
    f.write(js_code)
print("Updated js_topic_catalog.py")
