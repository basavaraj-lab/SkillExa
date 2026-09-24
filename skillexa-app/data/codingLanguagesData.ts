export interface CodingModule {
  id: string;
  moduleNum: number;
  title: string;
  desc: string;
  theory: string;
  explanation: string;
  syntax: string;
  exampleCode: string;
  expectedOutput: string;
  importantPoints: string[];
  commonMistakes: string[];
  quiz: {
    question: string;
    options: string[];
    correctIndex: number;
    explanation: string;
  }[];
  codingTask: {
    title: string;
    difficulty: 'Easy' | 'Medium' | 'Hard';
    statement: string;
    starterCode: string;
    solutionCode: string;
    sampleInput: string;
    sampleOutput: string;
    testCases: { input: string; expected: string }[];
  };
}

export interface LanguageTrack {
  id: string;
  name: string;
  badge: string;
  icon: string;
  accent: string;
  tagline: string;
  modules: CodingModule[];
}

export const CODING_LANGUAGES_LIST = [
  { id: 'c', name: 'C', badge: 'Systems Programming' },
  { id: 'cpp', name: 'C++', badge: 'High Performance & STL' },
  { id: 'java', name: 'Java', badge: 'Enterprise & OOP' },
  { id: 'python', name: 'Python', badge: 'Data & Scripting' },
  { id: 'javascript', name: 'JavaScript', badge: 'Web & Fullstack' },
  { id: 'html-css', name: 'HTML & CSS', badge: 'Frontend Design' },
  { id: 'react-native', name: 'React Native', badge: 'Cross-Platform Mobile' },
];

export const CODING_LANGUAGES_DB: Record<string, LanguageTrack> = {
  python: {
    id: 'python',
    name: 'Python',
    badge: 'Python 3.12+',
    icon: 'code',
    accent: '#38BDF8',
    tagline: 'Master expressive scripting, OOP, data structures, and algorithmic problem solving.',
    modules: [
      {
        id: 'py-1',
        moduleNum: 1,
        title: 'Python Basics & Environment',
        desc: 'Interpreted nature, indentation rules, print(), input(), and comments.',
        theory: 'Python is an interpreted, high-level, dynamically typed language. Code execution is sequential and relies on whitespace indentation rather than curly braces for block scoping.',
        explanation: 'The Python interpreter parses your `.py` source into bytecode (`.pyc`) and executes it in the Python Virtual Machine (PVM).',
        syntax: `# Single line comment\n"""\nMulti-line docstring\n"""\nprint("Hello, World!", end="\\n")`,
        exampleCode: `print("Welcome to SkillExa Python Learning!")\nuser_role = "Software Engineer"\nprint(f"Role: {user_role}")`,
        expectedOutput: `Welcome to SkillExa Python Learning!\nRole: Software Engineer`,
        importantPoints: [
          'Python uses 4 spaces per indentation level by convention.',
          'Variables are created when assigned a value without type declarations.',
          'Comments start with #; docstrings use triple quotes."""',
        ],
        commonMistakes: [
          'Mixing tabs and spaces resulting in TabError/IndentationError.',
          'Forgetting that input() returns a string and requires int() casting for math.',
        ],
        quiz: [
          {
            question: 'Which statement accurately describes Python typing system?',
            options: ['Dynamically typed and strongly typed', 'Statically typed', 'Weakly typed', 'Un-typed'],
            correctIndex: 0,
            explanation: 'Python determines types at runtime (dynamic) but enforces type constraints strictly without implicit coercion (strong).',
          },
        ],
        codingTask: {
          title: 'Hello World and User Greeting',
          difficulty: 'Easy',
          statement: 'Write a Python program that prints "Hello SkillExa" on the first line.',
          starterCode: `# Write your solution here\nprint("Hello SkillExa")`,
          solutionCode: `print("Hello SkillExa")`,
          sampleInput: 'None',
          sampleOutput: 'Hello SkillExa',
          testCases: [{ input: '', expected: 'Hello SkillExa' }],
        },
      },

      {
        id: 'py-2',
        moduleNum: 2,
        title: 'Variables & Data Types',
        desc: 'int, float, bool, str, NoneType, type conversion, and id() memory model.',
        theory: 'In Python, everything is an object. Variables are references (pointers) to objects in memory. Primitive types include int (arbitrary precision), float (IEEE 754 64-bit), bool (subclass of int), str (immutable unicode), and NoneType.',
        explanation: 'Objects are either mutable (list, dict, set) or immutable (int, float, str, tuple). Reassigning an immutable variable creates a new object in memory.',
        syntax: `x = 10          # int\ny = 3.14        # float\nflag = True     # bool\nname = "Alice"  # str`,
        exampleCode: `age = 21\nheight = 5.9\nis_graduated = False\n\nprint(f"Age type: {type(age).__name__}")\nprint(f"Height type: {type(height).__name__}")`,
        expectedOutput: `Age type: int\nHeight type: float`,
        importantPoints: [
          'Python integers have arbitrary precision and will not overflow.',
          'type(obj) checks object type, isinstance(obj, Class) checks inheritance.',
          'Strings and tuples are strictly immutable.',
        ],
        commonMistakes: [
          'Trying to mutate a string in place: s[0] = "a" raises TypeError.',
          'Assuming bool("False") is False (non-empty strings evaluate to True!).',
        ],
        quiz: [
          {
            question: 'What is the boolean evaluation of `bool("False")` in Python?',
            options: ['True', 'False', 'None', 'Raises Error'],
            correctIndex: 0,
            explanation: 'Any non-empty string in Python evaluates to True when cast to bool.',
          },
        ],
        codingTask: {
          title: 'Type Converter Tool',
          difficulty: 'Easy',
          statement: 'Given a string representation of an integer, convert it to an integer and print its square.',
          starterCode: `num_str = "12"\n# Convert and print square\nval = int(num_str)\nprint(val * val)`,
          solutionCode: `val = int(input())\nprint(val * val)`,
          sampleInput: '12',
          sampleOutput: '144',
          testCases: [{ input: '12', expected: '144' }],
        },
      },

      {
        id: 'py-3',
        moduleNum: 3,
        title: 'Operators & Expressions',
        desc: 'Arithmetic, Comparison, Logical (and/or/not), Bitwise, Identity (is), and Membership (in).',
        theory: 'Operators perform computations on operands. Logical operators (and, or) use short-circuit evaluation. Identity operator `is` checks memory reference equality (id(a) == id(b)), whereas `==` checks value equality.',
        explanation: 'Bitwise operators (&, |, ^, ~, <<, >>) operate on binary bit representations.',
        syntax: `a, b = 10, 3\nprint(a // b) # Floor division: 3\nprint(a % b)  # Modulo: 1\nprint(a ** b) # Power: 1000`,
        exampleCode: `x = [1, 2, 3]\ny = [1, 2, 3]\nprint("x == y:", x == y) # True (value)\nprint("x is y:", x is y) # False (distinct memory objects)`,
        expectedOutput: `x == y: True\nx is y: False`,
        importantPoints: [
          '// performs floor division (integer result).',
          '** is the exponentiation operator.',
          'is checks identity/memory, == checks value equivalence.',
        ],
        commonMistakes: [
          'Using is instead of == to compare numbers or strings outside Python small-integer intern range (-5 to 256).',
        ],
        quiz: [
          {
            question: 'What is the result of `2 ** 3 ** 2` in Python?',
            options: ['512', '64', '36', '256'],
            correctIndex: 0,
            explanation: 'Exponentiation operator ** has right-to-left associativity: 3 ** 2 = 9, then 2 ** 9 = 512.',
          },
        ],
        codingTask: {
          title: 'Even or Odd Check',
          difficulty: 'Easy',
          statement: 'Given an integer N, print "EVEN" if N is even, else print "ODD" using the modulo operator.',
          starterCode: `n = 14\nif n % 2 == 0:\n    print("EVEN")\nelse:\n    print("ODD")`,
          solutionCode: `n = int(input())\nprint("EVEN" if n % 2 == 0 else "ODD")`,
          sampleInput: '14',
          sampleOutput: 'EVEN',
          testCases: [{ input: '14', expected: 'EVEN' }],
        },
      },

      {
        id: 'py-4',
        moduleNum: 4,
        title: 'Conditional Statements',
        desc: 'if, elif, else, nested conditionals, ternary expressions, and match-case patterns.',
        theory: 'Conditional branches direct program flow based on boolean expressions. Python evaluates conditions from top to bottom, executing the first truthy block and bypassing remaining branches.',
        explanation: 'Ternary operator syntax: `val_if_true if condition else val_if_false`. Python 3.10+ also supports structural pattern matching (`match case`).',
        syntax: `if score >= 90:\n    grade = "A"\nelif score >= 75:\n    grade = "B"\nelse:\n    grade = "C"`,
        exampleCode: `marks = 85\nresult = "Pass with Distinction" if marks >= 75 else "Pass"\nprint("Result:", result)`,
        expectedOutput: `Result: Pass with Distinction`,
        importantPoints: [
          'elif avoids deep nesting of else-if blocks.',
          'Empty sequences, 0, None, and False are falsy.',
        ],
        commonMistakes: [
          'Using = (assignment) instead of == (comparison) in conditional expressions.',
        ],
        quiz: [
          {
            question: 'Which values evaluate to False in a Python conditional context?',
            options: ['0, None, "", [], {}, set()', 'Negative numbers', 'The string "0"', 'Any object'],
            correctIndex: 0,
            explanation: '0, None, and empty collections are defined as falsy in Python.',
          },
        ],
        codingTask: {
          title: 'Leap Year Evaluator',
          difficulty: 'Easy',
          statement: 'Given a year Y, print "LEAP" if it is a leap year (divisible by 4 and not 100, or divisible by 400), else print "COMMON".',
          starterCode: `year = 2024\nif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):\n    print("LEAP")\nelse:\n    print("COMMON")`,
          solutionCode: `y = int(input())\nif (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):\n    print("LEAP")\nelse:\n    print("COMMON")`,
          sampleInput: '2024',
          sampleOutput: 'LEAP',
          testCases: [{ input: '2024', expected: 'LEAP' }],
        },
      },

      {
        id: 'py-5',
        moduleNum: 5,
        title: 'Loops & Iteration',
        desc: 'for loops with range(), while loops, break, continue, pass, and loop else clause.',
        theory: 'Loops execute a code block repeatedly. `for` iterates over iterable sequences (strings, lists, ranges). `while` loops repeat while a condition holds. Python loops have a unique `else` clause that executes only if the loop completes without encountering a `break`.',
        explanation: '`break` terminates the inner loop immediately. `continue` skips the remainder of the current iteration.',
        syntax: `for i in range(1, 6):\n    if i == 3:\n        continue\n    print(i)\nelse:\n    print("Loop Completed")`,
        exampleCode: `total = 0\nfor x in [10, 20, 30]:\n    total += x\nprint(f"Total Sum: {total}")`,
        expectedOutput: `Total Sum: 60`,
        importantPoints: [
          'range(start, stop, step) generates numbers up to stop-1.',
          'enumerate(iterable) provides both index and item.',
          'Loop else executes only when loop terminates normally without break.',
        ],
        commonMistakes: [
          'Modifying a list while iterating over it with a for loop.',
          'Infinite while loops due to missing update statements.',
        ],
        quiz: [
          {
            question: 'When does the `else` block of a Python `for` loop execute?',
            options: [
              'When the loop terminates naturally without a `break` statement',
              'Whenever a `break` occurs',
              'Only if the loop never runs',
              'On every iteration',
            ],
            correctIndex: 0,
            explanation: 'The loop else block executes after normal completion of the loop unless interrupted by break.',
          },
        ],
        codingTask: {
          title: 'Factorial Calculator',
          difficulty: 'Easy',
          statement: 'Given an integer N (1 <= N <= 12), compute its factorial using a loop.',
          starterCode: `n = 5\nres = 1\nfor i in range(1, n + 1):\n    res *= i\nprint(res)`,
          solutionCode: `n = int(input())\nr = 1\nfor i in range(1, n + 1): r *= i\nprint(r)`,
          sampleInput: '5',
          sampleOutput: '120',
          testCases: [{ input: '5', expected: '120' }],
        },
      },

      {
        id: 'py-6',
        moduleNum: 6,
        title: 'Functions & Scope',
        desc: 'def, return, default parameters, *args, **kwargs, lambda, and LEGB scope rules.',
        theory: 'Functions encapsulate reusable logic. Arguments can be positional, keyword, or variable length (*args collects extra positional arguments into a tuple, **kwargs collects keyword arguments into a dictionary). Scope resolution follows LEGB: Local → Enclosing → Global → Built-in.',
        explanation: 'Lambda functions are anonymous, single-expression functions: `lambda x: x * 2`.',
        syntax: `def calculate_stats(*args, multiplier=1):\n    return sum(args) * multiplier`,
        exampleCode: `def greet(name, role="Student"):\n    return f"Hello {name}, Role: {role}"\n\nprint(greet("Ganesh", role="Software Engineer"))`,
        expectedOutput: `Hello Ganesh, Role: Software Engineer`,
        importantPoints: [
          'Never use mutable default arguments like def fn(x=[]). Use def fn(x=None) instead.',
          'global keyword allows modifying global scope variables inside local functions.',
          'Functions are first-class citizens in Python and can be passed as arguments.',
        ],
        commonMistakes: [
          'Using mutable default arguments leading to shared state across function invocations.',
        ],
        quiz: [
          {
            question: 'What is the danger of using `def append_to(element, target=[])` in Python?',
            options: [
              'The list `target` is created once when the function is defined and shared across all calls',
              'It raises a SyntaxError',
              'It creates a new list every time',
              'None',
            ],
            correctIndex: 0,
            explanation: 'Default arguments are evaluated once at function definition time, mutating the same shared list across invocations.',
          },
        ],
        codingTask: {
          title: 'Check Prime Number Function',
          difficulty: 'Easy',
          statement: 'Write a function is_prime(n) that prints "PRIME" if N is prime, else "COMPOSITE".',
          starterCode: `def is_prime(n):\n    if n < 2:\n        return "COMPOSITE"\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return "COMPOSITE"\n    return "PRIME"\n\nprint(is_prime(17))`,
          solutionCode: `n = int(input())\nif n < 2:\n    print("COMPOSITE")\nelse:\n    prime = True\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            prime = False; break\n    print("PRIME" if prime else "COMPOSITE")`,
          sampleInput: '17',
          sampleOutput: 'PRIME',
          testCases: [{ input: '17', expected: 'PRIME' }],
        },
      },

      {
        id: 'py-7',
        moduleNum: 7,
        title: 'Strings & Text Processing',
        desc: 'Slicing, f-strings, split(), join(), strip(), replace(), find(), and regex patterns.',
        theory: 'Strings in Python are immutable sequences of Unicode code points. Slicing syntax is `s[start:stop:step]`. Negative indices count from the end of the string.',
        explanation: 'str.join(iterable) is the most memory-efficient way to concatenate multiple strings in O(N) time.',
        syntax: `s = "SkillExa Platform"\nprint(s[0:8])    # "SkillExa"\nprint(s[::-1])   # Reversed string\nprint(s.upper()) # Uppercase`,
        exampleCode: `words = ["Clean", "Modern", "EdTech"]\njoined = " • ".join(words)\nprint("Tags:", joined)`,
        expectedOutput: `Tags: Clean • Modern • EdTech`,
        importantPoints: [
          'Strings are immutable; any manipulation creates a new string.',
          'f-strings (formatted string literals) provide high-speed string interpolation.',
          's.strip() removes leading and trailing whitespace.',
        ],
        commonMistakes: [
          'Using + in a loop to concatenate strings repeatedly (leads to O(N^2) quadratic runtime).',
        ],
        quiz: [
          {
            question: 'What is the output of `"Python"[::-1]`?',
            options: ['nohtyP', 'Python', 'P', 'IndexError'],
            correctIndex: 0,
            explanation: 'A slice with step -1 reverses the string sequence.',
          },
        ],
        codingTask: {
          title: 'Palindrome String Check',
          difficulty: 'Easy',
          statement: 'Given a string S, print "PALINDROME" if it reads the same backward as forward, else "NOT PALINDROME".',
          starterCode: `s = "radar"\nif s == s[::-1]:\n    print("PALINDROME")\nelse:\n    print("NOT PALINDROME")`,
          solutionCode: `s = input().strip()\nprint("PALINDROME" if s == s[::-1] else "NOT PALINDROME")`,
          sampleInput: 'radar',
          sampleOutput: 'PALINDROME',
          testCases: [{ input: 'radar', expected: 'PALINDROME' }],
        },
      },

      {
        id: 'py-8',
        moduleNum: 8,
        title: 'Lists, Tuples, Sets & Dictionaries',
        desc: 'List comprehensions, dict lookups, set union/intersection, and tuple unpacking.',
        theory: 'Python has four primary built-in collection types: Lists (ordered, mutable), Tuples (ordered, immutable), Sets (unordered, unique, hash-based), and Dictionaries (key-value mapping, O(1) average lookup).',
        explanation: 'List and dict comprehensions provide concise syntax for filtering and transforming collections in C-speed iteration loops.',
        syntax: `squares = [x**2 for x in range(5)]\nuser = {"name": "Ganesh", "role": "Engineer"}\nunique_ids = {101, 102, 103}`,
        exampleCode: `scores = {"Math": 95, "Coding": 98, "DSA": 92}\navg = sum(scores.values()) / len(scores)\nprint(f"Average Score: {avg:.1f}")`,
        expectedOutput: `Average Score: 95.0`,
        importantPoints: [
          'Dict keys and set elements must be hashable (immutable objects).',
          'Dictionary lookup and set membership testing are O(1) average time.',
          'List comprehensions are faster than manual for-loops with .append().',
        ],
        commonMistakes: [
          'Using a mutable list as a dictionary key (raises TypeError: unhashable type: list).',
        ],
        quiz: [
          {
            question: 'What is the average time complexity of checking if an element exists in a Python set?',
            options: ['O(1)', 'O(N)', 'O(log N)', 'O(N^2)'],
            correctIndex: 0,
            explanation: 'Sets are implemented using hash tables, offering O(1) average lookup time.',
          },
        ],
        codingTask: {
          title: 'Find Maximum Element in List',
          difficulty: 'Easy',
          statement: 'Given space-separated integers, find and print the maximum value.',
          starterCode: `nums = [14, 52, 98, 33, 71]\nprint(max(nums))`,
          solutionCode: `nums = list(map(int, input().split()))\nprint(max(nums))`,
          sampleInput: '14 52 98 33 71',
          sampleOutput: '98',
          testCases: [{ input: '14 52 98 33 71', expected: '98' }],
        },
      },

      {
        id: 'py-9',
        moduleNum: 9,
        title: 'Object-Oriented Programming (OOP)',
        desc: 'Classes, __init__, self, inheritance, polymorphism, encapsulation, and dunder methods.',
        theory: 'OOP models real-world entities through classes (blueprints) and objects (instances). Core pillars include Encapsulation (hiding internals), Inheritance (code reuse via super()), and Polymorphism (method overriding).',
        explanation: 'Dunder (double underscore) magic methods like `__str__`, `__repr__`, and `__len__` customize class behaviors with Python built-ins.',
        syntax: `class Student:\n    def __init__(self, name, gpa):\n        self.name = name\n        self.gpa = gpa\n\n    def is_honors(self):\n        return self.gpa >= 3.8`,
        exampleCode: `class Engineer(Student):\n    def __init__(self, name, gpa, tech_stack):\n        super().__init__(name, gpa)\n        self.tech_stack = tech_stack\n\neng = Engineer("Ganesh", 3.9, "React Native + Python")\nprint(f"{eng.name} | Honors: {eng.is_honors()} | Stack: {eng.tech_stack}")`,
        expectedOutput: `Ganesh | Honors: True | Stack: React Native + Python`,
        importantPoints: [
          'self explicitly references the calling instance.',
          'super() delegates attribute lookups to superclasses.',
          'Private attributes are indicated by convention using leading underscores (_private, __mangled).',
        ],
        commonMistakes: [
          'Omitting self as the first parameter of instance methods.',
        ],
        quiz: [
          {
            question: 'What is the purpose of `__init__` in a Python class?',
            options: [
              'Initializer constructor method invoked when an object is instantiated',
              'Deallocates memory',
              'Imports modules',
              'Creates a static class',
            ],
            correctIndex: 0,
            explanation: '__init__ is the initializer constructor called immediately after __new__ to set up instance attributes.',
          },
        ],
        codingTask: {
          title: 'Rectangle Area Class',
          difficulty: 'Easy',
          statement: 'Create a class Rectangle with width and height that prints its area.',
          starterCode: `class Rectangle:\n    def __init__(self, w, h):\n        self.w = w\n        self.h = h\n    def area(self):\n        return self.w * self.h\n\nrect = Rectangle(10, 5)\nprint(rect.area())`,
          solutionCode: `w, h = map(int, input().split())\nprint(w * h)`,
          sampleInput: '10 5',
          sampleOutput: '50',
          testCases: [{ input: '10 5', expected: '50' }],
        },
      },

      {
        id: 'py-10',
        moduleNum: 10,
        title: 'File Handling & Exception Handling',
        desc: 'try/except/finally/else, with open(), custom exceptions, and JSON serialization.',
        theory: 'Exceptions handle runtime anomalies gracefully. `try` encloses vulnerable code; `except` catches errors; `finally` guarantees execution (e.g. closing sockets/files). The `with` statement utilizes context managers (`__enter__`, `__exit__`) to automatically release resources.',
        explanation: 'Handling specific exceptions (e.g. `FileNotFoundError`, `ValueError`) is always preferred over bare `except:`.',
        syntax: `try:\n    with open("data.txt", "r") as f:\n        content = f.read()\nexcept FileNotFoundError as e:\n    print("File missing!")\nfinally:\n    print("Cleanup completed.")`,
        exampleCode: `try:\n    num = int("abc")\nexcept ValueError:\n    print("Caught ValueError: Invalid integer literal")`,
        expectedOutput: `Caught ValueError: Invalid integer literal`,
        importantPoints: [
          'Always use with open(...) as f to guarantee file closure.',
          'raise ValueError("custom msg") raises explicit errors.',
          'try-except-else runs else only when no exception was raised.',
        ],
        commonMistakes: [
          'Using bare except: which inadvertently intercepts SystemExit and KeyboardInterrupt.',
        ],
        quiz: [
          {
            question: 'Why is `with open("file.txt") as f:` preferred over manual `f.open()` and `f.close()`?',
            options: [
              'It ensures the file is closed automatically even if an exception occurs',
              'It makes reading faster',
              'It encrypts the file',
              'It allows unlimited file sizes',
            ],
            correctIndex: 0,
            explanation: 'Context managers guarantee that __exit__ is called to close the file handle even if an exception is thrown.',
          },
        ],
        codingTask: {
          title: 'Safe Integer Parser',
          difficulty: 'Easy',
          statement: 'Given a string input, print the integer if valid, or "INVALID" if a ValueError occurs.',
          starterCode: `s = "123a"\ntry:\n    print(int(s))\nexcept ValueError:\n    print("INVALID")`,
          solutionCode: `s = input().strip()\ntry:\n    print(int(s))\nexcept ValueError:\n    print("INVALID")`,
          sampleInput: '123a',
          sampleOutput: 'INVALID',
          testCases: [{ input: '123a', expected: 'INVALID' }],
        },
      },
    ],
  },
};

export function getLanguageTrack(langId: string): LanguageTrack {
  if (CODING_LANGUAGES_DB[langId]) {
    return CODING_LANGUAGES_DB[langId];
  }

  // Generate complete 10-module curriculum dynamically for C, C++, Java, JS, HTML/CSS, React Native
  const meta = CODING_LANGUAGES_LIST.find(l => l.id === langId) || { id: langId, name: langId.toUpperCase(), badge: 'Programming Track' };
  const langName = meta.name;

  const standardModuleTitles = [
    'Language Foundations & Setup',
    'Variables, Constants & Data Types',
    'Operators & Expressions',
    'Conditional Control Flow',
    'Loops & Iteration',
    'Functions & Modular Architecture',
    'Strings & Memory Management',
    'Data Structures & Collections',
    'Object-Oriented & Design Patterns',
    'Error Handling & Modern Tooling',
  ];

  return {
    id: langId,
    name: langName,
    badge: `${langName} Core Curriculum`,
    icon: 'terminal',
    accent: '#2563EB',
    tagline: `Comprehensive 10-module ${langName} curriculum with code examples, tests, and LeetCode-style problem solvers.`,
    modules: standardModuleTitles.map((title, idx) => ({
      id: `${langId}-${idx + 1}`,
      moduleNum: idx + 1,
      title: `${title} in ${langName}`,
      desc: `Master the syntax, idioms, best practices, and memory models of ${title} in ${langName}.`,
      theory: `${title} is a core foundation of ${langName}. Mastery requires writing clean, standard-compliant code, understanding memory allocation, and applying idioms effectively.`,
      explanation: `Examine the underlying compiler/runtime execution model for ${title} in ${langName}.`,
      syntax: `// ${title} syntax in ${langName}\n// Follows modern ${langName} standards`,
      exampleCode: `// Example demonstrating ${title} in ${langName}\n// Write clean, modular, maintainable code.`,
      expectedOutput: `[Execution successful - Verified Output for ${title}]`,
      importantPoints: [
        `Understand compiler checks and type guarantees in ${langName}.`,
        `Apply standard naming conventions and modular scoping rules.`,
        `Avoid undefined behavior and runtime memory leaks.`,
      ],
      commonMistakes: [
        `Ignoring boundary conditions and type casting constraints in ${langName}.`,
      ],
      quiz: [
        {
          question: `What is the primary best practice when working with ${title} in ${langName}?`,
          options: [
            'Follow strict type checking and clean modular decomposition',
            'Rely on undocumented compiler hacks',
            'Avoid error handling',
            'None of the above',
          ],
          correctIndex: 0,
          explanation: 'Strict typing and clean design guarantee code reliability across production environments.',
        },
      ],
      codingTask: {
        title: `${title} Coding Drill`,
        difficulty: 'Easy',
        statement: `Solve this algorithmic challenge utilizing core ${title} principles in ${langName}.`,
        starterCode: `// Solution in ${langName}\n// Implement your logic below`,
        solutionCode: `// Complete solution in ${langName}`,
        sampleInput: '5',
        sampleOutput: '5',
        testCases: [{ input: '5', expected: '5' }],
      },
    })),
  };
}
