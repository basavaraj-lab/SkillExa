import sys, os
sys.path.insert(0, os.path.abspath('.'))
import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    problems = json.load(f)

# Filter out if any exist
stack_ids = {
    "dsa-stack-array", "dsa-stack-linked-list", "dsa-stack-valid-parentheses",
    "dsa-stack-reverse-string", "dsa-stack-remove-duplicates", "dsa-stack-min-stack",
    "dsa-stack-next-greater", "dsa-stack-eval-rpn", "dsa-stack-daily-temperatures",
    "dsa-stack-decode-string", "dsa-stack-largest-rectangle", "dsa-stack-maximal-rectangle",
    "dsa-stack-basic-calculator", "dsa-stack-trapping-rain-water", "dsa-stack-sum-subarray-mins"
}
problems = [p for p in problems if p["id"] not in stack_ids]

stack_data = [
    # 1. Implement Stack Using Array
    {
        "id": "dsa-stack-array",
        "problem_num": 91,
        "title": "Implement Stack Using Array",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "Array Implementation",
        "difficulty": "EASY",
        "description": "Implement a stack using an array with push, pop, peek, and isEmpty operations.",
        "input_format": "Number of operations followed by the operations (e.g., '3 push 10 push 20 peek').",
        "output_format": "The output of peek/pop/isEmpty operation.",
        "constraints": "1 <= number of operations <= 1000\n-10^4 <= value <= 10^4",
        "time_complexity": "O(1) per operation",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Microsoft", "TCS", "Infosys"],
        "examples": [
            {"input": "3 push 10 push 20 peek", "output": "20", "explanation": "Pushed 10, 20. Peek returns 20."},
            {"input": "2 push 5 pop", "output": "5", "explanation": "Pushed 5. Pop returns 5."},
            {"input": "1 isEmpty", "output": "True", "explanation": "Stack has no elements."}
        ],
        "test_cases": [
            {"input": "3 push 10 push 20 peek", "expected": "20", "is_hidden": False},
            {"input": "2 push 5 pop", "expected": "5", "is_hidden": False},
            {"input": "1 isEmpty", "expected": "True", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\n// Implement Stack using array\n\nint main() {\n    // Your code here\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\n// Implement Stack using array\n\nint main() {\n    // Your code here\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // Your code here\n    }\n}",
            "python": "class Stack:\n    def __init__(self):\n        self.stack = []\n\n    def push(self, x):\n        pass\n\n    def pop(self):\n        pass\n\n    def peek(self):\n        pass\n\n    def isEmpty(self):\n        pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX 10000

typedef struct {
    int arr[MAX];
    int top;
} Stack;

void init(Stack *s) {
    s->top = -1;
}

void push(Stack *s, int x) {
    s->arr[++(s->top)] = x;
}

int pop(Stack *s) {
    if (s->top == -1) return -1;
    return s->arr[(s->top)--];
}

int peek(Stack *s) {
    if (s->top == -1) return -1;
    return s->arr[s->top];
}

bool isEmpty(Stack *s) {
    return s->top == -1;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    Stack s;
    init(&s);
    for (int i = 0; i < n; i++) {
        char op[20];
        scanf("%s", op);
        if (strcmp(op, "push") == 0) {
            int x; scanf("%d", &x);
            push(&s, x);
        } else if (strcmp(op, "pop") == 0) {
            printf("%d\\n", pop(&s));
        } else if (strcmp(op, "peek") == 0) {
            printf("%d\\n", peek(&s));
        } else if (strcmp(op, "isEmpty") == 0) {
            printf("%s\\n", isEmpty(&s) ? "True" : "False");
        }
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Stack {
    vector<int> stack;
public:
    void push(int x) {
        stack.push_back(x);
    }
    int pop() {
        if (stack.empty()) return -1;
        int val = stack.back();
        stack.pop_back();
        return val;
    }
    int peek() {
        if (stack.empty()) return -1;
        return stack.back();
    }
    bool isEmpty() {
        return stack.empty();
    }
};

int main() {
    int n;
    if (!(cin >> n)) return 0;
    Stack s;
    for (int i = 0; i < n; i++) {
        string op; cin >> op;
        if (op == "push") {
            int x; cin >> x;
            s.push(x);
        } else if (op == "pop") {
            cout << s.pop() << "\\n";
        } else if (op == "peek") {
            cout << s.peek() << "\\n";
        } else if (op == "isEmpty") {
            cout << (s.isEmpty() ? "True" : "False") << "\\n";
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

class Stack {
    private List<Integer> stack = new ArrayList<>();

    public void push(int x) {
        stack.add(x);
    }

    public int pop() {
        if (stack.isEmpty()) return -1;
        return stack.remove(stack.size() - 1);
    }

    public int peek() {
        if (stack.isEmpty()) return -1;
        return stack.get(stack.size() - 1);
    }

    public boolean isEmpty() {
        return stack.isEmpty();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        Stack s = new Stack();
        for (int i = 0; i < n; i++) {
            String op = sc.next();
            if (op.equals("push")) {
                int x = sc.nextInt();
                s.push(x);
            } else if (op.equals("pop")) {
                System.out.println(s.pop());
            } else if (op.equals("peek")) {
                System.out.println(s.peek());
            } else if (op.equals("isEmpty")) {
                System.out.println(s.isEmpty() ? "True" : "False");
            }
        }
    }
}""",
            "python": """import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            return -1
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        s = Stack()
        idx = 1
        for _ in range(n):
            op = tokens[idx]
            idx += 1
            if op == "push":
                x = int(tokens[idx])
                idx += 1
                s.push(x)
            elif op == "pop":
                print(s.pop())
            elif op == "peek":
                print(s.peek())
            elif op == "isEmpty":
                print(s.isEmpty())"""
        })
    },

    # 2. Implement Stack Using Linked List
    {
        "id": "dsa-stack-linked-list",
        "problem_num": 92,
        "title": "Implement Stack Using Linked List",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "Linked List Implementation",
        "difficulty": "EASY",
        "description": "Implement a stack using a singly linked list. Support push, pop, and peek operations.",
        "input_format": "Number of operations followed by operation commands.",
        "output_format": "Value output of operation.",
        "constraints": "1 <= operations <= 1000",
        "time_complexity": "O(1) per operation",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Microsoft", "Wipro"],
        "examples": [
            {"input": "3 push 10 push 20 pop", "output": "20", "explanation": "Popped top element 20."},
            {"input": "3 push 5 push 15 peek", "output": "15", "explanation": "Peek returns top element 15."},
            {"input": "1 pop", "output": "-1", "explanation": "Empty stack pop returns -1."}
        ],
        "test_cases": [
            {"input": "3 push 10 push 20 pop", "expected": "20", "is_hidden": False},
            {"input": "3 push 5 push 15 peek", "expected": "15", "is_hidden": False},
            {"input": "1 pop", "expected": "-1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\n// Implement Stack using Linked List",
            "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\n// Implement Stack using Linked List",
            "java": "import java.util.*;\n\npublic class Main {\n    // Implement Stack using Linked List\n}",
            "python": "class Node:\n    def __init__(self, data):\n        self.data = data\n        self.next = None\n\nclass Stack:\n    def __init__(self):\n        self.top = None\n\n    def push(self, x):\n        pass\n\n    def pop(self):\n        pass\n\n    def peek(self):\n        pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node {
    int data;
    struct Node* next;
};

typedef struct {
    struct Node* top;
} Stack;

void init(Stack *s) {
    s->top = NULL;
}

void push(Stack *s, int x) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = x;
    new_node->next = s->top;
    s->top = new_node;
}

int pop(Stack *s) {
    if (s->top == NULL) return -1;
    struct Node* temp = s->top;
    int val = temp->data;
    s->top = s->top->next;
    free(temp);
    return val;
}

int peek(Stack *s) {
    if (s->top == NULL) return -1;
    return s->top->data;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    Stack s;
    init(&s);
    for (int i = 0; i < n; i++) {
        char op[20];
        scanf("%s", op);
        if (strcmp(op, "push") == 0) {
            int x; scanf("%d", &x);
            push(&s, x);
        } else if (strcmp(op, "pop") == 0) {
            printf("%d\\n", pop(&s));
        } else if (strcmp(op, "peek") == 0) {
            printf("%d\\n", peek(&s));
        }
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int d) : data(d), next(nullptr) {}
};

class Stack {
    Node* topNode;
public:
    Stack() : topNode(nullptr) {}

    void push(int x) {
        Node* new_node = new Node(x);
        new_node->next = topNode;
        topNode = new_node;
    }

    int pop() {
        if (topNode == nullptr) return -1;
        int val = topNode->data;
        Node* temp = topNode;
        topNode = topNode->next;
        delete temp;
        return val;
    }

    int peek() {
        if (topNode == nullptr) return -1;
        return topNode->data;
    }
};

int main() {
    int n;
    if (!(cin >> n)) return 0;
    Stack s;
    for (int i = 0; i < n; i++) {
        string op; cin >> op;
        if (op == "push") {
            int x; cin >> x;
            s.push(x);
        } else if (op == "pop") {
            cout << s.pop() << "\\n";
        } else if (op == "peek") {
            cout << s.peek() << "\\n";
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

class Node {
    int data;
    Node next;
    Node(int d) { data = d; }
}

class Stack {
    Node top = null;

    public void push(int x) {
        Node newNode = new Node(x);
        newNode.next = top;
        top = newNode;
    }

    public int pop() {
        if (top == null) return -1;
        int val = top.data;
        top = top.next;
        return val;
    }

    public int peek() {
        if (top == null) return -1;
        return top.data;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        Stack s = new Stack();
        for (int i = 0; i < n; i++) {
            String op = sc.next();
            if (op.equals("push")) {
                int x = sc.nextInt();
                s.push(x);
            } else if (op.equals("pop")) {
                System.out.println(s.pop());
            } else if (op.equals("peek")) {
                System.out.println(s.peek());
            }
        }
    }
}""",
            "python": """import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return -1
        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            return -1
        return self.top.data

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        s = Stack()
        idx = 1
        for _ in range(n):
            op = tokens[idx]
            idx += 1
            if op == "push":
                x = int(tokens[idx])
                idx += 1
                s.push(x)
            elif op == "pop":
                print(s.pop())
            elif op == "peek":
                print(s.peek())"""
        })
    },

    # 3. Valid Parentheses
    {
        "id": "dsa-stack-valid-parentheses",
        "problem_num": 93,
        "title": "Valid Parentheses",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "Matching & Balance",
        "difficulty": "EASY",
        "description": "Given a string containing '(', ')', '{', '}', '[' and ']', determine whether the brackets are balanced.",
        "input_format": "A single line containing the bracket string.",
        "output_format": "True if balanced, else False.",
        "constraints": "1 <= s.length <= 10^4",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Google", "Facebook", "Microsoft"],
        "examples": [
            {"input": "()", "output": "True", "explanation": "Simple pair matching."},
            {"input": "({[]})", "output": "True", "explanation": "Properly nested pairs."},
            {"input": "([)]", "output": "False", "explanation": "Mismatched closing order."}
        ],
        "test_cases": [
            {"input": "()", "expected": "True", "is_hidden": False},
            {"input": "({[]})", "expected": "True", "is_hidden": False},
            {"input": "([)]", "expected": "False", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n\nbool isValid(char* s) {\n    // Your code here\n    return false;\n}\n\nint main() {\n    char s[100005];\n    if (scanf(\"%s\", s) == 1) {\n        printf(\"%s\\n\", isValid(s) ? \"True\" : \"False\");\n    }\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nbool isValid(string s) {\n    // Your code here\n    return false;\n}\n\nint main() {\n    string s;\n    if (cin >> s) cout << (isValid(s) ? \"True\" : \"False\") << \"\\n\";\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static boolean isValid(String s) {\n        // Your code here\n        return false;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) System.out.println(isValid(sc.next()) ? \"True\" : \"False\");\n    }\n}",
            "python": "def isValid(s):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    import sys\n    s = sys.stdin.read().strip()\n    if s: print(isValid(s))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isValid(char* s) {
    int n = strlen(s);
    char stack[100005];
    int top = -1;

    for (int i = 0; i < n; i++) {
        char ch = s[i];
        if (ch == '(' || ch == '{' || ch == '[') {
            stack[++top] = ch;
        } else {
            if (top == -1) return false;
            char expected = ' ';
            if (ch == ')') expected = '(';
            else if (ch == '}') expected = '{';
            else if (ch == ']') expected = '[';

            if (stack[top] != expected) return false;
            top--;
        }
    }
    return top == -1;
}

int main() {
    char s[100005];
    if (scanf("%s", s) == 1) {
        printf("%s\\n", isValid(s) ? "True" : "False");
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isValid(string s) {
    vector<char> stack;
    for (char ch : s) {
        if (ch == '(' || ch == '{' || ch == '[') {
            stack.push_back(ch);
        } else {
            if (stack.empty()) return false;
            char expected = ' ';
            if (ch == ')') expected = '(';
            else if (ch == '}') expected = '{';
            else if (ch == ']') expected = '[';

            if (stack.back() != expected) return false;
            stack.pop_back();
        }
    }
    return stack.empty();
}

int main() {
    string s;
    if (cin >> s) {
        cout << (isValid(s) ? "True" : "False") << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> pairs = new HashMap<>();
        pairs.put(')', '(');
        pairs.put('}', '{');
        pairs.put(']', '[');

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            } else {
                if (stack.isEmpty() || stack.peek() != pairs.get(ch)) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            System.out.println(isValid(sc.next()) ? "True" : "False");
        }
    }
}""",
            "python": """import sys

def isValid(s):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        print(isValid(s))"""
        })
    },

    # 4. Reverse a String Using Stack
    {
        "id": "dsa-stack-reverse-string",
        "problem_num": 94,
        "title": "Reverse a String Using Stack",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "LIFO Processing",
        "difficulty": "EASY",
        "description": "Given a string, reverse it using a stack.",
        "input_format": "A single word/string.",
        "output_format": "The reversed string.",
        "constraints": "1 <= s.length <= 10^5",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Adobe", "Cognizant"],
        "examples": [
            {"input": "hello", "output": "olleh", "explanation": "hello reversed is olleh."},
            {"input": "python", "output": "nohtyp", "explanation": "python reversed is nohtyp."},
            {"input": "abc", "output": "cba", "explanation": "abc reversed is cba."}
        ],
        "test_cases": [
            {"input": "hello", "expected": "olleh", "is_hidden": False},
            {"input": "python", "expected": "nohtyp", "is_hidden": False},
            {"input": "abc", "expected": "cba", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <string.h>\n\nint main() {\n    // Reverse string using stack\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    // Reverse string using stack\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // Reverse string using stack\n    }\n}",
            "python": "def reverseString(s):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

char stack[100005];
int top = -1;

int main() {
    char s[100005];
    if (scanf("%s", s) != 1) return 0;
    int n = strlen(s);
    for (int i = 0; i < n; i++) {
        stack[++top] = s[i];
    }
    char res[100005];
    int idx = 0;
    while (top >= 0) {
        res[idx++] = stack[top--];
    }
    res[idx] = '\\0';
    printf("%s\\n", res);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <vector>

using namespace std;

string reverseString(string s) {
    vector<char> stack;
    for (char ch : s) {
        stack.push_back(ch);
    }
    string result = "";
    while (!stack.empty()) {
        result += stack.back();
        stack.pop_back();
    }
    return result;
}

int main() {
    string s;
    if (cin >> s) {
        cout << reverseString(s) << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static String reverseString(String s) {
        Stack<Character> stack = new Stack<>();
        for (char ch : s.toCharArray()) {
            stack.push(ch);
        }
        StringBuilder result = new StringBuilder();
        while (!stack.isEmpty()) {
            result.append(stack.pop());
        }
        return result.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            System.out.println(reverseString(sc.next()));
        }
    }
}""",
            "python": """import sys

def reverseString(s):
    stack = []
    for ch in s:
        stack.append(ch)

    result = ""
    while stack:
        result += stack.pop()

    return result

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        print(reverseString(s))"""
        })
    },

    # 5. Remove Adjacent Duplicates from String
    {
        "id": "dsa-stack-remove-duplicates",
        "problem_num": 95,
        "title": "Remove Adjacent Duplicates from String",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "Adjacent Cancellation",
        "difficulty": "EASY",
        "description": "Given a string, repeatedly remove adjacent duplicate characters until no adjacent duplicates remain.",
        "input_format": "A single lowercase string.",
        "output_format": "The cleaned string, or 'Empty string' if empty.",
        "constraints": "1 <= s.length <= 10^5",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Bloomberg", "Google"],
        "examples": [
            {"input": "abbaca", "output": "ca", "explanation": "'bb' cancels to 'aaca', then 'aa' cancels to 'ca'."},
            {"input": "azxxzy", "output": "ay", "explanation": "'xx' cancels then 'zz' cancels to 'ay'."},
            {"input": "aabbcc", "output": "Empty string", "explanation": "All pairs cancel."}
        ],
        "test_cases": [
            {"input": "abbaca", "expected": "ca", "is_hidden": False},
            {"input": "azxxzy", "expected": "ay", "is_hidden": False},
            {"input": "aabbcc", "expected": "Empty string", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <string.h>\n\nint main() {\n    // Remove adjacent duplicates\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    // Remove adjacent duplicates\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // Remove adjacent duplicates\n    }\n}",
            "python": "def removeDuplicates(s):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

char stack[100005];
int top = -1;

int main() {
    char s[100005];
    if (scanf("%s", s) != 1) return 0;
    int n = strlen(s);

    for (int i = 0; i < n; i++) {
        if (top >= 0 && stack[top] == s[i]) {
            top--;
        } else {
            stack[++top] = s[i];
        }
    }
    if (top == -1) {
        printf("Empty string\\n");
    } else {
        stack[top + 1] = '\\0';
        printf("%s\\n", stack);
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>

using namespace std;

string removeDuplicates(string s) {
    string stack = "";
    for (char ch : s) {
        if (!stack.empty() && stack.back() == ch) {
            stack.pop_back();
        } else {
            stack.push_back(ch);
        }
    }
    return stack.empty() ? "Empty string" : stack;
}

int main() {
    string s;
    if (cin >> s) {
        cout << removeDuplicates(s) << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static String removeDuplicates(String s) {
        StringBuilder stack = new StringBuilder();
        for (char ch : s.toCharArray()) {
            int len = stack.length();
            if (len > 0 && stack.charAt(len - 1) == ch) {
                stack.deleteCharAt(len - 1);
            } else {
                stack.append(ch);
            }
        }
        return stack.length() == 0 ? "Empty string" : stack.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            System.out.println(removeDuplicates(sc.next()));
        }
    }
}""",
            "python": """import sys

def removeDuplicates(s):
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack) if stack else "Empty string"

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        print(removeDuplicates(s))"""
        })
    },

    # 6. Min Stack
    {
        "id": "dsa-stack-min-stack",
        "problem_num": 96,
        "title": "Min Stack",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "Auxiliary Tracking",
        "difficulty": "MEDIUM",
        "description": "Design a stack that supports push, pop, top, and retrieving the minimum element in O(1) time.",
        "input_format": "Number of operations followed by commands ('push X', 'pop', 'top', 'getMin').",
        "output_format": "The integer output of top/getMin operations.",
        "constraints": "Methods pop, top and getMin operations will always be called on non-empty stacks.",
        "time_complexity": "O(1) per operation",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Bloomberg", "Google", "Microsoft"],
        "examples": [
            {"input": "4 push 5 push 2 push 8 getMin", "output": "2", "explanation": "Minimum is 2."},
            {"input": "4 push 10 push 3 pop getMin", "output": "10", "explanation": "After popping 3, min is 10."},
            {"input": "3 push 4 push 1 top", "output": "1", "explanation": "Top element is 1."}
        ],
        "test_cases": [
            {"input": "4 push 5 push 2 push 8 getMin", "expected": "2", "is_hidden": False},
            {"input": "4 push 10 push 3 pop getMin", "expected": "10", "is_hidden": False},
            {"input": "3 push 4 push 1 top", "expected": "1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\n// Implement MinStack\n",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\n// Implement MinStack\n",
            "java": "import java.util.*;\n\npublic class Main {\n    // Implement MinStack\n}",
            "python": "class MinStack:\n    def __init__(self):\n        self.stack = []\n        self.min_stack = []\n\n    def push(self, val):\n        pass\n\n    def pop(self):\n        pass\n\n    def top(self):\n        pass\n\n    def getMin(self):\n        pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 10005

typedef struct {
    int stack[MAX];
    int min_stack[MAX];
    int top;
    int min_top;
} MinStack;

void init(MinStack *s) {
    s->top = -1;
    s->min_top = -1;
}

void push(MinStack *s, int val) {
    s->stack[++(s->top)] = val;
    if (s->min_top == -1 || val <= s->min_stack[s->min_top]) {
        s->min_stack[++(s->min_top)] = val;
    }
}

int pop(MinStack *s) {
    if (s->top == -1) return -1;
    int val = s->stack[(s->top)--];
    if (val == s->min_stack[s->min_top]) {
        s->min_top--;
    }
    return val;
}

int topVal(MinStack *s) {
    return s->top == -1 ? -1 : s->stack[s->top];
}

int getMin(MinStack *s) {
    return s->min_top == -1 ? -1 : s->min_stack[s->min_top];
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    MinStack s;
    init(&s);
    for (int i = 0; i < n; i++) {
        char op[20];
        scanf("%s", op);
        if (strcmp(op, "push") == 0) {
            int x; scanf("%d", &x);
            push(&s, x);
        } else if (strcmp(op, "pop") == 0) {
            pop(&s);
        } else if (strcmp(op, "top") == 0) {
            printf("%d\\n", topVal(&s));
        } else if (strcmp(op, "getMin") == 0) {
            printf("%d\\n", getMin(&s));
        }
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

class MinStack {
    vector<int> stack;
    vector<int> min_stack;
public:
    void push(int val) {
        stack.push_back(val);
        if (min_stack.empty() || val <= min_stack.back()) {
            min_stack.push_back(val);
        }
    }

    int pop() {
        if (stack.empty()) return -1;
        int val = stack.back();
        stack.pop_back();
        if (val == min_stack.back()) {
            min_stack.pop_back();
        }
        return val;
    }

    int top() {
        return stack.empty() ? -1 : stack.back();
    }

    int getMin() {
        return min_stack.empty() ? -1 : min_stack.back();
    }
};

int main() {
    int n;
    if (!(cin >> n)) return 0;
    MinStack s;
    for (int i = 0; i < n; i++) {
        string op; cin >> op;
        if (op == "push") {
            int x; cin >> x;
            s.push(x);
        } else if (op == "pop") {
            s.pop();
        } else if (op == "top") {
            cout << s.top() << "\\n";
        } else if (op == "getMin") {
            cout << s.getMin() << "\\n";
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

class MinStack {
    private Stack<Integer> stack = new Stack<>();
    private Stack<Integer> minStack = new Stack<>();

    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
    }

    public int pop() {
        if (stack.isEmpty()) return -1;
        int val = stack.pop();
        if (val == minStack.peek()) {
            minStack.pop();
        }
        return val;
    }

    public int top() {
        return stack.isEmpty() ? -1 : stack.peek();
    }

    public int getMin() {
        return minStack.isEmpty() ? -1 : minStack.peek();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        MinStack s = new MinStack();
        for (int i = 0; i < n; i++) {
            String op = sc.next();
            if (op.equals("push")) {
                int x = sc.nextInt();
                s.push(x);
            } else if (op.equals("pop")) {
                s.pop();
            } else if (op.equals("top")) {
                System.out.println(s.top());
            } else if (op.equals("getMin")) {
                System.out.println(s.getMin());
            }
        }
    }
}""",
            "python": """import sys

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.stack:
            return -1
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1] if self.stack else -1

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else -1

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        s = MinStack()
        idx = 1
        for _ in range(n):
            op = tokens[idx]
            idx += 1
            if op == "push":
                x = int(tokens[idx])
                idx += 1
                s.push(x)
            elif op == "pop":
                s.pop()
            elif op == "top":
                print(s.top())
            elif op == "getMin":
                print(s.getMin())"""
        })
    },

    # 7. Next Greater Element
    {
        "id": "dsa-stack-next-greater",
        "problem_num": 97,
        "title": "Next Greater Element",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "Monotonic Stack",
        "difficulty": "MEDIUM",
        "description": "Given an array, find the next greater element for every element. If none exists, output -1.",
        "input_format": "Space-separated integers.",
        "output_format": "Space-separated integers representing next greater elements.",
        "constraints": "1 <= arr.length <= 10^5\n-10^9 <= arr[i] <= 10^9",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Microsoft", "Flipkart", "Adobe"],
        "examples": [
            {"input": "4 5 2 10", "output": "5 10 10 -1", "explanation": "Next greater of 4 is 5, 5 is 10, 2 is 10, 10 has none."},
            {"input": "1 3 2 4", "output": "3 4 4 -1", "explanation": "Next greater elements."},
            {"input": "5 4 3 2", "output": "-1 -1 -1 -1", "explanation": "All elements in decreasing order."}
        ],
        "test_cases": [
            {"input": "4 5 2 10", "expected": "5 10 10 -1", "is_hidden": False},
            {"input": "1 3 2 4", "expected": "3 4 4 -1", "is_hidden": False},
            {"input": "5 4 3 2", "expected": "-1 -1 -1 -1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint main() {\n    // Next Greater Element\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    // Next Greater Element\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // Next Greater Element\n    }\n}",
            "python": "def nextGreater(arr):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

int main() {
    int arr[100005];
    int n = 0;
    while (scanf("%d", &arr[n]) == 1) {
        n++;
    }
    int result[100005];
    int stack[100005];
    int top = -1;

    for (int i = n - 1; i >= 0; i--) {
        while (top >= 0 && stack[top] <= arr[i]) {
            top--;
        }
        result[i] = (top >= 0) ? stack[top] : -1;
        stack[++top] = arr[i];
    }

    for (int i = 0; i < n; i++) {
        printf("%d%s", result[i], (i == n - 1) ? "\\n" : " ");
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

vector<int> nextGreater(vector<int>& arr) {
    int n = arr.size();
    vector<int> result(n, -1);
    vector<int> stack;

    for (int i = n - 1; i >= 0; i--) {
        while (!stack.empty() && stack.back() <= arr[i]) {
            stack.pop_back();
        }
        if (!stack.empty()) {
            result[i] = stack.back();
        }
        stack.push_back(arr[i]);
    }
    return result;
}

int main() {
    vector<int> arr;
    int x;
    while (cin >> x) arr.push_back(x);
    vector<int> res = nextGreater(arr);
    for (int i = 0; i < (int)res.size(); i++) {
        cout << res[i] << (i == (int)res.size() - 1 ? "\\n" : " ");
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int[] nextGreater(int[] arr) {
        int n = arr.length;
        int[] result = new int[n];
        Arrays.fill(result, -1);
        Stack<Integer> stack = new Stack<>();

        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= arr[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                result[i] = stack.peek();
            }
            stack.push(arr[i]);
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] arr = new int[list.size()];
        for (int i = 0; i < list.size(); i++) arr[i] = list.get(i);
        int[] res = nextGreater(arr);
        for (int i = 0; i < res.length; i++) {
            System.out.print(res[i] + (i == res.length - 1 ? "\\n" : " "));
        }
    }
}""",
            "python": """import sys

def nextGreater(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        arr = [int(x) for x in tokens]
        res = nextGreater(arr)
        print(*res)"""
        })
    },

    # 8. Evaluate Reverse Polish Notation
    {
        "id": "dsa-stack-eval-rpn",
        "problem_num": 98,
        "title": "Evaluate Reverse Polish Notation",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "Postfix Evaluation",
        "difficulty": "MEDIUM",
        "description": "Given an arithmetic expression in Reverse Polish Notation (postfix), evaluate its value using +, -, *, /.",
        "input_format": "Space-separated tokens representing RPN expression.",
        "output_format": "A single integer result.",
        "constraints": "1 <= tokens.length <= 10^4",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Google", "LinkedIn"],
        "examples": [
            {"input": "2 1 + 3 *", "output": "9", "explanation": "((2 + 1) * 3) = 9"},
            {"input": "4 13 5 / +", "output": "6", "explanation": "(4 + (13 / 5)) = 6"},
            {"input": "10 6 9 3 + -11 * / * 17 + 5 +", "output": "22", "explanation": "Evaluates to 22"}
        ],
        "test_cases": [
            {"input": "2 1 + 3 *", "expected": "9", "is_hidden": False},
            {"input": "4 13 5 / +", "expected": "6", "is_hidden": False},
            {"input": "10 6 9 3 + -11 * / * 17 + 5 +", "expected": "22", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint main() {\n    // Evaluate RPN\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    // Evaluate RPN\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // Evaluate RPN\n    }\n}",
            "python": "def evalRPN(tokens):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int stack[10005];
int top = -1;

int main() {
    char token[50];
    while (scanf("%s", token) == 1) {
        if (strcmp(token, "+") == 0) {
            int b = stack[top--];
            int a = stack[top--];
            stack[++top] = a + b;
        } else if (strcmp(token, "-") == 0) {
            int b = stack[top--];
            int a = stack[top--];
            stack[++top] = a - b;
        } else if (strcmp(token, "*") == 0) {
            int b = stack[top--];
            int a = stack[top--];
            stack[++top] = a * b;
        } else if (strcmp(token, "/") == 0) {
            int b = stack[top--];
            int a = stack[top--];
            stack[++top] = a / b;
        } else {
            stack[++top] = atoi(token);
        }
    }
    printf("%d\\n", stack[top]);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

int evalRPN(vector<string>& tokens) {
    vector<int> stack;
    for (string& token : tokens) {
        if (token == "+" || token == "-" || token == "*" || token == "/") {
            int b = stack.back(); stack.pop_back();
            int a = stack.back(); stack.pop_back();
            if (token == "+") stack.push_back(a + b);
            else if (token == "-") stack.push_back(a - b);
            else if (token == "*") stack.push_back(a * b);
            else stack.push_back(a / b);
        } else {
            stack.push_back(stoi(token));
        }
    }
    return stack.back();
}

int main() {
    vector<string> tokens;
    string s;
    while (cin >> s) tokens.push_back(s);
    cout << evalRPN(tokens) << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String token : tokens) {
            if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
                int b = stack.pop();
                int a = stack.pop();
                if (token.equals("+")) stack.push(a + b);
                else if (token.equals("-")) stack.push(a - b);
                else if (token.equals("*")) stack.push(a * b);
                else stack.push(a / b);
            } else {
                stack.push(Integer.parseInt(token));
            }
        }
        return stack.peek();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> list = new ArrayList<>();
        while (sc.hasNext()) list.add(sc.next());
        System.out.println(evalRPN(list.toArray(new String[0])));
    }
}""",
            "python": """import sys

def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[-1]

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        print(evalRPN(tokens))"""
        })
    },

    # 9. Daily Temperatures
    {
        "id": "dsa-stack-daily-temperatures",
        "problem_num": 99,
        "title": "Daily Temperatures",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "Monotonic Stack",
        "difficulty": "MEDIUM",
        "description": "Given an array of daily temperatures, find how many days you must wait until a warmer temperature. If none, return 0.",
        "input_format": "Space-separated integers representing temperatures.",
        "output_format": "Space-separated integers representing wait days.",
        "constraints": "1 <= temperatures.length <= 10^5\n30 <= temperatures[i] <= 100",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Google", "Facebook"],
        "examples": [
            {"input": "73 74 75 71 69 72 76 73", "output": "1 1 4 2 1 1 0 0", "explanation": "Wait 1 day for 74, 1 day for 75, 4 days for 76..."},
            {"input": "30 40 50 60", "output": "1 1 1 0", "explanation": "Each day is followed by warmer day except the last."},
            {"input": "80 70 60", "output": "0 0 0", "explanation": "Decreasing temperatures, no warmer days."}
        ],
        "test_cases": [
            {"input": "73 74 75 71 69 72 76 73", "expected": "1 1 4 2 1 1 0 0", "is_hidden": False},
            {"input": "30 40 50 60", "expected": "1 1 1 0", "is_hidden": False},
            {"input": "80 70 60", "expected": "0 0 0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint main() {\n    // Daily Temperatures\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    // Daily Temperatures\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // Daily Temperatures\n    }\n}",
            "python": "def dailyTemperatures(temperatures):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

int temps[100005];
int res[100005];
int stack[100005];
int top = -1;

int main() {
    int n = 0;
    while (scanf("%d", &temps[n]) == 1) {
        res[n] = 0;
        n++;
    }

    for (int i = 0; i < n; i++) {
        while (top >= 0 && temps[i] > temps[stack[top]]) {
            int prev_idx = stack[top--];
            res[prev_idx] = i - prev_idx;
        }
        stack[++top] = i;
    }

    for (int i = 0; i < n; i++) {
        printf("%d%s", res[i], (i == n - 1) ? "\\n" : " ");
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

vector<int> dailyTemperatures(vector<int>& temperatures) {
    int n = temperatures.size();
    vector<int> result(n, 0);
    vector<int> stack;

    for (int i = 0; i < n; i++) {
        while (!stack.empty() && temperatures[i] > temperatures[stack.back()]) {
            int index = stack.back();
            stack.pop_back();
            result[index] = i - index;
        }
        stack.push_back(i);
    }
    return result;
}

int main() {
    vector<int> temps;
    int x;
    while (cin >> x) temps.push_back(x);
    vector<int> res = dailyTemperatures(temps);
    for (int i = 0; i < (int)res.size(); i++) {
        cout << res[i] << (i == (int)res.size() - 1 ? "\\n" : " ");
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int index = stack.pop();
                result[index] = i - index;
            }
            stack.push(i);
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] temps = new int[list.size()];
        for (int i = 0; i < list.size(); i++) temps[i] = list.get(i);
        int[] res = dailyTemperatures(temps);
        for (int i = 0; i < res.length; i++) {
            System.out.print(res[i] + (i == res.length - 1 ? "\\n" : " "));
        }
    }
}""",
            "python": """import sys

def dailyTemperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)

    return result

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        arr = [int(x) for x in tokens]
        res = dailyTemperatures(arr)
        print(*res)"""
        })
    },

    # 10. Decode String
    {
        "id": "dsa-stack-decode-string",
        "problem_num": 100,
        "title": "Decode String",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "Nested Expression Parsing",
        "difficulty": "MEDIUM",
        "description": "Decode an encoded string where k[encoded_string] means the string is repeated k times.",
        "input_format": "A single encoded string.",
        "output_format": "The decoded string.",
        "constraints": "1 <= s.length <= 1000",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Google", "Amazon", "Cisco"],
        "examples": [
            {"input": "3[a]", "output": "aaa", "explanation": "'a' repeated 3 times."},
            {"input": "3[a2[c]]", "output": "accaccacc", "explanation": "'acc' repeated 3 times."},
            {"input": "2[abc]3[cd]", "output": "abcabccdcdcd", "explanation": "'abc' twice followed by 'cd' 3 times."}
        ],
        "test_cases": [
            {"input": "3[a]", "expected": "aaa", "is_hidden": False},
            {"input": "3[a2[c]]", "expected": "accaccacc", "is_hidden": False},
            {"input": "2[abc]3[cd]", "expected": "abcabccdcdcd", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <string.h>\n\nint main() {\n    // Decode String\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    // Decode String\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // Decode String\n    }\n}",
            "python": "def decodeString(s):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

char str_stack[500][10005];
int count_stack[500];
int top = -1;

int main() {
    char s[1005];
    if (scanf("%s", s) != 1) return 0;

    char curr_str[10005] = "";
    int curr_num = 0;

    int n = strlen(s);
    for (int i = 0; i < n; i++) {
        char ch = s[i];
        if (isdigit(ch)) {
            curr_num = curr_num * 10 + (ch - '0');
        } else if (ch == '[') {
            top++;
            strcpy(str_stack[top], curr_str);
            count_stack[top] = curr_num;
            curr_str[0] = '\\0';
            curr_num = 0;
        } else if (ch == ']') {
            int repeat = count_stack[top];
            char prev[10005];
            strcpy(prev, str_stack[top]);
            top--;

            char temp[10005] = "";
            for (int r = 0; r < repeat; r++) {
                strcat(temp, curr_str);
            }
            strcpy(curr_str, prev);
            strcat(curr_str, temp);
        } else {
            int len = strlen(curr_str);
            curr_str[len] = ch;
            curr_str[len + 1] = '\\0';
        }
    }
    printf("%s\\n", curr_str);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <vector>

using namespace std;

string decodeString(string s) {
    vector<pair<string, int>> stack;
    int current_num = 0;
    string current_string = "";

    for (char ch : s) {
        if (isdigit(ch)) {
            current_num = current_num * 10 + (ch - '0');
        } else if (ch == '[') {
            stack.push_back({current_string, current_num});
            current_string = "";
            current_num = 0;
        } else if (ch == ']') {
            pair<string, int> top = stack.back();
            string prev_string = top.first;
            int num = top.second;
            stack.pop_back();
            string repeated = "";
            for (int i = 0; i < num; i++) repeated += current_string;
            current_string = prev_string + repeated;
        } else {
            current_string += ch;
        }
    }
    return current_string;
}

int main() {
    string s;
    if (cin >> s) {
        cout << decodeString(s) << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static String decodeString(String s) {
        Stack<String> strStack = new Stack<>();
        Stack<Integer> countStack = new Stack<>();
        String currentString = "";
        int currentNum = 0;

        for (char ch : s.toCharArray()) {
            if (Character.isDigit(ch)) {
                currentNum = currentNum * 10 + (ch - '0');
            } else if (ch == '[') {
                strStack.push(currentString);
                countStack.push(currentNum);
                currentString = "";
                currentNum = 0;
            } else if (ch == ']') {
                String prevString = strStack.pop();
                int num = countStack.pop();
                StringBuilder sb = new StringBuilder(prevString);
                for (int i = 0; i < num; i++) {
                    sb.append(currentString);
                }
                currentString = sb.toString();
            } else {
                currentString += ch;
            }
        }
        return currentString;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            System.out.println(decodeString(sc.next()));
        }
    }
}""",
            "python": """import sys

def decodeString(s):
    stack = []
    current_num = 0
    current_string = ""

    for ch in s:
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)
        elif ch == '[':
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif ch == ']':
            previous_string, num = stack.pop()
            current_string = previous_string + current_string * num
        else:
            current_string += ch

    return current_string

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        print(decodeString(s))"""
        })
    },

    # 11. Largest Rectangle in Histogram
    {
        "id": "dsa-stack-largest-rectangle",
        "problem_num": 101,
        "title": "Largest Rectangle in Histogram",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "Monotonic Stack Boundaries",
        "difficulty": "HARD",
        "description": "Given an array of heights of histogram bars, find the area of the largest rectangle that can be formed.",
        "input_format": "Space-separated integers representing bar heights.",
        "output_format": "A single integer representing maximum area.",
        "constraints": "1 <= heights.length <= 10^5\n0 <= heights[i] <= 10^4",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Google", "Amazon", "Facebook", "Microsoft"],
        "examples": [
            {"input": "2 1 5 6 2 3", "output": "10", "explanation": "Bars 5 and 6 form rectangle of height 5, width 2 = 10."},
            {"input": "2 4", "output": "4", "explanation": "Height 4 width 1 gives area 4."},
            {"input": "2 2 2", "output": "6", "explanation": "Height 2 width 3 gives area 6."}
        ],
        "test_cases": [
            {"input": "2 1 5 6 2 3", "expected": "10", "is_hidden": False},
            {"input": "2 4", "expected": "4", "is_hidden": False},
            {"input": "2 2 2", "expected": "6", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint main() {\n    // Largest Rectangle in Histogram\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    // Largest Rectangle in Histogram\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // Largest Rectangle in Histogram\n    }\n}",
            "python": "def largestRectangleArea(heights):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

long long max(long long a, long long b) { return a > b ? a : b; }

int heights[100005];
int stack[100005];
int top = -1;

int main() {
    int n = 0;
    while (scanf("%d", &heights[n]) == 1) {
        n++;
    }

    long long max_area = 0;
    for (int i = 0; i <= n; i++) {
        int current = (i < n) ? heights[i] : 0;
        while (top >= 0 && current < heights[stack[top]]) {
            int h = heights[stack[top--]];
            int w = (top == -1) ? i : (i - stack[top] - 1);
            long long area = (long long)h * w;
            max_area = max(max_area, area);
        }
        stack[++top] = i;
    }

    printf("%lld\\n", max_area);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long largestRectangleArea(vector<int>& heights) {
    vector<int> stack;
    long long max_area = 0;
    int n = heights.size();

    for (int i = 0; i <= n; i++) {
        int current = (i < n) ? heights[i] : 0;
        while (!stack.empty() && current < heights[stack.back()]) {
            int h = heights[stack.back()];
            stack.pop_back();
            int w = stack.empty() ? i : (i - stack.back() - 1);
            max_area = max(max_area, (long long)h * w);
        }
        stack.push_back(i);
    }
    return max_area;
}

int main() {
    vector<int> heights;
    int x;
    while (cin >> x) heights.push_back(x);
    cout << largestRectangleArea(heights) << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static long largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        long maxArea = 0;
        int n = heights.length;

        for (int i = 0; i <= n; i++) {
            int current = (i < n) ? heights[i] : 0;
            while (!stack.isEmpty() && current < heights[stack.peek()]) {
                int h = heights[stack.pop()];
                int w = stack.isEmpty() ? i : (i - stack.peek() - 1);
                maxArea = Math.max(maxArea, (long) h * w);
            }
            stack.push(i);
        }
        return maxArea;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] heights = new int[list.size()];
        for (int i = 0; i < list.size(); i++) heights[i] = list.get(i);
        System.out.println(largestRectangleArea(heights));
    }
}""",
            "python": """import sys

def largestRectangleArea(heights):
    stack = []
    max_area = 0

    for i in range(len(heights) + 1):
        current = heights[i] if i < len(heights) else 0

        while stack and current < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        arr = [int(x) for x in tokens]
        print(largestRectangleArea(arr))"""
        })
    },

    # 12. Maximal Rectangle
    {
        "id": "dsa-stack-maximal-rectangle",
        "problem_num": 102,
        "title": "Maximal Rectangle",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "2D Matrix Histogram",
        "difficulty": "HARD",
        "description": "Given a rows x cols binary matrix containing only 0s and 1s, find the largest rectangular area containing only 1s.",
        "input_format": "rows cols followed by matrix elements (row by row).",
        "output_format": "A single integer maximum area.",
        "constraints": "1 <= rows, cols <= 200\nmatrix[i][j] is '0' or '1'",
        "time_complexity": "O(rows * cols)",
        "space_complexity": "O(cols)",
        "company_tags": ["Google", "Amazon", "Apple"],
        "examples": [
            {"input": "4 5 1 0 1 0 0 1 0 1 1 1 1 1 1 1 1 1 0 0 1 0", "output": "6", "explanation": "Max rectangle of 1s has area 6."},
            {"input": "2 2 1 1 1 1", "output": "4", "explanation": "2x2 rectangle has area 4."},
            {"input": "2 2 0 0 0 0", "output": "0", "explanation": "No 1s in matrix."}
        ],
        "test_cases": [
            {"input": "4 5 1 0 1 0 0 1 0 1 1 1 1 1 1 1 1 1 0 0 1 0", "expected": "6", "is_hidden": False},
            {"input": "2 2 1 1 1 1", "expected": "4", "is_hidden": False},
            {"input": "2 2 0 0 0 0", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint main() {\n    // Maximal Rectangle\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    // Maximal Rectangle\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // Maximal Rectangle\n    }\n}",
            "python": "def maximalRectangle(matrix):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

int max(int a, int b) { return a > b ? a : b; }

int largestRectangleArea(int *heights, int n) {
    int stack[500];
    int top = -1;
    int max_area = 0;

    for (int i = 0; i <= n; i++) {
        int current = (i < n) ? heights[i] : 0;
        while (top >= 0 && current < heights[stack[top]]) {
            int h = heights[stack[top--]];
            int w = (top == -1) ? i : (i - stack[top] - 1);
            max_area = max(max_area, h * w);
        }
        stack[++top] = i;
    }
    return max_area;
}

int main() {
    int rows, cols;
    if (scanf("%d %d", &rows, &cols) != 2) return 0;
    int heights[500] = {0};
    int max_area = 0;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            char val[10];
            scanf("%s", val);
            if (val[0] == '1') {
                heights[j] += 1;
            } else {
                heights[j] = 0;
            }
        }
        max_area = max(max_area, largestRectangleArea(heights, cols));
    }
    printf("%d\\n", max_area);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int largestRectangleArea(vector<int>& heights) {
    vector<int> stack;
    int max_area = 0;
    int n = heights.size();

    for (int i = 0; i <= n; i++) {
        int current = (i < n) ? heights[i] : 0;
        while (!stack.empty() && current < heights[stack.back()]) {
            int h = heights[stack.back()];
            stack.pop_back();
            int w = stack.empty() ? i : (i - stack.back() - 1);
            max_area = max(max_area, h * w);
        }
        stack.push_back(i);
    }
    return max_area;
}

int maximalRectangle(vector<vector<string>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return 0;
    int cols = matrix[0].size();
    vector<int> heights(cols, 0);
    int max_area = 0;

    for (auto& row : matrix) {
        for (int j = 0; j < cols; j++) {
            if (row[j] == "1") heights[j] += 1;
            else heights[j] = 0;
        }
        max_area = max(max_area, largestRectangleArea(heights));
    }
    return max_area;
}

int main() {
    int rows, cols;
    if (!(cin >> rows >> cols)) return 0;
    vector<vector<string>> matrix(rows, vector<string>(cols));
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cin >> matrix[i][j];
        }
    }
    cout << maximalRectangle(matrix) << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        int n = heights.length;

        for (int i = 0; i <= n; i++) {
            int current = (i < n) ? heights[i] : 0;
            while (!stack.isEmpty() && current < heights[stack.peek()]) {
                int h = heights[stack.pop()];
                int w = stack.isEmpty() ? i : (i - stack.peek() - 1);
                maxArea = Math.max(maxArea, h * w);
            }
            stack.push(i);
        }
        return maxArea;
    }

    public static int maximalRectangle(String[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int cols = matrix[0].length;
        int[] heights = new int[cols];
        int maxArea = 0;

        for (String[] row : matrix) {
            for (int j = 0; j < cols; j++) {
                if (row[j].equals("1")) heights[j] += 1;
                else heights[j] = 0;
            }
            maxArea = Math.max(maxArea, largestRectangleArea(heights));
        }
        return maxArea;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        String[][] matrix = new String[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = sc.next();
            }
        }
        System.out.println(maximalRectangle(matrix));
    }
}""",
            "python": """import sys

def largestRectangleArea(heights):
    stack = []
    max_area = 0

    for i in range(len(heights) + 1):
        current = heights[i] if i < len(heights) else 0

        while stack and current < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area

def maximalRectangle(matrix):
    if not matrix:
        return 0

    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in matrix:
        for j in range(cols):
            if row[j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0

        max_area = max(max_area, largestRectangleArea(heights))

    return max_area

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        rows = int(tokens[0])
        cols = int(tokens[1])
        idx = 2
        matrix = []
        for _ in range(rows):
            matrix.append(tokens[idx:idx+cols])
            idx += cols
        print(maximalRectangle(matrix))"""
        })
    },

    # 13. Basic Calculator
    {
        "id": "dsa-stack-basic-calculator",
        "problem_num": 103,
        "title": "Basic Calculator",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "Parenthesized Arithmetic",
        "difficulty": "HARD",
        "description": "Given a string containing integers, +, -, and parentheses, evaluate the mathematical expression.",
        "input_format": "A single line containing the expression.",
        "output_format": "A single integer result.",
        "constraints": "1 <= s.length <= 3 * 10^5\ns consists of digits, '+', '-', '(', ')', and ' '.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Google", "Amazon", "Facebook", "Microsoft"],
        "examples": [
            {"input": "1 + 1", "output": "2", "explanation": "1 + 1 = 2"},
            {"input": "2-(1+2)", "output": "-1", "explanation": "2 - 3 = -1"},
            {"input": "(1+(4+5+2)-3)+(6+8)", "output": "23", "explanation": "Evaluates to 23"}
        ],
        "test_cases": [
            {"input": "1 + 1", "expected": "2", "is_hidden": False},
            {"input": "2-(1+2)", "expected": "-1", "is_hidden": False},
            {"input": "(1+(4+5+2)-3)+(6+8)", "expected": "23", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <string.h>\n\nint main() {\n    // Basic Calculator\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    // Basic Calculator\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // Basic Calculator\n    }\n}",
            "python": "def calculate(s):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>
#include <ctype.h>

int stack[100005];
int top = -1;

int main() {
    char s[300005];
    if (!fgets(s, sizeof(s), stdin)) return 0;

    int result = 0;
    int number = 0;
    int sign = 1;
    int n = strlen(s);

    for (int i = 0; i < n; i++) {
        char ch = s[i];
        if (isdigit(ch)) {
            number = number * 10 + (ch - '0');
        } else if (ch == '+') {
            result += sign * number;
            number = 0;
            sign = 1;
        } else if (ch == '-') {
            result += sign * number;
            number = 0;
            sign = -1;
        } else if (ch == '(') {
            stack[++top] = result;
            stack[++top] = sign;
            result = 0;
            sign = 1;
        } else if (ch == ')') {
            result += sign * number;
            number = 0;
            result *= stack[top--];
            result += stack[top--];
        }
    }
    result += sign * number;
    printf("%d\\n", result);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <vector>
#include <cctype>

using namespace std;

int calculate(string s) {
    vector<int> stack;
    int result = 0;
    int number = 0;
    int sign = 1;

    for (char ch : s) {
        if (isdigit(ch)) {
            number = number * 10 + (ch - '0');
        } else if (ch == '+') {
            result += sign * number;
            number = 0;
            sign = 1;
        } else if (ch == '-') {
            result += sign * number;
            number = 0;
            sign = -1;
        } else if (ch == '(') {
            stack.push_back(result);
            stack.push_back(sign);
            result = 0;
            sign = 1;
        } else if (ch == ')') {
            result += sign * number;
            number = 0;
            result *= stack.back(); stack.pop_back();
            result += stack.back(); stack.pop_back();
        }
    }
    return result + sign * number;
}

int main() {
    string s;
    getline(cin, s);
    cout << calculate(s) << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int calculate(String s) {
        Stack<Integer> stack = new Stack<>();
        int result = 0;
        int number = 0;
        int sign = 1;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (Character.isDigit(ch)) {
                number = number * 10 + (ch - '0');
            } else if (ch == '+') {
                result += sign * number;
                number = 0;
                sign = 1;
            } else if (ch == '-') {
                result += sign * number;
                number = 0;
                sign = -1;
            } else if (ch == '(') {
                stack.push(result);
                stack.push(sign);
                result = 0;
                sign = 1;
            } else if (ch == ')') {
                result += sign * number;
                number = 0;
                result *= stack.pop();
                result += stack.pop();
            }
        }
        return result + sign * number;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(calculate(s));
    }
}""",
            "python": """import sys

def calculate(s):
    stack = []
    result = 0
    number = 0
    sign = 1

    for ch in s:
        if ch.isdigit():
            number = number * 10 + int(ch)
        elif ch == '+':
            result += sign * number
            number = 0
            sign = 1
        elif ch == '-':
            result += sign * number
            number = 0
            sign = -1
        elif ch == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif ch == ')':
            result += sign * number
            number = 0
            result *= stack.pop()
            result += stack.pop()

    return result + sign * number

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        print(calculate(s))"""
        })
    },

    # 14. Trapping Rain Water
    {
        "id": "dsa-stack-trapping-rain-water",
        "problem_num": 104,
        "title": "Trapping Rain Water",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "Bounded Volume",
        "difficulty": "HARD",
        "description": "Given an array representing heights of elevation bars, compute how much rainwater can be trapped after raining.",
        "input_format": "Space-separated non-negative integers representing elevation map.",
        "output_format": "A single integer total trapped water units.",
        "constraints": "1 <= height.length <= 10^5\n0 <= height[i] <= 10^5",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Google", "Facebook", "Microsoft", "Goldman Sachs"],
        "examples": [
            {"input": "0 1 0 2 1 0 1 3 2 1 2 1", "output": "6", "explanation": "6 units of rainwater are trapped."},
            {"input": "4 2 0 3 2 5", "output": "9", "explanation": "9 units of rain water trapped."},
            {"input": "1 2 3 4", "output": "0", "explanation": "Monotonically increasing bars cannot trap water."}
        ],
        "test_cases": [
            {"input": "0 1 0 2 1 0 1 3 2 1 2 1", "expected": "6", "is_hidden": False},
            {"input": "4 2 0 3 2 5", "expected": "9", "is_hidden": False},
            {"input": "1 2 3 4", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint main() {\n    // Trapping Rain Water\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    // Trapping Rain Water\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // Trapping Rain Water\n    }\n}",
            "python": "def trap(height):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

int min(int a, int b) { return a < b ? a : b; }

int height[100005];
int stack[100005];
int top = -1;

int main() {
    int n = 0;
    while (scanf("%d", &height[n]) == 1) {
        n++;
    }

    long long water = 0;
    for (int i = 0; i < n; i++) {
        while (top >= 0 && height[i] > height[stack[top]]) {
            int bottom = stack[top--];
            if (top < 0) break;
            int distance = i - stack[top] - 1;
            int bounded_height = min(height[i], height[stack[top]]) - height[bottom];
            water += (long long)distance * bounded_height;
        }
        stack[++top] = i;
    }
    printf("%lld\\n", water);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long trap(vector<int>& height) {
    vector<int> stack;
    long long water = 0;
    int n = height.size();

    for (int i = 0; i < n; i++) {
        while (!stack.empty() && height[i] > height[stack.back()]) {
            int bottom = stack.back();
            stack.pop_back();
            if (stack.empty()) break;
            int distance = i - stack.back() - 1;
            int bounded_height = min(height[i], height[stack.back()]) - height[bottom];
            water += (long long)distance * bounded_height;
        }
        stack.push_back(i);
    }
    return water;
}

int main() {
    vector<int> height;
    int x;
    while (cin >> x) height.push_back(x);
    cout << trap(height) << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static long trap(int[] height) {
        Stack<Integer> stack = new Stack<>();
        long water = 0;
        int n = height.length;

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && height[i] > height[stack.peek()]) {
                int bottom = stack.pop();
                if (stack.isEmpty()) break;
                int distance = i - stack.peek() - 1;
                int boundedHeight = Math.min(height[i], height[stack.peek()]) - height[bottom];
                water += (long) distance * boundedHeight;
            }
            stack.push(i);
        }
        return water;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] height = new int[list.size()];
        for (int i = 0; i < list.size(); i++) height[i] = list.get(i);
        System.out.println(trap(height));
    }
}""",
            "python": """import sys

def trap(height):
    stack = []
    water = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            bottom = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(height[i], height[stack[-1]]) - height[bottom]
            water += distance * bounded_height
        stack.append(i)

    return water

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        arr = [int(x) for x in tokens]
        print(trap(arr))"""
        })
    },

    # 15. Sum of Subarray Minimums
    {
        "id": "dsa-stack-sum-subarray-mins",
        "problem_num": 105,
        "title": "Sum of Subarray Minimums",
        "category": "Stack",
        "topic": "Stack",
        "subtopic": "Contribution Counting",
        "difficulty": "HARD",
        "description": "Given an array of integers, calculate the sum of the minimum element of every contiguous subarray. Return result modulo 10^9 + 7.",
        "input_format": "Space-separated integers.",
        "output_format": "A single integer modulo 10^9 + 7.",
        "constraints": "1 <= arr.length <= 10^5\n1 <= arr[i] <= 10^5",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Microsoft", "Google"],
        "examples": [
            {"input": "3 1 2 4", "output": "17", "explanation": "Subarrays min sum is 17."},
            {"input": "11 81 94 43 3", "output": "444", "explanation": "Total sum modulo 10^9+7 is 444."},
            {"input": "1 1", "output": "3", "explanation": "[1]: 1, [1]: 1, [1, 1]: 1. Sum = 3."}
        ],
        "test_cases": [
            {"input": "3 1 2 4", "expected": "17", "is_hidden": False},
            {"input": "11 81 94 43 3", "expected": "444", "is_hidden": False},
            {"input": "1 1", "expected": "3", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint main() {\n    // Sum of Subarray Minimums\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    // Sum of Subarray Minimums\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // Sum of Subarray Minimums\n    }\n}",
            "python": "def sumSubarrayMins(arr):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

#define MOD 1000000007

int arr[100005];
int left_arr[100005];
int right_arr[100005];
int stack[100005];
int top = -1;

int main() {
    int n = 0;
    while (scanf("%d", &arr[n]) == 1) {
        n++;
    }

    for (int i = 0; i < n; i++) {
        while (top >= 0 && arr[stack[top]] > arr[i]) {
            top--;
        }
        left_arr[i] = (top >= 0) ? (i - stack[top]) : (i + 1);
        stack[++top] = i;
    }

    top = -1;
    for (int i = n - 1; i >= 0; i--) {
        while (top >= 0 && arr[stack[top]] >= arr[i]) {
            top--;
        }
        right_arr[i] = (top >= 0) ? (stack[top] - i) : (n - i);
        stack[++top] = i;
    }

    long long result = 0;
    for (int i = 0; i < n; i++) {
        long long contrib = ((long long)arr[i] * left_arr[i]) % MOD;
        contrib = (contrib * right_arr[i]) % MOD;
        result = (result + contrib) % MOD;
    }

    printf("%lld\\n", result);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

int sumSubarrayMins(vector<int>& arr) {
    long long MOD = 1e9 + 7;
    int n = arr.size();
    vector<int> left(n), right(n);
    vector<int> stack;

    for (int i = 0; i < n; i++) {
        while (!stack.empty() && arr[stack.back()] > arr[i]) {
            stack.pop_back();
        }
        left[i] = stack.empty() ? (i + 1) : (i - stack.back());
        stack.push_back(i);
    }

    stack.clear();
    for (int i = n - 1; i >= 0; i--) {
        while (!stack.empty() && arr[stack.back()] >= arr[i]) {
            stack.pop_back();
        }
        right[i] = stack.empty() ? (n - i) : (stack.back() - i);
        stack.push_back(i);
    }

    long long result = 0;
    for (int i = 0; i < n; i++) {
        long long contrib = (1LL * arr[i] * left[i]) % MOD;
        contrib = (contrib * right[i]) % MOD;
        result = (result + contrib) % MOD;
    }
    return result;
}

int main() {
    vector<int> arr;
    int x;
    while (cin >> x) arr.push_back(x);
    cout << sumSubarrayMins(arr) << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int sumSubarrayMins(int[] arr) {
        long MOD = 1000000007L;
        int n = arr.length;
        int[] left = new int[n];
        int[] right = new int[n];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                stack.pop();
            }
            left[i] = stack.isEmpty() ? (i + 1) : (i - stack.peek());
            stack.push(i);
        }

        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop();
            }
            right[i] = stack.isEmpty() ? (n - i) : (stack.peek() - i);
            stack.push(i);
        }

        long result = 0;
        for (int i = 0; i < n; i++) {
            long contrib = ((long) arr[i] * left[i]) % MOD;
            contrib = (contrib * right[i]) % MOD;
            result = (result + contrib) % MOD;
        }
        return (int) result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] arr = new int[list.size()];
        for (int i = 0; i < list.size(); i++) arr[i] = list.get(i);
        System.out.println(sumSubarrayMins(arr));
    }
}""",
            "python": """import sys

def sumSubarrayMins(arr):
    MOD = 10**9 + 7
    n = len(arr)

    stack = []
    left = [0] * n
    right = [0] * n

    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        left[i] = i - stack[-1] if stack else i + 1
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        right[i] = stack[-1] - i if stack else n - i
        stack.append(i)

    result = 0
    for i in range(n):
        result += arr[i] * left[i] * right[i]

    return result % MOD

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        arr = [int(x) for x in tokens]
        print(sumSubarrayMins(arr))"""
        })
    }
]

problems.extend(stack_data)

with open("backend/app/data/dsa_problems_seed.json", "w", encoding="utf-8") as f:
    json.dump(problems, f, indent=2)

print(f"Successfully added 15 Stack problems! Total problems now: {len(problems)}")
