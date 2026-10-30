import sys, os
sys.path.insert(0, os.path.abspath('.'))
import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    problems = json.load(f)

# Filter out if any exist
ll_ids = {
    "dsa-ll-reverse", "dsa-ll-middle", "dsa-ll-detect-loop", "dsa-ll-remove-duplicates",
    "dsa-ll-delete-node", "dsa-ll-merge-two-sorted", "dsa-ll-remove-nth-from-end",
    "dsa-ll-intersection", "dsa-ll-add-two-numbers", "dsa-ll-sort-list",
    "dsa-ll-reverse-k-group", "dsa-ll-copy-random-pointer", "dsa-ll-merge-k-sorted",
    "dsa-ll-lru-cache", "dsa-ll-flatten-multilevel"
}
problems = [p for p in problems if p["id"] not in ll_ids]

ll_data = [
    # 1. Reverse a Linked List
    {
        "id": "dsa-ll-reverse",
        "problem_num": 76,
        "title": "Reverse a Linked List",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Pointers & In-place Reversal",
        "difficulty": "EASY",
        "description": "Given the head of a singly linked list, reverse the linked list and return its new head.",
        "input_format": "Space-separated integers representing nodes of the linked list.",
        "output_format": "Space-separated integers representing the reversed linked list.",
        "constraints": "0 <= number of nodes <= 5000\n-5000 <= Node.val <= 5000",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "company_tags": ["Amazon", "Microsoft", "Google", "Apple"],
        "examples": [
            {"input": "1 2 3 4 5", "output": "5 4 3 2 1", "explanation": "List reversed."},
            {"input": "1 2", "output": "2 1", "explanation": "Two elements reversed."},
            {"input": "10", "output": "10", "explanation": "Single node remains same."}
        ],
        "test_cases": [
            {"input": "1 2 3 4 5", "expected": "5 4 3 2 1", "is_hidden": False},
            {"input": "1 2", "expected": "2 1", "is_hidden": False},
            {"input": "10", "expected": "10", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdlib.h>\n\nstruct Node {\n    int data;\n    struct Node* next;\n};\n\nstruct Node* reverseList(struct Node* head) {\n    // Your code here\n    return head;\n}\n\nint main() {\n    int val;\n    struct Node *head = NULL, *tail = NULL;\n    while (scanf(\"%d\", &val) == 1) {\n        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));\n        temp->data = val; temp->next = NULL;\n        if (!head) head = tail = temp;\n        else { tail->next = temp; tail = temp; }\n    }\n    head = reverseList(head);\n    while (head) {\n        printf(\"%d%s\", head->data, head->next ? \" \" : \"\\n\");\n        head = head->next;\n    }\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nstruct Node {\n    int data;\n    Node* next;\n    Node(int val) : data(val), next(nullptr) {}\n};\n\nNode* reverseList(Node* head) {\n    // Your code here\n    return head;\n}\n\nint main() {\n    int x;\n    Node *head = nullptr, *tail = nullptr;\n    while (cin >> x) {\n        Node* temp = new Node(x);\n        if (!head) head = tail = temp;\n        else { tail->next = temp; tail = temp; }\n    }\n    head = reverseList(head);\n    while (head) {\n        cout << head->data << (head->next ? \" \" : \"\\n\");\n        head = head->next;\n    }\n    return 0;\n}",
            "java": "import java.util.*;\n\nclass Node {\n    int data;\n    Node next;\n    Node(int d) { data = d; }\n}\n\npublic class Main {\n    public static Node reverseList(Node head) {\n        // Your code here\n        return head;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        Node head = null, tail = null;\n        while (sc.hasNextInt()) {\n            Node temp = new Node(sc.nextInt());\n            if (head == null) head = tail = temp;\n            else { tail.next = temp; tail = temp; }\n        }\n        head = reverseList(head);\n        while (head != null) {\n            System.out.print(head.data + (head.next != null ? \" \" : \"\\n\"));\n            head = head.next;\n        }\n    }\n}",
            "python": "class Node:\n    def __init__(self, data):\n        self.data = data\n        self.next = None\n\ndef reverseList(head):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* reverseList(struct Node* head) {
    struct Node *prev = NULL;
    struct Node *curr = head;

    while (curr) {
        struct Node *next_node = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next_node;
    }
    return prev;
}

int main() {
    int val;
    struct Node *head = NULL, *tail = NULL;
    while (scanf("%d", &val) == 1) {
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = val; temp->next = NULL;
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
    }
    head = reverseList(head);
    while (head) {
        printf("%d%s", head->data, head->next ? " " : "\\n");
        head = head->next;
    }
    return 0;
}""",
            "cpp": """#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

Node* reverseList(Node* head) {
    Node *prev = nullptr;
    Node *curr = head;

    while (curr) {
        Node *next_node = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next_node;
    }
    return prev;
}

int main() {
    int x;
    Node *head = nullptr, *tail = nullptr;
    while (cin >> x) {
        Node* temp = new Node(x);
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
    }
    head = reverseList(head);
    while (head) {
        cout << head->data << (head->next ? " " : "\\n");
        head = head->next;
    }
    return 0;
}""",
            "java": """import java.util.*;

class Node {
    int data;
    Node next;
    Node(int d) { data = d; }
}

public class Main {
    public static Node reverseList(Node head) {
        Node prev = null;
        Node curr = head;

        while (curr != null) {
            Node next_node = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next_node;
        }
        return prev;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Node head = null, tail = null;
        while (sc.hasNextInt()) {
            Node temp = new Node(sc.nextInt());
            if (head == null) head = tail = temp;
            else { tail.next = temp; tail = temp; }
        }
        head = reverseList(head);
        while (head != null) {
            System.out.print(head.data + (head.next != null ? " " : "\\n"));
            head = head.next;
        }
    }
}""",
            "python": """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

def createList(arr):
    head = Node(arr[0]) if arr else None
    curr = head
    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next
    return head

def printList(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print(*result)

if __name__ == '__main__':
    import sys
    tokens = sys.stdin.read().split()
    if tokens:
        arr = [int(x) for x in tokens]
        head = createList(arr)
        head = reverseList(head)
        printList(head)"""
        })
    },

    # 2. Find the Middle of a Linked List
    {
        "id": "dsa-ll-middle",
        "problem_num": 77,
        "title": "Find the Middle of a Linked List",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Slow and Fast Pointers",
        "difficulty": "EASY",
        "description": "Given the head of a singly linked list, find and return the middle node value. If there are two middle nodes, return the second middle node.",
        "input_format": "Space-separated integers.",
        "output_format": "The integer data of the middle node.",
        "constraints": "1 <= number of nodes <= 5000\n1 <= Node.val <= 5000",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "company_tags": ["Amazon", "Adobe", "Qualcomm"],
        "examples": [
            {"input": "1 2 3 4 5", "output": "3", "explanation": "Odd length: 3 is the middle."},
            {"input": "1 2 3 4 5 6", "output": "4", "explanation": "Even length: second middle is 4."},
            {"input": "10", "output": "10", "explanation": "Single node middle is itself."}
        ],
        "test_cases": [
            {"input": "1 2 3 4 5", "expected": "3", "is_hidden": False},
            {"input": "1 2 3 4 5 6", "expected": "4", "is_hidden": False},
            {"input": "10", "expected": "10", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdlib.h>\n\nstruct Node { int data; struct Node* next; };\n\nstruct Node* middleNode(struct Node* head) {\n    // Your code here\n    return head;\n}\n\nint main() {\n    // Read input\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nstruct Node { int data; Node* next; Node(int v) : data(v), next(nullptr) {} };\n\nNode* middleNode(Node* head) {\n    // Your code here\n    return head;\n}",
            "java": "import java.util.*;\n\nclass Node { int data; Node next; Node(int d) { data = d; } }\n\npublic class Main {\n    public static Node middleNode(Node head) {\n        // Your code here\n        return head;\n    }\n}",
            "python": "def middleNode(head):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* middleNode(struct Node* head) {
    struct Node *slow = head;
    struct Node *fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

int main() {
    int val;
    struct Node *head = NULL, *tail = NULL;
    while (scanf("%d", &val) == 1) {
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = val; temp->next = NULL;
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
    }
    struct Node *mid = middleNode(head);
    if (mid) printf("%d\\n", mid->data);
    return 0;
}""",
            "cpp": """#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int v) : data(v), next(nullptr) {}
};

Node* middleNode(Node* head) {
    Node *slow = head;
    Node *fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

int main() {
    int x;
    Node *head = nullptr, *tail = nullptr;
    while (cin >> x) {
        Node* temp = new Node(x);
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
    }
    Node *mid = middleNode(head);
    if (mid) cout << mid->data << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

class Node {
    int data;
    Node next;
    Node(int d) { data = d; }
}

public class Main {
    public static Node middleNode(Node head) {
        Node slow = head;
        Node fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Node head = null, tail = null;
        while (sc.hasNextInt()) {
            Node temp = new Node(sc.nextInt());
            if (head == null) head = tail = temp;
            else { tail.next = temp; tail = temp; }
        }
        Node mid = middleNode(head);
        if (mid != null) System.out.println(mid.data);
    }
}""",
            "python": """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def createList(arr):
    head = Node(arr[0]) if arr else None
    curr = head
    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next
    return head

if __name__ == '__main__':
    import sys
    tokens = sys.stdin.read().split()
    if tokens:
        arr = [int(x) for x in tokens]
        head = createList(arr)
        mid = middleNode(head)
        print(mid.data if mid else "")"""
        })
    },

    # 3. Detect a Loop in Linked List
    {
        "id": "dsa-ll-detect-loop",
        "problem_num": 78,
        "title": "Detect a Loop in Linked List",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Floyd's Cycle-Finding Algorithm",
        "difficulty": "EASY",
        "description": "Given the head of a linked list, determine whether the linked list contains a cycle. Return True if a cycle exists; otherwise, return False.",
        "input_format": "Line 1: N and pos (pos is 0-indexed position that tail points to, or -1 for no cycle)\nLine 2: N space-separated integers",
        "output_format": "true or false",
        "constraints": "1 <= N <= 10^4\n-1 <= pos < N",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "company_tags": ["Amazon", "Microsoft", "Samsung"],
        "examples": [
            {"input": "4 1\\n1 2 3 4", "output": "true", "explanation": "Tail connects to index 1."},
            {"input": "4 -1\\n1 2 3 4", "output": "false", "explanation": "No cycle."},
            {"input": "1 0\\n1", "output": "true", "explanation": "Cycle to itself."}
        ],
        "test_cases": [
            {"input": "4 1\n1 2 3 4", "expected": "true", "is_hidden": False},
            {"input": "4 -1\n1 2 3 4", "expected": "false", "is_hidden": False},
            {"input": "1 0\n1", "expected": "true", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdbool.h>\n\nstruct Node { int data; struct Node* next; };\n\nbool hasCycle(struct Node* head) {\n    // Your code here\n    return false;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nstruct Node { int data; Node* next; Node(int v) : data(v), next(nullptr) {} };\n\nbool hasCycle(Node* head) {\n    // Your code here\n    return false;\n}",
            "java": "import java.util.*;\n\nclass Node { int data; Node next; Node(int d) { data = d; } }\n\npublic class Main {\n    public static boolean hasCycle(Node head) {\n        // Your code here\n        return false;\n    }\n}",
            "python": "def hasCycle(head):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

bool hasCycle(struct Node* head) {
    struct Node *slow = head;
    struct Node *fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}

int main() {
    int n, pos;
    if (scanf("%d %d", &n, &pos) != 2) return 0;
    struct Node* nodes[n];
    for (int i = 0; i < n; i++) {
        int v; scanf("%d", &v);
        nodes[i] = (struct Node*)malloc(sizeof(struct Node));
        nodes[i]->data = v;
        nodes[i]->next = NULL;
        if (i > 0) nodes[i - 1]->next = nodes[i];
    }
    if (pos >= 0 && pos < n) nodes[n - 1]->next = nodes[pos];
    printf("%s\\n", hasCycle(nodes[0]) ? "true" : "false");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int v) : data(v), next(nullptr) {}
};

bool hasCycle(Node* head) {
    Node *slow = head;
    Node *fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}

int main() {
    int n, pos;
    if (cin >> n >> pos) {
        vector<Node*> nodes(n);
        for (int i = 0; i < n; i++) {
            int v; cin >> v;
            nodes[i] = new Node(v);
            if (i > 0) nodes[i - 1]->next = nodes[i];
        }
        if (pos >= 0 && pos < n) nodes[n - 1]->next = nodes[pos];
        cout << (hasCycle(nodes[0]) ? "true" : "false") << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

class Node {
    int data;
    Node next;
    Node(int d) { data = d; }
}

public class Main {
    public static boolean hasCycle(Node head) {
        Node slow = head;
        Node fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int pos = sc.nextInt();
            Node[] nodes = new Node[n];
            for (int i = 0; i < n; i++) {
                nodes[i] = new Node(sc.nextInt());
                if (i > 0) nodes[i - 1].next = nodes[i];
            }
            if (pos >= 0 && pos < n) nodes[n - 1].next = nodes[pos];
            System.out.println(hasCycle(nodes[0]) ? "true" : "false");
        }
    }
}""",
            "python": """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

if __name__ == '__main__':
    import sys
    lines = sys.stdin.read().split()
    if len(lines) >= 2:
        n, pos = int(lines[0]), int(lines[1])
        vals = [int(x) for x in lines[2:2 + n]]
        nodes = [Node(v) for v in vals]
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]
        if 0 <= pos < n:
            nodes[-1].next = nodes[pos]
        print("true" if hasCycle(nodes[0]) else "false")"""
        })
    },

    # 4. Remove Duplicates from Sorted Linked List
    {
        "id": "dsa-ll-remove-duplicates",
        "problem_num": 79,
        "title": "Remove Duplicates from Sorted Linked List",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Pointers & Node Deletion",
        "difficulty": "EASY",
        "description": "Given the head of a sorted linked list, remove all duplicate elements so that each element appears only once.",
        "input_format": "Space-separated sorted integers.",
        "output_format": "Space-separated integers without duplicates.",
        "constraints": "1 <= number of nodes <= 300\n-100 <= Node.val <= 100",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "company_tags": ["Microsoft", "Adobe"],
        "examples": [
            {"input": "1 1 2 3 3", "output": "1 2 3", "explanation": "Duplicates removed."},
            {"input": "1 1 1 1", "output": "1", "explanation": "Reduced to 1 node."},
            {"input": "1 2 3 4", "output": "1 2 3 4", "explanation": "Already distinct."}
        ],
        "test_cases": [
            {"input": "1 1 2 3 3", "expected": "1 2 3", "is_hidden": False},
            {"input": "1 1 1 1", "expected": "1", "is_hidden": False},
            {"input": "1 2 3 4", "expected": "1 2 3 4", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nstruct Node { int data; struct Node* next; };\n\nstruct Node* removeDuplicates(struct Node* head) {\n    // Your code here\n    return head;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nstruct Node { int data; Node* next; Node(int v) : data(v), next(nullptr) {} };\n\nNode* removeDuplicates(Node* head) {\n    // Your code here\n    return head;\n}",
            "java": "import java.util.*;\n\nclass Node { int data; Node next; Node(int d) { data = d; } }\n\npublic class Main {\n    public static Node removeDuplicates(Node head) {\n        // Your code here\n        return head;\n    }\n}",
            "python": "def removeDuplicates(head):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* removeDuplicates(struct Node* head) {
    struct Node *curr = head;
    while (curr && curr->next) {
        if (curr->data == curr->next->data) {
            struct Node *dup = curr->next;
            curr->next = curr->next->next;
            free(dup);
        } else {
            curr = curr->next;
        }
    }
    return head;
}

int main() {
    int val;
    struct Node *head = NULL, *tail = NULL;
    while (scanf("%d", &val) == 1) {
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = val; temp->next = NULL;
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
    }
    head = removeDuplicates(head);
    while (head) {
        printf("%d%s", head->data, head->next ? " " : "\\n");
        head = head->next;
    }
    return 0;
}""",
            "cpp": """#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int v) : data(v), next(nullptr) {}
};

Node* removeDuplicates(Node* head) {
    Node *curr = head;
    while (curr && curr->next) {
        if (curr->data == curr->next->data) {
            Node *dup = curr->next;
            curr->next = curr->next->next;
            delete dup;
        } else {
            curr = curr->next;
        }
    }
    return head;
}

int main() {
    int x;
    Node *head = nullptr, *tail = nullptr;
    while (cin >> x) {
        Node* temp = new Node(x);
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
    }
    head = removeDuplicates(head);
    while (head) {
        cout << head->data << (head->next ? " " : "\\n");
        head = head->next;
    }
    return 0;
}""",
            "java": """import java.util.*;

class Node {
    int data;
    Node next;
    Node(int d) { data = d; }
}

public class Main {
    public static Node removeDuplicates(Node head) {
        Node curr = head;
        while (curr != null && curr.next != null) {
            if (curr.data == curr.next.data) {
                curr.next = curr.next.next;
            } else {
                curr = curr.next;
            }
        }
        return head;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Node head = null, tail = null;
        while (sc.hasNextInt()) {
            Node temp = new Node(sc.nextInt());
            if (head == null) head = tail = temp;
            else { tail.next = temp; tail = temp; }
        }
        head = removeDuplicates(head);
        while (head != null) {
            System.out.print(head.data + (head.next != null ? " " : "\\n"));
            head = head.next;
        }
    }
}""",
            "python": """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDuplicates(head):
    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

def createList(arr):
    head = Node(arr[0]) if arr else None
    curr = head
    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next
    return head

def printList(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print(*result)

if __name__ == '__main__':
    import sys
    tokens = sys.stdin.read().split()
    if tokens:
        arr = [int(x) for x in tokens]
        head = createList(arr)
        head = removeDuplicates(head)
        printList(head)"""
        })
    },

    # 5. Delete a Node in Linked List
    {
        "id": "dsa-ll-delete-node",
        "problem_num": 80,
        "title": "Delete a Node in Linked List",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Linear Search & Pointer Update",
        "difficulty": "EASY",
        "description": "Given the head of a linked list and an integer value key, delete the first occurrence of that value and return the updated head.",
        "input_format": "Line 1: Space-separated integers representing the list\nLine 2: Target integer key to delete",
        "output_format": "Space-separated integers of the updated list.",
        "constraints": "1 <= number of nodes <= 1000\n-1000 <= Node.val <= 1000",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "company_tags": ["TCS", "Infosys", "Wipro"],
        "examples": [
            {"input": "1 2 3 4 5\\n3", "output": "1 2 4 5", "explanation": "Node 3 deleted."},
            {"input": "1 2 3\\n1", "output": "2 3", "explanation": "Head node 1 deleted."},
            {"input": "1 2 3\\n5", "output": "1 2 3", "explanation": "5 not present, list unchanged."}
        ],
        "test_cases": [
            {"input": "1 2 3 4 5\n3", "expected": "1 2 4 5", "is_hidden": False},
            {"input": "1 2 3\n1", "expected": "2 3", "is_hidden": False},
            {"input": "1 2 3\n5", "expected": "1 2 3", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nstruct Node { int data; struct Node* next; };\n\nstruct Node* deleteNode(struct Node* head, int key) {\n    // Your code here\n    return head;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nstruct Node { int data; Node* next; Node(int v) : data(v), next(nullptr) {} };\n\nNode* deleteNode(Node* head, int key) {\n    // Your code here\n    return head;\n}",
            "java": "import java.util.*;\n\nclass Node { int data; Node next; Node(int d) { data = d; } }\n\npublic class Main {\n    public static Node deleteNode(Node head, int key) {\n        // Your code here\n        return head;\n    }\n}",
            "python": "def deleteNode(head, key):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* deleteNode(struct Node* head, int key) {
    if (!head) return NULL;
    if (head->data == key) {
        struct Node *temp = head->next;
        free(head);
        return temp;
    }
    struct Node *curr = head;
    while (curr->next) {
        if (curr->next->data == key) {
            struct Node *to_del = curr->next;
            curr->next = curr->next->next;
            free(to_del);
            break;
        }
        curr = curr->next;
    }
    return head;
}

int main() {
    int arr[1000]; int n = 0, key;
    char line[10000];
    if (fgets(line, sizeof(line), stdin)) {
        char *ptr = line; int v, off;
        while (sscanf(ptr, "%d%n", &v, &off) == 1) { arr[n++] = v; ptr += off; }
    }
    if (scanf("%d", &key) != 1) return 0;
    struct Node *head = NULL, *tail = NULL;
    for (int i = 0; i < n; i++) {
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = arr[i]; temp->next = NULL;
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
    }
    head = deleteNode(head, key);
    while (head) {
        printf("%d%s", head->data, head->next ? " " : "\\n");
        head = head->next;
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int v) : data(v), next(nullptr) {}
};

Node* deleteNode(Node* head, int key) {
    if (!head) return nullptr;
    if (head->data == key) {
        Node *temp = head->next;
        delete head;
        return temp;
    }
    Node *curr = head;
    while (curr->next) {
        if (curr->next->data == key) {
            Node *to_del = curr->next;
            curr->next = curr->next->next;
            delete to_del;
            break;
        }
        curr = curr->next;
    }
    return head;
}

int main() {
    string line;
    if (getline(cin, line)) {
        stringstream ss(line);
        int v, key;
        Node *head = nullptr, *tail = nullptr;
        while (ss >> v) {
            Node *temp = new Node(v);
            if (!head) head = tail = temp;
            else { tail->next = temp; tail = temp; }
        }
        if (cin >> key) {
            head = deleteNode(head, key);
            while (head) {
                cout << head->data << (head->next ? " " : "\\n");
                head = head->next;
            }
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

public class Main {
    public static Node deleteNode(Node head, int key) {
        if (head == null) return null;
        if (head.data == key) return head.next;
        Node curr = head;
        while (curr.next != null) {
            if (curr.next.data == key) {
                curr.next = curr.next.next;
                break;
            }
            curr = curr.next;
        }
        return head;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String[] tokens = sc.nextLine().trim().split("\\\\s+");
            if (sc.hasNextInt()) {
                int key = sc.nextInt();
                Node head = null, tail = null;
                for (String t : tokens) {
                    if (t.isEmpty()) continue;
                    Node temp = new Node(Integer.parseInt(t));
                    if (head == null) head = tail = temp;
                    else { tail.next = temp; tail = temp; }
                }
                head = deleteNode(head, key);
                while (head != null) {
                    System.out.print(head.data + (head.next != null ? " " : "\\n"));
                    head = head.next;
                }
            }
        }
    }
}""",
            "python": """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteNode(head, key):
    if head is None:
        return None
    if head.data == key:
        return head.next

    curr = head
    while curr.next:
        if curr.next.data == key:
            curr.next = curr.next.next
            break
        curr = curr.next
    return head

def createList(arr):
    head = Node(arr[0]) if arr else None
    curr = head
    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next
    return head

def printList(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print(*result)

if __name__ == '__main__':
    import sys
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    if len(lines) >= 2:
        arr = list(map(int, lines[0].split()))
        key = int(lines[1])
        head = createList(arr)
        head = deleteNode(head, key)
        printList(head)"""
        })
    },

    # 6. Merge Two Sorted Linked Lists
    {
        "id": "dsa-ll-merge-two-sorted",
        "problem_num": 81,
        "title": "Merge Two Sorted Linked Lists",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Sorted Merge & Dummy Node",
        "difficulty": "MEDIUM",
        "description": "Given the heads of two sorted linked lists, merge them into one sorted linked list and return its head.",
        "input_format": "Line 1: Space-separated integers of list 1\nLine 2: Space-separated integers of list 2",
        "output_format": "Space-separated merged sorted integers.",
        "constraints": "The number of nodes in both lists is in range [0, 50].\n-100 <= Node.val <= 100",
        "time_complexity": "O(M + N)",
        "space_complexity": "O(1)",
        "company_tags": ["Amazon", "Apple", "Microsoft"],
        "examples": [
            {"input": "1 2 4\\n1 3 4", "output": "1 1 2 3 4 4", "explanation": "Merged list in sorted order."},
            {"input": "1 3 5\\n2 4 6", "output": "1 2 3 4 5 6", "explanation": "Alternating merge."},
            {"input": "1 2 3\\n", "output": "1 2 3", "explanation": "Second list empty."}
        ],
        "test_cases": [
            {"input": "1 2 4\n1 3 4", "expected": "1 1 2 3 4 4", "is_hidden": False},
            {"input": "1 3 5\n2 4 6", "expected": "1 2 3 4 5 6", "is_hidden": False},
            {"input": "1 2 3", "expected": "1 2 3", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nstruct Node { int data; struct Node* next; };\n\nstruct Node* mergeTwoLists(struct Node* l1, struct Node* l2) {\n    // Your code here\n    return NULL;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nstruct Node { int data; Node* next; Node(int v) : data(v), next(nullptr) {} };\n\nNode* mergeTwoLists(Node* l1, Node* l2) {\n    // Your code here\n    return nullptr;\n}",
            "java": "import java.util.*;\n\nclass Node { int data; Node next; Node(int d) { data = d; } }\n\npublic class Main {\n    public static Node mergeTwoLists(Node l1, Node l2) {\n        // Your code here\n        return null;\n    }\n}",
            "python": "def mergeTwoLists(l1, l2):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* mergeTwoLists(struct Node* l1, struct Node* l2) {
    struct Node dummy;
    dummy.next = NULL;
    struct Node *curr = &dummy;

    while (l1 && l2) {
        if (l1->data <= l2->data) {
            curr->next = l1;
            l1 = l1->next;
        } else {
            curr->next = l2;
            l2 = l2->next;
        }
        curr = curr->next;
    }
    curr->next = l1 ? l1 : l2;
    return dummy.next;
}

struct Node* buildList(char *line) {
    char *ptr = line; int v, off;
    struct Node *head = NULL, *tail = NULL;
    while (sscanf(ptr, "%d%n", &v, &off) == 1) {
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = v; temp->next = NULL;
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
        ptr += off;
    }
    return head;
}

int main() {
    char l1[1000], l2[1000];
    struct Node *list1 = NULL, *list2 = NULL;
    if (fgets(l1, sizeof(l1), stdin)) list1 = buildList(l1);
    if (fgets(l2, sizeof(l2), stdin)) list2 = buildList(l2);
    struct Node *res = mergeTwoLists(list1, list2);
    while (res) {
        printf("%d%s", res->data, res->next ? " " : "\\n");
        res = res->next;
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <sstream>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int v) : data(v), next(nullptr) {}
};

Node* mergeTwoLists(Node* l1, Node* l2) {
    Node dummy(0);
    Node *curr = &dummy;

    while (l1 && l2) {
        if (l1->data <= l2->data) {
            curr->next = l1;
            l1 = l1->next;
        } else {
            curr->next = l2;
            l2 = l2->next;
        }
        curr = curr->next;
    }
    curr->next = l1 ? l1 : l2;
    return dummy.next;
}

Node* buildList(const string& line) {
    stringstream ss(line);
    int v;
    Node *head = nullptr, *tail = nullptr;
    while (ss >> v) {
        Node *temp = new Node(v);
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
    }
    return head;
}

int main() {
    string l1, l2;
    Node *list1 = nullptr, *list2 = nullptr;
    if (getline(cin, l1)) list1 = buildList(l1);
    if (getline(cin, l2)) list2 = buildList(l2);
    Node *res = mergeTwoLists(list1, list2);
    while (res) {
        cout << res->data << (res->next ? " " : "\\n");
        res = res->next;
    }
    return 0;
}""",
            "java": """import java.util.*;

class Node {
    int data;
    Node next;
    Node(int d) { data = d; }
}

public class Main {
    public static Node mergeTwoLists(Node l1, Node l2) {
        Node dummy = new Node(0);
        Node curr = dummy;

        while (l1 != null && l2 != null) {
            if (l1.data <= l2.data) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        curr.next = l1 != null ? l1 : l2;
        return dummy.next;
    }

    public static Node buildList(String line) {
        if (line == null || line.trim().isEmpty()) return null;
        String[] tokens = line.trim().split("\\\\s+");
        Node head = null, tail = null;
        for (String t : tokens) {
            if (t.isEmpty()) continue;
            Node temp = new Node(Integer.parseInt(t));
            if (head == null) head = tail = temp;
            else { tail.next = temp; tail = temp; }
        }
        return head;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Node list1 = null, list2 = null;
        if (sc.hasNextLine()) list1 = buildList(sc.nextLine());
        if (sc.hasNextLine()) list2 = buildList(sc.nextLine());
        Node res = mergeTwoLists(list1, list2);
        while (res != null) {
            System.out.print(res.data + (res.next != null ? " " : "\\n"));
            res = res.next;
        }
    }
}""",
            "python": """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeTwoLists(list1, list2):
    dummy = Node(0)
    curr = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    curr.next = list1 if list1 else list2
    return dummy.next

def createList(arr):
    dummy = Node(0)
    curr = dummy
    for x in arr:
        curr.next = Node(x)
        curr = curr.next
    return dummy.next

def printList(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print(*result)

if __name__ == '__main__':
    import sys
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    a = list(map(int, lines[0].split())) if len(lines) >= 1 else []
    b = list(map(int, lines[1].split())) if len(lines) >= 2 else []
    res = mergeTwoLists(createList(a), createList(b))
    printList(res)"""
        })
    },

    # 7. Remove Nth Node From End
    {
        "id": "dsa-ll-remove-nth-from-end",
        "problem_num": 82,
        "title": "Remove Nth Node From End of List",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Fast-Slow Pointer Gap",
        "difficulty": "MEDIUM",
        "description": "Given the head of a linked list, remove the nth node from the end of the list and return its head.",
        "input_format": "Line 1: Space-separated integers representing nodes\nLine 2: Target integer n",
        "output_format": "Space-separated integers of the updated list.",
        "constraints": "The number of nodes in list is sz.\n1 <= sz <= 30\n1 <= n <= sz",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "company_tags": ["Amazon", "Facebook", "Microsoft"],
        "examples": [
            {"input": "1 2 3 4 5\\n2", "output": "1 2 3 5", "explanation": "2nd node from end (4) removed."},
            {"input": "1\\n1", "output": "", "explanation": "Single node removed resulting in empty list."},
            {"input": "1 2\\n1", "output": "1", "explanation": "Tail node removed."}
        ],
        "test_cases": [
            {"input": "1 2 3 4 5\n2", "expected": "1 2 3 5", "is_hidden": False},
            {"input": "1\n1", "expected": "", "is_hidden": False},
            {"input": "1 2\n1", "expected": "1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nstruct Node { int data; struct Node* next; };\n\nstruct Node* removeNthFromEnd(struct Node* head, int n) {\n    // Your code here\n    return head;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nstruct Node { int data; Node* next; Node(int v) : data(v), next(nullptr) {} };\n\nNode* removeNthFromEnd(Node* head, int n) {\n    // Your code here\n    return head;\n}",
            "java": "import java.util.*;\n\nclass Node { int data; Node next; Node(int d) { data = d; } }\n\npublic class Main {\n    public static Node removeNthFromEnd(Node head, int n) {\n        // Your code here\n        return head;\n    }\n}",
            "python": "def removeNthFromEnd(head, n):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* removeNthFromEnd(struct Node* head, int n) {
    struct Node dummy;
    dummy.data = 0;
    dummy.next = head;

    struct Node *fast = &dummy;
    struct Node *slow = &dummy;

    for (int i = 0; i < n; i++) {
        if (!fast->next) return head;
        fast = fast->next;
    }
    while (fast->next) {
        slow = slow->next;
        fast = fast->next;
    }
    struct Node *to_del = slow->next;
    slow->next = slow->next->next;
    free(to_del);
    return dummy.next;
}

int main() {
    char line[10000];
    int n;
    if (!fgets(line, sizeof(line), stdin)) return 0;
    if (scanf("%d", &n) != 1) return 0;

    struct Node *head = NULL, *tail = NULL;
    char *ptr = line; int v, off;
    while (sscanf(ptr, "%d%n", &v, &off) == 1) {
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = v; temp->next = NULL;
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
        ptr += off;
    }
    head = removeNthFromEnd(head, n);
    while (head) {
        printf("%d%s", head->data, head->next ? " " : "\\n");
        head = head->next;
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <sstream>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int v) : data(v), next(nullptr) {}
};

Node* removeNthFromEnd(Node* head, int n) {
    Node dummy(0);
    dummy.next = head;

    Node *slow = &dummy;
    Node *fast = &dummy;

    for (int i = 0; i < n; i++) {
        if (!fast->next) return head;
        fast = fast->next;
    }
    while (fast->next) {
        slow = slow->next;
        fast = fast->next;
    }
    slow->next = slow->next->next;
    return dummy.next;
}

int main() {
    string line;
    if (getline(cin, line)) {
        int n;
        if (cin >> n) {
            stringstream ss(line);
            int v;
            Node *head = nullptr, *tail = nullptr;
            while (ss >> v) {
                Node *temp = new Node(v);
                if (!head) head = tail = temp;
                else { tail->next = temp; tail = temp; }
            }
            head = removeNthFromEnd(head, n);
            while (head) {
                cout << head->data << (head->next ? " " : "\\n");
                head = head->next;
            }
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

public class Main {
    public static Node removeNthFromEnd(Node head, int n) {
        Node dummy = new Node(0);
        dummy.next = head;

        Node slow = dummy;
        Node fast = dummy;

        for (int i = 0; i < n; i++) {
            if (fast.next == null) return head;
            fast = fast.next;
        }
        while (fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }
        slow.next = slow.next.next;
        return dummy.next;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String[] tokens = sc.nextLine().trim().split("\\\\s+");
            if (sc.hasNextInt()) {
                int n = sc.nextInt();
                Node head = null, tail = null;
                for (String t : tokens) {
                    if (t.isEmpty()) continue;
                    Node temp = new Node(Integer.parseInt(t));
                    if (head == null) head = tail = temp;
                    else { tail.next = temp; tail = temp; }
                }
                head = removeNthFromEnd(head, n);
                while (head != null) {
                    System.out.print(head.data + (head.next != null ? " " : "\\n"));
                    head = head.next;
                }
            }
        }
    }
}""",
            "python": """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeNthFromEnd(head, n):
    dummy = Node(0)
    dummy.next = head
    slow = dummy
    fast = dummy

    for i in range(n):
        if fast.next is None:
            return head
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next

def createList(arr):
    dummy = Node(0)
    curr = dummy
    for x in arr:
        curr.next = Node(x)
        curr = curr.next
    return dummy.next

def printList(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    if result:
        print(*result)

if __name__ == '__main__':
    import sys
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    if len(lines) >= 2:
        arr = list(map(int, lines[0].split()))
        n = int(lines[1])
        head = createList(arr)
        head = removeNthFromEnd(head, n)
        printList(head)"""
        })
    },

    # 8. Intersection of Two Linked Lists
    {
        "id": "dsa-ll-intersection",
        "problem_num": 83,
        "title": "Intersection of Two Linked Lists",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Pointer Cycle Switching",
        "difficulty": "MEDIUM",
        "description": "Given the heads of two singly linked lists, find the node value at which the two lists intersect. If they do not intersect, return None.",
        "input_format": "Line 1: Elements of list A preceding intersection, or full list\nLine 2: Elements of list B preceding intersection\nLine 3: Shared elements after intersection, or -1 for None",
        "output_format": "Intersection node value or None.",
        "constraints": "The number of nodes in each list is in range [1, 3 * 10^4].",
        "time_complexity": "O(M + N)",
        "space_complexity": "O(1)",
        "company_tags": ["Amazon", "Microsoft", "Airbnb"],
        "examples": [
            {"input": "4 1\\n5 6 1\\n8 4 5", "output": "8", "explanation": "Intersect at 8."},
            {"input": "1 2 3\\n4 5 6\\n-1", "output": "None", "explanation": "No intersection."},
            {"input": "1 2\\n\\n3", "output": "3", "explanation": "Intersect at 3."}
        ],
        "test_cases": [
            {"input": "4 1\n5 6 1\n8 4 5", "expected": "8", "is_hidden": False},
            {"input": "1 2 3\n4 5 6\n-1", "expected": "None", "is_hidden": False},
            {"input": "1 2\n\n3", "expected": "3", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nstruct Node { int data; struct Node* next; };\n\nstruct Node* getIntersectionNode(struct Node* headA, struct Node* headB) {\n    // Your code here\n    return NULL;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nstruct Node { int data; Node* next; Node(int v) : data(v), next(nullptr) {} };\n\nNode* getIntersectionNode(Node* headA, Node* headB) {\n    // Your code here\n    return nullptr;\n}",
            "java": "import java.util.*;\n\nclass Node { int data; Node next; Node(int d) { data = d; } }\n\npublic class Main {\n    public static Node getIntersectionNode(Node headA, Node headB) {\n        // Your code here\n        return null;\n    }\n}",
            "python": "def getIntersectionNode(headA, headB):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* getIntersectionNode(struct Node* headA, struct Node* headB) {
    struct Node *a = headA;
    struct Node *b = headB;

    while (a != b) {
        a = (a == NULL) ? headB : a->next;
        b = (b == NULL) ? headA : b->next;
    }
    return a;
}

int main() {
    char l1[1000], l2[1000], l3[1000];
    if (!fgets(l1, sizeof(l1), stdin)) return 0;
    if (!fgets(l2, sizeof(l2), stdin)) return 0;
    if (!fgets(l3, sizeof(l3), stdin)) return 0;

    struct Node *shared = NULL, *stail = NULL;
    char *ptr = l3; int v, off;
    while (sscanf(ptr, "%d%n", &v, &off) == 1) {
        if (v == -1) break;
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = v; temp->next = NULL;
        if (!shared) shared = stail = temp;
        else { stail->next = temp; stail = temp; }
        ptr += off;
    }

    struct Node *headA = NULL, *tailA = NULL;
    ptr = l1;
    while (sscanf(ptr, "%d%n", &v, &off) == 1) {
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = v; temp->next = NULL;
        if (!headA) headA = tailA = temp;
        else { tailA->next = temp; tailA = temp; }
        ptr += off;
    }
    if (tailA) tailA->next = shared;
    else headA = shared;

    struct Node *headB = NULL, *tailB = NULL;
    ptr = l2;
    while (sscanf(ptr, "%d%n", &v, &off) == 1) {
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = v; temp->next = NULL;
        if (!headB) headB = tailB = temp;
        else { tailB->next = temp; tailB = temp; }
        ptr += off;
    }
    if (tailB) tailB->next = shared;
    else headB = shared;

    struct Node *ans = getIntersectionNode(headA, headB);
    if (ans) printf("%d\\n", ans->data);
    else printf("None\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <sstream>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int v) : data(v), next(nullptr) {}
};

Node* getIntersectionNode(Node* headA, Node* headB) {
    Node *a = headA;
    Node *b = headB;

    while (a != b) {
        a = (a == nullptr) ? headB : a->next;
        b = (b == nullptr) ? headA : b->next;
    }
    return a;
}

int main() {
    string l1, l2, l3;
    if (getline(cin, l1) && getline(cin, l2) && getline(cin, l3)) {
        stringstream ss3(l3);
        int v;
        Node *shared = nullptr, *stail = nullptr;
        while (ss3 >> v) {
            if (v == -1) break;
            Node *temp = new Node(v);
            if (!shared) shared = stail = temp;
            else { stail->next = temp; stail = temp; }
        }

        stringstream ss1(l1), ss2(l2);
        Node *headA = nullptr, *tailA = nullptr;
        while (ss1 >> v) {
            Node *temp = new Node(v);
            if (!headA) headA = tailA = temp;
            else { tailA->next = temp; tailA = temp; }
        }
        if (tailA) tailA->next = shared;
        else headA = shared;

        Node *headB = nullptr, *tailB = nullptr;
        while (ss2 >> v) {
            Node *temp = new Node(v);
            if (!headB) headB = tailB = temp;
            else { tailB->next = temp; tailB = temp; }
        }
        if (tailB) tailB->next = shared;
        else headB = shared;

        Node *ans = getIntersectionNode(headA, headB);
        if (ans) cout << ans->data << "\\n";
        else cout << "None\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

class Node {
    int data;
    Node next;
    Node(int d) { data = d; }
}

public class Main {
    public static Node getIntersectionNode(Node headA, Node headB) {
        Node a = headA;
        Node b = headB;

        while (a != b) {
            a = (a == null) ? headB : a.next;
            b = (b == null) ? headA : b.next;
        }
        return a;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String l1 = sc.nextLine();
            String l2 = sc.hasNextLine() ? sc.nextLine() : "";
            String l3 = sc.hasNextLine() ? sc.nextLine() : "";

            Node shared = null, stail = null;
            if (!l3.trim().isEmpty() && !l3.trim().equals("-1")) {
                for (String t : l3.trim().split("\\\\s+")) {
                    if (t.isEmpty() || t.equals("-1")) continue;
                    Node temp = new Node(Integer.parseInt(t));
                    if (shared == null) shared = stail = temp;
                    else { stail.next = temp; stail = temp; }
                }
            }

            Node headA = null, tailA = null;
            if (!l1.trim().isEmpty()) {
                for (String t : l1.trim().split("\\\\s+")) {
                    if (t.isEmpty()) continue;
                    Node temp = new Node(Integer.parseInt(t));
                    if (headA == null) headA = tailA = temp;
                    else { tailA.next = temp; tailA = temp; }
                }
            }
            if (tailA != null) tailA.next = shared;
            else headA = shared;

            Node headB = null, tailB = null;
            if (!l2.trim().isEmpty()) {
                for (String t : l2.trim().split("\\\\s+")) {
                    if (t.isEmpty()) continue;
                    Node temp = new Node(Integer.parseInt(t));
                    if (headB == null) headB = tailB = temp;
                    else { tailB.next = temp; tailB = temp; }
                }
            }
            if (tailB != null) tailB.next = shared;
            else headB = shared;

            Node ans = getIntersectionNode(headA, headB);
            if (ans != null) System.out.println(ans.data);
            else System.out.println("None");
        }
    }
}""",
            "python": """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getIntersectionNode(headA, headB):
    a = headA
    b = headB

    while a != b:
        a = headB if a is None else a.next
        b = headA if b is None else b.next

    return a

if __name__ == '__main__':
    import sys
    lines = [line.strip() for line in sys.stdin.readlines()]
    while len(lines) < 3:
        lines.append("")

    l1, l2, l3 = lines[0], lines[1], lines[2]

    shared = None
    stail = None
    if l3 and l3 != "-1":
        for x in map(int, l3.split()):
            temp = Node(x)
            if not shared: shared = stail = temp
            else: stail.next = temp; stail = temp

    headA, tailA = None, None
    if l1:
        for x in map(int, l1.split()):
            temp = Node(x)
            if not headA: headA = tailA = temp
            else: tailA.next = temp; tailA = temp
    if tailA: tailA.next = shared
    else: headA = shared

    headB, tailB = None, None
    if l2:
        for x in map(int, l2.split()):
            temp = Node(x)
            if not headB: headB = tailB = temp
            else: tailB.next = temp; tailB = temp
    if tailB: tailB.next = shared
    else: headB = shared

    ans = getIntersectionNode(headA, headB)
    print(ans.data if ans else "None")"""
        })
    },

    # 9. Add Two Numbers
    {
        "id": "dsa-ll-add-two-numbers",
        "problem_num": 84,
        "title": "Add Two Numbers",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Arithmetic Simulation & Carry",
        "difficulty": "MEDIUM",
        "description": "Given two non-empty linked lists representing two non-negative integers in reverse order, add the two numbers and return the sum as a linked list.",
        "input_format": "Line 1: Space-separated digits of first number in reverse\nLine 2: Space-separated digits of second number in reverse",
        "output_format": "Space-separated digits of sum in reverse.",
        "constraints": "Number of nodes in each list is in range [1, 100].\n0 <= Node.val <= 9",
        "time_complexity": "O(max(N, M))",
        "space_complexity": "O(max(N, M))",
        "company_tags": ["Amazon", "Bloomberg", "Google"],
        "examples": [
            {"input": "2 4 3\\n5 6 4", "output": "7 0 8", "explanation": "342 + 465 = 807."},
            {"input": "0\\n0", "output": "0", "explanation": "0 + 0 = 0."},
            {"input": "9 9 9\\n1", "output": "0 0 0 1", "explanation": "999 + 1 = 1000."}
        ],
        "test_cases": [
            {"input": "2 4 3\n5 6 4", "expected": "7 0 8", "is_hidden": False},
            {"input": "0\n0", "expected": "0", "is_hidden": False},
            {"input": "9 9 9\n1", "expected": "0 0 0 1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nstruct Node { int data; struct Node* next; };\n\nstruct Node* addTwoNumbers(struct Node* l1, struct Node* l2) {\n    // Your code here\n    return NULL;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nstruct Node { int data; Node* next; Node(int v) : data(v), next(nullptr) {} };\n\nNode* addTwoNumbers(Node* l1, Node* l2) {\n    // Your code here\n    return nullptr;\n}",
            "java": "import java.util.*;\n\nclass Node { int data; Node next; Node(int d) { data = d; } }\n\npublic class Main {\n    public static Node addTwoNumbers(Node l1, Node l2) {\n        // Your code here\n        return null;\n    }\n}",
            "python": "def addTwoNumbers(l1, l2):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* addTwoNumbers(struct Node* l1, struct Node* l2) {
    struct Node dummy;
    dummy.data = 0; dummy.next = NULL;
    struct Node *curr = &dummy;
    int carry = 0;

    while (l1 || l2 || carry) {
        int total = carry;
        if (l1) { total += l1->data; l1 = l1->next; }
        if (l2) { total += l2->data; l2 = l2->next; }

        carry = total / 10;
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = total % 10;
        temp->next = NULL;
        curr->next = temp;
        curr = curr->next;
    }
    return dummy.next;
}

int main() {
    char s1[1000], s2[1000];
    if (!fgets(s1, sizeof(s1), stdin)) return 0;
    if (!fgets(s2, sizeof(s2), stdin)) return 0;

    struct Node *l1 = NULL, *t1 = NULL;
    char *ptr = s1; int v, off;
    while (sscanf(ptr, "%d%n", &v, &off) == 1) {
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = v; temp->next = NULL;
        if (!l1) l1 = t1 = temp;
        else { t1->next = temp; t1 = temp; }
        ptr += off;
    }

    struct Node *l2 = NULL, *t2 = NULL;
    ptr = s2;
    while (sscanf(ptr, "%d%n", &v, &off) == 1) {
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = v; temp->next = NULL;
        if (!l2) l2 = t2 = temp;
        else { t2->next = temp; t2 = temp; }
        ptr += off;
    }

    struct Node *res = addTwoNumbers(l1, l2);
    while (res) {
        printf("%d%s", res->data, res->next ? " " : "\\n");
        res = res->next;
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <sstream>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int v) : data(v), next(nullptr) {}
};

Node* addTwoNumbers(Node* l1, Node* l2) {
    Node dummy(0);
    Node *curr = &dummy;
    int carry = 0;

    while (l1 || l2 || carry) {
        int total = carry;
        if (l1) { total += l1->data; l1 = l1->next; }
        if (l2) { total += l2->data; l2 = l2->next; }

        carry = total / 10;
        curr->next = new Node(total % 10);
        curr = curr->next;
    }
    return dummy.next;
}

int main() {
    string s1, s2;
    if (getline(cin, s1) && getline(cin, s2)) {
        stringstream ss1(s1), ss2(s2);
        int v;
        Node *l1 = nullptr, *t1 = nullptr;
        while (ss1 >> v) {
            Node *temp = new Node(v);
            if (!l1) l1 = t1 = temp;
            else { t1->next = temp; t1 = temp; }
        }
        Node *l2 = nullptr, *t2 = nullptr;
        while (ss2 >> v) {
            Node *temp = new Node(v);
            if (!l2) l2 = t2 = temp;
            else { t2->next = temp; t2 = temp; }
        }
        Node *res = addTwoNumbers(l1, l2);
        while (res) {
            cout << res->data << (res->next ? " " : "\\n");
            res = res->next;
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

public class Main {
    public static Node addTwoNumbers(Node l1, Node l2) {
        Node dummy = new Node(0);
        Node curr = dummy;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int total = carry;
            if (l1 != null) { total += l1.data; l1 = l1.next; }
            if (l2 != null) { total += l2.data; l2 = l2.next; }

            carry = total / 10;
            curr.next = new Node(total % 10);
            curr = curr.next;
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String[] s1 = sc.nextLine().trim().split("\\\\s+");
            String[] s2 = sc.hasNextLine() ? sc.nextLine().trim().split("\\\\s+") : new String[0];

            Node l1 = null, t1 = null;
            for (String t : s1) {
                if (t.isEmpty()) continue;
                Node temp = new Node(Integer.parseInt(t));
                if (l1 == null) l1 = t1 = temp;
                else { t1.next = temp; t1 = temp; }
            }

            Node l2 = null, t2 = null;
            for (String t : s2) {
                if (t.isEmpty()) continue;
                Node temp = new Node(Integer.parseInt(t));
                if (l2 == null) l2 = t2 = temp;
                else { t2.next = temp; t2 = temp; }
            }

            Node res = addTwoNumbers(l1, l2);
            while (res != null) {
                System.out.print(res.data + (res.next != null ? " " : "\\n"));
                res = res.next;
            }
        }
    }
}""",
            "python": """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addTwoNumbers(l1, l2):
    dummy = Node(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.data
            l1 = l1.next
        if l2:
            total += l2.data
            l2 = l2.next

        carry = total // 10
        curr.next = Node(total % 10)
        curr = curr.next

    return dummy.next

def createList(arr):
    dummy = Node(0)
    curr = dummy
    for x in arr:
        curr.next = Node(x)
        curr = curr.next
    return dummy.next

def printList(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print(*result)

if __name__ == '__main__':
    import sys
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    if len(lines) >= 2:
        a = list(map(int, lines[0].split()))
        b = list(map(int, lines[1].split()))
        head = addTwoNumbers(createList(a), createList(b))
        printList(head)"""
        })
    },

    # 10. Sort a Linked List
    {
        "id": "dsa-ll-sort-list",
        "problem_num": 85,
        "title": "Sort a Linked List",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Merge Sort on Linked List",
        "difficulty": "MEDIUM",
        "description": "Given the head of a linked list, sort the list in ascending order using Merge Sort in O(N log N) time.",
        "input_format": "Space-separated integers.",
        "output_format": "Space-separated sorted integers.",
        "constraints": "Number of nodes is in range [0, 5 * 10^4].\n-10^5 <= Node.val <= 10^5",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(log N)",
        "company_tags": ["Google", "Amazon", "Facebook"],
        "examples": [
            {"input": "4 2 1 3", "output": "1 2 3 4", "explanation": "Sorted via merge sort."},
            {"input": "-1 5 3 4 0", "output": "-1 0 3 4 5", "explanation": "Negative numbers sorted."},
            {"input": "5 4 3 2 1", "output": "1 2 3 4 5", "explanation": "Reversed list sorted."}
        ],
        "test_cases": [
            {"input": "4 2 1 3", "expected": "1 2 3 4", "is_hidden": False},
            {"input": "-1 5 3 4 0", "expected": "-1 0 3 4 5", "is_hidden": False},
            {"input": "5 4 3 2 1", "expected": "1 2 3 4 5", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nstruct Node { int data; struct Node* next; };\n\nstruct Node* sortList(struct Node* head) {\n    // Your code here\n    return head;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nstruct Node { int data; Node* next; Node(int v) : data(v), next(nullptr) {} };\n\nNode* sortList(Node* head) {\n    // Your code here\n    return head;\n}",
            "java": "import java.util.*;\n\nclass Node { int data; Node next; Node(int d) { data = d; } }\n\npublic class Main {\n    public static Node sortList(Node head) {\n        // Your code here\n        return head;\n    }\n}",
            "python": "def sortList(head):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* merge(struct Node* a, struct Node* b) {
    struct Node dummy; dummy.next = NULL;
    struct Node *curr = &dummy;
    while (a && b) {
        if (a->data <= b->data) { curr->next = a; a = a->next; }
        else { curr->next = b; b = b->next; }
        curr = curr->next;
    }
    curr->next = a ? a : b;
    return dummy.next;
}

struct Node* sortList(struct Node* head) {
    if (!head || !head->next) return head;

    struct Node *slow = head, *fast = head->next;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    struct Node *mid = slow->next;
    slow->next = NULL;

    struct Node *left = sortList(head);
    struct Node *right = sortList(mid);
    return merge(left, right);
}

int main() {
    int v;
    struct Node *head = NULL, *tail = NULL;
    while (scanf("%d", &v) == 1) {
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = v; temp->next = NULL;
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
    }
    head = sortList(head);
    while (head) {
        printf("%d%s", head->data, head->next ? " " : "\\n");
        head = head->next;
    }
    return 0;
}""",
            "cpp": """#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int v) : data(v), next(nullptr) {}
};

Node* merge(Node* a, Node* b) {
    Node dummy(0);
    Node *curr = &dummy;
    while (a && b) {
        if (a->data <= b->data) { curr->next = a; a = a->next; }
        else { curr->next = b; b = b->next; }
        curr = curr->next;
    }
    curr->next = a ? a : b;
    return dummy.next;
}

Node* sortList(Node* head) {
    if (!head || !head->next) return head;

    Node *slow = head, *fast = head->next;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    Node *mid = slow->next;
    slow->next = nullptr;

    Node *left = sortList(head);
    Node *right = sortList(mid);
    return merge(left, right);
}

int main() {
    int v;
    Node *head = nullptr, *tail = nullptr;
    while (cin >> v) {
        Node *temp = new Node(v);
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
    }
    head = sortList(head);
    while (head) {
        cout << head->data << (head->next ? " " : "\\n");
        head = head->next;
    }
    return 0;
}""",
            "java": """import java.util.*;

class Node {
    int data;
    Node next;
    Node(int d) { data = d; }
}

public class Main {
    public static Node merge(Node a, Node b) {
        Node dummy = new Node(0);
        Node curr = dummy;
        while (a != null && b != null) {
            if (a.data <= b.data) { curr.next = a; a = a.next; }
            else { curr.next = b; b = b.next; }
            curr = curr.next;
        }
        curr.next = a != null ? a : b;
        return dummy.next;
    }

    public static Node sortList(Node head) {
        if (head == null || head.next == null) return head;

        Node slow = head, fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        Node mid = slow.next;
        slow.next = null;

        Node left = sortList(head);
        Node right = sortList(mid);
        return merge(left, right);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Node head = null, tail = null;
        while (sc.hasNextInt()) {
            Node temp = new Node(sc.nextInt());
            if (head == null) head = tail = temp;
            else { tail.next = temp; tail = temp; }
        }
        head = sortList(head);
        while (head != null) {
            System.out.print(head.data + (head.next != null ? " " : "\\n"));
            head = head.next;
        }
    }
}""",
            "python": """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sortList(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = sortList(head)
    right = sortList(mid)
    return merge(left, right)

def merge(a, b):
    dummy = Node(0)
    curr = dummy
    while a and b:
        if a.data <= b.data:
            curr.next = a
            a = a.next
        else:
            curr.next = b
            b = b.next
        curr = curr.next
    curr.next = a if a else b
    return dummy.next

def createList(arr):
    dummy = Node(0)
    curr = dummy
    for x in arr:
        curr.next = Node(x)
        curr = curr.next
    return dummy.next

def printList(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print(*result)

if __name__ == '__main__':
    import sys
    tokens = sys.stdin.read().split()
    if tokens:
        arr = [int(x) for x in tokens]
        head = sortList(createList(arr))
        printList(head)"""
        })
    },

    # 11. Reverse Nodes in K-Group
    {
        "id": "dsa-ll-reverse-k-group",
        "problem_num": 86,
        "title": "Reverse Nodes in K-Group",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Grouped In-place Reversal",
        "difficulty": "HARD",
        "description": "Given the head of a linked list, reverse the nodes of the list k at a time and return the modified list. If remaining nodes are fewer than k, leave them unchanged.",
        "input_format": "Line 1: Space-separated integers representing nodes\nLine 2: An integer k",
        "output_format": "Space-separated integers of the modified list.",
        "constraints": "Number of nodes is in range [1, 5000].\n1 <= k <= 5000",
        "time_complexity": "O(N)",
        "space_complexity": "O(N/k)",
        "company_tags": ["Amazon", "Microsoft", "Facebook"],
        "examples": [
            {"input": "1 2 3 4 5\\n2", "output": "2 1 4 3 5", "explanation": "Groups of 2 reversed."},
            {"input": "1 2 3 4 5\\n3", "output": "3 2 1 4 5", "explanation": "Remaining 4,5 unchanged."},
            {"input": "1 2 3 4 5 6\\n3", "output": "3 2 1 6 5 4", "explanation": "Two groups of 3 reversed."}
        ],
        "test_cases": [
            {"input": "1 2 3 4 5\n2", "expected": "2 1 4 3 5", "is_hidden": False},
            {"input": "1 2 3 4 5\n3", "expected": "3 2 1 4 5", "is_hidden": False},
            {"input": "1 2 3 4 5 6\n3", "expected": "3 2 1 6 5 4", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nstruct Node { int data; struct Node* next; };\n\nstruct Node* reverseKGroup(struct Node* head, int k) {\n    // Your code here\n    return head;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nstruct Node { int data; Node* next; Node(int v) : data(v), next(nullptr) {} };\n\nNode* reverseKGroup(Node* head, int k) {\n    // Your code here\n    return head;\n}",
            "java": "import java.util.*;\n\nclass Node { int data; Node next; Node(int d) { data = d; } }\n\npublic class Main {\n    public static Node reverseKGroup(Node head, int k) {\n        // Your code here\n        return head;\n    }\n}",
            "python": "def reverseKGroup(head, k):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* reverseKGroup(struct Node* head, int k) {
    int count = 0;
    struct Node *curr = head;
    while (curr && count < k) {
        curr = curr->next;
        count++;
    }
    if (count < k) return head;

    struct Node *prev = NULL;
    curr = head;
    for (int i = 0; i < k; i++) {
        struct Node *next_node = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next_node;
    }
    head->next = reverseKGroup(curr, k);
    return prev;
}

int main() {
    char line[10000];
    int k;
    if (!fgets(line, sizeof(line), stdin)) return 0;
    if (scanf("%d", &k) != 1) return 0;

    struct Node *head = NULL, *tail = NULL;
    char *ptr = line; int v, off;
    while (sscanf(ptr, "%d%n", &v, &off) == 1) {
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = v; temp->next = NULL;
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
        ptr += off;
    }
    head = reverseKGroup(head, k);
    while (head) {
        printf("%d%s", head->data, head->next ? " " : "\\n");
        head = head->next;
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <sstream>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int v) : data(v), next(nullptr) {}
};

Node* reverseKGroup(Node* head, int k) {
    int count = 0;
    Node *curr = head;
    while (curr && count < k) {
        curr = curr->next;
        count++;
    }
    if (count < k) return head;

    Node *prev = nullptr;
    curr = head;
    for (int i = 0; i < k; i++) {
        Node *next_node = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next_node;
    }
    head->next = reverseKGroup(curr, k);
    return prev;
}

int main() {
    string line;
    if (getline(cin, line)) {
        int k;
        if (cin >> k) {
            stringstream ss(line);
            int v;
            Node *head = nullptr, *tail = nullptr;
            while (ss >> v) {
                Node *temp = new Node(v);
                if (!head) head = tail = temp;
                else { tail->next = temp; tail = temp; }
            }
            head = reverseKGroup(head, k);
            while (head) {
                cout << head->data << (head->next ? " " : "\\n");
                head = head->next;
            }
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

public class Main {
    public static Node reverseKGroup(Node head, int k) {
        int count = 0;
        Node curr = head;
        while (curr != null && count < k) {
            curr = curr.next;
            count++;
        }
        if (count < k) return head;

        Node prev = null;
        curr = head;
        for (int i = 0; i < k; i++) {
            Node next_node = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next_node;
        }
        head.next = reverseKGroup(curr, k);
        return prev;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String[] tokens = sc.nextLine().trim().split("\\\\s+");
            if (sc.hasNextInt()) {
                int k = sc.nextInt();
                Node head = null, tail = null;
                for (String t : tokens) {
                    if (t.isEmpty()) continue;
                    Node temp = new Node(Integer.parseInt(t));
                    if (head == null) head = tail = temp;
                    else { tail.next = temp; tail = temp; }
                }
                head = reverseKGroup(head, k);
                while (head != null) {
                    System.out.print(head.data + (head.next != null ? " " : "\\n"));
                    head = head.next;
                }
            }
        }
    }
}""",
            "python": """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseKGroup(head, k):
    count = 0
    curr = head
    while curr and count < k:
        curr = curr.next
        count += 1

    if count < k:
        return head

    prev = None
    curr = head
    for i in range(k):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    head.next = reverseKGroup(curr, k)
    return prev

def createList(arr):
    dummy = Node(0)
    curr = dummy
    for x in arr:
        curr.next = Node(x)
        curr = curr.next
    return dummy.next

def printList(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print(*result)

if __name__ == '__main__':
    import sys
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    if len(lines) >= 2:
        arr = list(map(int, lines[0].split()))
        k = int(lines[1])
        head = createList(arr)
        head = reverseKGroup(head, k)
        printList(head)"""
        })
    },

    # 12. Copy List with Random Pointer
    {
        "id": "dsa-ll-copy-random-pointer",
        "problem_num": 87,
        "title": "Copy List with Random Pointer",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Deep Copy & Interweaving Nodes",
        "difficulty": "HARD",
        "description": "A linked list has a next pointer and a random pointer which can point to any node or null. Construct a deep copy of the list.",
        "input_format": "Number of nodes N, followed by N lines of 'val random_index' (random_index = -1 if null)",
        "output_format": "N lines of 'val random_index' representing the copied list.",
        "constraints": "0 <= n <= 1000\n-10^4 <= Node.val <= 10^4",
        "time_complexity": "O(N)",
        "space_complexity": "O(1) extra space",
        "company_tags": ["Amazon", "Microsoft", "Facebook"],
        "examples": [
            {"input": "1\\n7 -1", "output": "7 -1", "explanation": "Single node copy."},
            {"input": "2\\n1 1\\n2 1", "output": "1 1\\n2 1", "explanation": "2 nodes pointing to index 1."},
            {"input": "3\\n3 -1\\n3 0\\n3 -1", "output": "3 -1\\n3 0\\n3 -1", "explanation": "Copied list identical."}
        ],
        "test_cases": [
            {"input": "1\n7 -1", "expected": "7 -1", "is_hidden": False},
            {"input": "2\n1 1\n2 1", "expected": "1 1\n2 1", "is_hidden": False},
            {"input": "3\n3 -1\n3 0\n3 -1", "expected": "3 -1\n3 0\n3 -1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nstruct Node { int val; struct Node* next; struct Node* random; };\n\nstruct Node* copyRandomList(struct Node* head) {\n    // Your code here\n    return head;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nstruct Node { int val; Node* next; Node* random; Node(int v) : val(v), next(nullptr), random(nullptr) {} };\n\nNode* copyRandomList(Node* head) {\n    // Your code here\n    return head;\n}",
            "java": "import java.util.*;\n\nclass Node { int val; Node next; Node random; Node(int v) { val = v; } }\n\npublic class Main {\n    public static Node copyRandomList(Node head) {\n        // Your code here\n        return head;\n    }\n}",
            "python": "def copyRandomList(head):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int val;
    struct Node* next;
    struct Node* random;
};

struct Node* copyRandomList(struct Node* head) {
    if (!head) return NULL;

    struct Node *curr = head;
    while (curr) {
        struct Node *copy = (struct Node*)malloc(sizeof(struct Node));
        copy->val = curr->val;
        copy->next = curr->next;
        copy->random = NULL;
        curr->next = copy;
        curr = copy->next;
    }

    curr = head;
    while (curr) {
        if (curr->random) curr->next->random = curr->random->next;
        curr = curr->next->next;
    }

    curr = head;
    struct Node *dummy = (struct Node*)malloc(sizeof(struct Node));
    dummy->next = NULL;
    struct Node *copy_curr = dummy;

    while (curr) {
        struct Node *copy = curr->next;
        curr->next = copy->next;
        copy_curr->next = copy;
        copy_curr = copy;
        curr = curr->next;
    }
    return dummy->next;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    struct Node* nodes[n];
    int r_idx[n];
    for (int i = 0; i < n; i++) {
        nodes[i] = (struct Node*)malloc(sizeof(struct Node));
        scanf("%d %d", &nodes[i]->val, &r_idx[i]);
        nodes[i]->next = NULL;
        nodes[i]->random = NULL;
        if (i > 0) nodes[i - 1]->next = nodes[i];
    }
    for (int i = 0; i < n; i++) {
        if (r_idx[i] >= 0 && r_idx[i] < n) nodes[i]->random = nodes[r_idx[i]];
    }

    struct Node *copied = copyRandomList(nodes[0]);
    struct Node *temp = copied;
    struct Node *cop_nodes[n]; int c_count = 0;
    while (temp) { cop_nodes[c_count++] = temp; temp = temp->next; }

    for (int i = 0; i < c_count; i++) {
        int r = -1;
        if (cop_nodes[i]->random) {
            for (int j = 0; j < c_count; j++) {
                if (cop_nodes[i]->random == cop_nodes[j]) { r = j; break; }
            }
        }
        printf("%d %d\\n", cop_nodes[i]->val, r);
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

struct Node {
    int val;
    Node* next;
    Node* random;
    Node(int v) : val(v), next(nullptr), random(nullptr) {}
};

Node* copyRandomList(Node* head) {
    if (!head) return nullptr;

    Node *curr = head;
    while (curr) {
        Node *copy = new Node(curr->val);
        copy->next = curr->next;
        curr->next = copy;
        curr = copy->next;
    }

    curr = head;
    while (curr) {
        if (curr->random) curr->next->random = curr->random->next;
        curr = curr->next->next;
    }

    curr = head;
    Node dummy(0);
    Node *copy_curr = &dummy;

    while (curr) {
        Node *copy = curr->next;
        curr->next = copy->next;
        copy_curr->next = copy;
        copy_curr = copy;
        curr = curr->next;
    }
    return dummy.next;
}

int main() {
    int n;
    if (cin >> n) {
        vector<Node*> nodes(n);
        vector<int> r_idx(n);
        for (int i = 0; i < n; i++) {
            int v, r; cin >> v >> r;
            nodes[i] = new Node(v);
            r_idx[i] = r;
            if (i > 0) nodes[i - 1]->next = nodes[i];
        }
        for (int i = 0; i < n; i++) {
            if (r_idx[i] >= 0 && r_idx[i] < n) nodes[i]->random = nodes[r_idx[i]];
        }
        Node *copied = copyRandomList(nodes[0]);
        vector<Node*> c_nodes;
        while (copied) { c_nodes.push_back(copied); copied = copied->next; }

        for (size_t i = 0; i < c_nodes.size(); i++) {
            int r = -1;
            if (c_nodes[i]->random) {
                for (size_t j = 0; j < c_nodes.size(); j++) {
                    if (c_nodes[i]->random == c_nodes[j]) { r = j; break; }
                }
            }
            cout << c_nodes[i]->val << " " << r << "\\n";
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

class Node {
    int val;
    Node next;
    Node random;
    Node(int v) { val = v; }
}

public class Main {
    public static Node copyRandomList(Node head) {
        if (head == null) return null;

        Node curr = head;
        while (curr != null) {
            Node copy = new Node(curr.val);
            copy.next = curr.next;
            curr.next = copy;
            curr = copy.next;
        }

        curr = head;
        while (curr != null) {
            if (curr.random != null) curr.next.random = curr.random.next;
            curr = curr.next.next;
        }

        curr = head;
        Node dummy = new Node(0);
        Node copy_curr = dummy;

        while (curr != null) {
            Node copy = curr.next;
            curr.next = copy.next;
            copy_curr.next = copy;
            copy_curr = copy;
            curr = curr.next;
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            Node[] nodes = new Node[n];
            int[] r_idx = new int[n];
            for (int i = 0; i < n; i++) {
                nodes[i] = new Node(sc.nextInt());
                r_idx[i] = sc.nextInt();
                if (i > 0) nodes[i - 1].next = nodes[i];
            }
            for (int i = 0; i < n; i++) {
                if (r_idx[i] >= 0 && r_idx[i] < n) nodes[i].random = nodes[r_idx[i]];
            }
            Node copied = copyRandomList(nodes[0]);
            List<Node> cList = new ArrayList<>();
            while (copied != null) { cList.add(copied); copied = copied.next; }

            for (int i = 0; i < cList.size(); i++) {
                int r = -1;
                if (cList.get(i).random != null) {
                    for (int j = 0; j < cList.size(); j++) {
                        if (cList.get(i).random == cList.get(j)) { r = j; break; }
                    }
                }
                System.out.println(cList.get(i).val + " " + r);
            }
        }
    }
}""",
            "python": """class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

def copyRandomList(head):
    if head is None:
        return None

    curr = head
    while curr:
        copy = Node(curr.val)
        copy.next = curr.next
        curr.next = copy
        curr = copy.next

    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    curr = head
    dummy = Node(0)
    copy_curr = dummy

    while curr:
        copy = curr.next
        curr.next = copy.next
        copy_curr.next = copy
        copy_curr = copy
        curr = curr.next

    return dummy.next

if __name__ == '__main__':
    import sys
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        nodes = []
        r_indices = []
        idx = 1
        for i in range(n):
            val = int(tokens[idx])
            r = int(tokens[idx + 1])
            nodes.append(Node(val))
            r_indices.append(r)
            idx += 2
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]
        for i in range(n):
            if 0 <= r_indices[i] < n:
                nodes[i].random = nodes[r_indices[i]]

        res = copyRandomList(nodes[0])
        copied_nodes = []
        curr = res
        while curr:
            copied_nodes.append(curr)
            curr = curr.next

        for node in copied_nodes:
            r = -1
            if node.random in copied_nodes:
                r = copied_nodes.index(node.random)
            print(f"{node.val} {r}")"""
        })
    },

    # 13. Merge K Sorted Linked Lists
    {
        "id": "dsa-ll-merge-k-sorted",
        "problem_num": 88,
        "title": "Merge K Sorted Linked Lists",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Min-Heap / Divide and Conquer",
        "difficulty": "HARD",
        "description": "Given an array of k sorted linked lists, merge all the linked lists into one sorted linked list and return its head.",
        "input_format": "Line 1: An integer k\nFollowing k lines: Space-separated integers of each sorted linked list",
        "output_format": "Space-separated integers of merged list.",
        "constraints": "k == lists.length\n0 <= k <= 10^4\n0 <= total nodes <= 10^4",
        "time_complexity": "O(N log K)",
        "space_complexity": "O(K)",
        "company_tags": ["Amazon", "Google", "Facebook"],
        "examples": [
            {"input": "3\\n1 4 5\\n1 3 4\\n2 6", "output": "1 1 2 3 4 4 5 6", "explanation": "Merged 3 sorted lists."},
            {"input": "3\\n1 2\\n3 4\\n5 6", "output": "1 2 3 4 5 6", "explanation": "Merged non-overlapping lists."},
            {"input": "2\\n1 5 9\\n2 4 8", "output": "1 2 4 5 8 9", "explanation": "Merged 2 lists."}
        ],
        "test_cases": [
            {"input": "3\n1 4 5\n1 3 4\n2 6", "expected": "1 1 2 3 4 4 5 6", "is_hidden": False},
            {"input": "3\n1 2\n3 4\n5 6", "expected": "1 2 3 4 5 6", "is_hidden": False},
            {"input": "2\n1 5 9\n2 4 8", "expected": "1 2 4 5 8 9", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nstruct Node { int data; struct Node* next; };\n\nstruct Node* mergeKLists(struct Node* lists[], int k) {\n    // Your code here\n    return NULL;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nstruct Node { int data; Node* next; Node(int v) : data(v), next(nullptr) {} };\n\nNode* mergeKLists(vector<Node*>& lists) {\n    // Your code here\n    return nullptr;\n}",
            "java": "import java.util.*;\n\nclass Node { int data; Node next; Node(int d) { data = d; } }\n\npublic class Main {\n    public static Node mergeKLists(Node[] lists) {\n        // Your code here\n        return null;\n    }\n}",
            "python": "def mergeKLists(lists):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* mergeTwo(struct Node* l1, struct Node* l2) {
    struct Node dummy; dummy.next = NULL;
    struct Node *curr = &dummy;
    while (l1 && l2) {
        if (l1->data <= l2->data) { curr->next = l1; l1 = l1->next; }
        else { curr->next = l2; l2 = l2->next; }
        curr = curr->next;
    }
    curr->next = l1 ? l1 : l2;
    return dummy.next;
}

struct Node* mergeKLists(struct Node* lists[], int k) {
    if (k == 0) return NULL;
    int interval = 1;
    while (interval < k) {
        for (int i = 0; i + interval < k; i += interval * 2) {
            lists[i] = mergeTwo(lists[i], lists[i + interval]);
        }
        interval *= 2;
    }
    return lists[0];
}

int main() {
    int k;
    if (scanf("%d", &k) != 1) return 0;
    while (getchar() != '\\n');
    struct Node* lists[k];
    char line[10000];
    for (int i = 0; i < k; i++) {
        lists[i] = NULL;
        struct Node *tail = NULL;
        if (fgets(line, sizeof(line), stdin)) {
            char *ptr = line; int v, off;
            while (sscanf(ptr, "%d%n", &v, &off) == 1) {
                struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
                temp->data = v; temp->next = NULL;
                if (!lists[i]) lists[i] = tail = temp;
                else { tail->next = temp; tail = temp; }
                ptr += off;
            }
        }
    }
    struct Node *res = mergeKLists(lists, k);
    while (res) {
        printf("%d%s", res->data, res->next ? " " : "\\n");
        res = res->next;
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <queue>
#include <sstream>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int v) : data(v), next(nullptr) {}
};

struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->data > b->data;
    }
};

Node* mergeKLists(vector<Node*>& lists) {
    priority_queue<Node*, vector<Node*>, Compare> pq;
    for (Node* h : lists) {
        if (h) pq.push(h);
    }
    Node dummy(0);
    Node *curr = &dummy;

    while (!pq.empty()) {
        Node *node = pq.top(); pq.pop();
        curr->next = node;
        curr = curr->next;
        if (node->next) pq.push(node->next);
    }
    return dummy.next;
}

int main() {
    int k;
    if (cin >> k) {
        string dummy_line; getline(cin, dummy_line);
        vector<Node*> lists;
        for (int i = 0; i < k; i++) {
            string line;
            if (getline(cin, line)) {
                stringstream ss(line);
                int v;
                Node *head = nullptr, *tail = nullptr;
                while (ss >> v) {
                    Node *temp = new Node(v);
                    if (!head) head = tail = temp;
                    else { tail->next = temp; tail = temp; }
                }
                lists.push_back(head);
            }
        }
        Node *res = mergeKLists(lists);
        while (res) {
            cout << res->data << (res->next ? " " : "\\n");
            res = res->next;
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

public class Main {
    public static Node mergeKLists(List<Node> lists) {
        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.data, b.data));
        for (Node h : lists) {
            if (h != null) pq.add(h);
        }
        Node dummy = new Node(0);
        Node curr = dummy;

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            curr.next = node;
            curr = curr.next;
            if (node.next != null) pq.add(node.next);
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            sc.nextLine();
            List<Node> lists = new ArrayList<>();
            for (int i = 0; i < k; i++) {
                if (sc.hasNextLine()) {
                    String line = sc.nextLine().trim();
                    Node head = null, tail = null;
                    if (!line.isEmpty()) {
                        for (String t : line.split("\\\\s+")) {
                            if (t.isEmpty()) continue;
                            Node temp = new Node(Integer.parseInt(t));
                            if (head == null) head = tail = temp;
                            else { tail.next = temp; tail = temp; }
                        }
                    }
                    lists.add(head);
                }
            }
            Node res = mergeKLists(lists);
            while (res != null) {
                System.out.print(res.data + (res.next != null ? " " : "\\n"));
                res = res.next;
            }
        }
    }
}""",
            "python": """import heapq

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeKLists(lists):
    heap = []
    count = 0

    for head in lists:
        if head:
            heapq.heappush(heap, (head.data, count, head))
            count += 1

    dummy = Node(0)
    curr = dummy

    while heap:
        value, index, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.data, count, node.next))
            count += 1

    curr.next = None
    return dummy.next

def createList(arr):
    dummy = Node(0)
    curr = dummy
    for x in arr:
        curr.next = Node(x)
        curr = curr.next
    return dummy.next

def printList(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print(*result)

if __name__ == '__main__':
    import sys
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    if lines:
        k = int(lines[0])
        lists = []
        for i in range(1, 1 + k):
            if i < len(lines):
                arr = list(map(int, lines[i].split()))
                lists.append(createList(arr))
            else:
                lists.append(None)
        head = mergeKLists(lists)
        printList(head)"""
        })
    },

    # 14. LRU Cache
    {
        "id": "dsa-ll-lru-cache",
        "problem_num": 89,
        "title": "LRU Cache Design",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Hash Map & Doubly Linked List",
        "difficulty": "HARD",
        "description": "Design a Least Recently Used (LRU) Cache with fixed capacity. Implement get(key) and put(key, value) in O(1) average time.",
        "input_format": "Line 1: Capacity C\nLine 2: Number of operations M\nNext M lines: 'put key value' or 'get key'",
        "output_format": "The outputs for each get operation separated by newlines.",
        "constraints": "1 <= capacity <= 3000\n0 <= key <= 10^4\n0 <= value <= 10^5\nAt most 2 * 10^5 calls.",
        "time_complexity": "O(1) per operation",
        "space_complexity": "O(capacity)",
        "company_tags": ["Amazon", "Google", "Facebook", "Microsoft"],
        "examples": [
            {"input": "2\\n5\\nput 1 1\\nput 2 2\\nget 1\\nput 3 3\\nget 2", "output": "1\\n-1", "explanation": "2 evicted when 3 added."},
            {"input": "2\\n5\\nput 1 10\\nput 2 20\\nput 1 30\\nget 1\\nget 2", "output": "30\\n20", "explanation": "Key 1 updated to 30."},
            {"input": "1\\n4\\nput 1 10\\nput 2 20\\nget 1\\nget 2", "output": "-1\\n20", "explanation": "Capacity 1 evicts key 1."}
        ],
        "test_cases": [
            {"input": "2\n5\nput 1 1\nput 2 2\nget 1\nput 3 3\nget 2", "expected": "1\n-1", "is_hidden": False},
            {"input": "2\n5\nput 1 10\nput 2 20\nput 1 30\nget 1\nget 2", "expected": "30\n20", "is_hidden": False},
            {"input": "1\n4\nput 1 10\nput 2 20\nget 1\nget 2", "expected": "-1\n20", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\n// Implement LRU Cache\nint main() {\n    // Your code here\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nclass LRUCache {\npublic:\n    LRUCache(int capacity) {}\n    int get(int key) { return -1; }\n    void put(int key, int value) {}\n};",
            "java": "import java.util.*;\n\nclass LRUCache {\n    public LRUCache(int capacity) {}\n    public int get(int key) { return -1; }\n    public void put(int key, int value) {}\n}",
            "python": "class LRUCache:\n    def __init__(self, capacity: int):\n        pass\n    def get(self, key: int) -> int:\n        return -1\n    def put(self, key: int, value: int) -> None:\n        pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct DNode {
    int key;
    int val;
    struct DNode *prev, *next;
};

struct DNode* hash_table[10001];
struct DNode *head, *tail;
int cap = 0, size = 0;

void removeNode(struct DNode *node) {
    node->prev->next = node->next;
    node->next->prev = node->prev;
}

void addToHead(struct DNode *node) {
    node->next = head->next;
    node->prev = head;
    head->next->prev = node;
    head->next = node;
}

int get(int key) {
    if (key < 0 || key > 10000 || !hash_table[key]) return -1;
    struct DNode *node = hash_table[key];
    removeNode(node);
    addToHead(node);
    return node->val;
}

void put(int key, int val) {
    if (hash_table[key]) {
        struct DNode *node = hash_table[key];
        node->val = val;
        removeNode(node);
        addToHead(node);
    } else {
        if (size == cap) {
            struct DNode *lru = tail->prev;
            hash_table[lru->key] = NULL;
            removeNode(lru);
            free(lru);
            size--;
        }
        struct DNode *node = (struct DNode*)malloc(sizeof(struct DNode));
        node->key = key; node->val = val;
        hash_table[key] = node;
        addToHead(node);
        size++;
    }
}

int main() {
    int ops;
    if (scanf("%d %d", &cap, &ops) != 2) return 0;
    head = (struct DNode*)malloc(sizeof(struct DNode));
    tail = (struct DNode*)malloc(sizeof(struct DNode));
    head->next = tail; tail->prev = head;

    for (int i = 0; i <= 10000; i++) hash_table[i] = NULL;

    for (int i = 0; i < ops; i++) {
        char op[10]; scanf("%s", op);
        if (strcmp(op, "put") == 0) {
            int k, v; scanf("%d %d", &k, &v);
            put(k, v);
        } else {
            int k; scanf("%d", &k);
            printf("%d\\n", get(k));
        }
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <unordered_map>
#include <list>

using namespace std;

class LRUCache {
    int cap;
    list<pair<int, int>> dll;
    unordered_map<int, list<pair<int, int>>::iterator> mp;
public:
    LRUCache(int capacity) : cap(capacity) {}

    int get(int key) {
        if (mp.find(key) == mp.end()) return -1;
        dll.splice(dll.begin(), dll, mp[key]);
        return mp[key]->second;
    }

    void put(int key, int value) {
        if (mp.find(key) != mp.end()) {
            mp[key]->second = value;
            dll.splice(dll.begin(), dll, mp[key]);
        } else {
            if ((int)dll.size() == cap) {
                int old_key = dll.back().first;
                dll.pop_back();
                mp.erase(old_key);
            }
            dll.emplace_front(key, value);
            mp[key] = dll.begin();
        }
    }
};

int main() {
    int c, ops;
    if (cin >> c >> ops) {
        LRUCache cache(c);
        for (int i = 0; i < ops; i++) {
            string op; cin >> op;
            if (op == "put") {
                int k, v; cin >> k >> v;
                cache.put(k, v);
            } else {
                int k; cin >> k;
                cout << cache.get(k) << "\\n";
            }
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

class LRUCache {
    private final int capacity;
    private final LinkedHashMap<Integer, Integer> cache;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new LinkedHashMap<>(capacity, 0.75f, true) {
            protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
                return size() > LRUCache.this.capacity;
            }
        };
    }

    public int get(int key) {
        return cache.getOrDefault(key, -1);
    }

    public void put(int key, int value) {
        cache.put(key, value);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int c = sc.nextInt();
            int ops = sc.nextInt();
            LRUCache cache = new LRUCache(c);
            for (int i = 0; i < ops; i++) {
                String op = sc.next();
                if (op.equals("put")) {
                    cache.put(sc.nextInt(), sc.nextInt());
                } else {
                    System.out.println(cache.get(sc.nextInt()));
                }
            }
        }
    }
}""",
            "python": """from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

if __name__ == '__main__':
    import sys
    tokens = sys.stdin.read().split()
    if tokens:
        cap = int(tokens[0])
        ops = int(tokens[1])
        cache = LRUCache(cap)
        idx = 2
        for _ in range(ops):
            cmd = tokens[idx]
            if cmd == 'put':
                k, v = int(tokens[idx + 1]), int(tokens[idx + 2])
                cache.put(k, v)
                idx += 3
            else:
                k = int(tokens[idx + 1])
                print(cache.get(k))
                idx += 2"""
        })
    },

    # 15. Flatten a Multilevel Doubly Linked List
    {
        "id": "dsa-ll-flatten-multilevel",
        "problem_num": 90,
        "title": "Flatten a Multilevel Doubly Linked List",
        "category": "Linked List",
        "topic": "Linked List",
        "subtopic": "Doubly Linked List & DFS",
        "difficulty": "HARD",
        "description": "Given a multilevel doubly linked list where each node has a next, prev, and child pointer. Flatten the list so all nodes appear in a single-level doubly linked list. Child lists must appear immediately after parent nodes.",
        "input_format": "Serialized multilevel tree as pairs of (parent_val child_val) or preorder list.",
        "output_format": "Space-separated integers of flattened list.",
        "constraints": "Number of nodes will not exceed 1000.\n1 <= Node.val <= 10^5",
        "time_complexity": "O(N)",
        "space_complexity": "O(1) extra space",
        "company_tags": ["Bloomberg", "Facebook", "Amazon"],
        "examples": [
            {"input": "1 2 3\\n2 4 5", "output": "1 2 4 5 3", "explanation": "Child 4-5 inserted after 2."},
            {"input": "1 2\\n1 3 4", "output": "1 3 4 2", "explanation": "Child 3-4 inserted after 1."},
            {"input": "1 2 3\\n2 4\\n4 5", "output": "1 2 4 5 3", "explanation": "Nested child levels flattened."}
        ],
        "test_cases": [
            {"input": "1 2 3\n2 4 5", "expected": "1 2 4 5 3", "is_hidden": False},
            {"input": "1 2\n1 3 4", "expected": "1 3 4 2", "is_hidden": False},
            {"input": "1 2 3\n2 4\n4 5", "expected": "1 2 4 5 3", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nstruct Node { int val; struct Node *prev, *next, *child; };\n\nstruct Node* flatten(struct Node* head) {\n    // Your code here\n    return head;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nstruct Node { int val; Node *prev, *next, *child; Node(int v) : val(v), prev(nullptr), next(nullptr), child(nullptr) {} };\n\nNode* flatten(Node* head) {\n    // Your code here\n    return head;\n}",
            "java": "import java.util.*;\n\nclass Node { int val; Node prev, next, child; Node(int v) { val = v; } }\n\npublic class Main {\n    public static Node flatten(Node head) {\n        // Your code here\n        return head;\n    }\n}",
            "python": "def flatten(head):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node {
    int val;
    struct Node *prev, *next, *child;
};

struct Node* flatten(struct Node* head) {
    if (!head) return NULL;
    struct Node *curr = head;
    while (curr) {
        if (curr->child) {
            struct Node *next_node = curr->next;
            struct Node *child = curr->child;

            curr->next = child;
            child->prev = curr;
            curr->child = NULL;

            struct Node *tail = child;
            while (tail->next) tail = tail->next;

            if (next_node) {
                tail->next = next_node;
                next_node->prev = tail;
            }
        }
        curr = curr->next;
    }
    return head;
}

int main() {
    char l1[1000], l2[1000], l3[1000];
    if (!fgets(l1, sizeof(l1), stdin)) return 0;
    int has_l2 = fgets(l2, sizeof(l2), stdin) != NULL;
    int has_l3 = has_l2 && (fgets(l3, sizeof(l3), stdin) != NULL);

    struct Node *head = NULL, *tail = NULL;
    char *ptr = l1; int v, off;
    while (sscanf(ptr, "%d%n", &v, &off) == 1) {
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->val = v; temp->prev = tail; temp->next = NULL; temp->child = NULL;
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
        ptr += off;
    }

    if (has_l2) {
        int parent_v; ptr = l2;
        if (sscanf(ptr, "%d%n", &parent_v, &off) == 1) {
            ptr += off;
            struct Node *chead = NULL, *ctail = NULL;
            while (sscanf(ptr, "%d%n", &v, &off) == 1) {
                struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
                temp->val = v; temp->prev = ctail; temp->next = NULL; temp->child = NULL;
                if (!chead) chead = ctail = temp;
                else { ctail->next = temp; ctail = temp; }
                ptr += off;
            }
            struct Node *p = head;
            while (p && p->val != parent_v) p = p->next;
            if (p) p->child = chead;

            if (has_l3) {
                int p3; ptr = l3;
                if (sscanf(ptr, "%d%n", &p3, &off) == 1) {
                    ptr += off;
                    struct Node *c3head = NULL, *c3tail = NULL;
                    while (sscanf(ptr, "%d%n", &v, &off) == 1) {
                        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
                        temp->val = v; temp->prev = c3tail; temp->next = NULL; temp->child = NULL;
                        if (!c3head) c3head = c3tail = temp;
                        else { c3tail->next = temp; c3tail = temp; }
                        ptr += off;
                    }
                    struct Node *p2 = chead;
                    while (p2 && p2->val != p3) p2 = p2->next;
                    if (p2) p2->child = c3head;
                }
            }
        }
    }

    head = flatten(head);
    while (head) {
        printf("%d%s", head->val, head->next ? " " : "\\n");
        head = head->next;
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

struct Node {
    int val;
    Node *prev, *next, *child;
    Node(int v) : val(v), prev(nullptr), next(nullptr), child(nullptr) {}
};

Node* flatten(Node* head) {
    if (!head) return nullptr;
    Node *curr = head;
    while (curr) {
        if (curr->child) {
            Node *next_node = curr->next;
            Node *child = curr->child;

            curr->next = child;
            child->prev = curr;
            curr->child = nullptr;

            Node *tail = child;
            while (tail->next) tail = tail->next;

            if (next_node) {
                tail->next = next_node;
                next_node->prev = tail;
            }
        }
        curr = curr->next;
    }
    return head;
}

int main() {
    string l1, l2, l3;
    if (getline(cin, l1)) {
        stringstream ss1(l1);
        int v;
        Node *head = nullptr, *tail = nullptr;
        while (ss1 >> v) {
            Node *temp = new Node(v);
            temp->prev = tail;
            if (!head) head = tail = temp;
            else { tail->next = temp; tail = temp; }
        }

        if (getline(cin, l2) && !l2.empty()) {
            stringstream ss2(l2);
            int parent_v; ss2 >> parent_v;
            Node *chead = nullptr, *ctail = nullptr;
            while (ss2 >> v) {
                Node *temp = new Node(v);
                temp->prev = ctail;
                if (!chead) chead = ctail = temp;
                else { ctail->next = temp; ctail = temp; }
            }
            Node *p = head;
            while (p && p->val != parent_v) p = p->next;
            if (p) p->child = chead;

            if (getline(cin, l3) && !l3.empty()) {
                stringstream ss3(l3);
                int p3; ss3 >> p3;
                Node *c3head = nullptr, *c3tail = nullptr;
                while (ss3 >> v) {
                    Node *temp = new Node(v);
                    temp->prev = c3tail;
                    if (!c3head) c3head = c3tail = temp;
                    else { c3tail->next = temp; c3tail = temp; }
                }
                Node *p2 = chead;
                while (p2 && p2->val != p3) p2 = p2->next;
                if (p2) p2->child = c3head;
            }
        }
        head = flatten(head);
        while (head) {
            cout << head->val << (head->next ? " " : "\\n");
            head = head->next;
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

class Node {
    int val;
    Node prev, next, child;
    Node(int v) { val = v; }
}

public class Main {
    public static Node flatten(Node head) {
        if (head == null) return null;
        Node curr = head;
        while (curr != null) {
            if (curr.child != null) {
                Node next_node = curr.next;
                Node child = curr.child;

                curr.next = child;
                child.prev = curr;
                curr.child = null;

                Node tail = child;
                while (tail.next != null) tail = tail.next;

                if (next_node != null) {
                    tail.next = next_node;
                    next_node.prev = tail;
                }
            }
            curr = curr.next;
        }
        return head;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String l1 = sc.nextLine();
            Node head = null, tail = null;
            for (String t : l1.trim().split("\\\\s+")) {
                if (t.isEmpty()) continue;
                Node temp = new Node(Integer.parseInt(t));
                temp.prev = tail;
                if (head == null) head = tail = temp;
                else { tail.next = temp; tail = temp; }
            }

            if (sc.hasNextLine()) {
                String l2 = sc.nextLine().trim();
                if (!l2.isEmpty()) {
                    String[] t2 = l2.split("\\\\s+");
                    int parent_v = Integer.parseInt(t2[0]);
                    Node chead = null, ctail = null;
                    for (int i = 1; i < t2.length; i++) {
                        Node temp = new Node(Integer.parseInt(t2[i]));
                        temp.prev = ctail;
                        if (chead == null) chead = ctail = temp;
                        else { ctail.next = temp; ctail = temp; }
                    }
                    Node p = head;
                    while (p != null && p.val != parent_v) p = p.next;
                    if (p != null) p.child = chead;

                    if (sc.hasNextLine()) {
                        String l3 = sc.nextLine().trim();
                        if (!l3.isEmpty()) {
                            String[] t3 = l3.split("\\\\s+");
                            int p3 = Integer.parseInt(t3[0]);
                            Node c3head = null, c3tail = null;
                            for (int i = 1; i < t3.length; i++) {
                                Node temp = new Node(Integer.parseInt(t3[i]));
                                temp.prev = c3tail;
                                if (c3head == null) c3head = c3tail = temp;
                                else { c3tail.next = temp; c3tail = temp; }
                            }
                            Node p2 = chead;
                            while (p2 != null && p2.val != p3) p2 = p2.next;
                            if (p2 != null) p2.child = c3head;
                        }
                    }
                }
            }

            head = flatten(head);
            while (head != null) {
                System.out.print(head.val + (head.next != null ? " " : "\\n"));
                head = head.next;
            }
        }
    }
}""",
            "python": """class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.child = None

def flatten(head):
    if head is None:
        return None

    curr = head
    while curr:
        if curr.child:
            next_node = curr.next
            child = curr.child

            curr.next = child
            child.prev = curr
            curr.child = None

            tail = child
            while tail.next:
                tail = tail.next

            if next_node:
                tail.next = next_node
                next_node.prev = tail

        curr = curr.next

    return head

if __name__ == '__main__':
    import sys
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    if lines:
        vals = list(map(int, lines[0].split()))
        head = Node(vals[0])
        tail = head
        for v in vals[1:]:
            temp = Node(v)
            temp.prev = tail
            tail.next = temp
            tail = temp

        if len(lines) >= 2:
            t2 = list(map(int, lines[1].split()))
            parent_v = t2[0]
            chead = Node(t2[1])
            ctail = chead
            for v in t2[2:]:
                temp = Node(v)
                temp.prev = ctail
                ctail.next = temp
                ctail = temp
            p = head
            while p and p.val != parent_v: p = p.next
            if p: p.child = chead

            if len(lines) >= 3:
                t3 = list(map(int, lines[2].split()))
                p3 = t3[0]
                c3head = Node(t3[1])
                c3tail = c3head
                for v in t3[2:]:
                    temp = Node(v)
                    temp.prev = c3tail
                    c3tail.next = temp
                    c3tail = temp
                p2 = chead
                while p2 and p2.val != p3: p2 = p2.next
                if p2: p2.child = c3head

        head = flatten(head)
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print(*res)"""
        })
    }
]

problems.extend(ll_data)

for idx, p in enumerate(problems):
    p["problem_num"] = idx + 1

with open("backend/app/data/dsa_problems_seed.json", "w", encoding="utf-8") as f:
    json.dump(problems, f, indent=2)

print(f"Successfully added 15 Linked List problems! Total problems now: {len(problems)}")

