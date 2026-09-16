"""JavaScript Curriculum Catalog and Content Builder for 105 topics across 14 modules."""
from __future__ import annotations

JS_TOPIC_CATALOG = [
    # 1. Fundamentals
    {"id": 1, "title": "Introduction", "difficulty": "Beginner", "duration": "15 min", "category": "Fundamentals"},
    {"id": 2, "title": "Using JS in HTML", "difficulty": "Beginner", "duration": "15 min", "category": "Fundamentals"},
    {"id": 3, "title": "Browser Console", "difficulty": "Beginner", "duration": "15 min", "category": "Fundamentals"},
    {"id": 4, "title": "Variables", "difficulty": "Beginner", "duration": "20 min", "category": "Fundamentals"},
    {"id": 5, "title": "Data Types", "difficulty": "Beginner", "duration": "20 min", "category": "Fundamentals"},
    {"id": 6, "title": "Type Conversion and Coercion", "difficulty": "Beginner", "duration": "25 min", "category": "Fundamentals"},
    {"id": 7, "title": "Arithmetic & Assignment Operators", "difficulty": "Beginner", "duration": "20 min", "category": "Fundamentals"},
    {"id": 8, "title": "Comparison Operators - Chapter 1", "difficulty": "Beginner", "duration": "20 min", "category": "Fundamentals"},
    {"id": 801, "title": "Logical Operators - Chapter 2", "difficulty": "Beginner", "duration": "20 min", "category": "Fundamentals"},
    {"id": 9, "title": "Unary, Ternary & Comma Operators", "difficulty": "Beginner", "duration": "20 min", "category": "Fundamentals"},
    {"id": 10, "title": "Bitwise & Relational Operators", "difficulty": "Intermediate", "duration": "20 min", "category": "Fundamentals"},
    {"id": 11, "title": "Advanced Operators (Optional Chaining & BigInt)", "difficulty": "Intermediate", "duration": "20 min", "category": "Fundamentals"},
    {"id": 12, "title": "If, If-Else & Else-If Statements", "difficulty": "Beginner", "duration": "20 min", "category": "Fundamentals"},
    {"id": 13, "title": "Switch Statement", "difficulty": "Beginner", "duration": "20 min", "category": "Fundamentals"},
    {"id": 14, "title": "For Loop", "difficulty": "Beginner", "duration": "20 min", "category": "Fundamentals"},
    {"id": 15, "title": "While & Do-While Loops", "difficulty": "Beginner", "duration": "20 min", "category": "Fundamentals"},
    {"id": 16, "title": "Loop Control (Break & Continue)", "difficulty": "Intermediate", "duration": "20 min", "category": "Fundamentals"},
    {"id": 17, "title": "Global & Local Scope", "difficulty": "Intermediate", "duration": "20 min", "category": "Fundamentals"},
    {"id": 18, "title": "Block, Lexical & Module Scope", "difficulty": "Intermediate", "duration": "20 min", "category": "Fundamentals"},

    # 2. Functions
    {"id": 19, "title": "Function Declarations & Default Parameters", "difficulty": "Beginner", "duration": "20 min", "category": "Functions"},
    {"id": 20, "title": "Anonymous Functions & Function Expressions", "difficulty": "Beginner", "duration": "20 min", "category": "Functions"},
    {"id": 21, "title": "Arrow Functions & IIFE", "difficulty": "Intermediate", "duration": "20 min", "category": "Functions"},
    {"id": 22, "title": "Callback & Rest Parameter Functions", "difficulty": "Intermediate", "duration": "20 min", "category": "Functions"},
    {"id": 23, "title": "Constructor & Pure Functions", "difficulty": "Intermediate", "duration": "20 min", "category": "Functions"},
    {"id": 24, "title": "Generator Functions", "difficulty": "Advanced", "duration": "25 min", "category": "Functions"},
    {"id": 25, "title": "Higher-Order Functions Basics (Passing & Returning Functions)", "difficulty": "Advanced", "duration": "25 min", "category": "Functions"},
    {"id": 26, "title": "Array HOFs: Transformation & Filtering (map & filter)", "difficulty": "Advanced", "duration": "25 min", "category": "Functions"},
    {"id": 27, "title": "Array HOFs: Accumulation & Iteration (reduce & forEach)", "difficulty": "Advanced", "duration": "25 min", "category": "Functions"},
    {"id": 28, "title": "Array HOFs: Search & Predicate Testing (find, some & every)", "difficulty": "Advanced", "duration": "25 min", "category": "Functions"},
    {"id": 29, "title": "Advanced HOF Techniques (Composition, Currying & Memoization)", "difficulty": "Advanced", "duration": "25 min", "category": "Functions"},
    {"id": 30, "title": "Variable Hoisting & Temporal Dead Zone (var vs let/const)", "difficulty": "Intermediate", "duration": "20 min", "category": "Functions"},
    {"id": 31, "title": "Function Declaration vs Expression Hoisting", "difficulty": "Intermediate", "duration": "20 min", "category": "Functions"},
    {"id": 32, "title": "Hoisting in Functions & Classes", "difficulty": "Intermediate", "duration": "20 min", "category": "Functions"},
    {"id": 33, "title": "Loop Hoisting & Closure Timing", "difficulty": "Intermediate", "duration": "20 min", "category": "Functions"},
    {"id": 34, "title": "Function Parameters & Nested Hoisting", "difficulty": "Intermediate", "duration": "20 min", "category": "Functions"},
    {"id": 35, "title": "Function Binding", "difficulty": "Intermediate", "duration": "25 min", "category": "Functions"},
    {"id": 36, "title": "Closures", "difficulty": "Advanced", "duration": "30 min", "category": "Functions"},
    {"id": 37, "title": "Iterator", "difficulty": "Intermediate", "duration": "25 min", "category": "Functions"},

    # 3. Events
    {"id": 38, "title": "Introduction to JavaScript Events & Event Handlers", "difficulty": "Beginner", "duration": "20 min", "category": "Events"},
    {"id": 39, "title": "JavaScript addEventListener() & Window Event Listeners", "difficulty": "Beginner", "duration": "20 min", "category": "Events"},
    {"id": 40, "title": "Mouse Events (onclick, onmouseover & onmouseout)", "difficulty": "Beginner", "duration": "20 min", "category": "Events"},
    {"id": 41, "title": "Keyboard Events (onkeydown & onkeyup)", "difficulty": "Intermediate", "duration": "20 min", "category": "Events"},
    {"id": 42, "title": "Form & Focus Events (onchange, onsubmit, onfocus & onblur)", "difficulty": "Intermediate", "duration": "25 min", "category": "Events"},
    {"id": 43, "title": "Prevent the Default Action of an Event in JavaScript", "difficulty": "Intermediate", "duration": "20 min", "category": "Events"},
    {"id": 44, "title": "Event Propagation (Bubbling & Capturing)", "difficulty": "Intermediate", "duration": "25 min", "category": "Events"},
    {"id": 45, "title": "Event Loop in JavaScript", "difficulty": "Advanced", "duration": "30 min", "category": "Events"},


    # 5. JavaScript Data Structures
    {"id": 55, "title": "JavaScript Numbers - Chapter 1", "difficulty": "Beginner", "duration": "20 min", "category": "JavaScript Data Structures"},
    {"id": 551, "title": "JavaScript Numbers - Chapter 2", "difficulty": "Beginner", "duration": "20 min", "category": "JavaScript Data Structures"},
    {"id": 56, "title": "JavaScript Strings - Chapter 1", "difficulty": "Beginner", "duration": "20 min", "category": "JavaScript Data Structures"},
    {"id": 561, "title": "JavaScript Strings - Chapter 2", "difficulty": "Beginner", "duration": "20 min", "category": "JavaScript Data Structures"},
    {"id": 57, "title": "JavaScript Arrays", "difficulty": "Beginner", "duration": "25 min", "category": "JavaScript Data Structures"},
    {"id": 58, "title": "Map in JavaScript", "difficulty": "Intermediate", "duration": "25 min", "category": "JavaScript Data Structures"},
    {"id": 59, "title": "LinkedList in JavaScript", "difficulty": "Intermediate", "duration": "30 min", "category": "JavaScript Data Structures"},
    {"id": 60, "title": "Stack in JavaScript", "difficulty": "Intermediate", "duration": "25 min", "category": "JavaScript Data Structures"},
    {"id": 61, "title": "Queue in JavaScript - Chapter 1", "difficulty": "Intermediate", "duration": "20 min", "category": "JavaScript Data Structures"},
    {"id": 611, "title": "Queue in JavaScript - Chapter 2", "difficulty": "Intermediate", "duration": "25 min", "category": "JavaScript Data Structures"},
    {"id": 62, "title": "Sorting Algorithms - Chapter 1", "difficulty": "Intermediate", "duration": "25 min", "category": "JavaScript Data Structures"},
    {"id": 621, "title": "Sorting Algorithms - Chapter 2", "difficulty": "Intermediate", "duration": "30 min", "category": "JavaScript Data Structures"},
    {"id": 63, "title": "Typed Arrays", "difficulty": "Advanced", "duration": "30 min", "category": "JavaScript Data Structures"},
    {"id": 64, "title": "WeakMap", "difficulty": "Advanced", "duration": "25 min", "category": "JavaScript Data Structures"},
    {"id": 65, "title": "WeakSet", "difficulty": "Advanced", "duration": "25 min", "category": "JavaScript Data Structures"},
    {"id": 66, "title": "Deque", "difficulty": "Intermediate", "duration": "30 min", "category": "JavaScript Data Structures"},
    {"id": 67, "title": "Priority Queue (Heap)", "difficulty": "Advanced", "duration": "35 min", "category": "JavaScript Data Structures"},

    # 6. Object-Oriented Programming
    {"id": 68, "title": "Introduction to OOP", "difficulty": "Beginner", "duration": "20 min", "category": "Object-Oriented Programming"},
    {"id": 69, "title": "Objects", "difficulty": "Beginner", "duration": "20 min", "category": "Object-Oriented Programming"},
    {"id": 70, "title": "this Keyword", "difficulty": "Intermediate", "duration": "25 min", "category": "Object-Oriented Programming"},
    {"id": 71, "title": "Prototype", "difficulty": "Intermediate", "duration": "30 min", "category": "Object-Oriented Programming"},
    {"id": 72, "title": "Classes", "difficulty": "Intermediate", "duration": "25 min", "category": "Object-Oriented Programming"},
    {"id": 73, "title": "Constructor Method", "difficulty": "Intermediate", "duration": "25 min", "category": "Object-Oriented Programming"},
    {"id": 74, "title": "Getters and Setters", "difficulty": "Intermediate", "duration": "25 min", "category": "Object-Oriented Programming"},
    {"id": 75, "title": "Static Methods", "difficulty": "Intermediate", "duration": "20 min", "category": "Object-Oriented Programming"},
    {"id": 76, "title": "Inheritance", "difficulty": "Advanced", "duration": "30 min", "category": "Object-Oriented Programming"},
    {"id": 77, "title": "Encapsulation", "difficulty": "Advanced", "duration": "25 min", "category": "Object-Oriented Programming"},
    {"id": 78, "title": "Abstraction", "difficulty": "Advanced", "duration": "25 min", "category": "Object-Oriented Programming"},
    {"id": 79, "title": "Polymorphism", "difficulty": "Advanced", "duration": "30 min", "category": "Object-Oriented Programming"},

    # 7. Browser and Document Object Model
    {"id": 80, "title": "Browser Object Model (BOM)", "difficulty": "Beginner", "duration": "20 min", "category": "Browser and Document Object Model"},
    {"id": 81, "title": "Document Object Model (DOM)", "difficulty": "Beginner", "duration": "20 min", "category": "Browser and Document Object Model"},
    {"id": 82, "title": "Manipulate DOM Elements", "difficulty": "Intermediate", "duration": "25 min", "category": "Browser and Document Object Model"},
    {"id": 83, "title": "Event Handling in the DOM", "difficulty": "Intermediate", "duration": "25 min", "category": "Browser and Document Object Model"},

    # 8. Asynchronous JavaScript
    {"id": 84, "title": "Callbacks", "difficulty": "Intermediate", "duration": "25 min", "category": "Asynchronous JavaScript"},
    {"id": 85, "title": "Promise - Basics & Creation (Ch. 1)", "difficulty": "Intermediate", "duration": "30 min", "category": "Asynchronous JavaScript"},
    {"id": 86, "title": "Promise - Advanced Methods & Patterns (Ch. 2)", "difficulty": "Advanced", "duration": "30 min", "category": "Asynchronous JavaScript"},
    {"id": 87, "title": "Promise Chaining", "difficulty": "Advanced", "duration": "30 min", "category": "Asynchronous JavaScript"},
    {"id": 88, "title": "Async/Await", "difficulty": "Advanced", "duration": "30 min", "category": "Asynchronous JavaScript"},

    # 9. JavaScript JSON
    {"id": 89, "title": "JSON Tutorial", "difficulty": "Beginner", "duration": "20 min", "category": "JavaScript JSON"},
    {"id": 90, "title": "JSON vs JavaScript Object", "difficulty": "Beginner", "duration": "20 min", "category": "JavaScript JSON"},
    {"id": 91, "title": "Parse JSON Data in JS", "difficulty": "Intermediate", "duration": "20 min", "category": "JavaScript JSON"},
    {"id": 92, "title": "JavaScript JSON Parser", "difficulty": "Intermediate", "duration": "25 min", "category": "JavaScript JSON"},
    {"id": 93, "title": "Read JSON File Using JS", "difficulty": "Intermediate", "duration": "25 min", "category": "JavaScript JSON"},

    # 10. Regular Expression and Validation
    {"id": 94, "title": "Regular Expressions", "difficulty": "Intermediate", "duration": "30 min", "category": "Regular Expression and Validation"},
    {"id": 95, "title": "Form Validation", "difficulty": "Intermediate", "duration": "25 min", "category": "Regular Expression and Validation"},
    {"id": 96, "title": "Email Validation", "difficulty": "Intermediate", "duration": "20 min", "category": "Regular Expression and Validation"},
    {"id": 97, "title": "Number Validation", "difficulty": "Beginner", "duration": "20 min", "category": "Regular Expression and Validation"},
    {"id": 98, "title": "Username Validation", "difficulty": "Intermediate", "duration": "20 min", "category": "Regular Expression and Validation"},
    {"id": 99, "title": "Password Validation", "difficulty": "Intermediate", "duration": "25 min", "category": "Regular Expression and Validation"},
    {"id": 100, "title": "URL Validation", "difficulty": "Advanced", "duration": "25 min", "category": "Regular Expression and Validation"},

    # 11. Exception and Error Handling
    {"id": 101, "title": "Errors and Exceptions", "difficulty": "Beginner", "duration": "20 min", "category": "Exception and Error Handling"},
    {"id": 102, "title": "try-catch, throw Statement & finally Block", "difficulty": "Intermediate", "duration": "25 min", "category": "Exception and Error Handling"},
    {"id": 103, "title": "Custom Errors", "difficulty": "Advanced", "duration": "25 min", "category": "Exception and Error Handling"},
    {"id": 104, "title": "Debugging Basics & DevTools", "difficulty": "Beginner", "duration": "20 min", "category": "Exception and Error Handling"},
    {"id": 105, "title": "Advanced Debugging & Error Tracking", "difficulty": "Intermediate", "duration": "25 min", "category": "Exception and Error Handling"},

    # 12. Testing and Performance Optimization
    {"id": 106, "title": "Unit Testing with Jest", "difficulty": "Intermediate", "duration": "30 min", "category": "Testing and Performance Optimization"},
    {"id": 107, "title": "Memory Management", "difficulty": "Advanced", "duration": "30 min", "category": "Testing and Performance Optimization"},
    {"id": 108, "title": "Garbage Collection", "difficulty": "Advanced", "duration": "25 min", "category": "Testing and Performance Optimization"},
    {"id": 109, "title": "Lazy Loading", "difficulty": "Intermediate", "duration": "25 min", "category": "Testing and Performance Optimization"},
    {"id": 110, "title": "Debouncing", "difficulty": "Advanced", "duration": "30 min", "category": "Testing and Performance Optimization"},
    {"id": 111, "title": "Throttling", "difficulty": "Advanced", "duration": "30 min", "category": "Testing and Performance Optimization"},

    # 13. JavaScript Projects
    {"id": 112, "title": "Simple Tic-Tac-Toe Game", "difficulty": "Intermediate", "duration": "35 min", "category": "JavaScript Projects"},
]


def _build_js_topic(meta: dict[str, str | int]) -> dict[str, object]:
    topic_id = meta["id"]
    title = meta["title"]
    category = meta["category"]

    return {
        "id": topic_id,
        "title": title,
        "category": category,
        "difficulty": meta["difficulty"],
        "duration": meta["duration"],
        "concept": f"Master the core principles, modern ECMAScript standards, and best practices of {title} in JavaScript.",
        "theory": f"JavaScript is a high-level, interpreted or just-in-time compiled programming language with first-class functions. {title} plays an essential role in web development, dynamic client-side scripting, and Node.js server environments.",
        "syntax": f"console.log('{title}');",
        "example": {
            "code": f"console.log('SkillExa JavaScript Track: {title}');",
            "output": f"SkillExa JavaScript Track: {title}",
            "explanation": f"Demonstrates execution of {title} in JavaScript runtime environment.",
        },
        "fill_blanks": {
            "question": f"console.____('SkillExa JavaScript Track: {title}');",
            "answers": ["log"],
            "options": ["log", "print", "write", "display"],
        },
        "compiler": {
            "title": f"JavaScript Practice - {title}",
            "question": f"Complete the JavaScript code to log output to console.",
            "starter_code": f"console.____('Learning {title} on SkillExa!');",
            "options": ["log", "write", "print", "out"],
        },
        "skill_exa_test": [
            {
                "question": f"Which standard console method is used for logging information in JavaScript for {title}?",
                "options": ["console.log()", "print()", "System.out.println()", "cout <<"],
                "answer": "console.log()",
            }
        ],
    }


JS_TOPICS: dict[int, dict[str, object]] = {
    meta["id"]: _build_js_topic(meta) for meta in JS_TOPIC_CATALOG
}

# Override Topic 1: Introduction
JS_TOPICS[1] = {
    "id": 1,
    "title": "Introduction",
    "category": "Fundamentals",
    "difficulty": "Beginner",
    "duration": "15 min",
    "concept": "JavaScript is a versatile, dynamically typed programming language that brings life to web pages by making them interactive. It supports both client-side web browser scripting and server-side development via Node.js.",
    "theory": "Core Characteristics of JavaScript:\n\n1. Dynamically Typed: Variable types are determined at runtime without requiring explicit data type declarations.\n2. Single-Threaded: Executes one task at a time on a single main thread, using the Event Loop for non-blocking asynchronous operations.\n3. Compiled & Interpreted: Modern engines (like V8 and SpiderMonkey) combine JIT (Just-In-Time) compilation and interpretation for high performance.\n\n'Hello, World!' Program in JavaScript:\nIn web pages, JavaScript is written inside <script> tags and outputs messages to the browser developer console using console.log():\n\n<html>\n<head></head>\n<body>\n    <h1>Check the console for the message!</h1>\n    <script>\n        // This is our first JavaScript program\n        console.log(\"Hello, World!\");\n    </script>\n</body>\n</html>",
    "syntax": "// Standard JS Console Output Syntax\nconsole.log('Hello, World!');",
    "example": {
        "code": "// First JavaScript Hello World Program\nconsole.log('Hello, World!');\nconsole.log('Welcome to SkillExa JavaScript Track!');",
        "output": "Hello, World!\nWelcome to SkillExa JavaScript Track!",
        "explanation": "console.log() prints messages to standard output or the browser developer console.",
    },
    "fill_blanks": {
        "question": "// Output Hello World message to the console\nconsole.____('Hello, World!');",
        "answers": ["log"],
        "options": ["log", "write", "print", "display"],
    },
    "compiler": {
        "title": "JavaScript Hello World Sandbox",
        "question": "Complete the JavaScript code to log 'Hello, World!' to the console.",
        "starter_code": "// Complete your first JS program\nconsole.____('Hello, World!');",
        "options": ["log", "print", "write", "out"],
    },
    "skill_exa_test": [
        {
            "question": "What does it mean that JavaScript is 'dynamically typed'?",
            "options": [
                "Variable types are determined at runtime without explicit type declarations",
                "Variable types must be declared statically at compile time",
                "Variables can only hold string values",
                "Type checking is performed by the browser network driver"
            ],
            "answer": "Variable types are determined at runtime without explicit type declarations",
        },
        {
            "question": "How does JavaScript handle asynchronous operations despite being single-threaded?",
            "options": [
                "Using the Event Loop and asynchronous callbacks/promises",
                "By spawning multiple CPU OS threads for every function",
                "By forcing synchronous execution for all tasks",
                "JavaScript cannot run asynchronous code"
            ],
            "answer": "Using the Event Loop and asynchronous callbacks/promises",
        },
        {
            "question": "How do modern JavaScript engines like Chrome V8 optimize execution performance?",
            "options": [
                "By combining Just-In-Time (JIT) compilation and interpretation",
                "By interpreting code line-by-line without compilation",
                "By translating JavaScript into C++ source code before download",
                "By disabling memory garbage collection"
            ],
            "answer": "By combining Just-In-Time (JIT) compilation and interpretation",
        },
        {
            "question": "Which HTML element tag is used to embed JavaScript code inside an HTML web page?",
            "options": ["<script>", "<js>", "<javascript>", "<code>"],
            "answer": "<script>",
        },
        {
            "question": "Which standard method is used to output debugging messages to the browser developer console or terminal?",
            "options": ["console.log()", "print()", "System.out.println()", "document.write_line()"],
            "answer": "console.log()",
        }
    ],
}

# Override Topic 2: Using JS in HTML
JS_TOPICS[2] = {
    "id": 2,
    "title": "Using JS in HTML",
    "category": "Fundamentals",
    "difficulty": "Beginner",
    "duration": "15 min",
    "concept": "JavaScript can be added to HTML documents inline, internally using <script> tags, or externally via separate .js files linked with the src attribute. This enables dynamic page interactivity, DOM manipulation, and event handling.",
    "theory": "3 Methods for Adding JavaScript to HTML:\n\n1. INLINE JAVASCRIPT:\nWritten directly inside HTML element event handler attributes:\n<button onclick=\"alert('Clicked!')\">Click Here</button>\n\n2. INTERNAL JAVASCRIPT:\nWritten inside <script> tags within the HTML document:\n - Inside <head>: Initialized as page loads (useful for early configs).\n - Before </body>: Placed at bottom of <body> so scripts run after DOM content is fully loaded.\n\n3. EXTERNAL JAVASCRIPT (<script src=\"...\">):\nKeeps logic separate in an external .js file.\n - Full URL: src=\"https://example.com/js/script.js\"\n - Absolute path: src=\"/js/script.js\"\n - Relative path: src=\"script.js\"\n\nADVANTAGES OF EXTERNAL JAVASCRIPT:\n1. Faster Load Times: Browser caching prevents re-downloading script on navigation.\n2. Separation of Concerns: Separates HTML layout structure from JS interactive behavior.\n3. Code Reusability: A single .js file can be referenced across multiple HTML pages.",
    "syntax": "<!-- Internal JS -->\n<script>\n    function myFun() {\n        document.getElementById('demo').innerHTML = 'Content changed!';\n    }\n</script>\n\n<!-- External JS -->\n<script src=\"script.js\"></script>",
    "example": {
        "code": "<!-- Internal JS inside Body -->\n<h3 id=\"demo\">SkillExa JavaScript</h3>\n<button onclick=\"myFun()\">Change Content</button>\n<script>\nfunction myFun() {\n    console.log('DOM element content changed successfully!');\n}\nmyFun();\n</script>",
        "output": "DOM element content changed successfully!",
        "explanation": "myFun() changes element content and logs message to console.",
    },
    "fill_blanks": {
        "question": "<!-- Link external JavaScript file -->\n<script _____=\"script.js\"></script>",
        "answers": ["src"],
        "options": ["src", "href", "link", "path"],
    },
    "compiler": {
        "title": "JavaScript in HTML Practice",
        "question": "Complete the script tag attribute to reference an external script file.",
        "starter_code": "// Complete HTML script element attribute\n// <script _____='app.js'></script>\nconsole.log('External script referenced with src attribute');",
        "options": ["src", "href", "rel", "type"],
    },
    "skill_exa_test": [
        {
            "question": "Which HTML tag attribute is used to reference an external JavaScript file?",
            "options": ["src", "href", "link", "rel"],
            "answer": "src",
        },
        {
            "question": "Why is placing <script> tags right before the closing </body> tag considered a performance best practice?",
            "options": [
                "It allows the HTML DOM content to load and render first before running scripts",
                "It disables CSS styles automatically",
                "It prevents JavaScript from accessing DOM elements",
                "It forces scripts to execute synchronously before browser parsing"
            ],
            "answer": "It allows the HTML DOM content to load and render first before running scripts",
        },
        {
            "question": "Which of the following is NOT a major advantage of using External JavaScript files (.js)?",
            "options": [
                "It converts JavaScript into a compiled C++ binary automatically",
                "Browser caching speeds up subsequent page load times",
                "Separation of concerns between HTML structure and JS behavior",
                "Code reusability across multiple HTML documents"
            ],
            "answer": "It converts JavaScript into a compiled C++ binary automatically",
        },
        {
            "question": "What type of JavaScript inclusion is represented by <button onclick=\"alert('Hello')\">?",
            "options": ["Inline JavaScript", "Internal JavaScript", "External JavaScript", "Asynchronous Module"],
            "answer": "Inline JavaScript",
        },
        {
            "question": "Which of the following is a valid way to reference an external JavaScript file?",
            "options": [
                "All of the above (Full URL, Absolute path, and Relative path)",
                "Using full URL: src=\"https://domain.com/js/script.js\"",
                "Using absolute path: src=\"/js/script.js\"",
                "Using relative path: src=\"script.js\""
            ],
            "answer": "All of the above (Full URL, Absolute path, and Relative path)",
        }
    ],
}

# Override Topic 3: Browser Console
JS_TOPICS[3] = {
    "id": 3,
    "title": "Browser Console",
    "category": "Fundamentals",
    "difficulty": "Beginner",
    "duration": "15 min",
    "concept": "The console object provides access to the browser developer debugging console and Node.js terminal. It contains a rich suite of methods for logging, error reporting, performance profiling, tabular data formatting, and call stack tracing.",
    "theory": "Core Console Object Methods:\n\n1. console.log(): Logs general informational and debugging messages.\n2. console.error(): Logs error messages (highlighted in red in browser consoles).\n3. console.warn(): Logs warning alerts (highlighted in yellow).\n4. console.info(): Logs informational messages (supports %c CSS inline styling).\n5. console.table(): Displays arrays or objects in structured tabular format.\n6. console.time(label) & console.timeEnd(label): Measures code execution duration in milliseconds.\n7. console.assert(condition, msg): Logs error output ONLY if condition is false.\n8. console.group(label) & console.groupEnd(): Indents and groups related console outputs.\n9. console.count(label): Tracks and counts execution frequency of a label.\n10. console.trace(): Prints execution stack trace showing function call hierarchy.",
    "syntax": "console.log('Log message');\nconsole.error('Error message');\nconsole.warn('Warning message');\nconsole.table([{name: 'Amit', age: 30}]);\nconsole.time('loopTimer');\nconsole.timeEnd('loopTimer');",
    "example": {
        "code": "console.log('1. General log');\nconsole.warn('2. Warning alert');\nconsole.error('3. Error log');\n\nconsole.table([{ id: 1, name: 'SkillExa' }, { id: 2, name: 'JavaScript' }]);\n\nconsole.time('ExecutionTimer');\nfor (let i = 0; i < 1000; i++) {}\nconsole.timeEnd('ExecutionTimer');\n\nconsole.assert(5 > 10, 'Assertion failed: 5 is not greater than 10');",
        "output": "1. General log\n2. Warning alert\n3. Error log\nExecutionTimer: 0.12ms\nAssertion failed: 5 is not greater than 10",
        "explanation": "Demonstrates console logging, tabular array rendering, execution timing, and conditional assertion.",
    },
    "fill_blanks": {
        "question": "// Measure execution time of code block\nconsole.____('myTimer');\nfor (let i = 0; i < 100; i++) {}\nconsole.____('myTimer');",
        "answers": ["time", "timeEnd"],
        "options": ["time", "timeEnd", "start", "stop"],
    },
    "compiler": {
        "title": "JavaScript Console Object Sandbox",
        "question": "Complete the JavaScript code to log a tabular object and measure timer duration.",
        "starter_code": "console.____([{ name: 'Ritik', age: 30 }]);\nconsole.time('testTimer');\nconsole.____('testTimer');",
        "options": ["table", "timeEnd", "log", "error"],
    },
    "skill_exa_test": [
        {
            "question": "Which console method displays array or object data in a structured tabular row-and-column format?",
            "options": ["console.table()", "console.log()", "console.dir()", "console.group()"],
            "answer": "console.table()",
        },
        {
            "question": "What pair of console methods is used to measure the execution time of a code block in milliseconds?",
            "options": [
                "console.time() and console.timeEnd()",
                "console.start() and console.stop()",
                "console.timer() and console.clock()",
                "console.benchmark() and console.duration()"
            ],
            "answer": "console.time() and console.timeEnd()",
        },
        {
            "question": "When does console.assert(condition, message) log an error message to the console?",
            "options": [
                "ONLY when the condition evaluates to false",
                "ONLY when the condition evaluates to true",
                "Every time it is executed regardless of condition",
                "ONLY when an exception is thrown"
            ],
            "answer": "ONLY when the condition evaluates to false",
        },
        {
            "question": "Which console method outputs a stack trace showing the exact function call hierarchy leading to its invocation?",
            "options": ["console.trace()", "console.count()", "console.stack()", "console.info()"],
            "answer": "console.trace()",
        },
        {
            "question": "Which console method tracks and prints how many times it has been invoked with a specific label?",
            "options": ["console.count()", "console.table()", "console.assert()", "console.time()"],
            "answer": "console.count()",
        }
    ],
}

# Override Topic 4: Variables
JS_TOPICS[4] = {
    "id": 4,
    "title": "Variables",
    "category": "Fundamentals",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "Variables in JavaScript store data values and can be declared using var, let, or const. JavaScript is dynamically typed, so data types are determined at runtime without explicit type annotations.",
    "theory": "Before ES6 (2015), variables were declared only with 'var', which is function-scoped and subject to hoisting. ES6 introduced 'let' and 'const', which are block-scoped (limited to { } blocks). Key rules & facts:\n1. Scoping: 'var' is function-scoped; 'let' and 'const' are block-scoped.\n2. Redeclaration: 'var' allows redeclaration in the same scope, whereas 'let' and 'const' throw a SyntaxError.\n3. Const Mutability: 'const' prevents variable reassignment, but properties of objects or elements of arrays declared with 'const' CAN be mutated (e.g., const obj = {a:10}; obj.a = 20; is allowed).\n4. Naming Rules: Variable names must begin with a letter, $, or _, are case-sensitive, and cannot use reserved keywords like function or class.",
    "syntax": "// Legacy function-scoped declaration\nvar a = 10;\n\n// Preferred for mutable variables\nlet b = 20;\n\n// Preferred for constant references\nconst c = 30;",
    "example": {
        "code": "if (true) {\n    var x = 10; // Function-scoped\n    let y = 20; // Block-scoped\n}\nconsole.log('x (var): ' + x);\n\nconst obj = { a: 10 };\nobj.a = 20; // Allowed property mutation\nconsole.log('obj.a: ' + obj.a);",
        "output": "x (var): 10\nobj.a: 20",
        "explanation": "var x is accessible outside the if-block. obj.a is mutated successfully despite obj being declared with const.",
    },
    "fill_blanks": {
        "question": "if (true) {\n    var x = 10;\n    _____ y = 20;\n}\nconsole.log(x); // Outputs 10\n// y is inaccessible here because _____ is block-scoped!",
        "answers": ["let", "let"],
        "options": ["let", "var", "const", "static"],
    },
    "compiler": {
        "title": "JavaScript Variables Practice",
        "question": "Complete the code to declare a block-scoped variable and mutate a const array element.",
        "starter_code": "const arr = [10, 20, 30];\narr[2] = 40;\n_____ message = 'Array element updated to ' + arr[2];\nconsole.log(message);",
        "options": ["let", "var", "const", "def"],
    },
    "skill_exa_test": [
        {
            "question": "Which keyword in JavaScript declares a variable that is function-scoped rather than block-scoped?",
            "options": ["var", "let", "const", "static"],
            "answer": "var",
        },
        {
            "question": "What happens when you modify a property of an object declared with const (e.g. const obj = { a: 10 }; obj.a = 20;)?",
            "options": [
                "It is allowed and mutates the property value",
                "It throws a TypeError: Assignment to constant variable",
                "It throws a SyntaxError",
                "The object becomes undefined"
            ],
            "answer": "It is allowed and mutates the property value",
        },
        {
            "question": "Which of the following is an INVALID variable name in JavaScript?",
            "options": ["123name", "userName", "$price", "_temp"],
            "answer": "123name",
        },
        {
            "question": "What type of error is thrown when trying to redeclare a variable declared with 'let' in the same scope?",
            "options": ["SyntaxError", "ReferenceError", "TypeError", "RangeError"],
            "answer": "SyntaxError",
        },
        {
            "question": "Why were 'let' and 'const' introduced in ES6 (2015) as safer alternatives to 'var'?",
            "options": [
                "To provide block-scoped variables and prevent hoisting and global scope pollution bugs",
                "To make JavaScript statically typed",
                "To eliminate functions in JavaScript",
                "To speed up browser network requests"
            ],
            "answer": "To provide block-scoped variables and prevent hoisting and global scope pollution bugs",
        }
    ],
}

# Override Topic 5: Data Types
JS_TOPICS[5] = {
    "id": 5,
    "title": "Data Types",
    "category": "Fundamentals",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "JavaScript data types define the kind of values a variable can hold and how memory allocation, operations, comparisons, and calculations behave. Data types are categorized into 7 Primitive types and Non-Primitive (Reference) types.",
    "theory": "JavaScript Data Type Classification:\n\n1. PRIMITIVE DATA TYPES (Simple, immutable values stored directly in memory):\n - Number: Includes integers, floating-point numbers, and special values like Infinity, -Infinity, and NaN (Not-a-Number).\n - String: Character sequences surrounded by single ('), double (\"), or template literal (`) quotes.\n - Boolean: Logical values true and false.\n - Null: Represents an intentional empty or non-existent value.\n - Undefined: Automatically assigned to variables declared but not yet initialized.\n - Symbol (ES6): Immutable, guaranteed unique primitive identifiers for object properties.\n - BigInt (ES2020): Represents whole numbers greater than 2^53 - 1 (Number.MAX_SAFE_INTEGER).\n\n2. NON-PRIMITIVE / REFERENCE TYPES (Derived data types stored by reference):\n - Object: Key-value pairs created with {} ({ type: 'Company', location: 'Noida' }).\n - Array: Ordered collection of values ([1, 'two', { name: 'Object' }]).\n - Function: Reusable block of code (function greet(name) { return 'Hello ' + name; }).\n - Date: Built-in object for date and time creation and manipulation.\n - RegExp: Regular expressions for pattern matching (/hello/).",
    "syntax": "// Primitive Data Types\nlet num = 42;\nlet str = `Hello ${num}`;\nlet isReady = true;\nlet emptyVal = null;\nlet uninit;\nlet sym = Symbol('id');\nlet big = 9007199254740991n;\n\n// Non-Primitive Reference Type\nlet gfg = { type: 'Company', location: 'Noida' };",
    "example": {
        "code": "let n4 = 'something here too' / 2;\nconsole.log('n4: ' + n4);\n\nlet sym1 = Symbol('Geeks');\nlet sym2 = Symbol('Geeks');\nconsole.log('sym1 == sym2: ' + (sym1 == sym2));\n\nlet big = BigInt('0b1010101001010101001111111111111111');\nconsole.log('BigInt: ' + big);\n\nlet a2 = [1, 'two', { name: 'Object' }];\nconsole.log('Array length: ' + a2.length);",
        "output": "n4: NaN\nsym1 == sym2: false\nBigInt: 11431327743\nArray length: 3",
        "explanation": "Invalid math operations return NaN. Symbols create unique keys even with identical labels. BigInt supports large bitwise integer values.",
    },
    "fill_blanks": {
        "question": "let s1 = _____('Geeks');\nlet s2 = _____('Geeks');\nconsole.log(s1 == s2); // Outputs false because _____ creates unique keys!",
        "answers": ["Symbol", "Symbol", "Symbol"],
        "options": ["Symbol", "BigInt", "String", "Object"],
    },
    "compiler": {
        "title": "JavaScript Data Types Practice",
        "question": "Complete the JavaScript code to instantiate BigInt and print output.",
        "starter_code": "let bigVal = _____('9007199254740995');\nconsole.log('BigInt Value: ' + bigVal);",
        "options": ["BigInt", "Number", "Symbol", "String"],
    },
    "skill_exa_test": [
        {
            "question": "What is the result of evaluating an invalid math operation like 'something' / 2 in JavaScript?",
            "options": ["NaN (Not-a-Number)", "Infinity", "Null", "Undefined"],
            "answer": "NaN (Not-a-Number)",
        },
        {
            "question": "Which primitive data type introduced in ES6 creates guaranteed unique and immutable identifiers for object properties?",
            "options": ["Symbol", "BigInt", "String", "Set"],
            "answer": "Symbol",
        },
        {
            "question": "Which data type introduced in ES2020 represents integers larger than 2^53 - 1 (Number.MAX_SAFE_INTEGER)?",
            "options": ["BigInt", "Number", "Long", "Int64"],
            "answer": "BigInt",
        },
        {
            "question": "What is the difference between null and undefined in JavaScript?",
            "options": [
                "null represents an intentional empty value, whereas undefined means a variable has been declared but not assigned a value",
                "undefined is an object while null is a number",
                "null is block-scoped while undefined is function-scoped",
                "There is no difference; they are exact aliases"
            ],
            "answer": "null represents an intentional empty value, whereas undefined means a variable has been declared but not assigned a value",
        },
        {
            "question": "Which of the following is a Non-Primitive (Reference) data type in JavaScript?",
            "options": ["Object (including Arrays, Functions, Date, RegExp)", "Number", "Boolean", "Symbol"],
            "answer": "Object (including Arrays, Functions, Date, RegExp)",
        }
    ],
}

# Override Topic 6: Type Conversion and Coercion
JS_TOPICS[6] = {
    "id": 6,
    "title": "Type Conversion and Coercion",
    "category": "Fundamentals",
    "difficulty": "Beginner",
    "duration": "25 min",
    "concept": "Type Conversion (Explicit Casting) is when the programmer manually converts data types using Number(), String(), or Boolean(). Type Coercion (Implicit Casting) is the automatic conversion performed by the JavaScript engine during arithmetic operations and loose equality comparisons.",
    "theory": "1. TYPE CONVERSION (EXPLICIT TYPE CASTING):\nPerformed manually by the programmer using built-in functions:\n - String to Number: Number('123') -> 123, parseInt('123'), parseFloat('12.34').\n - Number to String: String(123) -> '123' or (123).toString().\n - Boolean to Number: Number(true) -> 1, Number(false) -> 0.\n - Boolean to String: String(true) -> 'true'.\n\n2. TYPE COERCION (IMPLICIT TYPE CASTING):\nPerformed automatically by the JavaScript engine during operations:\n - String + Number: '5' + 5 -> '55' (number is coerced to string).\n - String - Number: '5' - 2 -> 3 (string is coerced to number!).\n - Boolean + Number: true + 10 -> 11 (true is coerced to 1).\n - Loose Equality (==): '10' == 10 -> true (coerced before comparison).\n - Falsy in Boolean Context: '', 0, null, undefined, NaN, false evaluate to false in if-statements.\n\nBEST PRACTICES:\n- Always prefer explicit Type Conversion to prevent bugs.\n- Use strict equality (===) instead of loose equality (==) to prevent unexpected coercion.",
    "syntax": "// Explicit Conversion\nlet num = Number('123');\nlet str = String(456);\n\n// Implicit Coercion\nlet concatenated = '5' + 10; // '510'\nlet subtracted = '10' - 2;   // 8",
    "example": {
        "code": "let n = 5;\nlet s = '5';\nconsole.log('n + s (+ concat): ' + (n + s));\nconsole.log('s - 2 (- math): ' + (s - 2));\n\nlet bool = true;\nconsole.log('bool + 10: ' + (bool + 10));\n\nconsole.log('\"10\" == 10 (loose): ' + (\"10\" == 10));\nconsole.log('\"10\" === 10 (strict): ' + (\"10\" === 10));",
        "output": "n + s (+ concat): 55\ns - 2 (- math): 3\nbool + 10: 11\n\"10\" == 10 (loose): true\n\"10\" === 10 (strict): false",
        "explanation": "+ operator concatenates when string is present ('55'). - operator coerces string to number (3). true is coerced to 1. Strict equality (===) prevents coercion.",
    },
    "fill_blanks": {
        "question": "let numStr = '100';\nlet convertedNum = _____(numStr); // Explicit conversion\nlet coercedSubtraction = '10' - 2; // Implicit coercion resulting in _____",
        "answers": ["Number", "8"],
        "options": ["Number", "String", "8", "102"],
    },
    "compiler": {
        "title": "JavaScript Type Conversion Sandbox",
        "question": "Complete the code to explicitly convert string to number and compare with strict equality.",
        "starter_code": "let valStr = '50';\nlet valNum = _____(valStr);\nconsole.log('Strict comparison:', valStr _____ valNum);",
        "options": ["Number", "===", "==", "String"],
    },
    "skill_exa_test": [
        {
            "question": "What is the difference between Type Conversion and Type Coercion in JavaScript?",
            "options": [
                "Type Conversion is explicit (manual by programmer), while Type Coercion is implicit (automatic by JS engine)",
                "Type Conversion is automatic, while Type Coercion is manual",
                "Type Conversion only works on numbers, while Type Coercion only works on strings",
                "There is no difference; both terms mean the exact same thing"
            ],
            "answer": "Type Conversion is explicit (manual by programmer), while Type Coercion is implicit (automatic by JS engine)",
        },
        {
            "question": "What is the output of evaluating the expression '5' - 2 in JavaScript?",
            "options": ["3 (Number)", "'52' (String)", "NaN", "TypeError"],
            "answer": "3 (Number)",
        },
        {
            "question": "What is the result of true + 10 due to boolean-to-number type coercion?",
            "options": ["11", "'true10'", "true", "NaN"],
            "answer": "11",
        },
        {
            "question": "Why is using strict equality (===) recommended over loose equality (==)?",
            "options": [
                "Strict equality (===) checks both value and data type without performing implicit type coercion",
                "Strict equality executes faster on single-threaded CPUs",
                "Loose equality (==) deletes variables after comparison",
                "Strict equality automatically converts all strings to numbers"
            ],
            "answer": "Strict equality (===) checks both value and data type without performing implicit type coercion",
        },
        {
            "question": "Which of the following values is coerced to true when evaluated in a boolean context (e.g. inside an if condition)?",
            "options": ["'Hello' (Non-empty string)", "'' (Empty string)", "0 (Zero)", "null"],
            "answer": "'Hello' (Non-empty string)",
        }
    ],
}

# Override Topic 7: Arithmetic & Assignment Operators
JS_TOPICS[7] = {
    "id": 7,
    "title": "Arithmetic & Assignment Operators",
    "category": "Fundamentals",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "An operator is a symbol used to perform an operation on one or more values or variables. Arithmetic operators perform mathematical calculations (+, -, *, /, %, **), while assignment operators assign values to variables (=, +=, -=, *=, /=, %=). String concatenation uses + and +=.",
    "theory": "What is an Operator?\nAn operator is a symbol used to perform an operation on one or more values or variables.\n\nArithmetic & Assignment Operators Breakdown:\n\n1. ARITHMETIC OPERATORS:\n - + Addition & String Concatenation\n - - Subtraction\n - * Multiplication\n - / Division\n - % Remainder (Modulus)\n - ** Exponentiation (a ** b = a^b)\n\n2. ASSIGNMENT OPERATORS:\n - = Assigns right operand value to left variable.\n - += Adds and assigns (x += 5 is x = x + 5).\n - -= Subtracts and assigns.\n - *= Multiplies and assigns.\n - /= Divides and assigns.\n - %= Remainder and assigns.\n\n3. STRING CONCATENATION:\n - Operator + joins strings together: 'Hello' + ' ' + 'World'.\n - Operator += appends to existing string.",
    "syntax": "const sum = 5 + 3;\nconst p = 4 * 2;\nconst q = 8 / 2;\nconst exp = 2 ** 3;\n\nlet n = 10;\nn += 5;\nn *= 2;",
    "example": {
        "code": "const sum = 5 + 3;\nconst diff = 10 - 2;\nconst prod = 4 * 2;\nconst div = 8 / 2;\nconst exp = 2 ** 3;\nconsole.log(sum, diff, prod, div, exp);\n\nlet n = 10;\nn += 5;\nn *= 2;\nconsole.log('n:', n);\n\nlet s = 'Hello' + ' ' + 'World';\ns += '!';\nconsole.log(s);",
        "output": "8 8 8 4 8\nn: 30\nHello World!",
        "explanation": "Calculates math expressions. n += 5 makes n 15, then n *= 2 makes n 30. Strings join with + and +=.",
    },
    "fill_blanks": {
        "question": "let n = 10;\nn _____ 5; // Add 5 and assign (makes n 15)\nn _____ 2; // Multiply by 2 and assign (makes n 30)",
        "answers": ["+=", "*="],
        "options": ["+=", "*=", "=", "-="],
    },
    "compiler": {
        "title": "Arithmetic & Assignment Sandbox",
        "question": "Complete the JavaScript code to multiply 4 by 2 and use compound addition assignment.",
        "starter_code": "const p = 4 _____ 2;\nlet n = 10;\nn _____ 5;\nconsole.log('p:', p, 'n:', n);",
        "options": ["*", "+=", "=", "+"],
    },
    "skill_exa_test": [
        {
            "question": "What is the result of evaluating 10 % 3 in JavaScript?",
            "options": ["1", "3", "0", "3.33"],
            "answer": "1",
        },
        {
            "question": "What is the final value of variable n after executing: let n = 10; n += 5; n *= 2;?",
            "options": ["30", "25", "15", "100"],
            "answer": "30",
        },
        {
            "question": "Which JavaScript operator calculates exponentiation (raising a number to a power)?",
            "options": ["**", "^", "^^", "exp()"],
            "answer": "**",
        },
        {
            "question": "What is the output of evaluating 'Hello' + ' ' + 'World'?",
            "options": ["'Hello World'", "'HelloWorld'", "NaN", "TypeError"],
            "answer": "'Hello World'",
        },
        {
            "question": "What is the value of x after executing: let x = 20; x /= 4;?",
            "options": ["5", "80", "16", "24"],
            "answer": "5",
        }
    ],
}

# Override Topic 8: Comparison Operators - Chapter 1
JS_TOPICS[8] = {
    "id": 8,
    "title": "Comparison Operators - Chapter 1",
    "category": "Fundamentals",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "An operator is a symbol used to perform an operation on one or more values or variables. Comparison operators compare two values and return a boolean (true or false). Chapter 1 covers relational operators (>, <, >=, <=) and equality operators (== loose equality vs === strict equality, != vs !==).",
    "theory": "What is an Operator?\nAn operator is a symbol used to perform an operation on one or more values or variables.\n\n1. RELATIONAL COMPARISON OPERATORS:\n- > : Greater than (10 > 5 -> true)\n- < : Less than (3 < 8 -> true)\n- >= : Greater than or equal to (5 >= 5 -> true)\n- <= : Less than or equal to (4 <= 2 -> false)\n\n2. EQUALITY COMPARISON OPERATORS:\n- == : Loose equality (coerces types before comparison, e.g. '10' == 10 is true)\n- === : Strict equality (checks value AND type without coercion, e.g. '10' === 10 is false)\n- != : Loose inequality ('5' != 5 is false)\n- !== : Strict inequality ('5' !== 5 is true)\n\n3. BEST PRACTICES:\n- Always use strict equality (=== and !==) to prevent unexpected type coercion bugs.",
    "syntax": "console.log(10 > 5);      // true\nconsole.log(10 == '10');  // true (loose equality)\nconsole.log(10 === '10'); // false (strict equality)\nconsole.log(10 !== '10'); // true",
    "example": {
        "code": "console.log('10 > 5:', 10 > 5);\nconsole.log('5 <= 5:', 5 <= 5);\nconsole.log('\"10\" == 10:', \"10\" == 10);\nconsole.log('\"10\" === 10:', \"10\" === 10);\nconsole.log('\"10\" !== 10:', \"10\" !== 10);",
        "output": "10 > 5: true\n5 <= 5: true\n\"10\" == 10: true\n\"10\" === 10: false\n\"10\" !== 10: true",
        "explanation": "\"10\" == 10 is true due to implicit type coercion. \"10\" === 10 is false because String !== Number.",
    },
    "fill_blanks": {
        "question": "console.log('10' _____ 10); // Strict comparison returns false\nconsole.log('10' _____ 10); // Loose comparison returns true",
        "answers": ["===", "=="],
        "options": ["===", "==", "!==", ">="],
    },
    "compiler": {
        "title": "Comparison Operators Sandbox",
        "question": "Complete the JavaScript code using strict equality and relational operators.",
        "starter_code": "console.log('Strict equal:', '20' _____ 20);\nconsole.log('Greater check:', 50 _____ 25);",
        "options": ["===", ">", "==", "<="],
    },
    "skill_exa_test": [
        {
            "question": "What is the key difference between loose equality (==) and strict equality (===)?",
            "options": [
                "Strict equality (===) checks both value and data type without performing implicit type coercion",
                "Loose equality (==) checks type only",
                "Strict equality (===) converts strings to numbers automatically",
                "There is no difference"
            ],
            "answer": "Strict equality (===) checks both value and data type without performing implicit type coercion",
        },
        {
            "question": "What is the output of evaluating '10' === 10 in JavaScript?",
            "options": ["false", "true", "undefined", "TypeError"],
            "answer": "false",
        },
        {
            "question": "What is the output of evaluating '10' == 10 in JavaScript?",
            "options": ["true", "false", "null", "undefined"],
            "answer": "true",
        },
        {
            "question": "Which comparison operator returns true if the left operand is greater than or equal to the right operand?",
            "options": [">=", "<=", "==", "!="],
            "answer": ">=",
        },
        {
            "question": "What does the strict inequality operator (!==) return when comparing '5' !== 5?",
            "options": ["true", "false", "null", "undefined"],
            "answer": "true",
        },
    ],
}

# Override Topic 801: Logical Operators - Chapter 2
JS_TOPICS[801] = {
    "id": 801,
    "title": "Logical Operators - Chapter 2",
    "category": "Fundamentals",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "An operator is a symbol used to perform an operation on one or more values or variables. Logical operators perform boolean logic on operands: Logical AND (&&), Logical OR (||), and Logical NOT (!). Chapter 2 covers boolean evaluation, short-circuit behavior, and truthy/falsy conversion.",
    "theory": "What is an Operator?\nAn operator is a symbol used to perform an operation on one or more values or variables.\n\n1. LOGICAL OPERATORS:\n- && (Logical AND) : Returns true if BOTH operands are true. Short-circuits to false if left operand is falsy.\n- || (Logical OR) : Returns true if AT LEAST ONE operand is true. Short-circuits to true if left operand is truthy.\n- ! (Logical NOT) : Negates boolean value (!true is false, !false is true).\n\n2. SHORT-CIRCUIT EVALUATION:\n- false && expr : Immediately evaluates to false without evaluating right operand.\n- true || expr : Immediately evaluates to true without evaluating right operand.\n\n3. TRUTHY & FALSY VALUES:\n- Falsy values: false, 0, '', null, undefined, NaN.\n- All other values are truthy.",
    "syntax": "const a = true, b = false;\nconsole.log(a && b); // false\nconsole.log(a || b); // true\nconsole.log(!a);     // false\nconsole.log(!!'hello'); // true",
    "example": {
        "code": "const a = true, b = false;\nconsole.log('a && b:', a && b);\nconsole.log('a || b:', a || b);\nconsole.log('!a:', !a);\nconsole.log('!b:', !b);\nconsole.log('Short circuit fallback:', null || 'Default Name');",
        "output": "a && b: false\na || b: true\n!a: false\n!b: true\nShort circuit fallback: Default Name",
        "explanation": "a && b requires both operands to be true. a || b returns true because a is true. null || 'Default Name' returns fallback value.",
    },
    "fill_blanks": {
        "question": "const a = true, b = false;\nconsole.log(a _____ b); // Returns false because both are not true\nconsole.log(a _____ b); // Returns true because one operand is true",
        "answers": ["&&", "||"],
        "options": ["&&", "||", "!", "=="],
    },
    "compiler": {
        "title": "Logical Operators Sandbox",
        "question": "Complete the JavaScript code using logical OR and logical NOT operators.",
        "starter_code": "const isWeekend = false, isHoliday = true;\nconsole.log('Day off:', isWeekend _____ isHoliday);\nconsole.log('Not weekend:', _____isWeekend);",
        "options": ["||", "!", "&&", "==="],
    },
    "skill_exa_test": [
        {
            "question": "What is the output of true && false in JavaScript?",
            "options": ["false", "true", "null", "undefined"],
            "answer": "false",
        },
        {
            "question": "What is the output of false || true in JavaScript?",
            "options": ["true", "false", "null", "undefined"],
            "answer": "true",
        },
        {
            "question": "What does the logical NOT operator ! return when applied to falsy values like 0 or ''?",
            "options": ["true", "false", "null", "0"],
            "answer": "true",
        },
        {
            "question": "What is short-circuit evaluation in logical AND (&&) operations?",
            "options": [
                "If the left operand is falsy, evaluation stops immediately and returns the falsy value without evaluating the right operand",
                "It causes the browser to reload",
                "It throws a ReferenceError",
                "It converts booleans into numbers"
            ],
            "answer": "If the left operand is falsy, evaluation stops immediately and returns the falsy value without evaluating the right operand",
        },
        {
            "question": "What does !!'SkillExa' evaluate to in JavaScript?",
            "options": ["true", "false", "null", "undefined"],
            "answer": "true",
        },
    ],
}

# Override Topic 9: Unary, Ternary & Comma Operators
JS_TOPICS[9] = {
    "id": 9,
    "title": "Unary, Ternary & Comma Operators",
    "category": "Fundamentals",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "An operator is a symbol used to perform an operation on one or more values or variables. Unary operators operate on a single operand (+, -, ++, --, !, typeof, delete). Ternary operator (? :) is a shorthand conditional expression. Comma operator (,) evaluates expressions left-to-right and returns the rightmost operand value.",
    "theory": "What is an Operator?\nAn operator is a symbol used to perform an operation on one or more values or variables.\n\n1. UNARY OPERATORS (Operate on 1 operand):\n - + Unary Plus: Converts operand to number (+'42' -> 42).\n - - Negation: Changes sign of number (-5).\n - ++ Increment: Adds 1 (++x prefix vs x++ postfix).\n - -- Decrement: Subtracts 1 (--x vs x--).\n - ! Logical NOT: Inverts boolean value.\n - typeof: Returns data type name string.\n - delete: Removes property from object.\n\n2. TERNARY OPERATOR (? :):\nShorthand for if-else statements: condition ? expression1 : expression2\n\n3. COMMA OPERATOR (,):\nEvaluates operands sequentially from left to right and returns the rightmost operand: (n1 = 1, n2 = 2, n1 + n2) -> 3.",
    "syntax": "let x = 5;\nconsole.log(+x, -x, ++x, --x, !x);\n\nconst status = age >= 18 ? 'Adult' : 'Minor';\n\nlet n1, n2;\nconst res = (n1 = 1, n2 = 2, n1 + n2);",
    "example": {
        "code": "let x = 5;\nconsole.log('+x:', +x);\nconsole.log('-x:', -x);\nconsole.log('++x:', ++x);\n\nconst age = 18;\nconst status = age >= 18 ? 'Adult' : 'Minor';\nconsole.log('Status:', status);\n\nlet n1, n2;\nconst res = (n1 = 1, n2 = 2, n1 + n2);\nconsole.log('Comma result:', res);\n\nconsole.log('typeof 42:', typeof 42);",
        "output": "+x: 5\n-x: -5\n++x: 6\nStatus: Adult\nComma result: 3\ntypeof 42: number",
        "explanation": "++x increments 5 to 6 before logging. Ternary checks age >= 18. Comma operator returns rightmost sum result 3.",
    },
    "fill_blanks": {
        "question": "const age = 20;\nconst status = age >= 18 _____ 'Adult' : 'Minor';\nlet n1, n2;\nconst res = (n1 = 1, n2 = 2, n1 _____ n2);",
        "answers": ["?", "+"],
        "options": ["?", "+", ":", ","],
    },
    "compiler": {
        "title": "Unary, Ternary & Comma Sandbox",
        "question": "Complete the code using ternary operator and comma operator.",
        "starter_code": "const score = 85;\nconst result = score >= 50 _____ 'Pass' : 'Fail';\nlet a, b;\nconst total = (a = 10, b = 20, a _____ b);\nconsole.log('Result:', result, 'Total:', total);",
        "options": ["?", "+", ":", ","],
    },
    "skill_exa_test": [
        {
            "question": "What value is returned by the expression: const res = (n1 = 1, n2 = 2, n1 + n2);?",
            "options": ["3", "1", "2", "undefined"],
            "answer": "3",
        },
        {
            "question": "What is the difference between ++x (prefix) and x++ (postfix) increment operators?",
            "options": [
                "Prefix ++x increments before evaluating the expression; postfix x++ evaluates first then increments",
                "Prefix ++x adds 2, postfix x++ adds 1",
                "Postfix x++ works only on strings",
                "There is no difference"
            ],
            "answer": "Prefix ++x increments before evaluating the expression; postfix x++ evaluates first then increments",
        },
        {
            "question": "What is the result of evaluating typeof 'Hello'?",
            "options": ["'string'", "'String'", "'text'", "'char'"],
            "answer": "'string'",
        },
        {
            "question": "What does the ternary expression 5 > 10 ? 'Yes' : 'No' evaluate to?",
            "options": ["'No'", "'Yes'", "true", "false"],
            "answer": "'No'",
        },
        {
            "question": "What does the delete unary operator do when invoked on an object property (e.g. delete obj.prop)?",
            "options": [
                "Removes the property from the object",
                "Sets the property value to 0",
                "Deletes the entire object",
                "Converts property to string"
            ],
            "answer": "Removes the property from the object",
        }
    ],
}

# Override Topic 10: Bitwise & Relational Operators
JS_TOPICS[10] = {
    "id": 10,
    "title": "Bitwise & Relational Operators",
    "category": "Fundamentals",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "Bitwise operators perform calculations on 32-bit binary representations of numbers (&, |, ^, ~, <<, >>, >>>). Relational operators determine relationship between operands ('in' checks property existence, 'instanceof' checks constructor prototype).",
    "theory": "1. BITWISE OPERATORS (Operate on binary bit representations):\n - & Bitwise AND: 1 if both bits are 1.\n - | Bitwise OR: 1 if at least one bit is 1.\n - ^ Bitwise XOR: 1 if bits differ.\n - ~ Bitwise NOT: Inverts all bits.\n - << Left Shift: Shifts bits left, filling 0s on right.\n - >> Sign-propagating Right Shift: Shifts bits right, preserving sign.\n - >>> Zero-fill Right Shift: Shifts bits right, filling left bits with 0s.\n\n2. RELATIONAL OPERATORS:\n - in: Checks if property exists in an object ('length' in obj).\n - instanceof: Checks if object is instance of constructor ([] instanceof Array).",
    "syntax": "const resAnd = 5 & 1;\nconst resOr = 5 | 1;\n\nconst obj = { length: 10 };\nconsole.log('length' in obj);\nconsole.log([] instanceof Array);",
    "example": {
        "code": "const resAnd = 5 & 1; // 0101 & 0001 = 0001 (1)\nconst resOr = 5 | 1;  // 0101 | 0001 = 0101 (5)\nconsole.log('5 & 1:', resAnd);\nconsole.log('5 | 1:', resOr);\n\nconst obj = { length: 10 };\nconsole.log('\"length\" in obj:', 'length' in obj);\nconsole.log('[] instanceof Array:', [] instanceof Array);",
        "output": "5 & 1: 1\n5 | 1: 5\n\"length\" in obj: true\n[] instanceof Array: true",
        "explanation": "5 & 1 in binary is 0101 & 0001 = 0001 (1). Relational 'in' verifies length property exists. 'instanceof' verifies Array inheritance.",
    },
    "fill_blanks": {
        "question": "const obj = { length: 10 };\nconsole.log('length' _____ obj); // Checks property existence\nconsole.log([] _____ Array); // Checks prototype constructor",
        "answers": ["in", "instanceof"],
        "options": ["in", "instanceof", "typeof", "has"],
    },
    "compiler": {
        "title": "Bitwise & Relational Sandbox",
        "question": "Complete the JavaScript code using bitwise AND and relational instanceof operators.",
        "starter_code": "const res = 5 _____ 1;\nconsole.log('Bitwise AND:', res);\nconsole.log('Is Array:', [1, 2, 3] _____ Array);",
        "options": ["&", "instanceof", "in", "|"],
    },
    "skill_exa_test": [
        {
            "question": "What is the result of evaluating 5 & 1 using bitwise AND?",
            "options": ["1", "5", "6", "0"],
            "answer": "1",
        },
        {
            "question": "What does 'length' in { length: 10 } evaluate to?",
            "options": ["true", "false", "10", "undefined"],
            "answer": "true",
        },
        {
            "question": "What does [] instanceof Array evaluate to?",
            "options": ["true", "false", "Object", "undefined"],
            "answer": "true",
        },
        {
            "question": "What does the bitwise NOT operator ~ do?",
            "options": [
                "Inverts all bits of the binary representation",
                "Adds 1 to the number",
                "Converts number to boolean",
                "Shifts bits to the left"
            ],
            "answer": "Inverts all bits of the binary representation",
        },
        {
            "question": "What is the difference between >> and >>> shift operators?",
            "options": [
                ">> preserves the sign bit; >>> fills left bits with zeros regardless of sign",
                ">> shifts left; >>> shifts right",
                ">> works on strings; >>> works on numbers",
                "There is no difference"
            ],
            "answer": ">> preserves the sign bit; >>> fills left bits with zeros regardless of sign",
        }
    ],
}

# Override Topic 11: Advanced Operators (Optional Chaining & BigInt)
JS_TOPICS[11] = {
    "id": 11,
    "title": "Advanced Operators (Optional Chaining & BigInt)",
    "category": "Fundamentals",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "Optional Chaining (?.) safely accesses deeply nested object properties without throwing TypeError if references are null or undefined. BigInt operators perform arithmetic on arbitrarily large integers.",
    "theory": "1. OPTIONAL CHAINING OPERATOR (?.):\nSafely accesses nested properties: obj.address?.city returns city if address exists, or undefined if address is null/undefined (without throwing TypeError).\n\n2. NULLISH COALESCING OPERATOR (??):\nvalue ?? defaultValue returns defaultValue ONLY if value is null or undefined (unlike || which also falls back on 0 or '').\n\n3. BIGINT OPERATORS:\nArithmetic (+, -, *, /) on BigInt numbers denoted by 'n' suffix (12345678901234567890n + 98765432109876543210n).",
    "syntax": "const user = { name: 'Aman', address: { city: 'Delhi' } };\nconsole.log(user.address?.city);\nconsole.log(user.contact?.phone); // undefined\n\nconst big1 = 100n;\nconst big2 = 200n;\nconsole.log(big1 + big2);",
    "example": {
        "code": "const user = { name: 'Aman', address: { city: 'Delhi' } };\nconsole.log('City:', user.address?.city);\nconsole.log('Phone:', user.contact?.phone);\n\nconst count = 0;\nconsole.log('count || 10:', count || 10);\nconsole.log('count ?? 10:', count ?? 10);\n\nconst big1 = 123456789012345678901234567890n;\nconst big2 = 987654321098765432109876543210n;\nconsole.log('BigInt sum:', big1 + big2);",
        "output": "City: Delhi\nPhone: undefined\ncount || 10: 10\ncount ?? 10: 0\nBigInt sum: 111111111011111111101111111110n",
        "explanation": "user.contact?.phone returns undefined safely without error. count ?? 10 returns 0 because 0 is not nullish. BigInt sum performs exact arithmetic.",
    },
    "fill_blanks": {
        "question": "const user = { name: 'Aman' };\nconst phone = user.contact_____phone; // Returns undefined safely\nconst val = null _____ 'default'; // Returns 'default'",
        "answers": ["?.", "??"],
        "options": ["?.", "??", "||", "&&"],
    },
    "compiler": {
        "title": "Advanced Operators Sandbox",
        "question": "Complete the JavaScript code using optional chaining and BigInt addition.",
        "starter_code": "const data = { profile: { email: 'user@skillexa.com' } };\nconsole.log('Email:', data.profile_____email);\nconst b1 = 500n, b2 = 300n;\nconsole.log('BigInt Sum:', b1 _____ b2);",
        "options": ["?.", "+", "??", "in"],
    },
    "skill_exa_test": [
        {
            "question": "What does optional chaining (?. ) return when accessing a property on a null or undefined reference?",
            "options": ["undefined", "null", "TypeError exception", "false"],
            "answer": "undefined",
        },
        {
            "question": "What is the key difference between || (OR) and ?? (Nullish Coalescing)?",
            "options": [
                "?? falls back ONLY when value is null or undefined, whereas || falls back on any falsy value (like 0 or '')",
                "|| works only on numbers",
                "?? is deprecated",
                "There is no difference"
            ],
            "answer": "?? falls back ONLY when value is null or undefined, whereas || falls back on any falsy value (like 0 or '')",
        },
        {
            "question": "How are BigInt literals specified in JavaScript code?",
            "options": ["Appending an 'n' suffix to the integer (e.g. 100n)", "Wrapping number in quotes", "Using BigInt() keyword only", "Prefixing with 0b"],
            "answer": "Appending an 'n' suffix to the integer (e.g. 100n)",
        },
        {
            "question": "What happens if you attempt to add a BigInt and a standard Number directly without explicit conversion (10n + 5)?",
            "options": ["Throws a TypeError", "Returns 15n", "Returns 15", "Returns NaN"],
            "answer": "Throws a TypeError",
        },
        {
            "question": "Can optional chaining (?.) be used to safely invoke optional functions (e.g. obj.method?.())?",
            "options": ["Yes, it invokes the function only if it exists", "No, it works only on object properties", "Only in strict mode", "Only in Node.js"],
            "answer": "Yes, it invokes the function only if it exists",
        }
    ],
}

# Override Topic 12: If, If-Else & Else-If Statements
JS_TOPICS[12] = {
    "id": 12,
    "title": "If, If-Else & Else-If Statements",
    "category": "Fundamentals",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "Conditional statements in JavaScript control program execution flow by making decisions based on boolean expressions. if, if...else, and if...else if...else statements execute distinct blocks of code depending on evaluated conditions.",
    "theory": "JavaScript Conditional Execution Breakdown:\n\n1. IF STATEMENT:\nExecutes code inside { } ONLY if condition is truthy:\nconst age = 18;\nif (age >= 18) {\n    console.log('You are an adult.');\n}\n\n2. IF...ELSE STATEMENT:\nProvides a fallback block executed when condition is falsy:\nconst score = 40;\nif (score >= 50) {\n    console.log('You passed.');\n} else {\n    console.log('You failed.');\n}\n\n3. IF...ELSE IF...ELSE STATEMENT:\nEvaluates multiple sequential conditions until one evaluates to true:\nconst temp = 25;\nif (temp > 30) {\n    console.log('It is hot.');\n} else if (temp >= 20) {\n    console.log('It is warm.');\n} else {\n    console.log('It is cold.');\n}\n\n4. TRUTHY AND FALSY VALUES:\nIn JavaScript, 0, '', null, undefined, NaN, and false evaluate to false in conditional statements. All other values evaluate to true.",
    "syntax": "if (condition1) {\n    // Code executed if condition1 is true\n} else if (condition2) {\n    // Code executed if condition2 is true\n} else {\n    // Fallback code executed if all conditions are false\n}",
    "example": {
        "code": "const score = 85;\nif (score >= 90) {\n    console.log('Grade: A');\n} else if (score >= 75) {\n    console.log('Grade: B');\n} else if (score >= 50) {\n    console.log('Grade: C');\n} else {\n    console.log('Grade: F');\n}",
        "output": "Grade: B",
        "explanation": "score (85) fails score >= 90, matches score >= 75, outputs 'Grade: B', and skips remaining else blocks.",
    },
    "fill_blanks": {
        "question": "const score = 40;\nif (score >= 50) {\n    console.log('You passed.');\n} _____ {\n    console.log('You failed.');\n}",
        "answers": ["else"],
        "options": ["else", "elif", "otherwise", "then"],
    },
    "compiler": {
        "title": "Conditional Statements Sandbox",
        "question": "Complete the JavaScript code using else if statement to check temperature.",
        "starter_code": "const temp = 25;\nif (temp > 30) {\n    console.log('Hot');\n} _____ if (temp >= 20) {\n    console.log('Warm');\n} else {\n    console.log('Cold');\n}",
        "options": ["else", "then", "or", "case"],
    },
    "skill_exa_test": [
        {
            "question": "When does the block inside an 'if' statement execute in JavaScript?",
            "options": [
                "ONLY when the specified condition evaluates to a truthy value",
                "ONLY when the specified condition evaluates to false",
                "Every time the script runs regardless of condition",
                "Only when an error occurs"
            ],
            "answer": "ONLY when the specified condition evaluates to a truthy value",
        },
        {
            "question": "What is the purpose of the 'else' block in an if...else statement?",
            "options": [
                "To execute a fallback block of code when the if condition evaluates to false",
                "To restart the program from the beginning",
                "To define a new variable scope",
                "To convert string values to numbers"
            ],
            "answer": "To execute a fallback block of code when the if condition evaluates to false",
        },
        {
            "question": "Which of the following values is evaluated as FALSY inside a conditional statement in JavaScript?",
            "options": ["0", "'Hello'", "[]", "1"],
            "answer": "0",
        },
        {
            "question": "What is the output of: const x = 10; if (x > 15) { console.log('High'); } else if (x > 5) { console.log('Mid'); } else { console.log('Low'); }?",
            "options": ["Mid", "High", "Low", "Nothing"],
            "answer": "Mid",
        },
        {
            "question": "What happens when multiple conditions match in an if...else if...else chain?",
            "options": [
                "ONLY the FIRST matching condition block is executed, and remaining conditions are skipped",
                "All matching condition blocks are executed sequentially",
                "The program throws a SyntaxError",
                "The last matching condition block overrides previous ones"
            ],
            "answer": "ONLY the FIRST matching condition block is executed, and remaining conditions are skipped",
        }
    ],
}

# Override Topic 13: Switch Statement
JS_TOPICS[13] = {
    "id": 13,
    "title": "Switch Statement",
    "category": "Fundamentals",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "The switch statement evaluates an expression against multiple case values using strict equality (===) and executes matching code blocks. It provides a cleaner, structured alternative to long if...else if chains.",
    "theory": "Switch Statement Mechanics:\n\n1. Expression Matching:\nEvaluates target expression once and compares against each 'case' label using strict equality (===).\n\n2. The 'break' Statement:\nExits the switch block immediately. Omitting 'break' causes 'fall-through' into subsequent cases regardless of whether they match!\n\n3. The 'default' Clause:\nOptional catch-all block executed if no case match is found.\n\n4. Multi-case Grouping:\nMultiple case statements can share a single execution block by stacking case labels.",
    "syntax": "switch (expression) {\n    case value1:\n        // Code executed if expression === value1\n        break;\n    case value2:\n        // Code executed if expression === value2\n        break;\n    default:\n        // Fallback code if no cases match\n}",
    "example": {
        "code": "const day = 'Friday';\nswitch (day) {\n    case 'Monday':\n        console.log('Start of the workweek.');\n        break;\n    case 'Friday':\n        console.log('End of the workweek.');\n        break;\n    default:\n        console.log('Regular weekday.');\n}",
        "output": "End of the workweek.",
        "explanation": "day === 'Friday' matches case 'Friday', prints log, and break statement exits switch block.",
    },
    "fill_blanks": {
        "question": "const day = 'Friday';\nswitch (day) {\n    case 'Friday':\n        console.log('Weekend ready!');\n        _____;\n    _____:\n        console.log('Regular day');\n}",
        "answers": ["break", "default"],
        "options": ["break", "default", "continue", "stop"],
    },
    "compiler": {
        "title": "Switch Statement Sandbox",
        "question": "Complete the JavaScript code using switch case label and default clause.",
        "starter_code": "const fruit = 'Apple';\nswitch (fruit) {\n    _____ 'Apple':\n        console.log('Red fruit');\n        break;\n    _____:\n        console.log('Unknown fruit');\n}",
        "options": ["case", "default", "when", "if"],
    },
    "skill_exa_test": [
        {
            "question": "Which comparison operator is used by the switch statement to match expression against case labels?",
            "options": [
                "Strict equality (===)",
                "Loose equality (==)",
                "Greater than (>)",
                "Assignment (=)"
            ],
            "answer": "Strict equality (===)",
        },
        {
            "question": "What happens if you omit the 'break' statement at the end of a matching case block?",
            "options": [
                "Execution 'falls through' and continues executing subsequent case blocks regardless of matching",
                "The program immediately terminates with an exception",
                "The default block is automatically skipped",
                "The switch block restarts from the top"
            ],
            "answer": "Execution 'falls through' and continues executing subsequent case blocks regardless of matching",
        },
        {
            "question": "What is the purpose of the 'default' clause in a switch statement?",
            "options": [
                "To execute a fallback block of code when no case label matches the evaluated expression",
                "To declare global variables",
                "To force strict mode in JavaScript",
                "To clear browser memory"
            ],
            "answer": "To execute a fallback block of code when no case label matches the evaluated expression",
        },
        {
            "question": "What is the output of: const x = '5'; switch(x) { case 5: console.log('Number'); break; case '5': console.log('String'); break; }?",
            "options": ["String", "Number", "Both String and Number", "SyntaxError"],
            "answer": "String",
        },
        {
            "question": "Can multiple case statements share a single block of execution code in JavaScript?",
            "options": [
                "Yes, by stacking case labels without break statements (e.g. case 'A': case 'B': code; break;)",
                "No, every case must have a unique execution block",
                "Only in Node.js runtime",
                "Only when evaluating booleans"
            ],
            "answer": "Yes, by stacking case labels without break statements (e.g. case 'A': case 'B': code; break;)",
        }
    ],
}

# Override Topic 14: For Loop
JS_TOPICS[14] = {
    "id": 14,
    "title": "For Loop",
    "category": "Fundamentals",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "The for loop repeats a block of code a specified number of times by consolidating counter initialization, continuation condition, and counter update into a single header statement.",
    "theory": "For Loop Structure & Lifecycle:\n\n1. Syntax: for (initialization; condition; update) { block }\n - Initialization: Executed once before loop starts (e.g. let i = 1).\n - Condition: Evaluated BEFORE each iteration; if true, body runs; if false, loop terminates.\n - Update: Executed AFTER each iteration body (e.g. i++).\n\n2. Counter Variable Scoping:\nDeclaring loop counter with 'let' keeps it block-scoped inside loop; using 'var' leaks counter variable to outer scope.\n\n3. Infinite Loops:\nIf continuation condition never evaluates to false (e.g., missing counter update), the browser/engine hangs in an infinite loop.",
    "syntax": "for (initialization; condition; update) {\n    // Code block to be executed repeatedly\n}",
    "example": {
        "code": "let sum = 0;\nfor (let i = 1; i <= 5; i++) {\n    sum += i;\n}\nconsole.log('Sum 1 to 5:', sum);",
        "output": "Sum 1 to 5: 15",
        "explanation": "Iterates 5 times with i = 1, 2, 3, 4, 5, accumulating sum to 15.",
    },
    "fill_blanks": {
        "question": "// Print numbers 1 to 3\nfor (let i = 1; i <= 3; _____ ) {\n    console.log(i);\n}",
        "answers": ["i++"],
        "options": ["i++", "i--", "i = 0", "break"],
    },
    "compiler": {
        "title": "For Loop Sandbox",
        "question": "Complete the for loop header statement to iterate 4 times.",
        "starter_code": "_____ (let i = 1; i <= 4; i++) {\n    console.log('Step: ' + i);\n}",
        "options": ["for", "while", "loop", "repeat"],
    },
    "skill_exa_test": [
        {
            "question": "In what order are the 3 expressions inside a for loop header (initialization; condition; update) executed?",
            "options": [
                "Initialization (once) -> Condition check -> Body execution -> Update -> Repeat condition check",
                "Initialization -> Update -> Body execution -> Condition check",
                "Condition check -> Initialization -> Body execution -> Update",
                "Body execution -> Update -> Condition check -> Initialization"
            ],
            "answer": "Initialization (once) -> Condition check -> Body execution -> Update -> Repeat condition check",
        },
        {
            "question": "What happens if the condition expression inside a for loop header evaluates to false on the very first check?",
            "options": [
                "The loop body is skipped entirely and never executes",
                "The loop body executes exactly once",
                "A SyntaxError is thrown",
                "The counter is set to null"
            ],
            "answer": "The loop body is skipped entirely and never executes",
        },
        {
            "question": "Why is declaring loop counter variables with 'let' (for (let i = 0; ...)) preferred over 'var'?",
            "options": [
                "'let' restricts counter scope to the loop block, preventing global variable pollution",
                "'var' causes the loop to run backwards",
                "'let' makes loops run 10x faster",
                "There is no difference"
            ],
            "answer": "'let' restricts counter scope to the loop block, preventing global variable pollution",
        },
        {
            "question": "What is the output of: for (let i = 0; i < 3; i++) {} console.log(i); when declared with let?",
            "options": [
                "ReferenceError: i is not defined",
                "3",
                "0",
                "undefined"
            ],
            "answer": "ReferenceError: i is not defined",
        },
        {
            "question": "What causes an infinite loop in a for loop?",
            "options": [
                "A condition that always evaluates to true or missing counter update",
                "Declaring counter with let",
                "Using console.log inside the loop",
                "Using less than or equal (<=) operator"
            ],
            "answer": "A condition that always evaluates to true or missing counter update",
        }
    ],
}

# Override Topic 15: While & Do-While Loops
JS_TOPICS[15] = {
    "id": 15,
    "title": "While & Do-While Loops",
    "category": "Fundamentals",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "The while loop executes code repeatedly as long as a specified condition remains true (entry-controlled). The do...while loop executes the code block at least once before checking the condition (exit-controlled).",
    "theory": "1. WHILE LOOP (Entry-Controlled):\nEvaluates condition BEFORE executing loop body. If condition is false initially, body NEVER executes:\nlet i = 1;\nwhile (i <= 3) {\n    console.log(i);\n    i++;\n}\n\n2. DO...WHILE LOOP (Exit-Controlled):\nExecutes loop body FIRST, then evaluates condition at the bottom. Guarantees at least 1 execution even if condition is false:\nlet j = 10;\ndo {\n    console.log('Runs at least once:', j);\n    j++;\n} while (j < 5);\n\n3. Key Comparison:\n - while loop checks condition BEFORE entry.\n - do...while loop checks condition AFTER exit.",
    "syntax": "// while loop\nwhile (condition) {\n    // Code block\n}\n\n// do...while loop\ndo {\n    // Code block\n} while (condition);",
    "example": {
        "code": "let count = 1;\nwhile (count <= 3) {\n    console.log('while count:', count);\n    count++;\n}\n\nlet num = 10;\ndo {\n    console.log('do-while num (runs once):', num);\n    num++;\n} while (num < 5);",
        "output": "while count: 1\nwhile count: 2\nwhile count: 3\ndo-while num (runs once): 10",
        "explanation": "while loop runs 3 times while count <= 3. do-while loop runs once even though 10 < 5 is false.",
    },
    "fill_blanks": {
        "question": "let i = 1;\n_____ {\n    console.log(i);\n    i++;\n} _____ (i <= 3);",
        "answers": ["do", "while"],
        "options": ["do", "while", "for", "repeat"],
    },
    "compiler": {
        "title": "While & Do-While Sandbox",
        "question": "Complete the while loop to print numbers as long as count <= 3.",
        "starter_code": "let count = 1;\n_____ (count <= 3) {\n    console.log('Count: ' + count);\n    count++;\n}",
        "options": ["while", "do", "for", "if"],
    },
    "skill_exa_test": [
        {
            "question": "What is the primary difference between a while loop and a do...while loop in JavaScript?",
            "options": [
                "A do...while loop evaluates condition after executing body, guaranteeing at least one execution; while loop checks condition before entry",
                "while loops run faster than do...while loops",
                "do...while loops work only on arrays",
                "while loops do not require counter variables"
            ],
            "answer": "A do...while loop evaluates condition after executing body, guaranteeing at least one execution; while loop checks condition before entry",
        },
        {
            "question": "How many times will a do...while loop execute if its condition evaluates to false on the first check?",
            "options": ["Exactly 1 time", "0 times", "Infinite times", "2 times"],
            "answer": "Exactly 1 time",
        },
        {
            "question": "How many times will a while loop execute if its condition evaluates to false on the first check?",
            "options": ["0 times", "1 time", "Infinite times", "Undefined"],
            "answer": "0 times",
        },
        {
            "question": "What must be included inside the body of a while loop to prevent infinite loop bugs?",
            "options": [
                "A statement that updates variables involved in the continuation condition (e.g. i++)",
                "A break statement in every line",
                "A return statement",
                "A console.log statement"
            ],
            "answer": "A statement that updates variables involved in the continuation condition (e.g. i++)",
        },
        {
            "question": "Which loop type is considered 'exit-controlled'?",
            "options": ["do...while loop", "while loop", "for loop", "for...in loop"],
            "answer": "do...while loop",
        }
    ],
}

# Override Topic 16: Loop Control (Break & Continue)
JS_TOPICS[16] = {
    "id": 16,
    "title": "Loop Control (Break & Continue)",
    "category": "Fundamentals",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "Loop control statements alter normal iteration flow: break terminates loop execution immediately, while continue skips the current iteration and jumps to the next cycle.",
    "theory": "1. THE BREAK STATEMENT:\nTerminates the innermost loop or switch statement immediately. Execution resumes at statement following loop:\nfor (let i = 1; i <= 5; i++) {\n    if (i === 3) break;\n    console.log(i); // Prints 1, 2\n}\n\n2. THE CONTINUE STATEMENT:\nSkips remaining statements in current iteration body and jumps directly to counter update / condition check:\nfor (let i = 1; i <= 5; i++) {\n    if (i === 3) continue;\n    console.log(i); // Prints 1, 2, 4, 5 (skips 3!)\n}\n\n3. LABELED STATEMENTS:\nLabels (outerLoop: for (...)) allow break and continue to target specific outer nested loops.",
    "syntax": "// Terminate loop\nbreak;\n\n// Skip current iteration\ncontinue;\n\n// Labeled break\nlabelName: for (...) {\n    break labelName;\n}",
    "example": {
        "code": "console.log('--- Continue Output ---');\nfor (let i = 1; i <= 5; i++) {\n    if (i === 3) continue;\n    console.log('Item:', i);\n}\n\nconsole.log('--- Break Output ---');\nfor (let i = 1; i <= 5; i++) {\n    if (i === 4) break;\n    console.log('Val:', i);\n}",
        "output": "--- Continue Output ---\nItem: 1\nItem: 2\nItem: 4\nItem: 5\n--- Break Output ---\nVal: 1\nVal: 2\nVal: 3",
        "explanation": "continue skips printing Item 3. break stops loop when Val reaches 4.",
    },
    "fill_blanks": {
        "question": "for (let i = 1; i <= 5; i++) {\n    if (i === 3) _____; // Skip 3\n    if (i === 5) _____; // Stop loop\n    console.log(i);\n}",
        "answers": ["continue", "break"],
        "options": ["continue", "break", "stop", "exit"],
    },
    "compiler": {
        "title": "Loop Control Sandbox",
        "question": "Complete the code to skip iteration when i === 3.",
        "starter_code": "for (let i = 1; i <= 5; i++) {\n    if (i === 3) _____;\n    console.log('Num: ' + i);\n}",
        "options": ["continue", "break", "pass", "return"],
    },
    "skill_exa_test": [
        {
            "question": "What does the 'break' statement do when executed inside a loop?",
            "options": [
                "Terminates loop execution immediately and transfers control to statement following loop",
                "Skips current iteration and moves to next iteration",
                "Pauses script execution for 1 second",
                "Restarts loop counter from zero"
            ],
            "answer": "Terminates loop execution immediately and transfers control to statement following loop",
        },
        {
            "question": "What does the 'continue' statement do when executed inside a loop?",
            "options": [
                "Skips remaining code in current iteration body and jumps to next iteration cycle",
                "Terminates entire loop immediately",
                "Exits current function",
                "Deletes loop counter variable"
            ],
            "answer": "Skips remaining code in current iteration body and jumps to next iteration cycle",
        },
        {
            "question": "What is the output of: for (let i = 1; i <= 4; i++) { if (i === 2) continue; console.log(i); }?",
            "options": ["1, 3, 4", "1, 2, 3, 4", "1", "2, 3, 4"],
            "answer": "1, 3, 4",
        },
        {
            "question": "What is the output of: for (let i = 1; i <= 4; i++) { if (i === 3) break; console.log(i); }?",
            "options": ["1, 2", "1, 2, 3", "3, 4", "1, 2, 3, 4"],
            "answer": "1, 2",
        },
        {
            "question": "How can break or continue target an outer loop from inside a nested loop?",
            "options": [
                "Using labeled statements (e.g. break myLabel;)",
                "Using double semicolon (break;;)",
                "Using return keyword",
                "It is impossible in JavaScript"
            ],
            "answer": "Using labeled statements (e.g. break myLabel;)",
        }
    ],
}

# Override Topic 17: Global & Local Scope
JS_TOPICS[17] = {
    "id": 17,
    "title": "Global & Local Scope",
    "category": "Fundamentals",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "Scope in JavaScript defines where a variable can be accessed or used within a program. Global variables are accessible anywhere in the program, whereas Local (Function) variables exist only within the function body in which they are declared.",
    "theory": "Global vs Local Scope Breakdown:\n\n1. GLOBAL SCOPE:\nA variable declared outside any function or block is globally scoped. It can be accessed and modified from anywhere in the program, including inside functions.\nlet x = 10; // Global Variable\nfunction fun1() {\n    console.log(x); // Accessible inside function!\n}\nfun1();\n\n2. LOCAL (FUNCTION) SCOPE:\nA variable declared inside a function body is local to that function. It is created when the function executes and destroyed when the function finishes. It CANNOT be accessed outside the function.\nfunction fun2() {\n    let y = 20; // Local Variable\n    console.log(y);\n}\nfun2();\n// console.log(y); // ReferenceError: y is not defined\n\n3. VAR VS LET/CONST SCOPING:\n - var is function-scoped. Declared outside a function, it attaches to global scope.\n - let and const prevent accidental global variable creation and global namespace pollution.",
    "syntax": "// Global Scope\nlet globalVar = 10;\n\nfunction myFunc() {\n    // Local Scope\n    let localVar = 20;\n    console.log(globalVar, localVar);\n}",
    "example": {
        "code": "const globalX = 10;\n\nfunction fun1() {\n    console.log('Global globalX inside fun1:', globalX);\n}\n\nfunction fun2() {\n    let localY = 20;\n    console.log('Local localY inside fun2:', localY);\n}\n\nfun1();\nfun2();",
        "output": "Global globalX inside fun1: 10\nLocal localY inside fun2: 20",
        "explanation": "globalX is accessible anywhere. localY is local to fun2 and inaccessible outside.",
    },
    "fill_blanks": {
        "question": "const x = 10; // _____ Scope variable\n\nfunction fun2() {\n    let y = 20; // _____ Scope variable to fun2()\n    console.log(x, y);\n}",
        "answers": ["Global", "Local"],
        "options": ["Global", "Local", "Block", "Module"],
    },
    "compiler": {
        "title": "Global & Local Scope Sandbox",
        "question": "Complete the JavaScript code to log local variable inside function.",
        "starter_code": "let globalVal = 50;\nfunction showValues() {\n    let _____ = 100;\n    console.log(globalVal + localVal);\n}\nshowValues();",
        "options": ["localVal", "globalVal", "x", "val"],
    },
    "skill_exa_test": [
        {
            "question": "What is the scope of a variable declared outside of any function or block in a classic JavaScript script?",
            "options": [
                "Global Scope",
                "Local Scope",
                "Block Scope",
                "Module Scope"
            ],
            "answer": "Global Scope",
        },
        {
            "question": "What happens when you try to access a function-scoped local variable outside the function in which it was declared?",
            "options": [
                "Throws a ReferenceError",
                "Returns null",
                "Returns 0",
                "Automatically converts it to a global variable"
            ],
            "answer": "Throws a ReferenceError",
        },
        {
            "question": "Which variable declaration keyword in JavaScript is function-scoped rather than block-scoped?",
            "options": ["var", "let", "const", "static"],
            "answer": "var",
        },
        {
            "question": "What is the lifetime of a local variable declared inside a function?",
            "options": [
                "It is created when the function executes and destroyed when the function call finishes",
                "It persists in browser memory indefinitely until window close",
                "It exists only during compilation phase",
                "It is re-instantiated on every line of code"
            ],
            "answer": "It is created when the function executes and destroyed when the function call finishes",
        },
        {
            "question": "Why is relying heavily on Global variables considered a bad programming practice?",
            "options": [
                "Global variables increase risk of accidental variable name conflicts and bugs across scripts",
                "Global variables cannot hold string values",
                "Global variables execute 100x slower",
                "Global variables disable function execution"
            ],
            "answer": "Global variables increase risk of accidental variable name conflicts and bugs across scripts",
        }
    ],
}

# Override Topic 18: Block, Lexical & Module Scope
JS_TOPICS[18] = {
    "id": 18,
    "title": "Block, Lexical & Module Scope",
    "category": "Fundamentals",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "ES6 introduced Block Scope ({ } with let and const), Lexical Scope (nested function scope lookup), and Module Scope (file-level isolation) to provide strict variable visibility rules.",
    "theory": "1. BLOCK SCOPE ({ }):\nVariables declared with let or const inside { } blocks (if statements, loops, or plain {}) exist ONLY within that block.\n{\n    var x = 10;   // Does NOT have block scope (leaks out!)\n    let y = 20;   // Block-scoped\n    const z = 30; // Block-scoped\n}\nconsole.log(x); // 10 (Accessible!)\n// console.log(y); // ReferenceError!\n\n2. LEXICAL SCOPE:\nAn inner function has access to variables defined in its outer enclosing scope based on where functions are written in source code:\nfunction func1() {\n    const x = 10;\n    function func2() {\n        const y = 20;\n        console.log(x, y); // func2 accesses x from func1\n    }\n    func2();\n}\n\n3. MODULE SCOPE:\nVariables declared inside an ES module (script type='module') are scoped strictly to that module file and do not pollute global window/globalThis scope.",
    "syntax": "// Block Scope\n{\n    let b = 2;\n}\n\n// Lexical Scope\nfunction outer() {\n    const a = 1;\n    function inner() {\n        console.log(a); // Lexical access\n    }\n    inner();\n}",
    "example": {
        "code": "{\n    var leakedVar = 'I am var (leaks block)';\n    let blockLet = 'I am let (block-scoped)';\n    console.log(blockLet);\n}\nconsole.log(leakedVar);\n\nfunction func1() {\n    const x = 10;\n    function func2() {\n        const y = 20;\n        console.log(`Lexical Scope: x=${x}, y=${y}`);\n    }\n    func2();\n}\nfunc1();",
        "output": "I am let (block-scoped)\nI am var (leaks block)\nLexical Scope: x=10, y=20",
        "explanation": "blockLet is restricted to block. leakedVar leaks out because var is not block-scoped. func2 accesses x via lexical scope.",
    },
    "fill_blanks": {
        "question": "{\n    var x = 10; // Does NOT have _____ scope\n    let y = 20; // Has _____ scope\n}\nconsole.log(x); // Outputs 10",
        "answers": ["block", "block"],
        "options": ["block", "global", "lexical", "module"],
    },
    "compiler": {
        "title": "Block & Lexical Scope Sandbox",
        "question": "Complete the inner function to access variable from outer lexical scope.",
        "starter_code": "function outer() {\n    const x = 10;\n    function inner() {\n        const y = 20;\n        console.log(x + y); // Demonstrates _____ scope\n    }\n    inner();\n}\nouter();",
        "options": ["lexical", "global", "block", "dynamic"],
    },
    "skill_exa_test": [
        {
            "question": "Which variable declaration keywords in JavaScript enforce block scope inside { } curly braces?",
            "options": ["let and const", "var only", "var and let", "function"],
            "answer": "let and const",
        },
        {
            "question": "What happens when you access a 'var' variable outside of an 'if' block in which it was declared?",
            "options": [
                "It is accessible because var is function-scoped or global, not block-scoped",
                "It throws a ReferenceError",
                "It returns undefined automatically",
                "It deletes the variable"
            ],
            "answer": "It is accessible because var is function-scoped or global, not block-scoped",
        },
        {
            "question": "What is 'Lexical Scope' in JavaScript?",
            "options": [
                "An inner function can access variables from its outer enclosing scope based on code structure",
                "Variables are assigned dynamically at runtime from call stack",
                "Scope that changes every 5 seconds",
                "Variables accessible only inside HTML tags"
            ],
            "answer": "An inner function can access variables from its outer enclosing scope based on code structure",
        },
        {
            "question": "What is the Temporal Dead Zone (TDZ)?",
            "options": [
                "The period between entering scope and variable initialization where accessing let/const throws ReferenceError",
                "The time after garbage collection",
                "When a loop runs infinitely",
                "When an async promise is pending"
            ],
            "answer": "The period between entering scope and variable initialization where accessing let/const throws ReferenceError",
        },
        {
            "question": "What is the primary benefit of Module Scope in modern ES JavaScript?",
            "options": [
                "It isolates variables within specific script files, preventing global scope pollution",
                "It forces JavaScript to compile into C++",
                "It disables function hoisting",
                "It makes all variables constant"
            ],
            "answer": "It isolates variables within specific script files, preventing global scope pollution",
        }
    ],
}

# Override Topic 19: Function Declarations & Default Parameters
JS_TOPICS[19] = {
    "id": 19,
    "title": "Function Declarations & Default Parameters",
    "category": "Functions",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "Functions in JavaScript are reusable blocks of code that perform specific tasks. Parameters act as placeholders inside function declarations, while arguments are real values supplied when invoking the function. Default parameters provide fallback values when arguments are omitted.",
    "theory": "Function Declarations Breakdown:\n\n1. NAMED FUNCTION DECLARATIONS:\nDefined using the function keyword with an identifier name. Fully hoisted to top of scope.\nfunction greet(name) {\n    return 'Hello ' + name;\n}\n\n2. PARAMETERS VS ARGUMENTS:\n - Parameter: Placeholder defined in function signature (e.g. name).\n - Argument: Actual value passed when calling function (e.g. 'Alice').\n\n3. DEFAULT PARAMETERS (ES6):\nProvides fallback value if parameter is omitted or passed as undefined:\nfunction greet(name = 'Guest') {\n    return 'Hello, ' + name;\n}\n\n4. RETURN STATEMENT:\nSends a result back to call site and immediately terminates function execution.",
    "syntax": "function greet(name = 'Guest') {\n    return 'Hello, ' + name;\n}\nconst msg1 = greet();        // 'Hello, Guest'\nconst msg2 = greet('Alice'); // 'Hello, Alice'",
    "example": {
        "code": "function calculateTotal(price, taxRate = 0.18) {\n    return price + (price * taxRate);\n}\nconsole.log('Total with default tax:', calculateTotal(100));\nconsole.log('Total with custom tax:', calculateTotal(100, 0.10));",
        "output": "Total with default tax: 118\nTotal with custom tax: 110",
        "explanation": "calculateTotal uses default tax 0.18 when second argument is omitted.",
    },
    "fill_blanks": {
        "question": "function greet(name = 'Guest') {\n    _____ 'Hello, ' + name;\n}\nconsole.log(greet());",
        "answers": ["return"],
        "options": ["return", "send", "log", "default"],
    },
    "compiler": {
        "title": "Function Declaration Sandbox",
        "question": "Complete function declaration with default parameter.",
        "starter_code": "_____ add(a, b = 5) {\n    return a + b;\n}\nconsole.log(add(10));",
        "options": ["function", "def", "func", "fn"],
    },
    "skill_exa_test": [
        {
            "question": "What is the difference between a parameter and an argument in JavaScript functions?",
            "options": [
                "Parameters are placeholders defined in function signature; arguments are real values passed upon calling",
                "Arguments are defined in signature; parameters are passed upon calling",
                "Parameters work only with numbers",
                "There is no difference"
            ],
            "answer": "Parameters are placeholders defined in function signature; arguments are real values passed upon calling",
        },
        {
            "question": "When does a function use a default parameter value?",
            "options": [
                "When no argument or 'undefined' is passed for that parameter during call",
                "When null is passed",
                "Only when an exception occurs",
                "Default parameters must always be overridden"
            ],
            "answer": "When no argument or 'undefined' is passed for that parameter during call",
        },
        {
            "question": "What does the 'return' statement do inside a JavaScript function body?",
            "options": [
                "Specifies return value and terminates function execution immediately",
                "Restarts function from line 1",
                "Converts function to arrow function",
                "Pauses execution for 5 seconds"
            ],
            "answer": "Specifies return value and terminates function execution immediately",
        },
        {
            "question": "Are standard named Function Declarations hoisted in JavaScript?",
            "options": [
                "Yes, function declarations are fully hoisted to top of scope and can be called before declaration line",
                "No, function declarations throw ReferenceError if called before line",
                "Only in strict mode",
                "Only when declared inside loops"
            ],
            "answer": "Yes, function declarations are fully hoisted to top of scope and can be called before declaration line",
        },
        {
            "question": "What is returned by a JavaScript function that does NOT contain a return statement?",
            "options": ["undefined", "null", "0", "false"],
            "answer": "undefined",
        }
    ],
}

# Override Topic 20: Anonymous Functions & Function Expressions
JS_TOPICS[20] = {
    "id": 20,
    "title": "Anonymous Functions & Function Expressions",
    "category": "Functions",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "Anonymous functions are defined without an explicit name. A Function Expression creates a function as part of an assignment to a variable or passed as an argument.",
    "theory": "Anonymous Functions & Function Expressions:\n\n1. ANONYMOUS FUNCTIONS:\nFunctions without an identifier string after function keyword: function() { ... }\n\n2. FUNCTION EXPRESSIONS:\nAssigning an anonymous or named function to a variable:\nconst add = function(a, b) {\n    return a + b;\n};\n\n3. HOISTING DIFFERENCE:\nFunction expressions assigned to let/const/var are NOT hoisted prior to variable initialization! Calling them before assignment line throws ReferenceError or TypeError.",
    "syntax": "const greet = function() {\n    return 'Hi there!';\n};\nconsole.log(greet());",
    "example": {
        "code": "const multiply = function(a, b) {\n    return a * b;\n};\nconsole.log('2 * 4 =', multiply(2, 4));\n\nconst sayHi = function() {\n    return 'Hello from anonymous function expression!';\n};\nconsole.log(sayHi());",
        "output": "2 * 4 = 8\nHello from anonymous function expression!",
        "explanation": "multiply and sayHi store anonymous function references in const variables.",
    },
    "fill_blanks": {
        "question": "const add = _____ (a, b) {\n    return a + b;\n};\nconsole.log(add(2, 3));",
        "answers": ["function"],
        "options": ["function", "def", "lambda", "create"],
    },
    "compiler": {
        "title": "Function Expression Sandbox",
        "question": "Complete the anonymous function expression assignment.",
        "starter_code": "const square = _____ (n) {\n    return n * n;\n};\nconsole.log(square(4));",
        "options": ["function", "def", "val", "build"],
    },
    "skill_exa_test": [
        {
            "question": "What is an anonymous function in JavaScript?",
            "options": [
                "A function defined without an explicit name string identifier",
                "A function that cannot return values",
                "A function that runs only on server",
                "A function with no arguments"
            ],
            "answer": "A function defined without an explicit name string identifier",
        },
        {
            "question": "What happens if you invoke a Function Expression variable before its assignment line (e.g. const add = function(){})?",
            "options": [
                "Throws a ReferenceError or TypeError",
                "Executes successfully due to hoisting",
                "Returns null",
                "Compiles silently"
            ],
            "answer": "Throws a ReferenceError or TypeError",
        },
        {
            "question": "Can a Function Expression be assigned to a const variable?",
            "options": [
                "Yes, assigning to const prevents reassigning the function reference",
                "No, function expressions require let only",
                "Only in HTML event handlers",
                "Only inside switch blocks"
            ],
            "answer": "Yes, assigning to const prevents reassigning the function reference",
        },
        {
            "question": "Why are anonymous function expressions commonly used as callback arguments?",
            "options": [
                "They provide inline execution logic without cluttering outer scope with one-time function names",
                "They run faster on single CPU cores",
                "They disable variable scope",
                "They automatically handle promises"
            ],
            "answer": "They provide inline execution logic without cluttering outer scope with one-time function names",
        },
        {
            "question": "Can Function Expressions be named (e.g. const fn = function myName(){})?",
            "options": [
                "Yes, named function expressions help stack trace debugging",
                "No, function expressions must strictly be anonymous",
                "Only in Node.js",
                "Only in ES5"
            ],
            "answer": "Yes, named function expressions help stack trace debugging",
        }
    ],
}

# Override Topic 21: Arrow Functions & IIFE
JS_TOPICS[21] = {
    "id": 21,
    "title": "Arrow Functions & IIFE",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "ES6 Arrow Functions (=>) provide a concise syntax for writing functions with lexical this binding. Immediately Invoked Function Expressions (IIFE) execute immediately upon definition to create private variable scopes.",
    "theory": "1. ARROW FUNCTIONS (=>):\nProvides compact syntax and lexically binds 'this':\n - Single expression implicit return: const square = n => n * n;\n - Does NOT have its own 'this', 'arguments', or 'super'.\n - Cannot be used as constructor functions with new.\n\n2. IIFE (IMMEDIATELY INVOKED FUNCTION EXPRESSION):\nExecuted immediately after creation to form private scope:\n(function() {\n    console.log('This runs immediately!');\n})();",
    "syntax": "// Arrow Function\nconst double = n => n * 2;\n\n// IIFE\n(function() {\n    // Code runs immediately\n})();",
    "example": {
        "code": "const add = (a, b) => a + b;\nconsole.log('Arrow Add 3 + 7:', add(3, 7));\n\n(function() {\n    const privateKey = 'SKILLEXA_SECRET_123';\n    console.log('IIFE initialized privately with key length:', privateKey.length);\n})();",
        "output": "Arrow Add 3 + 7: 10\nIIFE initialized privately with key length: 19",
        "explanation": "add is a concise arrow function. IIFE executes immediately upon script load.",
    },
    "fill_blanks": {
        "question": "const square = n _____ n * n; // Arrow syntax\n( _____ () {\n    console.log('IIFE executed!');\n})();",
        "answers": ["=>", "function"],
        "options": ["=>", "function", "->", "def"],
    },
    "compiler": {
        "title": "Arrow Function & IIFE Sandbox",
        "question": "Complete the arrow function syntax.",
        "starter_code": "const greet = (name) _____ 'Hello ' + name;\nconsole.log(greet('SkillExa'));",
        "options": ["=>", "->", "=", "return"],
    },
    "skill_exa_test": [
        {
            "question": "What is the key difference between how 'this' is bound in arrow functions versus standard function declarations?",
            "options": [
                "Arrow functions do NOT have their own 'this'; they inherit 'this' lexically from surrounding scope",
                "Arrow functions rebind 'this' to window automatically",
                "Arrow functions create dynamic this bindings at call time",
                "There is no difference"
            ],
            "answer": "Arrow functions do NOT have their own 'this'; they inherit 'this' lexically from surrounding scope",
        },
        {
            "question": "Can an Arrow Function be invoked using the 'new' keyword as a constructor?",
            "options": [
                "No, attempting to call an arrow function with 'new' throws a TypeError",
                "Yes, arrow functions behave identically to constructor functions",
                "Only if declared with let",
                "Only in strict mode"
            ],
            "answer": "No, attempting to call an arrow function with 'new' throws a TypeError",
        },
        {
            "question": "What does an IIFE (Immediately Invoked Function Expression) do?",
            "options": [
                "Executes immediately after definition to create an isolated private variable scope",
                "Pauses execution until async promise settles",
                "Converts code into WebAssembly",
                "Fires when browser window resizes"
            ],
            "answer": "Executes immediately after definition to create an isolated private variable scope",
        },
        {
            "question": "What is the implicit return rule for single-expression Arrow Functions (e.g. const double = n => n * 2)?",
            "options": [
                "Omitting curly braces { } automatically returns evaluated expression without requiring explicit return keyword",
                "Implicit return works only for string outputs",
                "You must always write return keyword in arrow functions",
                "Implicit return returns undefined"
            ],
            "answer": "Omitting curly braces { } automatically returns evaluated expression without requiring explicit return keyword",
        },
        {
            "question": "Which of the following syntaxes correctly represents an IIFE in JavaScript?",
            "options": [
                "(function() { console.log('Run'); })();",
                "function() { console.log('Run'); }();",
                "iife function() { console.log('Run'); }",
                "run (function() { console.log('Run'); })"
            ],
            "answer": "(function() { console.log('Run'); })();",
        }
    ],
}

# Override Topic 22: Callback & Rest Parameter Functions
JS_TOPICS[22] = {
    "id": 22,
    "title": "Callback & Rest Parameter Functions",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "A Callback function is passed as an argument to another function and executed later. Rest parameter syntax (...args) collects an indefinite number of arguments into a true Array object.",
    "theory": "1. CALLBACK FUNCTIONS:\nA function passed into another function as an argument, invoked inside outer function body to complete an action:\nfunction num(n, callback) {\n    return callback(n);\n}\n\n2. REST PARAMETER FUNCTIONS (...args):\nCollects remaining arguments into an array signature:\nfunction sum(...nums) {\n    return nums.reduce((a, b) => a + b, 0);\n}\n - Rest parameter MUST be the last parameter in signature.\n - Provides true Array methods (map, filter, reduce) unlike legacy 'arguments'.",
    "syntax": "// Callback\nfunction num(n, callback) {\n    return callback(n);\n}\n\n// Rest Parameter\nfunction sum(...nums) {\n    return nums.reduce((a, b) => a + b, 0);\n}",
    "example": {
        "code": "function operateOnNum(n, callback) {\n    return callback(n);\n}\nconsole.log('Callback output:', operateOnNum(5, n => n * 2));\n\nfunction sum(...nums) {\n    return nums.reduce((total, n) => total + n, 0);\n}\nconsole.log('Rest Param Sum (1,2,3,4):', sum(1, 2, 3, 4));",
        "output": "Callback output: 10\nRest Param Sum (1,2,3,4): 10",
        "explanation": "operateOnNum executes double callback. sum gathers arguments 1,2,3,4 into array.",
    },
    "fill_blanks": {
        "question": "function num(n, _____) {\n    return callback(n);\n}\nfunction sum( _____ nums) {\n    return nums.length;\n}",
        "answers": ["callback", "..."],
        "options": ["callback", "...", "fn", "args"],
    },
    "compiler": {
        "title": "Callback & Rest Parameter Sandbox",
        "question": "Complete the rest parameter syntax to accept variable arguments.",
        "starter_code": "function total( _____ numbers) {\n    return numbers.reduce((a, b) => a + b, 0);\n}\nconsole.log(total(10, 20, 30));",
        "options": ["...", "array", "args", "rest"],
    },
    "skill_exa_test": [
        {
            "question": "What is a Callback Function in JavaScript?",
            "options": [
                "A function passed as an argument to another function, to be invoked inside outer function",
                "A function that returns a boolean only",
                "A function that calls window.location",
                "A function declared with static keyword"
            ],
            "answer": "A function passed as an argument to another function, to be invoked inside outer function",
        },
        {
            "question": "What does the rest parameter syntax (...nums) do in function signatures?",
            "options": [
                "Collects remaining arguments into a true Array object",
                "Converts numbers to strings",
                "Deletes arguments passed after position 1",
                "Forces arguments to be constant"
            ],
            "answer": "Collects remaining arguments into a true Array object",
        },
        {
            "question": "Where must a rest parameter (...args) be placed in a function parameter list?",
            "options": [
                "It MUST be the LAST parameter in the function signature",
                "It must be the first parameter",
                "It can be placed anywhere in signature",
                "It must be placed in a separate block"
            ],
            "answer": "It MUST be the LAST parameter in the function signature",
        },
        {
            "question": "What is a key advantage of rest parameters (...args) over legacy 'arguments' object?",
            "options": [
                "Rest parameters produce a true Array instance with array methods (map, reduce, filter)",
                "Rest parameters work only with strings",
                "Legacy arguments object is faster",
                "There is no advantage"
            ],
            "answer": "Rest parameters produce a true Array instance with array methods (map, reduce, filter)",
        },
        {
            "question": "What is the output of: function test(...nums){ return nums.length; } console.log(test(5, 10, 15));?",
            "options": ["3", "30", "[5, 10, 15]", "undefined"],
            "answer": "3",
        }
    ],
}

# Override Topic 23: Constructor & Pure Functions
JS_TOPICS[23] = {
    "id": 23,
    "title": "Constructor & Pure Functions",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "Constructor functions create and initialize object instances when invoked with the new keyword. Pure functions always return identical outputs for identical inputs without causing side effects.",
    "theory": "1. CONSTRUCTOR FUNCTIONS:\nUsed to blueprint and instantiate multiple objects with matching properties:\nfunction Person(name, age) {\n    this.name = name;\n    this.age = age;\n}\nconst user = new Person('Neha', 22);\n - Called with 'new' keyword.\n - 'this' points to newly created object instance.\n\n2. PURE FUNCTIONS:\n - Return same output for same input parameters.\n - Produce NO side effects (does not mutate global state, outer variables, or arguments).",
    "syntax": "// Constructor Function\nfunction Person(name, age) {\n    this.name = name;\n    this.age = age;\n}\nconst user = new Person('Neha', 22);\n\n// Pure Function\nfunction pureAdd(a, b) {\n    return a + b;\n}",
    "example": {
        "code": "function Person(name, age) {\n    this.name = name;\n    this.age = age;\n}\nconst user = new Person('Neha', 22);\nconsole.log('Created user object:', user.name, user.age);\n\nfunction pureSquare(n) {\n    return n * n;\n}\nconsole.log('Pure function result:', pureSquare(5));",
        "output": "Created user object: Neha 22\nPure function result: 25",
        "explanation": "new Person creates user instance. pureSquare produces 25 without side effects.",
    },
    "fill_blanks": {
        "question": "function User(name) {\n    this.name = name;\n}\nconst person = _____ User('Aman'); // Instantiate constructor\n\nfunction pureAdd(a, b) {\n    _____ a + b; // Pure return\n}",
        "answers": ["new", "return"],
        "options": ["new", "return", "create", "static"],
    },
    "compiler": {
        "title": "Constructor & Pure Function Sandbox",
        "question": "Complete the constructor instantiation using new keyword.",
        "starter_code": "function Product(title, price) {\n    this.title = title;\n    this.price = price;\n}\nconst p1 = _____ Product('Laptop', 1200);\nconsole.log(p1.title);",
        "options": ["new", "create", "build", "make"],
    },
    "skill_exa_test": [
        {
            "question": "What does the 'new' keyword do when calling a Constructor Function?",
            "options": [
                "Creates a empty object, binds 'this' to it, executes constructor body, and returns object",
                "Converts function to JSON",
                "Deletes object after execution",
                "Runs function asynchronously"
            ],
            "answer": "Creates a empty object, binds 'this' to it, executes constructor body, and returns object",
        },
        {
            "question": "What is the defining characteristic of a Pure Function?",
            "options": [
                "Always produces same output for same inputs and produces zero side effects",
                "Mutates global variables on every call",
                "Uses async/await only",
                "Must be declared with const keyword"
            ],
            "answer": "Always produces same output for same inputs and produces zero side effects",
        },
        {
            "question": "Which of the following is considered a 'side effect' in JavaScript functions?",
            "options": [
                "All of the above (Modifying global variables, mutating input objects, or console I/O)",
                "Modifying a global variable",
                "Mutating an object passed as an argument",
                "Writing data to disk or DOM"
            ],
            "answer": "All of the above (Modifying global variables, mutating input objects, or console I/O)",
        },
        {
            "question": "By convention, how are Constructor Functions named in JavaScript source code?",
            "options": [
                "Capitalized PascalCase (e.g. Person, Car)",
                "camelCase with underscore",
                "UPPERCASE_SNAKE_CASE",
                "lowercase single letters"
            ],
            "answer": "Capitalized PascalCase (e.g. Person, Car)",
        },
        {
            "question": "What happens if you invoke a Constructor Function WITHOUT the 'new' keyword (e.g. Person('Neha', 22)) in non-strict mode?",
            "options": [
                "'this' binds to global window/globalThis, polluting global scope instead of returning new instance",
                "Throws SyntaxError immediately",
                "Creates object instance automatically",
                "Returns null"
            ],
            "answer": "'this' binds to global window/globalThis, polluting global scope instead of returning new instance",
        }
    ],
}

# Override Topic 24: Generator Functions
JS_TOPICS[24] = {
    "id": 24,
    "title": "Generator Functions",
    "category": "Functions",
    "difficulty": "Advanced",
    "duration": "25 min",
    "concept": "A Generator Function is a special function defined using function* syntax that can pause its execution using the yield keyword and resume later upon calling next(), returning a Generator Iterator object ({ value, done }).",
    "theory": "1. Working & Iterator Protocol: Generator functions return a Generator object conforming to the iterator protocol. Calling gen.next() resumes execution until the next yield statement, returning { value, done }.\n2. State Preservation & Control: Each next() invocation resumes execution from where it was last paused, preserving local variable state across yields.\n3. Use Cases: Ideal for generating custom sequence iterators (e.g. Fibonacci), handling lazy infinite sequences (while(true) yield i++), and managing asynchronous control flows.\n4. Advantages & Limitations: Provides lazy evaluation (computing values on demand) and modularity, though debugging can be complex.",
    "syntax": "function* generatorFunction() {\n    yield 'Hello';\n    yield 'World';\n    return 'Done';\n}\nconst gen = generatorFunction();\nconsole.log(gen.next()); // { value: 'Hello', done: false }",
    "example": {
        "code": "function* fibonacci(limit) {\n    let [prev, current] = [0, 1];\n    while (limit--) {\n        yield current;\n        [prev, current] = [current, prev + current];\n    }\n}\nconst fib = fibonacci(5);\nconsole.log([...fib]);\n\nfunction* infiniteSeq() {\n    let i = 1;\n    while (true) {\n        yield i++;\n    }\n}\nconst seq = infiniteSeq();\nconsole.log(seq.next().value);\nconsole.log(seq.next().value);",
        "output": "[ 1, 1, 2, 3, 5 ]\n1\n2",
        "explanation": "fibonacci generator yields sequence values up to limit. infiniteSeq produces lazy on-demand numbers infinitely using while(true).",
    },
    "fill_blanks": {
        "question": "function_____ generate() {\n    _____ 'Step 1';\n}\nconst g = generate();\nconsole.log(g.next());",
        "answers": ["*", "yield"],
        "options": ["*", "yield", "async", "return"],
    },
    "compiler": {
        "title": "Generator Function Practice",
        "question": "Use the yield keyword to emit value 100 from generator.",
        "starter_code": "function* gen() {\n    _____ 100;\n}\nconst g = gen();\nconsole.log(g.next().value);",
        "options": ["yield", "return", "send", "emit"],
    },
    "skill_exa_test": [
        {
            "question": "How is a Generator Function declared in JavaScript?",
            "options": [
                "Using function* syntax with an asterisk",
                "Using async function syntax",
                "Using generator class syntax",
                "Using yield function syntax"
            ],
            "answer": "Using function* syntax with an asterisk",
        },
        {
            "question": "What does the 'yield' keyword do inside a Generator Function body?",
            "options": [
                "Pauses generator function execution and returns a value to the caller",
                "Permanently terminates function execution",
                "Throws a RangeError exception",
                "Converts string variables to numbers"
            ],
            "answer": "Pauses generator function execution and returns a value to the caller",
        },
        {
            "question": "What object shape is returned when calling .next() on a Generator object?",
            "options": [
                "{ value: any, done: boolean }",
                "{ data: any, status: string }",
                "[value, done]",
                "Promise object"
            ],
            "answer": "{ value: any, done: boolean }",
        },
        {
            "question": "What advantage does Lazy Evaluation provide in Generator Functions?",
            "options": [
                "Values are computed on demand when next() is called, improving performance for large or infinite sequences",
                "Executes code before compilation phase",
                "Deletes variables from memory automatically",
                "Bypasses strict mode error checks"
            ],
            "answer": "Values are computed on demand when next() is called, improving performance for large or infinite sequences",
        },
        {
            "question": "What is the value of 'done' when a Generator Function reaches its end or returns?",
            "options": ["true", "false", "undefined", "null"],
            "answer": "true",
        },
    ],
}

# Override Topic 25: Higher-Order Functions Basics (Passing & Returning Functions)
JS_TOPICS[25] = {
    "id": 25,
    "title": "Higher-Order Functions Basics (Passing & Returning Functions)",
    "category": "Functions",
    "difficulty": "Advanced",
    "duration": "25 min",
    "concept": "A Higher-Order Function (HOF) is a function that receives another function as an argument, returns a function as its result, or both. They enable modular, reusable, and declarative code patterns.",
    "theory": "1. Passing Functions as Arguments: In JavaScript, functions are first-class citizens and can be passed as callback parameters to control execution sequence.\n2. Returning Functions (Function Factories): Higher-order functions can generate and return customized function instances, taking advantage of closures to remember surrounding scope parameters.",
    "syntax": "function fun2(action) {\n    action();\n}\nfunction mul(factor) {\n    return function(num) {\n        return num * factor;\n    };\n}",
    "example": {
        "code": "function greet(name, callback) {\n    console.log('Hello, ' + name);\n    callback();\n}\ngreet('Alice', function() {\n    console.log('Goodbye!');\n});",
        "output": "Hello, Alice\nGoodbye!",
        "explanation": "greet is a higher-order function taking callback function as an argument and executing it after printing the greeting.",
    },
    "fill_blanks": {
        "question": "function run(fn) {\n    _____(10);\n}\nrun(function(x) {\n    console.log(x * 2);\n});",
        "answers": ["fn"],
        "options": ["fn", "run", "callback", "return"],
    },
    "compiler": {
        "title": "HOF Function Factory",
        "question": "Complete multiplier function factory that returns a new function.",
        "starter_code": "function createMultiplier(factor) {\n    _____ (num) => num * factor;\n}\nconst double = createMultiplier(2);\nconsole.log(double(5));",
        "options": ["return", "function", "const", "def"],
    },
    "skill_exa_test": [
        {
            "question": "What defines a Higher-Order Function in JavaScript?",
            "options": [
                "A function that accepts another function as an argument or returns a function",
                "A function with more than 10 lines of code",
                "A function defined inside an object constructor",
                "A function that executes asynchronously only"
            ],
            "answer": "A function that accepts another function as an argument or returns a function",
        },
        {
            "question": "Why are functions called 'First-Class Citizens' in JavaScript?",
            "options": [
                "Because functions can be assigned to variables, passed as arguments, and returned from other functions",
                "Because functions execute faster than loops",
                "Because functions have global execution scope by default",
                "Because functions can only be defined using the function keyword"
            ],
            "answer": "Because functions can be assigned to variables, passed as arguments, and returned from other functions",
        },
        {
            "question": "What is a 'Function Factory' pattern?",
            "options": [
                "A higher-order function that returns a customized new function instance",
                "An HTML canvas drawing function",
                "A method to delete objects from memory",
                "A loop structure that generates array elements"
            ],
            "answer": "A higher-order function that returns a customized new function instance",
        },
        {
            "question": "What will function apply(f, x) { return f(x); } apply(n => n + 3, 5); evaluate to?",
            "options": ["8", "53", "undefined", "TypeError"],
            "answer": "8",
        },
        {
            "question": "What feature allows a returned function to retain access to outer variables?",
            "options": ["Closure", "Prototypes", "Hoisting", "Strict Mode"],
            "answer": "Closure",
        },
    ],
}

# Override Topic 26: Array HOFs: Transformation & Filtering (map & filter)
JS_TOPICS[30] = {
    "id": 30,
    "title": "Array HOFs: Transformation & Filtering (map & filter)",
    "category": "Functions",
    "difficulty": "Advanced",
    "duration": "25 min",
    "concept": "map() transforms each element of an array using a callback function and returns a new array. filter() creates a new array containing only elements that satisfy a condition.",
    "theory": "1. map() Method: Iterates over each array element, invokes callback (element, index, array), and returns a new array containing transformed items without mutating the original array (immutability).\n2. filter() Method: Evaluates a predicate callback returning true or false for each element, producing a new array with elements that pass the condition.",
    "syntax": "const doubled = arr.map(n => n * 2);\nconst evens = arr.filter(n => n % 2 === 0);",
    "example": {
        "code": "const nums = [1, 2, 3, 4, 5];\nconst squared = nums.map(n => n * n);\nconst odds = nums.filter(n => n % 2 !== 0);\nconsole.log(squared);\nconsole.log(odds);",
        "output": "[ 1, 4, 9, 16, 25 ]\n[ 1, 3, 5 ]",
        "explanation": "map returns a new array of squared numbers. filter returns a new array containing only odd numbers.",
    },
    "fill_blanks": {
        "question": "const nums = [1, 2, 3];\n// Transform elements\nconst doubled = nums._____(n => n * 2);\n// Filter even numbers\nconst evens = nums._____(n => n % 2 === 0);",
        "answers": ["map", "filter"],
        "options": ["map", "filter", "reduce", "forEach"],
    },
    "compiler": {
        "title": "Array Transformation Challenge",
        "question": "Use map() to double each number in the array.",
        "starter_code": "const arr = [10, 20, 30];\nconst result = arr._____(x => x * 2);\nconsole.log(result);",
        "options": ["map", "filter", "forEach", "reduce"],
    },
    "skill_exa_test": [
        {
            "question": "What does the map() method return?",
            "options": [
                "A new array containing transformed elements",
                "A single accumulated number",
                "The original mutated array",
                "A boolean value"
            ],
            "answer": "A new array containing transformed elements",
        },
        {
            "question": "How does filter() determine which elements to include in the output array?",
            "options": [
                "Includes elements where callback returns truthy",
                "Includes elements where callback returns false",
                "Includes first 5 elements only",
                "Includes duplicate elements only"
            ],
            "answer": "Includes elements where callback returns truthy",
        },
        {
            "question": "Do map() and filter() mutate the original source array?",
            "options": [
                "No, both return a new array and preserve original array immutability",
                "Yes, both modify the source array directly",
                "map() mutates but filter() does not",
                "filter() mutates but map() does not"
            ],
            "answer": "No, both return a new array and preserve original array immutability",
        },
        {
            "question": "What is the output of [1, 2, 3].map(n => n + 1).filter(n => n > 2)?",
            "options": ["[ 3, 4 ]", "[ 2, 3, 4 ]", "[ 1, 2 ]", "[ 4 ]"],
            "answer": "[ 3, 4 ]",
        },
        {
            "question": "What parameters are passed to map() callback function?",
            "options": [
                "(currentValue, index, array)",
                "(accumulator, currentValue)",
                "(key, value)",
                "(element, nextElement)"
            ],
            "answer": "(currentValue, index, array)",
        },
    ],
}

# Override Topic 27: Array HOFs: Accumulation & Iteration (reduce & forEach)
JS_TOPICS[31] = {
    "id": 31,
    "title": "Array HOFs: Accumulation & Iteration (reduce & forEach)",
    "category": "Functions",
    "difficulty": "Advanced",
    "duration": "25 min",
    "concept": "reduce() aggregates array elements into a single accumulated value. forEach() executes a provided function once for each element to perform side effects.",
    "theory": "1. reduce() Method: Processes array items sequentially using callback (accumulator, current, index, array) => updatedAccumulator starting from an initial value seed.\n2. forEach() Method: Executes side-effects (logging, DOM updates) per item, returning undefined without generating a new array.",
    "syntax": "const sum = arr.reduce((acc, curr) => acc + curr, 0);\narr.forEach(item => console.log(item));",
    "example": {
        "code": "const nums = [1, 2, 3, 4, 5];\nconst sum = nums.reduce((acc, curr) => acc + curr, 0);\nconsole.log('Sum:', sum);\nnums.forEach(n => console.log('Item:', n * 2));",
        "output": "Sum: 15\nItem: 2\nItem: 4\nItem: 6\nItem: 8\nItem: 10",
        "explanation": "reduce aggregates array numbers into total 15 starting at seed 0. forEach logs multiplied items as side effects.",
    },
    "fill_blanks": {
        "question": "const nums = [10, 20];\n// Accumulate total sum\nconst sum = nums._____((acc, val) => acc + val, 0);\n// Log each number\nnums._____(n => console.log(n));",
        "answers": ["reduce", "forEach"],
        "options": ["reduce", "forEach", "map", "filter"],
    },
    "compiler": {
        "title": "Array Reducer Exercise",
        "question": "Complete the reduce function to compute array product.",
        "starter_code": "const arr = [2, 3, 4];\nconst product = arr._____((acc, curr) => acc * curr, 1);\nconsole.log('Product:', product);",
        "options": ["reduce", "map", "forEach", "filter"],
    },
    "skill_exa_test": [
        {
            "question": "What is the main purpose of the reduce() method?",
            "options": [
                "To accumulate array elements into a single result value",
                "To filter out duplicate array values",
                "To sort array elements alphabetically",
                "To check if an array contains negative numbers"
            ],
            "answer": "To accumulate array elements into a single result value",
        },
        {
            "question": "What does forEach() return after executing its callback for all array elements?",
            "options": ["undefined", "A new array", "The modified original array", "The length of the array"],
            "answer": "undefined",
        },
        {
            "question": "What is the second parameter passed to array.reduce(callback, initialValue)?",
            "options": [
                "The initial seed value for the accumulator",
                "The target element index",
                "The maximum array length",
                "A fallback error handler"
            ],
            "answer": "The initial seed value for the accumulator",
        },
        {
            "question": "How does forEach() differ from map()?",
            "options": [
                "map() returns a new transformed array, whereas forEach() executes side-effects and returns undefined",
                "forEach() is faster and returns a boolean",
                "map() mutates original array while forEach() does not",
                "There is no difference between map() and forEach()"
            ],
            "answer": "map() returns a new transformed array, whereas forEach() executes side-effects and returns undefined",
        },
        {
            "question": "What will [1, 2, 3, 4].reduce((acc, curr) => acc + curr, 10) evaluate to?",
            "options": ["20", "10", "24", "15"],
            "answer": "20",
        },
    ],
}

# Override Topic 28: Array HOFs: Search & Predicate Testing (find, some & every)
JS_TOPICS[32] = {
    "id": 32,
    "title": "Array HOFs: Search & Predicate Testing (find, some & every)",
    "category": "Functions",
    "difficulty": "Advanced",
    "duration": "25 min",
    "concept": "find() returns the first element satisfying a condition. some() checks if at least one element satisfies a condition. every() verifies if all elements satisfy a condition.",
    "theory": "1. find() Method: Searches array left-to-right, returning the first element for which callback returns true; returns undefined if no element matches.\n2. some() Method: Evaluates predicate callback, returning true as soon as any single element satisfies condition.\n3. every() Method: Evaluates predicate callback, returning true only if every single element passes condition.",
    "syntax": "const item = arr.find(n => n > 10);\nconst hasNeg = arr.some(n => n < 0);\nconst allPos = arr.every(n => n > 0);",
    "example": {
        "code": "const nums = [1, 2, 3, 4, 5];\nconst firstEven = nums.find(n => n % 2 === 0);\nconst hasNegative = nums.some(n => n < 0);\nconst allPositive = nums.every(n => n > 0);\nconsole.log(firstEven);\nconsole.log(hasNegative);\nconsole.log(allPositive);",
        "output": "2\nfalse\ntrue",
        "explanation": "find returns 2 (first even element). some returns false (no negatives). every returns true (all numbers > 0).",
    },
    "fill_blanks": {
        "question": "const arr = [5, 12, 8];\n// Find first number > 10\nconst found = arr._____(n => n > 10);\n// Check if all elements > 0\nconst valid = arr._____(n => n > 0);",
        "answers": ["find", "every"],
        "options": ["find", "every", "some", "filter"],
    },
    "compiler": {
        "title": "Array Search Test",
        "question": "Complete the search to find the first element matching condition.",
        "starter_code": "const users = ['Alice', 'Bob', 'Charlie'];\nconst match = users._____(name => name.startsWith('B'));\nconsole.log(match);",
        "options": ["find", "some", "every", "map"],
    },
    "skill_exa_test": [
        {
            "question": "What does find() return if no array element satisfies the condition?",
            "options": ["undefined", "null", "-1", "[]"],
            "answer": "undefined",
        },
        {
            "question": "What is the return value of some() and every() methods?",
            "options": ["Boolean (true or false)", "A new array", "The matching element", "Array index integer"],
            "answer": "Boolean (true or false)",
        },
        {
            "question": "Under what condition does every() return true?",
            "options": [
                "Only when ALL array elements satisfy the callback condition",
                "When at least one element matches",
                "When array is empty",
                "When first element is even"
            ],
            "answer": "Only when ALL array elements satisfy the callback condition",
        },
        {
            "question": "How does some() optimize search execution when encountering a matching element?",
            "options": [
                "It short-circuits immediately and returns true without checking remaining elements",
                "It checks all remaining elements twice",
                "It converts array to set",
                "It restarts from index 0"
            ],
            "answer": "It short-circuits immediately and returns true without checking remaining elements",
        },
        {
            "question": "What will [2, 4, 6].every(n => n % 2 === 0) evaluate to?",
            "options": ["true", "false", "2", "undefined"],
            "answer": "true",
        },
    ],
}

# Override Topic 29: Advanced HOF Techniques (Composition, Currying & Memoization)
JS_TOPICS[33] = {
    "id": 33,
    "title": "Advanced HOF Techniques (Composition, Currying & Memoization)",
    "category": "Functions",
    "difficulty": "Advanced",
    "duration": "25 min",
    "concept": "Advanced HOF techniques include Function Composition (combining sequential functions), Currying (transforming multi-arg functions into single-arg chains), and Memoization (caching execution results).",
    "theory": "1. Function Composition: Combines multiple functions into a single pipeline compose(f, g)(x) => f(g(x)) passing output of g(x) to f.\n2. Currying: Converts a function taking multiple arguments f(a, b) into nested single-argument calls f(a)(b).\n3. Memoization: Wraps a function with a cache store to return cached results for duplicate inputs, avoiding expensive recomputations.",
    "syntax": "const compose = (f, g) => x => f(g(x));\nconst curriedAdd = a => b => a + b;\nconst memoize = fn => { const cache = {}; return arg => cache[arg] || (cache[arg] = fn(arg)); };",
    "example": {
        "code": "function add2(x) { return x + 2; }\nfunction mul3(x) { return x * 3; }\nfunction compose(f, g) {\n    return function(x) {\n        return f(g(x));\n    };\n}\nconst addThenMul = compose(add2, mul3);\nconsole.log(addThenMul(4));",
        "output": "14",
        "explanation": "compose passes 4 into mul3(4) => 12, then passes 12 into add2(12) => 14.",
    },
    "fill_blanks": {
        "question": "// Currying\nconst mul = x => _____ => x * y;\nconst double = mul(2);\nconsole.log(double(5)); // 10",
        "answers": ["y"],
        "options": ["y", "x", "return", "function"],
    },
    "compiler": {
        "title": "Curried Function Challenge",
        "question": "Complete the curried multiplier function.",
        "starter_code": "const multiply = x => _____ => x * y;\nconst triple = multiply(3);\nconsole.log(triple(4));",
        "options": ["y", "x", "val", "return"],
    },
    "skill_exa_test": [
        {
            "question": "What is Function Composition in JavaScript?",
            "options": [
                "Combining multiple functions in sequence so output of one function becomes input to the next",
                "Converting object keys into function names",
                "Executing functions in reverse array order",
                "Compressing function strings to save memory"
            ],
            "answer": "Combining multiple functions in sequence so output of one function becomes input to the next",
        },
        {
            "question": "What is Currying in JavaScript?",
            "options": [
                "Transforming a function taking multiple arguments into a sequence of functions that each take a single argument",
                "Binding this keyword to global window object",
                "Catching errors inside try-catch block automatically",
                "Deleting unused function variables"
            ],
            "answer": "Transforming a function taking multiple arguments into a sequence of functions that each take a single argument",
        },
        {
            "question": "What problem does Memoization solve?",
            "options": [
                "Caches function execution results to avoid redundant expensive recalculations for duplicate inputs",
                "Prevents memory leaks in closure scopes",
                "Enforces strict type checking on function parameters",
                "Asynchronously defers function calls"
            ],
            "answer": "Caches function execution results to avoid redundant expensive recalculations for duplicate inputs",
        },
        {
            "question": "What does const add = x => y => x + y; add(3)(4); output?",
            "options": ["7", "34", "undefined", "TypeError"],
            "answer": "7",
        },
        {
            "question": "What data structure is commonly used inside a memoization HOF to store cached results?",
            "options": [
                "A JavaScript Object or Map cache",
                "An Array buffer",
                "HTML Canvas context",
                "A Set iterator"
            ],
            "answer": "A JavaScript Object or Map cache",
        },
    ],
}

# Override Topic 30: Variable Hoisting & Temporal Dead Zone (var vs let/const)
JS_TOPICS[30] = {
    "id": 30,
    "title": "Variable Hoisting & Temporal Dead Zone (var vs let/const)",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "In JavaScript, variable declarations are moved to top of scope during compilation. 'var' variables are hoisted and initialized to undefined, while 'let' and 'const' are hoisted but remain in the Temporal Dead Zone (TDZ) until initialized.",
    "theory": "1. var Hoisting: Declarations are hoisted to top of scope and initialized with undefined. Accessing before assignment yields undefined. Re-declaring var in the same scope is permitted without error.\n2. let & const TDZ: Declarations are hoisted but not initialized. Accessing them before declaration line throws a ReferenceError. The TDZ spans from scope entry until declaration execution.",
    "syntax": "console.log(a); // undefined\nvar a = 5;\nvar a = 20; // re-declaration allowed\n\nconsole.log(b); // ReferenceError: Cannot access 'b' before initialization\nlet b = 10;",
    "example": {
        "code": "console.log(a);\nvar a = 5;\nvar a = 20;\nconsole.log(a);",
        "output": "undefined\n20",
        "explanation": "var declaration is hoisted with value undefined. Subsequent assignment sets a to 5, and re-declaration overwrites a to 20.",
    },
    "fill_blanks": {
        "question": "console.log(x); // undefined\n_____ x = 50;\n\nconsole.log(y); // ReferenceError\n_____ y = 100;",
        "answers": ["var", "let"],
        "options": ["var", "let", "const", "function"],
    },
    "compiler": {
        "title": "Variable Hoisting Test",
        "question": "Use the keyword that hoists variable as undefined instead of throwing a TDZ ReferenceError.",
        "starter_code": "console.log(myVar);\n_____ myVar = 'SkillExa Hoisting Passed';",
        "options": ["var", "let", "const", "def"],
    },
    "skill_exa_test": [
        {
            "question": "What value is logged when accessing a 'var' variable before its declaration line?",
            "options": ["undefined", "ReferenceError", "null", "0"],
            "answer": "undefined",
        },
        {
            "question": "What error occurs when accessing a 'let' or 'const' variable during its Temporal Dead Zone (TDZ)?",
            "options": ["ReferenceError", "TypeError", "SyntaxError", "RangeError"],
            "answer": "ReferenceError",
        },
        {
            "question": "What happens when you re-declare a variable using 'var' within the same scope?",
            "options": [
                "The second declaration overwrites the first without throwing an error",
                "Throws a SyntaxError",
                "Throws a ReferenceError",
                "The program terminates immediately"
            ],
            "answer": "The second declaration overwrites the first without throwing an error",
        },
        {
            "question": "When are 'let' and 'const' variables initialized during program execution?",
            "options": [
                "Only when execution reaches the declaration line in code",
                "During compilation phase",
                "At program startup with undefined",
                "Inside global object constructor"
            ],
            "answer": "Only when execution reaches the declaration line in code",
        },
        {
            "question": "Does variable hoisting lift variable initializations alongside declarations?",
            "options": [
                "No, hoisting lifts declarations only, not initializations",
                "Yes, both declarations and initializations are hoisted",
                "Only for let and const variables",
                "Only inside async functions"
            ],
            "answer": "No, hoisting lifts declarations only, not initializations",
        },
    ],
}

# Override Topic 31: Function Declaration vs Expression Hoisting
JS_TOPICS[31] = {
    "id": 31,
    "title": "Function Declaration vs Expression Hoisting",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "Function declarations are hoisted with both their name and full body definition, making them callable anywhere in scope. Function expressions are treated like variable declarations where only the variable name is hoisted.",
    "theory": "1. Function Declaration Hoisting: Entire function body is hoisted during compilation. Calling greet() before declaration works seamlessly.\n2. Function Expression Hoisting: The variable holding the expression is hoisted as undefined (for var). Calling hello() before assignment throws TypeError: hello is not a function.",
    "syntax": "greet(); // Works! 'Hello'\nfunction greet() { console.log('Hello'); }\n\nhello(); // TypeError: hello is not a function\nvar hello = function() { console.log('Hi!'); };",
    "example": {
        "code": "greet();\nfunction greet() {\n    console.log('Function Declaration Hoisted!');\n}",
        "output": "Function Declaration Hoisted!",
        "explanation": "The entire function declaration is available before its position in the code.",
    },
    "fill_blanks": {
        "question": "greet(); // Works\n_____ greet() {\n    console.log('Hello!');\n}\n\nvar hello = _____() {\n    console.log('Hi!');\n};",
        "answers": ["function", "function"],
        "options": ["function", "const", "var", "let"],
    },
    "compiler": {
        "title": "Function Hoisting Practice",
        "question": "Use function declaration syntax so the function can be invoked before its definition.",
        "starter_code": "sayHi();\n_____ sayHi() {\n    console.log('SkillExa Function Hoisting Success!');\n}",
        "options": ["function", "var", "const", "let"],
    },
    "skill_exa_test": [
        {
            "question": "Why can a function declaration be called before its definition in code?",
            "options": [
                "Because function declarations are hoisted with both name and body definition",
                "Because JavaScript compiles code backwards",
                "Because function calls are deferred until end of file",
                "Because functions do not use memory"
            ],
            "answer": "Because function declarations are hoisted with both name and body definition",
        },
        {
            "question": "What error is thrown when calling a var function expression before its assignment line?",
            "options": ["TypeError", "ReferenceError", "SyntaxError", "URIError"],
            "answer": "TypeError",
        },
        {
            "question": "How are function expressions treated during the hoisting phase?",
            "options": [
                "Like variable declarations (variable is hoisted, assignment remains at execution line)",
                "Full body is hoisted like function declarations",
                "They are ignored by compiler",
                "Converted into arrow functions automatically"
            ],
            "answer": "Like variable declarations (variable is hoisted, assignment remains at execution line)",
        },
        {
            "question": "What is logged by: var f = function() {}; console.log(typeof f);?",
            "options": ["function", "undefined", "object", "string"],
            "answer": "function",
        },
        {
            "question": "Which of the following function definitions is FULLY hoisted with body?",
            "options": [
                "function greet() {}",
                "var greet = function() {}",
                "const greet = () => {}",
                "let greet = function() {}"
            ],
            "answer": "function greet() {}",
        },
    ],
}

# Override Topic 32: Hoisting in Functions & Classes
JS_TOPICS[32] = {
    "id": 32,
    "title": "Hoisting in Functions & Classes",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "Variables declared with let and const inside a function are hoisted to top of function scope but remain in TDZ. Classes are also hoisted, but accessing or instantiating them before declaration results in a ReferenceError.",
    "theory": "1. Function Scope TDZ: Inside function scope, let and const declarations are hoisted to top of block/function context, preventing access before initialization line.\n2. Class Hoisting & TDZ: Classes in ES6 are hoisted to top of scope but remain uninitialized in TDZ until code execution reaches class declaration, throwing ReferenceError on early new ClassName() instantiation.",
    "syntax": "function test() {\n    console.log(x); // ReferenceError\n    let x = 50;\n}\n\nconst obj = new MyClass(); // ReferenceError\nclass MyClass {\n    constructor() { this.name = 'Mahima'; }\n}",
    "example": {
        "code": "try {\n    const obj = new MyClass();\n} catch (err) {\n    console.log(err.name);\n}\nclass MyClass {\n    constructor() {\n        this.name = 'Mahima';\n    }\n}",
        "output": "ReferenceError",
        "explanation": "Although class MyClass is hoisted, it cannot be accessed before declaration due to TDZ, throwing ReferenceError.",
    },
    "fill_blanks": {
        "question": "function test() {\n    // TDZ in function scope\n    _____ x = 50;\n}\n\n_____ MyClass {\n    constructor() {}\n}",
        "answers": ["let", "class"],
        "options": ["let", "class", "var", "function"],
    },
    "compiler": {
        "title": "Class Declaration Order",
        "question": "Instantiate the class using new keyword after the class declaration line.",
        "starter_code": "class Student {\n    constructor(name) {\n        this.name = name;\n    }\n}\nconst s = _____ Student('SkillExa');\nconsole.log(s.name);",
        "options": ["new", "create", "class", "call"],
    },
    "skill_exa_test": [
        {
            "question": "What happens if you instantiate a class using 'new' before its declaration?",
            "options": ["Throws ReferenceError", "Creates empty object", "Returns undefined", "Throws TypeError"],
            "answer": "Throws ReferenceError",
        },
        {
            "question": "Are JavaScript ES6 classes hoisted to the top of their scope?",
            "options": [
                "Yes, but they remain in TDZ and cannot be accessed before declaration",
                "No, class declarations are not hoisted at all",
                "Yes, fully initialized like function declarations",
                "Only if declared using var keyword"
            ],
            "answer": "Yes, but they remain in TDZ and cannot be accessed before declaration",
        },
        {
            "question": "What is the scope of let x = 50 declared inside function test()?",
            "options": [
                "Local function scope (hoisted within test() block in TDZ)",
                "Global scope",
                "Module scope",
                "Universal window scope"
            ],
            "answer": "Local function scope (hoisted within test() block in TDZ)",
        },
        {
            "question": "Why do classes throw ReferenceError when accessed early, unlike function declarations?",
            "options": [
                "Classes stay in Temporal Dead Zone until execution reaches declaration line",
                "Classes are primitive values",
                "Class constructors do not return memory addresses",
                "Classes only run in strict mode"
            ],
            "answer": "Classes stay in Temporal Dead Zone until execution reaches declaration line",
        },
        {
            "question": "Which keyword defines an ES6 class structure in JavaScript?",
            "options": ["class", "struct", "interface", "type"],
            "answer": "class",
        },
    ],
}

# Override Topic 33: Loop Hoisting & Closure Timing
JS_TOPICS[33] = {
    "id": 33,
    "title": "Loop Hoisting & Closure Timing",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "When using var in loops, the loop variable is hoisted to function or global scope and shared across iterations. Using let creates a new block-scoped variable binding per loop iteration, avoiding unexpected closure issues.",
    "theory": "1. var Hoisting in Loops: var i is hoisted outside loop body. Callbacks inside setTimeout reference the single shared i variable, which equals total iterations after loop finishes (e.g. 3, 3, 3).\n2. let Block Scope in Loops: let creates a fresh i variable in each loop step scope, allowing asynchronous closures to log individual iteration values (0, 1, 2).",
    "syntax": "for (var i = 0; i < 3; i++) {\n    setTimeout(function() {\n        console.log(i); // 3, 3, 3\n    }, 100);\n}\nfor (let j = 0; j < 3; j++) {\n    setTimeout(function() {\n        console.log(j); // 0, 1, 2\n    }, 100);\n}",
    "example": {
        "code": "for (var i = 0; i < 3; i++) {\n    setTimeout(function() {\n        console.log(i);\n    }, 10);\n}",
        "output": "3\n3\n3",
        "explanation": "var i is hoisted to function scope. All setTimeout callbacks share the same i reference, logging 3 three times.",
    },
    "fill_blanks": {
        "question": "// Prints 0, 1, 2\nfor (_____ i = 0; i < 3; i++) {\n    setTimeout(() => console.log(i), 10);\n}\n\n// Prints 3, 3, 3\nfor (_____ j = 0; j < 3; j++) {\n    setTimeout(() => console.log(j), 10);\n}",
        "answers": ["let", "var"],
        "options": ["let", "var", "const", "static"],
    },
    "compiler": {
        "title": "Fix Loop Variable Scope",
        "question": "Use block-scoped 'let' inside the loop header to print loop indexes individually.",
        "starter_code": "for (_____ k = 0; k < 2; k++) {\n    setTimeout(() => console.log('Index:', k), 10);\n}",
        "options": ["let", "var", "global", "static"],
    },
    "skill_exa_test": [
        {
            "question": "Why does for(var i=0; i<3; i++) { setTimeout(()=>console.log(i),100); } print 3, 3, 3?",
            "options": [
                "var i is hoisted to outer scope and shared by all setTimeout callbacks",
                "setTimeout runs synchronously before loop finishes",
                "JavaScript array indices start at 3",
                "The loop condition fails silently"
            ],
            "answer": "var i is hoisted to outer scope and shared by all setTimeout callbacks",
        },
        {
            "question": "How does 'let' fix the shared index problem in for loops with callbacks?",
            "options": [
                "let creates a separate block-scoped binding for each loop iteration",
                "let pauses the loop execution automatically",
                "let prevents hoisting entirely in V8 engine",
                "let converts asynchronous code to synchronous"
            ],
            "answer": "let creates a separate block-scoped binding for each loop iteration",
        },
        {
            "question": "What is the scope of variable declared with 'var' inside a standard for loop?",
            "options": ["Enclosing function or global scope", "Block scope inside loop body", "Module scope only", "Timer queue scope"],
            "answer": "Enclosing function or global scope",
        },
        {
            "question": "What will for (let i = 0; i < 3; i++) console.log(i); output?",
            "options": ["0, 1, 2", "3, 3, 3", "undefined", "ReferenceError"],
            "answer": "0, 1, 2",
        },
        {
            "question": "Which built-in function schedules code to execute asynchronously after a delay?",
            "options": ["setTimeout", "setInterval", "setImmediate", "requestAnimationFrame"],
            "answer": "setTimeout",
        },
    ],
}

# Override Topic 34: Function Parameters & Nested Hoisting
JS_TOPICS[34] = {
    "id": 34,
    "title": "Function Parameters & Nested Hoisting",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "Functions are hoisted with their parameter declarations, but parameter values are passed during invocation. Hoisting also operates within nested function scopes independently of outer scopes.",
    "theory": "1. Hoisted Functions with Parameters: Entire function definition including parameter list is hoisted. Invoking test(10) before function test(num) passes 10 cleanly.\n2. Hoisting in Nested Functions: Variables declared with var inside inner functions are hoisted to top of inner function scope, initialized to undefined.",
    "syntax": "test(10); // 10\nfunction test(num) {\n    console.log(num);\n}\n\nfunction outer() {\n    console.log(a); // undefined\n    var a = 5;\n    function inner() {\n        console.log(b); // undefined\n        var b = 10;\n    }\n    inner();\n}\nouter();",
    "example": {
        "code": "test(10);\nfunction test(num) {\n    console.log(num);\n}\nfunction outer() {\n    console.log(a);\n    var a = 5;\n}\nouter();",
        "output": "10\nundefined",
        "explanation": "test function is hoisted with parameter num. Inside outer(), var a is hoisted to top of outer function scope as undefined.",
    },
    "fill_blanks": {
        "question": "test(10); // 10\n_____ test(num) {\n    console.log(num);\n}\n\nfunction outer() {\n    console.log(a); // undefined\n    _____ a = 5;\n}",
        "answers": ["function", "var"],
        "options": ["function", "var", "let", "const"],
    },
    "compiler": {
        "title": "Nested Hoisting Challenge",
        "question": "Complete the inner function declaration inside outer function context.",
        "starter_code": "function outer() {\n    _____ inner() {\n        console.log('SkillExa Nested Hoisting Passed!');\n    }\n    inner();\n}\nouter();",
        "options": ["function", "var", "let", "const"],
    },
    "skill_exa_test": [
        {
            "question": "Are function parameters available when a hoisted function is called before its definition?",
            "options": [
                "Yes, arguments passed at call site are bound to parameters during execution",
                "No, parameters are lost during hoisting",
                "Only primitive values can be passed",
                "Parameters become undefined permanently"
            ],
            "answer": "Yes, arguments passed at call site are bound to parameters during execution",
        },
        {
            "question": "Where is a var variable declared inside a nested inner function hoisted to?",
            "options": [
                "Top of the inner function scope",
                "Top of the outer function scope",
                "Global scope",
                "Top of the script file"
            ],
            "answer": "Top of the inner function scope",
        },
        {
            "question": "What is logged by: function outer() { console.log(a); var a = 5; } outer();?",
            "options": ["undefined", "5", "ReferenceError", "null"],
            "answer": "undefined",
        },
        {
            "question": "Can an inner function access variables declared in outer function scope after hoisting?",
            "options": [
                "Yes, via lexical environment closure chain",
                "No, inner function scopes are isolated from outer variables",
                "Only if declared using var keyword",
                "Only inside arrow functions"
            ],
            "answer": "Yes, via lexical environment closure chain",
        },
        {
            "question": "What happens if a nested function shares the same variable name as an outer scope variable?",
            "options": [
                "Inner variable shadows outer variable within inner function scope",
                "Throws SyntaxError",
                "Outer variable overwrites inner variable",
                "Both variables merge into an array"
            ],
            "answer": "Inner variable shadows outer variable within inner function scope",
        },
    ],
}

# Override Topic 35: Function Binding
JS_TOPICS[35] = {
    "id": 35,
    "title": "Function Binding",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "Function binding in JavaScript associates a function with a specific execution context ('this' value). Methods like bind(), call(), and apply() explicitly set context, while arrow functions inherit 'this' lexically.",
    "theory": "1. Default & Lost 'this' Binding: Functions executed as standalone calls bind 'this' to the global object or undefined in strict mode. Extracting an object method (const greet = person.greet; greet()) loses its original object context.\n2. bind() Method: bind() returns a new bound function with permanently set 'this' context and optional pre-filled arguments (partial application).\n3. call() & apply() Methods: call() invokes the function immediately with comma-separated arguments. apply() invokes immediately with arguments passed as an array.\n4. Arrow Functions & Lexical 'this': Arrow functions do not have their own 'this' binding; they inherit 'this' lexically from their enclosing parent scope.",
    "syntax": "const boundFn = fn.bind(thisArg, arg1, arg2);\nfn.call(thisArg, arg1, arg2);\nfn.apply(thisArg, [arg1, arg2]);\nconst arrowGreet = () => console.log(this.name); // lexical this",
    "example": {
        "code": "const person = {\n    name: 'GFG',\n    greet: function(city) {\n        console.log('Hello, ' + this.name + ' from ' + city);\n    }\n};\nconst greet = person.greet;\nconst boundGreet = greet.bind(person, 'Delhi');\nboundGreet();\ngreet.call(person, 'Noida');\ngreet.apply(person, ['Mumbai']);",
        "output": "Hello, GFG from Delhi\nHello, GFG from Noida\nHello, GFG from Mumbai",
        "explanation": "bind() creates a new bound function with pre-filled argument 'Delhi'. call() and apply() execute immediately with custom 'this' context.",
    },
    "fill_blanks": {
        "question": "const person = { name: 'GFG' };\nfunction show(city) {\n    console.log(this.name, city);\n}\n\n// Permanent binding\nconst bound = show._____(person);\n// Immediate invocation with array\nshow._____(person, ['Delhi']);",
        "answers": ["bind", "apply"],
        "options": ["bind", "apply", "call", "connect"],
    },
    "compiler": {
        "title": "Function Binding Exercise",
        "question": "Use call() to invoke the greet function with context bound to person object.",
        "starter_code": "const person = { name: 'SkillExa' };\nfunction greet(tag) {\n    console.log(this.name + ' ' + tag);\n}\ngreet._____(person, 'Mastered!');",
        "options": ["call", "apply", "bind", "set"],
    },
    "skill_exa_test": [
        {
            "question": "What does the bind() method in JavaScript return when called on a function?",
            "options": [
                "A new function with permanently bound 'this' context",
                "The return value of the executed function",
                "An array of arguments",
                "Undefined"
            ],
            "answer": "A new function with permanently bound 'this' context",
        },
        {
            "question": "How do arguments differ between call() and apply()?",
            "options": [
                "call() takes arguments individually comma-separated, while apply() takes arguments as an array",
                "apply() takes arguments comma-separated, while call() takes an array",
                "call() binds 'this' permanently, while apply() is temporary",
                "There is no difference between call() and apply()"
            ],
            "answer": "call() takes arguments individually comma-separated, while apply() takes arguments as an array",
        },
        {
            "question": "How do arrow functions handle the 'this' keyword?",
            "options": [
                "Arrow functions do not have their own 'this'; they inherit 'this' lexically from surrounding scope",
                "Arrow functions bind 'this' to window object permanently",
                "Arrow functions require bind() to use 'this'",
                "Arrow functions create dynamic 'this' binding at runtime"
            ],
            "answer": "Arrow functions do not have their own 'this'; they inherit 'this' lexically from surrounding scope",
        },
        {
            "question": "What happens when calling an unbound extracted method like const f = obj.func; f(); in non-strict mode?",
            "options": [
                "'this' resolves to global object (or undefined in strict mode), losing obj context",
                "'this' automatically stays bound to obj",
                "Throws a SyntaxError immediately",
                "Returns a closure function automatically"
            ],
            "answer": "'this' resolves to global object (or undefined in strict mode), losing obj context",
        },
        {
            "question": "What feature of bind() allows pre-filling initial arguments for a function?",
            "options": ["Partial Application", "Currying", "Lexical Scoping", "Method Chaining"],
            "answer": "Partial Application",
        },
    ],
}

# Override Topic 36: Closures
JS_TOPICS[36] = {
    "id": 36,
    "title": "Closures",
    "category": "Functions",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "A closure is the combination of a function bundled together with references to its surrounding lexical environment. It allows an inner function to retain access to variables from its outer scope even after the outer function has finished executing.",
    "theory": "1. Lexical Scoping: Closures rely on lexical scoping, meaning a function's scope is determined by where it is defined in source code, not where it is invoked.\n2. Private Variables & Encapsulation: Closures enable data privacy by hiding variables within function scope, preventing direct external modification.\n3. Closures & IIFE: Immediately Invoked Function Expressions use closures to encapsulate module state without polluting global namespace.\n4. Closures & Async Operations: Retains variable state across delayed execution timers (setTimeout) and promises.\n5. Closures with 'this' Keyword: 'this' is determined dynamically at call time. Arrow functions or explicit .bind(this) preserve desired 'this' context inside closure callbacks.\n6. Pitfalls: Excessive closure creation can retain unneeded references causing memory leaks, performance overhead, or loop variable sharing when using var.",
    "syntax": "function outer() {\n    let outerVar = \"I'm in outer scope!\";\n    return function inner() {\n        console.log(outerVar);\n    };\n}\nconst closure = outer();\nclosure();",
    "example": {
        "code": "const counterModule = (function() {\n    let count = 0;\n    return {\n        increment: function() {\n            count++;\n            console.log(count);\n        },\n        reset: function() {\n            count = 0;\n            console.log('Counter reset');\n        }\n    };\n})();\ncounterModule.increment();\ncounterModule.increment();\ncounterModule.reset();",
        "output": "1\n2\nCounter reset",
        "explanation": "The IIFE creates a private count variable encapsulated within the closure returned object methods increment() and reset().",
    },
    "fill_blanks": {
        "question": "function counter() {\n    let count = 0;\n    return _____ () {\n        count++;\n        return count;\n    };\n}\nconst inc = counter();\nconsole.log(inc()); // 1",
        "answers": ["function"],
        "options": ["function", "closure", "let", "return"],
    },
    "compiler": {
        "title": "Closure Data Encapsulation",
        "question": "Complete the closure function to preserve outer secret variable.",
        "starter_code": "function createSecret(secret) {\n    return _____ () => 'Secret: ' + secret;\n}\nconst getSecret = createSecret('SkillExa123');\nconsole.log(getSecret());",
        "options": ["function", "return", "const", "def"],
    },
    "skill_exa_test": [
        {
            "question": "What is a closure in JavaScript?",
            "options": [
                "The combination of a function and its surrounding lexical environment",
                "A method to delete variables from memory",
                "An object constructor function",
                "A synchronous loop control structure"
            ],
            "answer": "The combination of a function and its surrounding lexical environment",
        },
        {
            "question": "How does lexical scoping affect closures?",
            "options": [
                "A function retains access to variables in the scope where it was defined",
                "A function scope changes based on where it is executed",
                "All functions share global variables dynamically",
                "Lexical scope disables private variables"
            ],
            "answer": "A function retains access to variables in the scope where it was defined",
        },
        {
            "question": "Why are closures useful for creating private variables?",
            "options": [
                "They prevent outer code from directly accessing or modifying variables inside the closure scope",
                "They automatically convert variables to constant primitive types",
                "They move variables to global window scope",
                "They eliminate the need for function return statements"
            ],
            "answer": "They prevent outer code from directly accessing or modifying variables inside the closure scope",
        },
        {
            "question": "How does an arrow function solve 'this' binding issues inside a closure callback like setTimeout?",
            "options": [
                "Arrow functions do not have their own 'this'; they inherit 'this' lexically from surrounding scope",
                "Arrow functions automatically execute bind(this) on the window object",
                "Arrow functions convert 'this' into a string key",
                "Arrow functions reset 'this' to undefined"
            ],
            "answer": "Arrow functions do not have their own 'this'; they inherit 'this' lexically from surrounding scope",
        },
        {
            "question": "What is a potential pitfall of overusing closures in JavaScript?",
            "options": [
                "Memory leaks due to retained references to unneeded outer scope variables",
                "SyntaxError during compilation phase",
                "Automatic conversion of strings into numbers",
                "Loss of default parameters"
            ],
            "answer": "Memory leaks due to retained references to unneeded outer scope variables",
        },
    ],
}

# Override Topic 37: Iterator
JS_TOPICS[37] = {
    "id": 37,
    "title": "Iterator",
    "category": "Functions",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "A JavaScript iterator is an object that enables sequential traversal over collections (arrays, strings, maps, sets) step-by-step. It implements the Iterator Protocol returning { value, done } objects from its next() method.",
    "theory": "1. Iterator Protocol & next() Method: Iterators produce values sequentially. Calling next() returns an object with 'value' (current element) and 'done' (boolean flag indicating completion).\n2. for...of Loop Integration: The for...of loop automatically obtains an iterator via Symbol.iterator and invokes next() until done is true.\n3. Custom Iterators: Any custom object can be made iterable by defining a method at [Symbol.iterator] that returns an object containing next().",
    "syntax": "const iterator = array[Symbol.iterator]();\nconsole.log(iterator.next()); // { value: 1, done: false }\n\n// Custom Iterator\nobj[Symbol.iterator] = function() {\n    let i = 0;\n    return {\n        next: () => i < this.items.length ? { value: this.items[i++], done: false } : { done: true }\n    };\n};",
    "example": {
        "code": "const myIterable = {\n    values: [10, 20, 30],\n    [Symbol.iterator]: function() {\n        let index = 0;\n        return {\n            next: () => {\n                if (index < this.values.length) {\n                    return { value: this.values[index++], done: false };\n                } else {\n                    return { done: true };\n                }\n            }\n        };\n    }\n};\nfor (const val of myIterable) {\n    console.log(val);\n}",
        "output": "10\n20\n30",
        "explanation": "Symbol.iterator defines a custom iterator that yields array elements step-by-step until index reaches length.",
    },
    "fill_blanks": {
        "question": "const numbers = [1, 2];\nconst iterator = numbers[Symbol._____]();\nconsole.log(iterator._____()); // { value: 1, done: false }",
        "answers": ["iterator", "next"],
        "options": ["iterator", "next", "value", "done"],
    },
    "compiler": {
        "title": "Iterator Protocol Practice",
        "question": "Retrieve an iterator from array using Symbol.iterator and call next().",
        "starter_code": "const arr = ['A', 'B'];\nconst it = arr[Symbol._____]();\nconsole.log(it._____().value);",
        "options": ["iterator", "next", "value", "done"],
    },
    "skill_exa_test": [
        {
            "question": "What structure does each call to next() on a JavaScript iterator return?",
            "options": [
                "An object containing { value, done }",
                "A primitive string",
                "An array of remaining values",
                "A promise resolving to null"
            ],
            "answer": "An object containing { value, done }",
        },
        {
            "question": "What is the value of 'done' when an iterator reaches the end of a collection?",
            "options": ["true", "false", "undefined", "null"],
            "answer": "true",
        },
        {
            "question": "Which built-in Symbol property makes an object iterable for for...of loops?",
            "options": ["Symbol.iterator", "Symbol.iterable", "Symbol.loop", "Symbol.asyncIterator"],
            "answer": "Symbol.iterator",
        },
        {
            "question": "What statement is true regarding the for...of loop in JavaScript?",
            "options": [
                "It automatically retrieves and calls next() on an object's Symbol.iterator until done is true",
                "It iterates over object property keys as strings",
                "It only works with numbers",
                "It requires manual index incrementing"
            ],
            "answer": "It automatically retrieves and calls next() on an object's Symbol.iterator until done is true",
        },
        {
            "question": "What value is returned in { value, done } after an iterator has passed the last element?",
            "options": ["undefined", "null", "0", "false"],
            "answer": "undefined",
        },
    ],
}


# Override Topic 38: Introduction to JavaScript Events & Event Handlers
JS_TOPICS[38] = {
    "id": 38,
    "title": "Introduction to JavaScript Events & Event Handlers",
    "category": "Events",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "JavaScript events are browser actions triggered by user interactions (clicks, keypresses, hovers) or system states. Handlers can be attached inline, via DOM properties, or using addEventListener().",
    "theory": "1. Event Categories: Browser events fall into categories including Mouse (click, mouseover), Keyboard (keydown, keyup), Form (submit, change, focus, blur), and Window (load, scroll).\n2. 3 Event Handling Methods:\n   a. Inline HTML Attributes: <button onclick=\"myFunc()\"> (Mixes HTML & JS; not recommended for complex apps).\n   b. DOM Property Handlers: elem.onclick = function() {} (Simple, but overwrites existing handlers).\n   c. addEventListener() (Preferred): elem.addEventListener('click', handler) (Allows multiple listeners, clean separation of concerns, and listener removal).",
    "syntax": "// Preferred addEventListener method\nelement.addEventListener('click', (event) => {\n    console.log('Event triggered:', event.type);\n});",
    "example": {
        "code": "const button = {\n    listeners: {},\n    addEventListener(type, fn) {\n        this.listeners[type] = fn;\n    },\n    click() {\n        if (this.listeners['click']) this.listeners['click']({ type: 'click' });\n    }\n};\nbutton.addEventListener('click', (e) => console.log('Button clicked using listener! Event:', e.type));\nbutton.click();",
        "output": "Button clicked using listener! Event: click",
        "explanation": "Demonstrates registering an event listener and triggering it when the user clicks.",
    },
    "fill_blanks": {
        "question": "const btn = document.getElementById('myBtn');\n// Preferred event handling method\nbtn.____('click', () => {\n    alert('Clicked!');\n});",
        "answers": ["addEventListener"],
        "options": ["addEventListener", "onclick", "setListener", "attachEvent"],
    },
    "compiler": {
        "title": "Event Listener Practice",
        "question": "Use addEventListener to attach a click handler to the element.",
        "starter_code": "const btn = {\n    addEventListener(evt, cb) { cb('Clicked!'); }\n};\nbtn.____('click', (msg) => console.log(msg));",
        "options": ["addEventListener", "onclick", "listen", "trigger"],
    },
    "skill_exa_test": [
        {
            "question": "What is a JavaScript Event?",
            "options": [
                "An action or occurrence in the browser triggered by user interaction or system state",
                "A function that compiles CSS",
                "A database query language",
                "A synchronous loop control structure"
            ],
            "answer": "An action or occurrence in the browser triggered by user interaction or system state",
        },
        {
            "question": "Which event handling method is recommended for modern web development?",
            "options": ["addEventListener()", "Inline HTML attributes", "document.write()", "eval()"],
            "answer": "addEventListener()",
        },
        {
            "question": "Why is addEventListener() preferred over DOM property handlers like element.onclick = fn?",
            "options": [
                "It allows attaching multiple event listeners to the same event type without overwriting existing ones",
                "It prevents all syntax errors in code",
                "It runs synchronously before DOM rendering",
                "It deletes HTML tags automatically"
            ],
            "answer": "It allows attaching multiple event listeners to the same event type without overwriting existing ones",
        },
        {
            "question": "Which of the following is classified as a Keyboard Event in JavaScript?",
            "options": ["keydown", "click", "submit", "onload"],
            "answer": "keydown",
        },
        {
            "question": "What parameter is automatically passed into an event listener callback function?",
            "options": [
                "An Event Object containing event details (type, target, coordinates)",
                "The window title string",
                "A boolean flag true",
                "An array of numbers"
            ],
            "answer": "An Event Object containing event details (type, target, coordinates)",
        },
    ],
}


# Override Topic 39: JavaScript addEventListener() & Window Event Listeners
JS_TOPICS[39] = {
    "id": 39,
    "title": "JavaScript addEventListener() & Window Event Listeners",
    "category": "Events",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "The addEventListener() method attaches an event handler to a DOM element or the global window object. It allows attaching multiple listeners to a single target and supports window events like resize, scroll, and keydown.",
    "theory": "1. Syntax & Parameters: element.addEventListener(event, function, useCapture). 'event' is the event string (e.g. 'click'), 'function' is the callback handler, and 'useCapture' (optional boolean) specifies bubbling vs capturing.\n2. Multiple Event Listeners: Multiple handlers can be attached to the same element for different event types (e.g. click, mouseenter, mouseleave) or the same event type without overwriting.\n3. Global Window Event Listeners: Listening on the global 'window' object captures window-level interactions such as window resizing ('resize'), page scrolling ('scroll'), and keyboard navigation ('keydown').\n4. Key Reasons to Use addEventListener(): Clean separation of concerns (keeping HTML clean), support for multiple listeners, propagation control, ability to unbind using removeEventListener(), and access to full Event objects.",
    "syntax": "element.addEventListener('click', (event) => {\n    console.log('Clicked!', event);\n});\nwindow.addEventListener('resize', () => {\n    console.log('Width:', window.innerWidth);\n});",
    "example": {
        "code": "const mockElement = {\n    listeners: {},\n    addEventListener(type, cb) {\n        if (!this.listeners[type]) this.listeners[type] = [];\n        this.listeners[type].push(cb);\n    },\n    trigger(type, eventData) {\n        (this.listeners[type] || []).forEach(cb => cb(eventData));\n    }\n};\nmockElement.addEventListener('click', () => console.log('Listener 1: Background changed to lightblue'));\nmockElement.addEventListener('click', () => console.log('Listener 2: Message updated -> Button was clicked!'));\nmockElement.trigger('click');",
        "output": "Listener 1: Background changed to lightblue\nListener 2: Message updated -> Button was clicked!",
        "explanation": "Demonstrates attaching multiple event listeners to the exact same element for a single click event.",
    },
    "fill_blanks": {
        "question": "// Syntax: element.addEventListener(event, function, useCapture)\nconst btn = document.getElementById('myButton');\n// Attach multiple listeners\nbtn.____('click', function() {\n    btn.style.backgroundColor = 'lightblue';\n});\nwindow.____('resize', function() {\n    console.log(window.innerWidth);\n});",
        "answers": ["addEventListener", "addEventListener"],
        "options": ["addEventListener", "removeEventListener", "onclick", "onresize"],
    },
    "compiler": {
        "title": "addEventListener Practice",
        "question": "Use addEventListener to attach a keydown listener to window.",
        "starter_code": "const mockWindow = { addEventListener(evt, cb) { cb({ key: 'Enter' }); } };\nmockWindow.____('keydown', (e) => console.log('Window captured key:', e.key));",
        "options": ["addEventListener", "onkeydown", "listen", "setEvent"],
    },
    "skill_exa_test": [
        {
            "question": "What is the correct syntax signature for addEventListener()?",
            "options": [
                "element.addEventListener(event, function, useCapture)",
                "element.addEventListener(function, event)",
                "element.addEvent(event, callback)",
                "element.listen(eventType, function)"
            ],
            "answer": "element.addEventListener(event, function, useCapture)",
        },
        {
            "question": "What happens when you attach multiple event listeners of the same type to an element using addEventListener()?",
            "options": [
                "All attached listener callbacks execute sequentially when the event occurs",
                "The second listener overwrites the first listener",
                "Throws a TypeError at runtime",
                "Only the last registered listener executes"
            ],
            "answer": "All attached listener callbacks execute sequentially when the event occurs",
        },
        {
            "question": "Which global browser object is used to listen for window resizing (resize) or scrolling (scroll) events?",
            "options": ["window", "document", "navigator", "console"],
            "answer": "window",
        },
        {
            "question": "Which complementary method is used to remove an event listener previously attached with addEventListener()?",
            "options": ["removeEventListener()", "deleteEventListener()", "detachEvent()", "clearListener()"],
            "answer": "removeEventListener()",
        },
        {
            "question": "What is a primary advantage of addEventListener() over inline HTML event attributes (e.g. onclick=\"...\")?",
            "options": [
                "Keeps JavaScript code separate from HTML structure and supports multiple event listeners per element",
                "Executes code before DOM nodes are created",
                "Eliminates the need for CSS stylesheets",
                "Automatically validates form inputs"
            ],
            "answer": "Keeps JavaScript code separate from HTML structure and supports multiple event listeners per element",
        },
    ],
}

# Override Topic 40: Mouse Events (onclick, onmouseover & onmouseout)
JS_TOPICS[40] = {
    "id": 40,
    "title": "Mouse Events (onclick, onmouseover & onmouseout)",
    "category": "Events",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "Mouse events respond to user pointer actions. onclick fires when an element is clicked. onmouseover fires when entering an element boundary, and onmouseout fires when leaving.",
    "theory": "1. Click Event (onclick): Fires when a pointing device button is pressed and released on an element.\n2. Mouse Hover Enter (onmouseover): Triggers when the cursor pointer moves onto an element or one of its child elements, useful for hover effects, tooltips, or dynamic styling.\n3. Mouse Hover Exit (onmouseout): Triggers when the cursor pointer leaves an element's area, useful for resetting hover styles or hiding dropdown menus.",
    "syntax": "elem.onclick = () => console.log('Clicked');\nelem.onmouseover = () => console.log('Mouse entered');\nelem.onmouseout = () => console.log('Mouse left');",
    "example": {
        "code": "function handleHover(state) {\n    if (state === 'over') {\n        console.log('Hover Active: Background -> Cyan, Text -> Red');\n    } else if (state === 'out') {\n        console.log('Hover Reset: Background -> Black, Text -> Yellow');\n    }\n}\nhandleHover('over');\nhandleHover('out');",
        "output": "Hover Active: Background -> Cyan, Text -> Red\nHover Reset: Background -> Black, Text -> Yellow",
        "explanation": "Shows dynamic style state transitions triggered during onmouseover and onmouseout events.",
    },
    "fill_blanks": {
        "question": "const card = document.getElementById('card');\n// Mouse enters card\ncard._____ = () => console.log('Entered');\n// Mouse leaves card\ncard._____ = () => console.log('Left');",
        "answers": ["onmouseover", "onmouseout"],
        "options": ["onmouseover", "onmouseout", "onclick", "onkeydown"],
    },
    "compiler": {
        "title": "Mouse Hover Handler",
        "question": "Attach an onmouseover handler to trigger when the pointer enters the element.",
        "starter_code": "const box = {};\nbox._____ = () => console.log('Mouse Over Success!');\nbox.onmouseover();",
        "options": ["onmouseover", "onmouseout", "onclick", "onblur"],
    },
    "skill_exa_test": [
        {
            "question": "When does the onclick event trigger in JavaScript?",
            "options": [
                "When a user clicks on an element",
                "When the mouse pointer enters an element",
                "When a key is released",
                "When a form is reset"
            ],
            "answer": "When a user clicks on an element",
        },
        {
            "question": "What is the difference between onmouseover and onmouseout?",
            "options": [
                "onmouseover fires when pointer enters an element, while onmouseout fires when pointer leaves",
                "onmouseover fires on mouse click, while onmouseout fires on key release",
                "onmouseover is for touchscreen devices only",
                "There is no difference between them"
            ],
            "answer": "onmouseover fires when pointer enters an element, while onmouseout fires when pointer leaves",
        },
        {
            "question": "Which HTML elements DO NOT support onmouseover and onmouseout attributes?",
            "options": [
                "Non-visual metadata elements like <head>, <meta>, <title>, and <br>",
                "Buttons and div tags",
                "Images and paragraphs",
                "Form input fields"
            ],
            "answer": "Non-visual metadata elements like <head>, <meta>, <title>, and <br>",
        },
        {
            "question": "How can onmouseover improve User Experience (UX) on a webpage?",
            "options": [
                "By providing interactive feedback, tooltips, or highlight effects when hovering over items",
                "By speeding up server response times",
                "By saving form inputs to database automatically",
                "By disabling keypress events"
            ],
            "answer": "By providing interactive feedback, tooltips, or highlight effects when hovering over items",
        },
        {
            "question": "What DOM property accesses the target element clicked during an onclick event?",
            "options": ["event.target", "event.type", "event.key", "event.code"],
            "answer": "event.target",
        },
    ],
}

# Override Topic 41: Keyboard Events (onkeydown & onkeyup)
JS_TOPICS[41] = {
    "id": 41,
    "title": "Keyboard Events (onkeydown & onkeyup)",
    "category": "Events",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "Keyboard events capture user key actions on input fields or document context. onkeydown occurs when a key is pressed down, and onkeyup occurs when the key is released.",
    "theory": "1. Key Event Execution Sequence: When a user presses a key, events fire in sequence: 1) onkeydown -> 2) onkeypress -> 3) onkeyup.\n2. onkeydown Event: Fires immediately when any key is pushed down. Useful for capturing modifier keys (Ctrl, Shift, Alt), arrow navigation, or game controls.\n3. onkeyup Event: Fires when the pressed key is released. Ideal for real-time text input processing, character counting, or instant input validation.",
    "syntax": "input.addEventListener('keydown', (e) => console.log('Key down:', e.key));\ninput.addEventListener('keyup', (e) => console.log('Key released:', e.key));",
    "example": {
        "code": "function simulateKeyPress(key) {\n    console.log('1. Keydown:', key);\n    console.log('2. Keyup:', key);\n    console.log('Processed text input value:', key.toUpperCase());\n}\nsimulateKeyPress('a');",
        "output": "1. Keydown: a\n2. Keyup: a\nProcessed text input value: A",
        "explanation": "Illustrates keydown and keyup execution order during user keyboard input.",
    },
    "fill_blanks": {
        "question": "const input = document.getElementById('myInput');\n// Key pressed down\ninput.addEventListener('_____', (e) => console.log('Pressed:', e.key));\n// Key released\ninput.addEventListener('_____', (e) => console.log('Released:', e.key));",
        "answers": ["keydown", "keyup"],
        "options": ["keydown", "keyup", "change", "focus"],
    },
    "compiler": {
        "title": "Keyup Event Listener",
        "question": "Attach a keyup event listener to process keyboard input.",
        "starter_code": "const input = { addEventListener(evt, cb) { cb({ key: 'Enter' }); } };\ninput.____('keyup', (e) => console.log('Keyup registered:', e.key));",
        "options": ["addEventListener", "onkeyup", "onkeydown", "listen"],
    },
    "skill_exa_test": [
        {
            "question": "What is the correct chronological sequence of keyboard events when a key is pressed and released?",
            "options": [
                "onkeydown -> onkeypress -> onkeyup",
                "onkeyup -> onkeydown -> onkeypress",
                "onkeypress -> onkeyup -> onkeydown",
                "onkeydown -> onkeyup -> onkeypress"
            ],
            "answer": "onkeydown -> onkeypress -> onkeyup",
        },
        {
            "question": "What does the onkeyup event indicate?",
            "options": [
                "The user released a key after pressing it",
                "The user pushed down a key",
                "The mouse moved upward",
                "A form was submitted"
            ],
            "answer": "The user released a key after pressing it",
        },
        {
            "question": "Which property of the keyboard Event object yields the character representation of the key pressed (e.g. 'a', 'Enter')?",
            "options": ["event.key", "event.code", "event.which", "event.type"],
            "answer": "event.key",
        },
        {
            "question": "Why is onkeydown often used over onkeyup for game controls or navigation shortcuts?",
            "options": [
                "Because onkeydown responds immediately as soon as the key is pressed down",
                "Because onkeydown does not work with arrow keys",
                "Because onkeyup runs asynchronously after 5 seconds",
                "Because onkeydown cancels all mouse events"
            ],
            "answer": "Because onkeydown responds immediately as soon as the key is pressed down",
        },
        {
            "question": "Can keyboard events be attached to global document or window objects?",
            "options": [
                "Yes, allowing keyboard shortcuts to be captured anywhere on the page",
                "No, keyboard events only work inside <textarea>",
                "Only inside <button> tags",
                "Only inside forms"
            ],
            "answer": "Yes, allowing keyboard shortcuts to be captured anywhere on the page",
        },
    ],
}

# Override Topic 42: Form & Focus Events (onchange, onsubmit, onfocus & onblur)
JS_TOPICS[42] = {
    "id": 42,
    "title": "Form & Focus Events (onchange, onsubmit, onfocus & onblur)",
    "category": "Events",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "Form events manage user input and submission. onchange fires when input value changes and loses focus. onsubmit fires on form submit. onfocus and onblur handle focus gain/loss.",
    "theory": "1. onchange Event: Triggers when the value of a form element (<select>, <input type='checkbox'>, <input type='text'>) changes and loses focus.\n2. onsubmit Event: Triggers when a <form> is submitted via a submit button or Enter key press. Crucial for client-side input validation.\n3. Focus Events (onfocus vs onblur):\n   - onfocus: Triggers when an element receives cursor/keyboard focus (e.g. highlighting input field).\n   - onblur: Triggers when an element loses focus (opposite of onfocus; ideal for inline field validation or auto-formatting text like uppercase).",
    "syntax": "form.onsubmit = (e) => { e.preventDefault(); console.log('Submitted'); };\ninput.onfocus = () => input.style.background = 'yellow';\ninput.onblur = () => input.style.background = 'white';",
    "example": {
        "code": "const formState = { name: '', selectedSubject: '' };\nfunction handleSubjectChange(value) {\n    formState.selectedSubject = value;\n    console.log('onchange Selected Subject:', formState.selectedSubject);\n}\nfunction handleBlur(inputVal) {\n    formState.name = inputVal.toUpperCase();\n    console.log('onblur Formatted Username:', formState.name);\n}\nhandleSubjectChange('Data Structures');\nhandleBlur('alex');",
        "output": "onchange Selected Subject: Data Structures\nonblur Formatted Username: ALEX",
        "explanation": "Shows onchange updating dropdown selection and onblur auto-converting input text to uppercase upon blur.",
    },
    "fill_blanks": {
        "question": "const input = document.getElementById('nameInput');\n// Highlighting on focus gain\ninput._____ = () => input.style.borderColor = 'blue';\n// Formatting on focus loss\ninput._____ = () => input.value = input.value.toUpperCase();",
        "answers": ["onfocus", "onblur"],
        "options": ["onfocus", "onblur", "onchange", "onsubmit"],
    },
    "compiler": {
        "title": "Form Submit Event Practice",
        "question": "Attach onsubmit handler to validate form inputs.",
        "starter_code": "const form = {};\nform._____ = (e) => console.log('Form submission intercepted successfully!');\nform.onsubmit();",
        "options": ["onsubmit", "onchange", "onblur", "onfocus"],
    },
    "skill_exa_test": [
        {
            "question": "What is the difference between onchange and oninput events?",
            "options": [
                "oninput fires immediately on every keystroke, whereas onchange fires after the value changes AND the element loses focus",
                "onchange works only on images",
                "oninput is used only for form submission",
                "There is no difference between them"
            ],
            "answer": "oninput fires immediately on every keystroke, whereas onchange fires after the value changes AND the element loses focus",
        },
        {
            "question": "When does the onblur event fire?",
            "options": [
                "When an element loses focus",
                "When an element gains focus",
                "When a form is submitted",
                "When mouse hovers over element"
            ],
            "answer": "When an element loses focus",
        },
        {
            "question": "Which HTML tag supports the onsubmit event?",
            "options": ["<form>", "<div>", "<span>", "<button>"],
            "answer": "<form>",
        },
        {
            "question": "Why is onblur widely used in form field validation?",
            "options": [
                "It allows validating user input right after the user finishes typing and leaves the field",
                "It prevents the user from typing numbers",
                "It automatically clears form inputs",
                "It converts all inputs into arrays"
            ],
            "answer": "It allows validating user input right after the user finishes typing and leaves the field",
        },
        {
            "question": "Which event is the exact opposite of onblur?",
            "options": ["onfocus", "onchange", "onclick", "onkeydown"],
            "answer": "onfocus",
        },
    ],
}

# Override Topic 43: Window Load Events (onload) & preventDefault()
JS_TOPICS[43] = {
    "id": 43,
    "title": "Prevent the Default Action of an Event in JavaScript",
    "category": "Events",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "The preventDefault() method is used to stop the browser from performing its default action when an event occurs, allowing developers to implement custom behavior instead of the browser's built-in response.",
    "theory": "Preventing the Default Action of an Event in JavaScript:\n\nThe preventDefault() method stops the default behavior of an event (such as navigating to a new URL on link clicks or refreshing the page on form submission).\n\nKey Concepts & Properties:\n1. Standard Event Method: Prevents standard browser actions using event.preventDefault().\n2. Scope of Application: Commonly used with form submissions, link navigation, context menus, and keyboard shortcuts.\n3. Propagation Independence: calling preventDefault() does NOT stop event propagation (bubbling/capturing). Use stopPropagation() if you also want to halt propagation.\n\nTwo Implementation Approaches:\n\n1. Using 'return false' (Inline / Classic Event Handlers):\nReturning false from an inline event handler attribute or event property can prevent the default action.\nExample:\n<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <title>Prevent Default</title>\n</head>\n<body>\n    <a href=\"https://www.example.com/\" onclick=\"return handleClick()\">Click me</a>\n    <script>\n    function handleClick() {\n        alert(\"Event handled, but default action prevented\");\n        return false; // Prevents default link navigation\n    }\n    </script>\n</body>\n</html>\nOutput Note: handleClick() displays an alert and returns false, preventing browser navigation to https://www.example.com/.\n\n2. Using event.preventDefault() (Standard & Recommended):\nThe preventDefault() method is called directly on the Event object inside an event handler. It is modern, reliable, and widely supported across all modern browsers.\nExample:\n<a href=\"https://www.example.com/\" id=\"myLink\">Click me</a>\n<script>\nfunction handleClick(event) {\n    alert(\"Event handled, but default action prevented\");\n    event.preventDefault(); // Standard prevent default method\n}\ndocument.getElementById(\"myLink\").addEventListener(\"click\", handleClick);\n</script>",
    "syntax": "// Standard Event Method\nelement.addEventListener('click', function(event) {\n    event.preventDefault();\n});\n\n// Inline Return Statement Approach\nfunction handleClick() {\n    return false;\n}",
    "example": {
        "code": "function handleClick(event) {\n    console.log(\"Event handled, but default action prevented\");\n    event.preventDefault(); // Prevents standard browser link navigation or form submit\n}\n\nconst mockEvent = {\n    defaultPrevented: false,\n    preventDefault() {\n        this.defaultPrevented = true;\n        console.log(\"Browser default behavior cancelled successfully.\");\n    }\n};\n\nhandleClick(mockEvent);\nconsole.log(\"Is default prevented?\", mockEvent.defaultPrevented);",
        "output": "Event handled, but default action prevented\nBrowser default behavior cancelled successfully.\nIs default prevented? true",
        "explanation": "Calling event.preventDefault() sets the event's defaultPrevented flag to true and cancels default browser handling.",
    },
    "fill_blanks": {
        "question": "// Prevent standard browser form submission and page reload\nfunction handleSubmit(event) {\n    alert('Handling submit via JavaScript');\n    event._____();\n}",
        "answers": ["preventDefault"],
        "options": ["preventDefault", "stopPropagation", "cancelBubble", "returnValue"],
    },
    "compiler": {
        "title": "Prevent Default Action Sandbox",
        "question": "Call the standard method on the event object to cancel the browser's default link navigation.",
        "starter_code": "function handleClick(event) {\n    console.log('Link clicked - custom handler running');\n    event._____();\n}\n\nconst evt = { preventDefault() { console.log('Default link navigation prevented!'); } };\nhandleClick(evt);",
        "options": ["preventDefault", "stopPropagation", "cancel", "stop"],
    },
    "skill_exa_test": [
        {
            "question": "What is the primary function of the preventDefault() method in JavaScript?",
            "options": [
                "It stops the browser from executing its default built-in response for an event",
                "It stops the event from propagating up the DOM tree to parent elements",
                "It reloads the page with refreshed event parameters",
                "It detaches all event listeners from the target element"
            ],
            "answer": "It stops the browser from executing its default built-in response for an event",
        },
        {
            "question": "Does calling event.preventDefault() stop event propagation (bubbling/capturing)?",
            "options": [
                "No, preventDefault() does not stop propagation; use stopPropagation() if needed",
                "Yes, preventDefault() automatically stops bubbling and capturing",
                "Yes, but only for keyboard events",
                "No, preventDefault() is deprecated in modern browsers"
            ],
            "answer": "No, preventDefault() does not stop propagation; use stopPropagation() if needed",
        },
        {
            "question": "Which of the following events commonly use event.preventDefault()?",
            "options": [
                "Form submissions, link clicks (<a> tags), and context menu/keyboard events",
                "Window resize and scroll events only",
                "CSS transition and animation events only",
                "DOM node deletion events only"
            ],
            "answer": "Form submissions, link clicks (<a> tags), and context menu/keyboard events",
        },
        {
            "question": "How can you prevent the default action using an inline HTML handler attribute like onclick=\"...\"?",
            "options": [
                "By returning false from the inline event handler function (e.g. onclick=\"return handleClick()\")",
                "By returning true from the handler function",
                "By passing null as the event parameter",
                "Inline handlers cannot prevent default actions"
            ],
            "answer": "By returning false from the inline event handler function (e.g. onclick=\"return handleClick()\")",
        },
        {
            "question": "Which property on the Event object indicates whether preventDefault() has been called on the event?",
            "options": [
                "event.defaultPrevented",
                "event.isCancelled",
                "event.preventDefaultActive",
                "event.stopped"
            ],
            "answer": "event.defaultPrevented",
        },
    ],
}

# Override Topic 44: Event Propagation & Event Delegation
JS_TOPICS[44] = {
    "id": 44,
    "title": "Event Propagation (Bubbling & Capturing)",
    "category": "Events",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "Event Propagation defines the order in which event handlers trigger across DOM hierarchy (Bubbling vs Capturing). Event Bubbling flows bottom-up from target to root (default), while Event Capturing flows top-down from root to target (useCapture: true).",
    "theory": "1. Event Propagation Order: When an event occurs on a DOM element, it travels in 3 phases: 1) Capturing Phase (outermost parent down to target), 2) Target Phase (at the target element), and 3) Bubbling Phase (target up to root).\\n2. Event Bubbling (Default): Events start at the innermost target element (e.g. Component 3) and propagate upward to outer parents (Component 2 -> Component 1).\\n3. Event Capturing (Trickle-down): Events start at the outermost parent (Component 1) and propagate inward down to target (Component 3). Activated by passing true as the 3rd argument to addEventListener(type, handler, true).\\n4. Stopping Propagation: event.stopPropagation() prevents further propagation along the DOM tree.\\n5. Event Delegation: Technique of placing a single event listener on a parent container to handle events for multiple child elements dynamically using event.target.",
    "syntax": "// Event Bubbling (Default)\nelem.addEventListener('click', handler, false);\n\n// Event Capturing\nelem.addEventListener('click', handler, true);\n\n// Stop Propagation\nevent.stopPropagation();",
    "example": {
        "code": "function simulatePropagation(mode) {\n    console.log('--- Propagation Mode:', mode, '---');\n    const chain = ['Component 1 (Outer)', 'Component 2 (Middle)', 'Component 3 (Inner Target)'];\n    if (mode === 'capturing') {\n        chain.forEach(comp => console.log('Captured:', comp));\n    } else {\n        chain.reverse().forEach(comp => console.log('Bubbled:', comp));\n    }\n}\nsimulatePropagation('bubbling');\nsimulatePropagation('capturing');",
        "output": "--- Propagation Mode: bubbling ---\nBubbled: Component 3 (Inner Target)\nBubbled: Component 2 (Middle)\nBubbled: Component 1 (Outer)\n--- Propagation Mode: capturing ---\nCaptured: Component 1 (Outer)\nCaptured: Component 2 (Middle)\nCaptured: Component 3 (Inner Target)",
        "explanation": "Shows bottom-up event execution order during Bubbling vs top-down execution order during Capturing.",
    },
    "fill_blanks": {
        "question": "// Enable Event Capturing (top-down)\ndiv1.addEventListener('click', handler, ____);\n// Stop event propagation upward\nevent.____();",
        "answers": ["true", "stopPropagation"],
        "options": ["true", "stopPropagation", "false", "preventDefault"],
    },
    "compiler": {
        "title": "Event Propagation Control",
        "question": "Use stopPropagation() to prevent event bubbling to parent containers.",
        "starter_code": "const evt = { stopPropagation() { console.log('Event Propagation Stopped Successfully!'); } };\nfunction handleChildClick(e) {\n    e._____();\n}\nhandleChildClick(evt);",
        "options": ["stopPropagation", "preventDefault", "stop", "cancel"],
    },
    "skill_exa_test": [
        {
            "question": "What is Event Bubbling in JavaScript DOM?",
            "options": [
                "The default event propagation mechanism where an event triggers first on the target element and then propagates upward through ancestor elements",
                "When an event triggers only on the window object",
                "When events repeat infinitely in a loop",
                "When events are deleted automatically"
            ],
            "answer": "The default event propagation mechanism where an event triggers first on the target element and then propagates upward through ancestor elements",
        },
        {
            "question": "How do you enable Event Capturing (trickle-down propagation) in addEventListener()?",
            "options": [
                "Pass true as the third argument (useCapture parameter): addEventListener('click', handler, true)",
                "Pass false as the first argument",
                "Call element.capture() before binding",
                "Set event.capturing = true"
            ],
            "answer": "Pass true as the third argument (useCapture parameter): addEventListener('click', handler, true)",
        },
        {
            "question": "In what direction does Event Capturing propagate handlers across nested DOM elements?",
            "options": [
                "From the outermost parent element down to the innermost target element",
                "From the innermost target element up to the outermost parent",
                "Randomly across siblings",
                "Only horizontally between inputs"
            ],
            "answer": "From the outermost parent element down to the innermost target element",
        },
        {
            "question": "Which Event method prevents an event from continuing to bubble up or capture down the DOM tree?",
            "options": ["event.stopPropagation()", "event.preventDefault()", "event.stopImmediate()", "event.cancel()"],
            "answer": "event.stopPropagation()",
        },
        {
            "question": "What is the main benefit of Event Delegation?",
            "options": [
                "Attaching a single event listener to a parent container to handle events for current and future child elements efficiently",
                "Stopping all browser network requests",
                "Converting HTML elements into React components",
                "Accelerating CSS animations"
            ],
            "answer": "Attaching a single event listener to a parent container to handle events for current and future child elements efficiently",
        },
    ],
}


# Override Topic 45: Event Loop in JavaScript
JS_TOPICS[45] = {
    "id": 45,
    "title": "Event Loop in JavaScript",
    "category": "Events",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "The Event Loop is the mechanism in JavaScript that enables non-blocking asynchronous programming on a single thread by continuously coordinating the Call Stack, Web APIs, Microtask Queue, and Callback (Macrotask) Queue.",
    "theory": "Event Loop in JavaScript:\n\nJavaScript executes code synchronously in a single thread on the Call Stack. However, it handles asynchronous operations (API fetches, user events, timers) without pausing execution using the Event Loop.\n\nCore Components of the Event Loop Architecture:\n1. Call Stack: Last-In, First-Out (LIFO) stack where function execution frames are managed.\n2. Web APIs / Background Tasks: Browser or Node.js runtime APIs (setTimeout, setInterval, fetch, DOM events) that handle non-blocking asynchronous operations.\n3. Callback Queue (Task / Macrotask Queue): Holds callbacks ready for execution once asynchronous operations complete.\n4. Microtask Queue: Holds high-priority callbacks from Promises (.then(), .catch(), .finally()) and process.nextTick / MutationObserver. Microtasks are ALWAYS fully executed and drained before moving to the next macrotask.\n5. Event Loop: Continuously checks if the Call Stack is empty. When empty, it first processes all microtasks, then moves macrotasks from the Callback Queue to the Call Stack.\n\nCommon Event Loop Issues & Best Practices:\n- Blocking the Main Thread: Heavy synchronous operations (e.g. an infinite while(true) loop) block the Call Stack, preventing the Event Loop from processing UI updates or timer callbacks.\n- Delayed Execution of setTimeout: setTimeout guarantees a minimum delay, but a busy Call Stack will delay callback execution.\n- Microtask Priority: Microtasks always take precedence over macrotasks (even setTimeout with 0ms delay).\n- Avoiding Callback Hell: Use Promises or async/await instead of deeply nested callbacks.\n- Optimization: Offload CPU-intensive calculations to worker threads.",
    "syntax": "// Demonstration of Synchronous vs Microtask vs Macrotask Execution Order\nconsole.log(\"Start\");\n\nsetTimeout(() => {\n    console.log(\"setTimeout Callback (Macrotask Queue)\");\n}, 0);\n\nPromise.resolve().then(() => {\n    console.log(\"Promise Resolved (Microtask Queue)\");\n});\n\nconsole.log(\"End\");",
    "example": {
        "code": "console.log('Start');\n\nsetTimeout(() => {\n    console.log('setTimeout Callback');\n}, 0);\n\nPromise.resolve().then(() => {\n    console.log('Promise Resolved');\n});\n\nconsole.log('End');",
        "output": "Start\nEnd\nPromise Resolved\nsetTimeout Callback",
        "explanation": "Synchronous code executes first ('Start', 'End'). Then the Event Loop drains the Microtask Queue ('Promise Resolved') before executing the Callback/Macrotask Queue ('setTimeout Callback').",
    },
    "fill_blanks": {
        "question": "// The Event Loop processes the _____ Queue before the Callback (Macrotask) Queue.\nPromise.resolve().then(() => console.log('Promise'));\nsetTimeout(() => console.log('Timeout'), 0);",
        "answers": ["Microtask"],
        "options": ["Microtask", "Callback", "CallStack", "WebAPI"],
    },
    "compiler": {
        "title": "Event Loop Sandbox",
        "question": "Predict and complete the log statement to demonstrate Microtask queue priority.",
        "starter_code": "console.log('Start');\nsetTimeout(() => console.log('Macrotask'), 0);\nPromise.resolve().then(() => console.log('Microtask'));\nconsole.log('End');",
        "options": ["Start, End, Microtask, Macrotask", "Start, Macrotask, Microtask, End", "Microtask, Macrotask, Start, End", "Start, End, Macrotask, Microtask"],
    },
    "skill_exa_test": [
        {
            "question": "What is the primary role of the Event Loop in JavaScript?",
            "options": [
                "To continuously check if the Call Stack is empty and move queued callbacks (Microtasks/Macrotasks) onto the stack for execution",
                "To compile JavaScript code into native machine code binary",
                "To convert single-threaded execution into multi-threaded OS threads for every function",
                "To optimize CSS animations in the browser"
            ],
            "answer": "To continuously check if the Call Stack is empty and move queued callbacks (Microtasks/Macrotasks) onto the stack for execution",
        },
        {
            "question": "How does the Event Loop handle execution priority between the Microtask Queue (Promises) and the Callback Queue (setTimeout macrotasks)?",
            "options": [
                "The Microtask Queue has higher priority and is completely drained before processing tasks from the Callback Queue",
                "The Callback Queue has higher priority than the Microtask Queue",
                "Tasks are picked randomly regardless of queue type",
                "Microtasks and Macrotasks are executed in parallel on separate CPU cores"
            ],
            "answer": "The Microtask Queue has higher priority and is completely drained before processing tasks from the Callback Queue",
        },
        {
            "question": "Given the code: console.log('A'); setTimeout(() => console.log('B'), 0); Promise.resolve().then(() => console.log('C')); console.log('D'); - What is the output order?",
            "options": [
                "A, D, C, B",
                "A, B, C, D",
                "A, D, B, C",
                "C, B, A, D"
            ],
            "answer": "A, D, C, B",
        },
        {
            "question": "What happens when an infinite synchronous loop (e.g. while(true) {}) runs on the main thread in JavaScript?",
            "options": [
                "It occupies the Call Stack indefinitely, blocking the Event Loop and freezing UI renders and timer callbacks",
                "The Event Loop automatically spawns a background thread to bypass the loop",
                "Promises inside the Microtask Queue interrupt the while loop automatically",
                "The browser converts the while loop into a setTimeout call"
            ],
            "answer": "It occupies the Call Stack indefinitely, blocking the Event Loop and freezing UI renders and timer callbacks",
        },
        {
            "question": "Why might setTimeout(callback, 1000) take LONGER than 1000 milliseconds to execute its callback?",
            "options": [
                "Because if a long-running synchronous computation keeps the Call Stack busy, the callback must wait until the Call Stack clears",
                "Because setTimeout time is measured in seconds rather than milliseconds",
                "Because Promises cancel setTimeout timers automatically",
                "Because Web APIs pause timers whenever network requests are active"
            ],
            "answer": "Because if a long-running synchronous computation keeps the Call Stack busy, the callback must wait until the Call Stack clears",
        },
    ],
}

# Override Topic 55: JavaScript Numbers (Split into Chapter 1 & Chapter 2)
JS_TOPICS[55] = {
    "id": 55,
    "title": "JavaScript Numbers",
    "category": "JavaScript Data Structures",
    "difficulty": "Beginner",
    "duration": "25 min",
    "concept": "JavaScript numbers are primitive data types stored in IEEE 754 64-bit double-precision binary format. This topic is split into two core chapters: Chapter 1 covers numeric representation, literals, and precision; Chapter 2 covers type coercion, integer conversions, and standard Number methods.",
    "theory": "CHAPTER 1: NUMERIC TYPES, LITERALS & PRECISION\n\n1. IEEE 754 64-Bit Binary Format:\nJavaScript has only ONE numeric type (IEEE 754 double precision floating point).\n- Bits 0-51: Fraction / Mantissa (value)\n- Bits 52-62: Exponent\n- Bit 63: Sign bit\nInteger values are accurate up to 15 digits (range -2^53 + 1 to 2^53 - 1).\n\n2. Scientific Notation:\nExtra-large or extra-small numbers use exponent notation:\nlet a = 156e5;  // 15600000\nlet b = 156e-5; // 0.00156\n\n3. Floating Point Precision:\nBinary floating point math can cause precision loss (e.g. 0.22 + 0.12 = 0.33999999999999997).\nSolution: Multiply to integers before dividing: ((0.22 * 10) + (0.12 * 10)) / 10 = 0.34.\n\n4. Special Values (NaN & Infinity):\n- NaN: Returned when numeric operations fail (e.g. 0 / 0 or 'hello' * 2).\n- Infinity / -Infinity: Returned when exceeding maximum values (e.g. 1 / 0).\n\n5. Number Literals:\n- Decimal: let a = 33; let b = 3.3;\n- Octal (starts with 0o): let x = 0o562; (370 in decimal)\n- Binary (starts with 0b): let x = 0b11; (3 in decimal)\n- Hexadecimal (starts with 0x): let x = 0xfff; (4095 in decimal)\n\n\nCHAPTER 2: NUMBER COERCION, CONVERSIONS & METHODS\n\n1. String Concatenation vs Addition:\nThe + operator adds numbers but concatenates strings (10 + 15 = 25 vs '10' + '30' = '1030').\nOther operators (-, *, /) automatically convert numeric strings ('100' / '10' = 10).\n\n2. Type Coercion Rules:\n- undefined + 10 -> NaN\n- null + 5 -> 5 (null is coerced to 0)\n- true + 10 -> 11, false + 10 -> 10 (true=1, false=0)\n- Number('42') -> 42, Number('hello') -> NaN\n\n3. Conversions & Bitwise Operations:\nBitwise operations convert operands to 32-bit fixed-width integers.\n\n4. Standard Number Methods:\n- num.toString(base): Converts number to string (supports radix base 2 to 36).\n- num.toExponential(fractionDigits): Formats number in exponential notation.\n- num.toPrecision(precision): Formats number to specified length.\n- Number.isInteger(val): Returns true if value is an integer.\n- num.toLocaleString(locale): Formats number according to locale convention.\n\n5. Key Facts:\nJavaScript primitive numbers can also be created as objects using `new Number()`. BigInt handles integers beyond 2^53 - 1.",
    "syntax": "// Chapter 1: Number Literals & Scientific Notation\nlet bin = 0b1010; // Binary\nlet hex = 0xFF;   // Hexadecimal\nlet sci = 1.5e3;  // 1500\n\n// Chapter 2: Coercion & Methods\nlet n = null + 10;     // 10\nlet isInt = Number.isInteger(42); // true\nlet str = (255).toString(16);     // 'ff'",
    "example": {
        "code": "// Chapter 1 Example: IEEE 754 & Literals\nlet binVal = 0b11;\nlet hexVal = 0x10;\nlet floatMath = (0.22 * 10 + 0.12 * 10) / 10;\nconsole.log('Binary 0b11:', binVal);\nconsole.log('Hex 0x10:', hexVal);\nconsole.log('Scaled Float Math:', floatMath);\n\n// Chapter 2 Example: Coercion & Methods\nconsole.log('null + 5:', null + 5);\nconsole.log('undefined + 5:', undefined + 5);\nlet x = 21;\nconsole.log('x.toString(16):', x.toString(16));\nconsole.log('Number.isInteger(x):', Number.isInteger(x));",
        "output": "Binary 0b11: 3\nHex 0x10: 16\nScaled Float Math: 0.34\nnull + 5: 5\nundefined + 5: NaN\nx.toString(16): 15\nNumber.isInteger(x): true",
        "explanation": "Demonstrates binary/hex literals, float math scaling (Chapter 1), alongside implicit null/undefined coercion and Number methods (Chapter 2).",
    },
    "fill_blanks": {
        "question": "// Chapter 1: Binary literal representation for 3\nlet b = 0b11;\n// Chapter 2: Coercion of null to number in arithmetic\nlet sum = null + 10; // sum equals _____",
        "answers": ["10"],
        "options": ["10", "NaN", "null10", "undefined"],
    },
    "compiler": {
        "title": "JavaScript Numbers Sandbox",
        "question": "Complete the code to check if x is an integer and convert decimal 255 to hex string.",
        "starter_code": "let num = 255;\nconsole.log('Is Integer:', Number._____(num));\nconsole.log('Hex String:', num._____(16));",
        "options": ["isInteger", "toString", "isFinite", "toFixed"],
    },
    "skill_exa_test": [
        {
            "question": "How are numbers stored in JavaScript under the IEEE 754 standard?",
            "options": [
                "In double-precision 64-bit binary format (52 fraction bits, 11 exponent bits, 1 sign bit)",
                "As 32-bit single precision integers",
                "As dynamic string buffers",
                "As 128-bit decimal structures"
            ],
            "answer": "In double-precision 64-bit binary format (52 fraction bits, 11 exponent bits, 1 sign bit)",
        },
        {
            "question": "What is the result of evaluating 0.22 + 0.12 directly in JavaScript without rounding?",
            "options": [
                "0.33999999999999997 due to binary floating-point representation limits",
                "0.34 exactly",
                "0.34000000000000000",
                "NaN"
            ],
            "answer": "0.33999999999999997 due to binary floating-point representation limits",
        },
        {
            "question": "What values do null and undefined coerce to when used in numeric arithmetic operations?",
            "options": [
                "null coerces to 0, whereas undefined coerces to NaN",
                "Both coerce to 0",
                "Both coerce to NaN",
                "null coerces to NaN, whereas undefined coerces to 0"
            ],
            "answer": "null coerces to 0, whereas undefined coerces to NaN",
        },
        {
            "question": "Which of the following prefix notations represents a Binary number literal in JavaScript?",
            "options": [
                "0b or 0B (e.g. 0b11)",
                "0x or 0X (e.g. 0xFF)",
                "0o or 0O (e.g. 0o56)",
                "0d or 0D (e.g. 0d10)"
            ],
            "answer": "0b or 0B (e.g. 0b11)",
        },
        {
            "question": "Which method converts a number into a string representation in a specified radix base (from base 2 to base 36)?",
            "options": [
                "num.toString(radix)",
                "num.toFixed(radix)",
                "Number.parseBase(radix)",
                "num.toLocaleString(radix)"
            ],
            "answer": "num.toString(radix)",
        },
    ],
}

# Override Topic 56: JavaScript Strings (Split into Chapter 1 & Chapter 2)
JS_TOPICS[56] = {
    "id": 56,
    "title": "JavaScript Strings",
    "category": "JavaScript Data Structures",
    "difficulty": "Beginner",
    "duration": "25 min",
    "concept": "A JavaScript String is an immutable sequence of UTF-16 characters used to represent text. This topic is split into two core chapters: Chapter 1 covers string creation, immutability, template literals, and escape sequences; Chapter 2 covers string operations, search, manipulation methods, and primitive vs object comparisons.",
    "theory": "CHAPTER 1: STRING CREATION, REPRESENTATIONS & LITERALS\n\n1. String Definition & Immutability:\nJavaScript strings are primitive sequences of characters. Unlike C/C++/Java, JavaScript has no separate 'char' data type; a single character is simply a string of length 1. JavaScript strings are IMMUTABLE (their contents cannot be modified in-place after creation).\n\n2. Ways to Create Strings:\na. String Literals (Recommended):\n   - Single Quote: let s1 = 'abcd';\n   - Double Quote: let s2 = \"abcd\";\nb. String Constructor Object (Not Recommended for Primitives):\n   - let s = new String('abcd'); // Creates a String Object rather than primitive string.\nc. Template Literals (String Interpolation - ES6):\n   - Created using backticks (`). Allows dynamic expression embedding via ${expression}:\n     let topic = 'JavaScript';\n     let msg = `Learning ${topic} on SkillExa`;\nd. Empty Strings:\n   - Created with empty quotes: let empty = \"\";\ne. Multiline Strings:\n   - Template literals with backticks preserve line breaks natively:\n     let multiline = `First line\n     Second line`;\n\n3. Escape Characters & Breaking Long Strings:\n- Escape characters: \\' (single quote), \\\" (double quote), \\\\ (backslash).\n- Breaking long lines: Use string concatenation (+) rather than backslash (\\) for safety in strict mode.\n\n\nCHAPTER 2: STRING OPERATIONS, SEARCH, METHODS & COMPARISON\n\n1. Basic Properties & Concatenation:\n- Finding length: str.length property.\n- Concatenation: Combining strings using + operator (e.g. 'Java' + 'Script' -> 'JavaScript').\n\n2. Substring & Case Conversion Methods:\n- str.substring(startIndex, endIndex): Extracts characters from startIndex up to (excluding) endIndex.\n- str.toUpperCase() & str.toLowerCase(): Converts string to upper or lower case.\n\n3. Search & Replacement Methods:\n- str.indexOf(substring): Returns first index of substring, or -1 if not found.\n- str.replace(target, replacement): Replaces first occurrence. Use regular expression with global flag /g (e.g. str.replace(/HTML/g, 'JS')) to replace all occurrences.\n\n4. Whitespace Trimming & Character Access:\n- str.trim(): Removes leading and trailing whitespaces.\n- Character Access: Bracket notation str[index] or str.charAt(index).\n\n5. String Comparison & Primitive vs Object:\n- Loose Equality (==): Returns true when comparing String Object with Primitive String due to implicit coercion ('Ajay' == new String('Ajay')).\n- Strict Equality (===): Returns false because primitive string and String object are different data types.\n- str1.localeCompare(str2): Compares strings lexicographically (returns 0 if equal, negative if str1 < str2, positive if str1 > str2).",
    "syntax": "// Chapter 1: Literals, Template Literals & Escape Sequences\nlet str = \"Hello World\";\nlet template = `Interactive ${str}`;\nlet escaped = \"\\\"SkillExa\\\" Learning Platform\";\n\n// Chapter 2: String Operations & Comparison Methods\nlet upper = str.toUpperCase();\nlet sub = str.substring(0, 5);\nlet cmp = \"Ajay\".localeCompare(\"Ajay\"); // 0",
    "example": {
        "code": "// Chapter 1 Example: Template Literals & Creation\nlet name = 'JavaScript';\nlet greeting = `Welcome to ${name}!`;\nlet multiline = `Line 1\\nLine 2`;\nconsole.log(greeting);\n\n// Chapter 2 Example: Methods & Object Comparison\nlet str1 = '  Learn JS  ';\nlet trimmed = str1.trim();\nlet replaced = trimmed.replace('JS', 'JavaScript');\nconsole.log('Processed:', replaced);\n\nlet prim = 'SkillExa';\nlet obj = new String('SkillExa');\nconsole.log('prim == obj:', prim == obj);\nconsole.log('prim === obj:', prim === obj);\nconsole.log('localeCompare:', prim.localeCompare(obj));",
        "output": "Welcome to JavaScript!\nProcessed: Learn JavaScript\nprim == obj: true\nprim === obj: false\nlocaleCompare: 0",
        "explanation": "Demonstrates template interpolation (Chapter 1) alongside trim, replace, loose vs strict primitive/object equality, and localeCompare (Chapter 2).",
    },
    "fill_blanks": {
        "question": "// Chapter 1: Template literal interpolation syntax\nlet lang = 'JS';\nlet msg = `SkillExa ${lang}`;\n// Chapter 2: Strict comparison between primitive and String object returns _____\nconsole.log('abc' === new String('abc'));",
        "answers": ["false"],
        "options": ["false", "true", "0", "undefined"],
    },
    "compiler": {
        "title": "JavaScript Strings Sandbox",
        "question": "Complete the code to extract a substring and replace target text globally.",
        "starter_code": "let text = 'Learn HTML at SkillExa and HTML is fun';\nlet sub = text._____(0, 10);\nlet replaced = text.replace(/HTML/g, '____');\nconsole.log(sub);\nconsole.log(replaced);",
        "options": ["substring", "JavaScript", "slice", "Python"],
    },
    "skill_exa_test": [
        {
            "question": "Are strings in JavaScript mutable or immutable?",
            "options": [
                "Strings are immutable; their individual characters cannot be modified in-place after creation",
                "Strings are mutable; character elements can be modified using array bracket assignment str[0] = 'X'",
                "Strings are mutable only when declared with the let keyword",
                "Strings are mutable only inside class functions"
            ],
            "answer": "Strings are immutable; their individual characters cannot be modified in-place after creation",
        },
        {
            "question": "What is the difference between comparing a primitive string and a String object with == versus === (e.g. 'Ajay' == new String('Ajay') vs 'Ajay' === new String('Ajay'))?",
            "options": [
                "== returns true due to type coercion, whereas === returns false because primitives and String objects are different types",
                "Both == and === return true",
                "Both == and === return false",
                "== returns false and === returns true"
            ],
            "answer": "== returns true due to type coercion, whereas === returns false because primitives and String objects are different types",
        },
        {
            "question": "Which string method replaces ALL occurrences of a substring when using a regular expression with the /g flag?",
            "options": [
                "str.replace(/pattern/g, 'replacement')",
                "str.replaceAllSubstring()",
                "str.substringReplace()",
                "str.concatReplace()"
            ],
            "answer": "str.replace(/pattern/g, 'replacement')",
        },
        {
            "question": "Which feature introduced in ES6 uses backticks (`) to allow dynamic expression embedding (${expr}) and native multiline strings?",
            "options": [
                "Template Literals (String Interpolation)",
                "String Builders",
                "String Vectors",
                "Macro Statements"
            ],
            "answer": "Template Literals (String Interpolation)",
        },
        {
            "question": "What does str1.localeCompare(str2) return when str1 and str2 are lexicographically equal?",
            "options": [
                "0",
                "1",
                "-1",
                "true"
            ],
            "answer": "0",
        },
    ],
}

# Override Topic 57: JavaScript Arrays (Split into Chapter 1 & Chapter 2)
JS_TOPICS[57] = {
    "id": 57,
    "title": "JavaScript Arrays",
    "category": "JavaScript Data Structures",
    "difficulty": "Beginner",
    "duration": "25 min",
    "concept": "In JavaScript, an array is an ordered zero-indexed collection of values capable of storing heterogeneous data types. This topic is split into two core chapters: Chapter 1 covers array creation, indexing, modification, push/pop/shift/unshift/splice operations, and the constructor pitfall; Chapter 2 covers array length mutation, loops, concat, toString, and array recognition with Array.isArray() and instanceof.",
    "theory": "CHAPTER 1: ARRAY CREATION, INDEXING & BASIC OPERATIONS\n\n1. Array Definition & Indexing:\nAn array is an ordered sequence of elements stored in a single variable. Indexing starts at 0 (first element at index 0, last element at index length - 1). Arrays can store any data type (numbers, strings, objects, or nested arrays).\n\n2. Array Creation Methods:\na. Array Literal Syntax (Recommended): Uses square brackets [].\n   let arr1 = [];             // Empty array\n   let arr2 = [10, 20, 30];   // Initialized array\nb. Array Constructor Syntax: Uses new Array().\n   let arr3 = new Array(10, 20, 30);\nc. Array Constructor Pitfall:\n   - const a1 = [5];         // Creates an array with 1 element: [5]\n   - const a2 = new Array(5);// Creates an empty array with length 5!\n\n3. Accessing & Modifying Elements:\n- Accessing elements: arr[0] (first item), arr[arr.length - 1] (last item).\n- Modifying elements: Direct assignment arr[1] = \"Bootstrap\".\n\n4. Adding Elements:\n- arr.push(element): Appends element to the end of the array.\n- arr.unshift(element): Prepends element to the beginning of the array.\n\n5. Removing Elements:\n- arr.pop(): Removes and returns the last element.\n- arr.shift(): Removes and returns the first element.\n- arr.splice(startIndex, deleteCount): Removes or replaces elements starting from startIndex.\n\n\nCHAPTER 2: ARRAY LENGTH, ITERATION, METHODS & TYPE RECOGNITION\n\n1. Array Length Property & Mutation:\n- Finding length: arr.length property.\n- Mutating length:\n  - Increasing length (arr.length = 7) expands the array with empty slots.\n  - Decreasing length (arr.length = 2) truncates elements beyond index 1.\n\n2. Array Iteration:\n- Standard for loop: for (let i = 0; i < arr.length; i++) { console.log(arr[i]); }\n- Array.prototype.forEach(): arr.forEach(item => console.log(item));\n\n3. Concatenation & String Conversion:\n- arr1.concat(arr2): Joins arrays and returns a new combined array.\n- arr.toString(): Converts array elements into a comma-separated string (e.g. \"HTML,CSS,JS\").\n\n4. Checking & Recognizing Arrays:\n- typeof operator: Returns \"object\" for arrays (since arrays are objects in JS).\n- Array.isArray(arr): Standard method returning true if value is an array.\n- arr instanceof Array: Operator checking if value inherits from Array prototype.",
    "syntax": "// Chapter 1: Array Literals, Indexing & Mutating Operations\nlet arr = [\"HTML\", \"CSS\", \"JS\"];\narr.push(\"React\");    // Add to end\narr.unshift(\"Web\");   // Add to start\narr.pop();            // Remove from end\narr.shift();          // Remove from start\narr.splice(1, 1);     // Remove 1 item at index 1\n\n// Chapter 2: Length, Iteration & Array Recognition\narr.length = 5;       // Change length\narr.forEach(item => console.log(item));\nlet isArr = Array.isArray(arr); // true",
    "example": {
        "code": "// Chapter 1 Example: Creation, Operations & Pitfall\nlet a1 = [5];\nlet a2 = new Array(5);\nconsole.log('Literal [5]:', a1, '| length:', a1.length);\nconsole.log('Constructor new Array(5) length:', a2.length);\n\nlet tech = ['HTML', 'CSS', 'JS'];\ntech.push('Node.js');\ntech.unshift('WebDev');\nconsole.log('Modified Tech:', tech);\n\n// Chapter 2 Example: Iteration, Concat & Type Check\nlet framework = ['React', 'Vue'];\nlet merged = tech.concat(framework);\nconsole.log('Merged:', merged.toString());\nconsole.log('typeof merged:', typeof merged);\nconsole.log('Array.isArray(merged):', Array.isArray(merged));\nconsole.log('merged instanceof Array:', merged instanceof Array);",
        "output": "Literal [5]: [ 5 ] | length: 1\nConstructor new Array(5) length: 5\nModified Tech: [ 'WebDev', 'HTML', 'CSS', 'JS', 'Node.js' ]\nMerged: WebDev,HTML,CSS,JS,Node.js,React,Vue\ntypeof merged: object\nArray.isArray(merged): true\nmerged instanceof Array: true",
        "explanation": "Demonstrates array literals vs constructor pitfall, push/unshift (Chapter 1), alongside concat, toString, typeof 'object', Array.isArray(), and instanceof (Chapter 2).",
    },
    "fill_blanks": {
        "question": "// Chapter 1: Add element to beginning of array\nlet arr = ['CSS', 'JS'];\narr.____('HTML'); // ['HTML', 'CSS', 'JS']\n// Chapter 2: Method to reliably check if variable is an array\nconsole.log(Array.____(arr)); // true",
        "answers": ["unshift", "isArray"],
        "options": ["unshift", "push", "isArray", "isVector"],
    },
    "compiler": {
        "title": "JavaScript Arrays Sandbox",
        "question": "Complete the code to access the last element and verify if item is an Array instance.",
        "starter_code": "let items = ['HTML', 'CSS', 'JS'];\nlet lastItem = items[items.____ - 1];\nconsole.log('Last:', lastItem);\nconsole.log('Is Array:', items _____ Array);",
        "options": ["length", "instanceof", "size", "typeof"],
    },
    "skill_exa_test": [
        {
            "question": "What is the key difference between const a1 = [5] and const a2 = new Array(5) in JavaScript?",
            "options": [
                "a1 creates an array containing one element [5], whereas new Array(5) creates an empty array with length 5",
                "Both statements create an array containing one element [5]",
                "a1 creates an array of length 5, whereas new Array(5) throws a SyntaxError",
                "new Array(5) converts the number 5 into a string '5'"
            ],
            "answer": "a1 creates an array containing one element [5], whereas new Array(5) creates an empty array with length 5",
        },
        {
            "question": "Which methods are used to add elements to the START and END of a JavaScript array respectively?",
            "options": [
                "unshift() to add to the start, and push() to add to the end",
                "push() to add to the start, and unshift() to add to the end",
                "pop() to add to the start, and shift() to add to the end",
                "concat() to add to the start, and splice() to add to the end"
            ],
            "answer": "unshift() to add to the start, and push() to add to the end",
        },
        {
            "question": "What happens when you explicitly decrease an array's length property (e.g. arr.length = 2 on a 4-element array)?",
            "options": [
                "The array is truncated, permanently removing elements beyond index 1",
                "An error is thrown because array length is read-only",
                "The array elements are backed up into a temporary buffer",
                "The array elements are converted into null values without changing length"
            ],
            "answer": "The array is truncated, permanently removing elements beyond index 1",
        },
        {
            "question": "What does the typeof operator return when executed on a JavaScript array (e.g. typeof [1, 2, 3])?",
            "options": [
                "\"object\"",
                "\"array\"",
                "\"list\"",
                "\"collection\""
            ],
            "answer": "\"object\"",
        },
        {
            "question": "Which of the following methods reliably checks whether a variable is a JavaScript array?",
            "options": [
                "Array.isArray(variable) and (variable instanceof Array)",
                "typeof variable == 'array'",
                "variable.isArray()",
                "variable.type() == 'Array'"
            ],
            "answer": "Array.isArray(variable) and (variable instanceof Array)",
        },
    ],
}

# Override Topic 58: Map in JavaScript
JS_TOPICS[58] = {
    "id": 58,
    "title": "Map in JavaScript",
    "category": "JavaScript Data Structures",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "A JavaScript Map is a built-in collection of key-value pairs that preserves insertion order, allows keys of any data type (primitives, objects, functions), and uses internal hashing for O(1) average time complexity search, insertion, and deletion.",
    "theory": "JavaScript Map Data Structure:\n\nA Map holds key-value pairs where any value (objects and primitive values) may be used as either a key or a value. Unlike plain JavaScript Objects, Maps maintain insertion order and permit arbitrary key types.\n\nCore Characteristics of Map:\n1. Flexible Key Types: Unlike plain Objects (where keys are restricted to Strings and Symbols), Map keys can be numbers, booleans, objects, functions, or any primitive.\n2. Preserves Insertion Order: Iterating over a Map yields keys/values in the exact order they were inserted.\n3. Unique Keys: Duplicate keys are not allowed. Calling set(key, val) with an existing key overwrites the old value.\n4. Performance & Hashing: Uses internal hash-table lookup providing O(1) average time complexity for get(), set(), has(), and delete(). Recommended over plain Objects for frequent insertion and deletion tasks.\n\nCreation Methods:\n1. Constructor with Iterable:\n   let map1 = new Map([\n       ['name', 'SkillExa'],\n       ['age', 25],\n       ['city', 'Noida']\n   ]);\n2. Empty Constructor & set():\n   let map2 = new Map();\n   map2.set('name', 'GFG');\n\nCore Map Methods & Properties:\n- set(key, value): Adds or updates a key-value pair.\n- get(key): Returns the value associated with the key, or undefined if not found.\n- has(key): Returns true if the key exists in the Map; false otherwise.\n- delete(key): Removes the key-value pair and returns true if deleted.\n- clear(): Removes all key-value pairs from the Map.\n- size: Property returning the total number of key-value pairs.\n\nAdvantages of Map Over Plain Object:\n- Key Types: Objects only allow string/symbol keys; Map allows any type.\n- Order: Map preserves insertion order guaranteed; Object keys are unordered.\n- Size: Map has a built-in size property; Object size must be calculated manually.\n- Performance: Optimized for frequent additions and removals.",
    "syntax": "// Creation & Core Operations\nconst map = new Map();\nmap.set('key1', 'value1');\nmap.set(100, 'numberKey');\n\nlet val = map.get('key1');    // 'value1'\nlet exists = map.has(100);    // true\nlet count = map.size;         // 2\nmap.delete(100);              // Removes 100\nmap.clear();                  // Empties map",
    "example": {
        "code": "// Creating and Initializing a Map\nconst myMap = new Map([\n    ['name', 'SkillExa'],\n    ['age', 25]\n]);\n\n// 1. set(key, value) with various key types\nmyMap.set(1, 'One');\nconst objKey = { id: 101 };\nmyMap.set(objKey, 'ObjectValue');\n\n// 2. get(key) & has(key)\nconsole.log('get(name):', myMap.get('name'));\nconsole.log('get(objKey):', myMap.get(objKey));\nconsole.log('has(age):', myMap.has('age'));\n\n// 3. delete(key) & size\nmyMap.delete('age');\nconsole.log('Size after delete:', myMap.size);\nconsole.log('has(age) after delete:', myMap.has('age'));\n\n// 4. clear()\nmyMap.clear();\nconsole.log('Size after clear():', myMap.size);",
        "output": "get(name): SkillExa\nget(objKey): ObjectValue\nhas(age): true\nSize after delete: 3\nhas(age) after delete: false\nSize after clear(): 0",
        "explanation": "Demonstrates initializing a Map with 2D array entries, setting primitive & object keys, get/has/delete operations, and checking the size property.",
    },
    "fill_blanks": {
        "question": "// Add key-value pair to Map\nlet m = new Map();\nm.____('course', 'JS');\n// Check if key exists in Map\nif (m.____('course')) {\n    console.log(m.get('course'));\n}",
        "answers": ["set", "has"],
        "options": ["set", "has", "add", "contains"],
    },
    "compiler": {
        "title": "JavaScript Map Practice Sandbox",
        "question": "Complete the code to set a key, retrieve its size, and delete a key from the Map.",
        "starter_code": "let myMap = new Map();\nmyMap.set('a', 10);\nmyMap.set('b', 20);\nconsole.log('Count:', myMap.____);\nmyMap.____('a');\nconsole.log('Has a:', myMap.has('a'));",
        "options": ["size", "delete", "length", "remove"],
    },
    "skill_exa_test": [
        {
            "question": "What is a primary advantage of a JavaScript Map over a plain JavaScript Object regarding key data types?",
            "options": [
                "Map keys can be of any data type (including objects, functions, and numbers), whereas Object keys are restricted to Strings and Symbols",
                "Map keys can only be strings",
                "Objects support function keys, whereas Map does not",
                "Map automatically converts all keys into uppercase strings"
            ],
            "answer": "Map keys can be of any data type (including objects, functions, and numbers), whereas Object keys are restricted to Strings and Symbols",
        },
        {
            "question": "What is the average time complexity of get(), set(), has(), and delete() operations in a JavaScript Map?",
            "options": [
                "O(1) constant time due to internal hashing",
                "O(N) linear time requiring full array scans",
                "O(N log N) logarithmic time",
                "O(N²)"
            ],
            "answer": "O(1) constant time due to internal hashing",
        },
        {
            "question": "What happens when you insert a duplicate key into a Map using map.set(key, newValue)?",
            "options": [
                "The new value overwrites the existing value associated with that key",
                "An error is thrown indicating key collision",
                "The new value is ignored and the old value is kept",
                "A second entry with the same key is appended"
            ],
            "answer": "The new value overwrites the existing value associated with that key",
        },
        {
            "question": "Which Map property returns the total count of key-value pairs currently stored in the Map?",
            "options": [
                "map.size",
                "map.length",
                "map.count()",
                "map.total"
            ],
            "answer": "map.size",
        },
        {
            "question": "What does map.get('nonExistentKey') return when called with a key that is not in the Map?",
            "options": [
                "undefined",
                "null",
                "false",
                "-1"
            ],
            "answer": "undefined",
        },
    ],
}

# Override Topic 59: LinkedList in JavaScript
JS_TOPICS[59] = {
    "id": 59,
    "title": "LinkedList in JavaScript",
    "category": "JavaScript Data Structures",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "A Linked List is a dynamic linear data structure composed of nodes linked by pointers. Each Node holds data and a reference (next pointer) to the subsequent node, terminating at null. Unlike contiguous arrays, linked lists allocate memory dynamically and allow O(1) time insertions/deletions at the head.",
    "theory": "Implementation & Mechanics of LinkedList in JavaScript:\n\nA Linked List is a linear collection of data elements called Nodes, where linear order is determined by pointers rather than memory locations.\n\nCore Components:\n1. Node Class: Represents an individual element storing a `value` payload and a `next` pointer pointing to the following node.\n   class Node {\n       constructor(value) {\n           this.value = value;\n           this.next = null;\n       }\n   }\n\n2. LinkedList Class: Manages the node chain starting from a single `head` reference.\n   class LinkedList {\n       constructor() {\n           this.head = null;\n       }\n   }\n\nKey Operations on Singly Linked List:\n- append(value): Traverses to the tail node (where current.next is null) and attaches a new node.\n- prepend(value): Creates a new node, sets its next pointer to the current head, and updates head to the new node (O(1) time complexity).\n- insertAt(value, position): Inserts a node at index position by adjusting previous.next and newNode.next pointers.\n- deleteNode(value): Finds node with target value and bypasses it by connecting previous.next to current.next.next.\n- printList(): Traverses from head to end, outputting formatted chain string (e.g., '5->10->15->null').\n\nReal-World Use Cases:\n1. Web Browser History: Back and forward navigation through visited URLs.\n2. Music/Video Streaming Playlists: Dynamic addition and removal of tracks without resizing contiguous memory buffers.\n3. OS Dynamic Memory Allocation: Managing free and allocated memory chunks.\n4. Real-time Event Schedulers & Timelines: Dynamically inserting tasks or social media posts in order.\n\nAdvantages of Linked List vs. Array:\n- Dynamic Size: Grows or shrinks on demand without pre-allocation or array resizing overhead.\n- Efficient Insertions & Deletions: Prepending or inserting at a known node takes O(1) time pointer manipulation (unlike arrays which require shifting elements).\n- Flexible Non-Contiguous Storage: Nodes are allocated individually anywhere in heap memory.",
    "syntax": "// Node & LinkedList Class Definition\nclass Node {\n    constructor(val) {\n        this.value = val;\n        this.next = null;\n    }\n}\n\nclass LinkedList {\n    constructor() { this.head = null; }\n    prepend(val) {\n        let node = new Node(val);\n        node.next = this.head;\n        this.head = node;\n    }\n}",
    "example": {
        "code": "class Node {\n    constructor(value) {\n        this.value = value;\n        this.next = null;\n    }\n}\n\nclass LinkedList {\n    constructor() {\n        this.head = null;\n    }\n    append(value) {\n        let newNode = new Node(value);\n        if (!this.head) { this.head = newNode; return; }\n        let current = this.head;\n        while (current.next) { current = current.next; }\n        current.next = newNode;\n    }\n    prepend(value) {\n        let newNode = new Node(value);\n        newNode.next = this.head;\n        this.head = newNode;\n    }\n    insertAt(value, position) {\n        if (position === 0 || !this.head) { this.prepend(value); return; }\n        let newNode = new Node(value);\n        let current = this.head, previous = null, index = 0;\n        while (current && index < position) {\n            previous = current;\n            current = current.next;\n            index++;\n        }\n        previous.next = newNode;\n        newNode.next = current;\n    }\n    deleteNode(value) {\n        if (!this.head) return;\n        if (this.head.value === value) { this.head = this.head.next; return; }\n        let current = this.head;\n        while (current.next && current.next.value !== value) { current = current.next; }\n        if (current.next) { current.next = current.next.next; }\n    }\n    printList() {\n        let current = this.head, res = '';\n        while (current) { res += current.value + '->'; current = current.next; }\n        console.log(res + 'null');\n    }\n}\n\nlet list = new LinkedList();\nlist.append(10);\nlist.append(20);\nlist.append(30);\nlist.prepend(5);\nlist.insertAt(15, 2);\nlist.deleteNode(20);\nlist.printList();",
        "output": "5->10->15->30->null",
        "explanation": "Appends 10,20,30, prepends 5 (5->10->20->30), inserts 15 at index 2 (5->10->15->20->30), deletes 20, resulting in 5->10->15->30->null.",
    },
    "fill_blanks": {
        "question": "// Prepend node to beginning of LinkedList\nprepend(value) {\n    let newNode = new Node(value);\n    newNode.____ = this.head;\n    this.head = ____;\n}",
        "answers": ["next", "newNode"],
        "options": ["next", "newNode", "value", "previous"],
    },
    "compiler": {
        "title": "LinkedList Implementation Sandbox",
        "question": "Complete the Node class and prepend method to insert a node at the head of the LinkedList.",
        "starter_code": "class Node {\n    constructor(val) { this.value = val; this.____ = null; }\n}\nclass LinkedList {\n    constructor() { this.head = null; }\n    prepend(val) {\n        let node = new Node(val);\n        node.next = this.____;\n        this.head = node;\n    }\n}\nlet list = new LinkedList();\nlist.prepend(10);\nconsole.log('Head Value:', list.head.value);",
        "options": ["next", "head", "previous", "tail"],
    },
    "skill_exa_test": [
        {
            "question": "What two essential properties does a Node contain in a Singly Linked List?",
            "options": [
                "A value payload (data) and a reference (pointer) to the next node",
                "An array index integer and a string identifier",
                "A left child pointer and a right child pointer",
                "A key hash code and a capacity limit"
            ],
            "answer": "A value payload (data) and a reference (pointer) to the next node",
        },
        {
            "question": "What is the time complexity of prepending a new element at the beginning (head) of a Singly Linked List?",
            "options": [
                "O(1) constant time because only head pointers need updating",
                "O(N) linear time requiring traversal to the tail",
                "O(N log N) logarithmic time",
                "O(N²) quadratic time"
            ],
            "answer": "O(1) constant time because only head pointers need updating",
        },
        {
            "question": "How does deleting a middle node with a target value work in a Singly Linked List?",
            "options": [
                "By bypassing the target node and connecting the previous node's next pointer directly to the current node's next.next node",
                "By shifting all subsequent elements left in contiguous memory",
                "By setting the target node value to NaN",
                "By rebuilding the entire list from scratch"
            ],
            "answer": "By bypassing the target node and connecting the previous node's next pointer directly to the current node's next.next node",
        },
        {
            "question": "Which of the following real-world applications commonly uses a Linked List data structure?",
            "options": [
                "Web browser page history navigation (back and forward buttons) and music streaming playlists",
                "Hardware CPU cache L1 instruction registers",
                "GPU pixel rasterization shaders",
                "Static CSS stylesheet compilers"
            ],
            "answer": "Web browser page history navigation (back and forward buttons) and music streaming playlists",
        },
        {
            "question": "What is a major advantage of a Linked List over a standard JavaScript Array?",
            "options": [
                "Linked lists have dynamic size and permit O(1) insertions/deletions at the head without memory re-allocation or element shifting",
                "Linked lists allow random indexed access in O(1) time using arr[i]",
                "Linked lists consume zero memory for pointer references",
                "Linked lists are executed directly on the GPU"
            ],
            "answer": "Linked lists have dynamic size and permit O(1) insertions/deletions at the head without memory re-allocation or element shifting",
        },
    ],
}

# Override Topic 60: Stack in JavaScript
JS_TOPICS[60] = {
    "id": 60,
    "title": "Stack in JavaScript",
    "category": "JavaScript Data Structures",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "A Stack is a fundamental linear data structure in JavaScript that follows the Last In, First Out (LIFO) principle. Operations occur at a single end called the top. This topic covers LIFO mechanics, extreme conditions (Stack Underflow/Overflow), and both Array-based and Linked List-based implementations in O(1) time.",
    "theory": "Stack Data Structure in JavaScript:\n\nA Stack manages elements in a LIFO (Last In, First Out) sequence, where the most recently added item is the first one removed.\n\nCore Stack Operations:\n- push(element): Adds an element onto the top of the stack.\n- pop(): Removes and returns the top element from the stack.\n- peek(): Inspects the top element without removing it.\n- isEmpty(): Returns true if the stack contains zero elements.\n- size(): Returns the total number of items in the stack.\n\nExtreme Stack Conditions:\n1. Stack Underflow: Occurs when calling pop() or peek() on an empty stack. Handled by checking isEmpty() before accessing elements.\n2. Stack Overflow: Occurs when pushing into a stack that has reached maximum fixed capacity limit.\n\nTwo Implementation Approaches in JavaScript:\n\n1. Array-Based Stack Implementation:\nUses a JavaScript array performing push() and pop() at the end of the array in O(1) constant time.\nclass Stack {\n    constructor() { this.items = []; }\n    push(element) { this.items.push(element); }\n    pop() { return this.isEmpty() ? null : this.items.pop(); }\n    peek() { return this.isEmpty() ? null : this.items[this.items.length - 1]; }\n    isEmpty() { return this.items.length === 0; }\n    size() { return this.items.length; }\n}\n\n2. Linked List-Based Stack Implementation:\nUses a Singly Linked List performing push() and pop() at the head (top node) in O(1) constant time.\nclass Node {\n    constructor(value) { this.value = value; this.next = null; }\n}\nclass Stack {\n    constructor() { this.top = null; this.size = 0; }\n    push(value) {\n        const newNode = new Node(value);\n        newNode.next = this.top;\n        this.top = newNode;\n        this.size++;\n    }\n    pop() {\n        if (this.isEmpty()) return null;\n        const val = this.top.value;\n        this.top = this.top.next;\n        this.size--;\n        return val;\n    }\n}\n\nReal-World Applications:\n- Function Call Stack management (execution context tracking in JS engines).\n- Undo / Redo history in text editors.\n- Expression parsing & syntax checking (matching parentheses).\n\nTime & Space Complexity:\n- Push, Pop, Peek, isEmpty, Size: O(1) constant time complexity and O(1) auxiliary space.",
    "syntax": "// Array-based Stack\nlet arrayStack = [];\narrayStack.push(10);\nlet topItem = arrayStack.pop();\n\n// Class-based Stack\nclass Stack {\n    constructor() { this.items = []; }\n    push(item) { this.items.push(item); }\n    pop() { return this.items.pop(); }\n    peek() { return this.items[this.items.length - 1]; }\n}",
    "example": {
        "code": "// Array-Based Stack Implementation\nclass ArrayStack {\n    constructor() { this.items = []; }\n    push(elem) { this.items.push(elem); }\n    pop() { return this.isEmpty() ? null : this.items.pop(); }\n    peek() { return this.isEmpty() ? null : this.items[this.items.length - 1]; }\n    isEmpty() { return this.items.length === 0; }\n    size() { return this.items.length; }\n}\n\n// Linked List-Based Stack Implementation\nclass Node {\n    constructor(val) { this.value = val; this.next = null; }\n}\nclass LinkedListStack {\n    constructor() { this.top = null; this.size = 0; }\n    push(val) {\n        const newNode = new Node(val);\n        newNode.next = this.top;\n        this.top = newNode;\n        this.size++;\n    }\n    pop() {\n        if (!this.top) return null;\n        const val = this.top.value;\n        this.top = this.top.next;\n        this.size--;\n        return val;\n    }\n}\n\nlet s1 = new ArrayStack();\ns1.push('A'); s1.push('B'); s1.push('C');\nconsole.log('ArrayStack Top:', s1.peek());\nconsole.log('ArrayStack Popped:', s1.pop());\n\nlet s2 = new LinkedListStack();\ns2.push(100); s2.push(200);\nconsole.log('LLStack Top:', s2.top.value);\nconsole.log('LLStack Popped:', s2.pop());",
        "output": "ArrayStack Top: C\nArrayStack Popped: C\nLLStack Top: 200\nLLStack Popped: 200",
        "explanation": "Demonstrates LIFO push/pop/peek operations for both Array-based and Linked List-based Stack implementations in O(1) time.",
    },
    "fill_blanks": {
        "question": "// Stack operates on the _____ (Last In, First Out) principle.\nclass Stack {\n    push(elem) { this.items.push(elem); }\n    pop() { return this.items.____(); }\n}",
        "answers": ["LIFO", "pop"],
        "options": ["LIFO", "FIFO", "pop", "shift"],
    },
    "compiler": {
        "title": "Stack Data Structure Sandbox",
        "question": "Complete the peek and isEmpty methods for the Stack class.",
        "starter_code": "class Stack {\n    constructor() { this.items = []; }\n    push(x) { this.items.push(x); }\n    peek() { return this.items[this.items.____ - 1]; }\n    isEmpty() { return this.items.length _____ 0; }\n}\nlet s = new Stack(); s.push(42);\nconsole.log('Top:', s.peek());\nconsole.log('Is Empty:', s.isEmpty());",
        "options": ["length", "===", "size", "=="],
    },
    "skill_exa_test": [
        {
            "question": "What fundamental data ordering principle does a Stack follow in computer science?",
            "options": [
                "LIFO (Last In, First Out)",
                "FIFO (First In, First Out)",
                "LILO (Last In, Last Out)",
                "Random Access Order"
            ],
            "answer": "LIFO (Last In, First Out)",
        },
        {
            "question": "What is Stack Underflow?",
            "options": [
                "An extreme condition occurring when performing a pop or peek operation on an empty stack",
                "An extreme condition occurring when pushing into a full stack",
                "A memory leak caused by unreferenced nodes",
                "When a stack converts string elements into numbers"
            ],
            "answer": "An extreme condition occurring when performing a pop or peek operation on an empty stack",
        },
        {
            "question": "What is the time complexity of push(), pop(), and peek() operations in an Array-based or Linked List-based Stack in JavaScript?",
            "options": [
                "O(1) constant time",
                "O(N) linear time",
                "O(N log N) logarithmic time",
                "O(N²)"
            ],
            "answer": "O(1) constant time",
        },
        {
            "question": "How does a Linked List-based Stack achieve O(1) time complexity for push() and pop() operations?",
            "options": [
                "By performing insertions and removals exclusively at the head (top) of the linked list",
                "By traversing to the tail of the list for every operation",
                "By allocating contiguous memory arrays dynamically",
                "By sorting the list in descending order"
            ],
            "answer": "By performing insertions and removals exclusively at the head (top) of the linked list",
        },
        {
            "question": "Which of the following is a common real-world application of a Stack data structure?",
            "options": [
                "Function call stack management in JS engines, Undo/Redo operation history, and expression parenthetical parsing",
                "GPU texture image sampling",
                "Direct database disk table scanning",
                "Network router IP routing tables"
            ],
            "answer": "Function call stack management in JS engines, Undo/Redo operation history, and expression parenthetical parsing",
        },
    ],
}

# Override Topic 61: Queue in JavaScript - Chapter 1
JS_TOPICS[61] = {
    "id": 61,
    "title": "Queue in JavaScript - Chapter 1",
    "category": "JavaScript Data Structures",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "A Queue is a linear data structure following the FIFO (First In, First Out) principle. Chapter 1 covers core queue operations (enqueue, dequeue, peek, isEmpty, size), Array-based implementation, and Linked List-based implementation with O(1) performance optimization.",
    "theory": "1. FIFO Mechanics & Core Operations:\nA Queue is an ordered list where elements are inserted at the rear (enqueue) and removed from the front (dequeue), maintaining First In, First Out (FIFO) ordering.\n- enqueue(data): Adds element to the rear of the queue.\n- dequeue(): Removes and returns the element at the front of the queue.\n- peek(): Returns the front element without removing it.\n- isEmpty(): Returns true if the queue contains no elements.\n- size(): Returns the total number of queued elements.\n\n2. Array-Based Implementation:\nUses JavaScript array methods: `push()` to enqueue at the rear (O(1)) and `shift()` to dequeue from the front (O(N) due to element re-indexing).\nclass ArrayQueue {\n    constructor() { this.items = []; }\n    enqueue(elem) { this.items.push(elem); }\n    dequeue() { return this.isEmpty() ? null : this.items.shift(); }\n    peek() { return this.isEmpty() ? null : this.items[0]; }\n    isEmpty() { return this.items.length === 0; }\n    size() { return this.items.length; }\n}\n\n3. Linked List-Based Implementation (O(1) Optimization):\nUses `front` and `rear` node pointers. Adding to tail and removing from head both achieve O(1) constant time complexity without element shifting overhead.\nclass Node { constructor(data) { this.data = data; this.next = null; } }\nclass LinkedListQueue {\n    constructor() { this.front = null; this.rear = null; this.size = 0; }\n    enqueue(data) {\n        const node = new Node(data);\n        if (this.isEmpty()) { this.front = node; this.rear = node; }\n        else { this.rear.next = node; this.rear = node; }\n        this.size++;\n    }\n    dequeue() {\n        if (this.isEmpty()) return null;\n        const val = this.front.data;\n        this.front = this.front.next;\n        if (!this.front) this.rear = null;\n        this.size--;\n        return val;\n    }\n    peek() { return this.isEmpty() ? null : this.front.data; }\n    isEmpty() { return this.size === 0; }\n}",
    "syntax": "// Array Queue Implementation\nlet qArray = [];\nqArray.push(10); // Enqueue at rear\nlet frontVal = qArray.shift(); // Dequeue from front (O(N))\n\n// Linked List Queue Implementation (O(1))\nlet qLL = new LinkedListQueue();\nqLL.enqueue(100);\nlet val = qLL.dequeue();",
    "example": {
        "code": "class Node { constructor(d) { this.data = d; this.next = null; } }\nclass LLQueue {\n    constructor() { this.front = null; this.rear = null; this.size = 0; }\n    enqueue(d) {\n        let node = new Node(d);\n        if (!this.front) { this.front = node; this.rear = node; }\n        else { this.rear.next = node; this.rear = node; }\n        this.size++;\n    }\n    dequeue() {\n        if (!this.front) return null;\n        let val = this.front.data;\n        this.front = this.front.next;\n        if (!this.front) this.rear = null;\n        this.size--;\n        return val;\n    }\n    peek() { return this.front ? this.front.data : null; }\n}\nlet queue = new LLQueue();\nqueue.enqueue(10);\nqueue.enqueue(20);\nqueue.enqueue(30);\nconsole.log('Front element:', queue.peek());\nconsole.log('Dequeued element:', queue.dequeue());\nconsole.log('New front:', queue.peek());",
        "output": "Front element: 10\nDequeued element: 10\nNew front: 20",
        "explanation": "Demonstrates linked list queue enqueue and dequeue operations operating in O(1) constant time.",
    },
    "fill_blanks": {
        "question": "// Queue follows _____ (First In, First Out) ordering.\n// Removing the front element of an Array Queue using shift() takes O(_____) time complexity.",
        "answers": ["FIFO", "N"],
        "options": ["FIFO", "LIFO", "N", "1"],
    },
    "compiler": {
        "title": "Linked List Queue Sandbox",
        "question": "Complete the Linked List Queue enqueue and peek methods.",
        "starter_code": "class Node { constructor(d) { this.data = d; this.next = null; } }\nclass Queue {\n    constructor() { this.front = null; this.rear = null; }\n    enqueue(d) {\n        let node = new Node(d);\n        if (!this.front) { this.front = node; this.rear = node; }\n        else { this.____.next = node; this.rear = node; }\n    }\n    peek() { return this.front ? this.front.____ : null; }\n}\nlet q = new Queue(); q.enqueue(42);\nconsole.log('Front:', q.peek());",
        "options": ["rear", "data", "front", "next"],
    },
    "skill_exa_test": [
        {
            "question": "What fundamental data ordering principle does a Queue follow in computer science?",
            "options": [
                "FIFO (First In, First Out)",
                "LIFO (Last In, First Out)",
                "LILO (Last In, Last Out)",
                "Random Priority Access"
            ],
            "answer": "FIFO (First In, First Out)",
        },
        {
            "question": "Why is a Linked List implementation of a Queue more efficient than a simple JavaScript Array implementation?",
            "options": [
                "Because array dequeue requires shift() which takes O(N) linear time to re-index elements, whereas Linked List dequeue takes O(1) constant time",
                "Because arrays consume double the memory of linked lists",
                "Because linked lists do not support numerical data types",
                "Because arrays cannot execute inside loops"
            ],
            "answer": "Because array dequeue requires shift() which takes O(N) linear time to re-index elements, whereas Linked List dequeue takes O(1) constant time",
        },
        {
            "question": "In a Linked List Queue, which node pointer represents the element to be dequeued next?",
            "options": [
                "front",
                "rear",
                "tail",
                "middle"
            ],
            "answer": "front",
        },
        {
            "question": "What is the time complexity of the enqueue operation in an Array-based queue using Array.prototype.push()?",
            "options": [
                "O(1)",
                "O(N)",
                "O(N²)",
                "O(log N)"
            ],
            "answer": "O(1)",
        },
        {
            "question": "What value should a Queue peek() operation return when called on an empty queue?",
            "options": [
                "null or undefined",
                "0",
                "-1",
                "Error crash exception"
            ],
            "answer": "null or undefined",
        },
    ],
}

# Override Topic 611: Queue in JavaScript - Chapter 2
JS_TOPICS[611] = {
    "id": 611,
    "title": "Queue in JavaScript - Chapter 2",
    "category": "JavaScript Data Structures",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "Chapter 2 covers Circular Queue data structures using fixed-size buffers and modulo arithmetic (index + 1) % size to reuse array memory. Includes implementations using front/rear pointers and dynamic count management.",
    "theory": "1. Concept of Circular Queue:\nIn a fixed-capacity linear array, dequeuing elements creates empty space at the beginning that cannot be reused without shifting. A Circular Queue connects the last array index back to index 0 using modulo arithmetic `(index + 1) % capacity`.\n\n2. Circular Queue with Front & Rear Pointers:\nTracks `front` and `rear` indices initialized to -1.\n- Full condition: `(rear + 1) % capacity === front`\n- Enqueue: `rear = (rear + 1) % capacity; queue[rear] = element;`\n- Dequeue: `front = (front + 1) % capacity;` (Resets to -1 when front === rear).\n\n3. Circular Queue with Dynamic Count (Without Rear Pointer):\nMaintains `front` and `count` variable. The `rear` index is computed dynamically as `(front + count) % capacity`.\n- Full condition: `count === capacity`\n- Empty condition: `count === 0`\n- Enqueue: `let rear = (front + count) % capacity; queue[rear] = elem; count++;`\n- Dequeue: `front = (front + 1) % capacity; count--;`",
    "syntax": "// Circular Queue Modulo Index Calculation\nlet nextRear = (currentRear + 1) % capacity;\nlet nextFront = (currentFront + 1) % capacity;\nlet dynamicRear = (front + count) % capacity;",
    "example": {
        "code": "class CircularQueue {\n    constructor(cap) {\n        this.capacity = cap;\n        this.queue = new Array(cap);\n        this.front = -1;\n        this.count = 0;\n    }\n    isFull() { return this.count === this.capacity; }\n    isEmpty() { return this.count === 0; }\n    enqueue(element) {\n        if (this.isFull()) return console.log('Queue is full!');\n        if (this.front === -1) this.front = 0;\n        let rear = (this.front + this.count) % this.capacity;\n        this.queue[rear] = element;\n        this.count++;\n        console.log(`${element} added to queue`);\n    }\n    dequeue() {\n        if (this.isEmpty()) return console.log('Queue is empty!');\n        const elem = this.queue[this.front];\n        this.queue[this.front] = undefined;\n        if (this.count === 1) this.front = -1;\n        else this.front = (this.front + 1) % this.capacity;\n        this.count--;\n        return elem;\n    }\n}\nlet cq = new CircularQueue(3);\ncq.enqueue(10);\ncq.enqueue(20);\ncq.enqueue(30);\nconsole.log('Dequeued:', cq.dequeue());\ncq.enqueue(40);",
        "output": "10 added to queue\n20 added to queue\n30 added to queue\nDequeued: 10\n40 added to queue",
        "explanation": "Demonstrates circular array wrapping using modulo arithmetic where index 0 is reused after dequeuing 10.",
    },
    "fill_blanks": {
        "question": "// Circular queue computes next rear index using modulo: rear = (rear + 1) % _____\n// In a count-based circular queue, the queue is full when count equals _____",
        "answers": ["capacity", "capacity"],
        "options": ["capacity", "front", "0", "-1"],
    },
    "compiler": {
        "title": "Circular Queue Sandbox",
        "question": "Complete the Circular Queue rear modulo calculation and count increment.",
        "starter_code": "class CircularQueue {\n    constructor(size) {\n        this.size = size;\n        this.queue = new Array(size);\n        this.front = 0; this.count = 0;\n    }\n    enqueue(item) {\n        if (this.count === this.size) return false;\n        let rear = (this.front + this.count) % this.____;\n        this.queue[rear] = item;\n        this.count____;\n        return true;\n    }\n}\nlet cq = new CircularQueue(5); cq.enqueue('A');\nconsole.log('Count:', cq.count);",
        "options": ["size", "++", "front", "--"],
    },
    "skill_exa_test": [
        {
            "question": "How does a Circular Queue reuse array space when elements are dequeued?",
            "options": [
                "By using modulo arithmetic (e.g. (rear + 1) % capacity) to wrap index pointers back to 0 when reaching capacity",
                "By shifting all remaining elements to index 0 using a for loop",
                "By allocating a new array of double the size automatically",
                "By deleting empty slots with garbage collection"
            ],
            "answer": "By using modulo arithmetic (e.g. (rear + 1) % capacity) to wrap index pointers back to 0 when reaching capacity",
        },
        {
            "question": "In a Circular Queue implemented with front and dynamic count, how is the rear index calculated?",
            "options": [
                "rear = (front + count) % size",
                "rear = front + size",
                "rear = count / front",
                "rear = front - count"
            ],
            "answer": "rear = (front + count) % size",
        },
        {
            "question": "What is the time complexity of enqueue() and dequeue() operations in a Circular Queue?",
            "options": [
                "O(1) constant time for both enqueue and dequeue",
                "O(N) linear time for enqueue and O(1) for dequeue",
                "O(N log N) logarithmic time",
                "O(N²) quadratic time"
            ],
            "answer": "O(1) constant time for both enqueue and dequeue",
        },
        {
            "question": "What boolean condition indicates that a Circular Queue (with capacity size and count variable) is full?",
            "options": [
                "count === size",
                "front === -1",
                "count === 0",
                "rear === front"
            ],
            "answer": "count === size",
        },
        {
            "question": "What happens to the front index pointer in a Circular Queue when the last remaining element is dequeued?",
            "options": [
                "front is reset to -1",
                "front is incremented by 10",
                "front becomes equal to capacity",
                "front throws an unhandled error"
            ],
            "answer": "front is reset to -1",
        },
    ],
}

# Override Topic 62: Sorting Algorithms - Chapter 1 (Bubble, Selection & Insertion Sort)
JS_TOPICS[62] = {
    "id": 62,
    "title": "Sorting Algorithms - Chapter 1",
    "category": "JavaScript Data Structures",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "Sorting arranges list elements in ascending or descending order. Chapter 1 covers elementary O(N²) comparison sorting algorithms: Bubble Sort, Selection Sort, and Insertion Sort.",
    "theory": "1. Introduction to Sorting:\nSorting rearranges array elements according to a comparison operator. Element swapping in modern JavaScript is cleanly written using ES6 destructuring: `[arr[i], arr[j]] = [arr[j], arr[i]]`.\n\n2. Bubble Sort:\nRepeatedly compares adjacent elements and swaps them if out of order. Larger elements 'bubble up' to the end of the array.\n- Early Exit Optimization: Uses a `swapped` boolean flag. If no swaps occur during a full pass, the array is already sorted and execution breaks.\n- Time Complexity: O(N²) worst/average time, O(N) best case (when pre-sorted). Auxiliary Space: O(1).\n\n3. Selection Sort:\nDivides the array into sorted and unsorted regions. In each iteration, it finds the index of the minimum element in the unsorted region and swaps it into its correct position.\n- Memory Efficiency: Selection Sort performs fewer memory write operations (at most N swaps) compared to Bubble or Insertion Sort.\n- Time Complexity: O(N²) across all cases (best, average, worst). Auxiliary Space: O(1).\n\n4. Insertion Sort:\nBuilds the sorted array one element at a time by extracting a `key` element and shifting all greater preceding elements to the right.\n- Characteristics: Stable, adaptive (ideal for nearly-sorted inputs), and highly efficient for small dataset sizes.\n- Time Complexity: O(N²) worst/average, O(N) best case. Auxiliary Space: O(1).",
    "syntax": "// Bubble Sort (ES6 Swap)\nif (arr[j] > arr[j + 1]) {\n    [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];\n}\n\n// Selection Sort (Min Index Swap)\nlet minIdx = i;\nif (arr[j] < arr[minIdx]) minIdx = j;\n[arr[i], arr[minIdx]] = [arr[minIdx], arr[i]];\n\n// Insertion Sort (Key Shifting)\nlet key = arr[i], j = i - 1;\nwhile (j >= 0 && arr[j] > key) {\n    arr[j + 1] = arr[j]; j--;\n}\narr[j + 1] = key;",
    "example": {
        "code": "// 1. Bubble Sort with Early Exit\nfunction bubbleSort(arr) {\n    let n = arr.length;\n    for (let i = 0; i < n; i++) {\n        let swapped = false;\n        for (let j = 0; j < n - i - 1; j++) {\n            if (arr[j] > arr[j + 1]) {\n                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];\n                swapped = true;\n            }\n        }\n        if (!swapped) break;\n    }\n    return arr;\n}\n\n// 2. Selection Sort\nfunction selectionSort(arr) {\n    let n = arr.length;\n    for (let i = 0; i < n - 1; i++) {\n        let minIdx = i;\n        for (let j = i + 1; j < n; j++) {\n            if (arr[j] < arr[minIdx]) minIdx = j;\n        }\n        [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]];\n    }\n    return arr;\n}\n\n// 3. Insertion Sort\nfunction insertionSort(arr) {\n    let n = arr.length;\n    for (let i = 1; i < n; i++) {\n        let key = arr[i], j = i - 1;\n        while (j >= 0 && arr[j] > key) {\n            arr[j + 1] = arr[j];\n            j--;\n        }\n        arr[j + 1] = key;\n    }\n    return arr;\n}\n\nconsole.log('Bubble Sort:', bubbleSort([4, 2, 8, 1]));\nconsole.log('Selection Sort:', selectionSort([64, 25, 12, 22, 11]));\nconsole.log('Insertion Sort:', insertionSort([12, 11, 13, 5, 6]));",
        "output": "Bubble Sort: [ 1, 2, 4, 8 ]\nSelection Sort: [ 11, 12, 22, 25, 64 ]\nInsertion Sort: [ 5, 6, 11, 12, 13 ]",
        "explanation": "Executes Bubble, Selection, and Insertion sort algorithms returning cleanly sorted numeric arrays in O(1) space.",
    },
    "fill_blanks": {
        "question": "// ES6 Array Swapping: [arr[j], arr[j+1]] = [arr[j+1], ____];\n// Insertion Sort shifts elements while j >= 0 and arr[j] > ____;",
        "answers": ["arr[j]", "key"],
        "options": ["arr[j]", "key", "temp", "minIdx"],
    },
    "compiler": {
        "title": "Bubble & Selection Sort Sandbox",
        "question": "Complete the Selection Sort algorithm by setting the minIdx and swap.",
        "starter_code": "function selectionSort(arr) {\n    let n = arr.length;\n    for (let i = 0; i < n - 1; i++) {\n        let minIdx = i;\n        for (let j = i + 1; j < n; j++) {\n            if (arr[j] < arr[____]) minIdx = j;\n        }\n        [arr[i], arr[minIdx]] = [arr[____], arr[i]];\n    }\n    return arr;\n}\nconsole.log(selectionSort([3, 1, 2]));",
        "options": ["minIdx", "minIdx", "i", "j"],
    },
    "skill_exa_test": [
        {
            "question": "Which elementary sorting algorithm performs the fewest memory write operations (swaps) across execution?",
            "options": [
                "Selection Sort",
                "Bubble Sort",
                "Insertion Sort",
                "Merge Sort"
            ],
            "answer": "Selection Sort",
        },
        {
            "question": "Why is Insertion Sort adaptive and often preferred for small or nearly-sorted datasets?",
            "options": [
                "Because its inner loop skips execution when elements are already in order, taking O(N) best-case linear time",
                "Because it allocates a new auxiliary array of double size",
                "Because it uses binary search trees internally",
                "Because it runs in O(1) overall time complexity"
            ],
            "answer": "Because its inner loop skips execution when elements are already in order, taking O(N) best-case linear time",
        },
        {
            "question": "What is the primary benefit of adding a `swapped` boolean flag to a Bubble Sort implementation?",
            "options": [
                "It enables early termination in O(N) time if no elements are swapped during a pass",
                "It reduces space complexity to O(0)",
                "It transforms Bubble Sort into a non-comparison sort",
                "It forces the algorithm to run in reverse"
            ],
            "answer": "It enables early termination in O(N) time if no elements are swapped during a pass",
        },
        {
            "question": "What is the Auxiliary Space complexity of Bubble Sort, Selection Sort, and Insertion Sort?",
            "options": [
                "O(1) constant auxiliary space (in-place sorting)",
                "O(N) linear space",
                "O(N log N) space",
                "O(N²) space"
            ],
            "answer": "O(1) constant auxiliary space (in-place sorting)",
        },
        {
            "question": "In Insertion Sort, what happens to elements that are greater than the current `key`?",
            "options": [
                "They are shifted one position to the right to make room for the key",
                "They are immediately deleted from the array",
                "They are multiplied by -1",
                "They are moved to the back of the queue"
            ],
            "answer": "They are shifted one position to the right to make room for the key",
        },
    ],
}

# Override Topic 621: Sorting Algorithms - Chapter 2 (Merge Sort & Quick Sort)
JS_TOPICS[621] = {
    "id": 621,
    "title": "Sorting Algorithms - Chapter 2",
    "category": "JavaScript Data Structures",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "Chapter 2 covers efficient O(N log N) Divide-and-Conquer sorting algorithms: Merge Sort (recursive splitting & merging) and Quick Sort (Lomuto & Hoare partitioning).",
    "theory": "1. Divide-and-Conquer Paradigm:\nDivide-and-conquer breaks a large sorting problem into smaller sub-problems recursively, solves the sub-problems, and merges the sorted solutions.\n\n2. Merge Sort:\nRecursively splits the array into left and right halves using `mid = Math.floor(arr.length / 2)`, sorts each half recursively, and merges them using two pointers.\n- Performance: Guaranteed O(N log N) time complexity across ALL cases (best, average, worst).\n- Auxiliary Space: O(N) extra space needed for temporary array slices created during merge operations.\n- Stability: Merge Sort is a stable sorting algorithm.\n\n3. Quick Sort (Partitioning Schemes):\nSelects a 'pivot' element and partitions elements into two sub-arrays: elements smaller than pivot and elements greater than pivot.\n- Lomuto Partition: Chooses the LAST element `arr[high]` as pivot. Maintains pointer `i = low - 1` and iterates `j` from `low` to `high - 1`. Performs more swaps and is sensitive to duplicates.\n- Hoare Partition: Chooses the FIRST element `arr[low]` as pivot. Uses two pointers starting from both ends moving toward each other. Performs fewer swaps and handles repeated values better.\n- Time Complexity: O(N log N) average/best case, O(N²) worst case (e.g. sorted array with poor pivot selection).\n- Auxiliary Space: O(log N) due to recursive call stack.",
    "syntax": "// Merge Sort Recursive Structure\nconst mid = Math.floor(arr.length / 2);\nconst left = mergeSort(arr.slice(0, mid));\nconst right = mergeSort(arr.slice(mid));\nreturn merge(left, right);\n\n// Quick Sort Lomuto Partition\nlet pivot = arr[high], i = low - 1;\nfor (let j = low; j < high; j++) {\n    if (arr[j] < pivot) {\n        i++; [arr[i], arr[j]] = [arr[j], arr[i]];\n    }\n}\n[arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];",
    "example": {
        "code": "// 1. Merge Sort\nfunction mergeSort(arr) {\n    if (arr.length <= 1) return arr;\n    const mid = Math.floor(arr.length / 2);\n    const left = mergeSort(arr.slice(0, mid));\n    const right = mergeSort(arr.slice(mid));\n    return merge(left, right);\n}\nfunction merge(left, right) {\n    let result = [], i = 0, j = 0;\n    while (i < left.length && j < right.length) {\n        if (left[i] < right[j]) { result.push(left[i]); i++; }\n        else { result.push(right[j]); j++; }\n    }\n    return result.concat(left.slice(i), right.slice(j));\n}\n\n// 2. Quick Sort (Lomuto Partition)\nfunction quickSort(arr, low = 0, high = arr.length - 1) {\n    if (low < high) {\n        let pivot = arr[high], i = low - 1;\n        for (let j = low; j < high; j++) {\n            if (arr[j] < pivot) {\n                i++;\n                [arr[i], arr[j]] = [arr[j], arr[i]];\n            }\n        }\n        [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];\n        let pi = i + 1;\n        quickSort(arr, low, pi - 1);\n        quickSort(arr, pi + 1, high);\n    }\n    return arr;\n}\n\nconsole.log('Merge Sort:', mergeSort([38, 27, 43, 3, 9, 82, 10]));\nconsole.log('Quick Sort:', quickSort([10, 7, 8, 9, 1, 5]));",
        "output": "Merge Sort: [ 3, 9, 10, 27, 38, 43, 82 ]\nQuick Sort: [ 1, 5, 7, 8, 9, 10 ]",
        "explanation": "Executes Merge Sort and Quick Sort returning correctly ordered arrays using divide-and-conquer strategies.",
    },
    "fill_blanks": {
        "question": "// Merge Sort splits array at midpoint: const mid = Math.floor(arr.length / ____);\n// Quick Sort Lomuto partition selects the _____ element of sub-array as pivot.",
        "answers": ["2", "last"],
        "options": ["2", "last", "first", "10"],
    },
    "compiler": {
        "title": "Merge Sort Sandbox",
        "question": "Complete the Merge Sort recursive divide step.",
        "starter_code": "function mergeSort(arr) {\n    if (arr.length <= 1) return arr;\n    const mid = Math.floor(arr.length / ____);\n    const left = mergeSort(arr.slice(0, ____));\n    const right = mergeSort(arr.slice(mid));\n    return merge(left, right);\n}\nfunction merge(l, r) { return [...l, ...r].sort((a,b) => a-b); }\nconsole.log(mergeSort([4, 1, 3]));",
        "options": ["2", "mid", "1", "arr"],
    },
    "skill_exa_test": [
        {
            "question": "What is the worst-case time complexity of Merge Sort?",
            "options": [
                "O(N log N)",
                "O(N²)",
                "O(N)",
                "O(log N)"
            ],
            "answer": "O(N log N)",
        },
        {
            "question": "What is the key structural difference between Lomuto and Hoare partition schemes in Quick Sort?",
            "options": [
                "Lomuto picks the last element as pivot with single-direction pointers, whereas Hoare picks the first element as pivot with two pointers moving inwards",
                "Lomuto runs in O(1) time while Hoare runs in O(N³)",
                "Lomuto uses external linked lists while Hoare uses matrices",
                "Lomuto requires multi-threading support"
            ],
            "answer": "Lomuto picks the last element as pivot with single-direction pointers, whereas Hoare picks the first element as pivot with two pointers moving inwards",
        },
        {
            "question": "Why does standard Merge Sort require O(N) auxiliary space?",
            "options": [
                "Because it allocates new sub-arrays (left and right slices) during recursion to merge halves",
                "Because it converts numbers to strings",
                "Because it creates a hash map for every element",
                "Because it stores binary trees in RAM"
            ],
            "answer": "Because it allocates new sub-arrays (left and right slices) during recursion to merge halves",
        },
        {
            "question": "Under what condition does Quick Sort exhibit its worst-case O(N²) time complexity?",
            "options": [
                "When the input array is already sorted or reverse-sorted and bad pivot choices (e.g. smallest or largest element) are consistently picked",
                "When all array elements are even numbers",
                "When the array length is a prime number",
                "When sorting floating-point numbers"
            ],
            "answer": "When the input array is already sorted or reverse-sorted and bad pivot choices (e.g. smallest or largest element) are consistently picked",
        },
        {
            "question": "Which of the following sorting algorithms is guaranteed to maintain relative ordering of equal elements (is stable)?",
            "options": [
                "Merge Sort",
                "Quick Sort (standard in-place)",
                "Heap Sort",
                "Selection Sort"
            ],
            "answer": "Merge Sort",
        },
    ],
}

# Override Topic 63: Typed Arrays in JavaScript
JS_TOPICS[63] = {
    "id": 63,
    "title": "Typed Arrays",
    "category": "JavaScript Data Structures",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "TypedArrays are array-like objects used for high-performance handling of raw binary data in JavaScript. They act as typed views over underlying fixed-length ArrayBuffer memory, widely utilized in WebGL graphics, audio processing, canvas manipulation, and network sockets.",
    "theory": "1. ArrayBuffer & TypedArray Architecture:\n- ArrayBuffer: Represents a raw, fixed-length block of binary data memory. It cannot be read or modified directly.\n- TypedArray: Provides a typed view (e.g., Int8, Uint8, Float32) over an ArrayBuffer, interpreting raw bytes into structured numeric values.\n\n2. TypedArray Variants & Memory Specifications:\n- Int8Array: Signed 8-bit integers (-128 to 127), 1 byte (C `int8_t`).\n- Uint8Array: Unsigned 8-bit integers (0 to 255), 1 byte (C `uint8_t`).\n- Uint8ClampedArray: Unsigned 8-bit integers clamped to 0-255 range (ideal for canvas pixel RGBA rendering).\n- Int16Array: Signed 16-bit integers (-32,768 to 32,767), 2 bytes (C `int16_t`).\n- Uint16Array: Unsigned 16-bit integers (0 to 65,535), 2 bytes (C `uint16_t`).\n- Int32Array: Signed 32-bit integers (-2,147,483,648 to 2,147,483,647), 4 bytes (C `int32_t`).\n- Uint32Array: Unsigned 32-bit integers (0 to 4,294,967,295), 4 bytes (C `uint32_t`).\n- Float32Array: 32-bit IEEE 754 floating point numbers, 4 bytes (C `float`).\n- Float64Array: 64-bit IEEE 754 floating point numbers, 8 bytes (C `double`).\n- BigInt64Array / BigUint64Array: 64-bit integers for 64-bit precision, 8 bytes.\n\n3. Constructor Signatures:\nTypedArray itself is abstract and cannot be directly instantiated (`new TypedArray()` throws TypeError). You instantiate a specific subtype:\n- `new Uint8Array(length)`\n- `new Uint8Array(typedArray)`\n- `new Uint8Array(arrayLikeObject)`\n- `new Uint8Array(buffer [, byteOffset [, length]])` \n\n4. Utility Methods & Properties:\n- `fill(value, start, end)`: Fills array slots with a static value.\n- `includes(value, fromIndex)`: Checks if element exists in the typed array.\n- Properties: `length`, `byteLength`, `byteOffset`, `buffer`.",
    "syntax": "// 1. Instantiating via ArrayBuffer\nconst buffer = new ArrayBuffer(16);\nconst uint8 = new Uint8Array(buffer);\n\n// 2. Instantiating via Array / Values\nconst int8 = new Int8Array([10, 20, 30, 40]);\nint8.fill(5, 1, 3); // Fills index 1 and 2 with 5\n\n// 3. Searching inside TypedArray\nlet exists = int8.includes(20);",
    "example": {
        "code": "// Example 1: Creating ArrayBuffer and viewing via Uint8Array\nconst buffer = new ArrayBuffer(8);\nconst uint8 = new Uint8Array(buffer);\nconsole.log('Uint8 Length:', uint8.length);\nconsole.log('Byte Length:', uint8.byteLength);\n\n// Example 2: Modifying with fill()\nconst int8 = new Int8Array([0, 0, 0, 0]);\nint8.fill(4, 1, 3);\nconsole.log('Filled Int8Array:', int8);\n\n// Example 3: Searching using includes()\nconst int32 = new Int32Array([10, 20, 30, 40, 50]);\nconsole.log('Includes 20?:', int32.includes(20));\nconsole.log('Includes 20 from idx 3?:', int32.includes(20, 3));",
        "output": "Uint8 Length: 8\nByte Length: 8\nFilled Int8Array: Int8Array(4) [ 0, 4, 4, 0 ]\nIncludes 20?: true\nIncludes 20 from idx 3?: false",
        "explanation": "Demonstrates initializing ArrayBuffers, creating TypedArray views, executing memory fills, and searching elements with includes().",
    },
    "fill_blanks": {
        "question": "// Raw binary memory is stored in an _____ object.\n// To create a view of 8-bit unsigned integers, we instantiate new _____Array(buffer);",
        "answers": ["ArrayBuffer", "Uint8"],
        "options": ["ArrayBuffer", "Uint8", "Int32", "MemoryBuffer"],
    },
    "compiler": {
        "title": "TypedArray Constructor & View Sandbox",
        "question": "Complete the code to create an Int32Array view over an ArrayBuffer and check includes().",
        "starter_code": "const buffer = new ArrayBuffer(16);\nconst view = new ____Array(buffer);\nview[0] = 100;\nconsole.log('Length:', view.length);\nconsole.log('Includes 100?:', view.____(100));",
        "options": ["Int32", "includes", "Uint8", "indexOf"],
    },
    "skill_exa_test": [
        {
            "question": "What is the primary purpose of JavaScript TypedArray objects?",
            "options": [
                "To provide fast, structured, array-like views over raw binary data stored in an ArrayBuffer",
                "To automatically generate HTML forms",
                "To replace standard JavaScript string operations",
                "To encrypt network traffic automatically"
            ],
            "answer": "To provide fast, structured, array-like views over raw binary data stored in an ArrayBuffer",
        },
        {
            "question": "Can the base `TypedArray` class be instantiated directly using `new TypedArray()`?",
            "options": [
                "No, TypedArray is an abstract constructor; you must instantiate specific subtypes like Uint8Array or Float32Array",
                "Yes, it creates a generic binary array of size 0",
                "Yes, but only in strict mode",
                "Yes, if an ArrayBuffer is passed as an argument"
            ],
            "answer": "No, TypedArray is an abstract constructor; you must instantiate specific subtypes like Uint8Array or Float32Array",
        },
        {
            "question": "What is the size in bytes and equivalent C type for an `Int32Array` element?",
            "options": [
                "4 bytes, equivalent to C int32_t",
                "1 byte, equivalent to C int8_t",
                "2 bytes, equivalent to C int16_t",
                "8 bytes, equivalent to C int64_t"
            ],
            "answer": "4 bytes, equivalent to C int32_t",
        },
        {
            "question": "Which TypedArray variant is specially designed for HTML Canvas image pixel manipulation to clamp out-of-bound values to the range 0-255?",
            "options": [
                "Uint8ClampedArray",
                "Int8Array",
                "Float32Array",
                "Uint32Array"
            ],
            "answer": "Uint8ClampedArray",
        },
        {
            "question": "In the call `int8.fill(4, 1, 3)`, what do the parameters `(4, 1, 3)` represent?",
            "options": [
                "Value 4 to fill, starting at index 1 up to (excluding) index 3",
                "3 elements starting from index 4 with step size 1",
                "Fill 1 to 3 elements with index value 4",
                "Set length to 4 with offset 1 and capacity 3"
            ],
            "answer": "Value 4 to fill, starting at index 1 up to (excluding) index 3",
        },
    ],
}

# Override Topic 64: WeakMap in JavaScript
JS_TOPICS[64] = {
    "id": 64,
    "title": "WeakMap",
    "category": "JavaScript Data Structures",
    "difficulty": "Advanced",
    "duration": "25 min",
    "concept": "A WeakMap is a collection of key-value pairs where keys MUST be objects and values can be any type. Keys are weakly referenced, allowing automatic garbage collection when no other references to a key object remain, preventing memory leaks.",
    "theory": "1. Weak References & Garbage Collection:\nUnlike standard Map objects, keys in a WeakMap do not hold strong references to key objects. If an object key has no other references in memory (e.g. `obj = null`), the garbage collector automatically reclaims the object and silently deletes its associated entry from the WeakMap.\n\n2. Key Constraints (Objects Only):\nOnly objects (e.g. `{}` , functions, DOM elements) can serve as keys in a WeakMap. Primitive data types (strings, numbers, booleans, symbols) throw a `TypeError` if used as keys.\n\n3. Non-Iterable & No Size Property:\nBecause garbage collection timing is non-deterministic, WeakMap is NOT iterable. It lacks `.size`, `.keys()`, `.values()`, `.entries()`, and `.forEach()`. You can only query a specific key directly if you hold a reference to that key object.\n\n4. Supported Methods:\n- `wm.set(keyObj, value)`: Adds or updates an object key-value pair.\n- `wm.get(keyObj)`: Retrieves value associated with key object (or `undefined`).\n- `wm.has(keyObj)`: Returns boolean indicating if key object exists.\n- `wm.delete(keyObj)`: Deletes key object entry (returns boolean).\n\n5. Practical Use Cases:\n- Storing private data associated with objects or class instances.\n- Managing DOM element metadata without creating memory leaks when DOM nodes are removed from the document.",
    "syntax": "const wm = new WeakMap();\nlet objKey = { id: 1 };\nwm.set(objKey, 'Secret Data');\n\nlet val = wm.get(objKey);  // 'Secret Data'\nlet exists = wm.has(objKey); // true\nwm.delete(objKey);         // deletes entry",
    "example": {
        "code": "// 1. Instantiating WeakMap\nlet weakMap = new WeakMap();\n\nlet user1 = { name: 'Pranjal' };\nlet user2 = { name: 'Pranav' };\n\n// 2. Setting values with Object Keys\nweakMap.set(user1, 'Engineer');\nweakMap.set(user2, 'Designer');\n\nconsole.log('User1 Role:', weakMap.get(user1));\nconsole.log('User2 Role:', weakMap.get(user2));\nconsole.log('Has User1?:', weakMap.has(user1));\n\n// 3. Demonstrating garbage collection potential\nuser2 = null; // Reference broken; user2 and 'Designer' entry are now eligible for GC\n\n// 4. Deleting an entry\nweakMap.delete(user1);\nconsole.log('Has User1 after delete?:', weakMap.has(user1));",
        "output": "User1 Role: Engineer\nUser2 Role: Designer\nHas User1?: true\nHas User1 after delete?: false",
        "explanation": "Demonstrates setting object keys in a WeakMap, reading values via get(), checking presence via has(), breaking object references for garbage collection, and deleting entries.",
    },
    "fill_blanks": {
        "question": "// Keys in a WeakMap MUST be of type _____.\n// WeakMap does not support iteration or the _____ property because keys can be garbage collected.",
        "answers": ["object", "size"],
        "options": ["object", "string", "size", "length"],
    },
    "compiler": {
        "title": "WeakMap Sandbox",
        "question": "Complete the WeakMap set, get, and has operations.",
        "starter_code": "const wm = new WeakMap();\nlet item = { id: 101 };\nwm.____(item, 'Active');\nconsole.log('Value:', wm.____(item));\nconsole.log('Exists?:', wm.____(item));",
        "options": ["set", "get", "has", "add"],
    },
    "skill_exa_test": [
        {
            "question": "What data type is strictly required for keys in a JavaScript WeakMap?",
            "options": [
                "Objects only (primitive values are not allowed)",
                "Strings and Numbers only",
                "Symbols and Booleans",
                "Any JavaScript data type including primitives"
            ],
            "answer": "Objects only (primitive values are not allowed)",
        },
        {
            "question": "What happens when an object key in a WeakMap has all external references set to null?",
            "options": [
                "The key object and its associated value become eligible for automatic garbage collection",
                "The WeakMap throws a TypeError crash",
                "The value is automatically converted into a string 'null'",
                "The key is permanently stored in local memory"
            ],
            "answer": "The key object and its associated value become eligible for automatic garbage collection",
        },
        {
            "question": "Why are methods like `.forEach()`, `.keys()`, `.values()`, and `.size` omitted from WeakMap?",
            "options": [
                "Because weak references mean keys can be garbage collected non-deterministically at any time, making iteration unsafe",
                "Because WeakMap uses binary buffer tree structures",
                "Because JavaScript engines restrict loops inside objects",
                "Because WeakMap is deprecated in modern ES"
            ],
            "answer": "Because weak references mean keys can be garbage collected non-deterministically at any time, making iteration unsafe",
        },
        {
            "question": "What will happen if you attempt to execute `const wm = new WeakMap(); wm.set('key', 'val');`?",
            "options": [
                "TypeError: Invalid value used as weak map key (string primitive not allowed)",
                "It successfully stores the key-value pair",
                "It converts 'key' into a Symbol automatically",
                "It returns undefined quietly"
            ],
            "answer": "TypeError: Invalid value used as weak map key (string primitive not allowed)",
        },
        {
            "question": "Which of the following methods IS supported on a WeakMap instance?",
            "options": [
                "delete(key)",
                "forEach(callback)",
                "clear()",
                "values()"
            ],
            "answer": "delete(key)",
        },
    ],
}

# Override Topic 65: WeakSet in JavaScript
JS_TOPICS[65] = {
    "id": 65,
    "title": "WeakSet",
    "category": "JavaScript Data Structures",
    "difficulty": "Advanced",
    "duration": "25 min",
    "concept": "A WeakSet is a collection of unique objects where values are weakly referenced. Objects stored in a WeakSet can be automatically garbage-collected when no longer referenced elsewhere in the application, preventing memory leaks.",
    "theory": "1. Weak References & Garbage Collection:\nObjects in a WeakSet are weakly held. If an object stored in a WeakSet has no other references in memory (e.g. `obj = null`), the JavaScript engine's garbage collector automatically reclaims the object memory and removes it from the WeakSet.\n\n2. Objects-Only Constraint:\nUnlike standard Set which can hold any primitive or object data type, WeakSet strictly requires elements to be objects (e.g., `{}` , functions, DOM elements). Passing primitives (numbers, strings, booleans) throws a `TypeError`.\n\n3. Uniqueness & Membership:\nStores only unique object references. Adding the same object reference multiple times has no effect.\n\n4. Non-Iterable & No Size Property:\nBecause garbage collection happens non-deterministically in the background, WeakSet is non-iterable. It lacks `.size`, `.clear()`, `.keys()`, `.values()`, `.entries()`, and `.forEach()`.\n\n5. Supported Methods:\n- `ws.add(valueObj)`: Appends an object to the WeakSet.\n- `ws.has(valueObj)`: Returns boolean indicating if object is a member.\n- `ws.delete(valueObj)`: Removes object from the WeakSet.\n\n6. Common Use Cases:\n- Tracking object branding / instance tagging (e.g. marking objects as 'visited' or 'processed').\n- Guarding against recursive object traversal loops without leaking object memory.",
    "syntax": "const ws = new WeakSet();\nlet obj = { id: 1 };\n\nws.add(obj);      // Adds object to set\nlet isMember = ws.has(obj); // true\nws.delete(obj);   // Removes object",
    "example": {
        "code": "// 1. Instantiating WeakSet\nlet weakSet = new WeakSet();\n\nlet obj1 = { name: 'Pranjal' };\nlet obj2 = { name: 'Pranav' };\n\n// 2. Adding objects\nweakSet.add(obj1);\nweakSet.add(obj2);\n\nconsole.log('Has obj1?:', weakSet.has(obj1)); // true\nconsole.log('Has obj2?:', weakSet.has(obj2)); // true\n\n// 3. Deleting an object reference\nweakSet.delete(obj1);\nconsole.log('Has obj1 after delete?:', weakSet.has(obj1)); // false\n\n// 4. Nullifying external reference for GC\nobj2 = null; // obj2 reference removed; eligible for automatic garbage collection\nconsole.log('Has obj2 after nullifying?:', weakSet.has(obj2)); // false",
        "output": "Has obj1?: true\nHas obj2?: true\nHas obj1 after delete?: false\nHas obj2 after nullifying?: false",
        "explanation": "Demonstrates adding object references to a WeakSet, checking presence with has(), deleting items with delete(), and nullifying external object references for automatic garbage collection.",
    },
    "fill_blanks": {
        "question": "// A WeakSet can only store elements of type _____.\n// Like WeakMap, WeakSet does NOT support iteration or the _____ property.",
        "answers": ["object", "size"],
        "options": ["object", "primitive", "size", "length"],
    },
    "compiler": {
        "title": "WeakSet Operations Sandbox",
        "question": "Complete the WeakSet add, has, and delete operations.",
        "starter_code": "const ws = new WeakSet();\nlet user = { role: 'Admin' };\nws.____(user);\nconsole.log('Has user?:', ws.____(user));\nws.____(user);\nconsole.log('Has user after delete?:', ws.has(user));",
        "options": ["add", "has", "delete", "set"],
    },
    "skill_exa_test": [
        {
            "question": "What type of elements can be stored inside a JavaScript WeakSet?",
            "options": [
                "Objects only (primitives like strings or numbers are not allowed)",
                "Primitives only",
                "Strings, Numbers, and Booleans",
                "Any valid JavaScript data type"
            ],
            "answer": "Objects only (primitives like strings or numbers are not allowed)",
        },
        {
            "question": "What happens when an object stored in a WeakSet has its external reference set to null?",
            "options": [
                "The object becomes eligible for automatic garbage collection and is removed from the WeakSet",
                "The WeakSet throws a runtime TypeError exception",
                "The WeakSet preserves a permanent reference to the object",
                "The object is converted to an empty object {}"
            ],
            "answer": "The object becomes eligible for automatic garbage collection and is removed from the WeakSet",
        },
        {
            "question": "Which of the following methods IS supported by a WeakSet instance?",
            "options": [
                "has(value)",
                "forEach(callback)",
                "clear()",
                "values()"
            ],
            "answer": "has(value)",
        },
        {
            "question": "Why does WeakSet omit the `.size` property and iteration methods like `for...of`?",
            "options": [
                "Because weak references allow the garbage collector to sweep unreferenced objects at any time, making size and iteration non-deterministic",
                "Because WeakSet uses binary search trees",
                "Because WeakSet can only contain up to 10 elements",
                "Because iteration is restricted in ES6 strict mode"
            ],
            "answer": "Because weak references allow the garbage collector to sweep unreferenced objects at any time, making size and iteration non-deterministic",
        },
        {
            "question": "What exception is thrown if you execute `const ws = new WeakSet(); ws.add(42);`?",
            "options": [
                "TypeError: Invalid value used in weak set (42 is a primitive number)",
                "RangeError: Stack overflow",
                "SyntaxError: Unexpected number",
                "No exception is thrown"
            ],
            "answer": "TypeError: Invalid value used in weak set (42 is a primitive number)",
        },
    ],
}

# Override Topic 66: Deque in JavaScript
JS_TOPICS[66] = {
    "id": 66,
    "title": "Deque",
    "category": "JavaScript Data Structures",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "A Deque (Double-Ended Queue) is a linear data structure allowing data insertion and deletion from both the front and the rear. Operations can be implemented using standard Array methods or optimized using a fixed-size Circular Array buffer with modulo pointer arithmetic for O(1) efficiency.",
    "theory": "1. Deque Mechanics & Core Operations:\nUnlike a standard Queue (FIFO) or Stack (LIFO), a Deque supports insertion and deletion at both ends:\n- addFront(element): Inserts at the front.\n- addRear(element): Inserts at the rear.\n- removeFront(): Removes and returns element from the front.\n- removeRear(): Removes and returns element from the rear.\n- peekFront() & peekRear(): Access front or rear elements without removing.\n- isEmpty() & isFull(): Check empty/full status.\n\n2. Array-Based Implementation:\nUses Array prototype methods:\n- addFront -> unshift(elem)\n- addRear -> push(elem)\n- removeFront -> shift()\n- removeRear -> pop()\nTime Complexity: Rear operations are O(1), but Front operations are O(N) due to array element re-indexing.\n\n3. Circular Array Deque Implementation (O(1) Optimization):\nUtilizes fixed capacity with `front` and `rear` pointers and modulo arithmetic:\n- Add Front: `front = (front - 1 + capacity) % capacity`\n- Remove Front: `front = (front + 1) % capacity`\n- Add Rear: `rear = (rear + 1) % capacity`\n- Remove Rear: `rear = (rear - 1 + capacity) % capacity`\nTime Complexity: Guaranteed O(1) constant time for all 4 operations at both ends!\n\n4. Real-World Applications:\n- Sliding window problems (e.g. finding max in array windows of size K).\n- Undo/Redo operation histories.\n- Work-stealing algorithm queues in concurrency engines.",
    "syntax": "// 1. Array-Based Deque\nlet deque = [];\ndeque.unshift(10); // addFront\ndeque.push(20);    // addRear\nlet front = deque.shift(); // removeFront\nlet rear = deque.pop();    // removeRear\n\n// 2. Circular Deque Pointer Math\nfront = (front - 1 + capacity) % capacity; // Add Front\nrear = (rear + 1) % capacity;             // Add Rear",
    "example": {
        "code": "// 1. Circular Deque Implementation O(1)\nclass CircularDeque {\n    constructor(capacity) {\n        this.capacity = capacity;\n        this.items = new Array(capacity);\n        this.front = -1; this.rear = -1; this.size = 0;\n    }\n    isFull() { return this.size === this.capacity; }\n    isEmpty() { return this.size === 0; }\n    addFront(element) {\n        if (this.isFull()) return console.log('Full');\n        if (this.isEmpty()) this.front = this.rear = 0;\n        else this.front = (this.front - 1 + this.capacity) % this.capacity;\n        this.items[this.front] = element; this.size++;\n    }\n    addRear(element) {\n        if (this.isFull()) return console.log('Full');\n        if (this.isEmpty()) this.front = this.rear = 0;\n        else this.rear = (this.rear + 1) % this.capacity;\n        this.items[this.rear] = element; this.size++;\n    }\n    removeFront() {\n        if (this.isEmpty()) return null;\n        let val = this.items[this.front];\n        if (this.front === this.rear) this.front = this.rear = -1;\n        else this.front = (this.front + 1) % this.capacity;\n        this.size--; return val;\n    }\n    removeRear() {\n        if (this.isEmpty()) return null;\n        let val = this.items[this.rear];\n        if (this.front === this.rear) this.front = this.rear = -1;\n        else this.rear = (this.rear - 1 + this.capacity) % this.capacity;\n        this.size--; return val;\n    }\n}\n\nlet cdq = new CircularDeque(4);\ncdq.addRear(10); cdq.addRear(20);\ncdq.addFront(5); cdq.addFront(2);\nconsole.log('Removed Front:', cdq.removeFront());\nconsole.log('Removed Rear:', cdq.removeRear());",
        "output": "Removed Front: 2\nRemoved Rear: 20",
        "explanation": "Demonstrates inserting and deleting elements at both front and rear ends of a Circular Deque operating in O(1) constant time.",
    },
    "fill_blanks": {
        "question": "// A Deque allows insertion and deletion at both the _____ and the rear.\n// Moving the front pointer backward in a Circular Deque uses: front = (front - 1 + capacity) % _____",
        "answers": ["front", "capacity"],
        "options": ["front", "middle", "capacity", "size"],
    },
    "compiler": {
        "title": "Circular Deque Sandbox",
        "question": "Complete the Circular Deque addRear and removeFront index formulas.",
        "starter_code": "class Deque {\n    constructor(cap) { this.cap = cap; this.front = 0; this.rear = 0; this.size = 0; this.buf = new Array(cap); }\n    addRear(val) {\n        this.buf[this.rear] = val;\n        this.rear = (this.rear + 1) % this.____;\n        this.size++;\n    }\n    removeFront() {\n        let val = this.buf[this.front];\n        this.front = (this.front + 1) % this.____;\n        this.size--; return val;\n    }\n}\nlet d = new Deque(5); d.addRear(42);\nconsole.log('Val:', d.removeFront());",
        "options": ["cap", "cap", "size", "front"],
    },
    "skill_exa_test": [
        {
            "question": "What defines a Deque (Double-Ended Queue) data structure?",
            "options": [
                "A linear data structure allowing insertion and deletion at both the front and rear ends",
                "A stack that only allows insertion at the front",
                "A single-ended queue where elements can only be read from the middle",
                "A multi-threaded key-value database"
            ],
            "answer": "A linear data structure allowing insertion and deletion at both the front and rear ends",
        },
        {
            "question": "In a simple JavaScript Array implementation of a Deque, why do `addFront()` (unshift) and `removeFront()` (shift) take O(N) linear time?",
            "options": [
                "Because modifying index 0 forces JavaScript to re-index all remaining elements in the array",
                "Because arrays cannot allocate memory dynamically",
                "Because unshift() deletes the array buffer",
                "Because shift() sorts the array in descending order"
            ],
            "answer": "Because modifying index 0 forces JavaScript to re-index all remaining elements in the array",
        },
        {
            "question": "What is the formula to move the `front` pointer backward when inserting at the front of a Circular Deque?",
            "options": [
                "front = (front - 1 + capacity) % capacity",
                "front = front + capacity",
                "front = (front + 1) % capacity",
                "front = front * size"
            ],
            "answer": "front = (front - 1 + capacity) % capacity",
        },
        {
            "question": "What is the time complexity of all 4 insertion and deletion operations in a Circular Array Deque?",
            "options": [
                "O(1) constant time for addFront, addRear, removeFront, and removeRear",
                "O(N) linear time for all operations",
                "O(N log N) logarithmic time",
                "O(N²) quadratic time"
            ],
            "answer": "O(1) constant time for addFront, addRear, removeFront, and removeRear",
        },
        {
            "question": "Which algorithmic problem pattern commonly relies on a Deque for optimal O(N) performance?",
            "options": [
                "Sliding Window Maximum / Minimum problems",
                "Matrix multiplication",
                "Binary search tree insertion",
                "Regular expression parsing"
            ],
            "answer": "Sliding Window Maximum / Minimum problems",
        },
    ],
}

# Override Topic 67: Priority Queue (Heap) in JavaScript
JS_TOPICS[67] = {
    "id": 67,
    "title": "Priority Queue (Heap)",
    "category": "JavaScript Data Structures",
    "difficulty": "Advanced",
    "duration": "35 min",
    "concept": "A Priority Queue processes elements based on assigned priority levels rather than strict FIFO ordering. Higher priority elements are dequeued first. While simple arrays achieve O(N) insertion time, optimized Binary Heap implementations achieve O(log N) insertion and deletion via Min Heap or Max Heap structures.",
    "theory": "1. Priority Queue Concept & Mechanics:\nIn a Priority Queue, every element has an associated priority. Elements with higher priority are dequeued before lower priority ones. If elements have equal priority, they are served according to their entry sequence.\n\n2. Array-Based Implementation (Naive):\nStores elements as `QElement(element, priority)` objects in an array. `enqueue()` iterates to insert elements in sorted order using `splice()`. \n- Time Complexity: `enqueue()` O(N), `dequeue()` O(1) or O(N). Slower for dynamic large-scale workloads.\n\n3. Binary Heap Optimization (O(log N)):\nRepresented as a 0-indexed flat array where binary tree nodes correspond to index math:\n- Left Child: `2 * i + 1`\n- Right Child: `2 * i + 2`\n- Parent Index: `Math.floor((i - 1) / 2)`\n\n4. Min Heap vs Max Heap:\n- Min Heap: Root (index 0) holds the minimum priority value (smallest number = highest priority). Bubble up (`heapifyUp`) and sift down (`heapifyDown`) maintain parent <= child invariant.\n- Max Heap: Root (index 0) holds the maximum priority value (largest number = highest priority). Inverts comparison signs in heapify methods.\n\n5. Time & Space Complexity:\n- `peek()`: O(1)\n- `add()` / `enqueue()`: O(log N)\n- `remove()` / `dequeue()`: O(log N)\n- Auxiliary Space: O(N) for array storage.",
    "syntax": "// Binary Heap Index Calculations\nlet getLeftChildIndex = (parentIdx) => 2 * parentIdx + 1;\nlet getRightChildIndex = (parentIdx) => 2 * parentIdx + 2;\nlet getParentIndex = (childIdx) => Math.floor((childIdx - 1) / 2);\n\n// Swapping Heap Nodes\n[heap[i], heap[j]] = [heap[j], heap[i]];",
    "example": {
        "code": "// Optimized Min Heap Priority Queue O(log N)\nclass MinHeapPriorityQueue {\n    constructor() { this.heap = []; }\n    getParentIndex(i) { return Math.floor((i - 1) / 2); }\n    getLeftChildIndex(i) { return 2 * i + 1; }\n    getRightChildIndex(i) { return 2 * i + 2; }\n    swap(i1, i2) { [this.heap[i1], this.heap[i2]] = [this.heap[i2], this.heap[i1]]; }\n    peek() { return this.heap.length ? this.heap[0] : null; }\n    add(item) {\n        this.heap.push(item);\n        this.heapifyUp();\n    }\n    remove() {\n        if (!this.heap.length) return null;\n        let item = this.heap[0];\n        this.heap[0] = this.heap[this.heap.length - 1];\n        this.heap.pop();\n        this.heapifyDown();\n        return item;\n    }\n    heapifyUp() {\n        let index = this.heap.length - 1;\n        while (index > 0 && this.heap[this.getParentIndex(index)] > this.heap[index]) {\n            this.swap(this.getParentIndex(index), index);\n            index = this.getParentIndex(index);\n        }\n    }\n    heapifyDown() {\n        let index = 0;\n        while (this.getLeftChildIndex(index) < this.heap.length) {\n            let smallerChildIdx = this.getLeftChildIndex(index);\n            let rightIdx = this.getRightChildIndex(index);\n            if (rightIdx < this.heap.length && this.heap[rightIdx] < this.heap[smallerChildIdx]) {\n                smallerChildIdx = rightIdx;\n            }\n            if (this.heap[index] <= this.heap[smallerChildIdx]) break;\n            this.swap(index, smallerChildIdx);\n            index = smallerChildIdx;\n        }\n    }\n}\n\nlet pq = new MinHeapPriorityQueue();\npq.add(45); pq.add(12); pq.add(65); pq.add(32);\nconsole.log('Peek Highest Priority (Min):', pq.peek());\nconsole.log('Removed Top:', pq.remove());\nconsole.log('New Top:', pq.peek());",
        "output": "Peek Highest Priority (Min): 12\nRemoved Top: 12\nNew Top: 32",
        "explanation": "Demonstrates Min Heap Priority Queue adding elements in O(log N) time and extracting the minimum element (highest priority) in O(log N) time.",
    },
    "fill_blanks": {
        "question": "// In a Binary Heap stored in an array, the left child index of parent i is computed as 2 * i + _____\n// Adding or removing an element from a Binary Heap Priority Queue takes O(_____) logarithmic time.",
        "answers": ["1", "log N"],
        "options": ["1", "2", "log N", "N"],
    },
    "compiler": {
        "title": "Min Heap Priority Queue Sandbox",
        "question": "Complete the getParentIndex and heapifyUp loop condition.",
        "starter_code": "class Heap {\n    constructor() { this.heap = []; }\n    getParent(i) { return Math.floor((i - ____) / 2); }\n    add(val) {\n        this.heap.push(val);\n        let idx = this.heap.length - 1;\n        while (idx > 0 && this.heap[this.getParent(idx)] > this.heap[idx]) {\n            let pIdx = this.getParent(idx);\n            [this.heap[pIdx], this.heap[idx]] = [this.heap[idx], this.heap[pIdx]];\n            idx = pIdx;\n        }\n    }\n}\nlet h = new Heap(); h.add(20); h.add(5);\nconsole.log('Root:', h.heap[0]);",
        "options": ["1", "2", "idx", "0"],
    },
    "skill_exa_test": [
        {
            "question": "How does a Priority Queue differ from a standard FIFO Queue?",
            "options": [
                "Elements are dequeued based on their priority level rather than arrival sequence",
                "Elements are dequeued in Last In, First Out order",
                "Priority Queue only allows string elements",
                "Priority Queue automatically deletes duplicate items"
            ],
            "answer": "Elements are dequeued based on their priority level rather than arrival sequence",
        },
        {
            "question": "What is the time complexity of add() and remove() operations in a Binary Heap-based Priority Queue?",
            "options": [
                "O(log N) logarithmic time for both add and remove",
                "O(1) constant time for both add and remove",
                "O(N) linear time for both add and remove",
                "O(N²) quadratic time"
            ],
            "answer": "O(log N) logarithmic time for both add and remove",
        },
        {
            "question": "In a 0-indexed array representation of a Binary Heap, what is the formula to locate the left child index of parent index `i`?",
            "options": [
                "2 * i + 1",
                "2 * i + 2",
                "Math.floor((i - 1) / 2)",
                "i + 2"
            ],
            "answer": "2 * i + 1",
        },
        {
            "question": "In a Min Heap Priority Queue, which element is always located at root index 0?",
            "options": [
                "The element with the minimum value (highest priority)",
                "The element with the maximum value",
                "The most recently added element",
                "A random element"
            ],
            "answer": "The element with the minimum value (highest priority)",
        },
        {
            "question": "Why is an Array-based Priority Queue using `splice()` to insert items in order considered inefficient for large dynamic workloads?",
            "options": [
                "Because inserting an element into a sorted array takes O(N) linear time due to shifting elements",
                "Because JavaScript arrays cannot hold objects with numeric priorities",
                "Because arrays cannot run inside loops",
                "Because splice() throws an exception when array length exceeds 100"
            ],
            "answer": "Because inserting an element into a sorted array takes O(N) linear time due to shifting elements",
        },
    ],
}

# Override Topic 68: Introduction to OOP in JavaScript
JS_TOPICS[68] = {
    "id": 68,
    "title": "Introduction to OOP",
    "category": "Object-Oriented Programming",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "Object-Oriented Programming (OOP) is a programming paradigm based on objects that combine data (properties) and behavior (methods). It models real-world entities through four core pillars: Abstraction, Encapsulation, Inheritance, and Polymorphism, alongside object Associations (Aggregation and Composition).",
    "theory": "1. What is Object-Oriented Programming?\nOOP structures code into reusable, modular objects containing state (data) and behavior (methods). It enforces the DRY (Don't Repeat Yourself) principle and simplifies application scalability.\n\n2. Classes and Objects:\n- Class: A user-defined template or blueprint (e.g. `class Student`).\n- Object: An instance created from a class using `new Student(...)` possessing State, Behavior, and a unique memory Identity.\n\n3. The Four Core Pillars of OOP:\n- Abstraction: Hiding internal complexity and exposing only clean interfaces. Achieved using classes, modules, closures, and private fields (`#`).\n- Encapsulation: Bundling data and methods into a single unit while restricting direct external access using private class fields (`#privateField`).\n- Inheritance: Creating a child class derived from a parent class via `extends`, sharing properties/methods (\"is-a\" relationship).\n- Polymorphism: \"Many forms\" — allowing the same method name (e.g., `speak()`) to exhibit different behaviors when overridden in child classes.\n\n4. Object Association Types:\n- Association: General relationship between independent objects.\n- Aggregation (Weak Association): Container object references another object, but both can exist independently (e.g., Company and Employee).\n- Composition (Strong Association): Container object owns child objects; if the parent object is destroyed, child objects are also destroyed (e.g., House and Room).",
    "syntax": "// Class Blueprint & Object Instantiation\nclass Animal {\n    #sound; // Encapsulated private field\n    constructor(name, sound) {\n        this.name = name;\n        this.#sound = sound;\n    }\n    makeSound() { return `${this.name} says ${this.#sound}`; }\n}\n\n// Inheritance\nclass Dog extends Animal {\n    constructor(name) { super(name, 'Woof'); }\n}\n\nconst dog = new Dog('Tommy');\nconsole.log(dog.makeSound()); // 'Tommy says Woof'",
    "example": {
        "code": "// 1. Base Class with Encapsulation & Abstraction\nclass BankAccount {\n    #balance; // Private field\n    constructor(owner, initialBalance) {\n        this.owner = owner;\n        this.#balance = initialBalance;\n    }\n    deposit(amount) {\n        if (amount > 0) this.#balance += amount;\n    }\n    getBalance() {\n        return this.#balance;\n    }\n}\n\n// 2. Inheritance & Polymorphism\nclass SavingsAccount extends BankAccount {\n    constructor(owner, balance, interestRate) {\n        super(owner, balance);\n        this.interestRate = interestRate;\n    }\n    // Polymorphic method extension\n    addInterest() {\n        let interest = this.getBalance() * this.interestRate;\n        this.deposit(interest);\n    }\n}\n\nlet acc = new SavingsAccount('Rahul', 1000, 0.05);\nacc.deposit(500);\nacc.addInterest();\nconsole.log('Account Owner:', acc.owner);\nconsole.log('Final Balance:', acc.getBalance());",
        "output": "Account Owner: Rahul\nFinal Balance: 1575",
        "explanation": "Demonstrates class creation, private field encapsulation (#balance), inheritance with super(), and polymorphism.",
    },
    "fill_blanks": {
        "question": "// Data hiding and restricted access in JS classes is achieved using private fields starting with _____.\n// A child class inherits from a parent class using the _____ keyword.",
        "answers": ["#", "extends"],
        "options": ["#", "extends", "private", "inherits"],
    },
    "compiler": {
        "title": "OOP Class & Inheritance Sandbox",
        "question": "Complete the Car class definition and Child class inheritance.",
        "starter_code": "class Vehicle {\n    constructor(brand) { this.brand = brand; }\n    start() { return `${this.brand} starting...`; }\n}\nclass ElectricCar _____ Vehicle {\n    constructor(brand, battery) {\n        _____(brand);\n        this.battery = battery;\n    }\n}\nlet tesla = new ElectricCar('Tesla', '100kWh');\nconsole.log(tesla.start());",
        "options": ["extends", "super", "implements", "this"],
    },
    "skill_exa_test": [
        {
            "question": "What are the four primary pillars of Object-Oriented Programming (OOP)?",
            "options": [
                "Abstraction, Encapsulation, Inheritance, and Polymorphism",
                "Array, Object, Function, and Symbol",
                "Push, Pop, Shift, and Unshift",
                "Compilation, Interpretation, Parsing, and Execution"
            ],
            "answer": "Abstraction, Encapsulation, Inheritance, and Polymorphism",
        },
        {
            "question": "How do you define a private field in a modern JavaScript ES6+ class to enforce Encapsulation?",
            "options": [
                "By prefixing the property name with a hash symbol (e.g., `#balance`)",
                "By writing `private balance` inside the constructor",
                "By wrapping the property in square brackets `[balance]`",
                "By setting the property to null"
            ],
            "answer": "By prefixing the property name with a hash symbol (e.g., `#balance`)",
        },
        {
            "question": "What is the key difference between Aggregation and Composition in OOP association?",
            "options": [
                "In Aggregation, child objects exist independently of the parent; in Composition, destroying the parent also destroys the child objects",
                "Aggregation requires interfaces while Composition requires abstract classes",
                "Composition only works with primitive data types",
                "Aggregation does not allow method calls"
            ],
            "answer": "In Aggregation, child objects exist independently of the parent; in Composition, destroying the parent also destroys the child objects",
        },
        {
            "question": "In JavaScript inheritance, which keyword is used by a child class constructor to invoke the parent class constructor?",
            "options": [
                "super()",
                "parent()",
                "base()",
                "this()"
            ],
            "answer": "super()",
        },
        {
            "question": "Which OOP pillar is demonstrated when a child class provides its own custom implementation of a method already defined in its parent class?",
            "options": [
                "Polymorphism (Method Overriding)",
                "Encapsulation",
                "Aggregation",
                "Compilation"
            ],
            "answer": "Polymorphism (Method Overriding)",
        },
    ],
}

# Override Topic 69: Objects & Object Constructors
JS_TOPICS[69] = {
    "id": 69,
    "title": "Objects",
    "category": "Object-Oriented Programming",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "An object in JavaScript is a non-primitive collection of key-value pairs representing properties and methods. Constructor functions combined with the `new` keyword serve as blueprints for instantiating multiple objects with unique data and shared methods.",
    "theory": "1. Object Fundamentals:\nAn object groups related state (properties) and behavior (methods) into a single entity. Keys are strings or Symbols, and values can be any data type, including functions.\n\n2. Object Creation Techniques:\n- Object Literals: `const obj = { name: 'Rahul', age: 20 };`\n- Built-in `new Object()`: `let gfg = new Object(); gfg.a = 'JavaScript';`\n- Custom Constructor Functions: Functions invoked with `new` to instantiate multiple objects.\n\n3. Constructor Function Mechanics:\nWhen a function is called with `new`:\n1. A new empty object `{}` is created.\n2. `this` inside the constructor binds to the new object instance.\n3. Properties and methods attached to `this` are assigned to the instance.\n4. The new object is returned automatically.\n\n4. Property Access & Dynamic Assignment:\n- Dot Notation: `obj.property = value;`\n- Bracket Notation: `obj['property'] = value;` (useful for dynamic property keys or strings with spaces/dashes).\n\n5. Adding Methods to Constructors:\nMethods can be attached directly inside the constructor (`this.sayHello = function() { ... }`) or via prototype.",
    "syntax": "// Constructor Function\nfunction Person(name, age) {\n    this.name = name;\n    this.age = age;\n    this.sayHello = function() {\n        return `Hello, my name is ${this.name}`;\n    };\n}\n\n// Instantiating Objects\nconst p1 = new Person('John', 25);\nconst p2 = new Person('Alice', 30);",
    "example": {
        "code": "// 1. Constructor Function\nfunction Car(brand, model) {\n    this.brand = brand;\n    this.model = model;\n    this.getDetails = function() {\n        return `${this.brand} ${this.model}`;\n    };\n}\n\n// 2. Creating multiple instances\nconst car1 = new Car('Toyota', 'Camry');\nconst car2 = new Car('Honda', 'Civic');\n\nconsole.log('Car 1 Details:', car1.getDetails());\nconsole.log('Car 2 Details:', car2.getDetails());\n\n// 3. Dynamic Property Assignment (Dot & Bracket)\ncar1.year = 2022;\ncar2['color'] = 'Red';\n\nconsole.log('Car 1 Year:', car1.year);\nconsole.log('Car 2 Color:', car2['color']);",
        "output": "Car 1 Details: Toyota Camry\nCar 2 Details: Honda Civic\nCar 1 Year: 2022\nCar 2 Color: Red",
        "explanation": "Demonstrates instantiating objects using custom constructor functions and assigning properties dynamically via dot and bracket notation.",
    },
    "fill_blanks": {
        "question": "// Constructor functions are instantiated using the _____ keyword.\n// Inside a constructor function, the _____ keyword refers to the newly created object instance.",
        "answers": ["new", "this"],
        "options": ["new", "this", "create", "self"],
    },
    "compiler": {
        "title": "Object Constructor Sandbox",
        "question": "Complete the Person constructor function and instantiate person1.",
        "starter_code": "function Person(name, role) {\n    _____.name = name;\n    this.role = role;\n    this.getInfo = function() {\n        return `${this.name}: ${this.role}`;\n    };\n}\nconst p1 = _____ Person('Amit', 'Developer');\nconsole.log(p1.getInfo());",
        "options": ["this", "new", "self", "create"],
    },
    "skill_exa_test": [
        {
            "question": "What is the primary role of a constructor function in JavaScript?",
            "options": [
                "To initialize and instantiate new object instances when called with the `new` keyword",
                "To delete unused variables from RAM",
                "To compile JavaScript code into WebAssembly",
                "To create HTTP server routes"
            ],
            "answer": "To initialize and instantiate new object instances when called with the `new` keyword",
        },
        {
            "question": "Inside a constructor function, what does the `this` keyword refer to?",
            "options": [
                "The newly created object instance",
                "The global window object always",
                "The parent HTML element",
                "The outer function file"
            ],
            "answer": "The newly created object instance",
        },
        {
            "question": "Which operator is used to access or assign object properties when property keys are stored in variables?",
            "options": [
                "Square bracket notation `obj[varKey]`",
                "Dot notation `obj.varKey`",
                "Arrow notation `obj->varKey`",
                "Colon notation `obj::varKey`"
            ],
            "answer": "Square bracket notation `obj[varKey]`",
        },
        {
            "question": "What happens when a constructor function is invoked WITHOUT the `new` keyword in non-strict mode?",
            "options": [
                "It does not create a new object; properties are accidentally attached to the global object (window/global)",
                "It automatically inserts the `new` keyword for you",
                "It throws a SyntaxError",
                "It returns null quietly"
            ],
            "answer": "It does not create a new object; properties are accidentally attached to the global object (window/global)",
        },
        {
            "question": "Can you dynamically add new properties to an object instance after it has been created from a constructor?",
            "options": [
                "Yes, using either dot notation (`obj.prop = val`) or bracket notation (`obj['prop'] = val`)",
                "No, objects created from constructors are frozen permanently",
                "Only if the constructor returns a Proxy",
                "Only in strict mode"
            ],
            "answer": "Yes, using either dot notation (`obj.prop = val`) or bracket notation (`obj['prop'] = val`)",
        },
    ],
}

# Override Topic 70: this Keyword in JavaScript
JS_TOPICS[70] = {
    "id": 70,
    "title": "this Keyword",
    "category": "Object-Oriented Programming",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "In JavaScript, the `this` keyword dynamically refers to the execution context or calling object at runtime, determined by how a function is invoked rather than where it is declared.",
    "theory": "1. Dynamic Runtime Binding of `this`:\nUnlike lexical variable scope, `this` is bound at runtime based on the function invocation context.\n\n2. Execution Context Rules for `this`:\n- Object Method (Implicit Binding): When called as an object method (`obj.method()`), `this` refers to `obj`.\n- Standalone Function (Global Context): In non-strict mode, `this` refers to the global object (`window` in browser, `global` in Node). In strict mode (`'use strict'`), `this` is `undefined`.\n- Constructor Functions (`new` Binding): `this` refers to the newly created instance.\n- Explicit Binding (`call`, `apply`, `bind`):\n  - `fn.call(thisArg, arg1, arg2)`: Immediately invokes `fn` with `this` set to `thisArg`.\n  - `fn.apply(thisArg, [args])`: Immediately invokes `fn` with arguments array.\n  - `fn.bind(thisArg)`: Returns a new function with `this` permanently bound to `thisArg`.\n- Arrow Functions (Lexical `this`): Arrow functions do NOT have their own `this`; they capture `this` from the enclosing lexical scope.\n\n3. Precedence Order of `this` Binding:\n1. `new` keyword binding (Highest Priority)\n2. Explicit binding via `bind()`, `call()`, or `apply()`\n3. Implicit binding via object method call (`obj.method()`)\n4. Default binding (Global object or `undefined` in strict mode)",
    "syntax": "// Implicit Binding\nconst person = { name: 'Ram', greet() { return `Hello ${this.name}`; } };\n\n// Explicit Binding (call, apply, bind)\nfunction showAge() { return `${this.name} is ${this.age}`; }\nshowAge.call(person); // Explicit call\n\n// Lexical this in Arrow Function\nconst obj = { val: 42, getVal: () => this.val }; // inherits outer this",
    "example": {
        "code": "// 1. Implicit Binding\nconst person = {\n    name: 'Amit',\n    age: 22,\n    greet: function() {\n        return `Hello ${this.name}, age ${this.age}`;\n    }\n};\nconsole.log('Implicit:', person.greet());\n\n// 2. Explicit Binding with call() and bind()\nfunction introduce(greeting) {\n    return `${greeting}, I am ${this.name}`;\n}\nconst user2 = { name: 'Jatin' };\nconsole.log('Call():', introduce.call(user2, 'Welcome'));\n\nconst boundIntro = introduce.bind(user2);\nconsole.log('Bind():', boundIntro('Hi'));\n\n// 3. Arrow Function Lexical this\nconst user3 = {\n    name: 'Suresh',\n    regularFn: function() { console.log('Regular Fn Name:', this.name); },\n    arrowFn: () => { console.log('Arrow Fn this.name:', this.name); }\n};\nuser3.regularFn();\nuser3.arrowFn();",
        "output": "Implicit: Hello Amit, age 22\nCall(): Welcome, I am Jatin\nBind(): Hi, I am Jatin\nRegular Fn Name: Suresh\nArrow Fn this.name: undefined",
        "explanation": "Demonstrates implicit method binding, explicit binding via call() and bind(), and lexical scope inheritance in arrow functions.",
    },
    "fill_blanks": {
        "question": "// The method that returns a new function with `this` permanently bound is _____\n// Arrow functions do NOT have their own `this`; they inherit it from their _____ scope.",
        "answers": ["bind", "lexical"],
        "options": ["bind", "call", "lexical", "global"],
    },
    "compiler": {
        "title": "this Keyword Binding Sandbox",
        "question": "Complete the explicit call() and bind() methods.",
        "starter_code": "function getRole() { return `${this.user}: ${this.role}`; }\nconst admin = { user: 'Piyush', role: 'SuperAdmin' };\nconsole.log('Call:', getRole.____(admin));\nconst fn = getRole.____(admin);\nconsole.log('Bind:', fn());",
        "options": ["call", "bind", "apply", "run"],
    },
    "skill_exa_test": [
        {
            "question": "How is the value of the `this` keyword determined in JavaScript for a regular function?",
            "options": [
                "Dynamically at runtime based on how the function is invoked",
                "Statically at compile time based on function placement",
                "It always refers to the global window object",
                "It is fixed when the file is loaded"
            ],
            "answer": "Dynamically at runtime based on how the function is invoked",
        },
        {
            "question": "What is the key difference between `.call()` and `.bind()` when setting explicit `this` binding?",
            "options": [
                "`.call()` invokes the function immediately with the specified `this`, whereas `.bind()` returns a new function with `this` permanently bound",
                "`.call()` accepts arrays while `.bind()` accepts strings",
                "`.bind()` can only be used on arrow functions",
                "`.call()` is deprecated in ES6"
            ],
            "answer": "`.call()` invokes the function immediately with the specified `this`, whereas `.bind()` returns a new function with `this` permanently bound",
        },
        {
            "question": "How do Arrow Functions handle the `this` keyword?",
            "options": [
                "Arrow functions do not have their own `this`; they inherit `this` lexically from their surrounding outer scope",
                "Arrow functions bind `this` to the window object always",
                "Arrow functions create a new object for `this` every call",
                "Arrow functions cause `this` to throw a SyntaxError"
            ],
            "answer": "Arrow functions do not have their own `this`; they inherit `this` lexically from their surrounding outer scope",
        },
        {
            "question": "In strict mode (`'use strict'`), what is the value of `this` inside a standalone regular function call?",
            "options": [
                "undefined",
                "window / global",
                "null",
                "0"
            ],
            "answer": "undefined",
        },
        {
            "question": "Which of the following has the HIGHEST priority in determining the `this` context of a function call?",
            "options": [
                "`new` keyword constructor invocation",
                "Explicit `.bind()` or `.call()`",
                "Implicit object method call (`obj.fn()`)",
                "Default global scope"
            ],
            "answer": "`new` keyword constructor invocation",
        },
    ],
}

# Override Topic 71: Prototype in JavaScript
JS_TOPICS[71] = {
    "id": 71,
    "title": "Prototype",
    "category": "Object-Oriented Programming",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "JavaScript uses a prototype-based inheritance model where objects inherit properties and methods from other objects via an internal [[Prototype]] link. Defining methods on constructor prototypes optimizes memory by sharing a single method instance across all objects.",
    "theory": "1. What is a Prototype?\nEvery JavaScript object has an internal `[[Prototype]]` link pointing to another object (its prototype). When accessing a property/method, JS searches the object itself first, then traverses up the prototype chain until the property is found or `null` is reached.\n\n2. Constructor Functions & `.prototype`:\nFunctions have a `prototype` property. When a function is called as a constructor (`new Person()`), the created instance inherits methods defined on `Person.prototype`.\n- Memory Efficiency: Methods defined inside constructor functions (`this.sayHello = ...`) duplicate in RAM per instance. Defining methods on `.prototype` stores them once in memory.\n\n3. Prototypal Inheritance Mechanics:\nObjects inherit from parent constructors by linking prototypes:\n- `Dog.prototype = Object.create(Animal.prototype);`\n- `Dog.prototype.constructor = Dog;` (resets constructor pointer).\n- `Animal.call(this, name);` (invokes parent constructor context).\n\n4. Extending Built-in Object Prototypes:\nCustom helper methods can be added to built-in prototypes like `Array.prototype.sum = function() { ... }` or `String.prototype`, making them available to all arrays/strings globally.\n\n5. Prototype Chain Traversal:\nAll standard objects eventually link to `Object.prototype`, which links to `null` (end of chain). Objects created via `Object.create(null)` have no prototype.",
    "syntax": "// Adding method to Constructor Prototype\nfunction Person(name) { this.name = name; }\nPerson.prototype.sayHello = function() {\n    return `Hello, I am ${this.name}`;\n};\n\n// Extending Built-in Prototypes\nArray.prototype.first = function() { return this[0]; };\n\n// Prototypal Inheritance\nfunction Dog(name) { Animal.call(this, name); }\nDog.prototype = Object.create(Animal.prototype);\nDog.prototype.constructor = Dog;",
    "example": {
        "code": "// 1. Constructor & Shared Prototype Method\nfunction Person(name, age) {\n    this.name = name;\n    this.age = age;\n}\nPerson.prototype.introduce = function() {\n    return `Hello, my name is ${this.name} and I am ${this.age} years old.`;\n};\n\nconst person1 = new Person('Pranjal', 25);\nconst person2 = new Person('Ayaan', 30);\nconsole.log(person1.introduce());\nconsole.log(person2.introduce());\nconsole.log('Shared Method?:', person1.introduce === person2.introduce);\n\n// 2. Extending Array Prototype\nArray.prototype.sum = function() {\n    return this.reduce((acc, curr) => acc + curr, 0);\n};\nlet nums = [1, 2, 3, 4, 5];\nconsole.log('Array Sum via Prototype:', nums.sum());\n\n// 3. Prototypal Inheritance\nfunction Animal(name) { this.name = name; }\nAnimal.prototype.speak = function() { return `${this.name} makes a noise.`; };\n\nfunction Dog(name) { Animal.call(this, name); }\nDog.prototype = Object.create(Animal.prototype);\nDog.prototype.constructor = Dog;\nDog.prototype.speak = function() { return `${this.name} barks.`; };\n\nconst rex = new Dog('Rex');\nconsole.log(rex.speak());",
        "output": "Hello, my name is Pranjal and I am 25 years old.\nHello, my name is Ayaan and I am 30 years old.\nShared Method?: true\nArray Sum via Prototype: 15\nRex barks.",
        "explanation": "Demonstrates memory-efficient prototype methods shared across instances, extending Array.prototype, and prototypal inheritance using Object.create().",
    },
    "fill_blanks": {
        "question": "// Methods attached to Constructor._____ are shared across all instances without code duplication.\n// At the top of the prototype chain, Object.prototype.__proto__ points to _____.",
        "answers": ["prototype", "null"],
        "options": ["prototype", "null", "__proto__", "undefined"],
    },
    "compiler": {
        "title": "Prototype & Extension Sandbox",
        "question": "Complete the Person prototype method definition and Array.prototype extension.",
        "starter_code": "function Person(name) { this.name = name; }\nPerson.____.sayHello = function() {\n    return `Hi, I am ${this.name}`;\n};\nArray.prototype.first = function() {\n    return this[____];\n};\nlet p = new Person('Sheema');\nconsole.log(p.sayHello());\nconsole.log([10, 20].first());",
        "options": ["prototype", "0", "__proto__", "1"],
    },
    "skill_exa_test": [
        {
            "question": "What is the main performance benefit of attaching methods to a Constructor function's `prototype` rather than inside its constructor body?",
            "options": [
                "Methods on the prototype are stored once in memory and shared by all instances, whereas methods in constructors duplicate memory for every instance",
                "Prototype methods run in WebWorker threads automatically",
                "Methods in constructors cannot access `this`",
                "Prototype methods ignore strict mode"
            ],
            "answer": "Methods on the prototype are stored once in memory and shared by all instances, whereas methods in constructors duplicate memory for every instance",
        },
        {
            "question": "What happens when JavaScript searches for a property or method on an object?",
            "options": [
                "It checks the object itself, then traverses up the prototype chain until found or reaching null",
                "It searches all global variables in the file",
                "It converts the object to a string and searches with regex",
                "It queries the backend database"
            ],
            "answer": "It checks the object itself, then traverses up the prototype chain until found or reaching null",
        },
        {
            "question": "Which function is used to link a child constructor's prototype to a parent constructor's prototype in prototypal inheritance?",
            "options": [
                "Object.create(ParentConstructor.prototype)",
                "Object.assign(ParentConstructor)",
                "Object.freeze(ParentConstructor)",
                "Object.seal(ParentConstructor)"
            ],
            "answer": "Object.create(ParentConstructor.prototype)",
        },
        {
            "question": "What is the top-most prototype link at the end of the standard JavaScript prototype chain?",
            "options": [
                "null",
                "undefined",
                "Object",
                "Window"
            ],
            "answer": "null",
        },
        {
            "question": "How can you create a completely pure dictionary object in JavaScript that does NOT inherit from `Object.prototype`?",
            "options": [
                "Object.create(null)",
                "new Object(false)",
                "Object.freeze({})",
                "new Map(null)"
            ],
            "answer": "Object.create(null)",
        },
    ],
}

# Override Topic 72: Classes in JavaScript
JS_TOPICS[72] = {
    "id": 72,
    "title": "Classes",
    "category": "Object-Oriented Programming",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "Introduced in ES6, JavaScript classes provide a clean, structured syntax for creating object blueprints, managing constructor properties, defining shared methods, and implementing class inheritance using `extends` and `super`.",
    "theory": "1. ES6 Class Declaration Syntax:\nJavaScript classes offer a syntactic sugar over prototype-based inheritance:\n```js\nclass Person {\n    constructor(name, age) {\n        this.name = name;\n        this.age = age;\n    }\n    greet() {\n        return `Hello, I am ${this.name}`;\n    }\n}\n```\nMethods declared inside a class body (like `greet()`) are automatically attached to `Person.prototype`.\n\n2. The `constructor()` Method:\nA special method automatically executed when creating an instance via `new ClassName(...)`. It initializes object properties on `this`.\n\n3. Class Inheritance (`extends` and `super`):\nClasses use `extends` to establish inheritance relationships between parent and child classes:\n- `class ElectricCar extends Car`: Derives `ElectricCar` from `Car`.\n- `super(make, model, year)`: Must be called inside the child constructor before accessing `this` to initialize parent properties.\n\n4. Method Overriding & Extension:\nA child class can override parent methods by defining a method with the same name, or extend parent functionality by calling `super.methodName()`.\n\n5. Creating Multiple Independent Instances:\nInstantiating multiple objects (`c1 = new Car(...)`, `c2 = new Car(...)`) creates separate property states per object while sharing method references.",
    "syntax": "class Car {\n    constructor(make, model, year) {\n        this.make = make;\n        this.model = model;\n        this.year = year;\n    }\n    displayInfo() {\n        return `${this.year} ${this.make} ${this.model}`;\n    }\n}\n\nclass ElectricCar extends Car {\n    constructor(make, model, year, batteryLife) {\n        super(make, model, year); // Calls parent constructor\n        this.batteryLife = batteryLife;\n    }\n    displayBattery() {\n        return `Battery Life: ${this.batteryLife} hrs`;\n    }\n}",
    "example": {
        "code": "// 1. Parent Class Definition\nclass Car {\n    constructor(make, model, year) {\n        this.make = make;\n        this.model = model;\n        this.year = year;\n    }\n    displayInfo() {\n        return `${this.year} ${this.make} ${this.model}`;\n    }\n}\n\n// 2. Child Class Inheritance\nclass ElectricCar extends Car {\n    constructor(make, model, year, batteryLife) {\n        super(make, model, year);\n        this.batteryLife = batteryLife;\n    }\n    displayBattery() {\n        return `Battery Life: ${this.batteryLife} hours`;\n    }\n}\n\n// 3. Creating Instances & Invoking Methods\nlet c1 = new Car('Toyota', 'Corolla', 2021);\nlet c2 = new Car('Honda', 'Civic', 2020);\nlet tesla = new ElectricCar('Tesla', 'Model S', 2022, 24);\n\nconsole.log('Car 1:', c1.displayInfo());\nconsole.log('Car 2:', c2.displayInfo());\nconsole.log('Tesla Info:', tesla.displayInfo());\nconsole.log('Tesla Battery:', tesla.displayBattery());",
        "output": "Car 1: 2021 Toyota Corolla\nCar 2: 2020 Honda Civic\nTesla Info: 2022 Tesla Model S\nTesla Battery: Battery Life: 24 hours",
        "explanation": "Demonstrates ES6 class syntax, constructor property initialization, inheritance via extends and super(), and creating multiple independent instances.",
    },
    "fill_blanks": {
        "question": "// The special method called automatically when creating a class instance is _____\n// A child class invokes its parent class constructor using the _____ function.",
        "answers": ["constructor", "super"],
        "options": ["constructor", "super", "init", "parent"],
    },
    "compiler": {
        "title": "Classes & Inheritance Sandbox",
        "question": "Complete the Car class constructor and ElectricCar extends declaration.",
        "starter_code": "class Car {\n    _____(make, model) {\n        this.make = make;\n        this.model = model;\n    }\n    getMake() { return this.make; }\n}\nclass EV _____ Car {\n    constructor(make, model, battery) {\n        _____(make, model);\n        this.battery = battery;\n    }\n}\nlet n = new EV('Nissan', 'Leaf', 40);\nconsole.log(n.getMake());",
        "options": ["constructor", "extends", "super", "implements"],
    },
    "skill_exa_test": [
        {
            "question": "What is a JavaScript `class` under the hood?",
            "options": [
                "Syntactic sugar over JavaScript's existing prototype-based inheritance model",
                "A low-level C++ memory struct",
                "A compiler directive that disables garbage collection",
                "A thread pooling manager"
            ],
            "answer": "Syntactic sugar over JavaScript's existing prototype-based inheritance model",
        },
        {
            "question": "What happens when you define methods inside an ES6 `class` body outside the constructor?",
            "options": [
                "They are automatically added to the class's `prototype` object",
                "They are re-created for every single instance created with new",
                "They become global functions",
                "They throw a SyntaxError unless marked as static"
            ],
            "answer": "They are automatically added to the class's `prototype` object",
        },
        {
            "question": "What is the primary function of the `super()` call inside a child class constructor?",
            "options": [
                "To execute the parent class constructor and initialize `this` context for the child instance",
                "To convert the child class into a singleton",
                "To bind event listeners to the DOM",
                "To freeze object properties against modifications"
            ],
            "answer": "To execute the parent class constructor and initialize `this` context for the child instance",
        },
        {
            "question": "What exception is thrown if a child class constructor attempts to access `this` BEFORE calling `super()`?",
            "options": [
                "ReferenceError: Must call super constructor in derived class before accessing 'this'",
                "TypeError: Cannot read property of undefined",
                "SyntaxError: Invalid keyword placement",
                "No error is thrown"
            ],
            "answer": "ReferenceError: Must call super constructor in derived class before accessing 'this'",
        },
        {
            "question": "How do multiple instances created from the same class manage state and methods?",
            "options": [
                "Each instance maintains its own separate property state, while all instances share the same method references defined on the prototype",
                "All instances share the exact same property values in global memory",
                "Methods are duplicated per instance, while properties are shared",
                "Instances cannot hold different property values"
            ],
            "answer": "Each instance maintains its own separate property state, while all instances share the same method references defined on the prototype",
        },
    ],
}

# Override Topic 73: Constructor Method in JavaScript
JS_TOPICS[73] = {
    "id": 73,
    "title": "Constructor Method",
    "category": "Object-Oriented Programming",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "A constructor in JavaScript is a special function or class method (`constructor()`) used to create and initialize objects. It binds `this` to newly created instances, sets properties, and structures instance state.",
    "theory": "1. Constructor Function & Class constructor():\nConstructors automatically execute when instantiating an object via `new`. In ES6 classes, the `constructor()` method handles instance initialization.\n\n2. Built-in vs Custom Constructors:\n- Built-in Constructors: Native constructors like `new Array()`, `new Date()`, `new Object()`.\n- Custom Constructors: Custom blueprints (`function Book(title)` or `class Person { constructor() }`).\n\n3. Constructors vs Factory Functions:\n- Constructor Functions: Require `new`, automatically bind `this` to the instance, link prototype, and return `this` implicitly.\n- Factory Functions: Regular functions returning an object directly without `new` (`function createCar() { return { brand }; }`).\n\n4. Common Constructor Mistakes:\n- Forgetting `new`: Omitting `new` in regular function constructors accidentally attaches properties to the global object or throws in strict mode.\n- Method Duplication: Defining methods inside constructor bodies duplicates functions per instance in RAM. Attaching methods to `.prototype` or class body optimizes memory.\n- Arrow Function Methods: Arrow functions inside constructors do not have their own `this` binding.",
    "syntax": "// ES6 Class Constructor\nclass Person {\n    constructor(name, age) {\n        this.name = name;\n        this.age = age;\n    }\n}\n\n// Factory Function Alternative\nfunction createPerson(name, age) {\n    return { name, age };\n}",
    "example": {
        "code": "// 1. ES6 Class Constructor\nclass Person {\n    constructor(name, age) {\n        this.name = name;\n        this.age = age;\n    }\n    greet() {\n        return `Hello, I am ${this.name} and I am ${this.age} years old.`;\n    }\n}\nconst bob = new Person('Bob', 25);\nconsole.log('Class Constructor:', bob.greet());\n\n// 2. Factory Function (Without new)\nfunction createCar(brand, model) {\n    return {\n        brand,\n        model,\n        getDetails() { return `Car: ${this.brand} ${this.model}`; }\n    };\n}\nconst ford = createCar('Ford', 'Mustang');\nconsole.log('Factory Function:', ford.getDetails());\n\n// 3. Built-in Constructors\nconst arr = new Array(1, 2, 3);\nconst date = new Date('2026-01-01');\nconsole.log('Built-in Array:', arr);\nconsole.log('Built-in Date Year:', date.getFullYear());",
        "output": "Class Constructor: Hello, I am Bob and I am 25 years old.\nFactory Function: Car: Ford Mustang\nBuilt-in Array: [ 1, 2, 3 ]\nBuilt-in Date Year: 2026",
        "explanation": "Demonstrates ES6 class constructors, factory functions without the new keyword, and built-in JavaScript constructors.",
    },
    "fill_blanks": {
        "question": "// In an ES6 class, object property initialization is placed inside the _____() method.\n// Unlike constructors, factory functions return an object directly without needing the _____ keyword.",
        "answers": ["constructor", "new"],
        "options": ["constructor", "new", "init", "create"],
    },
    "compiler": {
        "title": "Constructor & Factory Function Sandbox",
        "question": "Complete the Book class constructor and createCar factory function.",
        "starter_code": "class Book {\n    _____(title, author) {\n        this.title = title;\n        this.author = author;\n    }\n}\nfunction createCar(brand) {\n    return { brand };\n}\nlet b = _____ Book('1984', 'George Orwell');\nlet c = createCar('Tesla');\nconsole.log(b.title);\nconsole.log(c.brand);",
        "options": ["constructor", "new", "init", "create"],
    },
    "skill_exa_test": [
        {
            "question": "What happens when you instantiate a class or constructor function using the `new` keyword?",
            "options": [
                "JavaScript creates a new empty object, sets its prototype to constructor.prototype, binds `this` to the new object, and returns it",
                "JavaScript compiles the function into C binary",
                "JavaScript deletes previous instances from RAM",
                "It executes the function in a WebWorker thread"
            ],
            "answer": "JavaScript creates a new empty object, sets its prototype to constructor.prototype, binds `this` to the new object, and returns it",
        },
        {
            "question": "What is the primary difference between a Constructor Function and a Factory Function?",
            "options": [
                "Constructors require the `new` keyword and bind `this`, whereas Factory Functions return an object directly without `new`",
                "Factory Functions cannot accept parameters",
                "Constructors cannot define methods",
                "Factory Functions require ES6 class syntax"
            ],
            "answer": "Constructors require the `new` keyword and bind `this`, whereas Factory Functions return an object directly without `new`",
        },
        {
            "question": "What issue occurs when methods are declared directly inside a function constructor body using `this.greet = function() { ... }`?",
            "options": [
                "Every instance creates its own copy of the function in RAM, leading to memory inefficiency",
                "The method cannot access `this` properties",
                "It throws a TypeError at runtime",
                "It forces strict mode on the whole file"
            ],
            "answer": "Every instance creates its own copy of the function in RAM, leading to memory inefficiency",
        },
        {
            "question": "Which of the following is a built-in JavaScript constructor?",
            "options": [
                "Date()",
                "Math()",
                "JSON()",
                "Console()"
            ],
            "answer": "Date()",
        },
        {
            "question": "What happens in non-strict mode if a developer forgets the `new` keyword when calling a function constructor `Person('Alice', 30)`?",
            "options": [
                "It fails to create a new instance and accidentally assigns properties to the global object (`window` / `global`)",
                "It automatically converts into a Factory Function",
                "It throws an unhandled SyntaxError",
                "It returns an empty object {}"
            ],
            "answer": "It fails to create a new instance and accidentally assigns properties to the global object (`window` / `global`)",
        },
    ],
}

# Override Topic 74: Getters and Setters in JavaScript
JS_TOPICS[74] = {
    "id": 74,
    "title": "Getters and Setters",
    "category": "Object-Oriented Programming",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "Getters (`get`) and Setters (`set`) are accessor methods used to retrieve and update object properties with controlled logic, enabling data validation, lazy computation, and property encapsulation.",
    "theory": "1. Getter and Setter Mechanics:\n- Getter (`get prop()`): Executed automatically when reading `obj.prop`. Evaluates and returns a property value without parentheses.\n- Setter (`set prop(value)`): Executed automatically when assigning `obj.prop = value`. Intercepts property modification to validate or transform data.\n\n2. Getter vs Regular Function:\n- Getter: Accessed like a property (`obj.name`), cleaner syntax, integrates seamlessly with property assignments.\n- Regular Function: Called explicitly as a method (`obj.getName()`).\n\n3. Encapsulation with Private Fields (`#`):\nGetters and setters are commonly paired with ES2020 private class fields (`#balance`) to restrict direct external access and enforce validation rules.\n\n4. Object.defineProperty() Accessors:\nAccessors can also be dynamically defined on existing objects using `Object.defineProperty(obj, 'prop', { get(), set() })`.\n\n5. Use Cases:\n- Data Validation (e.g., rejecting negative bank balances).\n- Computed Properties (e.g., calculating rectangle area from width and height dynamically).\n- Logging and Debugging property changes.",
    "syntax": "// Class Getter and Setter\nclass Person {\n    #name;\n    constructor(name) { this.#name = name; }\n    get name() { return this.#name; }\n    set name(newName) {\n        if (newName) this.#name = newName;\n    }\n}\n\n// Object Literal Accessor\nconst obj = {\n    _val: 10,\n    get val() { return this._val; },\n    set val(v) { this._val = v; }\n};",
    "example": {
        "code": "// 1. Class Accessors with Data Validation & Private Fields\nclass BankAccount {\n    #balance;\n    constructor(initialBalance) {\n        this.#balance = initialBalance;\n    }\n    get balance() {\n        return `$${this.#balance}`;\n    }\n    set balance(amount) {\n        if (amount < 0) {\n            console.log('Validation Error: Balance cannot be negative!');\n        } else {\n            this.#balance = amount;\n        }\n    }\n}\nconst acc = new BankAccount(1000);\nconsole.log('Current Balance:', acc.balance);\nacc.balance = -500; // Triggers validation error!\nacc.balance = 2500;\nconsole.log('Updated Balance:', acc.balance);\n\n// 2. Computed Property (Rectangle Area)\nclass Rectangle {\n    constructor(width, height) {\n        this.width = width;\n        this.height = height;\n    }\n    get area() {\n        return this.width * this.height;\n    }\n}\nconst rect = new Rectangle(10, 5);\nconsole.log('Calculated Area:', rect.area);",
        "output": "Current Balance: $1000\nValidation Error: Balance cannot be negative!\nUpdated Balance: $2500\nCalculated Area: 50",
        "explanation": "Demonstrates getters and setters providing balance validation on private #balance fields alongside computed rectangle area getters.",
    },
    "fill_blanks": {
        "question": "// The keyword used to define a property getter method is _____\n// The keyword used to define a property setter method is _____.",
        "answers": ["get", "set"],
        "options": ["get", "set", "fetch", "put"],
    },
    "compiler": {
        "title": "Getters & Setters Sandbox",
        "question": "Complete the Person class getter and setter methods.",
        "starter_code": "class User {\n    constructor(name) { this._name = name; }\n    _____ name() {\n        return this._name;\n    }\n    _____ name(newName) {\n        if (newName.length > 0) this._name = newName;\n    }\n}\nlet u = new User('Anjali');\nu.name = 'Ayushi';\nconsole.log(u.name);",
        "options": ["get", "set", "fetch", "assign"],
    },
    "skill_exa_test": [
        {
            "question": "How are JavaScript getters invoked when reading a property?",
            "options": [
                "Automatically like a regular property (e.g. `obj.prop`) without parentheses",
                "Explicitly like a method call `obj.prop()`",
                "Via the `new` keyword",
                "Using `Object.get(obj)`"
            ],
            "answer": "Automatically like a regular property (e.g. `obj.prop`) without parentheses",
        },
        {
            "question": "What is the primary advantage of using a setter method over direct property assignment?",
            "options": [
                "Setters allow data validation, encapsulation, and logging before modifying internal property state",
                "Setters increase execution speed by 10x",
                "Setters prevent objects from being garbage collected",
                "Setters automatically convert objects to JSON"
            ],
            "answer": "Setters allow data validation, encapsulation, and logging before modifying internal property state",
        },
        {
            "question": "In ES2020+, how can getters and setters work with truly private class properties?",
            "options": [
                "By pairing them with private class fields starting with a hash symbol (e.g., `#balance`)",
                "By marking properties with the `protected` keyword",
                "By storing properties in local storage",
                "By freezing the class constructor"
            ],
            "answer": "By pairing them with private class fields starting with a hash symbol (e.g., `#balance`)",
        },
        {
            "question": "What happens if a property has a `get` accessor defined but NO `set` accessor, and code attempts to assign a value `obj.prop = 10` in strict mode?",
            "options": [
                "TypeError: Cannot set property which has only a getter",
                "It converts the getter into a regular variable",
                "It deletes the property from the object",
                "It silently overwrites the getter method"
            ],
            "answer": "TypeError: Cannot set property which has only a getter",
        },
        {
            "question": "Which built-in Object method allows defining getters and setters dynamically on existing objects?",
            "options": [
                "Object.defineProperty(obj, prop, descriptor)",
                "Object.assign(obj, prop)",
                "Object.create(obj, prop)",
                "Object.freeze(obj, prop)"
            ],
            "answer": "Object.defineProperty(obj, prop, descriptor)",
        },
    ],
}

# Override Topic 75: Static Methods in JavaScript
JS_TOPICS[75] = {
    "id": 75,
    "title": "Static Methods",
    "category": "Object-Oriented Programming",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "Static methods and static properties are defined directly on the class constructor using the `static` keyword. They are called directly on the class itself rather than on instantiated objects, serving as utility functions or shared class-level state.",
    "theory": "1. Static Methods & Properties Definition:\nDeclared inside a class body using the `static` keyword:\n```js\nclass MathUtils {\n    static add(a, b) { return a + b; }\n}\n```\n- Invocation: Called on the class (`MathUtils.add(5, 3)`), NOT on instances (`const m = new MathUtils(); m.add(5, 3)` throws TypeError).\n\n2. Characteristics of Static Methods:\n- Class-Bound Context: Inside a static method, `this` refers to the **class constructor function itself**, not an instance object.\n- No Direct Access to Instance State: Static methods cannot access instance properties (`this.name`) unless an instance is passed as an argument.\n\n3. Common Design Patterns:\n- Utility / Helper Methods: Pure functions perform calculations or operations independently of instance state (e.g., `Math.max()`).\n- Class-Level Counters & State: Managing shared state across all instances (e.g. `static ID = 1; constructor() { this.id = Children.ID++; }`).\n- Factory Method Pattern: Creating class instances with custom initialization logic (`User.createUser('Ajay', 30)`).\n- Singleton Pattern: Ensuring only one instance of a class exists across the application (`DB.getInstance()`).",
    "syntax": "class ClassName {\n    static staticProperty = 'Shared Data';\n    static staticMethod() {\n        return 'Class Level Function';\n    }\n}\n\n// Calling Static Members\nconsole.log(ClassName.staticProperty);\nconsole.log(ClassName.staticMethod());",
    "example": {
        "code": "// 1. Static Utility Methods\nclass MathUtils {\n    static add(a, b) { return a + b; }\n    static multiply(a, b) { return a * b; }\n}\nconsole.log('Static Add:', MathUtils.add(5, 3));\nconsole.log('Static Multiply:', MathUtils.multiply(4, 6));\n\n// 2. Class-Level Counter with Static Property\nclass Child {\n    static ID_COUNTER = 1;\n    constructor(name) {\n        this.name = name;\n        this.id = Child.ID_COUNTER++;\n    }\n}\nlet c1 = new Child('Emma');\nlet c2 = new Child('James');\nconsole.log('Child 1 ID:', c1.id);\nconsole.log('Child 2 ID:', c2.id);\nconsole.log('Next Static ID:', Child.ID_COUNTER);\n\n// 3. Factory Method Pattern\nclass User {\n    constructor(name, role) {\n        this.name = name;\n        this.role = role;\n    }\n    static createAdmin(name) {\n        return new User(name, 'Admin');\n    }\n}\nconst admin = User.createAdmin('Ajay');\nconsole.log('Admin User:', admin);",
        "output": "Static Add: 8\nStatic Multiply: 24\nChild 1 ID: 1\nChild 2 ID: 2\nNext Static ID: 3\nAdmin User: User { name: 'Ajay', role: 'Admin' }",
        "explanation": "Demonstrates static utility functions, static class-level ID counters, and the static Factory Method pattern.",
    },
    "fill_blanks": {
        "question": "// Methods and properties declared with the _____ keyword belong to the class constructor itself.\n// Static methods are invoked directly on the _____ name, not on object instances.",
        "answers": ["static", "class"],
        "options": ["static", "class", "instance", "prototype"],
    },
    "compiler": {
        "title": "Static Methods & Factory Pattern Sandbox",
        "question": "Complete the static factory method and static utility method.",
        "starter_code": "class Calculator {\n    _____ add(a, b) { return a + b; }\n    static create() {\n        return new Calculator();\n    }\n}\nconsole.log('Add:', Calculator.add(10, 20));\nlet calc = Calculator.create();",
        "options": ["static", "class", "function", "public"],
    },
    "skill_exa_test": [
        {
            "question": "How are static methods invoked in JavaScript?",
            "options": [
                "Directly on the class name (e.g. `ClassName.staticMethod()`)",
                "On instantiated objects created with `new` (e.g. `instance.staticMethod()`)",
                "Via the `super` keyword inside constructors only",
                "Using `Object.call(staticMethod)`"
            ],
            "answer": "Directly on the class name (e.g. `ClassName.staticMethod()`)",
        },
        {
            "question": "Inside a static method, what does the `this` keyword refer to?",
            "options": [
                "The class constructor function itself",
                "The individual instance object",
                "The global window object always",
                "undefined"
            ],
            "answer": "The class constructor function itself",
        },
        {
            "question": "What happens if you attempt to call a static method on a class instance `const p = new Person(); p.staticMethod();`?",
            "options": [
                "TypeError: p.staticMethod is not a function",
                "It executes normally",
                "It converts the static method into an instance method",
                "It returns undefined quietly"
            ],
            "answer": "TypeError: p.staticMethod is not a function",
        },
        {
            "question": "Which software design pattern uses static methods to control object instantiation and enforce a single shared instance across the app?",
            "options": [
                "Singleton Pattern",
                "Decorator Pattern",
                "Observer Pattern",
                "Adapter Pattern"
            ],
            "answer": "Singleton Pattern",
        },
        {
            "question": "What is a primary use case for static properties in a JavaScript class?",
            "options": [
                "Storing shared class-level state, such as auto-incrementing ID counters or global configuration defaults",
                "Storing unique per-instance user names",
                "Overriding CSS styles dynamically",
                "Binding HTML event listeners"
            ],
            "answer": "Storing shared class-level state, such as auto-incrementing ID counters or global configuration defaults",
        },
    ],
}

# Override Topic 76: JavaScript Inheritance
JS_TOPICS[76] = {
    "id": 76,
    "title": "Inheritance",
    "category": "Object-Oriented Programming",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "Inheritance is a fundamental OOP mechanism allowing derived classes or objects to acquire properties and methods from a base entity, promoting code reusability, modularity, and hierarchical relationships.",
    "theory": "1. What is Inheritance in JavaScript?\nInheritance allows one object or class to inherit characteristics (properties and methods) from another parent object or class. This eliminates code duplication and supports method overriding.\n\n2. Prototype-Based Inheritance (ES5):\nJavaScript natively uses prototype delegation. To link child constructor functions to parent constructors:\n- Call Parent Constructor: `Parent.call(this, arg)` inside the child constructor to inherit instance properties.\n- Link Prototype Chain: `Child.prototype = Object.create(Parent.prototype);` \n- Reset Constructor Pointer: `Child.prototype.constructor = Child;` \n\n3. ES6 Class-Based Inheritance (`extends` & `super`):\nES6 provides clean class syntax over prototype inheritance:\n- `extends` Keyword: Connects child class to parent class (`class Dog extends Animal`).\n- `super()` Function: Invokes parent constructor. Must be called before referencing `this` in child constructors.\n- Method Overriding: Child classes redefine parent methods to customize behavior.\n\n4. Mixins (`Object.assign()`):\nMixins allow a constructor or object to inherit methods from multiple source objects without deep hierarchical chains:\n`Object.assign(Person.prototype, walkMixin, speakMixin);` \n\n5. Inheritance via `Object.create()` & `Object.setPrototypeOf()`:\n- `Object.create(proto)`: Instantiates a new object linked directly to `proto`.\n- `Object.setPrototypeOf(obj1, obj2)`: Dynamically mutates the prototype of `obj1` to point to `obj2`.",
    "syntax": "// ES6 Class Inheritance\nclass Animal {\n    constructor(name) { this.name = name; }\n    speak() { return `${this.name} makes a sound.`; }\n}\n\nclass Dog extends Animal {\n    constructor(name, breed) {\n        super(name);\n        this.breed = breed;\n    }\n    speak() { return `${this.name} barks: Woof!`; }\n}\n\n// Prototypal Inheritance\nfunction Parent(name) { this.name = name; }\nParent.prototype.greet = function() { return `Hello ${this.name}`; };\nfunction Child(name) { Parent.call(this, name); }\nChild.prototype = Object.create(Parent.prototype);\nChild.prototype.constructor = Child;",
    "example": {
        "code": "// 1. ES6 Class Inheritance (extends & super)\nclass Animal {\n    constructor(name) {\n        this.name = name;\n    }\n    speak() {\n        return `${this.name} makes a sound.`;\n    }\n}\nclass Dog extends Animal {\n    constructor(name, breed) {\n        super(name);\n        this.breed = breed;\n    }\n    speak() {\n        return `${this.name} (${this.breed}) barks: Woof!`;\n    }\n}\nconst myDog = new Dog('Buddy', 'Golden Retriever');\nconsole.log('Class Inheritance:', myDog.speak());\n\n// 2. Prototypal Inheritance with Object.create()\nlet parentObj = {\n    role: 'User',\n    getRole() { return `Role: ${this.role}`; }\n};\nlet childObj = Object.create(parentObj);\nchildObj.name = 'Pranjal';\nconsole.log('Object.create():', childObj.getRole(), '| Name:', childObj.name);\n\n// 3. Multiple Inheritance via Mixins (Object.assign)\nconst canWalk = { walk() { return `${this.name} walks.`; } };\nconst canSpeak = { talk() { return `${this.name} talks.`; } };\nfunction Person(name) { this.name = name; }\nObject.assign(Person.prototype, canWalk, canSpeak);\nconst p1 = new Person('Rahul');\nconsole.log('Mixin Walk:', p1.walk());\nconsole.log('Mixin Talk:', p1.talk());",
        "output": "Class Inheritance: Buddy (Golden Retriever) barks: Woof!\nObject.create(): Role: User | Name: Pranjal\nMixin Walk: Rahul walks.\nMixin Talk: Rahul talks.",
        "explanation": "Demonstrates ES6 class inheritance with super(), prototype delegation using Object.create(), and combining multiple behavior mixins via Object.assign().",
    },
    "fill_blanks": {
        "question": "// In ES6 classes, a child class uses the _____ keyword to inherit from a parent class.\n// Inside the child constructor, the _____() function must be called to execute the parent constructor.",
        "answers": ["extends", "super"],
        "options": ["extends", "super", "implements", "parent"],
    },
    "compiler": {
        "title": "Inheritance & Prototype Chain Sandbox",
        "question": "Complete the Dog class inheritance from Animal.",
        "starter_code": "class Animal {\n    constructor(name) { this.name = name; }\n    speak() { return 'Animal Sound'; }\n}\nclass Dog _____ Animal {\n    constructor(name) {\n        _____(name);\n    }\n}\nlet d = new Dog('Buddy');\nconsole.log(d.name);",
        "options": ["extends", "super", "inherits", "parent"],
    },
    "skill_exa_test": [
        {
            "question": "Which ES6 keyword is used by a child class to inherit properties and methods from a parent class?",
            "options": ["extends", "inherits", "implements", "prototype"],
            "answer": "extends",
        },
        {
            "question": "Why must `super()` be called inside a derived class constructor before referencing `this`?",
            "options": [
                "It initializes the parent class constructor and binds the parent instance scope to `this`",
                "It converts the child class into a singleton",
                "It prevents memory leaks in garbage collection",
                "It disables strict mode in the derived class"
            ],
            "answer": "It initializes the parent class constructor and binds the parent instance scope to `this`",
        },
        {
            "question": "In prototypal inheritance (ES5), which method creates a new object with its prototype set to an existing parent prototype object?",
            "options": [
                "Object.create(Parent.prototype)",
                "Object.assign(Parent.prototype)",
                "Object.freeze(Parent.prototype)",
                "Object.seal(Parent.prototype)"
            ],
            "answer": "Object.create(Parent.prototype)",
        },
        {
            "question": "How can JavaScript classes simulate multiple inheritance by sharing functionality across unrelated objects?",
            "options": [
                "Using Mixins with `Object.assign(TargetClass.prototype, mixin1, mixin2)`",
                "Using multiple `extends` keywords (`class Child extends A, B`)",
                "Using global variables inside constructors",
                "Using arrow functions in static blocks"
            ],
            "answer": "Using Mixins with `Object.assign(TargetClass.prototype, mixin1, mixin2)`",
        },
        {
            "question": "What does `Object.setPrototypeOf(obj1, obj2)` do?",
            "options": [
                "Dynamically sets the prototype (`[[Prototype]]`) of `obj1` to point to `obj2`",
                "Merges all key-value pairs from `obj2` into `obj1`",
                "Creates a deep clone of `obj2`",
                "Freezes `obj1` so properties cannot be added"
            ],
            "answer": "Dynamically sets the prototype (`[[Prototype]]`) of `obj1` to point to `obj2`",
        },
    ],
}

# Override Topic 77: Encapsulation in JavaScript
JS_TOPICS[77] = {
    "id": 77,
    "title": "Encapsulation",
    "category": "Object-Oriented Programming",
    "difficulty": "Advanced",
    "duration": "25 min",
    "concept": "Encapsulation is the practice of bundling data (properties) and methods within a single unit while restricting direct external access to internal state, enforcing controlled data access through public interfaces.",
    "theory": "1. What is Encapsulation?\nEncapsulation hides the internal state and implementation details of an object from external inspection. Access to private data is strictly controlled through exposed getter and setter public methods.\n\n2. Encapsulation Techniques in JavaScript:\na. Closures (Factory Functions / Function Constructors):\n   - Variables declared with `let` or `const` inside a function remain private to that function scope.\n   - Public methods exposed via returned object literal maintain closure access to private variables.\nb. Underscore Naming Convention (`_property`):\n   - Soft privacy convention where programmers prefix properties with `_` to signal that it should be treated as private. It does NOT enforce true privacy.\nc. Private Class Fields (`#field` - ES2020):\n   - Language-enforced true privacy. Accessing `obj.#field` from outside the class throws a `SyntaxError`.\n\n3. Public Getter and Setter Methods:\nPublic methods (e.g. `deposit()`, `withdraw()`, `getBalance()`) validate inputs before updating internal state, protecting objects from invalid state corruptions (e.g., negative bank balances).",
    "syntax": "// True Encapsulation with ES2020 Private Fields (#)\nclass BankAccount {\n    #balance; // Private field\n    constructor(balance) {\n        this.#balance = balance;\n    }\n    deposit(amount) {\n        if (amount > 0) this.#balance += amount;\n    }\n    getBalance() {\n        return this.#balance;\n    }\n}\n\n// Encapsulation with Closures\nfunction createAccount(initialBalance) {\n    let balance = initialBalance; // Private closure variable\n    return {\n        getBalance: () => balance,\n        deposit: (amt) => { if (amt > 0) balance += amt; }\n    };\n}",
    "example": {
        "code": "// 1. True Privacy using ES2020 Private Class Fields (#)\nclass BankAccount {\n    #accNum;\n    #balance;\n    constructor(accNum, balance) {\n        this.#accNum = accNum;\n        this.#balance = balance;\n    }\n    deposit(amount) {\n        if (amount > 0) {\n            this.#balance += amount;\n            console.log(`Deposited $${amount}`);\n        }\n    }\n    withdraw(amount) {\n        if (amount > 0 && amount <= this.#balance) {\n            this.#balance -= amount;\n            console.log(`Withdrew $${amount}`);\n        } else {\n            console.log('Transaction Declined: Insufficient Funds');\n        }\n    }\n    getBalance() {\n        return `$${this.#balance}`;\n    }\n}\nconst myAccount = new BankAccount('12345', 1000);\nmyAccount.deposit(500);\nmyAccount.withdraw(2000); // Declined\nmyAccount.withdraw(300);\nconsole.log('Final Account Balance:', myAccount.getBalance());\n\n// 2. Closure-Based Encapsulation\nfunction createStudent(name, mark) {\n    let _mark = mark; // Private variable\n    return {\n        name,\n        getMark: () => _mark,\n        setMark: (newMark) => { if (newMark >= 0 && newMark <= 100) _mark = newMark; }\n    };\n}\nconst student = createStudent('Rahul', 85);\nstudent.setMark(92);\nconsole.log(`Student ${student.name} Mark:`, student.getMark());",
        "output": "Deposited $500\nTransaction Declined: Insufficient Funds\nWithdrew $300\nFinal Account Balance: $1200\nStudent Rahul Mark: 92",
        "explanation": "Demonstrates strict encapsulation using ES2020 private class fields (#balance) and function closure variables for safe state mutation.",
    },
    "fill_blanks": {
        "question": "// True language-enforced private class fields in JavaScript are declared using the _____ prefix.\n// Encapsulation protects object state by restricting direct access and exposing controlled _____ methods.",
        "answers": ["#", "public"],
        "options": ["#", "public", "_", "static"],
    },
    "compiler": {
        "title": "Encapsulation & Private Fields Sandbox",
        "question": "Complete the BankAccount class with private balance encapsulation.",
        "starter_code": "class BankAccount {\n    _____balance;\n    constructor(bal) {\n        this.#balance = bal;\n    }\n    getBalance() {\n        return this._____balance;\n    }\n}\nlet a = new BankAccount(500);\nconsole.log(a.getBalance());",
        "options": ["#", "#", "_", "private"],
    },
    "skill_exa_test": [
        {
            "question": "What is the main goal of Encapsulation in Object-Oriented Programming?",
            "options": [
                "Hiding internal implementation details and protecting object state from direct external modification",
                "Converting JavaScript code into WebAssembly binary",
                "Enabling multi-threaded execution in Node.js",
                "Allowing direct manipulation of global variables"
            ],
            "answer": "Hiding internal implementation details and protecting object state from direct external modification",
        },
        {
            "question": "How are true private properties declared in ES2020+ JavaScript classes?",
            "options": [
                "By prefixing property names with a hash symbol (e.g. `#balance`)",
                "By prefixing property names with an underscore (e.g. `_balance`)",
                "By using the `private` keyword before variable declarations",
                "By wrapping properties in `Object.freeze()`"
            ],
            "answer": "By prefixing property names with a hash symbol (e.g. `#balance`)",
        },
        {
            "question": "What happens if external code attempts to access a private field directly `console.log(account.#balance)` outside its class body?",
            "options": [
                "JavaScript throws a SyntaxError",
                "It returns undefined quietly",
                "It automatically converts `#balance` into a public property",
                "It returns null"
            ],
            "answer": "JavaScript throws a SyntaxError",
        },
        {
            "question": "Does the underscore naming convention `this._name` provide true data privacy in JavaScript?",
            "options": [
                "No, it is purely a developer convention and the property remains publicly accessible",
                "Yes, V8 engine blocks access to any property starting with `_`",
                "Yes, but only in strict mode",
                "No, it converts the property into a symbol"
            ],
            "answer": "No, it is purely a developer convention and the property remains publicly accessible",
        },
        {
            "question": "How can closure scope be used to achieve encapsulation in pre-ES6 JavaScript?",
            "options": [
                "By declaring variables inside a function constructor/factory function and exposing getter/setter methods in the returned object",
                "By creating global variables inside `window`",
                "By storing properties inside array indices",
                "By exporting variables via CommonJS `module.exports`"
            ],
            "answer": "By declaring variables inside a function constructor/factory function and exposing getter/setter methods in the returned object",
        },
    ],
}

# Override Topic 78: Abstraction in JavaScript
JS_TOPICS[78] = {
    "id": 78,
    "title": "Abstraction",
    "category": "Object-Oriented Programming",
    "difficulty": "Advanced",
    "duration": "25 min",
    "concept": "Abstraction is an OOP principle that simplifies complex systems by hiding internal execution logic and exposing only simple, high-level interfaces for users to interact with.",
    "theory": "1. What is Abstraction in JavaScript?\nAbstraction focuses on *what* an object does rather than *how* it performs its internal operations. It hides complex inner algorithms (such as boiling water, database connections, or encryption algorithms) behind intuitive method names (like `makeCoffee()`, `save()`, or `encrypt()`).\n\n2. Key Benefits of Abstraction:\n- Simplified Complexity: Users interact with high-level functions without needing to understand underlying machinery.\n- Code Modularity & Maintainability: Internal implementation changes do not break external calling code.\n- Enhanced Security: Protects sensitive algorithms and structural logic from direct manipulation.\n- Reusability: Clean interfaces encourage code reuse across modules.\n\n3. Achieving Abstraction in JavaScript:\na. Via Functions: Encapsulating complex calculations inside functions (e.g. `calculateCircleArea(radius)` hides `Math.PI * r^2`).\nb. Via Class Private Methods (`#privateMethod()`): Marking internal helper methods as private so users only invoke high-level public trigger methods.\nc. Via Objects & Modules: Exposing high-level methods on objects while hiding private variables and helper functions inside module scope.\n\n4. Real-World Use Cases of Abstraction:\n- API Interfaces (Fetch / Axios abstraction).\n- Database ORMs (Work with `User.find()` instead of raw SQL queries).\n- Web Server Middleware (Abstracting authentication/logging).\n- Security & Encryption (Abstracting AES key generation into `encryptData()`).",
    "syntax": "// Abstraction using Class Private Methods\nclass CoffeeMachine {\n    makeCoffee() {\n        this.#boilWater();\n        this.#brewCoffee();\n        return 'Coffee is ready!';\n    }\n    #boilWater() { /* Internal logic */ }\n    #brewCoffee() { /* Internal logic */ }\n}\n\nconst machine = new CoffeeMachine();\nmachine.makeCoffee();",
    "example": {
        "code": "// 1. Class Abstraction with Private Helper Methods\nclass CoffeeMachine {\n    makeCoffee() {\n        this.#boilWater();\n        this.#brewCoffee();\n        return 'Hot Espresso Coffee is ready!';\n    }\n    #boilWater() {\n        console.log('Step 1: Boiling water to 95°C...');\n    }\n    #brewCoffee() {\n        console.log('Step 2: Brewing ground coffee beans...');\n    }\n}\nconst coffeeApp = new CoffeeMachine();\nconsole.log(coffeeApp.makeCoffee());\n\n// 2. High-Level Function Abstraction\nfunction calculateCircleArea(radius) {\n    return Math.PI * radius * radius;\n}\nconsole.log('Calculated Circle Area:', calculateCircleArea(5).toFixed(2));\n\n// 3. Database Access Abstraction (Mock ORM)\nclass UserORM {\n    saveUser(username) {\n        let query = this.#buildSQLQuery(username);\n        return this.#executeDatabaseQuery(query);\n    }\n    #buildSQLQuery(user) {\n        return `INSERT INTO users VALUES ('${user}')`;\n    }\n    #executeDatabaseQuery(sql) {\n        return `Executing: ${sql} -> SUCCESS`;\n    }\n}\nconst db = new UserORM();\nconsole.log(db.saveUser('Anjali'));",
        "output": "Step 1: Boiling water to 95°C...\nStep 2: Brewing ground coffee beans...\nHot Espresso Coffee is ready!\nCalculated Circle Area: 78.54\nExecuting: INSERT INTO users VALUES ('Anjali') -> SUCCESS",
        "explanation": "Demonstrates abstraction by hiding low-level steps (#boilWater, #buildSQLQuery) while providing clean high-level public APIs (makeCoffee, saveUser).",
    },
    "fill_blanks": {
        "question": "// Abstraction hides internal complex logic and exposes only essential _____ to the user.\n// In JavaScript classes, internal helper methods can be hidden using _____ private method declarations.",
        "answers": ["interfaces", "#"],
        "options": ["interfaces", "#", "variables", "_"],
    },
    "compiler": {
        "title": "Abstraction & Private Helper Methods Sandbox",
        "question": "Complete the CoffeeMachine class abstraction.",
        "starter_code": "class CoffeeMachine {\n    makeCoffee() {\n        this._____boilWater();\n        return 'Coffee Ready';\n    }\n    _____boilWater() {\n        console.log('Boiling...');\n    }\n}\nlet c = new CoffeeMachine();\nconsole.log(c.makeCoffee());",
        "options": ["#", "#", "_", "public"],
    },
    "skill_exa_test": [
        {
            "question": "What is the core concept of Abstraction in JavaScript?",
            "options": [
                "Hiding complex internal implementation details and presenting a simplified interface to the user",
                "Preventing classes from inheriting parent methods",
                "Encrypting source code before browser execution",
                "Compiling JavaScript into machine assembly code"
            ],
            "answer": "Hiding complex internal implementation details and presenting a simplified interface to the user",
        },
        {
            "question": "How does Abstraction differ from Encapsulation?",
            "options": [
                "Abstraction hides implementation complexity (what it does vs how), whereas Encapsulation hides and protects internal object data state",
                "Abstraction only applies to functions, while Encapsulation only applies to arrays",
                "Encapsulation is deprecated in ES6",
                "Abstraction requires TypeScript interfaces"
            ],
            "answer": "Abstraction hides implementation complexity (what it does vs how), whereas Encapsulation hides and protects internal object data state",
        },
        {
            "question": "Which feature in modern JavaScript helps enforce abstraction inside a class body?",
            "options": [
                "Private helper methods starting with `#` (e.g. `#boilWater()`)",
                "Global window variables",
                "Exporting variables with `var`",
                "Using double quotes around method names"
            ],
            "answer": "Private helper methods starting with `#` (e.g. `#boilWater()`)",
        },
        {
            "question": "Which real-world application relies heavily on Abstraction?",
            "options": [
                "Object-Relational Mapping (ORM) frameworks like Prisma/Sequelize abstracting raw SQL queries",
                "Inline HTML script tags",
                "Pure CSS flexbox layouts",
                "Plain JSON configuration strings"
            ],
            "answer": "Object-Relational Mapping (ORM) frameworks like Prisma/Sequelize abstracting raw SQL queries",
        },
        {
            "question": "What is a major maintenance benefit of using Abstraction?",
            "options": [
                "Internal implementation details can be updated or refactored without breaking external consumer code",
                "It speeds up network request downloads",
                "It turns async functions into synchronous loops",
                "It eliminates the need for unit testing"
            ],
            "answer": "Internal implementation details can be updated or refactored without breaking external consumer code",
        },
    ],
}

# Override Topic 79: Polymorphism in JavaScript
JS_TOPICS[79] = {
    "id": 79,
    "title": "Polymorphism",
    "category": "Object-Oriented Programming",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "Polymorphism ('many forms') is an OOP principle enabling a single method signature or interface to produce different behaviors depending on the target object type or parameter arguments.",
    "theory": "1. What is Polymorphism in JavaScript?\nPolymorphism allows objects of different classes to respond to the same method invocation in their own unique way. A single function call like `animal.speak()` produces different outputs whether `animal` is an instance of `Dog`, `Cat`, or `Cow`.\n\n2. Primary Forms of Polymorphism in JavaScript:\na. Method Overriding (Runtime Polymorphism):\n   - Derived subclasses redefine a method inherited from a base parent class.\n   - JavaScript dynamically decides at runtime which implementation to execute based on the instance type.\nb. Method Overloading (Simulated):\n   - JavaScript does NOT natively support method overloading with duplicate function signatures (as in C++ or Java).\n   - Method overloading is *simulated* by checking parameter length (`arguments.length`) or type inspection within a single method.\nc. Duck-Typing & Functional Polymorphism:\n   - \"If it walks like a duck and quacks like a duck, it's a duck.\"\n   - A function can accept any object as long as it exposes the expected method interface (e.g. `renderComponent(comp)` calling `comp.draw()`).\n\n3. Real-World Use Cases:\n- UI Component Libraries: Calling `component.render()` on `Button`, `Checkbox`, and `TextInput`.\n- Database Adapters: Invoking `db.connect()` on `PostgreSQLAdapter`, `MongoDBAdapter`, or `MySQLAdapter`.\n- File Parsers: Calling `parser.parse(file)` for `JSONParser`, `XMLParser`, or `CSVParser`.",
    "syntax": "// Class Method Overriding (Runtime Polymorphism)\nclass Animal {\n    speak() { return 'Generic Sound'; }\n}\nclass Dog extends Animal {\n    speak() { return 'Woof!'; }\n}\nclass Cat extends Animal {\n    speak() { return 'Meow!'; }\n}\n\n// Functional Duck-Typing\nfunction makeItSpeak(animal) {\n    return animal.speak();\n}",
    "example": {
        "code": "// 1. Class Method Overriding (Runtime Polymorphism)\nclass Animal {\n    speak() {\n        return 'Animal makes a sound';\n    }\n}\nclass Dog extends Animal {\n    speak() {\n        return 'Dog barks: Woof!';\n    }\n}\nclass Cat extends Animal {\n    speak() {\n        return 'Cat meows: Meow!';\n    }\n}\nconst animals = [new Dog(), new Cat(), new Animal()];\nanimals.forEach(a => console.log('Polymorphic Class:', a.speak()));\n\n// 2. Simulated Method Overloading\nclass Calculator {\n    add(a, b) {\n        if (b === undefined) {\n            return a + a; // Single argument: Double value\n        }\n        return a + b; // Two arguments: Sum\n    }\n}\nconst calc = new Calculator();\nconsole.log('Overload 1 Arg (add(5)):', calc.add(5));\nconsole.log('Overload 2 Args (add(5, 10)):', calc.add(5, 10));\n\n// 3. Functional Duck-Typing Polymorphism\nconst dogObj = { speak: () => 'Woof Woof' };\nconst catObj = { speak: () => 'Meow Meow' };\nfunction makeSound(pet) {\n    return pet.speak();\n}\nconsole.log('Duck Typing Dog:', makeSound(dogObj));\nconsole.log('Duck Typing Cat:', makeSound(catObj));",
        "output": "Polymorphic Class: Dog barks: Woof!\nPolymorphic Class: Cat meows: Meow!\nPolymorphic Class: Animal makes a sound\nOverload 1 Arg (add(5)): 10\nOverload 2 Args (add(5, 10)): 15\nDuck Typing Dog: Woof Woof\nDuck Typing Cat: Meow Meow",
        "explanation": "Demonstrates runtime polymorphism via class method overriding, simulated method overloading with default check, and functional duck-typing polymorphism.",
    },
    "fill_blanks": {
        "question": "// Derived subclasses provide custom implementations of parent methods through method _____.\n// JavaScript relies on _____ typing where an object is defined by its methods and properties rather than its exact class inheritance.",
        "answers": ["overriding", "duck"],
        "options": ["overriding", "duck", "overloading", "strict"],
    },
    "compiler": {
        "title": "Polymorphism & Method Overriding Sandbox",
        "question": "Complete the Dog class method overriding.",
        "starter_code": "class Animal {\n    speak() { return 'Sound'; }\n}\nclass Dog extends Animal {\n    _____() {\n        return 'Woof!';\n    }\n}\nlet d = new Dog();\nconsole.log(d.speak());",
        "options": ["speak", "bark", "sound", "override"],
    },
    "skill_exa_test": [
        {
            "question": "What is Polymorphism in Object-Oriented Programming?",
            "options": [
                "The ability of a single method or interface to perform different behaviors depending on the target object or arguments",
                "The process of creating multiple copies of an array",
                "A technique for minifying JavaScript files for production",
                "Storing function calls in local browser cookies"
            ],
            "answer": "The ability of a single method or interface to perform different behaviors depending on the target object or arguments",
        },
        {
            "question": "What is Method Overriding in JavaScript?",
            "options": [
                "When a subclass provides its own specific implementation of a method already defined in its parent class",
                "When a function calls itself recursively",
                "When two variables share the same name in global scope",
                "When a method is deleted using the `delete` operator"
            ],
            "answer": "When a subclass provides its own specific implementation of a method already defined in its parent class",
        },
        {
            "question": "Does JavaScript natively support true method overloading with multiple identical function names with different parameter signatures?",
            "options": [
                "No, JavaScript overwrites duplicate function declarations; overloading must be simulated via argument checking",
                "Yes, using the `overload` keyword",
                "Yes, but only inside ES6 classes",
                "No, it throws a compile-time error"
            ],
            "answer": "No, JavaScript overwrites duplicate function declarations; overloading must be simulated via argument checking",
        },
        {
            "question": "What is 'Duck Typing' in JavaScript polymorphism?",
            "options": [
                "Evaluating an object's suitability based on the presence of specific methods/properties rather than its explicit class hierarchy",
                "A strict typing system imported from TypeScript",
                "An algorithm for sorting objects alphabetically",
                "A method for validating HTML DOM elements"
            ],
            "answer": "Evaluating an object's suitability based on the presence of specific methods/properties rather than its explicit class hierarchy",
        },
        {
            "question": "Which of the following is a classic real-world use case of Polymorphism?",
            "options": [
                "Invoking a common `render()` method across diverse UI components (Buttons, Inputs, Modals) that draw themselves differently",
                "Calculating prime numbers using a while loop",
                "Reading a static CSS stylesheet file",
                "Defining constant primitive string values"
            ],
            "answer": "Invoking a common `render()` method across diverse UI components (Buttons, Inputs, Modals) that draw themselves differently",
        },
    ],
}

# Override Topic 80: Browser Object Model (BOM)
JS_TOPICS[80] = {
    "id": 80,
    "title": "Browser Object Model (BOM)",
    "category": "Browser and Document Object Model",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "The Browser Object Model (BOM) enables JavaScript to interact with the browser environment itself, offering objects to manage windows, navigate URLs, inspect screen dimensions, and read browser metadata.",
    "theory": "1. What is the Browser Object Model (BOM)?\nThe BOM provides objects exposed by the browser to control elements outside the webpage document context, such as browser windows, session history, screen resolution, and navigation.\n\n2. The Core BOM Objects:\na. `window` Object:\n   - Global root object in browser JavaScript.\n   - Hosts dialog methods (`alert()`, `confirm()`, `prompt()`) and window controls (`window.open()`, `window.resizeTo()`, `window.close()`).\n   - Contains properties like `window.innerWidth` and `window.innerHeight`.\nb. `navigator` Object:\n   - Provides information about the user's browser environment and device.\n   - Key properties: `navigator.userAgent`, `navigator.language`, `navigator.onLine`, `navigator.clipboard`.\nc. `location` Object:\n   - Manages document URL information and page navigation.\n   - Key properties: `location.href`, `location.protocol`, `location.hostname`, `location.pathname`.\n   - Key methods: `location.assign('URL')`, `location.reload()`.\nd. `screen` Object:\n   - Contains physical monitor dimensions and screen resolution data.\n   - Key properties: `screen.width`, `screen.height`, `screen.availWidth`.\ne. `history` Object:\n   - Controls the user's browser session history stack.\n   - Key methods: `history.back()`, `history.forward()`, `history.go(-1)`.",
    "syntax": "// Window & Location Object\nconsole.log(window.innerWidth);\nconsole.log(location.href);\n\n// Navigator & Screen Object\nconsole.log(navigator.userAgent);\nconsole.log(screen.width);\n\n// History Navigation\nhistory.back();",
    "example": {
        "code": "// 1. Mocking BOM Window & Screen Inspection\nconst mockWindow = {\n    innerWidth: 1920,\n    innerHeight: 1080,\n    alert: (msg) => console.log('Alert Dialog:', msg)\n};\nconsole.log('Window Dimensions:', `${mockWindow.innerWidth}x${mockWindow.innerHeight}`);\nmockWindow.alert('Welcome to BOM Tutorial!');\n\n// 2. Location Object URL Properties\nconst mockLocation = {\n    href: 'https://www.skillexa.com/courses/js?topic=bom#intro',\n    protocol: 'https:',\n    hostname: 'www.skillexa.com',\n    pathname: '/courses/js'\n};\nconsole.log('Full URL (href):', mockLocation.href);\nconsole.log('Protocol:', mockLocation.protocol);\nconsole.log('Hostname:', mockLocation.hostname);\nconsole.log('Pathname:', mockLocation.pathname);\n\n// 3. Navigator Browser Info\nconst mockNavigator = {\n    language: 'en-US',\n    onLine: true\n};\nconsole.log('Browser Language:', mockNavigator.language);\nconsole.log('Is Online?:', mockNavigator.onLine);",
        "output": "Window Dimensions: 1920x1080\nAlert Dialog: Welcome to BOM Tutorial!\nFull URL (href): https://www.skillexa.com/courses/js?topic=bom#intro\nProtocol: https:\nHostname: www.skillexa.com\nPathname: /courses/js\nBrowser Language: en-US\nIs Online?: true",
        "explanation": "Demonstrates retrieving window dimensions, parsing URL components via the location object, and accessing browser metadata through navigator.",
    },
    "fill_blanks": {
        "question": "// The top-level global object in browser JavaScript environment is the _____ object.\n// URL information and page redirection are handled by the window._____ object.",
        "answers": ["window", "location"],
        "options": ["window", "location", "document", "history"],
    },
    "compiler": {
        "title": "Browser Object Model (BOM) Sandbox",
        "question": "Complete the code to inspect location URL properties.",
        "starter_code": "let loc = {\n    href: 'https://skillexa.com/js',\n    hostname: 'skillexa.com'\n};\nconsole.log(loc._____);\nconsole.log(loc.hostname);",
        "options": ["href", "url", "link", "path"],
    },
    "skill_exa_test": [
        {
            "question": "What is the primary role of the Browser Object Model (BOM) in JavaScript?",
            "options": [
                "To interact with browser features outside page content, such as windows, location, history, and screen",
                "To structure database SQL queries",
                "To style CSS flexbox containers",
                "To manage multi-threaded CPU workers"
            ],
            "answer": "To interact with browser features outside page content, such as windows, location, history, and screen",
        },
        {
            "question": "Which BOM object provides information about the current document URL and allows redirecting to a new page?",
            "options": ["location", "navigator", "screen", "history"],
            "answer": "location",
        },
        {
            "question": "Which property of `navigator` returns the user's preferred language configuration?",
            "options": ["navigator.language", "navigator.locale", "navigator.lang", "navigator.userLanguage"],
            "answer": "navigator.language",
        },
        {
            "question": "How can JavaScript navigate back one page in the browser session history stack?",
            "options": ["history.back()", "history.previous()", "history.undo()", "window.goBack()"],
            "answer": "history.back()",
        },
        {
            "question": "Which properties of the `screen` object return the user monitor screen resolution?",
            "options": ["screen.width and screen.height", "screen.innerWidth and screen.innerHeight", "screen.sizeX and screen.sizeY", "screen.bounds"],
            "answer": "screen.width and screen.height",
        },
    ],
}

# Override Topic 81: Document Object Model (DOM)
JS_TOPICS[81] = {
    "id": 81,
    "title": "Document Object Model (DOM)",
    "category": "Browser and Document Object Model",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "The Document Object Model (DOM) is a programming interface representing an HTML document as a hierarchical tree of nodes, allowing JavaScript to dynamically access, inspect, and traverse webpage elements.",
    "theory": "1. What is the HTML DOM?\nThe DOM represents an HTML document as a structured logical tree of objects (the DOM Tree). Each HTML element, attribute, and piece of text becomes a node in the tree.\n\n2. DOM Node Hierarchy:\n- Document Node: Root of the entire DOM tree (`document`).\n- Element Nodes: HTML tags like `<div>`, `<h1>`, `<p>`.\n- Attribute Nodes: Element attributes like `id=\"title\"` or `class=\"active\"`.\n- Text Nodes: Text contained inside elements.\n\n3. Element Selection Methods:\na. `document.getElementById('id')`: Selects a single element by its unique ID.\nb. `document.getElementsByClassName('class')`: Returns a live HTMLCollection of elements with matching class.\nc. `document.getElementsByTagName('tag')`: Returns a live HTMLCollection of matching HTML tags.\nd. `document.querySelector('selector')`: Returns the FIRST element matching a CSS selector.\ne. `document.querySelectorAll('selector')`: Returns a static NodeList of ALL elements matching a CSS selector.\n\n4. DOM Tree Traversal:\n- Parent: `node.parentNode` / `node.parentElement`.\n- Children: `node.children`, `node.firstElementChild`, `node.lastElementChild`.\n- Siblings: `node.nextElementSibling`, `node.previousElementSibling`.",
    "syntax": "// Selecting DOM Elements\nconst title = document.getElementById('title');\nconst items = document.querySelectorAll('.item');\nconst firstPara = document.querySelector('p');\n\n// Traversing Nodes\nconst parent = title.parentElement;\nconst firstChild = parent.firstElementChild;",
    "example": {
        "code": "// 1. Mocking Selection Methods\nconst mockDOM = {\n    getElementById: (id) => ({ id, textContent: 'Main Heading' }),\n    querySelector: (sel) => ({ selector: sel, textContent: 'First Paragraph' }),\n    querySelectorAll: (sel) => [\n        { className: 'item', textContent: 'Item 1' },\n        { className: 'item', textContent: 'Item 2' }\n    ]\n};\n\nconst heading = mockDOM.getElementById('demo');\nconsole.log('getElementById:', heading.textContent);\n\nconst para = mockDOM.querySelector('p');\nconsole.log('querySelector:', para.textContent);\n\nconst listItems = mockDOM.querySelectorAll('.item');\nlistItems.forEach((item, index) => {\n    console.log(`NodeList Item ${index + 1}:`, item.textContent);\n});",
        "output": "getElementById: Main Heading\nquerySelector: First Paragraph\nNodeList Item 1: Item 1\nNodeList Item 2: Item 2",
        "explanation": "Demonstrates selecting HTML elements via getElementById, querySelector, and iterating NodeLists returned by querySelectorAll.",
    },
    "fill_blanks": {
        "question": "// The method that retrieves a single element by its unique ID attribute is document._____().\n// The method that returns all elements matching a CSS selector as a NodeList is document._____().",
        "answers": ["getElementById", "querySelectorAll"],
        "options": ["getElementById", "querySelectorAll", "getElementsByClassName", "querySelector"],
    },
    "compiler": {
        "title": "DOM Selection Sandbox",
        "question": "Complete the DOM element selection code.",
        "starter_code": "let doc = {\n    _____: (id) => ({ textContent: 'Selected Node' })\n};\nlet el = doc.getElementById('title');\nconsole.log(el.textContent);",
        "options": ["getElementById", "querySelector", "getElement", "select"],
    },
    "skill_exa_test": [
        {
            "question": "What is the HTML DOM in JavaScript?",
            "options": [
                "A hierarchical tree representation of an HTML document as nodes that JavaScript can inspect and manipulate",
                "A database engine inside Chrome",
                "A CSS styling library",
                "A tool for minifying JavaScript files"
            ],
            "answer": "A hierarchical tree representation of an HTML document as nodes that JavaScript can inspect and manipulate",
        },
        {
            "question": "What does `document.querySelector('p')` return?",
            "options": [
                "The FIRST element matching the `<p>` CSS selector",
                "An array of all `<p>` elements",
                "A plain text string of all paragraphs",
                "The parent node of paragraph elements"
            ],
            "answer": "The FIRST element matching the `<p>` CSS selector",
        },
        {
            "question": "What is the return type of `document.querySelectorAll('.list-item')`?",
            "options": ["A static NodeList", "A live HTMLCollection", "A single DOM element", "A JSON string"],
            "answer": "A static NodeList",
        },
        {
            "question": "Which property returns the immediate container parent node of an element in the DOM tree?",
            "options": ["parentNode", "children", "nextSibling", "rootNode"],
            "answer": "parentNode",
        },
        {
            "question": "How does `getElementsByClassName()` differ from `querySelectorAll()`?",
            "options": [
                "getElementsByClassName returns a live HTMLCollection, whereas querySelectorAll returns a static NodeList",
                "getElementsByClassName only works in Node.js",
                "querySelectorAll returns HTML strings",
                "There is no difference between them"
            ],
            "answer": "getElementsByClassName returns a live HTMLCollection, whereas querySelectorAll returns a static NodeList",
        },
    ],
}

# Override Topic 82: Manipulate DOM Elements
JS_TOPICS[82] = {
    "id": 82,
    "title": "Manipulate DOM Elements",
    "category": "Browser and Document Object Model",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "DOM manipulation allows JavaScript to update element content, toggle CSS classes, modify inline styles, create/append/remove elements dynamically, and manipulate custom data attributes.",
    "theory": "1. Modifying Element Content:\n- `textContent`: Sets or returns plain text inside an element (ignores HTML tags, safe against XSS attacks).\n- `innerHTML`: Sets or returns HTML markup inside an element (parses HTML tags).\n\n2. Manipulating CSS Classes (`classList` API):\n- `element.classList.add('active')`: Appends CSS class.\n- `element.classList.remove('bold')`: Removes CSS class.\n- `element.classList.toggle('highlight')`: Toggles class presence on/off.\n- `element.classList.contains('active')`: Checks if class exists.\n\n3. Setting Inline CSS Styles:\n- Individual Properties: `element.style.color = 'red'; element.style.fontSize = '20px';`\n- Multiple Styles: `element.style.cssText = 'color: blue; font-size: 18px;';` \n\n4. Creating, Adding, and Removing Nodes:\n- Create: `document.createElement('div')`.\n- Append: `parent.appendChild(newChild)` (adds to end of parent).\n- Insert Before: `parent.insertBefore(newNode, existingNode)`.\n- Remove Directly: `element.remove()`.\n- Remove Child: `parent.removeChild(childNode)`.\n\n5. Attributes & HTML5 Data Attributes:\n- Attributes: `getAttribute(attr)`, `setAttribute(attr, value)`, `removeAttribute(attr)`.\n- Custom Data Attributes: HTML `data-user-id=\"123\"` accessible via JS `element.dataset.userId`.",
    "syntax": "// Changing Content & Attributes\nel.textContent = 'Updated Text';\nel.innerHTML = '<strong>Bold Text</strong>';\nel.setAttribute('src', 'logo.png');\n\n// Class & Style Manipulation\nel.classList.add('highlight');\nel.classList.toggle('active');\nel.style.color = 'green';\n\n// Creating & Appending Elements\nconst newDiv = document.createElement('div');\nnewDiv.textContent = 'New Node';\ndocument.body.appendChild(newDiv);",
    "example": {
        "code": "// 1. Content & Style Manipulation Simulation\nlet element = {\n    textContent: 'Original Text',\n    innerHTML: 'Original HTML',\n    style: {},\n    classList: {\n        classes: new Set(['bold']),\n        add(cls) { this.classes.add(cls); },\n        remove(cls) { this.classes.delete(cls); },\n        toggle(cls) { this.classes.has(cls) ? this.classes.delete(cls) : this.classes.add(cls); }\n    },\n    dataset: {}\n};\n\nelement.textContent = 'Changed using textContent!';\nelement.style.color = 'red';\nelement.classList.add('highlight');\nelement.dataset.userId = '12345';\n\nconsole.log('Updated Text:', element.textContent);\nconsole.log('Element Style Color:', element.style.color);\nconsole.log('Class List:', Array.from(element.classList.classes));\nconsole.log('Dataset User ID:', element.dataset.userId);",
        "output": "Updated Text: Changed using textContent!\nElement Style Color: red\nClass List: [ 'bold', 'highlight' ]\nDataset User ID: 12345",
        "explanation": "Demonstrates setting element text content, applying CSS styles, manipulating class lists using classList.add, and setting HTML5 dataset properties.",
    },
    "fill_blanks": {
        "question": "// To update plain text inside an element safely without parsing HTML markup, use the _____ property.\n// To toggle CSS classes dynamically on an element, use element.classList._____().",
        "answers": ["textContent", "toggle"],
        "options": ["textContent", "toggle", "innerHTML", "add"],
    },
    "compiler": {
        "title": "DOM Element Manipulation Sandbox",
        "question": "Complete the element text and class manipulation.",
        "starter_code": "let el = {\n    textContent: '',\n    classList: { add: (c) => console.log('Added class:', c) }\n};\nel._____ = 'Hello SkillExa';\nel.classList._____('active');",
        "options": ["textContent", "add", "innerHTML", "toggle"],
    },
    "skill_exa_test": [
        {
            "question": "What is the difference between `textContent` and `innerHTML`?",
            "options": [
                "textContent sets/gets plain text ignoring HTML tags, whereas innerHTML parses and renders HTML tags",
                "textContent only works on buttons, innerHTML works on divs",
                "innerHTML is deprecated in ES6",
                "There is no difference between them"
            ],
            "answer": "textContent sets/gets plain text ignoring HTML tags, whereas innerHTML parses and renders HTML tags",
        },
        {
            "question": "Which `classList` method adds a class if it is missing or removes it if it is already present?",
            "options": ["classList.toggle()", "classList.add()", "classList.remove()", "classList.replace()"],
            "answer": "classList.toggle()",
        },
        {
            "question": "Which DOM method creates a new HTML element node in memory?",
            "options": ["document.createElement('tag')", "document.makeElement('tag')", "document.newNode('tag')", "document.build('tag')"],
            "answer": "document.createElement('tag')",
        },
        {
            "question": "How do you access an HTML5 custom data attribute `data-user-id=\"55\"` in JavaScript?",
            "options": ["element.dataset.userId", "element.data.userId", "element.getCustom('user-id')", "element.dataset['data-user-id']"],
            "answer": "element.dataset.userId",
        },
        {
            "question": "Which DOM method appends a new node as the last child of a parent element?",
            "options": ["parent.appendChild(newNode)", "parent.insertBefore(newNode)", "parent.prepend(newNode)", "parent.attach(newNode)"],
            "answer": "parent.appendChild(newNode)",
        },
    ],
}

# Override Topic 83: Event Handling in the DOM
JS_TOPICS[83] = {
    "id": 83,
    "title": "Event Handling in the DOM",
    "category": "Browser and Document Object Model",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "Event handling allows JavaScript to react dynamically to user interactions (clicks, keypresses, form submissions, window resizes) by attaching listener functions and handling event propagation.",
    "theory": "1. What is an Event?\nAn event is a signal that something has happened in the browser (user clicked a button, pressed a key, loaded a page, or submitted a form).\n\n2. Attaching Event Listeners:\n- `element.addEventListener(type, listener)`: The recommended standard for binding events. Allows multiple handlers for the same event type.\n- `element.removeEventListener(type, listener)`: Unbinds a registered event handler.\n\n3. Common Event Categories:\na. Window Events: `onload`, `onresize`, `onscroll`.\nb. Mouse Events: `click`, `dblclick`, `mouseover`, `mouseout`, `mousemove`.\nc. Keyboard Events: `keydown`, `keyup` (inspecting `event.key`).\nd. Form Events: `submit`, `change`, `focus`, `blur`.\n\n4. The Event Object (`e` / `event`):\nPassed automatically into event handler functions:\n- `event.target`: The exact DOM element that dispatched the event.\n- `event.key`: The key value pressed during keyboard events (e.g. `'Enter'`).\n- `event.preventDefault()`: Prevents default browser actions (e.g. form submission page refresh or link redirection).\n\n5. Event Propagation (Bubbling vs Capturing):\n- Event Bubbling: Event triggers on the target element first, then bubbles UP through parent elements (default behavior).\n- Event Capturing: Event trickles DOWN from document root to target element.\n- `event.stopPropagation()`: Stops event propagation from bubbling up or capturing down.",
    "syntax": "// Attaching Event Listener\nbutton.addEventListener('click', (event) => {\n    console.log('Target:', event.target);\n});\n\n// Preventing Default & Checking Key\ninput.addEventListener('keydown', (e) => {\n    if (e.key === 'Enter') {\n        e.preventDefault();\n        console.log('Enter key pressed!');\n    }\n});",
    "example": {
        "code": "// 1. Event Listener Simulation for Click Event\nfunction createMockElement(name) {\n    const listeners = {};\n    return {\n        name,\n        addEventListener(type, fn) {\n            if (!listeners[type]) listeners[type] = [];\n            listeners[type].push(fn);\n        },\n        trigger(type, eventObj) {\n            if (listeners[type]) {\n                listeners[type].forEach(fn => fn(eventObj));\n            }\n        }\n    };\n}\nconst btn = createMockElement('SubmitButton');\nbtn.addEventListener('click', (e) => {\n    console.log(`Event Fired on ${btn.name}! Target: ${e.targetName}`);\n});\nbtn.trigger('click', { targetName: 'SubmitButton' });\n\n// 2. Keyboard Event Handling & preventDefault Simulation\nconst inputField = createMockElement('SearchInput');\ninputField.addEventListener('keydown', (e) => {\n    if (e.key === 'Enter') {\n        e.preventDefault();\n        console.log('Enter pressed! Default submission prevented.');\n    }\n});\nlet preventCalled = false;\ninputField.trigger('keydown', {\n    key: 'Enter',\n    preventDefault() { preventCalled = true; }\n});\nconsole.log('Prevent Default Executed?:', preventCalled);",
        "output": "Event Fired on SubmitButton! Target: SubmitButton\nEnter pressed! Default submission prevented.\nPrevent Default Executed?: true",
        "explanation": "Demonstrates registering click and keydown event handlers via addEventListener, inspecting event parameters, and using preventDefault().",
    },
    "fill_blanks": {
        "question": "// The recommended method to attach an event listener to a DOM element is element._____().\n// To prevent default browser actions like form submissions, call event._____().",
        "answers": ["addEventListener", "preventDefault"],
        "options": ["addEventListener", "preventDefault", "removeEventListener", "stopPropagation"],
    },
    "compiler": {
        "title": "Event Handling Sandbox",
        "question": "Complete the click event listener attachment.",
        "starter_code": "let btn = {\n    _____: (type, fn) => fn({ target: 'Btn' })\n};\nbtn.addEventListener('click', (e) => {\n    console.log('Clicked:', e.target);\n});",
        "options": ["addEventListener", "on", "bind", "listen"],
    },
    "skill_exa_test": [
        {
            "question": "What is the standard recommended method for attaching event handlers to DOM elements in modern JavaScript?",
            "options": ["element.addEventListener(type, listener)", "element.onclick = listener", "element.attachEvent(type, listener)", "element.bind(type, listener)"],
            "answer": "element.addEventListener(type, listener)",
        },
        {
            "question": "What does `event.preventDefault()` do inside an event handler?",
            "options": [
                "It cancels default browser behavior associated with the event (e.g. page reload on form submit)",
                "It deletes the event listener from memory",
                "It stops event bubbling to parent elements",
                "It refreshes the current webpage"
            ],
            "answer": "It cancels default browser behavior associated with the event (e.g. page reload on form submit)",
        },
        {
            "question": "What is 'Event Bubbling' in the HTML DOM?",
            "options": [
                "When an event triggers on a target element and then propagates UP through its parent elements in the DOM tree",
                "When events execute in reverse alphabetical order",
                "When multiple click events fire simultaneously",
                "When events are automatically stored in local storage"
            ],
            "answer": "When an event triggers on a target element and then propagates UP through its parent elements in the DOM tree",
        },
        {
            "question": "Which property of the Event object references the exact DOM element that dispatched the event?",
            "options": ["event.target", "event.element", "event.srcElement", "event.origin"],
            "answer": "event.target",
        },
        {
            "question": "Which method halts further propagation of an event up or down the DOM tree?",
            "options": ["event.stopPropagation()", "event.preventDefault()", "event.stop()", "event.cancel()"],
            "answer": "event.stopPropagation()",
        },
    ],
}

# Override Topic 84: Callbacks in JavaScript
JS_TOPICS[84] = {
    "id": 84,
    "title": "Callbacks",
    "category": "Asynchronous JavaScript",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "A callback function is a function passed as an argument to another function, intended to be executed after an asynchronous operation or higher-order task completes.",
    "theory": "1. What is a Callback Function?\nA callback function is passed into another function as a parameter and invoked inside the outer function to complete an action. Callbacks can execute synchronously (immediately) or asynchronously (deferred).\n\n2. Synchronous vs Asynchronous Callbacks:\n- Synchronous Callbacks: Executed immediately during outer function execution (e.g. `arr.map(x => x * 2)` or `calc(5, 3, add)`).\n- Asynchronous Callbacks: Executed after an asynchronous task completes or after event loop tick (e.g., `setTimeout()`, `addEventListener()`, `fs.readFile()`, `fetch()`).\n\n3. Common Uses of Callbacks:\n- Higher-Order Functions: Customizing behavior dynamically.\n- Event Handling: Reacting to UI user interactions.\n- Asynchronous Data Retrieval: Fetching records from APIs or databases.\n\n4. Problems with Callbacks:\na. Callback Hell (Pyramid of Doom):\n   - When multiple asynchronous operations depend on previous results, deeply nested callback indentation makes code unreadable and unmaintainable.\nb. Error Handling Inversion:\n   - Handling errors requires error-first callback conventions (`callback(err, result)`). Forgetting error checks can lead to unhandled exceptions.\n\n5. Alternatives to Callbacks:\nModern JavaScript resolves callback hell using **Promises** and **Async/Await**.",
    "syntax": "// Higher-Order Callback\nfunction greet(name, callback) {\n    console.log(`Hello ${name}`);\n    callback();\n}\n\n// Error-First Callback Signature\nfunction divide(a, b, callback) {\n    if (b === 0) callback(new Error('Cannot divide by zero'), null);\n    else callback(null, a / b);\n}",
    "example": {
        "code": "// 1. Higher-Order Function Callback\nfunction calculate(a, b, operation) {\n    return operation(a, b);\n}\nconst add = (x, y) => x + y;\nconst multiply = (x, y) => x * y;\nconsole.log('Callback Add:', calculate(5, 3, add));\nconsole.log('Callback Multiply:', calculate(5, 3, multiply));\n\n// 2. Error-First Callback Pattern\nfunction divide(a, b, callback) {\n    if (b === 0) {\n        callback(new Error('Cannot divide by zero'), null);\n    } else {\n        callback(null, a / b);\n    }\n}\nfunction handleResult(err, res) {\n    if (err) console.log('Error Handled:', err.message);\n    else console.log('Division Result:', res);\n}\ndivide(10, 2, handleResult);\ndivide(10, 0, handleResult);\n\n// 3. Asynchronous Callback Simulation\nconsole.log('Start Sync');\nsetTimeout(() => {\n    console.log('Async Callback Executed after 100ms');\n}, 100);\nconsole.log('End Sync');",
        "output": "Callback Add: 8\nCallback Multiply: 15\nDivision Result: 5\nError Handled: Cannot divide by zero\nStart Sync\nEnd Sync\nAsync Callback Executed after 100ms",
        "explanation": "Demonstrates synchronous higher-order callbacks, Node-style error-first callbacks, and non-blocking asynchronous callbacks using setTimeout.",
    },
    "fill_blanks": {
        "question": "// A function passed as an argument to another function is called a _____ function.\n// In Node.js, asynchronous callbacks conventionally adopt the _____-first parameter signature.",
        "answers": ["callback", "error"],
        "options": ["callback", "error", "promise", "async"],
    },
    "compiler": {
        "title": "Callbacks & Higher-Order Functions Sandbox",
        "question": "Complete the calculate function with callback execution.",
        "starter_code": "function calc(a, b, _____) {\n    return callback(a, b);\n}\nfunction mul(x, y) {\n    return x * y;\n}\nconsole.log(calc(4, 5, mul));",
        "options": ["callback", "func", "operation", "fn"],
    },
    "skill_exa_test": [
        {
            "question": "What is a callback function in JavaScript?",
            "options": [
                "A function passed as an argument to another function to be executed later",
                "A built-in class method for creating objects",
                "A browser event that refreshes the webpage",
                "A function that returns HTML elements"
            ],
            "answer": "A function passed as an argument to another function to be executed later",
        },
        {
            "question": "What does the term 'Callback Hell' refer to in JavaScript?",
            "options": [
                "Deeply nested callback functions creating pyramid-like unreadable code structure",
                "A memory leak caused by unclosed event listeners",
                "An infinite loop inside a constructor function",
                "A server error thrown by fetch API"
            ],
            "answer": "Deeply nested callback functions creating pyramid-like unreadable code structure",
        },
        {
            "question": "What is the standard parameter ordering for Node.js error-first callbacks?",
            "options": [
                "The error object is passed as the first parameter `(err, result)`",
                "The result is passed as the first parameter `(result, err)`",
                "Only error messages are allowed",
                "Arguments are passed as an array `([err, result])`"
            ],
            "answer": "The error object is passed as the first parameter `(err, result)`",
        },
        {
            "question": "Which of the following is an example of an asynchronous callback?",
            "options": [
                "Passing a handler function to `setTimeout(callback, 1000)`",
                "Passing a mapper function to `[1,2,3].map(x => x * 2)`",
                "Calling `Math.max(5, 10)`",
                "Invoking a constructor via `new Person()`"
            ],
            "answer": "Passing a handler function to `setTimeout(callback, 1000)`",
        },
        {
            "question": "What are the primary modern alternatives designed to solve Callback Hell?",
            "options": [
                "Promises and Async/Await",
                "Global variables and `var` statements",
                "While loops and `switch` statements",
                "HTML DOM forms"
            ],
            "answer": "Promises and Async/Await",
        },
    ],
}

# Override Topic 85: Promise - Basics & Creation (Ch. 1)
JS_TOPICS[85] = {
    "id": 85,
    "title": "Promise - Basics & Creation (Ch. 1)",
    "category": "Asynchronous JavaScript",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "A Promise is a proxy for a value not necessarily known when the promise is created. It allows asynchronous methods to return values like synchronous methods by operating in Pending, Fulfilled, or Rejected states.",
    "theory": "1. What is a Promise?\nA Promise is an object representing the eventual completion (or failure) of an asynchronous task and its resulting value.\n\n2. The 3 States of a Promise:\n- **Pending**: Initial state; asynchronous operation in progress.\n- **Fulfilled**: Operation completed successfully (`resolve()` called with value).\n- **Rejected**: Operation failed (`reject()` called with error reason).\n\n3. Creating a Promise:\nConstructed using `new Promise((resolve, reject) => { ... })`:\n- `resolve(val)`: Transitions state from Pending to Fulfilled.\n- `reject(err)`: Transitions state from Pending to Rejected.\n\n4. Consuming Promises:\n- `.then(onFulfilled)`: Invoked when the promise resolves.\n- `.catch(onRejected)`: Invoked when the promise rejects.\n\n5. Immutability of Settlement:\nOnce a Promise settles (either fulfilled or rejected), its state and result value are frozen permanently and cannot be changed.",
    "syntax": "let promise = new Promise((resolve, reject) => {\n    let success = true;\n    if (success) resolve('Task Completed Successfully');\n    else reject(new Error('Task Failed'));\n});\n\npromise\n    .then(result => console.log(result))\n    .catch(error => console.error(error.message));",
    "example": {
        "code": "// 1. Basic Promise Creation & Consumption\nlet checkEven = new Promise((resolve, reject) => {\n    let number = 4;\n    if (number % 2 === 0) {\n        resolve(`Success: ${number} is an even number!`);\n    } else {\n        reject(`Failure: ${number} is an odd number!`);\n    }\n});\ncheckEven\n    .then(msg => console.log('Fulfilled:', msg))\n    .catch(err => console.log('Rejected:', err));\n\n// 2. Rejected Promise Handling\nlet checkOdd = new Promise((resolve, reject) => {\n    let num = 5;\n    if (num % 2 === 0) resolve('Even');\n    else reject('Validation Error: Number is odd');\n});\ncheckOdd\n    .then(msg => console.log('Fulfilled:', msg))\n    .catch(err => console.log('Caught Error:', err));",
        "output": "Fulfilled: Success: 4 is an even number!\nCaught Error: Validation Error: Number is odd",
        "explanation": "Demonstrates creating promises using new Promise(executor), transitioning between Pending, Fulfilled, and Rejected states via resolve and reject.",
    },
    "fill_blanks": {
        "question": "// A Promise starts in the _____ state before settling into fulfilled or rejected.\n// Invoking the _____() function marks a Promise as fulfilled with a result value.",
        "answers": ["pending", "resolve"],
        "options": ["pending", "resolve", "reject", "fulfilled"],
    },
    "compiler": {
        "title": "Promise Creation & Resolution Sandbox",
        "question": "Complete the promise constructor executor function.",
        "starter_code": "let p = new Promise((_____, reject) => {\n    let ok = true;\n    if (ok) resolve('Data Loaded');\n    else reject('Error');\n});\np.then(res => console.log(res));",
        "options": ["resolve", "fulfill", "done", "complete"],
    },
    "skill_exa_test": [
        {
            "question": "What are the three possible states of a JavaScript Promise?",
            "options": [
                "Pending, Fulfilled, and Rejected",
                "Starting, Running, and Stopped",
                "Created, Executed, and Deleted",
                "Async, Sync, and Paused"
            ],
            "answer": "Pending, Fulfilled, and Rejected",
        },
        {
            "question": "What function inside a Promise executor transitions its state from Pending to Fulfilled?",
            "options": ["resolve(value)", "reject(error)", "then(callback)", "fulfill(data)"],
            "answer": "resolve(value)",
        },
        {
            "question": "What happens once a Promise reaches a settled state (Fulfilled or Rejected)?",
            "options": [
                "Its state becomes immutable and can never change again",
                "It automatically restarts from Pending state",
                "It converts into a callback function",
                "It throws a TypeError"
            ],
            "answer": "Its state becomes immutable and can never change again",
        },
        {
            "question": "Which method is attached to a Promise to handle rejection errors?",
            "options": [".catch(error => ...)", ".then(data => ...)", ".finally(() => ...)", ".error(err => ...)"],
            "answer": ".catch(error => ...)",
        },
        {
            "question": "Are `resolve` and `reject` reserved JavaScript language keywords inside Promise executors?",
            "options": [
                "No, they are arbitrary parameter names for functions supplied by the JS engine to settle the promise",
                "Yes, they are strict ES6 reserved keywords",
                "Yes, but only in strict mode",
                "No, they are browser DOM global methods"
            ],
            "answer": "No, they are arbitrary parameter names for functions supplied by the JS engine to settle the promise",
        },
    ],
}

# Override Topic 86: Promise - Advanced Methods & Patterns (Ch. 2)
JS_TOPICS[86] = {
    "id": 86,
    "title": "Promise - Advanced Methods & Patterns (Ch. 2)",
    "category": "Asynchronous JavaScript",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "JavaScript Promises offer advanced static combinator methods (Promise.all, allSettled, race, any) and architectural patterns like promisification and sequential array reduction for handling complex concurrent workflows.",
    "theory": "1. Static Combinator Methods:\n- `Promise.all([p1, p2])`: Executes promises concurrently. Resolves with array of results when ALL fulfill; rejects immediately if ANY promise rejects (fail-fast).\n- `Promise.allSettled([p1, p2])`: Waits for ALL promises to settle regardless of outcome. Returns array of objects with `{ status: 'fulfilled'|'rejected', value/reason }`.\n- `Promise.race([p1, p2])`: Settles as soon as the FIRST promise settles (fulfilled or rejected). Commonly used for network timeout enforcement.\n- `Promise.any([p1, p2])`: Resolves with the FIRST fulfilled promise. Rejects only if ALL promises reject (AggregateError).\n\n2. Static Helper Methods:\n- `Promise.resolve(val)`: Returns an immediately resolved Promise with `val`.\n- `Promise.reject(reason)`: Returns an immediately rejected Promise with `reason`.\n\n3. Cleanup via `Promise.prototype.finally()`:\nExecutes cleanup code unconditionally after settlement, regardless of success or failure.\n\n4. Advanced Async Patterns:\n- Sequential Queueing via `Array.prototype.reduce()`: Chain promises sequentially across array items.\n- Promisification: Wrapping legacy callback-based functions inside a Promise constructor function.",
    "syntax": "// Promise.all & Promise.race\nPromise.all([p1, p2]).then(results => ...);\nPromise.race([fetchData, timeoutPromise]).then(res => ...).catch(err => ...);\n\n// Promisify Callback Function\nfunction promisifiedLoad(url) {\n    return new Promise((resolve, reject) => {\n        legacyLoad(url, (err, data) => {\n            if (err) reject(err);\n            else resolve(data);\n        });\n    });\n}",
    "example": {
        "code": "// 1. Promise.allSettled (Inspecting all outcomes)\nPromise.allSettled([\n    Promise.resolve('Task 1 Passed'),\n    Promise.reject('Task 2 Failed'),\n    Promise.resolve('Task 3 Passed')\n]).then(results => console.log('allSettled:', results.map(r => r.status)));\n\n// 2. Promise.race for Timeout Enforcement\nlet fetchData = new Promise(resolve => setTimeout(() => resolve('API Data'), 300));\nlet timeout = new Promise((_, reject) => setTimeout(() => reject('Timeout Error!'), 100));\nPromise.race([fetchData, timeout])\n    .then(res => console.log('Race Winner:', res))\n    .catch(err => console.log('Race Winner Error:', err));\n\n// 3. Promisification (Wrapping Callbacks into Promises)\nfunction legacyAsync(cb) {\n    setTimeout(() => cb(null, 'Promisified Output'), 50);\n}\nfunction promisifyLegacy() {\n    return new Promise((resolve, reject) => {\n        legacyAsync((err, data) => {\n            if (err) reject(err);\n            else resolve(data);\n        });\n    });\n}\npromisifyLegacy().then(data => console.log('Promisified:', data));",
        "output": "allSettled: [ 'fulfilled', 'rejected', 'fulfilled' ]\nRace Winner Error: Timeout Error!\nPromisified: Promisified Output",
        "explanation": "Demonstrates Promise.allSettled tracking, Promise.race handling timeouts, and wrapping legacy callback functions into clean Promises.",
    },
    "fill_blanks": {
        "question": "// The Promise static method that waits for ALL promises to settle regardless of failure is Promise._____().\n// The Promise static method that settles as soon as the FIRST promise settles is Promise._____().",
        "answers": ["allSettled", "race"],
        "options": ["allSettled", "race", "all", "any"],
    },
    "compiler": {
        "title": "Promise Static Methods Sandbox",
        "question": "Complete Promise.all execution.",
        "starter_code": "Promise.____([\n    Promise.resolve('Task A'),\n    Promise.resolve('Task B')\n]).then(results => console.log(results.join(' & ')));",
        "options": ["all", "race", "any", "allSettled"],
    },
    "skill_exa_test": [
        {
            "question": "What is the key behavior of `Promise.all([p1, p2])`?",
            "options": [
                "It resolves when ALL promises resolve, but rejects immediately if ANY single promise rejects",
                "It waits for the first promise to settle and ignores all others",
                "It converts promises into synchronous code",
                "It executes promises in sequential serial order"
            ],
            "answer": "It resolves when ALL promises resolve, but rejects immediately if ANY single promise rejects",
        },
        {
            "question": "How does `Promise.allSettled()` differ from `Promise.all()`?",
            "options": [
                "Promise.allSettled waits for all promises to finish regardless of resolution or rejection, returning status objects for each",
                "Promise.allSettled rejects if more than 2 promises fail",
                "Promise.allSettled only accepts string values",
                "Promise.allSettled cancels pending network requests"
            ],
            "answer": "Promise.allSettled waits for all promises to finish regardless of resolution or rejection, returning status objects for each",
        },
        {
            "question": "Which Promise static method resolves with the FIRST fulfilled promise, ignoring rejections unless ALL promises reject?",
            "options": ["Promise.any()", "Promise.race()", "Promise.all()", "Promise.allSettled()"],
            "answer": "Promise.any()",
        },
        {
            "question": "What is a common real-world use case for `Promise.race()`?",
            "options": [
                "Implementing request timeouts by racing a fetch Promise against a timer rejection Promise",
                "Sorting an array of numbers asynchronously",
                "Validating HTML DOM forms",
                "Encrypting user passwords"
            ],
            "answer": "Implementing request timeouts by racing a fetch Promise against a timer rejection Promise",
        },
        {
            "question": "What is 'Promisification' in JavaScript?",
            "options": [
                "Converting legacy callback-based asynchronous functions into functions that return a Promise",
                "Converting JSON strings into JavaScript objects",
                "Converting ES6 classes into prototype functions",
                "Compiling Node.js code to C++ binaries"
            ],
            "answer": "Converting legacy callback-based asynchronous functions into functions that return a Promise",
        },
    ],
}

# Override Topic 87: Promise Chaining
JS_TOPICS[87] = {
    "id": 87,
    "title": "Promise Chaining",
    "category": "Asynchronous JavaScript",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "Promise chaining allows executing a sequence of dependent or independent asynchronous tasks in fixed order by chaining .then() methods, eliminating callback nesting and centralizing error handling.",
    "theory": "1. What is Promise Chaining?\nPromise chaining links multiple asynchronous operations sequentially. Each `.then()` method returns a **new Promise**, allowing subsequent `.then()` methods to be appended in a flat, readable pipeline.\n\n2. Return Value Delegation inside `.then()`:\n- Returning a Value: If a `.then()` handler returns a primitive/object value, JavaScript automatically wraps it in `Promise.resolve(val)`.\n- Returning a Promise: If a `.then()` handler returns a new Promise, the next `.then()` in the chain pauses execution until that returned Promise resolves.\n\n3. Chaining Dependent Async Tasks:\nEnables data flow from step to step, where subsequent steps depend on previous step results (e.g., `fetchUser(userId) -> fetchOrders(user) -> processPayment(orders)`).\n\n4. Centralized Error Propagation (`.catch()`):\nA single `.catch()` at the bottom of the chain catches errors thrown or rejected at ANY previous step in the pipeline. Once an error occurs, control skips all intervening `.then()` handlers and jumps directly to `.catch()`.\n\n5. Combining Parallel and Sequential Operations:\nCombining `Promise.all()` with chaining allows running tasks in parallel before passing merged results to sequential processing steps.",
    "syntax": "task1()\n    .then(result1 => {\n        console.log(result1);\n        return task2(result1);\n    })\n    .then(result2 => {\n        console.log(result2);\n    })\n    .catch(error => {\n        console.error('Error anywhere in chain:', error.message);\n    });",
    "example": {
        "code": "// 1. Dependent Tasks Data Flow Chaining\nfunction fetchUser(userId) {\n    return Promise.resolve({ id: userId, name: 'GFG Student' });\n}\nfunction fetchOrders(user) {\n    return Promise.resolve([{ orderId: 101, user: user.name }, { orderId: 102, user: user.name }]);\n}\nfetchUser(101)\n    .then(user => {\n        console.log(`Step 1: User Loaded -> ${user.name}`);\n        return fetchOrders(user);\n    })\n    .then(orders => {\n        console.log(`Step 2: Total Orders Found -> ${orders.length}`);\n    })\n    .catch(err => console.error('Chain Error:', err));\n\n// 2. Error Propagation in Promise Chain\nPromise.resolve(5)\n    .then(num => {\n        console.log(`Value: ${num}`);\n        throw new Error('Step 2 Exception Triggered!');\n    })\n    .then(num => console.log('This will be skipped!'))\n    .catch(err => console.log('Centralized Catch:', err.message));\n\n// 3. Parallel Promise.all Chained with Sequential Step\nPromise.all([Promise.resolve('Task A'), Promise.resolve('Task B')])\n    .then(([r1, r2]) => {\n        console.log(`Parallel Results: ${r1}, ${r2}`);\n        return Promise.resolve('Final Task Complete');\n    })\n    .then(finalRes => console.log('Chained Final:', finalRes));",
        "output": "Step 1: User Loaded -> GFG Student\nStep 2: Total Orders Found -> 2\nValue: 5\nCentralized Catch: Step 2 Exception Triggered!\nParallel Results: Task A, Task B\nChained Final: Final Task Complete",
        "explanation": "Demonstrates dependent data flow through chained .then() calls, error propagation skipping steps to a single .catch(), and combining Promise.all parallel execution with sequential chaining.",
    },
    "fill_blanks": {
        "question": "// Each call to .then() returns a new _____, allowing further chaining.\n// Errors thrown anywhere inside a promise chain are caught by a single centralized ._____() block.",
        "answers": ["Promise", "catch"],
        "options": ["Promise", "catch", "then", "finally"],
    },
    "compiler": {
        "title": "Promise Chaining Sandbox",
        "question": "Complete the Promise chain multiplication sequence.",
        "starter_code": "Promise.resolve(5)\n    .____(num => num * 2)\n    .____(num => num + 3)\n    .then(val => console.log('Result:', val));",
        "options": ["then", "then", "catch", "resolve"],
    },
    "skill_exa_test": [
        {
            "question": "Why does Promise Chaining eliminate Callback Hell?",
            "options": [
                "It flattens asynchronous workflows into a sequential top-down structure using chained `.then()` calls instead of deeply nested functions",
                "It converts all asynchronous operations into synchronous loops",
                "It disables browser garbage collection",
                "It enforces strict typing on all function returns"
            ],
            "answer": "It flattens asynchronous workflows into a sequential top-down structure using chained `.then()` calls instead of deeply nested functions",
        },
        {
            "question": "What happens if a `.then()` callback returns a value `10` instead of a Promise?",
            "options": [
                "JavaScript automatically wraps the returned value in `Promise.resolve(10)` and passes it to the next `.then()`",
                "The promise chain breaks and stops executing",
                "It throws a TypeError",
                "It converts `10` into a string"
            ],
            "answer": "JavaScript automatically wraps the returned value in `Promise.resolve(10)` and passes it to the next `.then()`",
        },
        {
            "question": "What happens when an error is thrown inside the second `.then()` block of a 5-step promise chain?",
            "options": [
                "Subsequent `.then()` blocks are skipped, and control jumps directly to the nearest `.catch()` block",
                "The entire browser window freezes",
                "The chain ignores the error and continues executing remaining `.then()` blocks",
                "It restarts the chain from step 1"
            ],
            "answer": "Subsequent `.then()` blocks are skipped, and control jumps directly to the nearest `.catch()` block",
        },
        {
            "question": "How can data be passed from one asynchronous operation to another in a promise chain?",
            "options": [
                "By returning a value or Promise from inside a `.then()` handler, which receives it as the argument to the next `.then()`",
                "By setting global browser cookies",
                "By using `document.write()`",
                "By storing values in CSS variables"
            ],
            "answer": "By returning a value or Promise from inside a `.then()` handler, which receives it as the argument to the next `.then()`",
        },
        {
            "question": "What is the purpose of `.finally()` at the end of a promise chain?",
            "options": [
                "To execute cleanup logic regardless of whether the chain fulfilled or rejected",
                "To restart the promise chain automatically",
                "To convert the result into a JSON string",
                "To block UI rendering until network requests finish"
            ],
            "answer": "To execute cleanup logic regardless of whether the chain fulfilled or rejected",
        },
    ],
}

# Override Topic 88: Async/Await in JavaScript
JS_TOPICS[88] = {
    "id": 88,
    "title": "Async/Await",
    "category": "Asynchronous JavaScript",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "async/await is syntactic sugar built on Promises, allowing asynchronous non-blocking code to be written in a clean, synchronous-looking style with standard try...catch error handling.",
    "theory": "1. What is Async/Await?\nIntroduced in ES2017 (ES8), `async` and `await` simplify promise consumption. They make asynchronous code read like traditional synchronous step-by-step instructions without blocking the main event loop thread.\n\n2. The `async` Keyword:\n- Placed before a function declaration (`async function() { ... }`).\n- Transforms the function so that it **always returns a Promise**.\n- If the function returns a non-promise value, JavaScript automatically wraps it in `Promise.resolve()`.\n\n3. The `await` Keyword:\n- Placed before a Promise inside an `async` function (`const data = await promise;`).\n- Pauses the execution of the `async` function until the Promise settles (resolves or rejects).\n- Evaluates to the resolved value of the Promise.\n- Can ONLY be used inside `async` functions (or top-level modules).\n\n4. Error Handling with `try...catch`:\nInstead of chaining `.catch()`, errors in `await` calls are caught using standard synchronous `try { await ... } catch (error) { ... }` blocks.\n\n5. Parallel vs Sequential Execution:\n- Sequential: `const a = await task1(); const b = await task2();` (Wait for 1 before starting 2).\n- Parallel/Concurrent: `const [a, b] = await Promise.all([task1(), task2()]);` (Start both simultaneously).",
    "syntax": "async function fetchData() {\n    try {\n        const response = await fetch('https://api.example.com/data');\n        const data = await response.json();\n        console.log(data);\n    } catch (error) {\n        console.error('Error fetching data:', error.message);\n    }\n}",
    "example": {
        "code": "// 1. Async Function Returning Auto-Wrapped Promise\nconst getGreeting = async () => {\n    return 'Hello World from Async Function!';\n};\ngetGreeting().then(msg => console.log('Async Return:', msg));\n\n// 2. Await Keyword & Non-Blocking Execution Order\nconst processData = async () => {\n    let result = await Promise.resolve('Mock Fetch Completed');\n    console.log('Inside Async Function:', result);\n};\nconsole.log('1: Sync Start');\nprocessData();\nconsole.log('2: Sync End');\n\n// 3. Error Handling with try...catch\nasync function divideAsync(a, b) {\n    try {\n        if (b === 0) throw new Error('Divide by zero attempt');\n        let res = await Promise.resolve(a / b);\n        console.log(`Division Result: ${res}`);\n    } catch (err) {\n        console.log('Caught Async Error:', err.message);\n    }\n}\ndivideAsync(10, 2);\ndivideAsync(10, 0);",
        "output": "1: Sync Start\n2: Sync End\nAsync Return: Hello World from Async Function!\nInside Async Function: Mock Fetch Completed\nDivision Result: 5\nCaught Async Error: Divide by zero attempt",
        "explanation": "Demonstrates async functions wrapping return values in Promises, await pausing execution without blocking synchronous main thread, and try...catch error handling.",
    },
    "fill_blanks": {
        "question": "// An _____ function in JavaScript always returns a Promise.\n// The _____ keyword pauses execution of an async function until a Promise settles.",
        "answers": ["async", "await"],
        "options": ["async", "await", "defer", "promise"],
    },
    "compiler": {
        "title": "Async/Await & Error Handling Sandbox",
        "question": "Complete the async function with try...catch and await.",
        "starter_code": "_____ function getData() {\n    try {\n        let res = _____ Promise.resolve('Data Ready');\n        console.log(res);\n    } catch (err) {\n        console.error(err);\n    }\n}\ngetData();",
        "options": ["async", "await", "sync", "defer"],
    },
    "skill_exa_test": [
        {
            "question": "What does an `async` function in JavaScript always return?",
            "options": ["A Promise", "A Callback", "An Array", "Undefined"],
            "answer": "A Promise",
        },
        {
            "question": "Where can the `await` keyword be legally used in standard JavaScript code?",
            "options": [
                "Only inside `async` functions (or top-level ES modules)",
                "Inside any standard synchronous function",
                "Inside `for` loop headers only",
                "Inside CSS stylesheet blocks"
            ],
            "answer": "Only inside `async` functions (or top-level ES modules)",
        },
        {
            "question": "What happens when the `await` keyword is encountered inside an `async` function?",
            "options": [
                "It pauses execution of the `async` function until the Promise resolves or rejects, yielding thread control back to the event loop",
                "It blocks the entire browser thread, stopping user interactions",
                "It converts the Promise into a synchronous array",
                "It throws a SyntaxError"
            ],
            "answer": "It pauses execution of the `async` function until the Promise resolves or rejects, yielding thread control back to the event loop",
        },
        {
            "question": "How are rejection errors handled when using `async`/`await`?",
            "options": [
                "Using standard synchronous `try...catch` blocks around `await` expressions",
                "By passing error parameters into `await`",
                "Rejection errors are automatically ignored",
                "Using `.catch()` inside HTML attributes"
            ],
            "answer": "Using standard synchronous `try...catch` blocks around `await` expressions",
        },
        {
            "question": "How should two independent asynchronous tasks be awaited concurrently to optimize total execution time?",
            "options": [
                "Using `const [r1, r2] = await Promise.all([task1(), task2()]);`",
                "Using `const r1 = await task1(); const r2 = await task2();`",
                "Using a synchronous `while` loop",
                "Using `setTimeout()` around `await`"
            ],
            "answer": "Using `const [r1, r2] = await Promise.all([task1(), task2()]);`",
        },
    ],
}

# Override Topic 89: JSON Tutorial
JS_TOPICS[89] = {
    "id": 89,
    "title": "JSON Tutorial",
    "category": "JavaScript JSON",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "JSON (JavaScript Object Notation) is a lightweight, human-readable, text-based data format used extensively in Web APIs, configuration files, and cross-language client-server communication.",
    "theory": "1. What is JSON?\nJSON is a data interchange format derived from JavaScript object literal notation. It is language-independent and supported natively across Python, Java, C++, PHP, and Go.\n\n2. Features of JSON:\n- Human-Readable & Text-Based: Compact string representation easy to transmit across HTTP networks.\n- Language-Independent: Parsed natively into Python dicts (`json.loads`), Java objects (Jackson/Gson), or JS objects.\n- JSON vs XML: JSON is smaller, less verbose, faster to parse, and preferred for web APIs.\n\n3. JSON Data Flow (Server to Client):\n1. Server serializes object into JSON text string (`JSON.stringify(obj)`).\n2. String travels across HTTP API response stream.\n3. Client deserializes JSON string into native object (`JSON.parse(str)`).\n\n4. Data Types Supported in JSON:\nStrings (in double quotes), Numbers, Booleans (`true`/`false`), Objects (`{}`), Arrays (`[]`), and `null`.\n(Functions, `undefined`, and Symbols are NOT supported in standard JSON).",
    "syntax": "// Standard JSON String Format\nlet jsonString = '{\"name\": \"Mohit\", \"age\": 30, \"isStudent\": false}';\n\n// Parsing and Stringifying in JS\nlet obj = JSON.parse(jsonString);\nlet str = JSON.stringify(obj);",
    "example": {
        "code": "// 1. JSON String to JavaScript Object (JSON.parse)\nlet jsonString = '{\"name\": \"Mohit\", \"age\": 30, \"skills\": [\"JS\", \"Python\"]}';\nlet userObj = JSON.parse(jsonString);\nconsole.log('Parsed Object Name:', userObj.name);\nconsole.log('Parsed First Skill:', userObj.skills[0]);\n\n// 2. JavaScript Object to JSON String (JSON.stringify)\nlet student = { name: 'Anjali', score: 95, active: true };\nlet jsonText = JSON.stringify(student);\nconsole.log('Serialized JSON Text:', jsonText);\n\n// 3. Allowed vs Disallowed Data Types\nlet complexData = {\n    text: 'Hello',\n    num: 42,\n    nothing: null,\n    // Undefined & Functions are omitted in JSON!\n    temp: undefined,\n    sayHi() { return 'Hi'; }\n};\nconsole.log('Stripped JSON:', JSON.stringify(complexData));",
        "output": "Parsed Object Name: Mohit\nParsed First Skill: JS\nSerialized JSON Text: {\"name\":\"Anjali\",\"score\":95,\"active\":true}\nStripped JSON: {\"text\":\"Hello\",\"num\":42,\"nothing\":null}",
        "explanation": "Demonstrates parsing JSON strings into objects, stringifying objects into JSON text, and showing how undefined/functions are stripped during JSON serialization.",
    },
    "fill_blanks": {
        "question": "// The built-in JavaScript function used to parse a JSON string into an object is JSON._____().\n// The built-in JavaScript function used to convert an object into a JSON string is JSON._____().",
        "answers": ["parse", "stringify"],
        "options": ["parse", "stringify", "loads", "dumps"],
    },
    "compiler": {
        "title": "JSON Serialization & Parsing Sandbox",
        "question": "Complete the JSON parsing and stringifying code.",
        "starter_code": "let str = '{\"name\":\"Mohit\",\"age\":30}';\nlet obj = JSON._____(str);\nconsole.log(obj.name);\nlet json = JSON._____(obj);",
        "options": ["parse", "stringify", "convert", "encode"],
    },
    "skill_exa_test": [
        {
            "question": "What does JSON stand for?",
            "options": [
                "JavaScript Object Notation",
                "Java Standard Output Network",
                "JavaScript Online Namespace",
                "JSON Serialized Object System"
            ],
            "answer": "JavaScript Object Notation",
        },
        {
            "question": "Which of the following data types is NOT supported in standard JSON?",
            "options": ["Function / undefined", "String", "Number", "Array"],
            "answer": "Function / undefined",
        },
        {
            "question": "Why is JSON preferred over XML for modern Web APIs?",
            "options": [
                "JSON has smaller payload size, less markup verbosity, and is faster to parse in JavaScript",
                "JSON only runs on server hardware",
                "XML does not support numbers",
                "JSON encrypts all data automatically"
            ],
            "answer": "JSON has smaller payload size, less markup verbosity, and is faster to parse in JavaScript",
        },
        {
            "question": "In standard JSON formatting, how must keys and string values be enclosed?",
            "options": ["Double quotes only (\")", "Single quotes only (')", "Backticks (`)", "Unquoted"],
            "answer": "Double quotes only (\")",
        },
        {
            "question": "What happens when `JSON.stringify()` encounters a function property on an object?",
            "options": [
                "The function property is automatically omitted/stripped from the JSON output string",
                "It throws a Fatal SyntaxError",
                "It converts the function code into WebAssembly",
                "It wraps the function in HTML tags"
            ],
            "answer": "The function property is automatically omitted/stripped from the JSON output string",
        },
    ],
}

# Override Topic 90: JSON vs JavaScript Object
JS_TOPICS[90] = {
    "id": 90,
    "title": "JSON vs JavaScript Object",
    "category": "JavaScript JSON",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "While JSON and JavaScript Objects share similar syntax, JSON is a strict text-based data format for transmission, whereas JavaScript Objects are flexible in-memory data structures supporting executable methods.",
    "theory": "1. Purpose & Definition Differences:\n- **JSON**: Text-based string format for storing and transmitting data across heterogeneous systems.\n- **JavaScript Object**: In-memory data structure used for program logic and execution within a JavaScript application.\n\n2. Syntax Rules Comparison:\na. Keys:\n   - JSON: Keys MUST be enclosed in double quotes (`\"name\": \"Amit\"`).\n   - JS Object: Keys can be unquoted (`name: 'Amit'`) or quoted.\nb. String Values:\n   - JSON: String values MUST use double quotes (`\"Mumbai\"`).\n   - JS Object: Strings can use single quotes, double quotes, or template literals (`'Mumbai'`).\nc. Methods & Code:\n   - JSON: Cannot contain functions, methods, comments, or trailing commas.\n   - JS Object: Fully supports methods (`greet()`), closures, and internal execution logic.\nd. Data Types Supported:\n   - JSON: Limited to string, number, boolean, null, array, object.\n   - JS Object: Supports all JS types including `undefined`, `Function`, `Symbol`, `BigInt`.\n\n3. Converting Between JSON & Objects:\n- `JSON.parse(jsonText)`: Converts JSON string -> JS Object.\n- `JSON.stringify(jsObj)`: Converts JS Object -> JSON string.",
    "syntax": "// JSON String (Strict)\nconst jsonStr = '{\"name\": \"Amit\", \"age\": 25}';\n\n// JS Object (Flexible with Methods)\nconst userObj = {\n    name: 'Amit',\n    age: 25,\n    greet() { return `Hello ${this.name}`; }\n};",
    "example": {
        "code": "// 1. Flexible JavaScript Object with Method\nconst jsUser = {\n    name: 'Amit',\n    age: 25,\n    city: 'Mumbai',\n    greet: function() { return `Hello, I am ${this.name}`; }\n};\nconsole.log('JS Object Method Call:', jsUser.greet());\n\n// 2. Strict JSON String Representation\nconst jsonText = '{\"name\": \"Amit\", \"age\": 25, \"city\": \"Mumbai\"}';\nconsole.log('Type of JSON:', typeof jsonText);\n\n// 3. Converting Object to JSON (Method is stripped)\nconst convertedJSON = JSON.stringify(jsUser);\nconsole.log('Stringified Object (No Method):', convertedJSON);\n\n// 4. Converting JSON back to JS Object\nconst restoredObj = JSON.parse(jsonText);\nconsole.log('Restored Object Property:', restoredObj.city);",
        "output": "JS Object Method Call: Hello, I am Amit\nType of JSON: string\nStringified Object (No Method): {\"name\":\"Amit\",\"age\":25,\"city\":\"Mumbai\"}\nRestored Object Property: Mumbai",
        "explanation": "Demonstrates structural differences between JS objects containing methods and strict JSON strings, alongside JSON.stringify and JSON.parse conversions.",
    },
    "fill_blanks": {
        "question": "// Unlike JavaScript objects, keys in JSON strings must always be wrapped in _____ quotes.\n// Methods inside JavaScript objects are automatically _____ when converted to JSON using JSON.stringify().",
        "answers": ["double", "omitted"],
        "options": ["double", "omitted", "single", "preserved"],
    },
    "compiler": {
        "title": "JSON vs Object Comparison Sandbox",
        "question": "Complete conversion between JS object and JSON string.",
        "starter_code": "let obj = { name: 'Neha', age: 30 };\nlet json = JSON._____(obj);\nconsole.log(typeof json);\nlet back = JSON._____(json);\nconsole.log(back.name);",
        "options": ["stringify", "parse", "encode", "decode"],
    },
    "skill_exa_test": [
        {
            "question": "What is the primary fundamental difference between JSON and a JavaScript Object?",
            "options": [
                "JSON is a text string format for data exchange, whereas a JavaScript Object is an in-memory data structure for program logic",
                "JSON only runs in Python",
                "JavaScript Objects cannot store strings",
                "JSON allows executable functions"
            ],
            "answer": "JSON is a text string format for data exchange, whereas a JavaScript Object is an in-memory data structure for program logic",
        },
        {
            "question": "Are methods or functions allowed inside a JSON string?",
            "options": [
                "No, JSON is limited strictly to static data and cannot store executable functions",
                "Yes, using arrow function syntax",
                "Yes, but only in strict mode",
                "Yes, if passed inside square brackets"
            ],
            "answer": "No, JSON is limited strictly to static data and cannot store executable functions",
        },
        {
            "question": "What quote style is strictly required for property keys in JSON?",
            "options": ["Double quotes (\")", "Single quotes (')", "Backticks (`)", "No quotes"],
            "answer": "Double quotes (\")",
        },
        {
            "question": "Which method converts a JSON text string into a native JavaScript object?",
            "options": ["JSON.parse()", "JSON.stringify()", "JSON.toObject()", "JSON.decode()"],
            "answer": "JSON.parse()",
        },
        {
            "question": "Which JavaScript data type is valid in JS Objects but NOT supported in JSON format?",
            "options": ["undefined", "string", "boolean", "null"],
            "answer": "undefined",
        },
    ],
}

# Override Topic 91: Parse JSON Data in JS
JS_TOPICS[91] = {
    "id": 91,
    "title": "Parse JSON Data in JS",
    "category": "JavaScript JSON",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "Parsing JSON in JavaScript involves using JSON.parse() to transform a JSON text string into a usable JavaScript object or array, enabling safe property access and data manipulation.",
    "theory": "1. What is JSON Parsing?\nParsing converts raw incoming JSON string payloads from APIs or local files into native JavaScript objects, arrays, or primitive values.\n\n2. The `JSON.parse(text [, reviver])` Signature:\n- `text`: Valid JSON string to be parsed.\n- `reviver` (Optional): A transformation function `(key, value)` called for each key-value pair, allowing values to be mutated or cast during parsing.\n\n3. Common Parsing Scenarios:\na. Simple Objects: `JSON.parse('{\"name\": \"Mohit\"}')`.\nb. Array Strings: `JSON.parse('[{\"id\": 1}, {\"id\": 2}]')`.\nc. Nested Structures: `JSON.parse('{\"user\": {\"address\": {\"city\": \"Delhi\"}}}')`.\n\n4. Validation & Safe Error Handling (`try...catch`):\nIf `JSON.parse()` encounters malformed JSON (missing quotes, trailing commas, single quotes), it throws a `SyntaxError`. Always wrap parsing logic in a `try...catch` block when processing external data.\n\n5. Reviver Function Transformation:\nAllows dynamic type conversions during parsing (e.g. converting ISO date strings into `Date` instances or stringified numbers into integers).",
    "syntax": "// Simple Parsing\nconst obj = JSON.parse(jsonText);\n\n// Parsing with Reviver Function\nconst data = JSON.parse(jsonText, (key, val) => {\n    if (key === 'age') return Number(val);\n    return val;\n});",
    "example": {
        "code": "// 1. Parsing Simple & Nested JSON Strings\nconst nestedJSON = '{\"person\": {\"name\": \"Anjali\", \"address\": {\"city\": \"Noida\"}}}';\nconst parsedObj = JSON.parse(nestedJSON);\nconsole.log('City:', parsedObj.person.address.city);\n\n// 2. Parsing JSON Array Strings\nconst arrayJSON = '[{\"id\": 101, \"name\": \"Rahul\"}, {\"id\": 102, \"name\": \"Priya\"}]';\nconst users = JSON.parse(arrayJSON);\nusers.forEach(u => console.log(`User ${u.id}: ${u.name}`));\n\n// 3. Parsing with Reviver Function\nconst rawData = '{\"title\": \"JS Book\", \"price\": \"500\"}';\nconst parsedWithReviver = JSON.parse(rawData, (key, value) => {\n    if (key === 'price') return parseInt(value, 10); // Cast to integer\n    return value;\n});\nconsole.log('Parsed Price Type:', typeof parsedWithReviver.price, '| Value:', parsedWithReviver.price);\n\n// 4. Safe Parsing with try...catch\ntry {\n    const badJSON = '{name: \"UnquotedKey\"}'; // Malformed JSON!\n    JSON.parse(badJSON);\n} catch (err) {\n    console.log('Caught Invalid JSON Error:', err.name);\n}",
        "output": "City: Noida\nUser 101: Rahul\nUser 102: Priya\nParsed Price Type: number | Value: 500\nCaught Invalid JSON Error: SyntaxError",
        "explanation": "Demonstrates parsing nested JSON, array strings, transforming data types using a reviver function, and safely handling malformed JSON via try...catch.",
    },
    "fill_blanks": {
        "question": "// Parsing malformed JSON strings causes JSON.parse() to throw a _____.\n// The optional second argument to JSON.parse() used to transform values during parsing is called a _____ function.",
        "answers": ["SyntaxError", "reviver"],
        "options": ["SyntaxError", "reviver", "TypeError", "replacer"],
    },
    "compiler": {
        "title": "JSON Parsing & Reviver Sandbox",
        "question": "Complete the JSON.parse reviver transformation.",
        "starter_code": "let json = '{\"qty\": \"10\"}';\nlet data = JSON.parse(json, (key, val) => {\n    if (key === 'qty') return _____(val);\n    return val;\n});\nconsole.log(typeof data.qty);",
        "options": ["Number", "String", "Boolean", "Object"],
    },
    "skill_exa_test": [
        {
            "question": "What exception does `JSON.parse()` throw if given an invalid JSON string?",
            "options": ["SyntaxError", "TypeError", "ReferenceError", "URIError"],
            "answer": "SyntaxError",
        },
        {
            "question": "What is the purpose of the optional `reviver` function parameter in `JSON.parse(text, reviver)`?",
            "options": [
                "To inspect or transform key-value pairs before the parsed object is returned",
                "To encrypt the output object",
                "To format the JSON text with indentation spaces",
                "To download the JSON string to local disk"
            ],
            "answer": "To inspect or transform key-value pairs before the parsed object is returned",
        },
        {
            "question": "Why should `JSON.parse()` calls be wrapped inside `try...catch` blocks when dealing with external API responses?",
            "options": [
                "To prevent malformed or invalid JSON payloads from crashing the application",
                "To speed up parsing performance by 2x",
                "To convert XML into JSON automatically",
                "To enforce HTTPS connections"
            ],
            "answer": "To prevent malformed or invalid JSON payloads from crashing the application",
        },
        {
            "question": "Which of the following JSON strings will cause `JSON.parse()` to fail?",
            "options": [
                "'{ \"name\": \'Mohit\' }' (single quotes around string value)",
                "'{\"name\": \"Mohit\"}'",
                "'[1, 2, 3]'",
                "'{\"active\": true}'"
            ],
            "answer": "'{ \"name\": \'Mohit\' }' (single quotes around string value)",
        },
        {
            "question": "How do you access a nested property `city` after parsing `{\"user\": {\"city\": \"Delhi\"}}` into variable `data`?",
            "options": ["data.user.city", "data[\"user.city\"]", "data.get(\"user.city\")", "data->user->city"],
            "answer": "data.user.city",
        },
    ],
}

# Override Topic 92: JavaScript JSON Parser
JS_TOPICS[92] = {
    "id": 92,
    "title": "JavaScript JSON Parser",
    "category": "JavaScript JSON",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "A JSON parser converts JSON strings into structured JavaScript objects or arrays, mapping JSON primitives into native language data types for efficient manipulation in application logic.",
    "theory": "1. What is a JSON Parser?\nA JSON parser is a engine component or library method that reads formatted JSON text and constructs equivalent in-memory data structures (Objects and Arrays).\n\n2. Type Mapping Rules:\n- JSON Object (`{...}`) -> JavaScript `Object` (`{...}`).\n- JSON Array (`[...]`) -> JavaScript `Array` (`[...]`).\n- JSON String (`\"text\"`) -> JavaScript `String` (`\"text\"`).\n- JSON Number (`100`) -> JavaScript `Number` (`100`).\n- JSON Boolean (`true`/`false`) -> JavaScript `Boolean` (`true`/`false`).\n- JSON Null (`null`) -> JavaScript `null`.\n\n3. Reversibility & Data Type Loss:\nConversion between JS Objects and JSON is *reversible* for basic data types, but lossy for advanced types:\n- Functions, `undefined`, and `Symbol` properties are omitted.\n- `Date` objects are converted to ISO string representations.\n- `NaN` and `Infinity` become `null`.\n\n4. Node.js Native JSON Loading:\nIn Node.js CommonJS, `require('./data.json')` acts as a native JSON parser, reading and returning the parsed JavaScript object synchronously.",
    "syntax": "// Standard Parser Execution\nconst obj = JSON.parse(jsonStr);\n\n// Node.js Synchronous Require Parser\nconst config = require('./config.json');",
    "example": {
        "code": "// 1. Data Type Mapping in JSON Parser\nconst rawJSON = '{\"title\": \"GFG\", \"views\": 1500, \"verified\": true, \"tags\": [\"JS\", \"Web\"], \"meta\": null}';\nconst parsed = JSON.parse(rawJSON);\n\nconsole.log('Type of views:', typeof parsed.views);\nconsole.log('Is tags an Array?:', Array.isArray(parsed.tags));\nconsole.log('Meta value:', parsed.meta);\n\n// 2. Demonstrating Data Loss in Round-Trip Parsing\nconst originalObj = {\n    name: 'Test',\n    unassigned: undefined,\n    date: new Date('2026-01-01'),\n    notANumber: NaN,\n    func() { return 'Hello'; }\n};\nconst stringified = JSON.stringify(originalObj);\nconst roundTripObj = JSON.parse(stringified);\n\nconsole.log('Stringified:', stringified);\nconsole.log('Round-Trip Date Type:', typeof roundTripObj.date, '| Value:', roundTripObj.date);\nconsole.log('Round-Trip NaN value:', roundTripObj.notANumber);\nconsole.log('Has Function?:', 'func' in roundTripObj);",
        "output": "Type of views: number\nIs tags an Array?: true\nMeta value: null\nStringified: {\"name\":\"Test\",\"date\":\"2026-01-01T00:00:00.000Z\",\"notANumber\":null}\nRound-Trip Date Type: string | Value: 2026-01-01T00:00:00.000Z\nRound-Trip NaN value: null\nHas Function?: false",
        "explanation": "Demonstrates type mappings produced by the JSON parser, and shows how dates become ISO strings while NaN becomes null and functions are stripped.",
    },
    "fill_blanks": {
        "question": "// The JSON parser converts JSON array representations [...] into native JavaScript _____ objects.\n// During JSON serialization and parsing, NaN values are mapped to _____.",
        "answers": ["Array", "null"],
        "options": ["Array", "null", "Object", "undefined"],
    },
    "compiler": {
        "title": "JSON Parser Type Mapping Sandbox",
        "question": "Inspect parsed JSON data types.",
        "starter_code": "let json = '{\"count\": 10, \"list\": [1,2,3]}';\nlet data = JSON.parse(json);\nconsole.log(typeof data.count);\nconsole.log(Array.isArray(data.list));",
        "options": ["parse", "stringify", "convert", "type"],
    },
    "skill_exa_test": [
        {
            "question": "What does a JSON parser do?",
            "options": [
                "Converts JSON formatted text strings into native structured data types like JavaScript objects or arrays",
                "Compiles HTML tags into CSS rules",
                "Compresses image files for fast web delivery",
                "Parses SQL database tables into XML"
            ],
            "answer": "Converts JSON formatted text strings into native structured data types like JavaScript objects or arrays",
        },
        {
            "question": "What happens to `NaN` values during `JSON.stringify()` and `JSON.parse()` round-trip conversion?",
            "options": ["They are converted into `null`", "They remain `NaN`", "They throw a TypeError", "They become `0`"],
            "answer": "They are converted into `null`",
        },
        {
            "question": "How are JavaScript `Date` objects formatted when converted to JSON?",
            "options": ["Converted into ISO 8601 UTC date string format", "Converted into Unix timestamp numbers", "Omitted completely", "Converted into binary buffer"],
            "answer": "Converted into ISO 8601 UTC date string format",
        },
        {
            "question": "In Node.js CommonJS modules, how can local `.json` files be loaded and automatically parsed?",
            "options": [
                "Using `const data = require('./file.json');`",
                "Using `const data = JSON.load('./file.json');`",
                "Using `const data = fs.parse('./file.json');`",
                "Using `window.readJSON('./file.json');`"
            ],
            "answer": "Using `const data = require('./file.json');`",
        },
        {
            "question": "Are property order guarantees maintained when parsing JSON into JavaScript objects?",
            "options": [
                "Standard JavaScript objects do not guarantee key order for non-integer keys, though JSON preserves insertion sequence",
                "Yes, key order is strictly immutable across all environments",
                "No, keys are automatically sorted alphabetically",
                "Keys are reversed"
            ],
            "answer": "Standard JavaScript objects do not guarantee key order for non-integer keys, though JSON preserves insertion sequence",
        },
    ],
}

# Override Topic 93: Read JSON File Using JS
JS_TOPICS[93] = {
    "id": 93,
    "title": "Read JSON File Using JS",
    "category": "JavaScript JSON",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "JavaScript provides multiple techniques to read and parse JSON files, including the browser fetch() API, Node.js require(), ES Modules import assertions, and the Node.js fs module.",
    "theory": "1. Web Browser Context (`fetch()` API):\n- Asynchronously fetches local or remote `.json` files across HTTP.\n- Returns a Response stream; calling `response.json()` parses the JSON text into a Promise.\n```js\nfetch('./sample.json')\n    .then(res => res.json())\n    .then(data => console.log(data))\n    .catch(err => console.error(err));\n```\n\n2. Node.js CommonJS Context (`require()`):\n- Synchronously loads and automatically parses local `.json` files.\n```js\nconst sampleData = require('./sample.json');\n```\n\n3. ES Modules Context (`import` assertions / attributes):\n- Uses `import ... assert { type: 'json' }` (or `with { type: 'json' }`).\n- Standardized syntax supported in modern browsers and Node.js v17+.\n```js\nimport jsonData from './sample.json' assert { type: 'json' };\n```\n\n4. Node.js Asynchronous File System (`fs.promises`):\n- Reads JSON text file asynchronously using `fs.promises.readFile()` then parses via `JSON.parse()`.\n```js\nconst raw = await fs.promises.readFile('sample.json', 'utf-8');\nconst data = JSON.parse(raw);\n```",
    "syntax": "// Browser Fetch API\nfetch('data.json')\n    .then(response => response.json())\n    .then(data => console.log(data));\n\n// Node.js CommonJS Require\nconst data = require('./data.json');",
    "example": {
        "code": "// 1. Mocking Fetch API for Reading JSON File\nfunction mockFetchJSON(filePath) {\n    return Promise.resolve({\n        ok: true,\n        json: () => Promise.resolve({ name: 'Johina', age: 30, profession: 'Developer' })\n    });\n}\nmockFetchJSON('./sample.json')\n    .then(res => res.json())\n    .then(data => {\n        console.log('Fetch API Data Loaded:');\n        console.log(`Name: ${data.name} | Role: ${data.profession}`);\n    });\n\n// 2. Simulating Node.js require('./sample.json')\nconst mockRequireJSON = (path) => ({ dataset: ['Item A', 'Item B'], count: 2 });\nconst localData = mockRequireJSON('./sample.json');\nconsole.log('Node.js require() Data Count:', localData.count);\n\n// 3. Simulating Node.js fs.readFile + JSON.parse\nconst rawFileContent = '{\"status\": \"OK\", \"code\": 200}';\nconst parsedFile = JSON.parse(rawFileContent);\nconsole.log('fs.readFile Parsed Status:', parsedFile.status);",
        "output": "Fetch API Data Loaded:\nName: Johina | Role: Developer\nNode.js require() Data Count: 2\nfs.readFile Parsed Status: OK",
        "explanation": "Demonstrates fetching and parsing JSON asynchronously using fetch().json(), loading JSON in Node.js via require(), and parsing raw file strings with JSON.parse().",
    },
    "fill_blanks": {
        "question": "// In browser environments, the asynchronous API used to retrieve and parse JSON files is _____().\n// In Node.js CommonJS modules, local JSON files can be synchronously loaded using _____('./file.json').",
        "answers": ["fetch", "require"],
        "options": ["fetch", "require", "import", "read"],
    },
    "compiler": {
        "title": "Read JSON File Sandbox",
        "question": "Complete the fetch API JSON response parsing.",
        "starter_code": "function loadJSON() {\n    return Promise.resolve({ json: () => Promise.resolve({ success: true }) });\n}\nloadJSON()\n    .then(res => res.____())\n    .then(data => console.log(data.success));",
        "options": ["json", "text", "parse", "data"],
    },
    "skill_exa_test": [
        {
            "question": "How do you parse the JSON response body when using the browser `fetch()` API?",
            "options": ["By calling `response.json()`, which returns a Promise resolving to the parsed object", "By calling `JSON.parse(response)` directly", "By using `response.text()` without parsing", "By calling `response.toObject()`"],
            "answer": "By calling `response.json()`, which returns a Promise resolving to the parsed object",
        },
        {
            "question": "In Node.js CommonJS environment, how can a local `config.json` file be read synchronously?",
            "options": ["const config = require('./config.json');", "const config = fetch('./config.json');", "const config = window.loadJSON('./config.json');", "const config = JSON.read('./config.json');"],
            "answer": "const config = require('./config.json');",
        },
        {
            "question": "What is the ES Module import syntax with assertions for loading JSON files in modern JavaScript?",
            "options": [
                "import data from './file.json' assert { type: 'json' };",
                "import data from './file.json' as JSON;",
                "require('./file.json') with { format: 'json' };",
                "include './file.json';"
            ],
            "answer": "import data from './file.json' assert { type: 'json' };",
        },
        {
            "question": "If you read a JSON file using Node's `fs.promises.readFile()`, what step is required before accessing properties?",
            "options": ["Passing the returned UTF-8 string into `JSON.parse()`", "Calling `file.read()`", "No step needed; it parses automatically", "Decoding Base64"],
            "answer": "Passing the returned UTF-8 string into `JSON.parse()`",
        },
        {
            "question": "What happens if a JSON file requested via `fetch()` returns a 404 HTTP status?",
            "options": [
                "The response `response.ok` property is false, and attempting `response.json()` will likely fail to parse HTML error pages",
                "fetch automatically retries 5 times",
                "It returns null quietly",
                "It throws a CSS error"
            ],
            "answer": "The response `response.ok` property is false, and attempting `response.json()` will likely fail to parse HTML error pages",
        },
    ],
}

# Override Topic 94: Regular Expressions
JS_TOPICS[94] = {
    "id": 94,
    "title": "Regular Expressions",
    "category": "Regular Expression and Validation",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "JavaScript RegExp (Regular Expressions) are patterns used to search, match, extract, and manipulate text strings in JavaScript.",
    "theory": "1. Creating Regular Expressions:\n- Literal Notation: `/pattern/flags` (static compilation at parse time).\n- RegExp Constructor: `new RegExp('pattern', 'flags')` (dynamic creation at runtime).\n\n2. RegExp Flags:\n- `g` (global): Find all matches rather than stopping at the first.\n- `i` (ignoreCase): Perform case-insensitive pattern matching.\n- `m` (multiline): Treat beginning (`^`) and end (`$`) assertions across multiple lines.\n\n3. Character Classes & Range Brackets:\n- `[abc]`: Match any single character inside brackets.\n- `[^abc]`: Match any character NOT inside brackets.\n- `[0-9]`: Match any digit between 0 and 9.\n- `(x|y)`: Match alternative pattern x or y.\n\n4. Common Metacharacters:\n- `\\d` / `\\D`: Digit / Non-digit.\n- `\\w` / `\\W`: Word character (`[a-zA-Z0-9_]`) / Non-word character.\n- `\\s` / `\\S`: Whitespace / Non-whitespace.\n- `\\b` / `\\B`: Word boundary / Non-word boundary.\n- `.`: Match any single character except line terminators.\n\n5. Quantifiers:\n- `+` (1 or more), `*` (0 or more), `?` (0 or 1), `{X,Y}` (between X and Y times).\n- `^` (start of string), `$` (end of string).\n\n6. Primary Methods:\n- `regex.test(string)`: Returns `true` or `false`.\n- `regex.exec(string)`: Returns match array or `null`.\n- `string.match(regex)`: Returns array of matches.\n- `string.replace(regex, replacement)`: Replaces matched text.",
    "syntax": "// Literal Syntax\nconst regex = /pattern/flags;\n\n// Constructor Syntax\nconst regex = new RegExp('pattern', 'flags');\n\n// Testing a match\nconst isValid = regex.test('sample string');",
    "example": {
        "code": "// 1. Literal vs RegExp Constructor\nconst patt = /Geeks/i;\nconst dynamicPatt = new RegExp('geeks', 'i');\nconst s1 = 'geeksforgeeks';\nconst s2 = 'forgeeks';\n\nconsole.log('Patt Test s1:', patt.test(s1));\nconsole.log('Patt Test s2:', patt.test(s2));\nconsole.log('Dynamic Test s1:', dynamicPatt.test(s1));\n\n// 2. Extracting Numbers using Regex (\\d+ with global flag g)\nconst text = 'There are 123 apples and 456 oranges';\nconst numbers = text.match(/\\d+/g);\nconsole.log('Extracted Digits:', numbers.join(', '));\n\n// 3. Substring Replacement\nconst message = 'foo bar foo';\nconst replaced = message.replace(/foo/g, 'baz');\nconsole.log('Replaced String:', replaced);",
        "output": "Patt Test s1: true\nPatt Test s2: true\nDynamic Test s1: true\nExtracted Digits: 123, 456\nReplaced String: baz bar baz",
        "explanation": "Demonstrates creating regular expressions using literal and constructor syntax, extracting numeric patterns with match(), and replacing substrings with replace().",
    },
    "fill_blanks": {
        "question": "// The RegExp flag used for case-insensitive matching is _____.\n// The RegExp method that tests if a string matches a pattern and returns true or false is _____().",
        "answers": ["i", "test"],
        "options": ["i", "test", "g", "match"],
    },
    "compiler": {
        "title": "Regular Expressions Sandbox",
        "question": "Complete the regex test function.",
        "starter_code": "let pattern = /hello/____;\nlet str = 'Hello World';\nconsole.log(pattern.____(str));",
        "options": ["i", "test", "g", "match"],
    },
    "skill_exa_test": [
        {
            "question": "What is the primary difference between regular expression literal notation `/pattern/i` and `new RegExp('pattern', 'i')`?",
            "options": [
                "Literal notation is evaluated when the script is parsed, while the RegExp constructor allows dynamic regex compilation at runtime",
                "Literal notation only works in browsers while constructor works only in Node.js",
                "Constructor regexes cannot use flags",
                "Literal notation converts text into uppercase automatically"
            ],
            "answer": "Literal notation is evaluated when the script is parsed, while the RegExp constructor allows dynamic regex compilation at runtime",
        },
        {
            "question": "Which metacharacter matches any word character (letters, digits, and underscores)?",
            "options": ["\\w", "\\d", "\\s", "\\b"],
            "answer": "\\w",
        },
        {
            "question": "What does the `g` flag stand for in JavaScript Regular Expressions?",
            "options": [
                "Global match (find all occurrences rather than stopping after the first match)",
                "Group matching",
                "Greedy search mode",
                "Generate array"
            ],
            "answer": "Global match (find all occurrences rather than stopping after the first match)",
        },
        {
            "question": "What does `\\d+` match in a regular expression?",
            "options": [
                "One or more consecutive numeric digits",
                "Exactly one non-digit character",
                "Zero digits only",
                "A single decimal point"
            ],
            "answer": "One or more consecutive numeric digits",
        },
        {
            "question": "What value does `regex.test(string)` return?",
            "options": [
                "A boolean (`true` if a match is found, `false` otherwise)",
                "An array containing all matched substrings",
                "The index of the match",
                "A new regular expression instance"
            ],
            "answer": "A boolean (`true` if a match is found, `false` otherwise)",
        },
    ],
}

# Override Topic 95: Form Validation
JS_TOPICS[95] = {
    "id": 95,
    "title": "Form Validation",
    "category": "Regular Expression and Validation",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "Form Validation verifies user inputs before submission, preventing invalid, blank, or malformed data from being sent to the server.",
    "theory": "1. Purpose of Form Validation:\n- Prevents incomplete or invalid data entry.\n- Improves UX by highlighting errors next to invalid fields.\n- Reduces server load and protects against basic input errors.\n\n2. Two Primary Approaches:\na. Conditional Logic: Checks empty strings (`field === ''`), minimum length (`pass.length < 6`), and boolean flags (`agree.checked`).\nb. Regular Expression (Regex): Matches structured formats (email patterns, phone numbers, password strength rules).\n\n3. Preventing Default Form Submission:\nIn event handlers, `e.preventDefault()` (or `return false` in inline `onsubmit`) blocks form submission when errors are detected.\n\n4. Displaying & Resetting Errors:\n- Error messages are rendered inside dedicated `<span>` or `<div>` container elements.\n- A helper `resetErrors()` function clears text content across error spans before each new validation run or form reset.",
    "syntax": "// Intercepting Form Submission\nform.addEventListener('submit', function(e) {\n    e.preventDefault();\n    let isValid = validateForm();\n    if (isValid) {\n        // Submit form\n    }\n});",
    "example": {
        "code": "// Simulating Form Validation Function\nfunction validateRegistrationForm(inputData) {\n    const errors = {};\n    let isValid = true;\n\n    // 1. Name Check (non-empty & no digits)\n    if (!inputData.name || /\\d/.test(inputData.name)) {\n        errors.name = 'Please enter your name properly.';\n        isValid = false;\n    }\n\n    // 2. Email Check (basic syntax)\n    if (!inputData.email || !inputData.email.includes('@') || !inputData.email.includes('.')) {\n        errors.email = 'Please enter a valid email address.';\n        isValid = false;\n    }\n\n    // 3. Password Check (min length 6)\n    if (!inputData.password || inputData.password.length < 6) {\n        errors.password = 'Please enter a password with at least 6 characters.';\n        isValid = false;\n    }\n\n    return { isValid, errors };\n}\n\nconst invalidSubmission = { name: 'Rahul123', email: 'rahul.com', password: '123' };\nconst result = validateRegistrationForm(invalidSubmission);\nconsole.log('Form Is Valid?:', result.isValid);\nconsole.log('Name Error:', result.errors.name);\nconsole.log('Email Error:', result.errors.email);\nconsole.log('Password Error:', result.errors.password);",
        "output": "Form Is Valid?: false\nName Error: Please enter your name properly.\nEmail Error: Please enter a valid email address.\nPassword Error: Please enter a password with at least 6 characters.",
        "explanation": "Demonstrates multi-field form validation checking string conditions, regex pattern constraints, and returning targeted error messages.",
    },
    "fill_blanks": {
        "question": "// To prevent a form from submitting automatically when validation fails, call e._____().\n// Clearing error spans before validating ensures a _____ state for user feedback.",
        "answers": ["preventDefault", "clean"],
        "options": ["preventDefault", "clean", "stopImmediatePropagation", "blank"],
    },
    "compiler": {
        "title": "Form Validation Sandbox",
        "question": "Complete the form submission prevention check.",
        "starter_code": "function handleSubmit(e, isValid) {\n    if (!isValid) {\n        e._____();\n        console.log('Submission blocked');\n    }\n}",
        "options": ["preventDefault", "stopPropagation", "cancel", "stop"],
    },
    "skill_exa_test": [
        {
            "question": "Why is calling `event.preventDefault()` essential inside a form submit event listener?",
            "options": [
                "It stops the browser from executing its default page refresh/form POST action when validation fails",
                "It clears all input field values automatically",
                "It disables CSS styling on input fields",
                "It sends an AJAX request to the backend server"
            ],
            "answer": "It stops the browser from executing its default page refresh/form POST action when validation fails",
        },
        {
            "question": "What is the recommended practice for displaying input validation errors to users?",
            "options": [
                "Dynamically updating text content inside dedicated error `<span>` or `<div>` elements placed next to each field",
                "Displaying 10 consecutive `alert()` popups",
                "Printing errors to system log files",
                "Deleting the entire `<form>` element"
            ],
            "answer": "Dynamically updating text content inside dedicated error `<span>` or `<div>` elements placed next to each field",
        },
        {
            "question": "Which approach is best suited for complex pattern checks like email format or phone number validation?",
            "options": ["Regular Expressions (Regex)", "Simple equality checks (`===`)", "Math.random()", "setTimeout()"],
            "answer": "Regular Expressions (Regex)",
        },
        {
            "question": "What should be done with existing error message labels before running a new form validation routine?",
            "options": [
                "Reset/clear all error message strings to avoid displaying outdated errors",
                "Hide the entire web page",
                "Append duplicate text to existing errors",
                "Reload the web browser tab"
            ],
            "answer": "Reset/clear all error message strings to avoid displaying outdated errors",
        },
        {
            "question": "How can you check if a name input contains invalid numeric digits in JavaScript?",
            "options": ["Using `/\\d/.test(name)`", "Using `name === number`", "Using `name.toUpperCase()`", "Using `name.split('')`"],
            "answer": "Using `/\\d/.test(name)`",
        },
    ],
}

# Override Topic 96: Email Validation
JS_TOPICS[96] = {
    "id": 96,
    "title": "Email Validation",
    "category": "Regular Expression and Validation",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "Email validation in JavaScript verifies that user input matches the standard email structure (username@domain.tld) using regular expression pattern matching.",
    "theory": "1. Why Validate Emails?\n- Ensures correct communication address formatting before server processing.\n- Improves user data accuracy and prevents invalid form submissions.\n- Provides immediate visual feedback to the user.\n\n2. Standard Email Regular Expression:\n`/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/`\n\n3. Breakdown of Email Regex Pattern:\n- `^`: Matches start of the string.\n- `[a-zA-Z0-9._%+-]+`: Matches username part (alphanumeric plus `.`, `_`, `%`, `+`, `-`).\n- `@`: Matches the literal '@' character.\n- `[a-zA-Z0-9.-]+`: Matches domain name (alphanumeric, dots, hyphens).\n- `\\.`: Escapes period to match the literal dot before TLD.\n- `[a-zA-Z]{2,}$`: Matches top-level domain (at least 2 letters, e.g. `.com`, `.org`, `.in`).\n\n4. Validation Methods:\n- `regex.test(email)`: Returns `true` if email is valid, `false` otherwise.\n- `email.match(regex)`: Returns array of match results or `null` if invalid.",
    "syntax": "// Standard Email Validation Regex\nconst emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;\n\n// Check Email Validity\nconst isValid = emailRegex.test('user@example.com');",
    "example": {
        "code": "// 1. Email Regex Pattern Definition\nconst emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;\n\n// 2. Testing Email Candidates using test()\nconst email1 = 'test@example.com';\nconst email2 = 'invalid-email@com';\nconst email3 = 'user@domain.';\n\nconsole.log(`${email1} ->`, emailRegex.test(email1));\nconsole.log(`${email2} ->`, emailRegex.test(email2));\nconsole.log(`${email3} ->`, emailRegex.test(email3));\n\n// 3. Testing with match() Method\nconst matchResult = email1.match(emailRegex);\nconsole.log('Matched Email String:', matchResult ? matchResult[0] : 'No Match');",
        "output": "test@example.com -> true\ninvalid-email@com -> false\nuser@domain. -> false\nMatched Email String: test@example.com",
        "explanation": "Demonstrates evaluating valid and invalid email addresses using standard regular expression pattern matching via test() and match().",
    },
    "fill_blanks": {
        "question": "// In email regex, the escaped period \\. matches the literal _____ character before the top-level domain.\n// To ensure the top-level domain has at least 2 letters, we use [a-zA-Z]{____,}$.",
        "answers": ["dot", "2"],
        "options": ["dot", "2", "at", "3"],
    },
    "compiler": {
        "title": "Email Validation Sandbox",
        "question": "Complete email validation test.",
        "starter_code": "let regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;\nlet mail = 'admin@skillexa.com';\nif (regex.____(mail)) {\n    console.log('Valid');\n}",
        "options": ["test", "match", "check", "verify"],
    },
    "skill_exa_test": [
        {
            "question": "In the regex `/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/`, what does `\\.` match?",
            "options": [
                "The literal dot character (`.`) separating domain name and domain extension",
                "Any single character except newline",
                "The `@` symbol",
                "A whitespace character"
            ],
            "answer": "The literal dot character (`.`) separating domain name and domain extension",
        },
        {
            "question": "What does `[a-zA-Z]{2,}$` enforce at the end of the email regex?",
            "options": [
                "The Top-Level Domain (TLD) must consist of at least 2 alphabetic characters at the end of the string",
                "The email must end with 2 digits",
                "The username must have exactly 2 characters",
                "The email must contain 2 `@` symbols"
            ],
            "answer": "The Top-Level Domain (TLD) must consist of at least 2 alphabetic characters at the end of the string",
        },
        {
            "question": "What is returned by `email.match(regex)` if the email string fails validation?",
            "options": ["`null`", "`false`", "`undefined`", "`[]` (empty array)"],
            "answer": "`null`",
        },
        {
            "question": "Why is client-side email validation useful?",
            "options": [
                "Provides instant user feedback and prevents accidental typos before form submission",
                "Replaces backend database email verification completely",
                "Guarantees that the email inbox actually exists on the remote mail server",
                "Encrypts the user's password"
            ],
            "answer": "Provides instant user feedback and prevents accidental typos before form submission",
        },
        {
            "question": "Which symbol separates username from domain name in standard email addresses?",
            "options": ["`@`", "`.`", "`#`", "`$`"],
            "answer": "`@`",
        },
    ],
}

# Override Topic 97: Number Validation
JS_TOPICS[97] = {
    "id": 97,
    "title": "Number Validation",
    "category": "Regular Expression and Validation",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "Number validation ensures user inputs contain valid numeric values, checking types, integers, decimals, ranges, sign, and strict regex patterns.",
    "theory": "1. Methods for Number Validation:\na. Type & NaN Check: `typeof n === 'number' && !isNaN(n)`.\nb. Numeric String & Finite Check: `!isNaN(s) && isFinite(s)`.\nc. Integer Validation: `Number.isInteger(n)`.\nd. Float Validation: `typeof n === 'number' && !Number.isInteger(n)`.\ne. Range Checking: `n >= min && n <= max`.\nf. Sign & Parity Validation: Positive (`n > 0`), Negative (`n < 0`), Even (`n % 2 === 0`), Odd (`n % 2 !== 0`).\n\n2. Strict Regex Validation for Numeric Strings:\n`/^-?\\d+(\\.\\d+)?$/`\n- `^-?`: Optional negative sign.\n- `\\d+`: One or more integer digits.\n- `(\\.\\d+)?$`: Optional decimal part followed by end of string.",
    "syntax": "// Check Numeric Value\nconst isNum = n => typeof n === 'number' && !isNaN(n);\n\n// Strict Numeric Regex\nconst isStrictNumeric = s => /^-?\\d+(\\.\\d+)?$/.test(s);",
    "example": {
        "code": "// 1. Number & Numeric String Validation\nconst isNumStr = s => !isNaN(s) && isFinite(s);\nconsole.log(\"isNumStr '123':\", isNumStr('123'));\nconsole.log(\"isNumStr '123abc':\", isNumStr('123abc'));\n\n// 2. Integer & Float Validation\nconsole.log('Number.isInteger(42):', Number.isInteger(42));\nconsole.log('Number.isInteger(3.14):', Number.isInteger(3.14));\n\n// 3. Strict Regex Validation\nconst isStrict = s => /^-?\\d+(\\.\\d+)?$/.test(s);\nconsole.log(\"isStrict '123':\", isStrict('123'));\nconsole.log(\"isStrict '-123.45':\", isStrict('-123.45'));\nconsole.log(\"isStrict 'abc123':\", isStrict('abc123'));\n\n// 4. Range & Parity Validation\nconst inRange = (n, min, max) => n >= min && n <= max;\nconst isEven = n => typeof n === 'number' && n % 2 === 0;\nconsole.log('Is 10 in 5..15?:', inRange(10, 5, 15));\nconsole.log('Is 4 Even?:', isEven(4));",
        "output": "isNumStr '123': true\nisNumStr '123abc': false\nNumber.isInteger(42): true\nNumber.isInteger(3.14): false\nisStrict '123': true\nisStrict '-123.45': true\nisStrict 'abc123': false\nIs 10 in 5..15?: true\nIs 4 Even?: true",
        "explanation": "Demonstrates checking numeric strings with isFinite and isNaN, validating integers with Number.isInteger, strict regex numeric testing, range bounds, and parity.",
    },
    "fill_blanks": {
        "question": "// The built-in JavaScript method to check if a value is an integer is Number._____().\n// The JavaScript function that checks if a numeric value is finite is _____().",
        "answers": ["isInteger", "isFinite"],
        "options": ["isInteger", "isFinite", "isNaN", "parseInt"],
    },
    "compiler": {
        "title": "Number Validation Sandbox",
        "question": "Complete the strict integer validation check.",
        "starter_code": "function checkInt(val) {\n    return Number._____(val);\n}\nconsole.log(checkInt(42));",
        "options": ["isInteger", "isNaN", "isFinite", "parse"],
    },
    "skill_exa_test": [
        {
            "question": "Which native method checks whether a value is an integer without type coercion?",
            "options": ["Number.isInteger()", "isNaN()", "isFinite()", "parseInt()"],
            "answer": "Number.isInteger()",
        },
        {
            "question": "What does `isNaN('123')` return in JavaScript?",
            "options": ["`false` (because '123' can be coerced into the number 123)", "`true`", "`null`", "`undefined`"],
            "answer": "`false` (because '123' can be coerced into the number 123)",
        },
        {
            "question": "In the regex `/^-?\\d+(\\.\\d+)?$/`, what does `^-?` allow?",
            "options": [
                "An optional negative sign at the beginning of the number string",
                "Mandatory decimal point",
                "Any alphabetic letter",
                "Positive numbers only"
            ],
            "answer": "An optional negative sign at the beginning of the number string",
        },
        {
            "question": "How do you check if a number `n` is even in JavaScript?",
            "options": ["typeof n === 'number' && n % 2 === 0", "n / 2 === 0", "n.isEven()", "n && 2"],
            "answer": "typeof n === 'number' && n % 2 === 0",
        },
        {
            "question": "What does `isFinite(Infinity)` return?",
            "options": ["`false`", "`true`", "`NaN`", "`null`"],
            "answer": "`false`",
        },
    ],
}

# Override Topic 98: Username Validation
JS_TOPICS[98] = {
    "id": 98,
    "title": "Username Validation",
    "category": "Regular Expression and Validation",
    "difficulty": "Intermediate",
    "duration": "20 min",
    "concept": "Username validation ensures user account identifiers meet length, starting character, and allowed character constraints using regex patterns.",
    "theory": "1. Typical Username Constraints:\n- Must start with an alphabetic letter.\n- May contain letters, numbers, underscores, and dots.\n- Must be within character length bounds (e.g. 3 to 16 characters).\n- Must not start or end with special symbols like dots or underscores.\n\n2. Regular Expression Approach:\n`/^[a-zA-Z][a-zA-Z0-9_]{2,15}$/`\n- `^`: Start of string.\n- `[a-zA-Z]`: First character must be a letter.\n- `[a-zA-Z0-9_]{2,15}`: Remaining 2 to 15 characters (making total length 3 to 16).\n- `$`: End of string.\n\n3. Combined Custom Logic Approach:\n- Check `username.length < 3` or `username.length > 16`.\n- Test allowed characters: `/^[a-zA-Z0-9._]+$/`.\n- Check boundary characters: `username.startsWith('.')` or `username.endsWith('_')`.",
    "syntax": "// Username Regex Pattern\nfunction validateUsername(username) {\n    const pattern = /^[a-zA-Z][a-zA-Z0-9_]{2,15}$/;\n    return pattern.test(username);\n}",
    "example": {
        "code": "// 1. Simple Regex Username Validation\nfunction validateSimpleUser(username) {\n    const pattern = /^[a-zA-Z][a-zA-Z0-9_]{2,15}$/;\n    return pattern.test(username);\n}\nconsole.log('alex_99:', validateSimpleUser('alex_99'));\nconsole.log('123alex:', validateSimpleUser('123alex')); // Invalid: Starts with number\nconsole.log('ab:', validateSimpleUser('ab'));          // Invalid: Too short\n\n// 2. Custom Combined Logic Username Validation\nfunction validateCustomUser(username) {\n    if (username.length < 3) return 'Username is too short.';\n    if (username.length > 16) return 'Username is too long.';\n    if (!/^[a-zA-Z0-9._]+$/.test(username)) return 'Invalid characters.';\n    if (username.startsWith('.') || username.startsWith('_')) return 'Cannot start with dot/underscore.';\n    return 'Valid username.';\n}\nconsole.log('Custom Valid User:', validateCustomUser('mohit_kumar'));\nconsole.log('Custom Leading Dot:', validateCustomUser('.mohit'));",
        "output": "alex_99: true\n123alex: false\nab: false\nCustom Valid User: Valid username.\nCustom Leading Dot: Cannot start with dot/underscore.",
        "explanation": "Demonstrates validating usernames using single regex assertions and custom multi-step rules for length and character placement.",
    },
    "fill_blanks": {
        "question": "// The regex pattern /^[a-zA-Z][a-zA-Z0-9_]{2,15}$/ enforces that the first character must be a _____.\n// The total allowed character length range in {2,15} for remaining chars is _____ to 16 characters.",
        "answers": ["letter", "3"],
        "options": ["letter", "3", "digit", "2"],
    },
    "compiler": {
        "title": "Username Validation Sandbox",
        "question": "Complete the username regex match check.",
        "starter_code": "function isValidUser(name) {\n    const pattern = /^[a-zA-Z][a-zA-Z0-9_]{2,15}$/;\n    return pattern.____(name);\n}\nconsole.log(isValidUser('geek_user'));",
        "options": ["test", "match", "check", "verify"],
    },
    "skill_exa_test": [
        {
            "question": "Why does the regex `/^[a-zA-Z][a-zA-Z0-9_]{2,15}$/` use `{2,15}` instead of `{3,16}`?",
            "options": [
                "Because the first character `[a-zA-Z]` is matched separately, leaving 2 to 15 remaining characters to achieve a total length of 3 to 16",
                "Because regex indexing starts at 2",
                "Because usernames cannot exceed 15 bytes",
                "Because underscores count as 2 characters"
            ],
            "answer": "Because the first character `[a-zA-Z]` is matched separately, leaving 2 to 15 remaining characters to achieve a total length of 3 to 16",
        },
        {
            "question": "Which username will FAIL validation under `/^[a-zA-Z][a-zA-Z0-9_]{2,15}$/`?",
            "options": ["`99_alex` (starts with a digit)", "`alex_99`", "`JohnDoe`", "`user_123`"],
            "answer": "`99_alex` (starts with a digit)",
        },
        {
            "question": "What is the purpose of checking `username.startsWith('.')` during custom username validation?",
            "options": [
                "To prevent usernames from beginning with leading dots",
                "To force usernames to start with capital letters",
                "To convert usernames to lowercase",
                "To encrypt usernames"
            ],
            "answer": "To prevent usernames from beginning with leading dots",
        },
        {
            "question": "What regex character class allows letters, numbers, and underscores?",
            "options": ["`[a-zA-Z0-9_]`", "`[0-9]`", "`[a-z]`", "`[^a-z]`"],
            "answer": "`[a-zA-Z0-9_]`",
        },
        {
            "question": "What is the result of `validateUsername('a')` when enforcing a minimum length of 3?",
            "options": ["`false`", "`true`", "`null`", "`undefined`"],
            "answer": "`false`",
        },
    ],
}

# Override Topic 99: Password Validation
JS_TOPICS[99] = {
    "id": 99,
    "title": "Password Validation",
    "category": "Regular Expression and Validation",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "Password validation enforces security requirements using regular expression lookaheads to guarantee combinations of uppercase, lowercase, numbers, special characters, and length constraints.",
    "theory": "1. Why Validate Passwords?\n- Protects user accounts against weak or guessable passwords.\n- Ensures compliance with security policies.\n\n2. Advanced Password Regex with Positive Lookaheads `(?=...)`:\n`/^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@.#$!%*?&])[A-Za-z\\d@.#$!%*?&]{8,15}$/`\n\n3. Breakdown of Lookahead Rules:\n- `(?=.*[a-z])`: Positive lookahead asserting at least one lowercase letter.\n- `(?=.*[A-Z])`: Asserting at least one uppercase letter.\n- `(?=.*\\d)`: Asserting at least one numeric digit.\n- `(?=.*[@.#$!%*?&])`: Asserting at least one special character.\n- `[A-Za-z\\d@.#$!%*?&]{8,15}$`: Length must be between 8 and 15 characters.\n\n4. Password Strength Scoring:\nInstead of a binary check, evaluate multiple rules into a numeric score:\n- Array of regexes: `[/[a-z]/, /[A-Z]/, /\\d/, /[@.#$!%*?&]/]`.\n- Calculate score: `checks.reduce((acc, rgx) => acc + rgx.test(pwd), 0)`.",
    "syntax": "// Password Validation Regex\nconst passRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@.#$!%*?&])[A-Za-z\\d@.#$!%*?&]{8,15}$/;\n\n// Check Pass\nconst isStrong = passRegex.test('Geeks@123');",
    "example": {
        "code": "// 1. Password Validation using Regex with Lookaheads\nconst passRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@.#$!%*?&])[A-Za-z\\d@.#$!%*?&]{8,15}$/;\nconst p1 = 'Geeks@123';\nconst p2 = 'GeeksforGeeks';\nconst p3 = 'geeks123';\n\nconsole.log(p1, ':', passRegex.test(p1));\nconsole.log(p2, ':', passRegex.test(p2));\nconsole.log(p3, ':', passRegex.test(p3));\n\n// 2. Password Strength Evaluator\nfunction checkPasswordStrength(pwd) {\n    if (pwd.length < 8) return 'Too short';\n    if (pwd.length > 15) return 'Too lengthy';\n    const checks = [/[a-z]/, /[A-Z]/, /\\d/, /[@.#$!%*?&]/];\n    const score = checks.reduce((acc, rgx) => acc + rgx.test(pwd), 0);\n    const levels = ['Weak', 'Fair', 'Good', 'Strong', 'Very Strong'];\n    return levels[score];\n}\nconsole.log('Strength of Geeks@123:', checkPasswordStrength('Geeks@123'));\nconsole.log('Strength of GeeksforGeeks:', checkPasswordStrength('GeeksforGeeks'));",
        "output": "Geeks@123 : true\nGeeksforGeeks : false\ngeeks123 : false\nStrength of Geeks@123: Very Strong\nStrength of GeeksforGeeks: Good",
        "explanation": "Demonstrates validating complex password rules using lookaheads and scoring password strength based on matched character classes.",
    },
    "fill_blanks": {
        "question": "// Positive lookaheads in regex are written using the syntax (?=_____).\n// In password regex, {8,15} enforces a length constraint between _____ and 15 characters.",
        "answers": [".*", "8"],
        "options": [".*", "8", "?=", "6"],
    },
    "compiler": {
        "title": "Password Validation Sandbox",
        "question": "Complete password strength check.",
        "starter_code": "let passRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@.#$!%*?&])[A-Za-z\\d@.#$!%*?&]{8,15}$/;\nlet pwd = 'Geeks@123';\nconsole.log(passRegex.____(pwd));",
        "options": ["test", "match", "check", "verify"],
    },
    "skill_exa_test": [
        {
            "question": "What does `(?=.*[A-Z])` assert in a password validation regular expression?",
            "options": [
                "Positive lookahead asserting that the string contains at least one uppercase letter",
                "Forces the password to start with an uppercase letter",
                "Replaces all uppercase letters with lowercase",
                "Counts the total number of uppercase letters"
            ],
            "answer": "Positive lookahead asserting that the string contains at least one uppercase letter",
        },
        {
            "question": "Why did `GeeksforGeeks` fail validation under `/^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@.#$!%*?&])[A-Za-z\\d@.#$!%*?&]{8,15}$/`?",
            "options": [
                "It lacks a numeric digit and a special character",
                "It is too short",
                "It contains invalid letters",
                "It starts with a capital letter"
            ],
            "answer": "It lacks a numeric digit and a special character",
        },
        {
            "question": "How can password strength be dynamically scored in JavaScript?",
            "options": [
                "By testing password string against an array of individual character class regexes and summing up matched passes",
                "By measuring network latency",
                "By converting password into Base64",
                "By calling `console.log()`"
            ],
            "answer": "By testing password string against an array of individual character class regexes and summing up matched passes",
        },
        {
            "question": "What does `(?=.*\\d)` enforce in password regex?",
            "options": [
                "Asserts at least one numeric digit is present",
                "Asserts password must contain only numbers",
                "Asserts password ends with digit 0",
                "Asserts password length is 10 digits"
            ],
            "answer": "Asserts at least one numeric digit is present",
        },
        {
            "question": "What does `{8,15}$` specify at the end of the password regex?",
            "options": [
                "The total password length must be between 8 and 15 characters inclusive",
                "The password must contain exactly 8 numbers",
                "The password expires in 15 days",
                "The password must have 8 special symbols"
            ],
            "answer": "The total password length must be between 8 and 15 characters inclusive",
        },
    ],
}

# Override Topic 100: URL Validation
JS_TOPICS[100] = {
    "id": 100,
    "title": "URL Validation",
    "category": "Regular Expression and Validation",
    "difficulty": "Advanced",
    "duration": "25 min",
    "concept": "Validating URLs in JavaScript ensures string input matches web address structures using Regular Expressions, the native URL object, or npm packages.",
    "theory": "1. Components of a Valid URL:\n- Protocol: `http://` or `https://` (optional or required).\n- Domain name or IP address: `www.example.com`.\n- Extension / TLD: `.com`, `.org`, `.co.in`.\n- Path, query string, or hash fragment: `/path?search=js#section`.\n\n2. Approach 1: Regular Expression Pattern:\n`/^(https?:\\/\\/)?([\\da-z.-]+)\\.([a-z.]{2,6})([\\/\\w .-]*)*\\/?$/`\n- `^(https?:\\/\\/)?`: Optional http:// or https:// protocol.\n- `([\\da-z.-]+)`: Matches domain name.\n- `\\.([a-z.]{2,6})`: Matches dot and extension (2 to 6 chars).\n- `([\\/\\w .-]*)*\\/?$`: Matches optional path, query, or parameters.\n\n3. Approach 2: Built-in `URL` Object Constructor:\n`try { new URL(urlStr); return true; } catch (e) { return false; }`\n- Built-in, robust, and handles complex URLs without writing custom regex.\n\n4. Approach 3: Specialized npm Packages:\n- `is-url` and `is-url-http` npm libraries for Node.js / bundling environments.",
    "syntax": "// Regex URL Validation\nfunction isValidURLRegex(url) {\n    const pattern = /^(https?:\\/\\/)?([\\da-z.-]+)\\.([a-z.]{2,6})([\\/\\w .-]*)*\\/?$/;\n    return pattern.test(url);\n}\n\n// URL Constructor Validation\nfunction isValidURLObj(url) {\n    try {\n        new URL(url);\n        return true;\n    } catch (e) {\n        return false;\n    }\n}",
    "example": {
        "code": "// 1. Regex URL Validation\nfunction isValidURLRegex(url) {\n    const pattern = /^(https?:\\/\\/)?([\\da-z.-]+)\\.([a-z.]{2,6})([\\/\\w .-]*)*\\/?$/;\n    return pattern.test(url);\n}\nconsole.log('Regex https://www.geeksforgeeks.org:', isValidURLRegex('https://www.geeksforgeeks.org'));\nconsole.log('Regex invalid-url:', isValidURLRegex('invalid-url'));\n\n// 2. Built-in URL Object Validation\nfunction isValidURLObject(url) {\n    try {\n        new URL(url);\n        return true;\n    } catch (e) {\n        return false;\n    }\n}\nconsole.log('URL Object https://example.com:', isValidURLObject('https://example.com'));\nconsole.log('URL Object invalid-url:', isValidURLObject('invalid-url'));",
        "output": "Regex https://www.geeksforgeeks.org: true\nRegex invalid-url: false\nURL Object https://example.com: true\nURL Object invalid-url: false",
        "explanation": "Demonstrates URL validation using custom regular expressions and JavaScript's built-in URL object constructor try...catch block.",
    },
    "fill_blanks": {
        "question": "// The built-in JavaScript class used to parse and validate URLs without regex is _____.\n// In URL regex ^(https?:\\/\\/)?, the ? makes the protocol prefix _____.",
        "answers": ["URL", "optional"],
        "options": ["URL", "optional", "URI", "mandatory"],
    },
    "compiler": {
        "title": "URL Validation Sandbox",
        "question": "Complete the URL Object validation function.",
        "starter_code": "function checkURL(str) {\n    try {\n        new _____(str);\n        return true;\n    } catch (e) {\n        return false;\n    }\n}\nconsole.log(checkURL('https://skillexa.com'));",
        "options": ["URL", "URI", "Http", "Link"],
    },
    "skill_exa_test": [
        {
            "question": "How does `new URL(url)` validate a URL string in JavaScript?",
            "options": [
                "It attempts to parse the URL string; if invalid, it throws an error that can be caught in a `try...catch` block returning `false`",
                "It makes an HTTP web network request to test if server is online",
                "It converts the URL into an HTML link tag",
                "It encrypts the domain name"
            ],
            "answer": "It attempts to parse the URL string; if invalid, it throws an error that can be caught in a `try...catch` block returning `false`",
        },
        {
            "question": "In the URL regex `/^(https?:\\/\\/)?.../`, what does `(https?:\\/\\/)?` match?",
            "options": [
                "An optional `http://` or `https://` protocol prefix",
                "Mandatory `ftp://` protocol",
                "Domain name extension",
                "Port number 8080"
            ],
            "answer": "An optional `http://` or `https://` protocol prefix",
        },
        {
            "question": "Which npm packages are popular for URL validation in Node.js applications?",
            "options": ["`is-url` and `is-url-http`", "`express` and `koa`", "`react` and `vue`", "`jest` and `mocha`"],
            "answer": "`is-url` and `is-url-http`",
        },
        {
            "question": "What happens when `new URL('invalid-string')` is called without `try...catch`?",
            "options": ["It throws a `TypeError` exception", "It returns `null`", "It returns `false`", "It reloads the page"],
            "answer": "It throws a `TypeError` exception",
        },
        {
            "question": "What three main components form a standard web URL?",
            "options": [
                "Protocol, domain name (or IP), and path/query parameters",
                "Variables, functions, and objects",
                "HTML, CSS, and JS",
                "Username, password, and port only"
            ],
            "answer": "Protocol, domain name (or IP), and path/query parameters",
        },
    ],
}

# Override Topic 101: Errors and Exceptions
JS_TOPICS[101] = {
    "id": 101,
    "title": "Errors and Exceptions",
    "category": "Exception and Error Handling",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "JavaScript Error and Exception handling allows applications to detect runtime failures, intercept exceptions, and prevent unexpected application crashes.",
    "theory": "1. What is an Error in JavaScript?\nAn error is a problem or anomaly that disrupts standard application execution. If unhandled, runtime errors halt thread execution.\n\n2. Standard JavaScript Error Types:\n- **SyntaxError**: Code violates JS language syntax rules (missing parentheses, unclosed strings). Caught at parse time.\n- **ReferenceError**: Attempting to access an undeclared variable (e.g., `console.log(x)` when `x` is undefined).\n- **TypeError**: Performing an invalid operation on an incompatible data type (e.g. `num.toUpperCase()` or calling non-function objects).\n- **RangeError**: Numeric value is outside its allowed numeric boundaries or array length constraints (e.g., `new Array(-1)`).\n- **URIError**: Invalid URI decoding sequences passed into `decodeURIComponent()`.\n\n3. The Built-in `Error` Object:\nRepresents an error instance containing `name` (error type title), `message` (human-readable explanation), and `stack` (execution stack trace).\n\n4. Benefits of Exception Handling:\n- Graceful degradation.\n- Structured error logging.\n- Crash prevention.",
    "syntax": "// Standard Error Types Demonstration\ntry {\n    // Code that might throw\n} catch (err) {\n    console.log(err.name, err.message);\n}",
    "example": {
        "code": "// 1. Handling ReferenceError, TypeError, and RangeError\nfunction testBuiltInErrors(type) {\n    try {\n        if (type === 'reference') {\n            console.log(nonExistentVar); // ReferenceError\n        } else if (type === 'type') {\n            let count = 100;\n            count.toUpperCase(); // TypeError\n        } else if (type === 'range') {\n            let arr = new Array(-5); // RangeError\n        }\n    } catch (err) {\n        console.log(`Caught ${err.name}: ${err.message}`);\n    }\n}\n\ntestBuiltInErrors('reference');\ntestBuiltInErrors('type');\ntestBuiltInErrors('range');",
        "output": "Caught ReferenceError: nonExistentVar is not defined\nCaught TypeError: count.toUpperCase is not a function\nCaught RangeError: Invalid array length",
        "explanation": "Demonstrates catching different built-in JavaScript error types (ReferenceError, TypeError, RangeError) and inspecting their name and message properties.",
    },
    "fill_blanks": {
        "question": "// Accessing an undeclared variable throws a _____.\n// Calling a string method like toUpperCase() on a number throws a _____.",
        "answers": ["ReferenceError", "TypeError"],
        "options": ["ReferenceError", "TypeError", "SyntaxError", "RangeError"],
    },
    "compiler": {
        "title": "Errors and Exceptions Sandbox",
        "question": "Complete error property inspection.",
        "starter_code": "try {\n    console.log(x);\n} catch (err) {\n    console.log(err.____);\n}",
        "options": ["name", "type", "code", "file"],
    },
    "skill_exa_test": [
        {
            "question": "Which error type is thrown when accessing a variable that has not been declared?",
            "options": ["ReferenceError", "TypeError", "SyntaxError", "RangeError"],
            "answer": "ReferenceError",
        },
        {
            "question": "Which error occurs when passing an invalid negative length like `new Array(-1)`?",
            "options": ["RangeError", "TypeError", "ReferenceError", "URIError"],
            "answer": "RangeError",
        },
        {
            "question": "What is the result of attempting to invoke a non-function value (e.g. `(5)()` or `num.toUpperCase()`)?",
            "options": ["Throws a `TypeError` exception", "Returns `undefined`", "Returns `false`", "Relaunches the browser"],
            "answer": "Throws a `TypeError` exception",
        },
        {
            "question": "When are `SyntaxError` exceptions typically evaluated in JavaScript?",
            "options": [
                "During script parsing before code execution begins",
                "Only when network requests complete",
                "After the `finally` block finishes",
                "Only in Node.js"
            ],
            "answer": "During script parsing before code execution begins",
        },
        {
            "question": "Which standard property of an `Error` object contains the human-readable error description?",
            "options": ["`message`", "`name`", "`stack`", "`cause`"],
            "answer": "`message`",
        },
    ],
}

# Override Topic 102: try-catch, throw Statement & finally Block
JS_TOPICS[102] = {
    "id": 102,
    "title": "try-catch, throw Statement & finally Block",
    "category": "Exception and Error Handling",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "The try-catch-finally statement and throw operator provide structured error handling to intercept exceptions, throw custom messages, and execute cleanup tasks.",
    "theory": "1. The `try` Block:\nEncloses code that might generate a runtime exception.\n\n2. The `catch (error)` Block:\nExecutes ONLY if an exception is thrown in the `try` block. Receives the thrown exception object (`error`).\n\n3. The `throw` Statement:\nAllows manual creation of custom errors or re-throwing exceptions (`throw new Error('Message')`).\n\n4. The `finally` Block:\nExecutes unconditionally after `try` and `catch` finish, regardless of success or failure. Essential for resource cleanup (e.g. closing streams, resetting loading spinners).\n\n5. Handling Async Errors (`async/await`):\nAsynchronous functions wrap `await` calls inside `try...catch` blocks to catch rejected Promises.",
    "syntax": "try {\n    // Code that might throw\n    throw new Error('Custom failure');\n} catch (err) {\n    // Error handling\n} finally {\n    // Unconditional cleanup code\n}",
    "example": {
        "code": "// 1. Synchronous try-catch-finally with throw\nfunction processOrder(amount) {\n    try {\n        console.log('Processing order of amount:', amount);\n        if (amount <= 0) {\n            throw new Error('Invalid order amount');\n        }\n        return 'Order Success';\n    } catch (err) {\n        console.log('Caught Error:', err.message);\n        return 'Order Failed';\n    } finally {\n        console.log('Cleanup: Closing database connection.');\n    }\n}\n\nconsole.log('Test 1:', processOrder(100));\nconsole.log('Test 2:', processOrder(-10));",
        "output": "Processing order of amount: 100\nCleanup: Closing database connection.\nTest 1: Order Success\nProcessing order of amount: -10\nCaught Error: Invalid order amount\nCleanup: Closing database connection.\nTest 2: Order Failed",
        "explanation": "Demonstrates handling exceptions with try-catch, raising custom errors with throw, and ensuring cleanup runs in the finally block.",
    },
    "fill_blanks": {
        "question": "// The block that always runs regardless of whether an error occurred or not is the _____ block.\n// To manually raise an error in JavaScript, use the _____ keyword.",
        "answers": ["finally", "throw"],
        "options": ["finally", "throw", "catch", "try"],
    },
    "compiler": {
        "title": "try-catch-finally Sandbox",
        "question": "Complete the cleanup block execution.",
        "starter_code": "try {\n    throw new Error('Test');\n} catch(e) {\n    console.log(e.message);\n} _____ {\n    console.log('Always runs');\n}",
        "options": ["finally", "catch", "then", "end"],
    },
    "skill_exa_test": [
        {
            "question": "When does the `finally` block execute in a `try...catch...finally` construct?",
            "options": [
                "Unconditionally after `try` and `catch` finish, regardless of whether an error was thrown or caught",
                "Only if an error was caught in the `catch` block",
                "Only if NO error occurred in the `try` block",
                "Only when `process.exit()` is called"
            ],
            "answer": "Unconditionally after `try` and `catch` finish, regardless of whether an error was thrown or caught",
        },
        {
            "question": "What happens if a `throw` statement is executed inside a `try` block?",
            "options": [
                "Immediate execution of the current script block stops, and control transfers to the matching `catch` block",
                "The script ignores the error and continues to the next line",
                "The browser automatically reloads",
                "The program compiles into C++"
            ],
            "answer": "Immediate execution of the current script block stops, and control transfers to the matching `catch` block",
        },
        {
            "question": "What data types can be thrown using the `throw` statement?",
            "options": [
                "Any JavaScript value (Error instances, strings, numbers, objects, booleans)",
                "Only Error class instances",
                "Only strings",
                "Only numbers"
            ],
            "answer": "Any JavaScript value (Error instances, strings, numbers, objects, booleans)",
        },
        {
            "question": "How do you handle rejected Promises inside an `async` function?",
            "options": [
                "By wrapping `await` expressions in a `try...catch` block",
                "By calling `console.log()`",
                "By using `Number.isInteger()`",
                "Async functions cannot throw errors"
            ],
            "answer": "By wrapping `await` expressions in a `try...catch` block",
        },
        {
            "question": "What is a common real-world use case for the `finally` block?",
            "options": [
                "Releasing resources, closing database connections, or hiding UI loading spinners",
                "Validating email syntax",
                "Defining variable types",
                "Parsing JSON text"
            ],
            "answer": "Releasing resources, closing database connections, or hiding UI loading spinners",
        },
    ],
}

# Override Topic 103: Custom Errors
JS_TOPICS[103] = {
    "id": 103,
    "title": "Custom Errors",
    "category": "Exception and Error Handling",
    "difficulty": "Advanced",
    "duration": "25 min",
    "concept": "Custom Errors extend JavaScript's built-in Error class to create application-specific exception types with targeted properties and structured logging.",
    "theory": "1. Why Create Custom Errors?\nBuilt-in error classes (`TypeError`, `RangeError`) describe general runtime issues. Custom errors represent specific domain failures (e.g., `ValidationError`, `AuthError`, `DatabaseConnectionError`).\n\n2. ES6 Class Constructor extending `Error`:\n```js\nclass CustomError extends Error {\n    constructor(message) {\n        super(message);\n        this.name = 'CustomError';\n    }\n}\n```\n- `super(message)`: Invokes base `Error` constructor to initialize `message` and stack trace.\n\n3. Pre-ES6 Prototype Inheritance Approach:\nInheriting `Error.prototype` on a function constructor (`CustomError.prototype = Object.create(Error.prototype)`).\n\n4. Adding Custom Properties:\nAttach extra metadata such as HTTP status codes (`statusCode: 404`), error codes (`code: 'ERR_INVALID_AGE'`), or target field names.\n\n5. Checking Custom Error Instances:\nUse `err instanceof CustomError` inside `catch` blocks to handle specific error types.",
    "syntax": "// Extending Built-in Error Class\nclass ValidationError extends Error {\n    constructor(msg) {\n        super(msg);\n        this.name = 'ValidationError';\n    }\n}",
    "example": {
        "code": "// 1. Defining ES6 Custom Error Class\nclass ValidationError extends Error {\n    constructor(message, field) {\n        super(message);\n        this.name = 'ValidationError';\n        this.field = field;\n    }\n}\n\n// 2. Pre-ES6 Prototype Inheritance Custom Error\nfunction LegacyError(msg) {\n    this.message = msg;\n    this.name = 'LegacyError';\n}\nLegacyError.prototype = Object.create(Error.prototype);\n\n// 3. Testing Custom Error Handling\nfunction checkAge(age) {\n    if (age < 18) {\n        throw new ValidationError('Age must be 18 or above', 'age');\n    }\n    return 'Access granted';\n}\n\ntry {\n    checkAge(15);\n} catch (err) {\n    if (err instanceof ValidationError) {\n        console.log(`[${err.name}] Field '${err.field}': ${err.message}`);\n    } else {\n        console.log('Generic Error:', err.message);\n    }\n}",
        "output": "[ValidationError] Field 'age': Age must be 18 or above",
        "explanation": "Demonstrates creating a custom error class extending Error, attaching custom properties (field), and using instanceof for targeted error handling.",
    },
    "fill_blanks": {
        "question": "// To inherit from the built-in Error class in ES6, use the _____ keyword.\n// To check if a caught error is an instance of a custom error class, use the _____ operator.",
        "answers": ["extends", "instanceof"],
        "options": ["extends", "instanceof", "inherits", "typeof"],
    },
    "compiler": {
        "title": "Custom Errors Sandbox",
        "question": "Complete the custom error class definition.",
        "starter_code": "class AppError _____ Error {\n    constructor(msg) {\n        _____(msg);\n        this.name = 'AppError';\n    }\n}",
        "options": ["extends", "super", "implements", "base"],
    },
    "skill_exa_test": [
        {
            "question": "How do you create a custom error class extending the built-in `Error` class in ES6?",
            "options": [
                "`class CustomError extends Error { constructor(msg) { super(msg); this.name = 'CustomError'; } }`",
                "`function CustomError() { Error.call(this); }`",
                "`const CustomError = new Error();`",
                "`class CustomError implements Error {}`"
            ],
            "answer": "`class CustomError extends Error { constructor(msg) { super(msg); this.name = 'CustomError'; } }`",
        },
        {
            "question": "Why is calling `super(message)` mandatory inside a custom error class constructor?",
            "options": [
                "To invoke the parent `Error` class constructor and initialize the `message` property and stack trace",
                "To automatically log the error to the server console",
                "To convert the error message into uppercase",
                "To prevent `catch` blocks from running"
            ],
            "answer": "To invoke the parent `Error` class constructor and initialize the `message` property and stack trace",
        },
        {
            "question": "Which operator is used inside a `catch` block to check if an error is an instance of a specific custom error class?",
            "options": ["`instanceof`", "`typeof`", "`===`", "`in`"],
            "answer": "`instanceof`",
        },
        {
            "question": "What is a main advantage of custom errors over standard generic errors?",
            "options": [
                "They allow attaching domain-specific metadata (HTTP status codes, field names, error codes) for targeted handling",
                "They run 10x faster than standard errors",
                "They automatically fix syntax mistakes in code",
                "They prevent asynchronous Promise rejections"
            ],
            "answer": "They allow attaching domain-specific metadata (HTTP status codes, field names, error codes) for targeted handling",
        },
        {
            "question": "In pre-ES6 JavaScript, how were custom errors prototype-inherited?",
            "options": [
                "`CustomError.prototype = Object.create(Error.prototype);`",
                "`CustomError = Error.clone();`",
                "`Object.setPrototypeOf(CustomError, null);`",
                "`CustomError.prototype = Array.prototype;`"
            ],
            "answer": "`CustomError.prototype = Object.create(Error.prototype);`",
        },
    ],
}

# Override Topic 104: Debugging Basics & DevTools
JS_TOPICS[104] = {
    "id": 104,
    "title": "Debugging Basics & DevTools",
    "category": "Exception and Error Handling",
    "difficulty": "Beginner",
    "duration": "20 min",
    "concept": "Debugging is the systematic process of finding and fixing errors using browser Developer Tools, console logging, breakpoints, and the debugger statement.",
    "theory": "1. Three Main Bug Categories:\n- **Syntax Errors**: Invalid JS rules (caught during parse time).\n- **Runtime Errors**: Crashes occurring during execution (e.g. `TypeError`, `ReferenceError`).\n- **Logical Errors**: Code executes cleanly but produces incorrect business logic output.\n\n2. Browser Developer Tools (DevTools):\n- Access via `F12` or `Ctrl+Shift+I` (Cmd+Option+I on Mac).\n- **Console Tab**: Inspect values, run ad-hoc JS commands, view error trace logs.\n- **Sources Tab**: View source files, manage breakpoints, step through code line by line.\n\n3. Console Methods:\n- `console.log()`: General variable state inspection.\n- `console.warn()` / `console.error()`: Highlight warnings and errors.\n- `console.table()`: Render arrays/objects as structured tables.\n\n4. Breakpoints & the `debugger` Keyword:\n- **Breakpoints**: Pauses execution on specific source lines to inspect variable scope and call stacks.\n- **`debugger` Statement**: Built-in JS instruction that programmatically pauses execution if DevTools is open.",
    "syntax": "// Logging Output\nconsole.log('Value of x:', x);\n\n// Programmatic Breakpoint\nfunction test() {\n    let n = 42;\n    debugger; // Pauses execution if DevTools is open\n    return n;\n}",
    "example": {
        "code": "// 1. Identifying Logical Error using console.log\nfunction addNumbers(a, b) {\n    console.log(`Debug Inputs: a = ${a}, b = ${b}`);\n    // Bug: Subtracting instead of adding!\n    let result = a - b;\n    console.log(`Debug Result: ${result}`);\n    return result;\n}\n\n// 2. Programmatic Debugger Statement\nfunction runDebuggerTest() {\n    let val = 'SkillExa';\n    // debugger;\n    return val;\n}\n\nconst sum = addNumbers(5, 10);\nconsole.log('Final Calculated Result:', sum);\nconsole.log('Debugger Test Output:', runDebuggerTest());",
        "output": "Debug Inputs: a = 5, b = 10\nDebug Result: -5\nFinal Calculated Result: -5\nDebugger Test Output: SkillExa",
        "explanation": "Demonstrates tracking logical errors using console logging and using the debugger statement to pause execution in DevTools.",
    },
    "fill_blanks": {
        "question": "// The built-in JavaScript keyword that pauses execution and opens DevTools is _____.\n// To view arrays or objects as a formatted table in the console, use console._____().",
        "answers": ["debugger", "table"],
        "options": ["debugger", "table", "log", "break"],
    },
    "compiler": {
        "title": "Debugging Basics Sandbox",
        "question": "Complete the programmatic breakpoint instruction.",
        "starter_code": "function check() {\n    let score = 100;\n    _____;\n    return score;\n}",
        "options": ["debugger", "breakpoint", "pause", "stop"],
    },
    "skill_exa_test": [
        {
            "question": "What is the primary function of the `debugger;` statement in JavaScript?",
            "options": [
                "It pauses execution at that line and opens browser debugging tools if DevTools is active",
                "It fixes syntax errors automatically",
                "It logs the memory consumption to backend servers",
                "It converts JS code into HTML"
            ],
            "answer": "It pauses execution at that line and opens browser debugging tools if DevTools is active",
        },
        {
            "question": "What character shortcut opens Developer Tools in Chrome on Windows/Linux?",
            "options": ["F12 or Ctrl+Shift+I", "Ctrl+Alt+Delete", "Shift+Esc", "F5"],
            "answer": "F12 or Ctrl+Shift+I",
        },
        {
            "question": "What is a logical error in programming?",
            "options": [
                "Code executes without throwing runtime errors but produces incorrect outputs due to bad logic",
                "Code that fails to compile due to missing quotes",
                "Accessing an undeclared variable",
                "Network fetch connection failure"
            ],
            "answer": "Code executes without throwing runtime errors but produces incorrect outputs due to bad logic",
        },
        {
            "question": "Which `console` method renders arrays of objects as a visual tabular grid in DevTools?",
            "options": ["`console.table()`", "`console.grid()`", "`console.list()`", "`console.log()`"],
            "answer": "`console.table()`",
        },
        {
            "question": "What happens if a `debugger;` statement is executed while browser DevTools is CLOSED?",
            "options": [
                "It has no effect and execution continues normally",
                "It crashes the web browser tab",
                "It opens a popup window",
                "It throws a ReferenceError"
            ],
            "answer": "It has no effect and execution continues normally",
        },
    ],
}

# Override Topic 105: Advanced Debugging & Error Tracking
JS_TOPICS[105] = {
    "id": 105,
    "title": "Advanced Debugging & Error Tracking",
    "category": "Exception and Error Handling",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "Advanced debugging involves diagnosing undefined variable scopes, handling asynchronous Promise failures, catching JSON parsing bugs, and profiling memory leaks.",
    "theory": "1. Debugging Undefined Variables:\n- Undefined outputs usually stem from missing function arguments, unreturned function values, or out-of-scope variables.\n\n2. Debugging `JSON.parse()` Errors:\n- Parsing malformed JSON strings throws `SyntaxError`. Wrap parsing logic in `try...catch` to prevent app crashes.\n\n3. Debugging Asynchronous Code (Promises & `async/await`):\n- Attach `.catch()` handlers to Promise chains or wrap `await` calls in `try...catch`.\n- Monitor `window.addEventListener('unhandledrejection')` to log global async errors.\n\n4. Event Listener Debugging:\n- Ensure target element exists in DOM before invoking `addEventListener()`.\n\n5. Memory Leak Profiling:\n- Causes: Uncleaned `setInterval()` timer loops, detached DOM elements, excessive global array mutations.\n- Diagnosis: Use Chrome DevTools Memory tab Heap Snapshots to inspect memory accumulation.",
    "syntax": "// Safe JSON Parsing\ntry {\n    let data = JSON.parse(str);\n} catch (err) {\n    console.error('Parse Error:', err.message);\n}\n\n// Async Error Catching\nfetch(url).catch(err => console.error('Request Failed:', err));",
    "example": {
        "code": "// 1. Debugging JSON Parsing Errors\nfunction parseInput(jsonText) {\n    try {\n        return JSON.parse(jsonText);\n    } catch (err) {\n        console.log('Caught Bad JSON:', err.message);\n        return null;\n    }\n}\n\n// 2. Debugging Asynchronous Promise Rejections\nfunction loadData() {\n    return Promise.reject(new Error('API Server 500 Failure'))\n        .catch(err => {\n            console.log('Handled Async Rejection:', err.message);\n            return { fallback: true };\n        });\n}\n\n// 3. Detecting Potential Memory Leak Pattern\nfunction simulateTimerLeak() {\n    let cache = [];\n    const intervalId = setInterval(() => cache.push('data'), 100);\n    clearInterval(intervalId); // Cleanup timer to prevent leak!\n    console.log('Timer cleared safely.');\n}\n\nconsole.log('Parse Test:', parseInput('{invalid_json}'));\nloadData();\nsimulateTimerLeak();",
        "output": "Caught Bad JSON: Unexpected token i in JSON at position 1\nParse Test: null\nHandled Async Rejection: API Server 500 Failure\nTimer cleared safely.",
        "explanation": "Demonstrates safely debugging JSON parsing errors, handling async promise rejections with catch, and clearing timers to prevent memory leaks.",
    },
    "fill_blanks": {
        "question": "// Unhandled Promise rejections can be caught globally in browsers using the _____ event.\n// To prevent memory leaks from recurring timers, call _____(intervalId).",
        "answers": ["unhandledrejection", "clearInterval"],
        "options": ["unhandledrejection", "clearInterval", "clearTimeout", "onerror"],
    },
    "compiler": {
        "title": "Advanced Debugging Sandbox",
        "question": "Complete safe JSON parse handling.",
        "starter_code": "function safeParse(str) {\n    try {\n        return JSON.parse(str);\n    } _____ (err) {\n        return null;\n    }\n}",
        "options": ["catch", "finally", "except", "error"],
    },
    "skill_exa_test": [
        {
            "question": "Which browser window event catches unhandled Promise rejections globally?",
            "options": ["`unhandledrejection`", "`error`", "`reject`", "`asyncerror`"],
            "answer": "`unhandledrejection`",
        },
        {
            "question": "What common code pattern frequently causes memory leaks in JavaScript single-page applications?",
            "options": [
                "Running `setInterval()` timers without calling `clearInterval()` when components unmount",
                "Using `console.log()`",
                "Wrapping code in `try...catch`",
                "Calling `JSON.stringify()`"
            ],
            "answer": "Running `setInterval()` timers without calling `clearInterval()` when components unmount",
        },
        {
            "question": "What is the result of attempting `JSON.parse('{bad}')` without `try...catch` error handling?",
            "options": [
                "It throws an unhandled `SyntaxError` exception that halts application execution",
                "It returns `null` quietly",
                "It converts `{bad}` into `{bad: true}`",
                "It returns an empty array"
            ],
            "answer": "It throws an unhandled `SyntaxError` exception that halts application execution",
        },
        {
            "question": "Why might an event listener fail to trigger when a button is clicked?",
            "options": [
                "The target element ID did not exist in the DOM when `document.getElementById()` was called",
                "The browser developer tools are open",
                "The function used `console.log()`",
                "The button was styled with CSS"
            ],
            "answer": "The target element ID did not exist in the DOM when `document.getElementById()` was called",
        },
        {
            "answer": "Memory tab",
        },
    ],
}

# Override Topic 106: Unit Testing with Jest
JS_TOPICS[106] = {
    "id": 106,
    "title": "Unit Testing with Jest",
    "category": "Testing and Performance Optimization",
    "difficulty": "Intermediate",
    "duration": "30 min",
    "concept": "Jest is a zero-configuration JavaScript testing framework developed by Facebook for unit testing functions, async code, objects, callbacks, and mock implementations.",
    "theory": "1. What is Jest?\nA modern JavaScript testing framework known for fast performance, zero-config setup, snapshot testing, built-in mocking, and code coverage reports.\n\n2. Setup & Installation:\n- Install: `npm install --save-dev jest`.\n- Configure script in `package.json`: `\"scripts\": { \"test\": \"jest\" }`.\n- Execute tests: `npm test`.\n\n3. Writing Basic Assertions:\n- Test suite syntax: `test('description', () => { ... });`.\n- `.toBe(value)`: Checks exact equality (`===`) for primitive values.\n- `.toEqual(value)`: Checks deep equality for objects and arrays.\n\n4. Testing Asynchronous Code:\n- Promises / Async-Await: `test('async', async () => { const data = await fetchD(); expect(data).toBe('Data loaded'); });`.\n- Callbacks: Pass `done` callback to `test('name', (done) => { ... done(); })`.\n\n5. Mocking with Jest:\n- `jest.mock('./api')`: Mocks module imports to isolate tests.\n- `mockFn.mockReturnValue('Mocked data')`: Overrides returned values of mock functions.",
    "syntax": "// Standard Jest Unit Test Syntax\nconst sum = require('./sum');\n\ntest('adds 1 + 2 to equal 3', () => {\n    expect(sum(1, 2)).toBe(3);\n});",
    "example": {
        "code": "// 1. Simulating Jest Assertion Engine\nfunction expect(actual) {\n    return {\n        toBe: (expected) => {\n            const pass = actual === expected;\n            console.log(`toBe('${expected}'):`, pass ? 'PASSED' : 'FAILED');\n            return pass;\n        },\n        toEqual: (expected) => {\n            const pass = JSON.stringify(actual) === JSON.stringify(expected);\n            console.log(`toEqual(${JSON.stringify(expected)}):`, pass ? 'PASSED' : 'FAILED');\n            return pass;\n        }\n    };\n}\n\n// 2. Testing Normal Functions & Objects\nconst add = (a, b) => a + b;\nconst getObj = () => ({ name: 'Pranjal' });\n\nexpect(add(2, 3)).toBe(5);\nexpect(getObj()).toEqual({ name: 'Pranjal' });\n\n// 3. Testing Callback Functions\nfunction fetchData(cb) {\n    return cb('Hi');\n}\nfetchData((data) => {\n    expect(data).toBe('Hi');\n});",
        "output": "toBe('5'): PASSED\ntoEqual({\"name\":\"Pranjal\"}): PASSED\ntoBe('Hi'): PASSED",
        "explanation": "Demonstrates Jest-like assertion testing for primitive numbers with toBe(), objects with toEqual(), and callback execution parameters.",
    },
    "fill_blanks": {
        "question": "// To test primitive values for strict equality in Jest, use expect(val)._____().\n// To test objects or arrays for deep value equality in Jest, use expect(val)._____().",
        "answers": ["toBe", "toEqual"],
        "options": ["toBe", "toEqual", "toStrict", "toBeSame"],
    },
    "compiler": {
        "title": "Unit Testing with Jest Sandbox",
        "question": "Complete the Jest object assertion test.",
        "starter_code": "function getUser() { return { role: 'Admin' }; }\ntest('User role test', () => {\n    expect(getUser()).____({ role: 'Admin' });\n});",
        "options": ["toEqual", "toBe", "toContain", "toExist"],
    },
    "skill_exa_test": [
        {
            "question": "What is the key difference between `.toBe()` and `.toEqual()` in Jest assertions?",
            "options": [
                "`.toBe()` tests strict primitive equality (`===`), while `.toEqual()` performs deep recursive comparison on object and array properties",
                "`.toBe()` only tests strings while `.toEqual()` tests numbers",
                "`.toEqual()` is used for async Promises only",
                "There is no difference between them"
            ],
            "answer": "`.toBe()` tests strict primitive equality (`===`), while `.toEqual()` performs deep recursive comparison on object and array properties",
        },
        {
            "question": "How do you test asynchronous callback functions in Jest to ensure assertions complete before the test finishes?",
            "options": [
                "By accepting a `done` argument in the test function and invoking `done()` after assertions complete",
                "By calling `process.exit()`",
                "By calling `setTimeout()` with 10 seconds",
                "Jest cannot test callback functions"
            ],
            "answer": "By accepting a `done` argument in the test function and invoking `done()` after assertions complete",
        },
        {
            "question": "Which Jest function is used to mock external module dependencies during test execution?",
            "options": ["`jest.mock()`", "`jest.stub()`", "`jest.spy()`", "`jest.fake()`"],
            "answer": "`jest.mock()`",
        },
        {
            "question": "How do you generate a code coverage report when executing Jest tests?",
            "options": [
                "By passing the `--coverage` flag (e.g. `npx jest --coverage`)",
                "By running `npm build`",
                "By adding `console.log()` inside test files",
                "Code coverage requires paid licenses"
            ],
            "answer": "By passing the `--coverage` flag (e.g. `npx jest --coverage`)",
        },
        {
            "question": "What npm script command is typically used to run Jest tests?",
            "options": ["`npm test` or `npm run test`", "`npm start`", "`npm build`", "`npm compile`"],
            "answer": "`npm test` or `npm run test`",
        },
    ],
}

# Override Topic 107: Memory Management
JS_TOPICS[107] = {
    "id": 107,
    "title": "Memory Management",
    "category": "Testing and Performance Optimization",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "JavaScript memory management operates automatically across Allocation, Usage, and Deallocation phases, managing Stack and Heap memory.",
    "theory": "1. Memory Life Cycle:\n- **Allocation**: The JS engine allocates memory when variables, objects, or functions are created.\n- **Usage**: The program reads or writes allocated memory values.\n- **Deallocation**: Unused memory is automatically freed by the engine.\n\n2. Types of Memory in JavaScript:\na. **Stack Memory (Primitive Types)**:\n   - Stores primitive data types (`number`, `string`, `boolean`, `null`, `undefined`, `symbol`).\n   - LIFO (Last-In, First-Out) structure, fast access, automatic cleanup on function scope exit.\nb. **Heap Memory (Reference Types)**:\n   - Stores complex reference types (`objects`, `arrays`, `functions`).\n   - Unstructured large memory pool, dynamic allocation, variables on Stack store pointers/references to Heap memory locations.\n\n3. Optimization Techniques:\n- Minimize DOM manipulation (batch updates, DocumentFragment).\n- Prevent memory leaks (remove event listeners, clear timers, break circular references).\n- Cache array length in loops (`for (let i = 0, len = arr.length; i < len; i++)`).\n\n4. Profiling Tools:\nChrome DevTools Memory tab Heap Snapshots and Node.js `process.memoryUsage()`.",
    "syntax": "// Primitive (Stack) Copy by Value\nlet a = 10;\nlet b = a;\n\n// Reference (Heap) Copy by Pointer\nlet obj1 = { name: 'Ajay' };\nlet obj2 = obj1;",
    "example": {
        "code": "// 1. Stack Memory (Primitives - Copy by Value)\nlet n1 = 10;\nlet n2 = n1;\nn2 = 20;\nconsole.log('n1 (Stack value unaffected):', n1);\nconsole.log('n2 (Stack independent copy):', n2);\n\n// 2. Heap Memory (Reference Types - Copy by Pointer)\nlet obj1 = { name: 'Ajay' };\nlet obj2 = obj1;\nobj2.name = 'Vijay';\nconsole.log('obj1 name (Heap mutated via reference):', obj1.name);\n\n// 3. Node.js Memory Usage Inspection\nconst mem = process.memoryUsage();\nconsole.log('Heap Total Allocated:', mem.heapTotal > 0);",
        "output": "n1 (Stack value unaffected): 10\nn2 (Stack independent copy): 20\nobj1 name (Heap mutated via reference): Vijay\nHeap Total Allocated: true",
        "explanation": "Demonstrates primitive copy-by-value behavior stored in Stack memory vs reference mutation behavior stored in Heap memory.",
    },
    "fill_blanks": {
        "question": "// Primitive data types like numbers and booleans are stored directly in _____ memory.\n// Complex reference types like objects and arrays are allocated in _____ memory.",
        "answers": ["Stack", "Heap"],
        "options": ["Stack", "Heap", "Cache", "Disk"],
    },
    "compiler": {
        "title": "Memory Management Sandbox",
        "question": "Inspect primitive value copy in Stack memory.",
        "starter_code": "let x = 5;\nlet y = x;\ny = 15;\nconsole.log(x);",
        "options": ["5", "15", "undefined", "NaN"],
    },
    "skill_exa_test": [
        {
            "question": "Which memory region in JavaScript stores primitive data types and operates on a LIFO (Last-In, First-Out) structure?",
            "options": ["Stack Memory", "Heap Memory", "Virtual Memory", "ROM"],
            "answer": "Stack Memory",
        },
        {
            "question": "Where are complex reference data types like Objects, Arrays, and Functions stored in JavaScript?",
            "options": ["Heap Memory", "Stack Memory", "CPU Cache", "Cookie Storage"],
            "answer": "Heap Memory",
        },
        {
            "question": "What happens when you copy an object variable (`let obj2 = obj1`) in JavaScript?",
            "options": [
                "Both variables store pointers referencing the exact same object location in Heap memory",
                "A complete deep copy of the object is created automatically in Stack memory",
                "The original object is deleted",
                "It throws a TypeError"
            ],
            "answer": "Both variables store pointers referencing the exact same object location in Heap memory",
        },
        {
            "question": "What are the three main phases of the JavaScript memory lifecycle?",
            "options": [
                "Allocation -> Usage -> Deallocation (Release)",
                "Compilation -> Execution -> Termination",
                "Mark -> Sweep -> Compact",
                "Fetch -> Decode -> Execute"
            ],
            "answer": "Allocation -> Usage -> Deallocation (Release)",
        },
        {
            "question": "Which Node.js method provides memory consumption details for heapTotal and heapUsed?",
            "options": ["`process.memoryUsage()`", "`console.memory()`", "`v8.getHeap()`", "`window.memory`"],
            "answer": "`process.memoryUsage()`",
        },
    ],
}

# Override Topic 108: Garbage Collection
JS_TOPICS[108] = {
    "id": 108,
    "title": "Garbage Collection",
    "category": "Testing and Performance Optimization",
    "difficulty": "Advanced",
    "duration": "25 min",
    "concept": "Garbage Collection (GC) in JavaScript is an automatic memory management process that frees memory occupied by unreachable objects.",
    "theory": "1. Concept of Unreachable Objects:\nObjects in JavaScript remain in memory as long as they are reachable from the root (global objects, active function stacks). When an object has zero references pointing to it, it becomes unreachable and is marked for Garbage Collection.\n\n2. Primary GC Algorithms:\na. **Reference Counting**:\n   - Counts active references to each object. Reclaims memory when count drops to zero.\n   - *Limitation*: Fails to reclaim circular references (where object A references B and B references A).\nb. **Mark-and-Sweep Algorithm** (Modern Standard):\n   - **Mark Phase**: Traverses all objects reachable from the root and marks them as \"in use\".\n   - **Sweep Phase**: Scans memory heap and reclaims memory of all unmarked/unreachable objects.\n\n3. Common GC Trigger Scenarios:\n- Nullifying variables (`user = null`).\n- Removing array elements via `.splice()`.\n- Out-of-scope function local variables.\n\n4. GC Best Practices:\n- Nullify large object references when finished.\n- Clear intervals (`clearInterval`) and timeouts (`clearTimeout`).\n- Remove unused DOM event listeners.\n- Use `WeakMap` / `WeakSet` for transient object keys.",
    "syntax": "// Making an Object Unreachable for Garbage Collection\nlet user = { name: 'Pranjal' };\nuser = null; // Object is now unreachable and eligible for GC",
    "example": {
        "code": "// 1. Simulating Mark-and-Sweep Garbage Collection\nclass GCSimulator {\n    constructor() {\n        this.heap = [];\n    }\n    createObj(name) {\n        const obj = { name, refCount: 1, marked: false };\n        this.heap.push(obj);\n        return obj;\n    }\n    mark() {\n        this.heap.forEach(o => { if (o.refCount > 0) o.marked = true; });\n    }\n    sweep() {\n        this.heap = this.heap.filter(o => o.marked);\n    }\n    runGC() {\n        this.mark();\n        this.sweep();\n    }\n}\n\nconst gc = new GCSimulator();\nconst activeObj = gc.createObj('Object 1');\nconst deadObj = gc.createObj('Object 2');\n\ndeadObj.refCount = 0; // Reference removed!\ngc.runGC();\n\nconsole.log('Heap Size after GC:', gc.heap.length);\nconsole.log('Surviving Object:', gc.heap[0].name);",
        "output": "Heap Size after GC: 1\nSurviving Object: Object 1",
        "explanation": "Demonstrates how setting object reference count to 0 allows the mark-and-sweep algorithm to identify unreachable objects and sweep them from memory.",
    },
    "fill_blanks": {
        "question": "// In modern JavaScript engines, the primary garbage collection algorithm used is _____.\n// An object becomes eligible for garbage collection when it is no longer _____ from the root.",
        "answers": ["Mark-and-Sweep", "reachable"],
        "options": ["Mark-and-Sweep", "reachable", "Reference Counting", "visible"],
    },
    "compiler": {
        "title": "Garbage Collection Sandbox",
        "question": "Make object unreachable for Garbage Collection.",
        "starter_code": "let data = { title: 'Test' };\ndata = _____;\nconsole.log(data);",
        "options": ["null", "undefined", "false", "0"],
    },
    "skill_exa_test": [
        {
            "question": "How does the Mark-and-Sweep garbage collection algorithm identify objects to remove from memory?",
            "options": [
                "It traverses reachable objects starting from root objects, marks them as 'in use', and sweeps away all unmarked (unreachable) objects",
                "It deletes objects created more than 10 minutes ago",
                "It counts lines of code",
                "It removes all global variables periodically"
            ],
            "answer": "It traverses reachable objects starting from root objects, marks them as 'in use', and sweeps away all unmarked (unreachable) objects",
        },
        {
            "question": "What major limitation affects the basic Reference Counting garbage collection algorithm?",
            "options": [
                "It fails to clean up circular references where two objects reference each other but are otherwise isolated",
                "It cannot delete string variables",
                "It runs only in Node.js",
                "It causes CPU overheating"
            ],
            "answer": "It fails to clean up circular references where two objects reference each other but are otherwise isolated",
        },
        {
            "question": "What happens when a variable pointing to an object is reassigned to `null` (`user = null`)?",
            "options": [
                "The reference to the object is removed, making the object eligible for garbage collection if no other references exist",
                "The browser reloads the webpage",
                "The variable throws a ReferenceError",
                "The object is saved to disk"
            ],
            "answer": "The reference to the object is removed, making the object eligible for garbage collection if no other references exist",
        },
        {
            "question": "Why should `WeakMap` or `WeakSet` be used for temporary object key storage?",
            "options": [
                "Because keys in WeakMap are held weakly, allowing garbage collection of keys when no other references exist",
                "Because WeakMap converts keys into integers automatically",
                "Because WeakMap disables garbage collection completely",
                "Because WeakMap is synchronous"
            ],
            "answer": "Because keys in WeakMap are held weakly, allowing garbage collection of keys when no other references exist",
        },
        {
            "question": "Do developers need to manually deallocate memory in standard JavaScript?",
            "options": [
                "No, JavaScript engines handle garbage collection automatically in the background",
                "Yes, developers must call `free()` on every object",
                "Yes, using C-style `malloc()`",
                "No, memory is infinite in JavaScript"
            ],
            "answer": "No, JavaScript engines handle garbage collection automatically in the background",
        },
    ],
}

# Override Topic 109: Lazy Loading
JS_TOPICS[109] = {
    "id": 109,
    "title": "Lazy Loading",
    "category": "Testing and Performance Optimization",
    "difficulty": "Intermediate",
    "duration": "25 min",
    "concept": "Lazy Loading is a performance optimization technique that defers resource loading (images, videos, scripts, or data) until they enter the viewport.",
    "theory": "1. Benefits of Lazy Loading:\n- Faster initial page load time.\n- Reduced initial bandwidth and data consumption.\n- Improved browser performance and SEO scores.\n\n2. HTML5 Native Lazy Loading:\n`loading=\"lazy\"` attribute on `<img>` and `<iframe>` elements allows browsers to manage lazy loading automatically without JS.\n\n3. IntersectionObserver API:\nModern browser API that detects when an element enters or intersects the viewport:\n```js\nconst observer = new IntersectionObserver((entries, obs) => {\n    entries.forEach(entry => {\n        if (entry.isIntersecting) {\n            const img = entry.target;\n            img.src = img.dataset.src; // Replace placeholder with real URL\n            obs.unobserve(img); // Stop tracking\n        }\n    });\n});\n```\n\n4. Script Defer vs Async:\n- `async`: Loads script in parallel and executes immediately upon download (out of order, non-blocking).\n- `defer`: Loads script in parallel and executes after HTML parsing completes (maintains execution order).",
    "syntax": "// HTML5 Native Attribute\n<img src=\"image.jpg\" loading=\"lazy\" alt=\"Lazy Image\">\n\n// IntersectionObserver API\nconst observer = new IntersectionObserver(callback, options);",
    "example": {
        "code": "// 1. Simulating IntersectionObserver Lazy Loading Logic\nclass LazyLoadSimulator {\n    constructor(callback) {\n        this.callback = callback;\n    }\n    simulateViewportEntry(entries) {\n        this.callback(entries, this);\n    }\n    unobserve(element) {\n        console.log(`Stopped tracking: ${element.alt}`);\n    }\n}\n\nconst imgElement = {\n    src: '',\n    dataset: { src: 'https://media.example.com/actual-image.webp' },\n    alt: 'Banner Image'\n};\n\nconst lazyObserver = new LazyLoadSimulator((entries, observer) => {\n    entries.forEach(entry => {\n        if (entry.isIntersecting) {\n            const img = entry.target;\n            img.src = img.dataset.src;\n            console.log('Loaded Image URL:', img.src);\n            observer.unobserve(img);\n        }\n    });\n});\n\n// Simulate user scrolling image into viewport\nlazyObserver.simulateViewportEntry([{ target: imgElement, isIntersecting: true }]);",
        "output": "Loaded Image URL: https://media.example.com/actual-image.webp\nStopped tracking: Banner Image",
        "explanation": "Demonstrates using IntersectionObserver callback to dynamically set img.src from dataset.src when elements enter the viewport.",
    },
    "fill_blanks": {
        "question": "// The modern JavaScript browser API used to detect when elements enter the viewport is _____.\n// The HTML attribute used for native browser lazy loading on <img> tags is loading=\"_____\".",
        "answers": ["IntersectionObserver", "lazy"],
        "options": ["IntersectionObserver", "lazy", "MutationObserver", "async"],
    },
    "compiler": {
        "title": "Lazy Loading Sandbox",
        "question": "Complete the IntersectionObserver unobserve call.",
        "starter_code": "const observer = new IntersectionObserver((entries, obs) => {\n    entries.forEach(entry => {\n        if (entry.isIntersecting) {\n            entry.target.src = entry.target.dataset.src;\n            obs._____(entry.target);\n        }\n    });\n});",
        "options": ["unobserve", "disconnect", "stop", "remove"],
    },
    "skill_exa_test": [
        {
            "question": "What is the primary objective of implementing Lazy Loading in web applications?",
            "options": [
                "Deferring the loading of non-critical resources until they are needed in the viewport to improve initial page load speed",
                "Encrypting images before sending them across HTTP",
                "Converting PNG images into SVG format",
                "Running tests in parallel"
            ],
            "answer": "Deferring the loading of non-critical resources until they are needed in the viewport to improve initial page load speed",
        },
        {
            "question": "Which browser API detects when an element intersects or enters the visible viewport area?",
            "options": ["IntersectionObserver API", "MutationObserver API", "ResizeObserver API", "Fetch API"],
            "answer": "IntersectionObserver API",
        },
        {
            "question": "What is the difference between `<script async>` and `<script defer>`?",
            "options": [
                "`async` executes immediately once downloaded, while `defer` waits until HTML parsing is completely finished before executing",
                "`defer` executes immediately while `async` waits for click events",
                "`async` only works in React apps",
                "`defer` prevents CSS from loading"
            ],
            "answer": "`async` executes immediately once downloaded, while `defer` waits until HTML parsing is completely finished before executing",
        },
        {
            "question": "Which HTML5 attribute enables native browser lazy loading without custom JavaScript code?",
            "options": ["`loading=\"lazy\"`", "`lazy=\"true\"`", "`defer=\"lazy\"`", "`async=\"true\"`"],
            "answer": "`loading=\"lazy\"`",
        },
        {
            "question": "Why call `observer.unobserve(target)` after an image has finished lazy loading?",
            "options": [
                "To stop viewport intersection tracking for that image and optimize performance",
                "To delete the image from the DOM",
                "To clear browser cookies",
                "To restart the animation"
            ],
            "answer": "To stop viewport intersection tracking for that image and optimize performance",
        },
    ],
}

# Override Topic 110: Debouncing
JS_TOPICS[110] = {
    "id": 110,
    "title": "Debouncing",
    "category": "Testing and Performance Optimization",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "Debouncing is a rate-limiting technique that delays function execution until user activity has paused for a defined time.",
    "theory": "1. What is Debouncing?\nDebouncing controls function execution frequency during rapidly triggered events (typing, window resize, scroll pause). It ensures the function executes ONLY once after user activity stops for a set delay.\n\n2. Debounce Function Implementation:\n```js\nfunction debounce(func, delay) {\n    let timer;\n    return function(...args) {\n        clearTimeout(timer); // Cancel previous timer\n        timer = setTimeout(() => {\n            func.apply(this, args);\n        }, delay);\n    };\n}\n```\n\n3. Working Mechanism:\n- Rapid event triggers reset the internal `setTimeout` timer via `clearTimeout`.\n- The target function executes only after the specified pause duration.\n\n4. Typical Use Cases:\n- Search Bar Input (autocomplete API calls).\n- Window Resizing calculations.\n- Real-time Form Field Validation.\n\n5. Debouncing vs Throttling:\n- **Debouncing**: Executes function once AFTER events stop for a delay.\n- **Throttling**: Executes function at fixed regular intervals during continuous events.",
    "syntax": "// Higher-Order Debounce Helper\nfunction debounce(fn, delay) {\n    let timer;\n    return function(...args) {\n        clearTimeout(timer);\n        timer = setTimeout(() => fn.apply(this, args), delay);\n    };\n}",
    "example": {
        "code": "// 1. Debounce Function Helper\nfunction createDebouncedFunction(fn, delay) {\n    let timer;\n    return function(...args) {\n        clearTimeout(timer);\n        timer = setTimeout(() => fn(...args), delay);\n    };\n}\n\n// 2. Simulating User Typing in Search Input\nlet apiRequests = [];\nfunction handleSearch(query) {\n    apiRequests.push(`Query: '${query}'`);\n}\n\nconst debouncedSearch = createDebouncedFunction(handleSearch, 100);\n\n// Rapid keystrokes within 100ms\ndebouncedSearch('H');\ndebouncedSearch('Hel');\ndebouncedSearch('Hello'); // Only this final call executes after pause!\n\nsetTimeout(() => {\n    console.log('Total API Requests Sent:', apiRequests.length);\n    console.log('Logged Request:', apiRequests[0]);\n}, 150);",
        "output": "Total API Requests Sent: 1\nLogged Request: Query: 'Hello'",
        "explanation": "Demonstrates how debouncing cancels earlier timer instances using clearTimeout() so that only the final search query triggers an API request.",
    },
    "fill_blanks": {
        "question": "// In a debounce implementation, clearing the previous timer using _____ prevents early execution.\n// Debouncing executes the target function only after user events _____ for a specified delay.",
        "answers": ["clearTimeout", "stop"],
        "options": ["clearTimeout", "stop", "clearInterval", "start"],
    },
    "compiler": {
        "title": "Debouncing Sandbox",
        "question": "Complete the debounce timer cancellation.",
        "starter_code": "function debounce(fn, delay) {\n    let timer;\n    return function(...args) {\n        _____(timer);\n        timer = setTimeout(() => fn.apply(this, args), delay);\n    };\n}",
        "options": ["clearTimeout", "clearInterval", "stopTimeout", "cancelTimer"],
    },
    "skill_exa_test": [
        {
            "question": "What is the main purpose of applying debouncing to a search bar input field?",
            "options": [
                "To delay sending API search requests until the user finishes typing for a specified pause duration",
                "To automatically translate search queries",
                "To force API requests on every single keystroke",
                "To encrypt search input text"
            ],
            "answer": "To delay sending API search requests until the user finishes typing for a specified pause duration",
        },
        {
            "question": "Which function is called inside a debounced wrapper to cancel previously scheduled timers when rapid events occur?",
            "options": ["`clearTimeout()`", "`clearInterval()`", "`cancelAnimationFrame()`", "`resetTimer()`"],
            "answer": "`clearTimeout()`",
        },
        {
            "question": "What is the key functional difference between Debouncing and Throttling?",
            "options": [
                "Debouncing executes a function once after activity stops for a delay, while Throttling executes a function at fixed regular intervals during continuous activity",
                "Debouncing only works in Python while Throttling works in JavaScript",
                "Throttling delays execution until mouse hover",
                "They are completely identical"
            ],
            "answer": "Debouncing executes a function once after activity stops for a delay, while Throttling executes a function at fixed regular intervals during continuous activity",
        },
        {
            "question": "What type of function is `debounce()` in JavaScript?",
            "options": [
                "A Higher-Order Function (takes a function and delay as parameters and returns a new debounced wrapper function)",
                "A constructor function",
                "An async generator",
                "A native DOM element"
            ],
            "answer": "A Higher-Order Function (takes a function and delay as parameters and returns a new debounced wrapper function)",
        },
        {
            "question": "What happens if a user types 10 characters rapidly within 50ms when a search function is debounced by 300ms?",
            "options": [
                "The search function executes exactly once, 300ms after the 10th character is typed",
                "The search function executes 10 times",
                "The search function never executes",
                "It throws a SyntaxError"
            ],
            "answer": "The search function executes exactly once, 300ms after the 10th character is typed",
        },
    ],
}

# Override Topic 111: Throttling
JS_TOPICS[111] = {
    "id": 111,
    "title": "Throttling",
    "category": "Testing and Performance Optimization",
    "difficulty": "Advanced",
    "duration": "30 min",
    "concept": "Throttling is a performance optimization technique that restricts function execution to at most once per fixed time interval.",
    "theory": "1. What is Throttling?\nThrottling controls how often a function executes within a fixed time interval. It ensures functions run at a steady, controlled rate during heavy, continuous events (scrolling, window resizing, mouse movement).\n\n2. Implementation Approaches:\na. **Timestamp-based (`Date.now()`)**:\n   ```js\n   function throttle(fn, delay) {\n       let lastTime = 0;\n       return function(...args) {\n           let now = Date.now();\n           if (now - lastTime >= delay) {\n               fn.apply(this, args);\n               lastTime = now;\n           }\n       };\n   }\n   ```\nb. **`setTimeout` with Boolean Flag**:\n   Sets `isThrottled = true`, executes function, and resets flag after `delay` ms.\n\n3. Why Requirement for Throttling?\n- Reduces CPU & memory spikes.\n- Prevents unresponsive UIs during infinite scroll or resize handlers.\n- Protects backend APIs against excessive rate limit calls.\n\n4. Typical Use Cases:\n- Scroll event handling (infinite scrolling).\n- Window resize event handling.\n- Drag-and-drop mouse move events.\n- API rate-limiting.",
    "syntax": "// Timestamp-Based Throttle Implementation\nfunction throttle(fn, delay) {\n    let lastTime = 0;\n    return function(...args) {\n        let now = Date.now();\n        if (now - lastTime >= delay) {\n            fn.apply(this, args);\n            lastTime = now;\n        }\n    };\n}",
    "example": {
        "code": "// 1. Timestamp-based Throttle Helper\nfunction throttle(fn, delay) {\n    let lastTime = 0;\n    return function(...args) {\n        let now = Date.now();\n        if (now - lastTime >= delay) {\n            fn.apply(this, args);\n            lastTime = now;\n        }\n    };\n}\n\n// 2. Simulating Rapid Continuous Scroll Events\nlet executions = 0;\nfunction handleScroll() {\n    executions++;\n}\n\nconst throttledScroll = throttle(handleScroll, 100);\n\n// Rapid calls triggered at t=0ms\nthrottledScroll(); // Executes (now - 0 >= 100)\nthrottledScroll(); // Ignored (0ms gap)\nthrottledScroll(); // Ignored (0ms gap)\n\nconsole.log('Throttled Executions Count:', executions);",
        "output": "Throttled Executions Count: 1",
        "explanation": "Demonstrates restricting continuous execution calls using a timestamp gap check (now - lastTime >= delay).",
    },
    "fill_blanks": {
        "question": "// Throttling ensures a function executes at most once per fixed time _____.\n// To track elapsed time in a timestamp throttle, we compare Date.now() against _____.",
        "answers": ["interval", "lastTime"],
        "options": ["interval", "lastTime", "delay", "timeout"],
    },
    "compiler": {
        "title": "Throttling Sandbox",
        "question": "Complete the timestamp gap check in throttle.",
        "starter_code": "function throttle(fn, delay) {\n    let lastTime = 0;\n    return function(...args) {\n        let now = Date.now();\n        if (now - lastTime >= _____) {\n            fn.apply(this, args);\n            lastTime = now;\n        }\n    };\n}",
        "options": ["delay", "now", "lastTime", "1000"],
    },
    "skill_exa_test": [
        {
            "question": "What is the primary goal of applying throttling to scroll or resize event listeners?",
            "options": [
                "To limit function execution frequency to at most once per fixed time interval, preventing browser lag and CPU spikes",
                "To delay function execution until scrolling completely stops",
                "To disable user scrolling",
                "To encrypt event data"
            ],
            "answer": "To limit function execution frequency to at most once per fixed time interval, preventing browser lag and CPU spikes",
        },
        {
            "question": "In a timestamp-based `throttle(fn, delay)` implementation, when is `fn` allowed to execute?",
            "options": [
                "When `Date.now() - lastTime >= delay`",
                "When `Date.now() === 0`",
                "When `lastTime > delay`",
                "Only on page load"
            ],
            "answer": "When `Date.now() - lastTime >= delay`",
        },
        {
            "question": "Which user interaction is a primary candidate for Throttling rather than Debouncing?",
            "options": [
                "Infinite scrolling page handler where intermediate scroll progress needs to be processed continuously at a steady rate",
                "Search bar autocomplete input field",
                "Form submission button click",
                "Text input auto-save on typing pause"
            ],
            "answer": "Infinite scrolling page handler where intermediate scroll progress needs to be processed continuously at a steady rate",
        },
        {
            "question": "What happens to event triggers that occur during the throttle delay interval?",
            "options": [
                "They are ignored until the current time interval completes",
                "They throw a TypeError",
                "They are stored in a database",
                "They reload the webpage"
            ],
            "answer": "They are ignored until the current time interval completes",
        },
        {
            "question": "Which method can be used inside `setTimeout` throttling to reset the throttle flag after the delay ends?",
            "options": [
                "Setting boolean flag `isThrottled = false` inside `setTimeout` callback",
                "Calling `window.close()`",
                "Calling `Math.random()`",
                "Deleting the function"
            ],
            "answer": "Setting boolean flag `isThrottled = false` inside `setTimeout` callback",
        },
    ],
}

# Override Topic 112: Simple Tic-Tac-Toe Game
JS_TOPICS[112] = {
    "id": 112,
    "title": "Simple Tic-Tac-Toe Game",
    "category": "JavaScript Projects",
    "difficulty": "Intermediate",
    "duration": "35 min",
    "concept": "Building a simple, interactive turn-based Tic-Tac-Toe web application using HTML flexbox layout, CSS styling, and JavaScript DOM manipulation, event listeners, 2D winning pattern evaluation, draw detection, and state resets.",
    "theory": "1. Project Overview & Features:\n- Interactive 2-player turn-based gameplay ('O' and 'X').\n- Automatic result checking for 8 winning patterns (3 rows, 3 columns, 2 diagonals).\n- Draw detection when all 9 grid boxes are filled without a winning line.\n- Modal announcement banner for winner and draw status.\n- Reset & New Game buttons to restart gameplay dynamically.\n\n2. HTML Board Structure & CSS Flexbox Grid:\n- Game grid built with 9 HTML `<button class=\"box\"></button>` elements inside a `.game` wrapper container.\n- CSS flexbox layout centers the board and uses `vmin` units for responsiveness (`height: 60vmin; width: 60vmin; gap: 1.5vmin;`).\n- Interactive box styling with rounded borders, box shadows, hover effects (`background-color: chocolate`), and large font sizes (`8vmin`).\n- Result container (`.msg-container.hide`) kept hidden by default using `display: none` until game over.\n\n3. JavaScript State Tracking & 2D Win Patterns:\n- `turnO`: Boolean flag (`true` for Player O, `false` for Player X).\n- `winPatterns`: 2D array containing the 8 winning index triplets:\n  `[[0,1,2], [0,3,6], [0,4,8], [1,4,7], [2,5,8], [2,4,6], [3,4,5], [6,7,8]]`.\n\n4. Event Listeners & Move Logic:\n- Iterate over boxes via `document.querySelectorAll('.box')` and attach `click` event listeners.\n- On click: set box text ('O' or 'X'), set color, set `box.disabled = true` to lock choice, toggle `turnO = !turnO`, and call `checkWinner()`.\n\n5. Winner Checking & Reset Logic:\n- `checkWinner()` loops through `winPatterns` to verify if values at positions `p1`, `p2`, and `p3` match.\n- If matched, invoke `showWinner(winner)`, display `.msg-container`, and call `disableBoxes()` to block further moves.\n- If no winner and `[...boxes].every(b => b.innerText !== \"\")` is true, trigger 'Match Drawn'.\n- `resetGame()` clears all box text, re-enables buttons (`box.disabled = false`), hides message container, and resets `turnO = true`.",
    "syntax": "// Turn-based Move & Win Pattern Check Syntax\nlet turnO = true;\nconst winPatterns = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,5,8],[2,4,6],[3,4,5],[6,7,8]];\n\nboxes.forEach(box => {\n    box.addEventListener('click', () => {\n        box.innerText = turnO ? 'O' : 'X';\n        box.disabled = true;\n        turnO = !turnO;\n        checkWinner();\n    });\n});",
    "example": {
        "code": "// 1. Simulating Tic-Tac-Toe Game Logic Engine in JavaScript\nclass TicTacToeGame {\n    constructor() {\n        this.boxes = Array(9).fill('');\n        this.turnO = true; // Player O starts\n        this.winner = null;\n        this.isDraw = false;\n        this.winPatterns = [\n            [0, 1, 2], [0, 3, 6], [0, 4, 8],\n            [1, 4, 7], [2, 5, 8], [2, 4, 6],\n            [3, 4, 5], [6, 7, 8]\n        ];\n    }\n    makeMove(index) {\n        if (this.boxes[index] !== '' || this.winner) return;\n        this.boxes[index] = this.turnO ? 'O' : 'X';\n        this.turnO = !this.turnO;\n        this.checkWinner();\n    }\n    checkWinner() {\n        for (let pattern of this.winPatterns) {\n            let [p1, p2, p3] = pattern;\n            let v1 = this.boxes[p1], v2 = this.boxes[p2], v3 = this.boxes[p3];\n            if (v1 !== '' && v1 === v2 && v2 === v3) {\n                this.winner = v1;\n                return;\n            }\n        }\n        if (this.boxes.every(val => val !== '')) {\n            this.isDraw = true;\n        }\n    }\n}\n\n// 2. Play sample game: Player O completes top row (indices 0, 1, 2)\nconst ttt = new TicTacToeGame();\nttt.makeMove(0); // O at 0\nttt.makeMove(3); // X at 3\nttt.makeMove(1); // O at 1\nttt.makeMove(4); // X at 4\nttt.makeMove(2); // O at 2 -> Win!\n\nconsole.log('Game Winner:', ttt.winner);\nconsole.log('Top Row State:', ttt.boxes.slice(0, 3).join(' | '));",
        "output": "Game Winner: O\nTop Row State: O | O | O",
        "explanation": "Demonstrates executing Tic-Tac-Toe turn-based player moves, state array updates, and winning pattern evaluation to declare Player O the winner.",
    },
    "fill_blanks": {
        "question": "<!-- Tic-Tac-Toe HTML, CSS & JavaScript Code -->\n<!-- HTML Structure -->\n<div class=\"msg-container hide\">\n    <p id=\"msg\">Winner</p>\n    <button id=\"new-btn\">New Game</button>\n</div>\n<div class=\"container\">\n    <div class=\"game\">\n        <button class=\"box\"></button><button class=\"box\"></button><button class=\"box\"></button>\n        <button class=\"box\"></button><button class=\"box\"></button><button class=\"box\"></button>\n        <button class=\"box\"></button><button class=\"box\"></button><button class=\"box\"></button>\n    </div>\n</div>\n<button id=\"reset\">Reset Game</button>\n\n<!-- JavaScript Game Logic -->\n<script>\nlet boxes = [...document.querySelectorAll('.box')];\nlet turnO = true;\nlet msgContainer = document.querySelector('.msg-container');\nlet msg = document.querySelector('#msg');\n\nconst winPatterns = [\n    [0, 1, 2], [0, 3, 6], [0, 4, 8],\n    [1, 4, 7], [2, 5, 8], [2, 4, 6],\n    [3, 4, 5], [6, 7, 8]\n];\n\nboxes.forEach((box) => {\n    box._____('click', function () {\n        if (turnO) {\n            box.innerText = 'O';\n            turnO = false;\n            box._____ = true;\n            checkWinner();\n        } else {\n            box.innerText = 'X';\n            turnO = true;\n            box.disabled = true;\n            checkWinner();\n        }\n    });\n});\n\nconst showWinner = (winner) => {\n    msg.innerText = `Congratulations, Winner is ${winner}`;\n    msgContainer.classList._____('hide');\n};\n</script>",
        "answers": ["addEventListener", "disabled", "remove"],
        "options": ["addEventListener", "disabled", "remove", "querySelectorAll", "enabled", "add"],
    },
    "compiler": {
        "title": "Tic-Tac-Toe Sandbox",
        "question": "Complete the JavaScript winner checking condition by ensuring all 3 position values in a win pattern are strictly equal.",
        "starter_code": "const checkWinner = (boxes, winPatterns) => {\n    for (let pattern of winPatterns) {\n        let pos1Val = boxes[pattern[0]];\n        let pos2Val = boxes[pattern[1]];\n        let pos3Val = boxes[pattern[2]];\n        if (pos1Val !== '' && pos2Val !== '' && pos3Val !== '' && pos1Val === pos2Val && pos2Val _____ pos3Val) {\n            return pos1Val;\n        }\n    }\n    return null;\n};",
        "options": ["===", "!==", "==", "="],
    },
    "skill_exa_test": [
        {
            "question": "How are winning line combinations defined in the JavaScript Tic-Tac-Toe game logic?",
            "options": [
                "A 2D array (`winPatterns`) containing 8 index triplets representing all winning rows, columns, and diagonals",
                "A 1D array of strings",
                "Calculated dynamically using `Math.random()`",
                "Stored in browser cookies"
            ],
            "answer": "A 2D array (`winPatterns`) containing 8 index triplets representing all winning rows, columns, and diagonals",
        },
        {
            "question": "What DOM property is set to `true` on a grid box button after a player clicks it?",
            "options": ["`box.disabled = true`", "`box.hidden = true`", "`box.locked = true`", "`box.value = true`"],
            "answer": "`box.disabled = true`",
        },
        {
            "question": "Which JavaScript array method checks if every grid box is non-empty to declare a Match Draw?",
            "options": ["`[...boxes].every(box => box.innerText !== \"\")`", "`[...boxes].filter()`", "`[...boxes].map()`", "`[...boxes].includes()`"],
            "answer": "`[...boxes].every(box => box.innerText !== \"\")`",
        },
        {
            "question": "Which DOM operation reveals the winner announcement container when a player wins the game?",
            "options": [
                "`msgContainer.classList.remove('hide')`",
                "`msgContainer.style.visibility = 'none'`",
                "`msgContainer.classList.add('hide')`",
                "`msgContainer.remove()`"
            ],
            "answer": "`msgContainer.classList.remove('hide')`",
        },
        {
            "question": "What actions does the `resetGame()` function execute when starting a fresh game?",
            "options": [
                "Resets `turnO = true`, clears box text, re-enables all grid buttons, and hides the result message banner",
                "Reloads the entire webpage from the server",
                "Deletes all HTML buttons from the DOM",
                "Changes player markers from X and O to numbers"
            ],
            "answer": "Resets `turnO = true`, clears box text, re-enables all grid buttons, and hides the result message banner",
        },
    ],
}





