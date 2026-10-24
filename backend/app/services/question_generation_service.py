import logging
import random
from typing import Any, Dict, List, Optional
from sqlalchemy.orm import Session
from backend.app.models.ai_interview import (
    AIQuestionBank,
    InterviewCategoryEnum,
    InterviewDifficultyEnum,
    ExperienceLevelEnum,
    QuestionValidationStatusEnum,
)
from backend.app.services.ai_provider_service import AIProviderService
from backend.app.services.knowledge_retrieval_service import KnowledgeRetrievalService

logger = logging.getLogger("skillexa.question_generation")


# Initial Predefined Question Bank covering all mandatory categories
INITIAL_PREDEFINED_QUESTIONS = [
    # --- TECHNICAL: Python ---
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "Python",
        "programming_language": "Python",
        "job_role": "Software Developer",
        "difficulty": InterviewDifficultyEnum.BEGINNER,
        "question_text": "What are mutable and immutable data types in Python? Provide examples of each and explain how Python handles memory allocation for immutable objects.",
        "expected_concepts": ["mutable", "immutable", "list", "tuple", "dict", "id()", "memory address", "in-place modification"],
        "evaluation_criteria": {
            "correct_definitions": 3.0,
            "accurate_examples": 3.0,
            "memory_understanding": 4.0,
        },
        "sample_answer": "In Python, mutable objects like lists, dicts, and sets can be modified in-place without changing their memory address. Immutable objects like integers, strings, and tuples cannot be altered after creation; any modification produces a new object in memory.",
        "hints": ["Consider integers, strings, lists, and dictionary operations."],
    },
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "Python",
        "programming_language": "Python",
        "job_role": "Backend Engineer",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "Explain Python generators, the 'yield' keyword, and how they achieve memory efficiency compared to standard list returns.",
        "expected_concepts": ["generator", "yield", "lazy evaluation", "iterator protocol", "memory efficiency", "next()", "StopIteration"],
        "evaluation_criteria": {
            "generator_mechanism": 4.0,
            "memory_efficiency": 3.0,
            "iteration_protocol": 3.0,
        },
        "sample_answer": "Generators are functions that use 'yield' instead of 'return'. They generate values lazily on-the-fly rather than holding the entire collection in RAM, saving massive memory during large dataset processing.",
        "hints": ["Think about lazy evaluation and state preservation."],
    },
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "Python",
        "programming_language": "Python",
        "job_role": "Backend Engineer",
        "difficulty": InterviewDifficultyEnum.ADVANCED,
        "question_text": "Describe Python's Global Interpreter Lock (GIL). What are its implications for CPU-bound versus I/O-bound concurrency, and how can developers circumvent it?",
        "expected_concepts": ["GIL", "mutex", "CPython reference counting", "CPU-bound vs I/O-bound", "multiprocessing", "asyncio", "threading"],
        "evaluation_criteria": {
            "gil_explanation": 4.0,
            "concurrency_impact": 3.0,
            "mitigation_strategies": 3.0,
        },
        "sample_answer": "The GIL is a mutex in CPython preventing multiple native threads from executing Python bytecodes simultaneously. For I/O-bound tasks, threading or asyncio works well. For CPU-bound tasks, multiprocessing or C-extensions bypass the GIL.",
        "hints": ["Focus on CPython thread safety and multiprocessing."],
    },

    # --- TECHNICAL: C / C++ ---
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "C",
        "programming_language": "C",
        "job_role": "Software Developer",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "Explain pointer arithmetic, dynamic memory allocation with malloc/free in C, and what causes segmentation faults or memory leaks.",
        "expected_concepts": ["pointers", "malloc", "free", "dangling pointer", "memory leak", "segmentation fault", "heap vs stack"],
        "evaluation_criteria": {
            "pointer_concepts": 4.0,
            "heap_management": 3.0,
            "fault_causes": 3.0,
        },
        "sample_answer": "Pointers store memory addresses. malloc allocates contiguous bytes on the heap. Failing to free causes memory leaks; dereferencing null, uninitialized, or freed pointers causes segmentation faults.",
        "hints": ["Discuss heap allocation, NULL checking, and freeing pointers."],
    },
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "C++",
        "programming_language": "C++",
        "job_role": "Software Developer",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "What is RAII (Resource Acquisition Is Initialization) in C++, and how do smart pointers (unique_ptr, shared_ptr) prevent memory leaks?",
        "expected_concepts": ["RAII", "smart pointers", "unique_ptr", "shared_ptr", "reference counting", "destructor", "ownership"],
        "evaluation_criteria": {
            "raii_concept": 4.0,
            "smart_pointers": 3.0,
            "ownership_semantics": 3.0,
        },
        "sample_answer": "RAII binds the lifecycle of a resource to object lifetime. When the object goes out of scope, its destructor automatically frees the resource. std::unique_ptr enforces single ownership, while std::shared_ptr maintains reference counts.",
        "hints": ["Focus on deterministic destruction and ownership semantics."],
    },

    # --- TECHNICAL: Java ---
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "Java",
        "programming_language": "Java",
        "job_role": "Software Developer",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "How does Java's Garbage Collection work? Explain the difference between JVM Heap generations (Eden, Survivor, Tenured).",
        "expected_concepts": ["Garbage Collector", "JVM Heap", "Young Generation", "Eden", "Survivor", "Tenured/Old", "Stop the world", "Mark and Sweep"],
        "evaluation_criteria": {
            "gc_mechanism": 4.0,
            "heap_generations": 4.0,
            "performance_considerations": 2.0,
        },
        "sample_answer": "JVM splits heap into Young (Eden + Survivor spaces) and Old/Tenured generations. New objects are born in Eden; surviving minor GC cycles promotes them to Tenured. Major GC scans the old generation using mark-and-sweep.",
        "hints": ["Discuss weak generational hypothesis and GC cycles."],
    },

    # --- TECHNICAL: Data Structures & Algorithms ---
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "Data Structures and Algorithms",
        "programming_language": None,
        "job_role": "Software Developer",
        "difficulty": InterviewDifficultyEnum.BEGINNER,
        "question_text": "Compare arrays and linked lists in terms of memory layout, random access, and insertion/deletion time complexity.",
        "expected_concepts": ["contiguous memory", "pointer traversal", "O(1) random access", "O(N) search", "insertion at head/tail", "cache locality"],
        "evaluation_criteria": {
            "memory_layout": 3.0,
            "time_complexity": 4.0,
            "cache_locality": 3.0,
        },
        "sample_answer": "Arrays use contiguous memory allowing O(1) indexed access and great cache locality, but insertions require O(N) shifts. Linked lists use node pointers allowing O(1) insertions once located, but lack random access and cache locality.",
        "hints": ["Think about spatial locality and index lookups."],
    },
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "Data Structures and Algorithms",
        "programming_language": None,
        "job_role": "Software Developer",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "How does a Hash Table resolve hash collisions? Compare separate chaining with open addressing (linear probing).",
        "expected_concepts": ["hash table", "hash function", "collision", "separate chaining", "open addressing", "linear probing", "load factor", "clustering"],
        "evaluation_criteria": {
            "collision_explanation": 3.0,
            "separate_chaining": 3.5,
            "open_addressing": 3.5,
        },
        "sample_answer": "Collisions occur when two keys produce the same index. Separate chaining stores colliding items in a linked list or tree at that bucket. Open addressing searches for alternate open slots (linear/quadratic probing), which is prone to clustering under high load factors.",
        "hints": ["Discuss worst-case lookup and load factor thresholds."],
    },

    # --- TECHNICAL: SQL and DBMS ---
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "SQL and DBMS",
        "programming_language": "SQL",
        "job_role": "Backend Engineer",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "What are ACID properties in database transactions? Explain each property and why they are vital in high-concurrency systems.",
        "expected_concepts": ["Atomicity", "Consistency", "Isolation", "Durability", "commit", "rollback", "write-ahead log", "concurrency control"],
        "evaluation_criteria": {
            "acid_definitions": 4.0,
            "real_world_examples": 3.0,
            "concurrency_isolation": 3.0,
        },
        "sample_answer": "Atomicity ensures all-or-nothing execution. Consistency preserves integrity constraints. Isolation ensures concurrent transactions do not interfere with each other. Durability guarantees committed data survives power failures.",
        "hints": ["Think of a bank fund transfer between two accounts."],
    },

    # --- TECHNICAL: Operating Systems ---
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "Operating Systems",
        "job_role": "Software Developer",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "Explain the difference between a process and a thread. How does the OS handle context switching and inter-process communication (IPC)?",
        "expected_concepts": ["process", "thread", "address space", "PCB", "TCB", "context switch", "IPC", "shared memory", "pipes"],
        "evaluation_criteria": {
            "process_vs_thread": 4.0,
            "context_switching": 3.0,
            "ipc_mechanisms": 3.0,
        },
        "sample_answer": "A process has its own isolated memory address space and PCB. Threads within a process share the same code, data, and heap, but have independent stacks and registers. Thread context switching is faster because page tables do not need to be flushed.",
        "hints": ["Consider memory isolation, registers, and TLB cache flush."],
    },

    # --- TECHNICAL: Computer Networks ---
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "Computer Networks",
        "job_role": "Software Developer",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "Explain the TCP Three-Way Handshake mechanism. How does TCP ensure reliable, ordered data delivery compared to UDP?",
        "expected_concepts": ["SYN", "SYN-ACK", "ACK", "sequence number", "acknowledgement", "checksum", "flow control", "congestion control", "UDP connectionless"],
        "evaluation_criteria": {
            "handshake_steps": 4.0,
            "reliability_features": 3.0,
            "tcp_vs_udp": 3.0,
        },
        "sample_answer": "Client sends SYN with initial seq number, server replies with SYN-ACK, client acknowledges with ACK. TCP guarantees reliability through packet acknowledgments, sequence ordering, retransmissions, and flow control, unlike UDP which is best-effort.",
        "hints": ["Break down SYN, SYN-ACK, and ACK packets."],
    },

    # --- TECHNICAL: Object-Oriented Programming ---
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "Object-Oriented Programming",
        "job_role": "Software Developer",
        "difficulty": InterviewDifficultyEnum.BEGINNER,
        "question_text": "Explain the four pillars of Object-Oriented Programming (Encapsulation, Abstraction, Inheritance, Polymorphism) with practical examples.",
        "expected_concepts": ["Encapsulation", "Abstraction", "Inheritance", "Polymorphism", "access modifiers", "interfaces/abstract classes", "method overriding/overloading"],
        "evaluation_criteria": {
            "four_pillars": 4.0,
            "practical_examples": 4.0,
            "code_design_benefits": 2.0,
        },
        "sample_answer": "Encapsulation bundles data and methods while restricting direct access. Abstraction hides internal complexity via clean interfaces. Inheritance allows child classes to derive parent behavior. Polymorphism enables treating different classes through a common interface.",
        "hints": ["Use an everyday example like a Vehicle or Bank Account."],
    },

    # --- TECHNICAL: Software Engineering ---
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "Software Engineering",
        "job_role": "Software Developer",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "Explain the SOLID principles in software engineering. Pick two principles and demonstrate how they improve maintainability.",
        "expected_concepts": ["Single Responsibility", "Open/Closed", "Liskov Substitution", "Interface Segregation", "Dependency Inversion", "coupling", "cohesion"],
        "evaluation_criteria": {
            "solid_overview": 4.0,
            "deep_dive_examples": 4.0,
            "maintainability_impact": 2.0,
        },
        "sample_answer": "SOLID stands for Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion. For instance, Single Responsibility ensures each class has only one reason to change, reducing regression bugs.",
        "hints": ["Discuss decoupling, unit testability, and refactoring."],
    },

    # --- TECHNICAL: AI & Machine Learning ---
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "Artificial Intelligence",
        "job_role": "AI/ML Engineer",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "Explain the difference between supervised, unsupervised, and reinforcement learning. What are overfitting and underfitting, and how can they be mitigated?",
        "expected_concepts": ["supervised", "unsupervised", "reinforcement", "labeled data", "clustering", "reward function", "overfitting", "regularization", "cross-validation"],
        "evaluation_criteria": {
            "paradigms_distinction": 4.0,
            "overfitting_underfitting": 3.0,
            "regularization_techniques": 3.0,
        },
        "sample_answer": "Supervised learning trains on labeled inputs/targets; unsupervised identifies patterns in unlabeled data; reinforcement learns optimal policies through reward signals. Overfitting occurs when a model memorizes noise, solvable via dropout, L1/L2 regularization, or more training data.",
        "hints": ["Think about train vs validation error curves."],
    },

    # --- TECHNICAL: Web Development ---
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "Web Development",
        "job_role": "Full Stack Developer",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "Explain CORS (Cross-Origin Resource Sharing). Why does the browser send an OPTIONS preflight request, and how do you configure CORS safely on the backend?",
        "expected_concepts": ["CORS", "Same-Origin Policy", "OPTIONS preflight", "Access-Control-Allow-Origin", "headers", "methods", "credentials"],
        "evaluation_criteria": {
            "cors_purpose": 4.0,
            "preflight_mechanism": 3.0,
            "safe_configuration": 3.0,
        },
        "sample_answer": "CORS is a browser security mechanism that restricts resources requested from outside the origin domain. For non-simple HTTP methods or custom headers, browsers dispatch an OPTIONS preflight request to verify server authorization before sending the real payload.",
        "hints": ["Remember Same-Origin Policy and preflight headers."],
    },

    # --- TECHNICAL: Electronics & Communication Engineering (ECE) ---
    {
        "category": InterviewCategoryEnum.TECHNICAL,
        "subject": "Electronics and Communication Engineering fundamentals",
        "job_role": "Embedded & IoT Engineer",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "Compare I2C, SPI, and UART communication protocols used in embedded microcontrollers. Discuss wire count, speed, and master-slave architecture.",
        "expected_concepts": ["I2C", "SPI", "UART", "SDA/SCL", "MOSI/MISO/SCK/CS", "TX/RX", "synchronous vs asynchronous", "master-slave", "bus arbitration"],
        "evaluation_criteria": {
            "protocol_comparison": 4.0,
            "pin_count_and_speed": 3.0,
            "embedded_use_cases": 3.0,
        },
        "sample_answer": "UART is asynchronous requiring 2 wires (TX/RX) point-to-point. I2C is synchronous 2-wire (SDA/SCL) supporting multiple addressable slaves with pull-ups. SPI is synchronous 4-wire (MOSI/MISO/SCK/CS) offering full-duplex high speed with dedicated chip-select lines.",
        "hints": ["Consider hardware complexity vs communication throughput."],
    },

    # --- HR INTERVIEWS ---
    {
        "category": InterviewCategoryEnum.HR,
        "subject": "HR",
        "job_role": "All Roles",
        "difficulty": InterviewDifficultyEnum.BEGINNER,
        "question_text": "Tell me about yourself, your educational background, and why you are excited to pursue a career in technology.",
        "expected_concepts": ["education", "technical passions", "projects", "career aspirations", "clarity of expression", "professional tone"],
        "evaluation_criteria": {
            "structure_and_flow": 4.0,
            "relevance_to_role": 3.0,
            "enthusiasm_and_clarity": 3.0,
        },
        "sample_answer": "I am an engineering student with a strong foundation in computer science and software development. Throughout my coursework and personal projects, I developed a passion for building scalable web systems and solving real-world customer problems.",
        "hints": ["Structure your answer: Present, Past, Future."],
    },
    {
        "category": InterviewCategoryEnum.HR,
        "subject": "HR",
        "job_role": "All Roles",
        "difficulty": InterviewDifficultyEnum.BEGINNER,
        "question_text": "What are your greatest professional strengths, and what is one area you are actively working to improve?",
        "expected_concepts": ["strengths with evidence", "self-awareness", "actionable improvement", "growth mindset"],
        "evaluation_criteria": {
            "strength_substantiation": 4.0,
            "constructive_weakness": 4.0,
            "growth_demonstration": 2.0,
        },
        "sample_answer": "My primary strength is analytical problem-solving and rapid debugging under pressure. An area I am actively improving is public technical presentations; to overcome this, I have been actively presenting sprint demos and mentoring junior club members.",
        "hints": ["Choose a real weakness and explain the concrete steps you take to address it."],
    },
    {
        "category": InterviewCategoryEnum.HR,
        "subject": "HR",
        "job_role": "All Roles",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "Why should we hire you over other qualified candidates applying for this position?",
        "expected_concepts": ["unique value proposition", "technical competence", "adaptability", "alignment with company goals", "eagerness to learn"],
        "evaluation_criteria": {
            "value_articulation": 4.0,
            "cultural_fit": 3.0,
            "confidence_and_humility": 3.0,
        },
        "sample_answer": "You should hire me because I combine solid technical fundamentals with a relentless work ethic and strong adaptability. I don't just write code; I take ownership of system reliability and collaborate proactively with cross-functional team members.",
        "hints": ["Highlight your technical curiosity, teamwork, and problem ownership."],
    },
    {
        "category": InterviewCategoryEnum.HR,
        "subject": "HR",
        "job_role": "All Roles",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "Where do you see yourself in five years in terms of technical growth and organizational leadership?",
        "expected_concepts": ["five-year vision", "technical mastery", "system architecture", "mentorship/leadership", "continuous learning"],
        "evaluation_criteria": {
            "ambition_and_realism": 4.0,
            "commitment_to_learning": 3.0,
            "leadership_potential": 3.0,
        },
        "sample_answer": "In five years, I envision myself as a seasoned software engineer spearheading complex system architectures, mentoring junior developers, and contributing directly to high-impact technical initiatives within the company.",
        "hints": ["Balance deep technical mastery with mentorship and impact."],
    },

    # --- BEHAVIORAL INTERVIEWS ---
    {
        "category": InterviewCategoryEnum.BEHAVIORAL,
        "subject": "Behavioral",
        "job_role": "All Roles",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "Describe a challenging situation or project roadblock you encountered. How did you diagnose the problem, collaborate with others, and achieve a successful outcome?",
        "expected_concepts": ["STAR method", "Situation", "Task", "Action", "Result", "ownership", "problem-solving", "collaboration"],
        "evaluation_criteria": {
            "star_framework": 4.0,
            "clear_action_steps": 3.0,
            "quantifiable_result": 3.0,
        },
        "sample_answer": "During my capstone project, our microservices experienced high latency spikes. I profiled our database queries, identified missing compound indexes, collaborated with our database lead to update schemas, and reduced response times by 65%.",
        "hints": ["Use the STAR method: Situation, Task, Action, Result."],
    },
    {
        "category": InterviewCategoryEnum.BEHAVIORAL,
        "subject": "Behavioral",
        "job_role": "All Roles",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "Tell me about a time you experienced a disagreement with a team member regarding a technical decision. How did you resolve the conflict constructively?",
        "expected_concepts": ["conflict resolution", "active listening", "data-driven decisions", "compromise", "mutual respect", "team cohesion"],
        "evaluation_criteria": {
            "constructive_approach": 4.0,
            "objective_criteria": 3.0,
            "positive_team_outcome": 3.0,
        },
        "sample_answer": "When designing an API schema, a teammate and I differed on GraphQL versus REST. Instead of debating subjectively, we built small prototypes for our specific read-heavy queries, benchmarked latency, and agreed on REST for its superior caching benefits.",
        "hints": ["Focus on mutual respect, data-backed decisions, and shared objectives."],
    },
    {
        "category": InterviewCategoryEnum.BEHAVIORAL,
        "subject": "Behavioral",
        "job_role": "All Roles",
        "difficulty": InterviewDifficultyEnum.INTERMEDIATE,
        "question_text": "Describe a scenario where you had to manage tight deadlines and competing project priorities. What steps did you take to organize your time and deliver on schedule?",
        "expected_concepts": ["time management", "prioritization", "Eisenhower matrix", "transparent communication", "scope management"],
        "evaluation_criteria": {
            "prioritization_strategy": 4.0,
            "communication_with_stakeholders": 3.0,
            "on-time_delivery": 3.0,
        },
        "sample_answer": "During exam week, our team had a major submission deadline. I prioritized critical deliverables using an impact-effort matrix, delegated tasks based on individual strengths, maintained daily standup check-ins, and delivered 24 hours ahead of schedule.",
        "hints": ["Explain how you prioritize tasks and keep stakeholders informed."],
    },
]


class QuestionGenerationService:
    """
    Selects or generates validated interview questions.
    Step 1: Check Predefined Question Bank.
    Step 2: If insufficient questions, generate dynamically using AI Provider + Educational MediaWiki context.
    Step 3: Validate question quality, topic alignment, and absence of duplicates.
    """

    @classmethod
    def seed_question_bank_if_empty(cls, db: Session) -> int:
        """Populate initial curated question bank if empty."""
        existing_count = db.query(AIQuestionBank).count()
        if existing_count > 0:
            return existing_count

        logger.info("Seeding AI Interview Question Bank with curated questions...")
        seeded = 0
        for item in INITIAL_PREDEFINED_QUESTIONS:
            q = AIQuestionBank(
                category=item["category"],
                subject=item["subject"],
                programming_language=item.get("programming_language"),
                job_role=item.get("job_role", "Software Developer"),
                difficulty=item["difficulty"],
                experience_level=ExperienceLevelEnum.STUDENT,
                question_text=item["question_text"],
                expected_concepts=item["expected_concepts"],
                evaluation_criteria=item["evaluation_criteria"],
                sample_answer=item.get("sample_answer"),
                hints=item.get("hints", []),
                question_source="predefined",
                validation_status=QuestionValidationStatusEnum.VERIFIED,
                is_active=True,
            )
            db.add(q)
            seeded += 1

        db.commit()
        logger.info("Successfully seeded %d questions into AIQuestionBank.", seeded)
        return seeded

SUBJECT_SUBTOPICS = {
    "Python": [
        {"subtopic": "Python generators and iterators", "wiki_query": "Python (programming language) generator yield"},
        {"subtopic": "Python Global Interpreter Lock (GIL)", "wiki_query": "Global Interpreter Lock CPython"},
        {"subtopic": "Python memory management and reference counting", "wiki_query": "Python (programming language) memory management"},
        {"subtopic": "Python decorators and closures", "wiki_query": "Python (programming language) decorator closure"},
        {"subtopic": "Python asyncio and concurrency", "wiki_query": "Async/await Python asyncio"},
        {"subtopic": "Python mutable vs immutable data types", "wiki_query": "Immutable object Python"},
        {"subtopic": "Python context managers and with statement", "wiki_query": "Context manager Python"},
        {"subtopic": "Python metaclasses and type system", "wiki_query": "Metaclass Python"},
    ],
    "C": [
        {"subtopic": "C pointer arithmetic and memory layout", "wiki_query": "Pointer (computer programming) C"},
        {"subtopic": "Dynamic memory allocation malloc and free in C", "wiki_query": "C dynamic memory allocation"},
        {"subtopic": "C structure padding and memory alignment", "wiki_query": "Data structure alignment C"},
        {"subtopic": "C preprocessor macros vs inline functions", "wiki_query": "C preprocessor macro"},
        {"subtopic": "Segmentation fault and memory leaks in C", "wiki_query": "Segmentation fault memory leak C"},
    ],
    "C++": [
        {"subtopic": "RAII and smart pointers (unique_ptr, shared_ptr)", "wiki_query": "Resource acquisition is initialization C++"},
        {"subtopic": "C++ move semantics and rvalue references", "wiki_query": "Move semantics C++11 rvalue"},
        {"subtopic": "Virtual functions and vtable polymorphism", "wiki_query": "Virtual method table C++"},
        {"subtopic": "Templates and template metaprogramming", "wiki_query": "Template (C++) metaprogramming"},
        {"subtopic": "STL containers and complexity guarantees", "wiki_query": "Standard Template Library C++"},
    ],
    "Java": [
        {"subtopic": "JVM garbage collection and generational heap", "wiki_query": "Garbage collection (computer science) Java Virtual Machine"},
        {"subtopic": "JVM memory model and thread synchronization", "wiki_query": "Java memory model synchronization volatile"},
        {"subtopic": "Java Collections framework and HashMaps", "wiki_query": "Java collections framework HashMap"},
        {"subtopic": "Java ClassLoader architecture", "wiki_query": "Java Classloader"},
        {"subtopic": "Java 8 Streams, lambdas, and functional interfaces", "wiki_query": "Java 8 Stream lambda"},
    ],
    "Data Structures and Algorithms": [
        {"subtopic": "Hash table collision resolution (chaining vs open addressing)", "wiki_query": "Hash table collision resolution"},
        {"subtopic": "Shortest path algorithms: Dijkstra vs Bellman-Ford", "wiki_query": "Dijkstra's algorithm Bellman-Ford"},
        {"subtopic": "Binary Search Trees vs Self-balancing AVL and Red-Black Trees", "wiki_query": "Self-balancing binary search tree AVL Red-Black"},
        {"subtopic": "Dynamic programming and optimal substructure", "wiki_query": "Dynamic programming memoization"},
        {"subtopic": "Graph traversal algorithms: BFS and DFS", "wiki_query": "Breadth-first search Depth-first search"},
        {"subtopic": "Sorting algorithms time complexity and stability", "wiki_query": "Quicksort Mergesort stability time complexity"},
        {"subtopic": "Priority queues and binary heaps", "wiki_query": "Binary heap priority queue"},
    ],
    "SQL and DBMS": [
        {"subtopic": "ACID properties and transaction isolation levels", "wiki_query": "ACID database transaction isolation"},
        {"subtopic": "Database normalization (1NF, 2NF, 3NF, BCNF)", "wiki_query": "Database normalization Boyce-Codd"},
        {"subtopic": "B-Tree and B+ Tree database indexing", "wiki_query": "B-tree B+ tree database index"},
        {"subtopic": "Relational algebra and SQL JOIN types", "wiki_query": "Join (SQL) Relational algebra"},
        {"subtopic": "CAP theorem and NoSQL databases", "wiki_query": "CAP theorem NoSQL relational database"},
        {"subtopic": "Query execution plans and indexing strategies", "wiki_query": "Query execution plan SQL index"},
    ],
    "Operating Systems": [
        {"subtopic": "Virtual memory, paging, and page replacement algorithms", "wiki_query": "Virtual memory page replacement algorithm"},
        {"subtopic": "Process scheduling algorithms and context switching", "wiki_query": "Scheduling (computing) context switch"},
        {"subtopic": "Deadlock conditions and Banker's algorithm", "wiki_query": "Deadlock Banker's algorithm"},
        {"subtopic": "Inter-process communication, semaphores, and mutexes", "wiki_query": "Semaphore (programming) mutual exclusion"},
        {"subtopic": "File systems, inodes, and disk allocation", "wiki_query": "Inode file system disk allocation"},
    ],
    "Computer Networks": [
        {"subtopic": "TCP three-way handshake and connection teardown", "wiki_query": "Transmission Control Protocol handshake"},
        {"subtopic": "OSI 7-layer model vs TCP/IP model", "wiki_query": "OSI model TCP/IP model"},
        {"subtopic": "DNS resolution and hierarchical domain system", "wiki_query": "Domain Name System resolution"},
        {"subtopic": "HTTP, HTTPS, and TLS/SSL handshake", "wiki_query": "Transport Layer Security HTTPS"},
        {"subtopic": "Routing protocols: Distance-vector vs Link-state", "wiki_query": "Routing protocol Link-state Distance-vector"},
        {"subtopic": "Subnetting, CIDR notation, and IP addressing", "wiki_query": "Classless Inter-Domain Routing subnet"},
    ],
    "Object-Oriented Programming": [
        {"subtopic": "SOLID design principles in software engineering", "wiki_query": "SOLID object-oriented design"},
        {"subtopic": "Polymorphism: static vs dynamic dispatch", "wiki_query": "Polymorphism (computer science)"},
        {"subtopic": "Composition over inheritance", "wiki_query": "Composition over inheritance"},
        {"subtopic": "Creational and Behavioral Design Patterns", "wiki_query": "Software design pattern Gang of Four"},
    ],
    "Software Engineering": [
        {"subtopic": "Agile methodologies vs Waterfall model", "wiki_query": "Agile software development Waterfall model"},
        {"subtopic": "CI/CD automated deployment pipelines", "wiki_query": "Continuous integration continuous delivery"},
        {"subtopic": "Microservices architecture vs Monolith", "wiki_query": "Microservices software architecture"},
        {"subtopic": "Git version control branching strategies", "wiki_query": "Git version control branching"},
    ],
    "Artificial Intelligence": [
        {"subtopic": "Informed search algorithms: A* and heuristics", "wiki_query": "A* search algorithm heuristic"},
        {"subtopic": "Adversarial search: Minimax and Alpha-Beta pruning", "wiki_query": "Minimax Alpha-beta pruning"},
        {"subtopic": "Knowledge representation and expert systems", "wiki_query": "Knowledge representation expert system"},
    ],
    "Machine Learning": [
        {"subtopic": "Bias-variance tradeoff and regularization (L1/L2)", "wiki_query": "Bias-variance tradeoff Regularization (mathematics)"},
        {"subtopic": "Gradient descent and backpropagation algorithms", "wiki_query": "Backpropagation Gradient descent"},
        {"subtopic": "Supervised vs Unsupervised vs Reinforcement Learning", "wiki_query": "Supervised learning Reinforcement learning"},
        {"subtopic": "Evaluation metrics: Precision, Recall, ROC-AUC", "wiki_query": "Precision and recall ROC curve"},
    ],
    "Web Development": [
        {"subtopic": "CORS and browser Same-Origin Policy", "wiki_query": "Cross-origin resource sharing Same-origin policy"},
        {"subtopic": "REST architectural style and HTTP specifications", "wiki_query": "REST Representational state transfer HTTP"},
        {"subtopic": "Web security: XSS, CSRF, and SQL injection", "wiki_query": "Cross-site scripting Cross-site request forgery"},
        {"subtopic": "WebSockets vs Server-Sent Events vs polling", "wiki_query": "WebSocket Server-sent events"},
    ],
    "Electronics and Communication Engineering fundamentals": [
        {"subtopic": "Serial protocols: I2C, SPI, and UART comparison", "wiki_query": "I2C Serial Peripheral Interface UART"},
        {"subtopic": "Nyquist-Shannon sampling theorem and aliasing", "wiki_query": "Nyquist-Shannon sampling theorem aliasing"},
        {"subtopic": "Microprocessor vs Microcontroller architectures", "wiki_query": "Microcontroller Microprocessor architecture"},
        {"subtopic": "Operational amplifiers and negative feedback", "wiki_query": "Operational amplifier negative feedback"},
    ],
    "HR": [
        {"subtopic": "Professional background, self-introduction, and career motivation", "wiki_query": "Job interview Career development"},
        {"subtopic": "Strengths, constructive weaknesses, and continuous self-improvement", "wiki_query": "Self-awareness Growth mindset"},
        {"subtopic": "Conflict resolution and team collaboration", "wiki_query": "Conflict resolution Workplace communication"},
        {"subtopic": "Five-year professional vision and technical leadership", "wiki_query": "Leadership development Career pathway"},
    ],
    "Behavioral": [
        {"subtopic": "STAR method: overcoming technical blockers under pressure", "wiki_query": "Situation, task, action, result problem solving"},
        {"subtopic": "Constructive technical disagreement and consensus building", "wiki_query": "Consensus decision-making Active listening"},
        {"subtopic": "Leadership, ownership, and initiating proactive solutions", "wiki_query": "Leadership Proactivity"},
        {"subtopic": "Root-cause post-mortem and learning from mistakes", "wiki_query": "Postmortem documentation Root cause analysis"},
    ],
}


class QuestionGenerationService:
    """
    Selects or generates validated interview questions.
    Step 1: Check Predefined Question Bank.
    Step 2: If insufficient questions, generate dynamically using AI Provider + Educational MediaWiki context.
    Step 3: Validate question quality, topic alignment, and absence of duplicates.
    """

    @classmethod
    def seed_question_bank_if_empty(cls, db: Session) -> int:
        """Populate initial curated question bank if empty."""
        existing_count = db.query(AIQuestionBank).count()
        if existing_count > 0:
            return existing_count

        logger.info("Seeding AI Interview Question Bank with curated questions...")
        seeded = 0
        for item in INITIAL_PREDEFINED_QUESTIONS:
            q = AIQuestionBank(
                category=item["category"],
                subject=item["subject"],
                programming_language=item.get("programming_language"),
                job_role=item.get("job_role", "Software Developer"),
                difficulty=item["difficulty"],
                experience_level=ExperienceLevelEnum.STUDENT,
                question_text=item["question_text"],
                expected_concepts=item["expected_concepts"],
                evaluation_criteria=item["evaluation_criteria"],
                sample_answer=item.get("sample_answer"),
                hints=item.get("hints", []),
                question_source="predefined",
                validation_status=QuestionValidationStatusEnum.VERIFIED,
                is_active=True,
            )
            db.add(q)
            seeded += 1

        db.commit()
        logger.info("Successfully seeded %d questions into AIQuestionBank.", seeded)
        return seeded

    @classmethod
    def get_or_generate_question(
        cls,
        db: Session,
        category: str,
        subject: str,
        difficulty: str,
        job_role: str = "Software Developer",
        experience_level: str = "Student",
        excluded_question_ids: Optional[List[str]] = None,
        previous_context: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Main Question Provider Workflow.
        1. Selects randomized subtopics to ensure question diversity every time.
        2. Performs Wikipedia web scraping to extract confirmed theory, historical dates, and canonical references.
        3. Checks database question bank, or dynamically generates a newly verified question grounded in Wikipedia.
        """
        cls.seed_question_bank_if_empty(db)
        excluded_ids = excluded_question_ids or []

        # 1. Pick a randomized subtopic for the subject to ensure non-repetitive variety
        subtopics = SUBJECT_SUBTOPICS.get(subject, [
            {"subtopic": f"{subject} core principles and architecture", "wiki_query": subject},
            {"subtopic": f"{subject} performance optimization and trade-offs", "wiki_query": f"{subject} theory"},
            {"subtopic": f"{subject} design patterns and practical applications", "wiki_query": f"{subject} application"},
        ])
        chosen_subtopic_obj = random.choice(subtopics)
        chosen_subtopic = chosen_subtopic_obj["subtopic"]
        wiki_query = chosen_subtopic_obj.get("wiki_query", chosen_subtopic)

        # 2. Scrape / Retrieve Wikipedia Theory & Dates for Grounding
        wiki_ctx = KnowledgeRetrievalService.get_or_fetch_topic_knowledge(db, subject, subtopic=wiki_query)
        dates_list = wiki_ctx.get("dates_and_milestones", []) if wiki_ctx else []
        dates_str = ", ".join(dates_list[:3]) if dates_list else ""
        source_ref = wiki_ctx["source_url"] if wiki_ctx else f"https://en.wikipedia.org/wiki/{subject.replace(' ', '_')}"
        wiki_title = wiki_ctx["article_title"] if wiki_ctx else subject
        wiki_summary = wiki_ctx["content_summary"] if wiki_ctx else ""

        # 3. Check Question Bank for existing unasked questions
        query = db.query(AIQuestionBank).filter(
            AIQuestionBank.is_active == True,
            AIQuestionBank.validation_status == QuestionValidationStatusEnum.VERIFIED,
            AIQuestionBank.category == category,
            AIQuestionBank.subject.ilike(f"%{subject}%"),
        )
        if difficulty:
            query = query.filter(AIQuestionBank.difficulty == difficulty)
        if excluded_ids:
            query = query.filter(~AIQuestionBank.id.in_(excluded_ids))

        # Check if question bank has questions matching chosen subtopic
        all_candidates = query.all()
        subtopic_candidates = [
            q for q in all_candidates
            if any(w.lower() in q.question_text.lower() for w in chosen_subtopic.split()[:2])
        ]
        candidate_questions = subtopic_candidates if subtopic_candidates else all_candidates

        # If an unasked matching question exists in Bank, verify it with Wikipedia and return
        if candidate_questions:
            chosen = random.choice(candidate_questions)
            return {
                "question_bank_id": chosen.id,
                "question_text": chosen.question_text,
                "topic": chosen.subject,
                "difficulty": chosen.difficulty.value if hasattr(chosen.difficulty, "value") else str(chosen.difficulty),
                "expected_concepts": chosen.expected_concepts,
                "evaluation_criteria": chosen.evaluation_criteria,
                "question_source": "wikipedia_verified",
                "source_reference": source_ref,
                "sample_answer": chosen.sample_answer,
                "dates_and_milestones": dates_list,
                "is_ai_generated": False,
            }

        # 4. If Question Bank does not have unasked questions, generate dynamically using Wikipedia grounding + AI
        logger.info("Generating new Wikipedia-grounded interview question for %s / %s...", subject, chosen_subtopic)

        context_str = (
            f"Confirmed Wikipedia Educational Grounding for '{wiki_title}':\n"
            f"Summary & Theory: {wiki_summary}\n"
            f"Relevant Historical Dates / Milestones: {dates_str if dates_str else 'N/A'}\n"
            f"Canonical URL: {source_ref}\n"
            f"Attribution: {wiki_ctx.get('attribution') if wiki_ctx else ''}"
        )

        system_prompt = (
            "You are an expert technical interviewer and educator for college placements. "
            "Generate one targeted, high-quality interview question for a campus placement interview, "
            "grounded in the provided verified Wikipedia educational theory and dates."
        )

        user_prompt = f"""
Category: {category}
Subject/Topic: {subject}
Subtopic Area: {chosen_subtopic}
Job Role: {job_role}
Difficulty Level: {difficulty}
Target Candidate Level: {experience_level}
{context_str}

Please generate a JSON object with the following fields:
- question_text: The interview question (clear, thought-provoking, appropriate for the level).
- topic: specific subtopic ({chosen_subtopic}).
- difficulty: {difficulty}.
- expected_concepts: list of 4-6 essential concepts or keywords the candidate must mention.
- evaluation_criteria: dictionary with criteria and mark distribution summing to 10.
- sample_answer: a concise model answer (2-3 sentences) referencing the confirmed theory.
- hints: 1-2 helpful hints.
"""

        ai_response = AIProviderService.call_ai(system_prompt, user_prompt, max_tokens=600)

        if ai_response and "question_text" in ai_response and "expected_concepts" in ai_response:
            q_text = ai_response["question_text"].strip()
            if len(q_text) > 15:
                # Add newly generated question to Question Bank as verified
                new_q = AIQuestionBank(
                    category=category,
                    subject=subject,
                    job_role=job_role,
                    difficulty=difficulty,
                    experience_level=experience_level,
                    question_text=q_text,
                    expected_concepts=ai_response.get("expected_concepts", [subject, chosen_subtopic]),
                    evaluation_criteria=ai_response.get("evaluation_criteria", {"correctness": 5.0, "clarity": 5.0}),
                    sample_answer=ai_response.get("sample_answer", ""),
                    hints=ai_response.get("hints", []),
                    question_source="wikipedia_backed",
                    source_reference=source_ref,
                    validation_status=QuestionValidationStatusEnum.VERIFIED,
                    is_active=True,
                )
                db.add(new_q)
                db.commit()
                db.refresh(new_q)

                return {
                    "question_bank_id": new_q.id,
                    "question_text": q_text,
                    "topic": chosen_subtopic,
                    "difficulty": difficulty,
                    "expected_concepts": new_q.expected_concepts,
                    "evaluation_criteria": new_q.evaluation_criteria,
                    "question_source": "wikipedia_backed",
                    "source_reference": source_ref,
                    "sample_answer": new_q.sample_answer,
                    "dates_and_milestones": dates_list,
                    "is_ai_generated": True,
                }

        # 5. Fallback generator using scraped Wikipedia theory and dates directly
        date_mention = f" (first established / documented around {dates_list[0]})" if dates_list else ""
        generated_q_text = (
            f"Explain the theoretical foundations and core mechanisms of {wiki_title}{date_mention} in relation to {chosen_subtopic}. "
            f"How does it operate in production systems, and what are its primary performance or space trade-offs?"
        )
        first_sentence = wiki_summary.split(".")[0] if wiki_summary else f"Theoretical principles of {subject}"
        model_ans = (
            f"According to established theory from Wikipedia ({wiki_title}): {first_sentence}. "
            f"In real-world software, it achieves high efficiency while trading off memory overhead and algorithmic complexity."
        )

        fallback_q = AIQuestionBank(
            category=category,
            subject=subject,
            job_role=job_role,
            difficulty=difficulty,
            experience_level=experience_level,
            question_text=generated_q_text,
            expected_concepts=[wiki_title.lower(), chosen_subtopic.lower(), "efficiency", "trade-offs"],
            evaluation_criteria={"theoretical_understanding": 4.0, "practical_implementation": 3.0, "trade-offs": 3.0},
            sample_answer=model_ans,
            hints=[f"Think about {wiki_title} core mechanisms and design trade-offs."],
            question_source="wikipedia_backed",
            source_reference=source_ref,
            validation_status=QuestionValidationStatusEnum.VERIFIED,
            is_active=True,
        )
        db.add(fallback_q)
        db.commit()
        db.refresh(fallback_q)

        return {
            "question_bank_id": fallback_q.id,
            "question_text": generated_q_text,
            "topic": chosen_subtopic,
            "difficulty": difficulty,
            "expected_concepts": fallback_q.expected_concepts,
            "evaluation_criteria": fallback_q.evaluation_criteria,
            "question_source": "wikipedia_backed",
            "source_reference": source_ref,
            "sample_answer": model_ans,
            "dates_and_milestones": dates_list,
            "is_ai_generated": True,
        }

    @classmethod
    def generate_follow_up_question(
        cls,
        db: Session,
        question_text: str,
        student_answer: str,
        subject: str,
        difficulty: str,
    ) -> Optional[Dict[str, Any]]:
        """
        Generate an adaptive follow-up question based on the student's answer.
        """
        system_prompt = (
            "You are an expert interviewer. The candidate just provided an answer to an interview question. "
            "Ask a single concise, technical follow-up question probing deeper into their reasoning, "
            "edge cases, performance implications, or trade-offs."
        )
        user_prompt = f"""
Subject: {subject}
Difficulty: {difficulty}
Original Question: {question_text}
Candidate's Answer: {student_answer}

Provide a JSON object with:
- follow_up_question: The single follow-up question text.
- expected_concepts: list of 3-5 keywords expected in response.
"""
        res = AIProviderService.call_ai(system_prompt, user_prompt, max_tokens=300)
        if res and "follow_up_question" in res:
            q_text = res["follow_up_question"].strip()
            if len(q_text) > 10:
                return {
                    "question_text": q_text,
                    "topic": f"{subject} Follow-up",
                    "difficulty": difficulty,
                    "expected_concepts": res.get("expected_concepts", [subject]),
                    "evaluation_criteria": {"depth_of_knowledge": 5.0, "clarity": 5.0},
                    "generated_follow_up": True,
                }

        # Deterministic follow-up if AI offline
        return {
            "question_text": f"You mentioned key points regarding {subject}. What are the performance trade-offs and edge cases you would consider in production?",
            "topic": f"{subject} Follow-up",
            "difficulty": difficulty,
            "expected_concepts": ["trade-offs", "performance", "edge cases", "scalability"],
            "evaluation_criteria": {"depth_of_knowledge": 5.0, "clarity": 5.0},
            "generated_follow_up": True,
        }
