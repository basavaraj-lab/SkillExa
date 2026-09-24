import {
  CommunityContentItem,
  CommunityFilterOptions,
  FacultyInterview,
  FacultyNote,
  FacultyQuiz,
  FacultyVideo,
  QuestionMetadata,
  StudentQuizSubmission,
  StudentTopicPerformance,
} from '../data/curriculumSchema';

export type FacultyQuestion = QuestionMetadata;

// Initial Mock Seed Data
let facultyNotesList: FacultyNote[] = [
  {
    id: 'fn-1',
    section: 'engineering',
    category: 'subjects',
    subject: 'Embedded Systems',
    topic: 'Microcontrollers',
    subtopic: 'ARM Cortex-M Architecture',
    title: 'ARM Cortex-M Hardware & Memory Mapped I/O',
    introduction: 'Complete architectural reference for registers, memory mapping, and deterministic interrupts.',
    theory: 'ARM Cortex-M series implements the ARMv7-M architecture with NVIC (Nested Vectored Interrupt Controller) providing low-latency interrupt handling.',
    importantConcepts: [
      'Memory Mapped GPIO registers (MODER, ODR, IDR, BSRR).',
      'Bit-banding feature in Cortex-M3/M4 for atomic bit manipulation.',
      'SysTick 24-bit system timer for OS tick generation.',
    ],
    formulas: ['Reload_Value = (Clock_Frequency * Desired_Time_Seconds) - 1'],
    rules: [
      'Always configure RCC clock gating before accessing peripheral registers.',
      'Declare hardware pointers as volatile to prevent compiler register caching.',
    ],
    examples: [
      {
        title: 'Atomic Pin Set Using BSRR Register',
        example: `// Set Pin 5 without read-modify-write\nGPIOA->BSRR = (1 << 5);`,
        explanation: 'Writing to the lower 16 bits of BSRR sets the pin atomically in hardware.',
      },
    ],
    importantPoints: [
      'BSRR atomic writes prevent race conditions when shared across multiple ISRs.',
    ],
    commonMistakes: [
      'Using read-modify-write (ODR |= (1 << 5)) inside nested interrupt contexts.',
    ],
    quickRevision: 'ARM Cortex-M uses NVIC for preemption, SysTick for OS timing, and memory-mapped registers for peripheral control.',
    pdfUrl: 'https://example.com/arm-cortex-notes.pdf',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    facultyName: 'Dr. Kusumadhara S',
    facultyDesignation: 'Associate Professor & HOD in-charge',
    facultyDepartment: 'ECE Department',
    collegeId: 'clg-kvg',
    collegeName: 'KVG College of Engineering',
    isVerifiedFaculty: true,
    visibility: 'college',
    published: true,
    createdAt: '2026-08-15',
  },
  {
    id: 'fn-2',
    section: 'competitive',
    category: 'english',
    subject: 'English Language',
    topic: 'Tenses & Verb Forms',
    subtopic: 'Past Anteriority & Inversion',
    title: 'Mastering Sequence of Tenses in Competitive Exams',
    introduction: 'Essential rules for SSC CGL, Banking, and PSC sentence improvement.',
    theory: 'When two actions happened in the past, the earlier action takes Past Perfect (had + V3) and the later action takes Simple Past (V2).',
    importantConcepts: [
      'By the time + Past Indefinite -> Past Perfect in main clause.',
      'Inversion after negative adverbs: "Hardly had I...", "No sooner did he...".',
    ],
    formulas: ['Hardly / Scarcely + had + Subject + V3 ... when + Subject + V2'],
    rules: [
      'Never use "than" with Hardly/Scarcely; always use "when".',
      'Use "than" exclusively with "No sooner".',
    ],
    examples: [
      {
        title: 'Negative Adverb Inversion',
        example: 'No sooner had the bell rung than the students entered the examination hall.',
        explanation: '"No sooner" takes auxiliary "had" before the subject and links with "than".',
      },
    ],
    importantPoints: ['High frequency spotting-the-error pattern in Tier 1 exams.'],
    commonMistakes: ['Writing "No sooner...when" instead of "No sooner...than".'],
    quickRevision: 'Past Anterior = had + V3; No sooner links with than; Hardly links with when.',
    facultyName: 'Prof. Ananya Sen',
    facultyDesignation: 'Senior Professor of English',
    facultyDepartment: 'Dept. of Humanities',
    collegeId: 'clg-presidency',
    collegeName: 'Presidency College',
    isVerifiedFaculty: true,
    visibility: 'community',
    published: true,
    createdAt: '2026-08-14',
  },
  {
    id: 'fn-comm-python',
    section: 'engineering',
    category: 'programming',
    subject: 'Programming in Python',
    topic: 'Functions & Scope',
    subtopic: 'Closures, *args, **kwargs & Decorators',
    language: 'python',
    title: 'Python Functions Mastery: First-Class Citizens, Closures & Decorator Patterns',
    introduction: 'Complete guide to functional paradigms, variable unpacking, LEGB scope resolution, and writing production decorators in Python.',
    theory: 'In Python, functions are first-class objects that can be passed as arguments, returned from other functions, and bound to variables. Variable resolution follows LEGB (Local, Enclosing, Global, Built-in).',
    importantConcepts: [
      '*args gathers positional arguments into a tuple; **kwargs gathers named arguments into a dict.',
      'Closures retain state of the enclosing scope even after outer function execution terminates.',
      'Decorators wrap a function modifying its behavior via Higher-Order Functions without altering source code.',
      'The @functools.wraps decorator preserves original function docstrings and signature.',
    ],
    formulas: ['def decorator(func): def wrapper(*args, **kwargs): return func(*args, **kwargs)'],
    rules: [
      'Default mutable arguments (e.g. def foo(x=[])) are evaluated once at function definition time, creating shared mutable bugs. Always use x=None.',
      'Use nonlocal keyword to mutate enclosing (non-global) variables in nested scopes.',
    ],
    examples: [
      {
        title: 'Execution Timer Decorator',
        example: `import time\nfrom functools import wraps\n\ndef timer_dec(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        print(f"{func.__name__} took {time.time() - start:.4f}s")\n        return result\n    return wrapper`,
        explanation: 'Uses wraps to preserve metadata and captures execution delta across arbitrary arguments.',
      },
    ],
    importantPoints: [
      'High frequency topic in FAANG/Product company technical interviews.',
      'Crucial for understanding Python web frameworks (FastAPI, Flask, Django).',
    ],
    commonMistakes: [
      'Using mutable default arguments like def append_to(item, target=[]).',
      'Forgetting to return the result from inside wrapper function in decorators.',
    ],
    quickRevision: 'LEGB rule governs scope; Closures retain enclosing state; Decorators wrap functions using closures; Avoid mutable defaults.',
    pdfUrl: 'https://example.com/python-functions-deepdive.pdf',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    facultyName: 'Dr. Sunita Rao',
    facultyDesignation: 'Professor & Head of Computer Science',
    facultyDepartment: 'Computer Science & Engineering',
    collegeId: 'clg-rvce',
    collegeName: 'R.V. College of Engineering (RVCE)',
    isVerifiedFaculty: true,
    visibility: 'community',
    published: true,
    createdAt: '2026-08-16',
  },
  {
    id: 'fn-comm-c-pointers',
    section: 'engineering',
    category: 'programming',
    subject: 'Programming in C',
    topic: 'Pointers & Memory',
    subtopic: 'Dynamic Memory & Void Pointers',
    language: 'c',
    title: 'C Pointers Deep Dive: Pointer Arithmetic, Memory Layout & Double Pointers',
    introduction: 'Exhaustive reference to virtual memory layout, stack vs heap allocation, pointer arithmetic, and avoiding dangling pointers/leaks.',
    theory: 'A pointer stores the virtual memory address of another variable. Pointer arithmetic scales by sizeof(type). Double pointers (**ptr) are required to modify pointer targets across function boundaries.',
    importantConcepts: [
      'Stack memory is allocated/freed automatically with call frames; Heap is manually managed via malloc/calloc/free.',
      'ptr + 1 advances the pointer address by sizeof(*ptr) bytes, not 1 single byte.',
      'void* is a generic raw pointer that must be type-cast before dereferencing.',
      'Always set pointers to NULL after freeing to prevent dangling pointer vulnerabilities.',
    ],
    formulas: ['Address(ptr + i) = Base_Address + i * sizeof(Type)'],
    rules: [
      'Never return the address of a local stack variable from a function.',
      'Every malloc/calloc call must have a corresponding free call to avoid memory leaks.',
    ],
    examples: [
      {
        title: 'Allocating a 2D Array via Double Pointer',
        example: `int **matrix = (int **)malloc(rows * sizeof(int *));\nfor(int i = 0; i < rows; i++) {\n    matrix[i] = (int *)malloc(cols * sizeof(int));\n}`,
        explanation: 'Allocates an array of row pointers, then allocates column memory for each row.',
      },
    ],
    importantPoints: ['Core subject for Operating Systems, Embedded Systems, and Core System Design.'],
    commonMistakes: [
      'Dereferencing uninitialized or NULL pointers (causes Segmentation Fault SIGSEGV).',
      'Freeing memory twice (Double Free error).',
    ],
    quickRevision: 'Pointers store addresses; Arithmetic scales with type size; Always free heap allocations; Set freed pointers to NULL.',
    pdfUrl: 'https://example.com/c-pointers-mastery.pdf',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    facultyName: 'Prof. Vikram Hegde',
    facultyDesignation: 'Associate Professor of Computer Engineering',
    facultyDepartment: 'Dept. of Information Science',
    collegeId: 'clg-bmsce',
    collegeName: 'B.M.S. College of Engineering (BMSCE)',
    isVerifiedFaculty: true,
    visibility: 'community',
    published: true,
    createdAt: '2026-08-16',
  },
  {
    id: 'fn-comm-dsa-trees',
    section: 'engineering',
    category: 'dsa',
    subject: 'Data Structures & Algorithms',
    topic: 'Binary Search Trees & Balancing',
    subtopic: 'AVL Rotations & Inorder Successor',
    language: 'python',
    title: 'DSA Tree Masterclass: BST Operations, Inorder Properties & AVL Self-Balancing',
    introduction: 'In-depth analysis of BST lookup guarantees, recursive/iterative traversals, deleting nodes with 2 children, and AVL tree height balance factors.',
    theory: 'A Binary Search Tree enforces the invariant: Left Subtree < Root <= Right Subtree. Inorder traversal of a BST yields keys in strictly ascending sorted order. AVL trees maintain balance factor in {-1, 0, 1} with O(log N) worst-case time.',
    importantConcepts: [
      'BST Search/Insert/Delete average time: O(log N); Skewed tree worst case: O(N).',
      'AVL Tree uses Left and Right rotations (LL, RR, LR, RL) to restore height balance in O(1) time per insert.',
      'Inorder Successor is the smallest node in the right subtree (or deepest ancestor whose left child is also an ancestor).',
    ],
    formulas: ['Balance_Factor(node) = Height(Left_Subtree) - Height(Right_Subtree)'],
    rules: [
      'When deleting a node with two children, replace with its Inorder Successor or Inorder Predecessor.',
      'Check balance factors bottom-up from insertion point to root.',
    ],
    examples: [
      {
        title: 'Finding Inorder Successor in BST',
        example: `def get_successor(root, node):\n    if node.right:\n        curr = node.right\n        while curr.left: curr = curr.left\n        return curr\n    succ = None\n    while root:\n        if node.val < root.val:\n            succ = root\n            root = root.left\n        elif node.val > root.val:\n            root = root.right\n        else: break\n    return succ`,
        explanation: 'O(H) search using BST ordering properties without parent pointers.',
      },
    ],
    importantPoints: ['Must-know topic for Google, Microsoft, and Amazon SDE interview rounds.'],
    commonMistakes: ['Assuming BST is balanced without explicit balancing mechanism (causes O(N) degradation).'],
    quickRevision: 'BST inorder = sorted order; AVL balance factor within {-1,0,+1}; Search/Insert/Delete O(log N).',
    pdfUrl: 'https://example.com/dsa-bst-avl-notes.pdf',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    facultyName: 'Dr. Arvind Menon',
    facultyDesignation: 'Professor of Algorithms & Data Systems',
    facultyDepartment: 'Dept. of Computer Science & Engineering',
    collegeId: 'clg-nits',
    collegeName: 'National Institute of Technology Karnataka (NIT Surathkal)',
    isVerifiedFaculty: true,
    visibility: 'community',
    published: true,
    createdAt: '2026-08-15',
  },
  {
    id: 'fn-comm-quant',
    section: 'competitive',
    category: 'aptitude',
    subject: 'Quantitative Aptitude',
    topic: 'Percentage & Profit/Loss',
    subtopic: 'Successive Percentage & Dishonest Dealer',
    title: 'Quantitative Aptitude: Short Tricks for Profit, Loss, Marked Price & Discount',
    introduction: 'Speed math and fraction conversion formulas for SBI PO, IBPS, SSC CGL, and campus placement aptitude rounds.',
    theory: 'Profit and Loss are strictly calculated on Cost Price (CP) unless stated otherwise. Discount is always computed on Marked Price (MP). Equivalent successive discount formula avoids lengthy calculations.',
    importantConcepts: [
      'Fraction shortcuts: 1/6 = 16.66%, 1/7 = 14.28%, 1/8 = 12.5%, 1/9 = 11.11%, 1/11 = 9.09%.',
      'Net Successive Percentage Change = a + b + (ab / 100).',
      'Dishonest dealer profit % = [ (True Weight - False Weight) / False Weight ] * 100.',
    ],
    formulas: [
      'SP = CP * (100 + Profit%) / 100',
      'Effective Discount = d1 + d2 - (d1 * d2 / 100)',
      'MP / CP = (100 + Profit%) / (100 - Discount%)',
    ],
    rules: [
      'If two items are sold at same SP, one at x% profit and other at x% loss, overall is always a loss of (x/10)^2 %.',
    ],
    examples: [
      {
        title: 'Two Successive Discounts Problem',
        example: 'Find single equivalent discount for 20% and 10% successive discounts:\nNet = 20 + 10 - (20 * 10 / 100) = 30 - 2 = 28%.',
        explanation: 'Applying the formula computes the answer in under 5 seconds.',
      },
    ],
    importantPoints: ['Core arithmetic chapter carrying 4-6 questions in all aptitude tests.'],
    commonMistakes: ['Calculating discount on CP instead of MP.'],
    quickRevision: 'Profit on CP; Discount on MP; Net successive = a + b + ab/100; Same SP profit/loss = always loss.',
    pdfUrl: 'https://example.com/quant-profit-loss-cheatsheet.pdf',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    facultyName: 'Prof. Rajesh Sharma',
    facultyDesignation: 'Head of Aptitude & Competitive Training',
    facultyDepartment: 'School of Mathematical Sciences',
    collegeId: 'clg-dit',
    collegeName: 'Delhi Institute of Technology',
    isVerifiedFaculty: true,
    visibility: 'community',
    published: true,
    createdAt: '2026-08-16',
  },
];

let facultyVideosList: FacultyVideo[] = [
  {
    id: 'fv-1',
    section: 'engineering',
    subject: 'Embedded Systems',
    topic: 'Microcontrollers',
    subtopic: 'GPIO Architecture',
    title: 'ARM Cortex-M GPIO & BSRR Register Explained in Detail',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    description: 'Comprehensive breakdown of atomic register manipulation and GPIO MODER configuration.',
    duration: '18 mins',
    facultyName: 'Dr. Kusumadhara S',
    facultyDesignation: 'Associate Professor',
    facultyDepartment: 'ECE Department',
    collegeId: 'clg-kvg',
    collegeName: 'KVG College of Engineering',
    isVerifiedFaculty: true,
    visibility: 'college',
    published: true,
    createdAt: '2026-08-15',
  },
  {
    id: 'fv-comm-python',
    section: 'engineering',
    category: 'programming',
    subject: 'Programming in Python',
    topic: 'Functions & Scope',
    subtopic: 'First-Class Functions & Decorators',
    language: 'python',
    title: 'Mastering Python Decorators & Higher-Order Functions with Live IDE Tracing',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    description: 'Step-by-step visual demonstration of Python stack frames, closure scope bindings, and practical timer/logger decorator implementations.',
    duration: '24 mins',
    facultyName: 'Dr. Sunita Rao',
    facultyDesignation: 'Professor & HOD CSE',
    facultyDepartment: 'Computer Science & Engineering',
    collegeId: 'clg-rvce',
    collegeName: 'R.V. College of Engineering (RVCE)',
    isVerifiedFaculty: true,
    visibility: 'community',
    published: true,
    createdAt: '2026-08-16',
  },
  {
    id: 'fv-comm-c-mem',
    section: 'engineering',
    category: 'programming',
    subject: 'Programming in C',
    topic: 'Pointers & Memory',
    subtopic: 'Memory Layout & Leaks',
    language: 'c',
    title: 'Visualizing C Virtual Memory: Heap, Stack, and Avoiding Dangling Pointers',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    description: 'Memory architecture lecture showing exact pointer address offsets, double pointers, and memory sanitization in C.',
    duration: '21 mins',
    facultyName: 'Prof. Vikram Hegde',
    facultyDesignation: 'Associate Professor',
    facultyDepartment: 'Information Science',
    collegeId: 'clg-bmsce',
    collegeName: 'B.M.S. College of Engineering (BMSCE)',
    isVerifiedFaculty: true,
    visibility: 'community',
    published: true,
    createdAt: '2026-08-16',
  },
  {
    id: 'fv-comm-dsa-trees',
    section: 'engineering',
    category: 'dsa',
    subject: 'Data Structures & Algorithms',
    topic: 'Binary Search Trees & Balancing',
    subtopic: 'AVL Rotations',
    language: 'python',
    title: 'AVL Tree Self-Balancing & Rotations Explained Step-by-Step with Code',
    videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    description: 'Clear animations of LL, RR, LR, and RL rotations to maintain log(N) height invariant in Binary Search Trees.',
    duration: '28 mins',
    facultyName: 'Dr. Arvind Menon',
    facultyDesignation: 'Professor of Algorithms',
    facultyDepartment: 'CSE Department',
    collegeId: 'clg-nits',
    collegeName: 'National Institute of Technology Karnataka (NIT Surathkal)',
    isVerifiedFaculty: true,
    visibility: 'community',
    published: true,
    createdAt: '2026-08-15',
  },
];

let facultyQuestionBank: QuestionMetadata[] = [
  {
    id: 'qb-1',
    section: 'engineering',
    category: 'subjects',
    subject: 'Embedded Systems',
    topic: 'Microcontrollers',
    subtopic: 'Registers',
    difficulty: 'medium',
    questionType: 'mcq',
    question: 'Which register in ARM Cortex-M microcontrollers enables atomic bit setting without read-modify-write?',
    options: ['ODR (Output Data Register)', 'BSRR (Bit Set/Reset Register)', 'IDR (Input Data Register)', 'MODER (Mode Register)'],
    correctAnswer: 1,
    explanation: 'BSRR allows atomic pin manipulation in a single clock cycle, eliminating race conditions.',
    marks: 2,
    negativeMarks: 0.5,
    isFacultyCreated: true,
    facultyName: 'Dr. Kusumadhara S',
  },
  {
    id: 'qb-comm-py1',
    section: 'engineering',
    category: 'programming',
    subject: 'Programming in Python',
    topic: 'Functions & Scope',
    subtopic: 'Closures',
    difficulty: 'medium',
    questionType: 'mcq',
    question: 'What is the output of the following Python closure snippet?\n\ndef outer(x):\n    def inner(y):\n        return x + y\n    return inner\n\nf = outer(10)\nprint(f(5))',
    options: ['15', '10', 'TypeError: missing argument', 'None'],
    correctAnswer: 0,
    explanation: 'The inner function forms a closure over x=10. Calling f(5) computes 10 + 5 = 15.',
    marks: 2,
    negativeMarks: 0.5,
    isFacultyCreated: true,
    facultyName: 'Dr. Sunita Rao (RVCE)',
  },
  {
    id: 'qb-comm-py2',
    section: 'engineering',
    category: 'programming',
    subject: 'Programming in Python',
    topic: 'Functions & Scope',
    subtopic: 'Default Arguments',
    difficulty: 'hard',
    questionType: 'mcq',
    question: 'What happens when a mutable object like a list is used as a default parameter value in Python (e.g. def fn(val, acc=[]))?',
    options: [
      'A new list is created on every function call',
      'The same list is reused across all invocations, causing state leakage',
      'Python throws a SyntaxError at compile time',
      'The list is automatically converted into an immutable tuple',
    ],
    correctAnswer: 1,
    explanation: 'In Python, default parameter expressions are evaluated once when the function is defined, sharing the mutable object across subsequent calls.',
    marks: 2,
    negativeMarks: 0.5,
    isFacultyCreated: true,
    facultyName: 'Dr. Sunita Rao (RVCE)',
  },
  {
    id: 'qb-comm-c1',
    section: 'engineering',
    category: 'programming',
    subject: 'Programming in C',
    topic: 'Pointers & Memory',
    subtopic: 'Pointer Arithmetic',
    difficulty: 'medium',
    questionType: 'mcq',
    question: 'If int *ptr = 0x1000 on a 32-bit architecture with sizeof(int) = 4, what is the value of (ptr + 3)?',
    options: ['0x1003', '0x100C (0x1000 + 12)', '0x1004', '0x1006'],
    correctAnswer: 1,
    explanation: 'Pointer arithmetic scales by sizeof(int) = 4 bytes. 0x1000 + (3 * 4) = 0x1000 + 12 (0xC in hex) = 0x100C.',
    marks: 2,
    negativeMarks: 0.5,
    isFacultyCreated: true,
    facultyName: 'Prof. Vikram Hegde (BMSCE)',
  },
  {
    id: 'qb-comm-dsa1',
    section: 'engineering',
    category: 'dsa',
    subject: 'Data Structures & Algorithms',
    topic: 'Binary Search Trees & Balancing',
    subtopic: 'Traversals',
    difficulty: 'medium',
    questionType: 'mcq',
    question: 'Which tree traversal on a valid Binary Search Tree always visits the node keys in non-decreasing (sorted) order?',
    options: ['Preorder (Root, Left, Right)', 'Inorder (Left, Root, Right)', 'Postorder (Left, Right, Root)', 'Level Order (BFS)'],
    correctAnswer: 1,
    explanation: 'Because all nodes in the left subtree are smaller and right subtree are larger, Inorder traversal strictly yields sorted keys.',
    marks: 2,
    negativeMarks: 0.5,
    isFacultyCreated: true,
    facultyName: 'Dr. Arvind Menon (NIT Surathkal)',
  },
  {
    id: 'qb-comm-quant1',
    section: 'competitive',
    category: 'aptitude',
    subject: 'Quantitative Aptitude',
    topic: 'Percentage & Profit/Loss',
    subtopic: 'Successive Discount',
    difficulty: 'medium',
    questionType: 'mcq',
    question: 'A shopkeeper offers two successive discounts of 20% and 15% on a shirt with Marked Price Rs. 1000. What is the final selling price?',
    options: ['Rs. 650', 'Rs. 680', 'Rs. 700', 'Rs. 720'],
    correctAnswer: 1,
    explanation: 'Single equivalent discount = 20 + 15 - (20 * 15 / 100) = 35 - 3 = 32%. Final SP = 1000 * (1 - 0.32) = Rs. 680.',
    marks: 2,
    negativeMarks: 0.5,
    isFacultyCreated: true,
    facultyName: 'Prof. Rajesh Sharma (DIT)',
  },
];

let facultyQuizzesList: FacultyQuiz[] = [
  {
    id: 'fq-1',
    section: 'engineering',
    subject: 'Embedded Systems',
    topic: 'Microcontrollers',
    quizName: 'ARM Cortex-M Architecture Assessment',
    description: '10-minute assessment on registers, NVIC interrupts, and bus protocols.',
    durationMinutes: 10,
    difficulty: 'medium',
    totalMarks: 10,
    negativeMarks: 0.5,
    passingScore: 6,
    questions: [
      facultyQuestionBank[0],
      {
        id: 'qb-3',
        section: 'engineering',
        category: 'subjects',
        subject: 'Embedded Systems',
        topic: 'Microcontrollers',
        subtopic: 'Interrupts',
        difficulty: 'medium',
        questionType: 'mcq',
        question: 'What is the function of the NVIC in ARM Cortex-M microcontrollers?',
        options: [
          'Nested Vectored Interrupt Controller for deterministic low-latency interrupt handling',
          'Network Virtual Interface Card for Wi-Fi',
          'Non-Volatile Instruction Cache',
          'Numerical Vector Instruction Compiler',
        ],
        correctAnswer: 0,
        explanation: 'NVIC manages hardware interrupt priorities, nesting, and tail-chaining.',
        marks: 2,
        negativeMarks: 0.5,
        isFacultyCreated: true,
        facultyName: 'Dr. Kusumadhara S',
      },
    ],
    published: true,
    assignedClasses: ['ECE Batch 2026', 'CSE Embedded Elective'],
    startDate: '2026-08-15',
    endDate: '2026-08-25',
    facultyName: 'Dr. Kusumadhara S',
    facultyDesignation: 'Associate Professor',
    facultyDepartment: 'ECE Department',
    collegeId: 'clg-kvg',
    collegeName: 'KVG College of Engineering',
    isVerifiedFaculty: true,
    visibility: 'college',
    createdAt: '2026-08-15',
  },
  {
    id: 'fq-comm-py',
    section: 'engineering',
    category: 'programming',
    subject: 'Programming in Python',
    topic: 'Functions & Scope',
    subtopic: 'Functions & Decorators Assessment',
    language: 'python',
    quizName: 'Python Functions, Closures & Decorators Speed Test',
    description: '5 challenging questions testing your mastery of Python first-class functions, LEGB scope, closures, and decorators.',
    durationMinutes: 12,
    difficulty: 'medium',
    totalMarks: 10,
    negativeMarks: 0.5,
    passingScore: 6,
    questions: [
      facultyQuestionBank[1],
      facultyQuestionBank[2],
      {
        id: 'qb-comm-py3',
        section: 'engineering',
        category: 'programming',
        subject: 'Programming in Python',
        topic: 'Functions & Scope',
        subtopic: 'Unpacking',
        difficulty: 'medium',
        questionType: 'mcq',
        question: 'What does the * operator do when placed before a parameter in a function definition like def func(*args)?',
        options: [
          'Packs any arbitrary number of positional arguments into a single tuple',
          'Packs named keyword arguments into a dictionary',
          'Declares a C-style memory pointer',
          'Multiplies all arguments before execution',
        ],
        correctAnswer: 0,
        explanation: '*args captures variable positional arguments as a tuple.',
        marks: 2,
        negativeMarks: 0.5,
        isFacultyCreated: true,
        facultyName: 'Dr. Sunita Rao',
      },
    ],
    published: true,
    facultyName: 'Dr. Sunita Rao',
    facultyDesignation: 'Professor & HOD CSE',
    facultyDepartment: 'Computer Science & Engineering',
    collegeId: 'clg-rvce',
    collegeName: 'R.V. College of Engineering (RVCE)',
    isVerifiedFaculty: true,
    visibility: 'community',
    createdAt: '2026-08-16',
  },
  {
    id: 'fq-comm-c-ptrs',
    section: 'engineering',
    category: 'programming',
    subject: 'Programming in C',
    topic: 'Pointers & Memory',
    subtopic: 'Memory Management Quiz',
    language: 'c',
    quizName: 'C Pointers & Memory Allocation Master Quiz',
    description: 'Assess your deep understanding of pointer arithmetic, heap allocation, and double pointers.',
    durationMinutes: 15,
    difficulty: 'hard',
    totalMarks: 10,
    negativeMarks: 0.5,
    passingScore: 6,
    questions: [
      facultyQuestionBank[3],
      {
        id: 'qb-comm-c2',
        section: 'engineering',
        category: 'programming',
        subject: 'Programming in C',
        topic: 'Pointers & Memory',
        subtopic: 'Double Pointers',
        difficulty: 'hard',
        questionType: 'mcq',
        question: 'Why is a double pointer (e.g. Node **head_ref) passed to a linked list insertion function like insert_at_head(Node **head_ref, int val)?',
        options: [
          'To modify the caller’s original head pointer address inside the function',
          'To double the speed of memory allocation',
          'Because C does not support single pointers in structs',
          'To automatically allocate heap memory for the node',
        ],
        correctAnswer: 0,
        explanation: 'Passing a double pointer allows the function to reassign the original pointer target across the call stack frame.',
        marks: 2,
        negativeMarks: 0.5,
        isFacultyCreated: true,
        facultyName: 'Prof. Vikram Hegde',
      },
    ],
    published: true,
    facultyName: 'Prof. Vikram Hegde',
    facultyDesignation: 'Associate Professor',
    facultyDepartment: 'Information Science',
    collegeId: 'clg-bmsce',
    collegeName: 'B.M.S. College of Engineering (BMSCE)',
    isVerifiedFaculty: true,
    visibility: 'community',
    createdAt: '2026-08-16',
  },
  {
    id: 'fq-comm-quant',
    section: 'competitive',
    category: 'aptitude',
    subject: 'Quantitative Aptitude',
    topic: 'Percentage & Profit/Loss',
    subtopic: 'Profit & Loss Quiz',
    quizName: 'Profit, Loss & Successive Discount Speed Test',
    description: 'Fast-paced aptitude test for competitive exams and campus placements.',
    durationMinutes: 10,
    difficulty: 'medium',
    totalMarks: 10,
    negativeMarks: 0.5,
    passingScore: 6,
    questions: [
      facultyQuestionBank[5],
      {
        id: 'qb-comm-quant2',
        section: 'competitive',
        category: 'aptitude',
        subject: 'Quantitative Aptitude',
        topic: 'Percentage & Profit/Loss',
        subtopic: 'Dishonest Dealer',
        difficulty: 'medium',
        questionType: 'mcq',
        question: 'A dishonest merchant professes to sell his goods at cost price but uses a 900g weight instead of 1kg. What is his profit percentage?',
        options: ['10%', '11.11%', '12.5%', '9.09%'],
        correctAnswer: 1,
        explanation: 'Profit% = [(1000 - 900) / 900] * 100 = 100/900 * 100 = 11.11%.',
        marks: 2,
        negativeMarks: 0.5,
        isFacultyCreated: true,
        facultyName: 'Prof. Rajesh Sharma',
      },
    ],
    published: true,
    facultyName: 'Prof. Rajesh Sharma',
    facultyDesignation: 'Head of Aptitude Training',
    facultyDepartment: 'School of Mathematical Sciences',
    collegeId: 'clg-dit',
    collegeName: 'Delhi Institute of Technology',
    isVerifiedFaculty: true,
    visibility: 'community',
    createdAt: '2026-08-16',
  },
];

let studentSubmissionsList: StudentQuizSubmission[] = [
  {
    id: 'sub-1',
    quizId: 'fq-1',
    quizTitle: 'ARM Cortex-M Architecture Assessment',
    studentId: 'std-101',
    studentName: 'Ganesh Sharan',
    subject: 'Embedded Systems',
    topic: 'Microcontrollers',
    score: 8,
    totalMarks: 10,
    accuracy: 80,
    correctAnswersCount: 4,
    wrongAnswersCount: 1,
    skippedCount: 0,
    timeSpent: '7 mins 42s',
    submittedAt: '2026-08-16 10:35',
  },
];

let facultyInterviewsList: FacultyInterview[] = [
  {
    id: 'int-1',
    studentId: 'std-101',
    studentName: 'Ganesh Sharan',
    interviewType: 'Engineering Viva',
    subjectOrRole: 'Embedded Systems & Microcontrollers',
    difficulty: 'medium',
    scheduledTime: 'Today, 2:30 PM',
    status: 'Scheduled',
    questions: [
      'Explain the difference between Harvard and Von Neumann architectures.',
      'How does the SysTick timer work in ARM Cortex-M?',
      'What is atomic bit setting and why is BSRR preferred over ODR?',
      'Describe the difference between polling and interrupt-driven I/O.',
    ],
    facultyName: 'Dr. Kusumadhara S',
    createdAt: '2026-08-15',
  },
];

let studentPerformancesList: StudentTopicPerformance[] = [
  {
    studentId: 'std-101',
    studentName: 'Ganesh Sharan',
    email: 'ganesh@kvgce.edu.in',
    overallScore: 88,
    quizzesCompletedCount: 5,
    quizAccuracy: 86,
    notesCompletedCount: 18,
    codingSolvedCount: 45,
    dsaProgressPct: 85,
    interviewsConductedCount: 2,
    interviewsScore: 90,
    topicMastery: [
      { section: 'engineering', subject: 'Embedded Systems', topic: 'Microcontrollers', percentage: 90 },
      { section: 'engineering', subject: 'Embedded Systems', topic: 'GPIO & Registers', percentage: 85 },
      { section: 'engineering', subject: 'Embedded Systems', topic: 'Interrupts & NVIC', percentage: 80 },
    ],
  },
  {
    studentId: 'std-102',
    studentName: 'Ananya Rao',
    email: 'ananya@kvgce.edu.in',
    overallScore: 82,
    quizzesCompletedCount: 4,
    quizAccuracy: 82,
    notesCompletedCount: 15,
    codingSolvedCount: 38,
    dsaProgressPct: 75,
    interviewsConductedCount: 1,
    interviewsScore: 84,
    topicMastery: [
      { section: 'engineering', subject: 'Embedded Systems', topic: 'Microcontrollers', percentage: 85 },
      { section: 'engineering', subject: 'Embedded Systems', topic: 'GPIO & Registers', percentage: 80 },
    ],
  },
  {
    studentId: 'std-103',
    studentName: 'Rahul Verma',
    email: 'rahul@kvgce.edu.in',
    overallScore: 76,
    quizzesCompletedCount: 3,
    quizAccuracy: 75,
    notesCompletedCount: 12,
    codingSolvedCount: 29,
    dsaProgressPct: 65,
    interviewsConductedCount: 1,
    interviewsScore: 78,
    topicMastery: [
      { section: 'engineering', subject: 'Embedded Systems', topic: 'Microcontrollers', percentage: 75 },
    ],
  },
];

type Listener = () => void;
const listeners: Set<Listener> = new Set();

function notify() {
  listeners.forEach((l) => l());
}

export const FacultySystemStore = {
  subscribe(listener: Listener) {
    listeners.add(listener);
    return () => {
      listeners.delete(listener);
    };
  },

  getStats() {
    return {
      totalStudents: studentPerformancesList.length,
      activeStudents: studentPerformancesList.length,
      notesPublished: facultyNotesList.filter((n) => n.published).length,
      quizzesCreated: facultyQuizzesList.length,
      interviewsConducted: facultyInterviewsList.filter((i) => i.status === 'Completed').length,
      pendingEvaluations: facultyInterviewsList.filter((i) => i.status === 'Pending Evaluation' || i.status === 'Scheduled').length,
      averageStudentScore: Math.round(
        studentPerformancesList.reduce((acc, s) => acc + s.overallScore, 0) / (studentPerformancesList.length || 1)
      ),
    };
  },

  // Notes
  getNotes(): FacultyNote[] {
    return [...facultyNotesList];
  },
  getNotesForTopic(topic: string): FacultyNote[] {
    return facultyNotesList.filter(
      (n) =>
        n.published &&
        (n.topic.toLowerCase().includes(topic.toLowerCase()) || topic.toLowerCase().includes(n.topic.toLowerCase()))
    );
  },
  addNote(note: Omit<FacultyNote, 'id' | 'createdAt'>): FacultyNote {
    const newNote: FacultyNote = {
      ...note,
      visibility: note.visibility || 'college',
      id: `fn-${Date.now()}-${Math.random().toString(36).substr(2, 4)}`,
      createdAt: new Date().toISOString().split('T')[0],
    };
    facultyNotesList.unshift(newNote);
    notify();
    return newNote;
  },
  updateNote(id: string, updates: Partial<FacultyNote>) {
    facultyNotesList = facultyNotesList.map((n) => (n.id === id ? { ...n, ...updates } : n));
    notify();
  },
  deleteNote(id: string) {
    facultyNotesList = facultyNotesList.filter((n) => n.id !== id);
    notify();
  },

  // Videos
  getVideos(): FacultyVideo[] {
    return [...facultyVideosList];
  },
  getVideosForTopic(topic: string): FacultyVideo[] {
    return facultyVideosList.filter(
      (v) =>
        v.published &&
        (v.topic.toLowerCase().includes(topic.toLowerCase()) || topic.toLowerCase().includes(v.topic.toLowerCase()))
    );
  },
  addVideo(video: Omit<FacultyVideo, 'id' | 'createdAt'>): FacultyVideo {
    const newV: FacultyVideo = {
      ...video,
      visibility: video.visibility || 'college',
      id: `fv-${Date.now()}-${Math.random().toString(36).substr(2, 4)}`,
      createdAt: new Date().toISOString().split('T')[0],
    };
    facultyVideosList.unshift(newV);
    notify();
    return newV;
  },
  deleteVideo(id: string) {
    facultyVideosList = facultyVideosList.filter((v) => v.id !== id);
    notify();
  },

  // Question Bank
  getQuestionBank(): QuestionMetadata[] {
    return [...facultyQuestionBank];
  },
  getQuestionsForTopic(subject: string, topic: string) {
    return facultyQuestionBank
      .filter(
        (q) =>
          q.topic.toLowerCase().includes(topic.toLowerCase()) ||
          topic.toLowerCase().includes(q.topic.toLowerCase()) ||
          q.subject.toLowerCase().includes(subject.toLowerCase())
      )
      .map((q) => ({
        id: q.id,
        question: q.question,
        options: q.options || [],
        correctIndex: typeof q.correctAnswer === 'number' ? q.correctAnswer : 0,
        explanation: q.explanation,
        facultyName: q.facultyName || 'Faculty Educator',
      }));
  },
  addQuestionToBank(q: Omit<QuestionMetadata, 'id'>): QuestionMetadata {
    const newQ: QuestionMetadata = {
      ...q,
      id: `qb-${Date.now()}-${Math.random().toString(36).substr(2, 4)}`,
      isFacultyCreated: true,
    };
    facultyQuestionBank.unshift(newQ);
    notify();
    return newQ;
  },
  deleteQuestionFromBank(id: string) {
    facultyQuestionBank = facultyQuestionBank.filter((q) => q.id !== id);
    notify();
  },

  // Quizzes
  getQuizzes(): FacultyQuiz[] {
    return [...facultyQuizzesList];
  },
  getQuizzesForTopic(topic: string): FacultyQuiz[] {
    return facultyQuizzesList.filter(
      (q) =>
        q.published &&
        (q.topic.toLowerCase().includes(topic.toLowerCase()) || topic.toLowerCase().includes(q.topic.toLowerCase()))
    );
  },
  addQuiz(quiz: Omit<FacultyQuiz, 'id' | 'createdAt'>): FacultyQuiz {
    const newQuiz: FacultyQuiz = {
      ...quiz,
      visibility: quiz.visibility || 'college',
      id: `fq-${Date.now()}-${Math.random().toString(36).substr(2, 4)}`,
      createdAt: new Date().toISOString().split('T')[0],
    };
    facultyQuizzesList.unshift(newQuiz);
    notify();
    return newQuiz;
  },
  deleteQuiz(id: string) {
    facultyQuizzesList = facultyQuizzesList.filter((q) => q.id !== id);
    notify();
  },

  // Submissions
  getSubmissions(): StudentQuizSubmission[] {
    return [...studentSubmissionsList];
  },
  recordSubmission(sub: Omit<StudentQuizSubmission, 'id' | 'submittedAt'>) {
    const newSub: StudentQuizSubmission = {
      ...sub,
      id: `sub-${Date.now()}`,
      submittedAt: new Date().toISOString().replace('T', ' ').substring(0, 16),
    };
    studentSubmissionsList.unshift(newSub);
    notify();
  },

  // Interviews
  getInterviews(): FacultyInterview[] {
    return [...facultyInterviewsList];
  },
  addInterview(interview: Omit<FacultyInterview, 'id' | 'createdAt'>): FacultyInterview {
    const newInt: FacultyInterview = {
      ...interview,
      id: `int-${Date.now()}`,
      createdAt: new Date().toISOString().split('T')[0],
    };
    facultyInterviewsList.unshift(newInt);
    notify();
    return newInt;
  },
  evaluateInterview(id: string, evaluation: Pick<FacultyInterview, 'scores' | 'feedback' | 'status'>) {
    facultyInterviewsList = facultyInterviewsList.map((i) => (i.id === id ? { ...i, ...evaluation } : i));
    notify();
  },

  // Student Performance
  getStudentPerformances(): StudentTopicPerformance[] {
    return [...studentPerformancesList];
  },
  getStudentById(id: string): StudentTopicPerformance | undefined {
    return studentPerformancesList.find((s) => s.studentId === id);
  },

  // 🌍 SKILLEXA COMMUNITY CONTENT ENGINE
  getCommunityContent(filter?: CommunityFilterOptions): CommunityContentItem[] {
    const communityItems: CommunityContentItem[] = [];

    // 1. Convert Published Community Notes
    facultyNotesList
      .filter((n) => n.published && n.visibility === 'community')
      .forEach((n) => {
        communityItems.push({
          id: `comm-note-${n.id}`,
          type: n.pdfUrl ? 'pdf' : 'note',
          title: n.title,
          facultyName: n.facultyName,
          facultyDesignation: n.facultyDesignation || 'Verified Educator',
          collegeName: n.collegeName || 'SkillExa Partner University',
          collegeId: n.collegeId,
          isVerified: n.isVerifiedFaculty ?? true,
          section: n.section,
          category: n.category || (n.section === 'engineering' ? 'subjects' : 'english'),
          subject: n.subject,
          topic: n.topic,
          subtopic: n.subtopic,
          language: n.language,
          publishedDate: n.createdAt,
          summary: n.introduction || n.theory.substring(0, 120),
          viewsCount: 340 + Math.floor(n.title.length * 12),
          rating: 4.9,
          targetParams: {
            section: n.section,
            subject: n.subject,
            topic: n.topic,
            subtopic: n.subtopic,
            language: n.language,
            noteId: n.id,
          },
        });
      });

    // 2. Convert Published Community Quizzes
    facultyQuizzesList
      .filter((q) => q.published && q.visibility === 'community')
      .forEach((q) => {
        communityItems.push({
          id: `comm-quiz-${q.id}`,
          type: 'quiz',
          title: q.quizName,
          facultyName: q.facultyName,
          facultyDesignation: q.facultyDesignation || 'Assessment Specialist',
          collegeName: q.collegeName || 'SkillExa Partner University',
          collegeId: q.collegeId,
          isVerified: q.isVerifiedFaculty ?? true,
          section: q.section,
          category: q.category || (q.section === 'engineering' ? 'subjects' : 'aptitude'),
          subject: q.subject,
          topic: q.topic,
          subtopic: q.subtopic,
          language: q.language,
          publishedDate: q.createdAt,
          summary: q.description,
          duration: `${q.durationMinutes} mins`,
          questionsCount: q.questions.length,
          viewsCount: 520 + Math.floor(q.quizName.length * 15),
          rating: 4.8,
          targetParams: {
            section: q.section,
            subject: q.subject,
            topic: q.topic,
            subtopic: q.subtopic,
            language: q.language,
            quizId: q.id,
          },
        });
      });

    // 3. Convert Published Community Videos
    facultyVideosList
      .filter((v) => v.published && v.visibility === 'community')
      .forEach((v) => {
        communityItems.push({
          id: `comm-video-${v.id}`,
          type: 'video',
          title: v.title,
          facultyName: v.facultyName,
          facultyDesignation: v.facultyDesignation || 'Lecturer',
          collegeName: v.collegeName || 'SkillExa Partner University',
          collegeId: v.collegeId,
          isVerified: v.isVerifiedFaculty ?? true,
          section: v.section,
          category: v.category || (v.section === 'engineering' ? 'subjects' : 'english'),
          subject: v.subject,
          topic: v.topic,
          subtopic: v.subtopic,
          language: v.language,
          publishedDate: v.createdAt,
          summary: v.description,
          duration: v.duration || '20 mins',
          viewsCount: 890 + Math.floor(v.title.length * 18),
          rating: 5.0,
          targetParams: {
            section: v.section,
            subject: v.subject,
            topic: v.topic,
            subtopic: v.subtopic,
            language: v.language,
            videoId: v.id,
          },
        });
      });

    // Filter Logic
    if (!filter) return communityItems;

    return communityItems.filter((item) => {
      // 1. Search Query
      if (filter.searchQuery && filter.searchQuery.trim()) {
        const q = filter.searchQuery.toLowerCase().trim();
        const matchesTitle = item.title.toLowerCase().includes(q);
        const matchesSubject = item.subject.toLowerCase().includes(q);
        const matchesTopic = item.topic.toLowerCase().includes(q);
        const matchesFaculty = item.facultyName.toLowerCase().includes(q);
        const matchesCollege = item.collegeName.toLowerCase().includes(q);
        if (!matchesTitle && !matchesSubject && !matchesTopic && !matchesFaculty && !matchesCollege) {
          return false;
        }
      }

      // 2. Category Filter
      if (filter.category && filter.category !== 'all') {
        if (filter.category === 'engineering' && item.section !== 'engineering') return false;
        if (filter.category === 'competitive' && item.section !== 'competitive') return false;
        if (filter.category === 'programming' && item.category !== 'programming') return false;
        if (filter.category === 'dsa' && item.category !== 'dsa') return false;
      }

      // 3. Content Type Filter
      if (filter.contentType && filter.contentType !== 'all') {
        if (filter.contentType === 'notes' && item.type !== 'note') return false;
        if (filter.contentType === 'pdf' && item.type !== 'pdf') return false;
        if (filter.contentType === 'quiz' && item.type !== 'quiz') return false;
        if (filter.contentType === 'video' && item.type !== 'video') return false;
        if (filter.contentType === 'coding' && item.type !== 'coding') return false;
      }

      // 4. Subject Filter
      if (filter.subject && filter.subject !== 'all') {
        if (!item.subject.toLowerCase().includes(filter.subject.toLowerCase())) return false;
      }

      // 5. Topic Filter
      if (filter.topic && filter.topic !== 'all') {
        if (!item.topic.toLowerCase().includes(filter.topic.toLowerCase())) return false;
      }

      // 6. Language Filter
      if (filter.language && filter.language !== 'all') {
        if (item.language !== filter.language) return false;
      }

      return true;
    });
  },
};

export const FacultyStore = FacultySystemStore;
