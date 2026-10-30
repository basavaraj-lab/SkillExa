import sys, os
sys.path.insert(0, os.path.abspath('.'))
import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    problems = json.load(f)

queue_ids = {
    "dsa-queue-array", "dsa-queue-circular", "dsa-queue-stack-using-queue",
    "dsa-queue-generate-binary", "dsa-queue-reverse", "dsa-queue-two-stacks",
    "dsa-queue-first-non-repeating", "dsa-queue-recent-calls", "dsa-queue-sliding-window-max",
    "dsa-queue-first-negative", "dsa-queue-rotten-oranges", "dsa-queue-shortest-path-binary",
    "dsa-queue-perfect-squares", "dsa-queue-open-lock", "dsa-queue-sliding-puzzle"
}
problems = [p for p in problems if p["id"] not in queue_ids]

queue_data = [
    # 1. Implement Queue Using Array
    {
        "id": "dsa-queue-array",
        "problem_num": 106,
        "title": "Implement Queue Using Array",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "Array Queue Implementation",
        "difficulty": "EASY",
        "description": "Implement a queue using an array with enqueue, dequeue, peek, and isEmpty operations.",
        "input_format": "Number of operations followed by commands ('enqueue X', 'dequeue', 'peek', 'isEmpty').",
        "output_format": "Output of dequeue/peek/isEmpty.",
        "constraints": "1 <= operations <= 1000",
        "time_complexity": "O(1) per operation",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "TCS", "Infosys", "Wipro"],
        "examples": [
            {"input": "4 enqueue 10 enqueue 20 enqueue 30 dequeue", "output": "10", "explanation": "Dequeued front element 10."},
            {"input": "3 enqueue 5 enqueue 15 peek", "output": "5", "explanation": "Peek front element is 5."},
            {"input": "1 isEmpty", "output": "True", "explanation": "Empty queue returns True."}
        ],
        "test_cases": [
            {"input": "4 enqueue 10 enqueue 20 enqueue 30 dequeue", "expected": "10", "is_hidden": False},
            {"input": "3 enqueue 5 enqueue 15 peek", "expected": "5", "is_hidden": False},
            {"input": "1 isEmpty", "expected": "True", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n\n// Implement Queue using Array\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\n// Implement Queue using Array\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "class Queue:\n    def __init__(self):\n        self.queue = []\n\n    def enqueue(self, x):\n        pass\n\n    def dequeue(self):\n        pass\n\n    def peek(self):\n        pass\n\n    def isEmpty(self):\n        pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define MAX 10005

typedef struct {
    int arr[MAX];
    int front;
    int rear;
} Queue;

void init(Queue *q) {
    q->front = 0;
    q->rear = 0;
}

void enqueue(Queue *q, int x) {
    q->arr[q->rear++] = x;
}

int dequeue(Queue *q) {
    if (q->front == q->rear) return -1;
    return q->arr[q->front++];
}

int peek(Queue *q) {
    if (q->front == q->rear) return -1;
    return q->arr[q->front];
}

bool isEmpty(Queue *q) {
    return q->front == q->rear;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    Queue q;
    init(&q);
    for (int i = 0; i < n; i++) {
        char op[20];
        scanf("%s", op);
        if (strcmp(op, "enqueue") == 0) {
            int x; scanf("%d", &x);
            enqueue(&q, x);
        } else if (strcmp(op, "dequeue") == 0) {
            printf("%d\\n", dequeue(&q));
        } else if (strcmp(op, "peek") == 0) {
            printf("%d\\n", peek(&q));
        } else if (strcmp(op, "isEmpty") == 0) {
            printf("%s\\n", isEmpty(&q) ? "True" : "False");
        }
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Queue {
    vector<int> q;
    int frontIdx = 0;
public:
    void enqueue(int x) {
        q.push_back(x);
    }
    int dequeue() {
        if (frontIdx >= (int)q.size()) return -1;
        return q[frontIdx++];
    }
    int peek() {
        if (frontIdx >= (int)q.size()) return -1;
        return q[frontIdx];
    }
    bool isEmpty() {
        return frontIdx >= (int)q.size();
    }
};

int main() {
    int n;
    if (!(cin >> n)) return 0;
    Queue q;
    for (int i = 0; i < n; i++) {
        string op; cin >> op;
        if (op == "enqueue") {
            int x; cin >> x;
            q.enqueue(x);
        } else if (op == "dequeue") {
            cout << q.dequeue() << "\\n";
        } else if (op == "peek") {
            cout << q.peek() << "\\n";
        } else if (op == "isEmpty") {
            cout << (q.isEmpty() ? "True" : "False") << "\\n";
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

class Queue {
    private List<Integer> list = new ArrayList<>();
    private int frontIdx = 0;

    public void enqueue(int x) {
        list.add(x);
    }

    public int dequeue() {
        if (frontIdx >= list.size()) return -1;
        return list.get(frontIdx++);
    }

    public int peek() {
        if (frontIdx >= list.size()) return -1;
        return list.get(frontIdx);
    }

    public boolean isEmpty() {
        return frontIdx >= list.size();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        Queue q = new Queue();
        for (int i = 0; i < n; i++) {
            String op = sc.next();
            if (op.equals("enqueue")) {
                int x = sc.nextInt();
                q.enqueue(x);
            } else if (op.equals("dequeue")) {
                System.out.println(q.dequeue());
            } else if (op.equals("peek")) {
                System.out.println(q.peek());
            } else if (op.equals("isEmpty")) {
                System.out.println(q.isEmpty() ? "True" : "False");
            }
        }
    }
}""",
            "python": """import sys

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.queue:
            return -1
        return self.queue.pop(0)

    def peek(self):
        if not self.queue:
            return -1
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        q = Queue()
        idx = 1
        for _ in range(n):
            op = tokens[idx]
            idx += 1
            if op == "enqueue":
                x = int(tokens[idx])
                idx += 1
                q.enqueue(x)
            elif op == "dequeue":
                print(q.dequeue())
            elif op == "peek":
                print(q.peek())
            elif op == "isEmpty":
                print(q.isEmpty())"""
        })
    },

    # 2. Implement Circular Queue
    {
        "id": "dsa-queue-circular",
        "problem_num": 107,
        "title": "Implement Circular Queue",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "Ring Buffer",
        "difficulty": "EASY",
        "description": "Implement a circular queue with fixed capacity. When rear reaches the last index, wrap around to index 0.",
        "input_format": "k (capacity), num_operations, followed by operation commands.",
        "output_format": "Space-separated Boolean/Integer results of operations.",
        "constraints": "1 <= k <= 1000",
        "time_complexity": "O(1) per operation",
        "space_complexity": "O(k)",
        "company_tags": ["Amazon", "Microsoft", "Goldman Sachs"],
        "examples": [
            {"input": "3 3 enQueue 10 enQueue 20 enQueue 30", "output": "True True True", "explanation": "3 elements enqueued successfully."},
            {"input": "2 3 enQueue 1 enQueue 2 enQueue 3", "output": "True True False", "explanation": "Capacity 2 reached, 3rd enqueue fails."},
            {"input": "2 4 enQueue 1 enQueue 2 deQueue enQueue 3", "output": "True True True True", "explanation": "Wrap-around space made after dequeue."}
        ],
        "test_cases": [
            {"input": "3 3 enQueue 10 enQueue 20 enQueue 30", "expected": "True True True", "is_hidden": False},
            {"input": "2 3 enQueue 1 enQueue 2 enQueue 3", "expected": "True True False", "is_hidden": False},
            {"input": "2 4 enQueue 1 enQueue 2 deQueue enQueue 3", "expected": "True True True True", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <stdlib.h>\n#include <string.h>\n\n// Implement Circular Queue\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\n// Implement Circular Queue\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "class MyCircularQueue:\n    def __init__(self, k):\n        pass\n\n    def enQueue(self, value):\n        pass\n\n    def deQueue(self):\n        pass\n\n    def Front(self):\n        pass\n\n    def Rear(self):\n        pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int *queue;
    int size;
    int front;
    int rear;
    int count;
} MyCircularQueue;

MyCircularQueue* createQueue(int k) {
    MyCircularQueue *q = (MyCircularQueue*)malloc(sizeof(MyCircularQueue));
    q->queue = (int*)malloc(sizeof(int) * k);
    q->size = k;
    q->front = 0;
    q->rear = -1;
    q->count = 0;
    return q;
}

bool enQueue(MyCircularQueue* q, int value) {
    if (q->count == q->size) return false;
    q->rear = (q->rear + 1) % q->size;
    q->queue[q->rear] = value;
    q->count++;
    return true;
}

bool deQueue(MyCircularQueue* q) {
    if (q->count == 0) return false;
    q->front = (q->front + 1) % q->size;
    q->count--;
    return true;
}

int Front(MyCircularQueue* q) {
    if (q->count == 0) return -1;
    return q->queue[q->front];
}

int Rear(MyCircularQueue* q) {
    if (q->count == 0) return -1;
    return q->queue[q->rear];
}

int main() {
    int k, n;
    if (scanf("%d %d", &k, &n) != 2) return 0;
    MyCircularQueue *q = createQueue(k);
    for (int i = 0; i < n; i++) {
        char op[20];
        scanf("%s", op);
        if (strcmp(op, "enQueue") == 0) {
            int v; scanf("%d", &v);
            printf("%s%s", enQueue(q, v) ? "True" : "False", (i == n - 1) ? "\\n" : " ");
        } else if (strcmp(op, "deQueue") == 0) {
            printf("%s%s", deQueue(q) ? "True" : "False", (i == n - 1) ? "\\n" : " ");
        } else if (strcmp(op, "Front") == 0) {
            printf("%d%s", Front(q), (i == n - 1) ? "\\n" : " ");
        } else if (strcmp(op, "Rear") == 0) {
            printf("%d%s", Rear(q), (i == n - 1) ? "\\n" : " ");
        }
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

class MyCircularQueue {
    vector<int> queue;
    int size;
    int front;
    int rear;
    int count;
public:
    MyCircularQueue(int k) : queue(k), size(k), front(0), rear(-1), count(0) {}

    bool enQueue(int value) {
        if (count == size) return false;
        rear = (rear + 1) % size;
        queue[rear] = value;
        count++;
        return true;
    }

    bool deQueue() {
        if (count == 0) return false;
        front = (front + 1) % size;
        count--;
        return true;
    }

    int Front() {
        if (count == 0) return -1;
        return queue[front];
    }

    int Rear() {
        if (count == 0) return -1;
        return queue[rear];
    }
};

int main() {
    int k, n;
    if (!(cin >> k >> n)) return 0;
    MyCircularQueue q(k);
    for (int i = 0; i < n; i++) {
        string op; cin >> op;
        if (op == "enQueue") {
            int v; cin >> v;
            cout << (q.enQueue(v) ? "True" : "False") << (i == n - 1 ? "\\n" : " ");
        } else if (op == "deQueue") {
            cout << (q.deQueue() ? "True" : "False") << (i == n - 1 ? "\\n" : " ");
        } else if (op == "Front") {
            cout << q.Front() << (i == n - 1 ? "\\n" : " ");
        } else if (op == "Rear") {
            cout << q.Rear() << (i == n - 1 ? "\\n" : " ");
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

class MyCircularQueue {
    private int[] queue;
    private int size;
    private int front = 0;
    private int rear = -1;
    private int count = 0;

    public MyCircularQueue(int k) {
        this.size = k;
        this.queue = new int[k];
    }

    public boolean enQueue(int value) {
        if (count == size) return false;
        rear = (rear + 1) % size;
        queue[rear] = value;
        count++;
        return true;
    }

    public boolean deQueue() {
        if (count == 0) return false;
        front = (front + 1) % size;
        count--;
        return true;
    }

    public int Front() {
        if (count == 0) return -1;
        return queue[front];
    }

    public int Rear() {
        if (count == 0) return -1;
        return queue[rear];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int k = sc.nextInt();
        int n = sc.nextInt();
        MyCircularQueue q = new MyCircularQueue(k);
        for (int i = 0; i < n; i++) {
            String op = sc.next();
            if (op.equals("enQueue")) {
                int v = sc.nextInt();
                System.out.print((q.enQueue(v) ? "True" : "False") + (i == n - 1 ? "\\n" : " "));
            } else if (op.equals("deQueue")) {
                System.out.print((q.deQueue() ? "True" : "False") + (i == n - 1 ? "\\n" : " "));
            } else if (op.equals("Front")) {
                System.out.print(q.Front() + (i == n - 1 ? "\\n" : " "));
            } else if (op.equals("Rear")) {
                System.out.print(q.Rear() + (i == n - 1 ? "\\n" : " "));
            }
        }
    }
}""",
            "python": """import sys

class MyCircularQueue:
    def __init__(self, k):
        self.queue = [0] * k
        self.size = k
        self.front = 0
        self.rear = -1
        self.count = 0

    def enQueue(self, value):
        if self.count == self.size:
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.count == 0:
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self):
        if self.count == 0:
            return -1
        return self.queue[self.front]

    def Rear(self):
        if self.count == 0:
            return -1
        return self.queue[self.rear]

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        k = int(tokens[0])
        n = int(tokens[1])
        q = MyCircularQueue(k)
        idx = 2
        res = []
        for _ in range(n):
            op = tokens[idx]
            idx += 1
            if op == "enQueue":
                v = int(tokens[idx])
                idx += 1
                res.append(str(q.enQueue(v)))
            elif op == "deQueue":
                res.append(str(q.deQueue()))
            elif op == "Front":
                res.append(str(q.Front()))
            elif op == "Rear":
                res.append(str(q.Rear()))
        print(*res)"""
        })
    },

    # 3. Implement Stack Using Queue
    {
        "id": "dsa-queue-stack-using-queue",
        "problem_num": 108,
        "title": "Implement Stack Using Queue",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "Stack Adaptation",
        "difficulty": "EASY",
        "description": "Implement a LIFO stack using a single queue. Support push, pop, top, and empty operations.",
        "input_format": "Number of operations followed by commands ('push X', 'pop', 'top', 'empty').",
        "output_format": "Output of pop/top/empty.",
        "constraints": "1 <= operations <= 1000",
        "time_complexity": "O(N) push, O(1) pop/top",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Bloomberg", "Google"],
        "examples": [
            {"input": "4 push 10 push 20 push 30 top", "output": "30", "explanation": "Top element is 30."},
            {"input": "3 push 5 push 15 pop", "output": "15", "explanation": "Popped last pushed element 15."},
            {"input": "3 push 7 pop empty", "output": "True", "explanation": "Pushed 7, popped 7, now empty."}
        ],
        "test_cases": [
            {"input": "4 push 10 push 20 push 30 top", "expected": "30", "is_hidden": False},
            {"input": "3 push 5 push 15 pop", "expected": "15", "is_hidden": False},
            {"input": "3 push 7 pop empty", "expected": "True", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n\n// Implement Stack using Queue\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <queue>\n#include <string>\n\nusing namespace std;\n\n// Implement Stack using Queue\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "class MyStack:\n    def __init__(self):\n        pass\n    def push(self, x):\n        pass\n    def pop(self):\n        pass\n    def top(self):\n        pass\n    def empty(self):\n        pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define MAX 10005

typedef struct {
    int q[MAX];
    int front;
    int rear;
} MyStack;

void init(MyStack *s) {
    s->front = 0;
    s->rear = 0;
}

void push(MyStack *s, int x) {
    s->q[s->rear++] = x;
    int sz = s->rear - s->front;
    for (int i = 0; i < sz - 1; i++) {
        s->q[s->rear++] = s->q[s->front++];
    }
}

int pop(MyStack *s) {
    if (s->front == s->rear) return -1;
    return s->q[s->front++];
}

int top(MyStack *s) {
    if (s->front == s->rear) return -1;
    return s->q[s->front];
}

bool empty(MyStack *s) {
    return s->front == s->rear;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    MyStack s;
    init(&s);
    for (int i = 0; i < n; i++) {
        char op[20];
        scanf("%s", op);
        if (strcmp(op, "push") == 0) {
            int x; scanf("%d", &x);
            push(&s, x);
        } else if (strcmp(op, "pop") == 0) {
            int val = pop(&s);
            if (i == n - 1) printf("%d\\n", val);
        } else if (strcmp(op, "top") == 0) {
            printf("%d\\n", top(&s));
        } else if (strcmp(op, "empty") == 0) {
            printf("%s\\n", empty(&s) ? "True" : "False");
        }
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <queue>
#include <string>

using namespace std;

class MyStack {
    queue<int> q;
public:
    void push(int x) {
        q.push(x);
        int sz = q.size();
        for (int i = 0; i < sz - 1; i++) {
            q.push(q.front());
            q.pop();
        }
    }

    int pop() {
        if (q.empty()) return -1;
        int val = q.front();
        q.pop();
        return val;
    }

    int top() {
        if (q.empty()) return -1;
        return q.front();
    }

    bool empty() {
        return q.empty();
    }
};

int main() {
    int n;
    if (!(cin >> n)) return 0;
    MyStack s;
    for (int i = 0; i < n; i++) {
        string op; cin >> op;
        if (op == "push") {
            int x; cin >> x;
            s.push(x);
        } else if (op == "pop") {
            int val = s.pop();
            if (i == n - 1) cout << val << "\\n";
        } else if (op == "top") {
            cout << s.top() << "\\n";
        } else if (op == "empty") {
            cout << (s.empty() ? "True" : "False") << "\\n";
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

class MyStack {
    private Queue<Integer> q = new LinkedList<>();

    public void push(int x) {
        q.add(x);
        int sz = q.size();
        for (int i = 0; i < sz - 1; i++) {
            q.add(q.remove());
        }
    }

    public int pop() {
        if (q.isEmpty()) return -1;
        return q.remove();
    }

    public int top() {
        if (q.isEmpty()) return -1;
        return q.peek();
    }

    public boolean empty() {
        return q.isEmpty();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        MyStack s = new MyStack();
        for (int i = 0; i < n; i++) {
            String op = sc.next();
            if (op.equals("push")) {
                int x = sc.nextInt();
                s.push(x);
            } else if (op.equals("pop")) {
                int val = s.pop();
                if (i == n - 1) System.out.println(val);
            } else if (op.equals("top")) {
                System.out.println(s.top());
            } else if (op.equals("empty")) {
                System.out.println(s.empty() ? "True" : "False");
            }
        }
    }
}""",
            "python": """import sys
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if not self.queue:
            return -1
        return self.queue.popleft()

    def top(self):
        if not self.queue:
            return -1
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        s = MyStack()
        idx = 1
        for i in range(n):
            op = tokens[idx]
            idx += 1
            if op == "push":
                x = int(tokens[idx])
                idx += 1
                s.push(x)
            elif op == "pop":
                val = s.pop()
                if i == n - 1:
                    print(val)
            elif op == "top":
                print(s.top())
            elif op == "empty":
                print(s.empty())"""
        })
    },

    # 4. Generate Binary Numbers from 1 to N
    {
        "id": "dsa-queue-generate-binary",
        "problem_num": 109,
        "title": "Generate Binary Numbers from 1 to N",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "BFS Sequence Generation",
        "difficulty": "EASY",
        "description": "Given an integer N, generate binary representations of all numbers from 1 to N using a queue.",
        "input_format": "A single integer N.",
        "output_format": "Space-separated binary representations from 1 to N.",
        "constraints": "1 <= N <= 10^4",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Paytm", "Samsung"],
        "examples": [
            {"input": "1", "output": "1", "explanation": "1 in binary is 1."},
            {"input": "3", "output": "1 10 11", "explanation": "1, 2, 3 in binary."},
            {"input": "5", "output": "1 10 11 100 101", "explanation": "First 5 binary numbers."}
        ],
        "test_cases": [
            {"input": "1", "expected": "1", "is_hidden": False},
            {"input": "3", "expected": "1 10 11", "is_hidden": False},
            {"input": "5", "expected": "1 10 11 100 101", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <string.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def generateBinary(n):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

char queue[20005][50];
int front = 0;
int rear = 0;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    strcpy(queue[rear++], "1");
    for (int i = 0; i < n; i++) {
        char cur[50];
        strcpy(cur, queue[front++]);
        printf("%s%s", cur, (i == n - 1) ? "\\n" : " ");

        char s0[50], s1[50];
        sprintf(s0, "%s0", cur);
        sprintf(s1, "%s1", cur);
        strcpy(queue[rear++], s0);
        strcpy(queue[rear++], s1);
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

vector<string> generateBinary(int n) {
    queue<string> q;
    q.push("1");
    vector<string> result;
    for (int i = 0; i < n; i++) {
        string cur = q.front();
        q.pop();
        result.push_back(cur);
        q.push(cur + "0");
        q.push(cur + "1");
    }
    return result;
}

int main() {
    int n;
    if (cin >> n) {
        vector<string> res = generateBinary(n);
        for (int i = 0; i < n; i++) {
            cout << res[i] << (i == n - 1 ? "\\n" : " ");
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static List<String> generateBinary(int n) {
        Queue<String> queue = new LinkedList<>();
        queue.add("1");
        List<String> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String cur = queue.remove();
            result.add(cur);
            queue.add(cur + "0");
            queue.add(cur + "1");
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            List<String> res = generateBinary(n);
            for (int i = 0; i < res.size(); i++) {
                System.out.print(res.get(i) + (i == res.size() - 1 ? "\\n" : " "));
            }
        }
    }
}""",
            "python": """import sys
from collections import deque

def generateBinary(n):
    queue = deque(["1"])
    result = []
    for _ in range(n):
        current = queue.popleft()
        result.append(current)
        queue.append(current + "0")
        queue.append(current + "1")
    return result

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        print(*generateBinary(n))"""
        })
    },

    # 5. Reverse a Queue
    {
        "id": "dsa-queue-reverse",
        "problem_num": 110,
        "title": "Reverse a Queue",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "Queue Reversal via Stack",
        "difficulty": "EASY",
        "description": "Given a queue of integers, reverse its elements using a stack.",
        "input_format": "N followed by N integers in the queue.",
        "output_format": "Space-separated reversed queue elements.",
        "constraints": "1 <= N <= 10^5",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Flipkart", "Accenture"],
        "examples": [
            {"input": "4 1 2 3 4", "output": "4 3 2 1", "explanation": "Queue reversed."},
            {"input": "3 10 20 30", "output": "30 20 10", "explanation": "Queue reversed."},
            {"input": "1 5", "output": "5", "explanation": "Single element queue remains same."}
        ],
        "test_cases": [
            {"input": "4 1 2 3 4", "expected": "4 3 2 1", "is_hidden": False},
            {"input": "3 10 20 30", "expected": "30 20 10", "is_hidden": False},
            {"input": "1 5", "expected": "5", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <queue>\n#include <stack>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "from collections import deque\n\ndef reverseQueue(queue):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    int arr[100005];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    int stack[100005];
    int top = -1;
    for (int i = 0; i < n; i++) {
        stack[++top] = arr[i];
    }
    for (int i = 0; i < n; i++) {
        arr[i] = stack[top--];
    }
    for (int i = 0; i < n; i++) {
        printf("%d%s", arr[i], (i == n - 1) ? "\\n" : " ");
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <queue>
#include <stack>

using namespace std;

void reverseQueue(queue<int>& q) {
    stack<int> s;
    while (!q.empty()) {
        s.push(q.front());
        q.pop();
    }
    while (!s.empty()) {
        q.push(s.top());
        s.pop();
    }
}

int main() {
    int n;
    if (!(cin >> n)) return 0;
    queue<int> q;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        q.push(x);
    }
    reverseQueue(q);
    for (int i = 0; i < n; i++) {
        cout << q.front() << (i == n - 1 ? "\\n" : " ");
        q.pop();
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void reverseQueue(Queue<Integer> queue) {
        Stack<Integer> stack = new Stack<>();
        while (!queue.isEmpty()) {
            stack.push(queue.remove());
        }
        while (!stack.isEmpty()) {
            queue.add(stack.pop());
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            q.add(sc.nextInt());
        }
        reverseQueue(q);
        for (int i = 0; i < n; i++) {
            System.out.print(q.remove() + (i == n - 1 ? "\\n" : " "));
        }
    }
}""",
            "python": """import sys
from collections import deque

def reverseQueue(queue):
    stack = []
    while queue:
        stack.append(queue.popleft())
    while stack:
        queue.append(stack.pop())
    return queue

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        arr = [int(x) for x in tokens[1:1+n]]
        q = deque(arr)
        reverseQueue(q)
        print(*q)"""
        })
    },

    # 6. Implement Queue Using Two Stacks
    {
        "id": "dsa-queue-two-stacks",
        "problem_num": 111,
        "title": "Implement Queue Using Two Stacks",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "Amortized Operations",
        "difficulty": "MEDIUM",
        "description": "Implement a FIFO queue using two stacks. Support push, pop, peek, and empty operations.",
        "input_format": "Number of operations followed by commands ('push X', 'pop', 'peek', 'empty').",
        "output_format": "Output of pop/peek/empty.",
        "constraints": "1 <= operations <= 1000",
        "time_complexity": "Amortized O(1) per operation",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Microsoft", "Goldman Sachs"],
        "examples": [
            {"input": "4 push 10 push 20 push 30 pop", "output": "10", "explanation": "Popped first pushed element 10."},
            {"input": "3 push 5 push 15 peek", "output": "5", "explanation": "Peek front element is 5."},
            {"input": "3 push 7 pop empty", "output": "True", "explanation": "Queue is empty."}
        ],
        "test_cases": [
            {"input": "4 push 10 push 20 push 30 pop", "expected": "10", "is_hidden": False},
            {"input": "3 push 5 push 15 peek", "expected": "5", "is_hidden": False},
            {"input": "3 push 7 pop empty", "expected": "True", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n\n// Implement Queue using Two Stacks\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <stack>\n#include <string>\n\nusing namespace std;\n\n// Implement Queue using Two Stacks\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "class MyQueue:\n    def __init__(self):\n        pass\n    def push(self, x):\n        pass\n    def pop(self):\n        pass\n    def peek(self):\n        pass\n    def empty(self):\n        pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define MAX 10005

typedef struct {
    int s1[MAX];
    int s2[MAX];
    int top1;
    int top2;
} MyQueue;

void init(MyQueue *q) {
    q->top1 = -1;
    q->top2 = -1;
}

void push(MyQueue *q, int x) {
    q->s1[++(q->top1)] = x;
}

void move(MyQueue *q) {
    if (q->top2 == -1) {
        while (q->top1 >= 0) {
            q->s2[++(q->top2)] = q->s1[(q->top1)--];
        }
    }
}

int pop(MyQueue *q) {
    move(q);
    if (q->top2 == -1) return -1;
    return q->s2[(q->top2)--];
}

int peek(MyQueue *q) {
    move(q);
    if (q->top2 == -1) return -1;
    return q->s2[q->top2];
}

bool empty(MyQueue *q) {
    return q->top1 == -1 && q->top2 == -1;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    MyQueue q;
    init(&q);
    for (int i = 0; i < n; i++) {
        char op[20];
        scanf("%s", op);
        if (strcmp(op, "push") == 0) {
            int x; scanf("%d", &x);
            push(&q, x);
        } else if (strcmp(op, "pop") == 0) {
            int val = pop(&q);
            if (i == n - 1) printf("%d\\n", val);
        } else if (strcmp(op, "peek") == 0) {
            printf("%d\\n", peek(&q));
        } else if (strcmp(op, "empty") == 0) {
            printf("%s\\n", empty(&q) ? "True" : "False");
        }
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <stack>
#include <string>

using namespace std;

class MyQueue {
    stack<int> s1, s2;
    void move() {
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
    }
public:
    void push(int x) {
        s1.push(x);
    }
    int pop() {
        move();
        if (s2.empty()) return -1;
        int val = s2.top();
        s2.pop();
        return val;
    }
    int peek() {
        move();
        if (s2.empty()) return -1;
        return s2.top();
    }
    bool empty() {
        return s1.empty() && s2.empty();
    }
};

int main() {
    int n;
    if (!(cin >> n)) return 0;
    MyQueue q;
    for (int i = 0; i < n; i++) {
        string op; cin >> op;
        if (op == "push") {
            int x; cin >> x;
            q.push(x);
        } else if (op == "pop") {
            int val = q.pop();
            if (i == n - 1) cout << val << "\\n";
        } else if (op == "peek") {
            cout << q.peek() << "\\n";
        } else if (op == "empty") {
            cout << (q.empty() ? "True" : "False") << "\\n";
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

class MyQueue {
    private Stack<Integer> s1 = new Stack<>();
    private Stack<Integer> s2 = new Stack<>();

    public void push(int x) {
        s1.push(x);
    }

    private void move() {
        if (s2.isEmpty()) {
            while (!s1.isEmpty()) {
                s2.push(s1.pop());
            }
        }
    }

    public int pop() {
        move();
        if (s2.isEmpty()) return -1;
        return s2.pop();
    }

    public int peek() {
        move();
        if (s2.isEmpty()) return -1;
        return s2.peek();
    }

    public boolean empty() {
        return s1.isEmpty() && s2.isEmpty();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        MyQueue q = new MyQueue();
        for (int i = 0; i < n; i++) {
            String op = sc.next();
            if (op.equals("push")) {
                int x = sc.nextInt();
                q.push(x);
            } else if (op.equals("pop")) {
                int val = q.pop();
                if (i == n - 1) System.out.println(val);
            } else if (op.equals("peek")) {
                System.out.println(q.peek());
            } else if (op.equals("empty")) {
                System.out.println(q.empty() ? "True" : "False");
            }
        }
    }
}""",
            "python": """import sys

class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def move(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

    def pop(self):
        self.move()
        if not self.s2:
            return -1
        return self.s2.pop()

    def peek(self):
        self.move()
        if not self.s2:
            return -1
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        q = MyQueue()
        idx = 1
        for i in range(n):
            op = tokens[idx]
            idx += 1
            if op == "push":
                x = int(tokens[idx])
                idx += 1
                q.push(x)
            elif op == "pop":
                val = q.pop()
                if i == n - 1:
                    print(val)
            elif op == "peek":
                print(q.peek())
            elif op == "empty":
                print(q.empty())"""
        })
    },

    # 7. First Non-Repeating Character in a Stream
    {
        "id": "dsa-queue-first-non-repeating",
        "problem_num": 112,
        "title": "First Non-Repeating Character in a Stream",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "Frequency Stream Filtering",
        "difficulty": "MEDIUM",
        "description": "Given a stream of lowercase characters, find the first non-repeating character after every character is inserted. If none exists, print #.",
        "input_format": "A single string of lowercase letters.",
        "output_format": "String representing first non-repeating character at each step.",
        "constraints": "1 <= s.length <= 10^5",
        "time_complexity": "O(N)",
        "space_complexity": "O(1) (26 characters)",
        "company_tags": ["Amazon", "Flipkart", "Paytm"],
        "examples": [
            {"input": "aabc", "output": "a#bb", "explanation": "At 'a': 'a', at second 'a': '#', at 'b': 'b', at 'c': 'b'."},
            {"input": "abc", "output": "aaa", "explanation": "At each step 'a' remains the first unique."},
            {"input": "aabb", "output": "a#b#", "explanation": "Duplicates cancel unique candidates."}
        ],
        "test_cases": [
            {"input": "aabc", "expected": "a#bb", "is_hidden": False},
            {"input": "abc", "expected": "aaa", "is_hidden": False},
            {"input": "aabb", "expected": "a#b#", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <string.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n#include <queue>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def firstNonRepeating(s):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

char queue[100005];
int front = 0;
int rear = 0;
int freq[26] = {0};

int main() {
    char s[100005];
    if (scanf("%s", s) != 1) return 0;
    char res[100005];
    int len = strlen(s);

    for (int i = 0; i < len; i++) {
        char ch = s[i];
        freq[ch - 'a']++;
        queue[rear++] = ch;

        while (front < rear && freq[queue[front] - 'a'] > 1) {
            front++;
        }

        if (front < rear) {
            res[i] = queue[front];
        } else {
            res[i] = '#';
        }
    }
    res[len] = '\\0';
    printf("%s\\n", res);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <queue>
#include <vector>

using namespace std;

string firstNonRepeating(string s) {
    queue<char> q;
    vector<int> freq(26, 0);
    string result = "";

    for (char ch : s) {
        freq[ch - 'a']++;
        q.push(ch);

        while (!q.empty() && freq[q.front() - 'a'] > 1) {
            q.pop();
        }

        if (!q.empty()) result += q.front();
        else result += '#';
    }
    return result;
}

int main() {
    string s;
    if (cin >> s) {
        cout << firstNonRepeating(s) << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static String firstNonRepeating(String s) {
        Queue<Character> queue = new LinkedList<>();
        int[] freq = new int[26];
        StringBuilder result = new StringBuilder();

        for (char ch : s.toCharArray()) {
            freq[ch - 'a']++;
            queue.add(ch);

            while (!queue.isEmpty() && freq[queue.peek() - 'a'] > 1) {
                queue.remove();
            }

            if (!queue.isEmpty()) {
                result.append(queue.peek());
            } else {
                result.append('#');
            }
        }
        return result.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            System.out.println(firstNonRepeating(sc.next()));
        }
    }
}""",
            "python": """import sys
from collections import deque

def firstNonRepeating(s):
    queue = deque()
    freq = {}
    result = ""

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
        queue.append(ch)

        while queue and freq[queue[0]] > 1:
            queue.popleft()

        if queue:
            result += queue[0]
        else:
            result += '#'

    return result

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        print(firstNonRepeating(s))"""
        })
    },

    # 8. Number of Recent Calls
    {
        "id": "dsa-queue-recent-calls",
        "problem_num": 113,
        "title": "Number of Recent Calls",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "Sliding Time Window",
        "difficulty": "MEDIUM",
        "description": "Implement RecentCounter class that counts the number of requests received in the last 3000 milliseconds [t - 3000, t].",
        "input_format": "N followed by N timestamp pings in increasing order.",
        "output_format": "Space-separated count of active requests for each ping.",
        "constraints": "1 <= pings <= 10^5\n1 <= t <= 10^9",
        "time_complexity": "O(1) amortized per ping",
        "space_complexity": "O(W) where W <= 3000",
        "company_tags": ["Google", "Amazon", "Apple"],
        "examples": [
            {"input": "4 1 100 3001 3002", "output": "1 2 3 3", "explanation": "At 3002, 1 drops out of [2, 3002]."},
            {"input": "3 1 3000 3001", "output": "1 2 3", "explanation": "All three pings within 3000ms."},
            {"input": "3 100 200 4000", "output": "1 2 1", "explanation": "At 4000, 100 and 200 expire."}
        ],
        "test_cases": [
            {"input": "4 1 100 3001 3002", "expected": "1 2 3 3", "is_hidden": False},
            {"input": "3 1 3000 3001", "expected": "1 2 3", "is_hidden": False},
            {"input": "3 100 200 4000", "expected": "1 2 1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <queue>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "class RecentCounter:\n    def __init__(self):\n        pass\n    def ping(self, t):\n        pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int queue[100005];
int front = 0;
int rear = 0;

int ping(int t) {
    queue[rear++] = t;
    while (queue[front] < t - 3000) {
        front++;
    }
    return rear - front;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    for (int i = 0; i < n; i++) {
        int t; scanf("%d", &t);
        printf("%d%s", ping(t), (i == n - 1) ? "\\n" : " ");
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class RecentCounter {
    queue<int> q;
public:
    int ping(int t) {
        q.push(t);
        while (q.front() < t - 3000) {
            q.pop();
        }
        return q.size();
    }
};

int main() {
    int n;
    if (!(cin >> n)) return 0;
    RecentCounter counter;
    for (int i = 0; i < n; i++) {
        int t; cin >> t;
        cout << counter.ping(t) << (i == n - 1 ? "\\n" : " ");
    }
    return 0;
}""",
            "java": """import java.util.*;

class RecentCounter {
    private Queue<Integer> q = new LinkedList<>();

    public int ping(int t) {
        q.add(t);
        while (q.peek() < t - 3000) {
            q.remove();
        }
        return q.size();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        RecentCounter counter = new RecentCounter();
        for (int i = 0; i < n; i++) {
            System.out.print(counter.ping(sc.nextInt()) + (i == n - 1 ? "\\n" : " "));
        }
    }
}""",
            "python": """import sys
from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        counter = RecentCounter()
        res = [counter.ping(int(t)) for t in tokens[1:1+n]]
        print(*res)"""
        })
    },

    # 9. Sliding Window Maximum
    {
        "id": "dsa-queue-sliding-window-max",
        "problem_num": 114,
        "title": "Sliding Window Maximum",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "Monotonic Deque",
        "difficulty": "MEDIUM",
        "description": "Given an array and window size K, find the maximum element in every contiguous sliding window of size K.",
        "input_format": "N K followed by N space-separated integers.",
        "output_format": "Space-separated maximum values for each window.",
        "constraints": "1 <= nums.length <= 10^5\n1 <= k <= nums.length",
        "time_complexity": "O(N)",
        "space_complexity": "O(K)",
        "company_tags": ["Amazon", "Google", "Microsoft", "Uber"],
        "examples": [
            {"input": "8 3 1 3 -1 -3 5 3 6 7", "output": "3 3 5 5 6 7", "explanation": "Maximums of each window of size 3."},
            {"input": "5 2 1 2 3 4 5", "output": "2 3 4 5", "explanation": "Window size 2 maxes."},
            {"input": "4 4 4 3 2 1", "output": "4", "explanation": "Window size equals array length."}
        ],
        "test_cases": [
            {"input": "8 3 1 3 -1 -3 5 3 6 7", "expected": "3 3 5 5 6 7", "is_hidden": False},
            {"input": "5 2 1 2 3 4 5", "expected": "2 3 4 5", "is_hidden": False},
            {"input": "4 4 4 3 2 1", "expected": "4", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <deque>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def maxSlidingWindow(nums, k):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int nums[100005];
int dq[100005];
int head = 0;
int tail = 0;

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2) return 0;
    for (int i = 0; i < n; i++) scanf("%d", &nums[i]);

    int first = 1;
    for (int i = 0; i < n; i++) {
        while (head < tail && dq[head] <= i - k) {
            head++;
        }
        while (head < tail && nums[dq[tail - 1]] <= nums[i]) {
            tail--;
        }
        dq[tail++] = i;

        if (i >= k - 1) {
            if (!first) printf(" ");
            printf("%d", nums[dq[head]]);
            first = 0;
        }
    }
    printf("\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <deque>

using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<int> dq;
    vector<int> result;
    for (int i = 0; i < (int)nums.size(); i++) {
        while (!dq.empty() && dq.front() <= i - k) dq.pop_front();
        while (!dq.empty() && nums[dq.back()] <= nums[i]) dq.pop_back();
        dq.push_back(i);
        if (i >= k - 1) result.push_back(nums[dq.front()]);
    }
    return result;
}

int main() {
    int n, k;
    if (cin >> n >> k) {
        vector<int> nums(n);
        for (int i = 0; i < n; i++) cin >> nums[i];
        vector<int> res = maxSlidingWindow(nums, k);
        for (int i = 0; i < (int)res.size(); i++) {
            cout << res[i] << (i == (int)res.size() - 1 ? "\\n" : " ");
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> dq = new ArrayDeque<>();
        int n = nums.length;
        int[] result = new int[n - k + 1];
        int idx = 0;

        for (int i = 0; i < n; i++) {
            while (!dq.isEmpty() && dq.peekFirst() <= i - k) dq.pollFirst();
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();
            dq.offerLast(i);
            if (i >= k - 1) result[idx++] = nums[dq.peekFirst()];
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
        int[] res = maxSlidingWindow(nums, k);
        for (int i = 0; i < res.length; i++) {
            System.out.print(res[i] + (i == res.length - 1 ? "\\n" : " "));
        }
    }
}""",
            "python": """import sys
from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    result = []
    for i in range(len(nums)):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        k = int(tokens[1])
        arr = [int(x) for x in tokens[2:2+n]]
        print(*maxSlidingWindow(arr, k))"""
        })
    },

    # 10. First Negative Number in Every Window
    {
        "id": "dsa-queue-first-negative",
        "problem_num": 115,
        "title": "First Negative Number in Every Window",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "Window Filtering",
        "difficulty": "MEDIUM",
        "description": "Given an array of integers and a window size K, find the first negative integer in every contiguous window of size K. Return 0 if none.",
        "input_format": "N K followed by N integers.",
        "output_format": "Space-separated first negative integers for each window.",
        "constraints": "1 <= N <= 10^5\n1 <= K <= N",
        "time_complexity": "O(N)",
        "space_complexity": "O(K)",
        "company_tags": ["Amazon", "Microsoft", "Directi"],
        "examples": [
            {"input": "8 3 12 -1 -7 8 -15 30 16 28", "output": "-1 -1 -7 -15 -15 0", "explanation": "First negative in each window of 3."},
            {"input": "5 2 -1 2 3 -4 5", "output": "-1 0 -4 -4", "explanation": "Window size 2 results."},
            {"input": "4 2 1 2 3 4", "output": "0 0 0", "explanation": "No negative numbers exist."}
        ],
        "test_cases": [
            {"input": "8 3 12 -1 -7 8 -15 30 16 28", "expected": "-1 -1 -7 -15 -15 0", "is_hidden": False},
            {"input": "5 2 -1 2 3 -4 5", "expected": "-1 0 -4 -4", "is_hidden": False},
            {"input": "4 2 1 2 3 4", "expected": "0 0 0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <deque>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def firstNegative(arr, k):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int arr[100005];
int dq[100005];
int head = 0;
int tail = 0;

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2) return 0;
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    int first = 1;
    for (int i = 0; i < n; i++) {
        if (arr[i] < 0) dq[tail++] = i;
        while (head < tail && dq[head] <= i - k) head++;

        if (i >= k - 1) {
            if (!first) printf(" ");
            printf("%d", (head < tail) ? arr[dq[head]] : 0);
            first = 0;
        }
    }
    printf("\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <deque>

using namespace std;

vector<int> firstNegative(vector<int>& arr, int k) {
    deque<int> dq;
    vector<int> result;
    for (int i = 0; i < (int)arr.size(); i++) {
        if (arr[i] < 0) dq.push_back(i);
        while (!dq.empty() && dq.front() <= i - k) dq.pop_front();
        if (i >= k - 1) {
            result.push_back(!dq.empty() ? arr[dq.front()] : 0);
        }
    }
    return result;
}

int main() {
    int n, k;
    if (cin >> n >> k) {
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];
        vector<int> res = firstNegative(arr, k);
        for (int i = 0; i < (int)res.size(); i++) {
            cout << res[i] << (i == (int)res.size() - 1 ? "\\n" : " ");
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int[] firstNegative(int[] arr, int k) {
        Deque<Integer> dq = new ArrayDeque<>();
        int n = arr.length;
        int[] result = new int[n - k + 1];
        int idx = 0;

        for (int i = 0; i < n; i++) {
            if (arr[i] < 0) dq.offerLast(i);
            while (!dq.isEmpty() && dq.peekFirst() <= i - k) dq.pollFirst();
            if (i >= k - 1) {
                result[idx++] = !dq.isEmpty() ? arr[dq.peekFirst()] : 0;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int[] res = firstNegative(arr, k);
        for (int i = 0; i < res.length; i++) {
            System.out.print(res[i] + (i == res.length - 1 ? "\\n" : " "));
        }
    }
}""",
            "python": """import sys
from collections import deque

def firstNegative(arr, k):
    dq = deque()
    result = []
    for i in range(len(arr)):
        if arr[i] < 0:
            dq.append(i)
        while dq and dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(arr[dq[0]] if dq else 0)
    return result

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        k = int(tokens[1])
        arr = [int(x) for x in tokens[2:2+n]]
        print(*firstNegative(arr, k))"""
        })
    },

    # 11. Rotten Oranges
    {
        "id": "dsa-queue-rotten-oranges",
        "problem_num": 116,
        "title": "Rotten Oranges",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "Multi-Source BFS",
        "difficulty": "HARD",
        "description": "Given a grid where 0=empty, 1=fresh, 2=rotten. Every minute, rotten oranges rot 4-directionally adjacent fresh oranges. Return minimum minutes to rot all, or -1 if impossible.",
        "input_format": "rows cols followed by grid values row by row.",
        "output_format": "A single integer minutes, or -1.",
        "constraints": "1 <= rows, cols <= 100",
        "time_complexity": "O(R * C)",
        "space_complexity": "O(R * C)",
        "company_tags": ["Amazon", "Microsoft", "Google"],
        "examples": [
            {"input": "3 3 2 1 1 1 1 0 0 1 1", "output": "4", "explanation": "4 minutes to infect all fresh oranges."},
            {"input": "3 3 2 1 1 0 1 1 1 0 1", "output": "-1", "explanation": "Orange at (2,0) cannot be reached."},
            {"input": "2 2 0 2 0 0", "output": "0", "explanation": "No fresh oranges initially."}
        ],
        "test_cases": [
            {"input": "3 3 2 1 1 1 1 0 0 1 1", "expected": "4", "is_hidden": False},
            {"input": "3 3 2 1 1 0 1 1 1 0 1", "expected": "-1", "is_hidden": False},
            {"input": "2 2 0 2 0 0", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <queue>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def orangesRotting(grid):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

typedef struct { int r, c, t; } Point;
Point queue[10005];
int front = 0, rear = 0;
int grid[105][105];

int main() {
    int rows, cols;
    if (scanf("%d %d", &rows, &cols) != 2) return 0;
    int fresh = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &grid[i][j]);
            if (grid[i][j] == 2) queue[rear++] = (Point){i, j, 0};
            else if (grid[i][j] == 1) fresh++;
        }
    }

    int dr[] = {1, -1, 0, 0};
    int dc[] = {0, 0, 1, -1};
    int time = 0;

    while (front < rear) {
        Point p = queue[front++];
        if (p.t > time) time = p.t;
        for (int d = 0; d < 4; d++) {
            int nr = p.r + dr[d];
            int nc = p.c + dc[d];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                grid[nr][nc] = 2;
                fresh--;
                queue[rear++] = (Point){nr, nc, p.t + 1};
            }
        }
    }
    printf("%d\\n", fresh == 0 ? time : -1);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Point {
    int r, c, t;
    Point(int _r, int _c, int _t) : r(_r), c(_c), t(_t) {}
};

int orangesRotting(vector<vector<int> >& grid) {
    int rows = grid.size(), cols = grid[0].size();
    queue<Point> q;
    int fresh = 0;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == 2) q.push(Point(i, j, 0));
            else if (grid[i][j] == 1) fresh++;
        }
    }

    int dr[] = {1, -1, 0, 0};
    int dc[] = {0, 0, 1, -1};
    int time = 0;

    while (!q.empty()) {
        Point p = q.front();
        q.pop();
        time = max(time, p.t);

        for (int d = 0; d < 4; d++) {
            int nr = p.r + dr[d], nc = p.c + dc[d];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                grid[nr][nc] = 2;
                fresh--;
                q.push(Point(nr, nc, p.t + 1));
            }
        }
    }
    return fresh == 0 ? time : -1;
}

int main() {
    int rows, cols;
    if (cin >> rows >> cols) {
        vector<vector<int> > grid(rows, vector<int>(cols));
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) cin >> grid[i][j];
        }
        cout << orangesRotting(grid) << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int orangesRotting(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        Queue<int[]> q = new LinkedList<>();
        int fresh = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) q.add(new int[]{i, j, 0});
                else if (grid[i][j] == 1) fresh++;
            }
        }

        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};
        int time = 0;

        while (!q.isEmpty()) {
            int[] cur = q.remove();
            int r = cur[0], c = cur[1], t = cur[2];
            time = Math.max(time, t);

            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d], nc = c + dc[d];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                    grid[nr][nc] = 2;
                    fresh--;
                    q.add(new int[]{nr, nc, t + 1});
                }
            }
        }
        return fresh == 0 ? time : -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int rows = sc.nextInt(), cols = sc.nextInt();
        int[][] grid = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) grid[i][j] = sc.nextInt();
        }
        System.out.println(orangesRotting(grid));
    }
}""",
            "python": """import sys
from collections import deque

def orangesRotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    queue = deque()
    fresh = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    time = 0

    while queue:
        r, c, t = queue.popleft()
        time = max(time, t)
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, t + 1))

    return time if fresh == 0 else -1

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        rows = int(tokens[0])
        cols = int(tokens[1])
        idx = 2
        grid = []
        for _ in range(rows):
            grid.append([int(x) for x in tokens[idx:idx+cols]])
            idx += cols
        print(orangesRotting(grid))"""
        })
    },

    # 12. Shortest Path in Binary Matrix
    {
        "id": "dsa-queue-shortest-path-binary",
        "problem_num": 117,
        "title": "Shortest Path in Binary Matrix",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "8-Directional Grid BFS",
        "difficulty": "HARD",
        "description": "Find shortest 8-directional clear path (cells with value 0) from top-left (0,0) to bottom-right (N-1, N-1). Return length or -1.",
        "input_format": "N followed by N x N grid values.",
        "output_format": "A single integer length or -1.",
        "constraints": "1 <= N <= 100",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)",
        "company_tags": ["Google", "Facebook", "Amazon"],
        "examples": [
            {"input": "2 0 1 1 0", "output": "2", "explanation": "(0,0) -> (1,1) diagonal path length 2."},
            {"input": "3 0 0 0 1 1 0 1 1 0", "output": "4", "explanation": "Path of length 4."},
            {"input": "2 1 0 1 0", "output": "-1", "explanation": "Start cell is blocked."}
        ],
        "test_cases": [
            {"input": "2 0 1 1 0", "expected": "2", "is_hidden": False},
            {"input": "3 0 0 0 1 1 0 1 1 0", "expected": "4", "is_hidden": False},
            {"input": "2 1 0 1 0", "expected": "-1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <queue>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def shortestPathBinaryMatrix(grid):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

typedef struct { int r, c, dist; } Node;
Node queue[20005];
int front = 0, rear = 0;
int grid[105][105];
int visited[105][105];

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &grid[i][j]);
            visited[i][j] = 0;
        }
    }

    if (grid[0][0] != 0 || grid[n-1][n-1] != 0) {
        printf("-1\\n");
        return 0;
    }

    queue[rear++] = (Node){0, 0, 1};
    visited[0][0] = 1;

    int dr[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dc[] = {-1, 0, 1, -1, 1, -1, 0, 1};

    int ans = -1;
    while (front < rear) {
        Node cur = queue[front++];
        if (cur.r == n - 1 && cur.c == n - 1) {
            ans = cur.dist;
            break;
        }
        for (int d = 0; d < 8; d++) {
            int nr = cur.r + dr[d];
            int nc = cur.c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0 && !visited[nr][nc]) {
                visited[nr][nc] = 1;
                queue[rear++] = (Node){nr, nc, cur.dist + 1};
            }
        }
    }
    printf("%d\\n", ans);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Step {
    int r, c, dist;
    Step(int _r, int _c, int _d) : r(_r), c(_c), dist(_d) {}
};

int shortestPathBinaryMatrix(vector<vector<int> >& grid) {
    int n = grid.size();
    if (grid[0][0] != 0 || grid[n-1][n-1] != 0) return -1;

    queue<Step> q;
    q.push(Step(0, 0, 1));
    vector<vector<bool> > visited(n, vector<bool>(n, false));
    visited[0][0] = true;

    int dr[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dc[] = {-1, 0, 1, -1, 1, -1, 0, 1};

    while (!q.empty()) {
        Step s = q.front();
        q.pop();
        if (s.r == n - 1 && s.c == n - 1) return s.dist;

        for (int d = 0; d < 8; d++) {
            int nr = s.r + dr[d], nc = s.c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0 && !visited[nr][nc]) {
                visited[nr][nc] = true;
                q.push(Step(nr, nc, s.dist + 1));
            }
        }
    }
    return -1;
}

int main() {
    int n;
    if (cin >> n) {
        vector<vector<int> > grid(n, vector<int>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) cin >> grid[i][j];
        }
        cout << shortestPathBinaryMatrix(grid) << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] != 0 || grid[n-1][n-1] != 0) return -1;

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0, 1});
        boolean[][] visited = new boolean[n][n];
        visited[0][0] = true;

        int[] dr = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dc = {-1, 0, 1, -1, 1, -1, 0, 1};

        while (!q.isEmpty()) {
            int[] cur = q.remove();
            int r = cur[0], c = cur[1], dist = cur[2];
            if (r == n - 1 && c == n - 1) return dist;

            for (int d = 0; d < 8; d++) {
                int nr = r + dr[d], nc = c + dc[d];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0 && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    q.add(new int[]{nr, nc, dist + 1});
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) grid[i][j] = sc.nextInt();
        }
        System.out.println(shortestPathBinaryMatrix(grid));
    }
}""",
            "python": """import sys
from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1

    queue = deque([(0, 0, 1)])
    visited = {(0, 0)}

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    while queue:
        r, c, dist = queue.popleft()
        if r == n - 1 and c == n - 1:
            return dist

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        idx = 1
        grid = []
        for _ in range(n):
            grid.append([int(x) for x in tokens[idx:idx+n]])
            idx += n
        print(shortestPathBinaryMatrix(grid))"""
        })
    },

    # 13. Perfect Squares
    {
        "id": "dsa-queue-perfect-squares",
        "problem_num": 118,
        "title": "Perfect Squares",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "BFS Shortest State Path",
        "difficulty": "HARD",
        "description": "Given a positive integer N, find the minimum number of perfect square numbers whose sum equals N using BFS.",
        "input_format": "A single integer N.",
        "output_format": "A single integer minimum steps.",
        "constraints": "1 <= N <= 10^4",
        "time_complexity": "O(N * sqrt(N))",
        "space_complexity": "O(N)",
        "company_tags": ["Google", "Amazon", "Microsoft"],
        "examples": [
            {"input": "12", "output": "3", "explanation": "4 + 4 + 4 = 12 (3 squares)."},
            {"input": "13", "output": "2", "explanation": "4 + 9 = 13 (2 squares)."},
            {"input": "1", "output": "1", "explanation": "1 is a perfect square."}
        ],
        "test_cases": [
            {"input": "12", "expected": "3", "is_hidden": False},
            {"input": "13", "expected": "2", "is_hidden": False},
            {"input": "1", "expected": "1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <queue>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def numSquares(n):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <math.h>

typedef struct { int rem, steps; } Node;
Node queue[20005];
int front = 0, rear = 0;
int visited[10005] = {0};

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;

    int squares[105];
    int num_sq = 0;
    for (int i = 1; i * i <= n; i++) squares[num_sq++] = i * i;

    queue[rear++] = (Node){n, 0};
    visited[n] = 1;

    while (front < rear) {
        Node cur = queue[front++];
        if (cur.rem == 0) {
            printf("%d\\n", cur.steps);
            return 0;
        }
        for (int i = 0; i < num_sq; i++) {
            int next_val = cur.rem - squares[i];
            if (next_val >= 0 && !visited[next_val]) {
                visited[next_val] = 1;
                queue[rear++] = (Node){next_val, cur.steps + 1};
            }
        }
    }
    printf("-1\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <queue>
#include <vector>
#include <cmath>

using namespace std;

int numSquares(int n) {
    queue<pair<int, int> > q;
    q.push(make_pair(n, 0));
    vector<bool> visited(n + 1, false);
    visited[n] = true;

    vector<int> squares;
    for (int i = 1; i * i <= n; i++) squares.push_back(i * i);

    while (!q.empty()) {
        pair<int, int> p = q.front();
        q.pop();
        int rem = p.first, steps = p.second;
        if (rem == 0) return steps;

        for (int sq : squares) {
            int next_val = rem - sq;
            if (next_val >= 0 && !visited[next_val]) {
                visited[next_val] = true;
                q.push(make_pair(next_val, steps + 1));
            }
        }
    }
    return -1;
}

int main() {
    int n;
    if (cin >> n) {
        cout << numSquares(n) << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int numSquares(int n) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{n, 0});
        boolean[] visited = new boolean[n + 1];
        visited[n] = true;

        List<Integer> squares = new ArrayList<>();
        for (int i = 1; i * i <= n; i++) squares.add(i * i);

        while (!queue.isEmpty()) {
            int[] cur = queue.remove();
            int rem = cur[0], steps = cur[1];
            if (rem == 0) return steps;

            for (int sq : squares) {
                int nextVal = rem - sq;
                if (nextVal >= 0 && !visited[nextVal]) {
                    visited[nextVal] = true;
                    queue.add(new int[]{nextVal, steps + 1});
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            System.out.println(numSquares(sc.nextInt()));
        }
    }
}""",
            "python": """import sys
from collections import deque
from math import isqrt

def numSquares(n):
    queue = deque([(n, 0)])
    visited = {n}
    squares = [i * i for i in range(1, isqrt(n) + 1)]

    while queue:
        remaining, steps = queue.popleft()
        if remaining == 0:
            return steps
        for square in squares:
            next_value = remaining - square
            if next_value >= 0 and next_value not in visited:
                visited.add(next_value)
                queue.append((next_value, steps + 1))
    return -1

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        print(numSquares(n))"""
        })
    },

    # 14. Open the Lock
    {
        "id": "dsa-queue-open-lock",
        "problem_num": 119,
        "title": "Open the Lock",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "State Graph BFS",
        "difficulty": "HARD",
        "description": "Given a 4-wheel lock (each 0-9), dead-end combinations, and target code. Find minimum rotations from '0000' to target without hitting dead ends. Return -1 if impossible.",
        "input_format": "Number of deadends, list of deadends, target string.",
        "output_format": "A single integer moves or -1.",
        "constraints": "1 <= deadends.length <= 500\ntarget != '0000'",
        "time_complexity": "O(10^4)",
        "space_complexity": "O(10^4)",
        "company_tags": ["Google", "Amazon", "Facebook"],
        "examples": [
            {"input": "5 0201 0101 0102 1212 2002 0202", "output": "6", "explanation": "Shortest valid sequence takes 6 moves."},
            {"input": "1 8888 0009", "output": "1", "explanation": "Turn last digit from 0 to 9 in 1 move."},
            {"input": "8 8887 8889 8878 8898 8788 8988 7888 9888 8888", "output": "-1", "explanation": "Target blocked by deadends."}
        ],
        "test_cases": [
            {"input": "5 0201 0101 0102 1212 2002 0202", "expected": "6", "is_hidden": False},
            {"input": "1 8888 0009", "expected": "1", "is_hidden": False},
            {"input": "8 8887 8889 8878 8898 8788 8988 7888 9888 8888", "expected": "-1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <queue>\n#include <unordered_set>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def openLock(deadends, target):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

int dead[10000] = {0};
int visited[10000] = {0};
int queue[10000];
int steps_arr[10000];
int front = 0, rear = 0;

int to_code(int d0, int d1, int d2, int d3) {
    return d0 * 1000 + d1 * 100 + d2 * 10 + d3;
}

int main() {
    int m;
    if (scanf("%d", &m) != 1) return 0;
    for (int i = 0; i < m; i++) {
        char s[10]; scanf("%s", s);
        int val = (s[0]-'0')*1000 + (s[1]-'0')*100 + (s[2]-'0')*10 + (s[3]-'0');
        dead[val] = 1;
    }
    char target_str[10];
    scanf("%s", target_str);
    int target = (target_str[0]-'0')*1000 + (target_str[1]-'0')*100 + (target_str[2]-'0')*10 + (target_str[3]-'0');

    if (dead[0]) {
        printf("-1\\n");
        return 0;
    }

    queue[rear] = 0;
    steps_arr[rear++] = 0;
    visited[0] = 1;

    while (front < rear) {
        int cur = queue[front];
        int st = steps_arr[front++];
        if (cur == target) {
            printf("%d\\n", st);
            return 0;
        }

        int d[4];
        d[0] = cur / 1000;
        d[1] = (cur / 100) % 10;
        d[2] = (cur / 10) % 10;
        d[3] = cur % 10;

        for (int i = 0; i < 4; i++) {
            int orig = d[i];
            int opts[2] = {(orig + 1) % 10, (orig + 9) % 10};
            for (int k = 0; k < 2; k++) {
                d[i] = opts[k];
                int next_code = to_code(d[0], d[1], d[2], d[3]);
                if (!dead[next_code] && !visited[next_code]) {
                    visited[next_code] = 1;
                    queue[rear] = next_code;
                    steps_arr[rear++] = st + 1;
                }
            }
            d[i] = orig;
        }
    }
    printf("-1\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

int openLock(vector<string>& deadends, string target) {
    unordered_set<string> dead(deadends.begin(), deadends.end());
    if (dead.count("0000")) return -1;

    queue<pair<string, int> > q;
    q.push(make_pair("0000", 0));
    unordered_set<string> visited;
    visited.insert("0000");

    while (!q.empty()) {
        pair<string, int> p = q.front();
        q.pop();
        string cur = p.first;
        int steps = p.second;
        if (cur == target) return steps;

        for (int i = 0; i < 4; i++) {
            int d = cur[i] - '0';
            int changes[] = {-1, 1};
            for (int c = 0; c < 2; c++) {
                int next_d = (d + changes[c] + 10) % 10;
                string next_s = cur;
                next_s[i] = next_d + '0';
                if (!dead.count(next_s) && !visited.count(next_s)) {
                    visited.insert(next_s);
                    q.push(make_pair(next_s, steps + 1));
                }
            }
        }
    }
    return -1;
}

int main() {
    int m;
    if (cin >> m) {
        vector<string> deadends(m);
        for (int i = 0; i < m; i++) cin >> deadends[i];
        string target; cin >> target;
        cout << openLock(deadends, target) << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int openLock(String[] deadends, String target) {
        Set<String> dead = new HashSet<>(Arrays.asList(deadends));
        if (dead.contains("0000")) return -1;

        Queue<String> queue = new LinkedList<>();
        Queue<Integer> steps = new LinkedList<>();
        queue.add("0000");
        steps.add(0);

        Set<String> visited = new HashSet<>();
        visited.add("0000");

        while (!queue.isEmpty()) {
            String cur = queue.remove();
            int st = steps.remove();
            if (cur.equals(target)) return st;

            char[] chars = cur.toCharArray();
            for (int i = 0; i < 4; i++) {
                char orig = chars[i];
                for (int change : new int[]{-1, 1}) {
                    int nextD = (orig - '0' + change + 10) % 10;
                    chars[i] = (char) ('0' + nextD);
                    String nextS = new String(chars);
                    if (!dead.contains(nextS) && !visited.contains(nextS)) {
                        visited.add(nextS);
                        queue.add(nextS);
                        steps.add(st + 1);
                    }
                }
                chars[i] = orig;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int m = sc.nextInt();
        String[] deadends = new String[m];
        for (int i = 0; i < m; i++) deadends[i] = sc.next();
        String target = sc.next();
        System.out.println(openLock(deadends, target));
    }
}""",
            "python": """import sys
from collections import deque

def openLock(deadends, target):
    dead = set(deadends)
    if "0000" in dead:
        return -1

    queue = deque([("0000", 0)])
    visited = {"0000"}

    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps

        for i in range(4):
            digit = int(current[i])
            for change in (-1, 1):
                new_digit = (digit + change) % 10
                next_state = current[:i] + str(new_digit) + current[i+1:]
                if next_state not in dead and next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, steps + 1))
    return -1

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        m = int(tokens[0])
        deadends = tokens[1:1+m]
        target = tokens[1+m]
        print(openLock(deadends, target))"""
        })
    },

    # 15. Sliding Puzzle
    {
        "id": "dsa-queue-sliding-puzzle",
        "problem_num": 120,
        "title": "Sliding Puzzle",
        "category": "Queue",
        "topic": "Queue",
        "subtopic": "Permutation BFS",
        "difficulty": "HARD",
        "description": "On a 2x3 board with numbers 0 to 5, find minimum swaps of 0 with adjacent cells to reach [[1,2,3],[4,5,0]]. Return -1 if impossible.",
        "input_format": "6 integers representing the 2x3 board.",
        "output_format": "A single integer minimum moves or -1.",
        "constraints": "board is a permutation of [0, 1, 2, 3, 4, 5]",
        "time_complexity": "O(6!) = O(720)",
        "space_complexity": "O(6!) = O(720)",
        "company_tags": ["Google", "Airbnb", "Amazon"],
        "examples": [
            {"input": "1 2 3 4 0 5", "output": "1", "explanation": "Swap 0 and 5 in 1 move."},
            {"input": "1 2 3 5 4 0", "output": "-1", "explanation": "Target permutation cannot be reached."},
            {"input": "4 1 2 5 0 3", "output": "5", "explanation": "Takes 5 swaps."}
        ],
        "test_cases": [
            {"input": "1 2 3 4 0 5", "expected": "1", "is_hidden": False},
            {"input": "1 2 3 5 4 0", "expected": "-1", "is_hidden": False},
            {"input": "4 1 2 5 0 3", "expected": "5", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <queue>\n#include <unordered_set>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def slidingPuzzle(board):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

char queue[1000][10];
int steps[1000];
int front = 0, rear = 0;
char visited[1000][10];
int v_count = 0;

int is_visited(char *s) {
    for (int i = 0; i < v_count; i++) {
        if (strcmp(visited[i], s) == 0) return 1;
    }
    return 0;
}

int main() {
    char start[10] = "";
    for (int i = 0; i < 6; i++) {
        int x; scanf("%d", &x);
        char ch[2] = { (char)('0' + x), '\\0' };
        strcat(start, ch);
    }

    int adj[6][3] = {
        {1, 3, -1},
        {0, 2, 4},
        {1, 5, -1},
        {0, 4, -1},
        {1, 3, 5},
        {2, 4, -1}
    };

    strcpy(queue[rear], start);
    steps[rear++] = 0;
    strcpy(visited[v_count++], start);

    while (front < rear) {
        char cur[10];
        strcpy(cur, queue[front]);
        int st = steps[front++];

        if (strcmp(cur, "123450") == 0) {
            printf("%d\\n", st);
            return 0;
        }

        int zero = 0;
        for (int i = 0; i < 6; i++) if (cur[i] == '0') { zero = i; break; }

        for (int k = 0; k < 3; k++) {
            int next_pos = adj[zero][k];
            if (next_pos == -1) continue;

            char next_s[10];
            strcpy(next_s, cur);
            next_s[zero] = next_s[next_pos];
            next_s[next_pos] = '0';

            if (!is_visited(next_s)) {
                strcpy(visited[v_count++], next_s);
                strcpy(queue[rear], next_s);
                steps[rear++] = st + 1;
            }
        }
    }
    printf("-1\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>
#include <algorithm>

using namespace std;

int slidingPuzzle(vector<vector<int> >& board) {
    string start = "";
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) start += to_string(board[i][j]);
    }
    string target = "123450";

    int adj[6][3] = {
        {1, 3, -1},
        {0, 2, 4},
        {1, 5, -1},
        {0, 4, -1},
        {1, 3, 5},
        {2, 4, -1}
    };

    queue<pair<string, int> > q;
    q.push(make_pair(start, 0));
    unordered_set<string> visited;
    visited.insert(start);

    while (!q.empty()) {
        pair<string, int> p = q.front();
        q.pop();
        string state = p.first;
        int steps = p.second;
        if (state == target) return steps;

        int zero = state.find('0');
        for (int k = 0; k < 3; k++) {
            int next_pos = adj[zero][k];
            if (next_pos == -1) continue;

            string next_state = state;
            swap(next_state[zero], next_state[next_pos]);
            if (!visited.count(next_state)) {
                visited.insert(next_state);
                q.push(make_pair(next_state, steps + 1));
            }
        }
    }
    return -1;
}

int main() {
    vector<vector<int> > board(2, vector<int>(3));
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) cin >> board[i][j];
    }
    cout << slidingPuzzle(board) << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int slidingPuzzle(int[][] board) {
        StringBuilder start = new StringBuilder();
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 3; j++) start.append(board[i][j]);
        }
        String target = "123450";

        int[][] neighbors = {
            {1, 3},
            {0, 2, 4},
            {1, 5},
            {0, 4},
            {1, 3, 5},
            {2, 4}
        };

        Queue<String> queue = new LinkedList<>();
        Queue<Integer> steps = new LinkedList<>();
        queue.add(start.toString());
        steps.add(0);

        Set<String> visited = new HashSet<>();
        visited.add(start.toString());

        while (!queue.isEmpty()) {
            String state = queue.remove();
            int st = steps.remove();
            if (state.equals(target)) return st;

            int zero = state.indexOf('0');
            for (int nextPos : neighbors[zero]) {
                char[] chars = state.toCharArray();
                chars[zero] = chars[nextPos];
                chars[nextPos] = '0';
                String nextState = new String(chars);

                if (!visited.contains(nextState)) {
                    visited.add(nextState);
                    queue.add(nextState);
                    steps.add(st + 1);
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] board = new int[2][3];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 3; j++) board[i][j] = sc.nextInt();
        }
        System.out.println(slidingPuzzle(board));
    }
}""",
            "python": """import sys
from collections import deque

def slidingPuzzle(board):
    start = ''.join(str(x) for row in board for x in row)
    target = "123450"

    neighbors = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4],
        4: [1, 3, 5],
        5: [2, 4]
    }

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, steps = queue.popleft()
        if state == target:
            return steps
        zero = state.index('0')
        for next_pos in neighbors[zero]:
            chars = list(state)
            chars[zero], chars[next_pos] = chars[next_pos], chars[zero]
            new_state = ''.join(chars)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, steps + 1))
    return -1

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        board = [
            [int(tokens[0]), int(tokens[1]), int(tokens[2])],
            [int(tokens[3]), int(tokens[4]), int(tokens[5])]
        ]
        print(slidingPuzzle(board))"""
        })
    }
]

problems.extend(queue_data)

with open("backend/app/data/dsa_problems_seed.json", "w", encoding="utf-8") as f:
    json.dump(problems, f, indent=2)

print(f"Successfully added 15 Queue problems! Total problems now: {len(problems)}")
