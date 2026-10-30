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

// Initial Faculty Notes Data - contains verified uploaded CSS Notes
let facultyNotesList: FacultyNote[] = [
  {
    id: 'cb3129be-48a8-44b4-9f50-6e50f0e9ecd7',
    section: 'engineering',
    category: 'subjects',
    subject: 'Embedded Systems',
    topic: 'CSS Notes',
    title: 'CSS Notes',
    description: 'css notes',
    introduction: 'css notes',
    theory: 'css notes',
    fileName: 'CSS_Notes.pdf',
    fileSize: 3238025,
    downloadUrl: '/api/notes/cb3129be-48a8-44b4-9f50-6e50f0e9ecd7/download',
    pdfUrl: '/api/notes/cb3129be-48a8-44b4-9f50-6e50f0e9ecd7/download',
    importantConcepts: [],
    formulas: [],
    examples: [],
    importantPoints: ['Verified Faculty Study Material'],
    commonMistakes: [],
    quickRevision: 'css notes',
    facultyName: 'Dr. Ramesh Kumar',
    facultyDesignation: 'Associate Professor & HOD',
    facultyDepartment: 'ECE Department',
    collegeId: '0f669a91-5c8d-4304-a815-818bde05e996',
    collegeName: 'KVG College of Engineering',
    isVerifiedFaculty: true,
    visibility: 'college',
    published: true,
    createdAt: '2026-10-30',
  },
];

let facultyVideosList: FacultyVideo[] = [];

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
    studentId: 'bb296f4d-31ea-4fb6-b155-c1b11d44f234',
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
    studentId: '0b084f31-31a9-4d5d-b8a9-fbbd2f272b79',
    studentName: 'Basavaraju R K',
    email: 'basavarajurk49@gmail.com',
    overallScore: 92,
    quizzesCompletedCount: 6,
    quizAccuracy: 91,
    notesCompletedCount: 22,
    codingSolvedCount: 54,
    dsaProgressPct: 89,
    interviewsConductedCount: 2,
    interviewsScore: 94,
    topicMastery: [
      { section: 'engineering', subject: 'Embedded Systems', topic: 'Microcontrollers', percentage: 94 },
      { section: 'engineering', subject: 'Embedded Systems', topic: 'GPIO & Registers', percentage: 90 },
      { section: 'engineering', subject: 'Embedded Systems', topic: 'Interrupts & NVIC', percentage: 88 },
    ],
  },
  {
    studentId: '6eb4f020-5d7f-4949-8f79-824e3265a71f',
    studentName: 'Sathysaimedu',
    email: 'sathysaimedu@gmail.com',
    overallScore: 84,
    quizzesCompletedCount: 4,
    quizAccuracy: 82,
    notesCompletedCount: 16,
    codingSolvedCount: 38,
    dsaProgressPct: 78,
    interviewsConductedCount: 1,
    interviewsScore: 85,
    topicMastery: [
      { section: 'engineering', subject: 'Embedded Systems', topic: 'Microcontrollers', percentage: 85 },
      { section: 'engineering', subject: 'Embedded Systems', topic: 'GPIO & Registers', percentage: 82 },
      { section: 'engineering', subject: 'Embedded Systems', topic: 'Interrupts & NVIC', percentage: 79 },
    ],
  },
  {
    studentId: '46ade83d-d095-4bdf-8b15-66991945cb08',
    studentName: 'Student Scholar',
    email: 'student@skillexa.edu',
    overallScore: 80,
    quizzesCompletedCount: 3,
    quizAccuracy: 78,
    notesCompletedCount: 14,
    codingSolvedCount: 32,
    dsaProgressPct: 72,
    interviewsConductedCount: 1,
    interviewsScore: 80,
    topicMastery: [
      { section: 'engineering', subject: 'Embedded Systems', topic: 'Microcontrollers', percentage: 82 },
      { section: 'engineering', subject: 'Embedded Systems', topic: 'GPIO & Registers', percentage: 78 },
      { section: 'engineering', subject: 'Embedded Systems', topic: 'Interrupts & NVIC', percentage: 75 },
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
  setNotes(notes: FacultyNote[]) {
    facultyNotesList = [...notes];
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
  setStudentPerformances(list: StudentTopicPerformance[]) {
    studentPerformancesList = [...list];
    notify();
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
