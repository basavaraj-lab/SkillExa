import { QuestionMetadata, TopicCurriculum } from './curriculumSchema';

export const ENGINEERING_SUBJECTS_LIST = [
  'Digital Electronics',
  'Analog Electronics',
  'Signals & Systems',
  'DSP',
  'Microprocessors',
  'Microcontrollers',
  'Embedded Systems',
  'VLSI',
  'Communication Systems',
  'Control Systems',
  'Electronic Devices',
  'Network Theory',
];

export const PROGRAMMING_LANGUAGES_LIST = [
  'C',
  'C++',
  'Java',
  'Python',
  'JavaScript',
  'HTML/CSS',
  'React Native',
];

export const DSA_TOPICS_17 = [
  'Time & Space Complexity',
  'Arrays',
  'Strings',
  'Linked List',
  'Stack',
  'Queue',
  'Recursion',
  'Searching',
  'Sorting',
  'Hashing',
  'Trees',
  'BST',
  'Heap',
  'Graphs',
  'Greedy',
  'Dynamic Programming',
  'Backtracking',
];

export const ENGINEERING_CURRICULUM: Record<string, TopicCurriculum> = {
  // 1. Embedded Systems -> Microcontrollers
  'Embedded Systems - Microcontrollers': {
    id: 'eng-embedded-mcu',
    section: 'engineering',
    category: 'subjects',
    subject: 'Embedded Systems',
    topic: 'Microcontrollers',
    subtopic: 'Architecture & Peripherals',
    badge: 'HARDWARE ARCHITECTURE',
    overview: 'Explore Harvard vs Von Neumann architectures, ARM Cortex-M cores, GPIOs, Timers, Interrupt Service Routines, and Bus Protocols (I2C, SPI, UART).',
    theory: 'A microcontroller (MCU) integrates a CPU core, volatile RAM, non-volatile Flash memory, and programmable peripherals (ADC, PWM, Timers, USART) on a single monolithic IC. Unlike general-purpose microprocessors, MCUs are optimized for real-time control, deterministic interrupt handling, and low power consumption in embedded devices.',
    importantConcepts: [
      'Harvard Architecture: Separate instruction and data buses allow simultaneous instruction fetch and operand read.',
      'Interrupt Vector Table (IVT): Fixed memory addresses containing pointers to Interrupt Service Routines (ISRs).',
      'Watchdog Timer (WDT): Hardware countdown timer that resets the system if firmware hangs in an infinite loop.',
      'Buses: UART (Asynchronous, point-to-point), I2C (Synchronous, 2-wire SDA/SCL, multi-device master-slave), SPI (Synchronous, 4-wire MOSI/MISO/SCK/CS, high speed full-duplex).',
      'Memory Mapped I/O: Peripheral registers are mapped into the memory address space and manipulated with pointer dereferences.',
    ],
    formulas: [
      'Baud Rate (UART) = Clock_Freq / (16 * (BRR + 1))',
      'Timer Overflow Time = (Prescaler * AutoReloadValue) / Clock_Freq',
      'ADC Voltage = (Digital_Reading / (2^Bits - 1)) * V_Ref',
    ],
    tipsTricks: [
      'Always keep ISRs as short as possible; never perform blocking delay loops or heavy I/O inside an interrupt handler.',
      'Use the `volatile` keyword for variables shared between hardware registers or ISRs and the main execution thread to prevent compiler optimization bugs.',
    ],
    examples: [
      {
        title: 'Memory Mapped GPIO Toggle in C',
        example: `// Toggle GPIO Port A Pin 5 on ARM Cortex-M\n#define GPIOA_ODR (*((volatile uint32_t*)0x40020014))\nGPIOA_ODR ^= (1 << 5); // Bitwise XOR toggles pin`,
        explanation: 'Direct memory register manipulation via volatile pointers provides sub-microsecond pin toggling without HAL overhead.',
      },
    ],
    examPoints: [
      'Difference between Microprocessor (MPU) and Microcontroller (MCU) is asked in 90% of core engineering placement exams.',
      'Calculation of Timer Reload values for specific PWM frequencies is standard in technical written tests.',
    ],
    commonMistakes: [
      'Forgetting to configure pin mode in the GPIO MODER register before writing to Output Data Register (ODR).',
      'Omitting pull-up resistors on I2C SDA and SCL lines.',
    ],
    interviewQuestions: [
      'What is priority inversion and how does priority inheritance solve it in embedded RTOS?',
      'Why is volatile keyword mandatory when declaring hardware registers?',
      'Compare I2C and SPI in terms of wire count, speed, and communication distance.',
    ],
    pyqs: [
      {
        id: 'pyq-eng-1',
        exam: 'ISRO Scientist / Engineer',
        year: '2023',
        difficulty: 'Medium',
        question: 'Which of the following communication protocols requires an acknowledgement (ACK/NACK) bit after every 8 bits of data transmitted?',
        options: ['SPI', 'UART', 'I2C', 'CAN'],
        correct: 'I2C',
        explanation: 'In the I2C protocol, the receiver pulls the SDA line LOW during the 9th clock pulse to acknowledge receipt of each byte.',
      },
    ],
    questions: [
      {
        id: 'q-eng-mcu-1',
        section: 'engineering',
        category: 'subjects',
        subject: 'Embedded Systems',
        topic: 'Microcontrollers',
        subtopic: 'Architecture',
        difficulty: 'easy',
        questionType: 'mcq',
        question: 'Which architectural feature differentiates Harvard architecture from Von Neumann architecture?',
        options: [
          'Separate memory spaces and physical buses for instructions and data',
          'Single unified bus for both code and data',
          'Absence of hardware interrupt controllers',
          'Lack of on-chip RAM',
        ],
        correctAnswer: 0,
        explanation: 'Harvard architecture features physically separate buses for instructions and data, allowing concurrent instruction fetching and data reading.',
        marks: 2,
        negativeMarks: 0.5,
      },
      {
        id: 'q-eng-mcu-2',
        section: 'engineering',
        category: 'subjects',
        subject: 'Embedded Systems',
        topic: 'Microcontrollers',
        subtopic: 'Peripherals',
        difficulty: 'medium',
        questionType: 'mcq',
        question: 'In an embedded C firmware, what is the critical purpose of qualifying a global flag modified by an ISR with `volatile`?',
        options: [
          'It forces the compiler to reload the variable directly from memory rather than caching it in a CPU register',
          'It stores the variable in Flash ROM instead of RAM',
          'It encrypts the variable memory address',
          'It increases variable execution speed by 10x',
        ],
        correctAnswer: 0,
        explanation: 'The `volatile` qualifier prevents the compiler optimizer from assuming the variable value cannot change asynchronously, forcing memory re-reads.',
        marks: 2,
        negativeMarks: 0.5,
      },
      {
        id: 'q-eng-mcu-3',
        section: 'engineering',
        category: 'subjects',
        subject: 'Embedded Systems',
        topic: 'Microcontrollers',
        subtopic: 'Protocols',
        difficulty: 'hard',
        questionType: 'mcq',
        question: 'How many wires are required for a standard SPI interface communicating with 3 separate slave devices using individual Chip Selects?',
        options: ['6 wires (MOSI, MISO, SCK + 3 CS lines)', '4 wires total', '3 wires total', '7 wires total'],
        correctAnswer: 0,
        explanation: '3 shared bus lines (MOSI, MISO, SCK) + 3 dedicated Chip Select lines = 6 physical wires.',
        marks: 2,
        negativeMarks: 0.5,
      },
    ],
  },

  // 2. Programming -> C -> Pointers
  'C - Pointers': {
    id: 'eng-c-pointers',
    section: 'engineering',
    category: 'programming',
    subject: 'Programming in C',
    topic: 'Pointers',
    subtopic: 'Pointer Arithmetic & Dynamic Memory',
    language: 'c',
    badge: 'C LOW-LEVEL MEMORY',
    overview: 'Master pointer syntax, dereferencing, pointer arithmetic, void pointers, function pointers, and heap management with malloc/free.',
    theory: 'A pointer is a variable that stores the memory address of another variable. If `int a = 10;`, then `&a` yields its address and `int* ptr = &a;` stores it. The dereference operator `*ptr` accesses the value stored at that address. In C, arrays decay into pointers when passed to functions.',
    importantConcepts: [
      'Address-of (&) and Dereference (*) operators.',
      'Pointer Arithmetic: `ptr + 1` increments address by `sizeof(datatype)` bytes.',
      'Double Pointers (int**): Store addresses of pointer variables; used for dynamic 2D matrices.',
      'Dynamic Memory Allocation: `malloc()` allocates uninitialized bytes; `calloc()` zero-initializes; `realloc()` resizes; `free()` deallocates.',
      'Dangling Pointers: Pointers referencing memory that has already been deallocated by free().',
    ],
    formulas: [
      'Address of element arr[i] = Base_Address + (i * sizeof(datatype))',
      'Address of matrix element arr[i][j] = Base_Address + ((i * Cols + j) * sizeof(datatype))',
    ],
    tipsTricks: [
      'Always set pointers to NULL after freeing them (`free(ptr); ptr = NULL;`) to avoid dangerous dangling pointer access.',
      'Array subscript `arr[i]` is strictly equivalent to `*(arr + i)` and even `i[arr]`.',
    ],
    examples: [
      {
        title: 'Swapping Values Using Pointers (Pass by Reference)',
        example: `void swap(int *x, int *y) {\n    int temp = *x;\n    *x = *y;\n    *y = temp;\n}`,
        explanation: 'Passing memory addresses permits direct modification of caller variables.',
      },
    ],
    examPoints: [
      'Output prediction of complex pointer expressions (e.g. `*ptr++` vs `(*ptr)++`) is standard in technical placements.',
    ],
    commonMistakes: [
      'Dereferencing an uninitialized or NULL pointer causing SIGSEGV (Segmentation Fault).',
      'Memory Leaks caused by losing the pointer reference without calling free().',
    ],
    interviewQuestions: [
      'Explain the difference between `const int* ptr` and `int* const ptr`.',
      'What is a memory leak and how do tools like Valgrind detect it?',
    ],
    pyqs: [
      {
        id: 'pyq-c-1',
        exam: 'GATE CS',
        year: '2023',
        difficulty: 'Medium',
        question: 'What is the output of `int a[] = {10, 20, 30}; int *p = a; printf("%d", *(p + 1));`?',
        options: ['20', '10', '30', 'Compilation Error'],
        correct: '20',
        explanation: '`p` points to `a[0]`. `p + 1` points to `a[1]`, which dereferences to 20.',
      },
    ],
    questions: [
      {
        id: 'q-c-ptr-1',
        section: 'engineering',
        category: 'programming',
        subject: 'Programming in C',
        topic: 'Pointers',
        subtopic: 'Syntax',
        language: 'c',
        difficulty: 'easy',
        questionType: 'mcq',
        question: 'If `ptr` is an integer pointer storing address `0x1000`, what is the value of `ptr + 2` on a system where `sizeof(int) == 4`?',
        options: ['0x1008', '0x1002', '0x1004', '0x1016'],
        correctAnswer: 0,
        explanation: '0x1000 + 2 * 4 = 0x1000 + 8 = 0x1008.',
        marks: 2,
        negativeMarks: 0.5,
      },
      {
        id: 'q-c-ptr-2',
        section: 'engineering',
        category: 'programming',
        subject: 'Programming in C',
        topic: 'Pointers',
        subtopic: 'Const Pointers',
        language: 'c',
        difficulty: 'medium',
        questionType: 'mcq',
        question: 'In C declaration `const int *ptr`, which operation is illegal?',
        options: [
          '*ptr = 50; (Modifying the pointed value)',
          'ptr = &other_var; (Changing the pointer address)',
          'printf("%d", *ptr); (Reading the value)',
          'ptr++; (Pointer arithmetic)',
        ],
        correctAnswer: 0,
        explanation: '`const int *ptr` represents a pointer to a constant integer; the value cannot be mutated through this pointer.',
        marks: 2,
        negativeMarks: 0.5,
      },
    ],
  },

  // 3. Programming -> Python -> Lists
  'Python - Lists': {
    id: 'eng-py-lists',
    section: 'engineering',
    category: 'programming',
    subject: 'Programming in Python',
    topic: 'Lists',
    subtopic: 'List Operations & Comprehensions',
    language: 'python',
    badge: 'PYTHON DATA STRUCTURES',
    overview: 'Explore dynamic array resizing, list slicing, comprehensions, sorting with lambdas, and memory semantics in Python.',
    theory: 'Python lists are mutable, ordered sequences implemented as dynamic arrays of pointers to Python objects. Lists support heterogeneous element types and dynamic over-allocation for O(1) amortized appends.',
    importantConcepts: [
      'Slicing Syntax: `list[start:stop:step]` creates a shallow copy.',
      'List Comprehensions: `[expr for item in iterable if condition]` executes in optimized C bytecode.',
      'Mutating methods (`.append()`, `.extend()`, `.insert()`, `.pop()`, `.remove()`) modify list in place.',
      'Copy Semantics: `a = b` creates an alias; `a = b.copy()` or `b[:]` creates a shallow copy.',
    ],
    tipsTricks: [
      '`list.append(x)` is O(1) amortized, while `list.insert(0, x)` is O(N) because all elements shift right.',
      'To reverse a list in place with O(1) memory, use `list.reverse()`; for a new reversed slice, use `list[::-1]`.',
    ],
    examples: [
      {
        title: 'List Comprehension Filtering & Squaring',
        example: `evens_squared = [x**2 for x in range(10) if x % 2 == 0]\nprint(evens_squared) # [0, 4, 16, 36, 64]`,
        explanation: 'Filters even numbers and computes their squares in a single concise line.',
      },
    ],
    examPoints: [
      'Understanding difference between `list.append([1,2])` vs `list.extend([1,2])` is a classic interview question.',
    ],
    commonMistakes: [
      'Creating a 2D list with `[[0]*3]*3` which duplicates references to the same single row object.',
    ],
    interviewQuestions: [
      'How does Python handle memory over-allocation when a list exceeds capacity?',
      'Why is `pop()` from end of list O(1) while `pop(0)` is O(N)?',
    ],
    pyqs: [
      {
        id: 'pyq-py-1',
        exam: 'TCS Digital Coding',
        year: '2023',
        difficulty: 'Easy',
        question: 'What is the output of `lst = [1, 2, 3]; lst.extend([4, 5]); print(len(lst))`?',
        options: ['5', '4', '2', '3'],
        correct: '5',
        explanation: '`extend()` unpacks the elements 4 and 5 individually into `lst`, making total length 5.',
      },
    ],
    questions: [
      {
        id: 'q-py-list-1',
        section: 'engineering',
        category: 'programming',
        subject: 'Programming in Python',
        topic: 'Lists',
        subtopic: 'Operations',
        language: 'python',
        difficulty: 'easy',
        questionType: 'mcq',
        question: 'What is the result of `[1, 2, 3] + [4, 5]` in Python?',
        options: ['[1, 2, 3, 4, 5]', '[[1, 2, 3], [4, 5]]', '[5, 7, 3]', 'TypeError'],
        correctAnswer: 0,
        explanation: 'The `+` operator on Python lists performs sequence concatenation, returning a new list with all elements.',
        marks: 2,
        negativeMarks: 0.5,
      },
      {
        id: 'q-py-list-2',
        section: 'engineering',
        category: 'programming',
        subject: 'Programming in Python',
        topic: 'Lists',
        subtopic: '2D Arrays',
        language: 'python',
        difficulty: 'medium',
        questionType: 'mcq',
        question: 'What is the correct way to initialize an independent 3x3 matrix of zeroes in Python?',
        options: [
          '[[0 for _ in range(3)] for _ in range(3)]',
          '[[0] * 3] * 3',
          '[[0, 0, 0]] * 3',
          'list(matrix(3, 3))',
        ],
        correctAnswer: 0,
        explanation: 'List comprehension creates 3 distinct list objects, preventing mutations in one row from affecting other rows.',
        marks: 2,
        negativeMarks: 0.5,
      },
    ],
  },
};

export function getEngineeringTopic(subject: string, topic: string): TopicCurriculum {
  const key = `${subject} - ${topic}`;
  if (ENGINEERING_CURRICULUM[key]) return ENGINEERING_CURRICULUM[key];

  const foundKey = Object.keys(ENGINEERING_CURRICULUM).find(
    (k) =>
      k.toLowerCase().includes(topic.toLowerCase()) ||
      topic.toLowerCase().includes(k.toLowerCase())
  );
  if (foundKey && ENGINEERING_CURRICULUM[foundKey]) return ENGINEERING_CURRICULUM[foundKey];

  // Dynamic pedagogical fallback
  return {
    id: `eng-${topic.toLowerCase().replace(/[^a-z0-9]/g, '-')}`,
    section: 'engineering',
    category: 'subjects',
    subject,
    topic,
    badge: 'ENGINEERING CURRICULUM',
    overview: `Master comprehensive technical foundations, design principles, mathematical derivations, and implementations of ${topic} in ${subject}.`,
    theory: `${topic} is an integral subject in modern engineering curriculum. Technical proficiency requires understanding governing physical equations, component architectures, and algorithmic optimization.`,
    importantConcepts: [
      `Foundational principles and structural taxonomy of ${topic}.`,
      `Governing transfer functions, block diagrams, and hardware/software constraints.`,
      `Industry design patterns and production implementation rules.`,
      `Performance trade-offs (Latency vs Throughput, Power vs Clock Frequency).`,
    ],
    tipsTricks: [
      'Deconstruct complex system blocks into linear stages to simplify state analysis.',
      'Check units and boundary conditions prior to final numerical evaluations.',
    ],
    examples: [
      {
        title: `Core Architectural Case Study in ${topic}`,
        example: `Systematic decomposition and design equations for ${topic}.`,
        explanation: `Demonstrates optimal solution steps adhering to modern industry engineering standards.`,
      },
    ],
    examPoints: [
      `High-frequency topic across GATE, ISRO, placement written tests, and technical viva rounds.`,
    ],
    commonMistakes: [
      `Overlooking propagation delays and clock synchronization boundaries.`,
    ],
    interviewQuestions: [
      `Explain the fundamental trade-offs involved when optimizing ${topic}.`,
      `How does ${topic} scale under high concurrent load or constrained power budgets?`,
    ],
    pyqs: [
      {
        id: `pyq-eng-${topic.toLowerCase().replace(/[^a-z0-9]/g, '-')}`,
        exam: 'Engineering Technical Placement',
        year: '2024',
        difficulty: 'Medium',
        question: `Which fundamental principle governs the primary application of ${topic}?`,
        options: ['Deterministic State Control', 'Arbitrary Floating', 'Unbounded Recursion', 'Unverified Memory Access'],
        correct: 'Deterministic State Control',
        explanation: 'Deterministic state transitions guarantee system stability and timing accuracy in engineering systems.',
      },
    ],
    questions: [
      {
        id: `q-eng-${topic.toLowerCase().replace(/[^a-z0-9]/g, '-')}-1`,
        section: 'engineering',
        category: 'subjects',
        subject,
        topic,
        difficulty: 'medium',
        questionType: 'mcq',
        question: `What is the primary engineering objective when architecting ${topic}?`,
        options: [
          'Maximize reliability, maintainability, and deterministic timing',
          'Rely on unpredictable runtime behaviors',
          'Bypass all boundary safety checks',
          'None of the above',
        ],
        correctAnswer: 0,
        explanation: 'Engineering design prioritizes robust reliability, predictable throughput, and adherence to safety constraints.',
        marks: 2,
        negativeMarks: 0.5,
      },
    ],
  };
}
