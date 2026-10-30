import sys, os
sys.path.insert(0, os.path.abspath('.'))
import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    problems = json.load(f)

tree_ids = {
    "dsa-tree-max-depth", "dsa-tree-count-nodes", "dsa-tree-inorder-traversal",
    "dsa-tree-preorder-traversal", "dsa-tree-postorder-traversal", "dsa-tree-level-order-traversal",
    "dsa-tree-invert-binary-tree", "dsa-tree-diameter-binary-tree", "dsa-tree-check-balanced",
    "dsa-tree-lowest-common-ancestor", "dsa-tree-max-path-sum", "dsa-tree-serialize-deserialize",
    "dsa-tree-construct-from-pre-in", "dsa-tree-max-width", "dsa-tree-recover-bst"
}
problems = [p for p in problems if p["id"] not in tree_ids]

tree_data = [
    # 16. Maximum Depth of Binary Tree
    {
        "id": "dsa-tree-max-depth",
        "problem_num": 151,
        "title": "Maximum Depth of Binary Tree",
        "category": "Trees",
        "topic": "Binary Tree Traversal",
        "subtopic": "Tree Height / Depth",
        "difficulty": "EASY",
        "description": "Find the maximum depth (height in nodes) of a binary tree from root to deepest leaf.",
        "input_format": "Number of elements followed by level-order values ('N' for null).",
        "output_format": "Integer representing maximum depth.",
        "constraints": "0 <= number of nodes <= 10^4, -100 <= Node.val <= 100",
        "time_complexity": "O(N)",
        "space_complexity": "O(H) where H is tree height",
        "company_tags": ["Amazon", "Google", "Apple", "Microsoft"],
        "examples": [
            {"input": "3\n1 2 3", "output": "2", "explanation": "Root 1 at depth 1, leaves 2 and 3 at depth 2."},
            {"input": "5\n1 2 3 4 5", "output": "3", "explanation": "Leaves 4 and 5 reach depth 3."},
            {"input": "1\n1", "output": "1", "explanation": "Single node has depth 1."}
        ],
        "test_cases": [
            {"input": "3\n1 2 3", "expected": "2", "is_hidden": False},
            {"input": "5\n1 2 3 4 5", "expected": "3", "is_hidden": False},
            {"input": "1\n1", "expected": "1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def max_depth(root):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build_tree(char values[][20], int count) {
    if (count == 0 || strcmp(values[0], "N") == 0) return NULL;
    Node* root = createNode(atoi(values[0]));
    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        Node* curr = q[head++];
        if (strcmp(values[i], "N") != 0) {
            curr->left = createNode(atoi(values[i]));
            q[tail++] = curr->left;
        }
        i++;
        if (i < count && strcmp(values[i], "N") != 0) {
            curr->right = createNode(atoi(values[i]));
            q[tail++] = curr->right;
        }
        i++;
    }
    return root;
}

int max_depth(Node* root) {
    if (!root) return 0;
    int l = max_depth(root->left);
    int r = max_depth(root->right);
    return 1 + (l > r ? l : r);
}

int main() {
    char tok[50];
    if (scanf("%s", tok) != 1) return 0;
    char values[2000][20];
    int count = 0;
    while (scanf("%s", values[count]) == 1) {
        if (strcmp(values[count], "/") == 0) continue;
        count++;
    }
    Node* root = build_tree(values, count);
    printf("%d\\n", max_depth(root));
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build_tree(const vector<string>& values) {
    if (values.empty() || values[0] == "N") return NULL;
    Node* root = new Node(stoi(values[0]));
    queue<Node*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        Node* curr = q.front();
        q.pop();
        if (values[i] != "N") {
            curr->left = new Node(stoi(values[i]));
            q.push(curr->left);
        }
        i++;
        if (i < values.size() && values[i] != "N") {
            curr->right = new Node(stoi(values[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

int max_depth(Node* root) {
    if (!root) return 0;
    return 1 + max(max_depth(root->left), max_depth(root->right));
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    vector<string> values;
    while (cin >> token) {
        if (token != "/") values.push_back(token);
    }
    Node* root = build_tree(values);
    cout << max_depth(root) << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static Node build_tree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("N")) return null;
        Node root = new Node(Integer.parseInt(values.get(0)));
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.size()) {
            Node curr = q.poll();
            if (!values.get(i).equals("N")) {
                curr.left = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < values.size() && !values.get(i).equals("N")) {
                curr.right = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    static int max_depth(Node root) {
        if (root == null) return 0;
        return 1 + Math.max(max_depth(root.left), max_depth(root.right));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        sc.next();
        List<String> values = new ArrayList<>();
        while (sc.hasNext()) {
            String tok = sc.next();
            if (!tok.equals("/")) values.add(tok);
        }
        Node root = build_tree(values);
        System.out.println(max_depth(root));
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if raw:
        n = int(raw[0])
        values = raw[1:]
        root = build_tree(values)
        print(max_depth(root))"""
        })
    },

    # 17. Count Total Nodes
    {
        "id": "dsa-tree-count-nodes",
        "problem_num": 152,
        "title": "Count Total Nodes in Binary Tree",
        "category": "Trees",
        "topic": "Binary Tree Traversal",
        "subtopic": "Tree Node Counting",
        "difficulty": "EASY",
        "description": "Count the total number of nodes in a given binary tree.",
        "input_format": "Number of elements followed by level-order values ('N' for null).",
        "output_format": "Total count of nodes.",
        "constraints": "0 <= number of nodes <= 5 * 10^4",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "company_tags": ["Amazon", "Google"],
        "examples": [
            {"input": "3\n1 2 3", "output": "3", "explanation": "3 nodes present."},
            {"input": "5\n1 2 3 4 5", "output": "5", "explanation": "5 nodes present."},
            {"input": "1\n10", "output": "1", "explanation": "Single node."}
        ],
        "test_cases": [
            {"input": "3\n1 2 3", "expected": "3", "is_hidden": False},
            {"input": "5\n1 2 3 4 5", "expected": "5", "is_hidden": False},
            {"input": "1\n10", "expected": "1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def count_nodes(root):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build_tree(char values[][20], int count) {
    if (count == 0 || strcmp(values[0], "N") == 0) return NULL;
    Node* root = createNode(atoi(values[0]));
    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        Node* curr = q[head++];
        if (strcmp(values[i], "N") != 0) {
            curr->left = createNode(atoi(values[i]));
            q[tail++] = curr->left;
        }
        i++;
        if (i < count && strcmp(values[i], "N") != 0) {
            curr->right = createNode(atoi(values[i]));
            q[tail++] = curr->right;
        }
        i++;
    }
    return root;
}

int count_nodes(Node* root) {
    if (!root) return 0;
    return 1 + count_nodes(root->left) + count_nodes(root->right);
}

int main() {
    char tok[50];
    if (scanf("%s", tok) != 1) return 0;
    char values[2000][20];
    int count = 0;
    while (scanf("%s", values[count]) == 1) {
        if (strcmp(values[count], "/") == 0) continue;
        count++;
    }
    Node* root = build_tree(values, count);
    printf("%d\\n", count_nodes(root));
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build_tree(const vector<string>& values) {
    if (values.empty() || values[0] == "N") return NULL;
    Node* root = new Node(stoi(values[0]));
    queue<Node*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        Node* curr = q.front();
        q.pop();
        if (values[i] != "N") {
            curr->left = new Node(stoi(values[i]));
            q.push(curr->left);
        }
        i++;
        if (i < values.size() && values[i] != "N") {
            curr->right = new Node(stoi(values[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

int count_nodes(Node* root) {
    if (!root) return 0;
    return 1 + count_nodes(root->left) + count_nodes(root->right);
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    vector<string> values;
    while (cin >> token) {
        if (token != "/") values.push_back(token);
    }
    Node* root = build_tree(values);
    cout << count_nodes(root) << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static Node build_tree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("N")) return null;
        Node root = new Node(Integer.parseInt(values.get(0)));
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.size()) {
            Node curr = q.poll();
            if (!values.get(i).equals("N")) {
                curr.left = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < values.size() && !values.get(i).equals("N")) {
                curr.right = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    static int count_nodes(Node root) {
        if (root == null) return 0;
        return 1 + count_nodes(root.left) + count_nodes(root.right);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        sc.next();
        List<String> values = new ArrayList<>();
        while (sc.hasNext()) {
            String tok = sc.next();
            if (!tok.equals("/")) values.add(tok);
        }
        Node root = build_tree(values);
        System.out.println(count_nodes(root));
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if raw:
        n = int(raw[0])
        values = raw[1:]
        root = build_tree(values)
        print(count_nodes(root))"""
        })
    },

    # 18. Inorder Traversal
    {
        "id": "dsa-tree-inorder-traversal",
        "problem_num": 153,
        "title": "Inorder Traversal",
        "category": "Trees",
        "topic": "Tree Traversals",
        "subtopic": "Left-Root-Right",
        "difficulty": "EASY",
        "description": "Print the nodes in Left -> Root -> Right inorder traversal order.",
        "input_format": "Number of elements followed by level-order values ('N' for null).",
        "output_format": "List of node values in inorder traversal.",
        "constraints": "0 <= number of nodes <= 100",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "company_tags": ["Amazon", "Microsoft"],
        "examples": [
            {"input": "3\n1 2 3", "output": "[2, 1, 3]", "explanation": "Inorder: Left(2) -> Root(1) -> Right(3)."},
            {"input": "5\n1 2 3 4 5", "output": "[4, 2, 5, 1, 3]", "explanation": "Subtree 2 gives [4, 2, 5], then 1, then 3."},
            {"input": "1\n10", "output": "[10]", "explanation": "Single node traversal."}
        ],
        "test_cases": [
            {"input": "3\n1 2 3", "expected": "[2, 1, 3]", "is_hidden": False},
            {"input": "5\n1 2 3 4 5", "expected": "[4, 2, 5, 1, 3]", "is_hidden": False},
            {"input": "1\n10", "expected": "[10]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def inorder(root):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build_tree(char values[][20], int count) {
    if (count == 0 || strcmp(values[0], "N") == 0) return NULL;
    Node* root = createNode(atoi(values[0]));
    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        Node* curr = q[head++];
        if (strcmp(values[i], "N") != 0) {
            curr->left = createNode(atoi(values[i]));
            q[tail++] = curr->left;
        }
        i++;
        if (i < count && strcmp(values[i], "N") != 0) {
            curr->right = createNode(atoi(values[i]));
            q[tail++] = curr->right;
        }
        i++;
    }
    return root;
}

int res[2000];
int res_count = 0;

void inorder(Node* root) {
    if (!root) return;
    inorder(root->left);
    res[res_count++] = root->val;
    inorder(root->right);
}

int main() {
    char tok[50];
    if (scanf("%s", tok) != 1) return 0;
    char values[2000][20];
    int count = 0;
    while (scanf("%s", values[count]) == 1) {
        if (strcmp(values[count], "/") == 0) continue;
        count++;
    }
    Node* root = build_tree(values, count);
    inorder(root);

    printf("[");
    for (int i = 0; i < res_count; i++) {
        printf("%d%s", res[i], (i == res_count - 1 ? "" : ", "));
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build_tree(const vector<string>& values) {
    if (values.empty() || values[0] == "N") return NULL;
    Node* root = new Node(stoi(values[0]));
    queue<Node*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        Node* curr = q.front();
        q.pop();
        if (values[i] != "N") {
            curr->left = new Node(stoi(values[i]));
            q.push(curr->left);
        }
        i++;
        if (i < values.size() && values[i] != "N") {
            curr->right = new Node(stoi(values[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

void inorder(Node* root, vector<int>& res) {
    if (!root) return;
    inorder(root->left, res);
    res.push_back(root->val);
    inorder(root->right, res);
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    vector<string> values;
    while (cin >> token) {
        if (token != "/") values.push_back(token);
    }
    Node* root = build_tree(values);
    vector<int> res;
    inorder(root, res);

    cout << "[";
    for (size_t i = 0; i < res.size(); i++) {
        cout << res[i] << (i == res.size() - 1 ? "" : ", ");
    }
    cout << "]\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static Node build_tree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("N")) return null;
        Node root = new Node(Integer.parseInt(values.get(0)));
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.size()) {
            Node curr = q.poll();
            if (!values.get(i).equals("N")) {
                curr.left = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < values.size() && !values.get(i).equals("N")) {
                curr.right = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    static void inorder(Node root, List<Integer> res) {
        if (root == null) return;
        inorder(root.left, res);
        res.add(root.val);
        inorder(root.right, res);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        sc.next();
        List<String> values = new ArrayList<>();
        while (sc.hasNext()) {
            String tok = sc.next();
            if (!tok.equals("/")) values.add(tok);
        }
        Node root = build_tree(values);
        List<Integer> res = new ArrayList<>();
        inorder(root, res);
        System.out.println(res.toString());
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if raw:
        n = int(raw[0])
        values = raw[1:]
        root = build_tree(values)
        print(inorder(root))"""
        })
    },

    # 19. Preorder Traversal
    {
        "id": "dsa-tree-preorder-traversal",
        "problem_num": 154,
        "title": "Preorder Traversal",
        "category": "Trees",
        "topic": "Tree Traversals",
        "subtopic": "Root-Left-Right",
        "difficulty": "EASY",
        "description": "Print the nodes in Root -> Left -> Right preorder traversal order.",
        "input_format": "Number of elements followed by level-order values ('N' for null).",
        "output_format": "List of node values in preorder traversal.",
        "constraints": "0 <= number of nodes <= 100",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "company_tags": ["Amazon", "Microsoft"],
        "examples": [
            {"input": "3\n1 2 3", "output": "[1, 2, 3]", "explanation": "Preorder: Root(1) -> Left(2) -> Right(3)."},
            {"input": "5\n1 2 3 4 5", "output": "[1, 2, 4, 5, 3]", "explanation": "1, then left subtree (2, 4, 5), then 3."},
            {"input": "1\n10", "output": "[10]", "explanation": "Single node traversal."}
        ],
        "test_cases": [
            {"input": "3\n1 2 3", "expected": "[1, 2, 3]", "is_hidden": False},
            {"input": "5\n1 2 3 4 5", "expected": "[1, 2, 4, 5, 3]", "is_hidden": False},
            {"input": "1\n10", "expected": "[10]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def preorder(root):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build_tree(char values[][20], int count) {
    if (count == 0 || strcmp(values[0], "N") == 0) return NULL;
    Node* root = createNode(atoi(values[0]));
    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        Node* curr = q[head++];
        if (strcmp(values[i], "N") != 0) {
            curr->left = createNode(atoi(values[i]));
            q[tail++] = curr->left;
        }
        i++;
        if (i < count && strcmp(values[i], "N") != 0) {
            curr->right = createNode(atoi(values[i]));
            q[tail++] = curr->right;
        }
        i++;
    }
    return root;
}

int res[2000];
int res_count = 0;

void preorder(Node* root) {
    if (!root) return;
    res[res_count++] = root->val;
    preorder(root->left);
    preorder(root->right);
}

int main() {
    char tok[50];
    if (scanf("%s", tok) != 1) return 0;
    char values[2000][20];
    int count = 0;
    while (scanf("%s", values[count]) == 1) {
        if (strcmp(values[count], "/") == 0) continue;
        count++;
    }
    Node* root = build_tree(values, count);
    preorder(root);

    printf("[");
    for (int i = 0; i < res_count; i++) {
        printf("%d%s", res[i], (i == res_count - 1 ? "" : ", "));
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build_tree(const vector<string>& values) {
    if (values.empty() || values[0] == "N") return NULL;
    Node* root = new Node(stoi(values[0]));
    queue<Node*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        Node* curr = q.front();
        q.pop();
        if (values[i] != "N") {
            curr->left = new Node(stoi(values[i]));
            q.push(curr->left);
        }
        i++;
        if (i < values.size() && values[i] != "N") {
            curr->right = new Node(stoi(values[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

void preorder(Node* root, vector<int>& res) {
    if (!root) return;
    res.push_back(root->val);
    preorder(root->left, res);
    preorder(root->right, res);
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    vector<string> values;
    while (cin >> token) {
        if (token != "/") values.push_back(token);
    }
    Node* root = build_tree(values);
    vector<int> res;
    preorder(root, res);

    cout << "[";
    for (size_t i = 0; i < res.size(); i++) {
        cout << res[i] << (i == res.size() - 1 ? "" : ", ");
    }
    cout << "]\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static Node build_tree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("N")) return null;
        Node root = new Node(Integer.parseInt(values.get(0)));
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.size()) {
            Node curr = q.poll();
            if (!values.get(i).equals("N")) {
                curr.left = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < values.size() && !values.get(i).equals("N")) {
                curr.right = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    static void preorder(Node root, List<Integer> res) {
        if (root == null) return;
        res.add(root.val);
        preorder(root.left, res);
        preorder(root.right, res);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        sc.next();
        List<String> values = new ArrayList<>();
        while (sc.hasNext()) {
            String tok = sc.next();
            if (!tok.equals("/")) values.add(tok);
        }
        Node root = build_tree(values);
        List<Integer> res = new ArrayList<>();
        preorder(root, res);
        System.out.println(res.toString());
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if raw:
        n = int(raw[0])
        values = raw[1:]
        root = build_tree(values)
        print(preorder(root))"""
        })
    },

    # 20. Postorder Traversal
    {
        "id": "dsa-tree-postorder-traversal",
        "problem_num": 155,
        "title": "Postorder Traversal",
        "category": "Trees",
        "topic": "Tree Traversals",
        "subtopic": "Left-Right-Root",
        "difficulty": "EASY",
        "description": "Print the nodes in Left -> Right -> Root postorder traversal order.",
        "input_format": "Number of elements followed by level-order values ('N' for null).",
        "output_format": "List of node values in postorder traversal.",
        "constraints": "0 <= number of nodes <= 100",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "company_tags": ["Amazon", "Microsoft"],
        "examples": [
            {"input": "3\n1 2 3", "output": "[2, 3, 1]", "explanation": "Postorder: Left(2) -> Right(3) -> Root(1)."},
            {"input": "5\n1 2 3 4 5", "output": "[4, 5, 2, 3, 1]", "explanation": "Left children first, then right, then root."},
            {"input": "1\n10", "output": "[10]", "explanation": "Single node traversal."}
        ],
        "test_cases": [
            {"input": "3\n1 2 3", "expected": "[2, 3, 1]", "is_hidden": False},
            {"input": "5\n1 2 3 4 5", "expected": "[4, 5, 2, 3, 1]", "is_hidden": False},
            {"input": "1\n10", "expected": "[10]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def postorder(root):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build_tree(char values[][20], int count) {
    if (count == 0 || strcmp(values[0], "N") == 0) return NULL;
    Node* root = createNode(atoi(values[0]));
    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        Node* curr = q[head++];
        if (strcmp(values[i], "N") != 0) {
            curr->left = createNode(atoi(values[i]));
            q[tail++] = curr->left;
        }
        i++;
        if (i < count && strcmp(values[i], "N") != 0) {
            curr->right = createNode(atoi(values[i]));
            q[tail++] = curr->right;
        }
        i++;
    }
    return root;
}

int res[2000];
int res_count = 0;

void postorder(Node* root) {
    if (!root) return;
    postorder(root->left);
    postorder(root->right);
    res[res_count++] = root->val;
}

int main() {
    char tok[50];
    if (scanf("%s", tok) != 1) return 0;
    char values[2000][20];
    int count = 0;
    while (scanf("%s", values[count]) == 1) {
        if (strcmp(values[count], "/") == 0) continue;
        count++;
    }
    Node* root = build_tree(values, count);
    postorder(root);

    printf("[");
    for (int i = 0; i < res_count; i++) {
        printf("%d%s", res[i], (i == res_count - 1 ? "" : ", "));
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build_tree(const vector<string>& values) {
    if (values.empty() || values[0] == "N") return NULL;
    Node* root = new Node(stoi(values[0]));
    queue<Node*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        Node* curr = q.front();
        q.pop();
        if (values[i] != "N") {
            curr->left = new Node(stoi(values[i]));
            q.push(curr->left);
        }
        i++;
        if (i < values.size() && values[i] != "N") {
            curr->right = new Node(stoi(values[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

void postorder(Node* root, vector<int>& res) {
    if (!root) return;
    postorder(root->left, res);
    postorder(root->right, res);
    res.push_back(root->val);
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    vector<string> values;
    while (cin >> token) {
        if (token != "/") values.push_back(token);
    }
    Node* root = build_tree(values);
    vector<int> res;
    postorder(root, res);

    cout << "[";
    for (size_t i = 0; i < res.size(); i++) {
        cout << res[i] << (i == res.size() - 1 ? "" : ", ");
    }
    cout << "]\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static Node build_tree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("N")) return null;
        Node root = new Node(Integer.parseInt(values.get(0)));
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.size()) {
            Node curr = q.poll();
            if (!values.get(i).equals("N")) {
                curr.left = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < values.size() && !values.get(i).equals("N")) {
                curr.right = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    static void postorder(Node root, List<Integer> res) {
        if (root == null) return;
        postorder(root.left, res);
        postorder(root.right, res);
        res.add(root.val);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        sc.next();
        List<String> values = new ArrayList<>();
        while (sc.hasNext()) {
            String tok = sc.next();
            if (!tok.equals("/")) values.add(tok);
        }
        Node root = build_tree(values);
        List<Integer> res = new ArrayList<>();
        postorder(root, res);
        System.out.println(res.toString());
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if raw:
        n = int(raw[0])
        values = raw[1:]
        root = build_tree(values)
        print(postorder(root))"""
        })
    },

    # 21. Level Order Traversal
    {
        "id": "dsa-tree-level-order-traversal",
        "problem_num": 156,
        "title": "Level Order Traversal",
        "category": "Trees",
        "topic": "Tree Traversals",
        "subtopic": "Breadth-First Search",
        "difficulty": "MEDIUM",
        "description": "Print the binary tree level by level as a list of lists of values.",
        "input_format": "Number of elements followed by level-order values ('N' for null).",
        "output_format": "List of lists representing level order traversal.",
        "constraints": "0 <= number of nodes <= 2000",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Microsoft", "Facebook"],
        "examples": [
            {"input": "3\n1 2 3", "output": "[[1], [2, 3]]", "explanation": "Level 0: [1], Level 1: [2, 3]."},
            {"input": "5\n1 2 3 4 5", "output": "[[1], [2, 3], [4, 5]]", "explanation": "Level 0: [1], Level 1: [2, 3], Level 2: [4, 5]."},
            {"input": "1\n10", "output": "[[10]]", "explanation": "Single level."}
        ],
        "test_cases": [
            {"input": "3\n1 2 3", "expected": "[[1], [2, 3]]", "is_hidden": False},
            {"input": "5\n1 2 3 4 5", "expected": "[[1], [2, 3], [4, 5]]", "is_hidden": False},
            {"input": "1\n10", "expected": "[[10]]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def level_order(root):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build_tree(char values[][20], int count) {
    if (count == 0 || strcmp(values[0], "N") == 0) return NULL;
    Node* root = createNode(atoi(values[0]));
    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        Node* curr = q[head++];
        if (strcmp(values[i], "N") != 0) {
            curr->left = createNode(atoi(values[i]));
            q[tail++] = curr->left;
        }
        i++;
        if (i < count && strcmp(values[i], "N") != 0) {
            curr->right = createNode(atoi(values[i]));
            q[tail++] = curr->right;
        }
        i++;
    }
    return root;
}

int main() {
    char tok[50];
    if (scanf("%s", tok) != 1) return 0;
    char values[2000][20];
    int count = 0;
    while (scanf("%s", values[count]) == 1) {
        if (strcmp(values[count], "/") == 0) continue;
        count++;
    }
    Node* root = build_tree(values, count);
    if (!root) { printf("[]\\n"); return 0; }

    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;

    printf("[");
    int firstLevel = 1;
    while (head < tail) {
        int sz = tail - head;
        if (!firstLevel) printf(", ");
        firstLevel = 0;
        printf("[");
        for (int i = 0; i < sz; i++) {
            Node* curr = q[head++];
            printf("%d%s", curr->val, (i == sz - 1 ? "" : ", "));
            if (curr->left) q[tail++] = curr->left;
            if (curr->right) q[tail++] = curr->right;
        }
        printf("]");
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build_tree(const vector<string>& values) {
    if (values.empty() || values[0] == "N") return NULL;
    Node* root = new Node(stoi(values[0]));
    queue<Node*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        Node* curr = q.front();
        q.pop();
        if (values[i] != "N") {
            curr->left = new Node(stoi(values[i]));
            q.push(curr->left);
        }
        i++;
        if (i < values.size() && values[i] != "N") {
            curr->right = new Node(stoi(values[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    vector<string> values;
    while (cin >> token) {
        if (token != "/") values.push_back(token);
    }
    Node* root = build_tree(values);
    if (!root) { cout << "[]\\n"; return 0; }

    queue<Node*> q;
    q.push(root);
    vector<vector<int>> result;

    while (!q.empty()) {
        int sz = q.size();
        vector<int> level;
        for (int i = 0; i < sz; i++) {
            Node* curr = q.front();
            q.pop();
            level.push_back(curr->val);
            if (curr->left) q.push(curr->left);
            if (curr->right) q.push(curr->right);
        }
        result.push_back(level);
    }

    cout << "[";
    for (size_t i = 0; i < result.size(); i++) {
        cout << "[";
        for (size_t j = 0; j < result[i].size(); j++) {
            cout << result[i][j] << (j == result[i].size() - 1 ? "" : ", ");
        }
        cout << "]" << (i == result.size() - 1 ? "" : ", ");
    }
    cout << "]\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static Node build_tree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("N")) return null;
        Node root = new Node(Integer.parseInt(values.get(0)));
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.size()) {
            Node curr = q.poll();
            if (!values.get(i).equals("N")) {
                curr.left = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < values.size() && !values.get(i).equals("N")) {
                curr.right = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        sc.next();
        List<String> values = new ArrayList<>();
        while (sc.hasNext()) {
            String tok = sc.next();
            if (!tok.equals("/")) values.add(tok);
        }
        Node root = build_tree(values);
        if (root == null) { System.out.println("[]"); return; }

        Queue<Node> q = new LinkedList<>();
        q.add(root);
        List<List<Integer>> result = new ArrayList<>();

        while (!q.isEmpty()) {
            int sz = q.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < sz; i++) {
                Node curr = q.poll();
                level.add(curr.val);
                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
            result.add(level);
        }

        System.out.println(result.toString());
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def level_order(root):
    if not root:
        return []
    q = deque([root])
    result = []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if raw:
        n = int(raw[0])
        values = raw[1:]
        root = build_tree(values)
        print(level_order(root))"""
        })
    },

    # 22. Invert Binary Tree
    {
        "id": "dsa-tree-invert-binary-tree",
        "problem_num": 157,
        "title": "Invert Binary Tree",
        "category": "Trees",
        "topic": "Binary Tree Modification",
        "subtopic": "Tree Mirroring",
        "difficulty": "MEDIUM",
        "description": "Invert a binary tree (swap left and right child of every node) and return its level-order representation.",
        "input_format": "Number of elements followed by level-order values ('N' for null).",
        "output_format": "Level order traversal of the inverted tree.",
        "constraints": "0 <= number of nodes <= 100",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "company_tags": ["Google", "Twitter", "Amazon"],
        "examples": [
            {"input": "3\n1 2 3", "output": "[[1], [3, 2]]", "explanation": "Children 2 and 3 swapped."},
            {"input": "5\n1 2 3 4 5", "output": "[[1], [3, 2], [5, 4]]", "explanation": "Inverted tree level by level."},
            {"input": "1\n10", "output": "[[10]]", "explanation": "Single node unchanged."}
        ],
        "test_cases": [
            {"input": "3\n1 2 3", "expected": "[[1], [3, 2]]", "is_hidden": False},
            {"input": "5\n1 2 3 4 5", "expected": "[[1], [3, 2], [5, 4]]", "is_hidden": False},
            {"input": "1\n10", "expected": "[[10]]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def invert_tree(root):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build_tree(char values[][20], int count) {
    if (count == 0 || strcmp(values[0], "N") == 0) return NULL;
    Node* root = createNode(atoi(values[0]));
    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        Node* curr = q[head++];
        if (strcmp(values[i], "N") != 0) {
            curr->left = createNode(atoi(values[i]));
            q[tail++] = curr->left;
        }
        i++;
        if (i < count && strcmp(values[i], "N") != 0) {
            curr->right = createNode(atoi(values[i]));
            q[tail++] = curr->right;
        }
        i++;
    }
    return root;
}

Node* invert_tree(Node* root) {
    if (!root) return NULL;
    Node* temp = root->left;
    root->left = root->right;
    root->right = temp;
    invert_tree(root->left);
    invert_tree(root->right);
    return root;
}

int main() {
    char tok[50];
    if (scanf("%s", tok) != 1) return 0;
    char values[2000][20];
    int count = 0;
    while (scanf("%s", values[count]) == 1) {
        if (strcmp(values[count], "/") == 0) continue;
        count++;
    }
    Node* root = build_tree(values, count);
    root = invert_tree(root);
    if (!root) { printf("[]\\n"); return 0; }

    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;

    printf("[");
    int firstLevel = 1;
    while (head < tail) {
        int sz = tail - head;
        if (!firstLevel) printf(", ");
        firstLevel = 0;
        printf("[");
        for (int i = 0; i < sz; i++) {
            Node* curr = q[head++];
            printf("%d%s", curr->val, (i == sz - 1 ? "" : ", "));
            if (curr->left) q[tail++] = curr->left;
            if (curr->right) q[tail++] = curr->right;
        }
        printf("]");
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build_tree(const vector<string>& values) {
    if (values.empty() || values[0] == "N") return NULL;
    Node* root = new Node(stoi(values[0]));
    queue<Node*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        Node* curr = q.front();
        q.pop();
        if (values[i] != "N") {
            curr->left = new Node(stoi(values[i]));
            q.push(curr->left);
        }
        i++;
        if (i < values.size() && values[i] != "N") {
            curr->right = new Node(stoi(values[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

Node* invert_tree(Node* root) {
    if (!root) return NULL;
    swap(root->left, root->right);
    invert_tree(root->left);
    invert_tree(root->right);
    return root;
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    vector<string> values;
    while (cin >> token) {
        if (token != "/") values.push_back(token);
    }
    Node* root = build_tree(values);
    root = invert_tree(root);
    if (!root) { cout << "[]\\n"; return 0; }

    queue<Node*> q;
    q.push(root);
    vector<vector<int>> result;

    while (!q.empty()) {
        int sz = q.size();
        vector<int> level;
        for (int i = 0; i < sz; i++) {
            Node* curr = q.front();
            q.pop();
            level.push_back(curr->val);
            if (curr->left) q.push(curr->left);
            if (curr->right) q.push(curr->right);
        }
        result.push_back(level);
    }

    cout << "[";
    for (size_t i = 0; i < result.size(); i++) {
        cout << "[";
        for (size_t j = 0; j < result[i].size(); j++) {
            cout << result[i][j] << (j == result[i].size() - 1 ? "" : ", ");
        }
        cout << "]" << (i == result.size() - 1 ? "" : ", ");
    }
    cout << "]\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static Node build_tree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("N")) return null;
        Node root = new Node(Integer.parseInt(values.get(0)));
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.size()) {
            Node curr = q.poll();
            if (!values.get(i).equals("N")) {
                curr.left = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < values.size() && !values.get(i).equals("N")) {
                curr.right = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    static Node invert_tree(Node root) {
        if (root == null) return null;
        Node temp = root.left;
        root.left = root.right;
        root.right = temp;
        invert_tree(root.left);
        invert_tree(root.right);
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        sc.next();
        List<String> values = new ArrayList<>();
        while (sc.hasNext()) {
            String tok = sc.next();
            if (!tok.equals("/")) values.add(tok);
        }
        Node root = build_tree(values);
        root = invert_tree(root);
        if (root == null) { System.out.println("[]"); return; }

        Queue<Node> q = new LinkedList<>();
        q.add(root);
        List<List<Integer>> result = new ArrayList<>();

        while (!q.isEmpty()) {
            int sz = q.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < sz; i++) {
                Node curr = q.poll();
                level.add(curr.val);
                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
            result.add(level);
        }

        System.out.println(result.toString());
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root

def level_order(root):
    if not root:
        return []
    q = deque([root])
    result = []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if raw:
        n = int(raw[0])
        values = raw[1:]
        root = build_tree(values)
        root = invert_tree(root)
        print(level_order(root))"""
        })
    },

    # 23. Diameter of Binary Tree
    {
        "id": "dsa-tree-diameter-binary-tree",
        "problem_num": 158,
        "title": "Diameter of Binary Tree",
        "category": "Trees",
        "topic": "Tree Properties",
        "subtopic": "Longest Path in Edges",
        "difficulty": "MEDIUM",
        "description": "Find the length of the diameter of a binary tree (the length of the longest path between any two nodes in edges).",
        "input_format": "Number of elements followed by level-order values ('N' for null).",
        "output_format": "Integer representing diameter in edges.",
        "constraints": "1 <= number of nodes <= 10^4",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "company_tags": ["Facebook", "Amazon", "Microsoft"],
        "examples": [
            {"input": "3\n1 2 3", "output": "2", "explanation": "Path 2 -> 1 -> 3 has length 2 edges."},
            {"input": "5\n1 2 3 4 5", "output": "3", "explanation": "Path 4 -> 2 -> 1 -> 3 has length 3 edges."},
            {"input": "1\n10", "output": "0", "explanation": "Single node has 0 edges."}
        ],
        "test_cases": [
            {"input": "3\n1 2 3", "expected": "2", "is_hidden": False},
            {"input": "5\n1 2 3 4 5", "expected": "3", "is_hidden": False},
            {"input": "1\n10", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def diameter(root):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build_tree(char values[][20], int count) {
    if (count == 0 || strcmp(values[0], "N") == 0) return NULL;
    Node* root = createNode(atoi(values[0]));
    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        Node* curr = q[head++];
        if (strcmp(values[i], "N") != 0) {
            curr->left = createNode(atoi(values[i]));
            q[tail++] = curr->left;
        }
        i++;
        if (i < count && strcmp(values[i], "N") != 0) {
            curr->right = createNode(atoi(values[i]));
            q[tail++] = curr->right;
        }
        i++;
    }
    return root;
}

int max_diam = 0;

int height(Node* node) {
    if (!node) return 0;
    int l = height(node->left);
    int r = height(node->right);
    if (l + r > max_diam) max_diam = l + r;
    return 1 + (l > r ? l : r);
}

int main() {
    char tok[50];
    if (scanf("%s", tok) != 1) return 0;
    char values[2000][20];
    int count = 0;
    while (scanf("%s", values[count]) == 1) {
        if (strcmp(values[count], "/") == 0) continue;
        count++;
    }
    Node* root = build_tree(values, count);
    height(root);
    printf("%d\\n", max_diam);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build_tree(const vector<string>& values) {
    if (values.empty() || values[0] == "N") return NULL;
    Node* root = new Node(stoi(values[0]));
    queue<Node*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        Node* curr = q.front();
        q.pop();
        if (values[i] != "N") {
            curr->left = new Node(stoi(values[i]));
            q.push(curr->left);
        }
        i++;
        if (i < values.size() && values[i] != "N") {
            curr->right = new Node(stoi(values[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

int max_d = 0;

int height(Node* node) {
    if (!node) return 0;
    int l = height(node->left);
    int r = height(node->right);
    max_d = max(max_d, l + r);
    return 1 + max(l, r);
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    vector<string> values;
    while (cin >> token) {
        if (token != "/") values.push_back(token);
    }
    Node* root = build_tree(values);
    height(root);
    cout << max_d << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static Node build_tree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("N")) return null;
        Node root = new Node(Integer.parseInt(values.get(0)));
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.size()) {
            Node curr = q.poll();
            if (!values.get(i).equals("N")) {
                curr.left = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < values.size() && !values.get(i).equals("N")) {
                curr.right = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    static int maxD = 0;

    static int height(Node node) {
        if (node == null) return 0;
        int l = height(node.left);
        int r = height(node.right);
        maxD = Math.max(maxD, l + r);
        return 1 + Math.max(l, r);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        sc.next();
        List<String> values = new ArrayList<>();
        while (sc.hasNext()) {
            String tok = sc.next();
            if (!tok.equals("/")) values.add(tok);
        }
        Node root = build_tree(values);
        height(root);
        System.out.println(maxD);
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def diameter(root):
    result = [0]
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        result[0] = max(result[0], left + right)
        return 1 + max(left, right)
    height(root)
    return result[0]

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if raw:
        n = int(raw[0])
        values = raw[1:]
        root = build_tree(values)
        print(diameter(root))"""
        })
    },

    # 24. Check Balanced Binary Tree
    {
        "id": "dsa-tree-check-balanced",
        "problem_num": 159,
        "title": "Check Balanced Binary Tree",
        "category": "Trees",
        "topic": "Tree Properties",
        "subtopic": "Height Balanced Tree",
        "difficulty": "MEDIUM",
        "description": "Determine if a binary tree is height-balanced (height difference between left and right subtrees <= 1 for all nodes).",
        "input_format": "Number of elements followed by level-order values ('N' for null).",
        "output_format": "True or False.",
        "constraints": "0 <= number of nodes <= 5000",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "company_tags": ["Amazon", "Google", "Bloomberg"],
        "examples": [
            {"input": "3\n1 2 3", "output": "True", "explanation": "Heights of both subtrees are 1, difference 0."},
            {"input": "5\n1 2 3 4 5", "output": "True", "explanation": "Subtree height difference <= 1 everywhere."},
            {"input": "5\n1 2 N 3 N 4 N", "output": "False", "explanation": "Skewed chain, height difference exceeds 1."}
        ],
        "test_cases": [
            {"input": "3\n1 2 3", "expected": "True", "is_hidden": False},
            {"input": "5\n1 2 3 4 5", "expected": "True", "is_hidden": False},
            {"input": "5\n1 2 N 3 N 4 N", "expected": "False", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def is_balanced(root):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build_tree(char values[][20], int count) {
    if (count == 0 || strcmp(values[0], "N") == 0) return NULL;
    Node* root = createNode(atoi(values[0]));
    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        Node* curr = q[head++];
        if (strcmp(values[i], "N") != 0) {
            curr->left = createNode(atoi(values[i]));
            q[tail++] = curr->left;
        }
        i++;
        if (i < count && strcmp(values[i], "N") != 0) {
            curr->right = createNode(atoi(values[i]));
            q[tail++] = curr->right;
        }
        i++;
    }
    return root;
}

int checkHeight(Node* node) {
    if (!node) return 0;
    int l = checkHeight(node->left);
    if (l == -1) return -1;
    int r = checkHeight(node->right);
    if (r == -1) return -1;
    if (abs(l - r) > 1) return -1;
    return 1 + (l > r ? l : r);
}

int main() {
    char tok[50];
    if (scanf("%s", tok) != 1) return 0;
    char values[2000][20];
    int count = 0;
    while (scanf("%s", values[count]) == 1) {
        if (strcmp(values[count], "/") == 0) continue;
        count++;
    }
    Node* root = build_tree(values, count);
    printf("%s\\n", checkHeight(root) != -1 ? "True" : "False");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build_tree(const vector<string>& values) {
    if (values.empty() || values[0] == "N") return NULL;
    Node* root = new Node(stoi(values[0]));
    queue<Node*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        Node* curr = q.front();
        q.pop();
        if (values[i] != "N") {
            curr->left = new Node(stoi(values[i]));
            q.push(curr->left);
        }
        i++;
        if (i < values.size() && values[i] != "N") {
            curr->right = new Node(stoi(values[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

int checkHeight(Node* node) {
    if (!node) return 0;
    int l = checkHeight(node->left);
    if (l == -1) return -1;
    int r = checkHeight(node->right);
    if (r == -1) return -1;
    if (abs(l - r) > 1) return -1;
    return 1 + max(l, r);
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    vector<string> values;
    while (cin >> token) {
        if (token != "/") values.push_back(token);
    }
    Node* root = build_tree(values);
    cout << (checkHeight(root) != -1 ? "True" : "False") << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static Node build_tree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("N")) return null;
        Node root = new Node(Integer.parseInt(values.get(0)));
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.size()) {
            Node curr = q.poll();
            if (!values.get(i).equals("N")) {
                curr.left = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < values.size() && !values.get(i).equals("N")) {
                curr.right = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    static int checkHeight(Node node) {
        if (node == null) return 0;
        int l = checkHeight(node.left);
        if (l == -1) return -1;
        int r = checkHeight(node.right);
        if (r == -1) return -1;
        if (Math.abs(l - r) > 1) return -1;
        return 1 + Math.max(l, r);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        sc.next();
        List<String> values = new ArrayList<>();
        while (sc.hasNext()) {
            String tok = sc.next();
            if (!tok.equals("/")) values.add(tok);
        }
        Node root = build_tree(values);
        System.out.println(checkHeight(root) != -1 ? "True" : "False");
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def is_balanced(root):
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    return height(root) != -1

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if raw:
        n = int(raw[0])
        values = raw[1:]
        root = build_tree(values)
        print(is_balanced(root))"""
        })
    },

    # 25. Lowest Common Ancestor
    {
        "id": "dsa-tree-lowest-common-ancestor",
        "problem_num": 160,
        "title": "Lowest Common Ancestor of a Binary Tree",
        "category": "Trees",
        "topic": "Binary Tree LCA",
        "subtopic": "Tree Ancestry",
        "difficulty": "MEDIUM",
        "description": "Given a binary tree and two node values p and q, find the lowest common ancestor (LCA) node.",
        "input_format": "Number of elements, level-order values, then p and q.",
        "output_format": "Value of LCA node.",
        "constraints": "Number of nodes in tree [2, 10^5], all node values unique.",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "company_tags": ["Facebook", "Amazon", "Microsoft"],
        "examples": [
            {"input": "7\n3 5 1 6 2 0 8\n5 1", "output": "3", "explanation": "LCA of 5 and 1 is root 3."},
            {"input": "7\n3 5 1 6 2 0 8\n5 4", "output": "5", "explanation": "LCA of 5 and 4 (in subtree) is 5."},
            {"input": "3\n1 2 3\n2 3", "output": "1", "explanation": "LCA of 2 and 3 is 1."}
        ],
        "test_cases": [
            {"input": "7\n3 5 1 6 2 0 8\n5 1", "expected": "3", "is_hidden": False},
            {"input": "7\n3 5 1 6 2 0 8\n5 4", "expected": "5", "is_hidden": False},
            {"input": "3\n1 2 3\n2 3", "expected": "1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def lowest_common_ancestor(root, p, q):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build_tree(char values[][20], int count) {
    if (count == 0 || strcmp(values[0], "N") == 0) return NULL;
    Node* root = createNode(atoi(values[0]));
    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        Node* curr = q[head++];
        if (strcmp(values[i], "N") != 0) {
            curr->left = createNode(atoi(values[i]));
            q[tail++] = curr->left;
        }
        i++;
        if (i < count && strcmp(values[i], "N") != 0) {
            curr->right = createNode(atoi(values[i]));
            q[tail++] = curr->right;
        }
        i++;
    }
    return root;
}

Node* lca(Node* root, int p, int q) {
    if (!root || root->val == p || root->val == q) return root;
    Node* left = lca(root->left, p, q);
    Node* right = lca(root->right, p, q);
    if (left && right) return root;
    return left ? left : right;
}

int main() {
    char tok[50];
    if (scanf("%s", tok) != 1) return 0;
    char tokens[2000][20];
    int count = 0;
    while (scanf("%s", tokens[count]) == 1) {
        if (strcmp(tokens[count], "/") == 0) continue;
        count++;
    }
    if (count < 2) return 0;
    int p = atoi(tokens[count - 2]);
    int q_val = atoi(tokens[count - 1]);
    int tree_count = count - 2;

    Node* root = build_tree(tokens, tree_count);
    Node* ans = lca(root, p, q_val);
    if (ans) printf("%d\\n", ans->val);
    else printf("-1\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build_tree(const vector<string>& values) {
    if (values.empty() || values[0] == "N") return NULL;
    Node* root = new Node(stoi(values[0]));
    queue<Node*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        Node* curr = q.front();
        q.pop();
        if (values[i] != "N") {
            curr->left = new Node(stoi(values[i]));
            q.push(curr->left);
        }
        i++;
        if (i < values.size() && values[i] != "N") {
            curr->right = new Node(stoi(values[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

Node* lca(Node* root, int p, int q) {
    if (!root || root->val == p || root->val == q) return root;
    Node* left = lca(root->left, p, q);
    Node* right = lca(root->right, p, q);
    if (left && right) return root;
    return left ? left : right;
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    vector<string> all_tokens;
    while (cin >> token) {
        if (token != "/") all_tokens.push_back(token);
    }
    if (all_tokens.size() < 2) return 0;
    int p = stoi(all_tokens[all_tokens.size() - 2]);
    int q_val = stoi(all_tokens[all_tokens.size() - 1]);
    all_tokens.pop_back();
    all_tokens.pop_back();

    Node* root = build_tree(all_tokens);
    Node* ans = lca(root, p, q_val);
    if (ans) cout << ans->val << "\\n";
    else cout << -1 << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static Node build_tree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("N")) return null;
        Node root = new Node(Integer.parseInt(values.get(0)));
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.size()) {
            Node curr = q.poll();
            if (!values.get(i).equals("N")) {
                curr.left = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < values.size() && !values.get(i).equals("N")) {
                curr.right = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    static Node lca(Node root, int p, int q) {
        if (root == null || root.val == p || root.val == q) return root;
        Node left = lca(root.left, p, q);
        Node right = lca(root.right, p, q);
        if (left != null && right != null) return root;
        return left != null ? left : right;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        sc.next();
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String tok = sc.next();
            if (!tok.equals("/")) tokens.add(tok);
        }
        if (tokens.size() < 2) return;
        int p = Integer.parseInt(tokens.get(tokens.size() - 2));
        int q = Integer.parseInt(tokens.get(tokens.size() - 1));
        List<String> treeVals = tokens.subList(0, tokens.size() - 2);

        Node root = build_tree(treeVals);
        Node ans = lca(root, p, q);
        System.out.println(ans != null ? ans.val : -1);
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def lowest_common_ancestor(root, p, q):
    if not root or root.val == p or root.val == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if len(raw) >= 3:
        p = int(raw[-2])
        q = int(raw[-1])
        values = raw[1:-2]
        root = build_tree(values)
        ans = lowest_common_ancestor(root, p, q)
        print(ans.val if ans else -1)"""
        })
    },

    # 26. Binary Tree Maximum Path Sum
    {
        "id": "dsa-tree-max-path-sum",
        "problem_num": 161,
        "title": "Binary Tree Maximum Path Sum",
        "category": "Trees",
        "topic": "Tree DP",
        "subtopic": "Max Path Sum Across Any Node",
        "difficulty": "HARD",
        "description": "Find the maximum path sum of any non-empty path in a binary tree.",
        "input_format": "Number of elements followed by level-order values ('N' for null).",
        "output_format": "Maximum path sum.",
        "constraints": "-1000 <= Node.val <= 1000, 1 <= number of nodes <= 3 * 10^4",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "company_tags": ["Facebook", "Google", "Amazon"],
        "examples": [
            {"input": "3\n1 2 3", "output": "6", "explanation": "Path 2 -> 1 -> 3 has sum 6."},
            {"input": "7\n-10 9 20 N N 15 7", "output": "42", "explanation": "Path 15 -> 20 -> 7 has sum 42."},
            {"input": "1\n-3", "output": "-3", "explanation": "Single node with value -3."}
        ],
        "test_cases": [
            {"input": "3\n1 2 3", "expected": "6", "is_hidden": False},
            {"input": "7\n-10 9 20 N N 15 7", "expected": "42", "is_hidden": False},
            {"input": "1\n-3", "expected": "-3", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def max_path_sum(root):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build_tree(char values[][20], int count) {
    if (count == 0 || strcmp(values[0], "N") == 0) return NULL;
    Node* root = createNode(atoi(values[0]));
    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        Node* curr = q[head++];
        if (strcmp(values[i], "N") != 0) {
            curr->left = createNode(atoi(values[i]));
            q[tail++] = curr->left;
        }
        i++;
        if (i < count && strcmp(values[i], "N") != 0) {
            curr->right = createNode(atoi(values[i]));
            q[tail++] = curr->right;
        }
        i++;
    }
    return root;
}

int max_sum = -1000000000;

int dfs(Node* root) {
    if (!root) return 0;
    int l = dfs(root->left);
    int r = dfs(root->right);
    if (l < 0) l = 0;
    if (r < 0) r = 0;
    int pathThrough = root->val + l + r;
    if (pathThrough > max_sum) max_sum = pathThrough;
    return root->val + (l > r ? l : r);
}

int main() {
    char tok[50];
    if (scanf("%s", tok) != 1) return 0;
    char values[2000][20];
    int count = 0;
    while (scanf("%s", values[count]) == 1) {
        if (strcmp(values[count], "/") == 0) continue;
        count++;
    }
    Node* root = build_tree(values, count);
    dfs(root);
    printf("%d\\n", max_sum);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build_tree(const vector<string>& values) {
    if (values.empty() || values[0] == "N") return NULL;
    Node* root = new Node(stoi(values[0]));
    queue<Node*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        Node* curr = q.front();
        q.pop();
        if (values[i] != "N") {
            curr->left = new Node(stoi(values[i]));
            q.push(curr->left);
        }
        i++;
        if (i < values.size() && values[i] != "N") {
            curr->right = new Node(stoi(values[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

int max_sum = -1e9;

int dfs(Node* root) {
    if (!root) return 0;
    int l = max(0, dfs(root->left));
    int r = max(0, dfs(root->right));
    max_sum = max(max_sum, root->val + l + r);
    return root->val + max(l, r);
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    vector<string> values;
    while (cin >> token) {
        if (token != "/") values.push_back(token);
    }
    Node* root = build_tree(values);
    dfs(root);
    cout << max_sum << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static Node build_tree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("N")) return null;
        Node root = new Node(Integer.parseInt(values.get(0)));
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.size()) {
            Node curr = q.poll();
            if (!values.get(i).equals("N")) {
                curr.left = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < values.size() && !values.get(i).equals("N")) {
                curr.right = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    static int maxSum = Integer.MIN_VALUE;

    static int dfs(Node root) {
        if (root == null) return 0;
        int l = Math.max(0, dfs(root.left));
        int r = Math.max(0, dfs(root.right));
        maxSum = Math.max(maxSum, root.val + l + r);
        return root.val + Math.max(l, r);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        sc.next();
        List<String> values = new ArrayList<>();
        while (sc.hasNext()) {
            String tok = sc.next();
            if (!tok.equals("/")) values.add(tok);
        }
        Node root = build_tree(values);
        dfs(root);
        System.out.println(maxSum);
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def max_path_sum(root):
    answer = [float('-inf')]
    def dfs(node):
        if not node:
            return 0
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))
        answer[0] = max(answer[0], node.val + left + right)
        return node.val + max(left, right)
    dfs(root)
    return answer[0]

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if raw:
        values = raw[1:]
        root = build_tree(values)
        print(max_path_sum(root))"""
        })
    },

    # 27. Serialize and Deserialize Binary Tree
    {
        "id": "dsa-tree-serialize-deserialize",
        "problem_num": 162,
        "title": "Serialize and Deserialize Binary Tree",
        "category": "Trees",
        "topic": "Binary Tree Serialization",
        "subtopic": "String Conversion & Reconstruction",
        "difficulty": "HARD",
        "description": "Serialize a binary tree to a level-order string and reconstruct the original tree.",
        "input_format": "Number of elements followed by level-order values ('N' for null).",
        "output_format": "Serialized string on line 1, reconstructed level-order list on line 2.",
        "constraints": "Number of nodes <= 1000",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Google", "Facebook"],
        "examples": [
            {"input": "3\n1 2 3", "output": "1 2 3 N N N N\n[[1], [2, 3]]", "explanation": "Tree serialized with leaf nulls, reconstructed properly."},
            {"input": "1\n10", "output": "10 N N\n[[10]]", "explanation": "Root with both null children."},
            {"input": "1\nN", "output": "N\n[]", "explanation": "Empty tree."}
        ],
        "test_cases": [
            {"input": "3\n1 2 3", "expected": "1 2 3 N N N N\n[[1], [2, 3]]", "is_hidden": False},
            {"input": "1\n10", "expected": "10 N N\n[[10]]", "is_hidden": False},
            {"input": "1\nN", "expected": "N\n[]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def serialize(root):\n    # Your code here\n    pass\n\ndef deserialize(data):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build_tree(char values[][20], int count) {
    if (count == 0 || strcmp(values[0], "N") == 0) return NULL;
    Node* root = createNode(atoi(values[0]));
    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        Node* curr = q[head++];
        if (strcmp(values[i], "N") != 0) {
            curr->left = createNode(atoi(values[i]));
            q[tail++] = curr->left;
        }
        i++;
        if (i < count && strcmp(values[i], "N") != 0) {
            curr->right = createNode(atoi(values[i]));
            q[tail++] = curr->right;
        }
        i++;
    }
    return root;
}

int main() {
    char tok[50];
    if (scanf("%s", tok) != 1) return 0;
    char values[2000][20];
    int count = 0;
    while (scanf("%s", values[count]) == 1) {
        if (strcmp(values[count], "/") == 0) continue;
        count++;
    }
    Node* root = build_tree(values, count);
    if (!root) {
        printf("N\\n[]\\n");
        return 0;
    }

    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int first = 1;

    while (head < tail) {
        Node* curr = q[head++];
        if (!first) printf(" ");
        first = 0;
        if (!curr) {
            printf("N");
        } else {
            printf("%d", curr->val);
            q[tail++] = curr->left;
            q[tail++] = curr->right;
        }
    }
    printf("\\n");

    head = 0; tail = 0;
    q[tail++] = root;
    printf("[");
    int firstL = 1;
    while (head < tail) {
        int sz = tail - head;
        if (!firstL) printf(", ");
        firstL = 0;
        printf("[");
        for (int i = 0; i < sz; i++) {
            Node* curr = q[head++];
            printf("%d%s", curr->val, (i == sz - 1 ? "" : ", "));
            if (curr->left) q[tail++] = curr->left;
            if (curr->right) q[tail++] = curr->right;
        }
        printf("]");
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <sstream>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build_tree(const vector<string>& values) {
    if (values.empty() || values[0] == "N") return NULL;
    Node* root = new Node(stoi(values[0]));
    queue<Node*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        Node* curr = q.front();
        q.pop();
        if (values[i] != "N") {
            curr->left = new Node(stoi(values[i]));
            q.push(curr->left);
        }
        i++;
        if (i < values.size() && values[i] != "N") {
            curr->right = new Node(stoi(values[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

string serialize(Node* root) {
    if (!root) return "N";
    string res = "";
    queue<Node*> q;
    q.push(root);
    bool first = true;
    while (!q.empty()) {
        Node* curr = q.front();
        q.pop();
        if (!first) res += " ";
        first = false;
        if (!curr) {
            res += "N";
        } else {
            res += to_string(curr->val);
            q.push(curr->left);
            q.push(curr->right);
        }
    }
    return res;
}

Node* deserialize(const string& data) {
    stringstream ss(data);
    string tok;
    vector<string> values;
    while (ss >> tok) values.push_back(tok);
    return build_tree(values);
}

void printLevelOrder(Node* root) {
    if (!root) { cout << "[]\\n"; return; }
    queue<Node*> q;
    q.push(root);
    vector<vector<int>> res;
    while (!q.empty()) {
        int sz = q.size();
        vector<int> level;
        for (int i = 0; i < sz; i++) {
            Node* curr = q.front();
            q.pop();
            level.push_back(curr->val);
            if (curr->left) q.push(curr->left);
            if (curr->right) q.push(curr->right);
        }
        res.push_back(level);
    }
    cout << "[";
    for (size_t i = 0; i < res.size(); i++) {
        cout << "[";
        for (size_t j = 0; j < res[i].size(); j++) {
            cout << res[i][j] << (j == res[i].size() - 1 ? "" : ", ");
        }
        cout << "]" << (i == res.size() - 1 ? "" : ", ");
    }
    cout << "]\\n";
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    vector<string> values;
    while (cin >> token) {
        if (token != "/") values.push_back(token);
    }
    Node* root = build_tree(values);
    string data = serialize(root);
    cout << data << "\\n";
    printLevelOrder(deserialize(data));
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static Node build_tree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("N")) return null;
        Node root = new Node(Integer.parseInt(values.get(0)));
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.size()) {
            Node curr = q.poll();
            if (!values.get(i).equals("N")) {
                curr.left = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < values.size() && !values.get(i).equals("N")) {
                curr.right = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    static String serialize(Node root) {
        if (root == null) return "N";
        StringBuilder sb = new StringBuilder();
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        boolean first = true;
        while (!q.isEmpty()) {
            Node curr = q.poll();
            if (!first) sb.append(" ");
            first = false;
            if (curr == null) {
                sb.append("N");
            } else {
                sb.append(curr.val);
                q.add(curr.left);
                q.add(curr.right);
            }
        }
        return sb.toString();
    }

    static void printLevelOrder(Node root) {
        if (root == null) { System.out.println("[]"); return; }
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        List<List<Integer>> result = new ArrayList<>();
        while (!q.isEmpty()) {
            int sz = q.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < sz; i++) {
                Node curr = q.poll();
                level.add(curr.val);
                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
            result.add(level);
        }
        System.out.println(result.toString());
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        sc.next();
        List<String> values = new ArrayList<>();
        while (sc.hasNext()) {
            String tok = sc.next();
            if (!tok.equals("/")) values.add(tok);
        }
        Node root = build_tree(values);
        String data = serialize(root);
        System.out.println(data);
        List<String> reconstructed = Arrays.asList(data.split(" "));
        printLevelOrder(build_tree(reconstructed));
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def serialize(root):
    if not root:
        return "N"
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        if not node:
            result.append("N")
        else:
            result.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
    return " ".join(result)

def deserialize(data):
    values = data.split()
    if values[0] == "N":
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != "N":
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != "N":
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def level_order(root):
    if not root:
        return []
    q = deque([root])
    result = []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if raw:
        n = int(raw[0])
        values = raw[1:]
        root = build_tree(values)
        data = serialize(root)
        print(data)
        print(level_order(deserialize(data)))"""
        })
    },

    # 28. Construct Binary Tree from Inorder and Preorder
    {
        "id": "dsa-tree-construct-from-pre-in",
        "problem_num": 163,
        "title": "Construct Tree from Preorder and Inorder Traversal",
        "category": "Trees",
        "topic": "Tree Construction",
        "subtopic": "Preorder & Inorder Reconstruction",
        "difficulty": "HARD",
        "description": "Construct a binary tree given its preorder and inorder traversal arrays, returning its level order representation.",
        "input_format": "Preorder elements on line 1, inorder elements on line 2 (or separated by '/').",
        "output_format": "Level order traversal of the reconstructed tree.",
        "constraints": "1 <= preorder.length <= 3000, all values unique.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Microsoft", "Facebook"],
        "examples": [
            {"input": "1 2 4 5 3\n4 2 5 1 3", "output": "[[1], [2, 3], [4, 5]]", "explanation": "Root is 1, left subtree contains {4, 2, 5}, right subtree contains {3}."},
            {"input": "1 2 3\n2 1 3", "output": "[[1], [2, 3]]", "explanation": "Root 1 with left child 2 and right child 3."},
            {"input": "1\n1", "output": "[[1]]", "explanation": "Single node."}
        ],
        "test_cases": [
            {"input": "1 2 4 5 3\n4 2 5 1 3", "expected": "[[1], [2, 3], [4, 5]]", "is_hidden": False},
            {"input": "1 2 3\n2 1 3", "expected": "[[1], [2, 3]]", "is_hidden": False},
            {"input": "1\n1", "expected": "[[1]]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def build_from_pre_in(preorder, inorder):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build(int* pre, int preL, int preR, int* in, int inL, int inR) {
    if (preL > preR || inL > inR) return NULL;
    int rootVal = pre[preL];
    Node* root = createNode(rootVal);

    int idx = inL;
    while (idx <= inR && in[idx] != rootVal) idx++;
    int leftSize = idx - inL;

    root->left = build(pre, preL + 1, preL + leftSize, in, inL, idx - 1);
    root->right = build(pre, preL + leftSize + 1, preR, in, idx + 1, inR);
    return root;
}

int main() {
    char line1[2000], line2[2000];
    if (!fgets(line1, sizeof(line1), stdin)) return 0;
    if (strchr(line1, '/')) {
        char *slash = strchr(line1, '/');
        *slash = '\\0';
        strcpy(line2, slash + 1);
    } else {
        if (!fgets(line2, sizeof(line2), stdin)) line2[0] = '\\0';
    }

    int pre[1000], in[1000];
    int npre = 0, nin = 0;
    char *tok = strtok(line1, " \\t\\r\\n");
    while (tok) {
        pre[npre++] = atoi(tok);
        tok = strtok(NULL, " \\t\\r\\n");
    }
    tok = strtok(line2, " \\t\\r\\n");
    while (tok) {
        in[nin++] = atoi(tok);
        tok = strtok(NULL, " \\t\\r\\n");
    }

    Node* root = build(pre, 0, npre - 1, in, 0, nin - 1);
    if (!root) { printf("[]\\n"); return 0; }

    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;

    printf("[");
    int firstL = 1;
    while (head < tail) {
        int sz = tail - head;
        if (!firstL) printf(", ");
        firstL = 0;
        printf("[");
        for (int i = 0; i < sz; i++) {
            Node* curr = q[head++];
            printf("%d%s", curr->val, (i == sz - 1 ? "" : ", "));
            if (curr->left) q[tail++] = curr->left;
            if (curr->right) q[tail++] = curr->right;
        }
        printf("]");
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <algorithm>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build(const vector<int>& pre, int preL, int preR, const vector<int>& in, int inL, int inR) {
    if (preL > preR || inL > inR) return NULL;
    int rootVal = pre[preL];
    Node* root = new Node(rootVal);

    int idx = inL;
    while (idx <= inR && in[idx] != rootVal) idx++;
    int leftSize = idx - inL;

    root->left = build(pre, preL + 1, preL + leftSize, in, inL, idx - 1);
    root->right = build(pre, preL + leftSize + 1, preR, in, idx + 1, inR);
    return root;
}

int main() {
    string line1, line2;
    if (!getline(cin, line1)) return 0;
    if (line1.find('/') != string::npos) {
        size_t pos = line1.find('/');
        line2 = line1.substr(pos + 1);
        line1 = line1.substr(0, pos);
    } else {
        getline(cin, line2);
    }

    vector<int> pre, in;
    stringstream ss1(line1), ss2(line2);
    int x;
    while (ss1 >> x) pre.push_back(x);
    while (ss2 >> x) in.push_back(x);

    Node* root = build(pre, 0, (int)pre.size() - 1, in, 0, (int)in.size() - 1);
    if (!root) { cout << "[]\\n"; return 0; }

    queue<Node*> q;
    q.push(root);
    vector<vector<int>> res;
    while (!q.empty()) {
        int sz = q.size();
        vector<int> level;
        for (int i = 0; i < sz; i++) {
            Node* curr = q.front();
            q.pop();
            level.push_back(curr->val);
            if (curr->left) q.push(curr->left);
            if (curr->right) q.push(curr->right);
        }
        res.push_back(level);
    }

    cout << "[";
    for (size_t i = 0; i < res.size(); i++) {
        cout << "[";
        for (size_t j = 0; j < res[i].size(); j++) {
            cout << res[i][j] << (j == res[i].size() - 1 ? "" : ", ");
        }
        cout << "]" << (i == res.size() - 1 ? "" : ", ");
    }
    cout << "]\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static Node build(int[] pre, int preL, int preR, int[] in, int inL, int inR) {
        if (preL > preR || inL > inR) return null;
        int rootVal = pre[preL];
        Node root = new Node(rootVal);

        int idx = inL;
        while (idx <= inR && in[idx] != rootVal) idx++;
        int leftSize = idx - inL;

        root.left = build(pre, preL + 1, preL + leftSize, in, inL, idx - 1);
        root.right = build(pre, preL + leftSize + 1, preR, in, idx + 1, inR);
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine()) return;
        String line1 = sc.nextLine();
        String line2 = "";
        if (line1.contains("/")) {
            String[] parts = line1.split("/", 2);
            line1 = parts[0];
            line2 = parts[1];
        } else if (sc.hasNextLine()) {
            line2 = sc.nextLine();
        }

        List<Integer> preList = new ArrayList<>();
        Scanner s1 = new Scanner(line1);
        while (s1.hasNextInt()) preList.add(s1.nextInt());

        List<Integer> inList = new ArrayList<>();
        Scanner s2 = new Scanner(line2);
        while (s2.hasNextInt()) inList.add(s2.nextInt());

        int[] pre = preList.stream().mapToInt(i -> i).toArray();
        int[] in = inList.stream().mapToInt(i -> i).toArray();

        Node root = build(pre, 0, pre.length - 1, in, 0, in.length - 1);
        if (root == null) { System.out.println("[]"); return; }

        Queue<Node> q = new LinkedList<>();
        q.add(root);
        List<List<Integer>> result = new ArrayList<>();
        while (!q.isEmpty()) {
            int sz = q.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < sz; i++) {
                Node curr = q.poll();
                level.add(curr.val);
                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
            result.add(level);
        }
        System.out.println(result.toString());
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_from_pre_in(preorder, inorder):
    if not preorder:
        return None
    root_val = preorder[0]
    root = Node(root_val)
    index = inorder.index(root_val)
    root.left = build_from_pre_in(preorder[1:index + 1], inorder[:index])
    root.right = build_from_pre_in(preorder[index + 1:], inorder[index + 1:])
    return root

def level_order(root):
    if not root:
        return []
    q = deque([root])
    result = []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if '/' in raw:
        parts = raw.split('/')
        preorder = list(map(int, parts[0].split()))
        inorder_values = list(map(int, parts[1].split()))
    else:
        lines = [l for l in raw.splitlines() if l.strip()]
        preorder = list(map(int, lines[0].split())) if len(lines) > 0 else []
        inorder_values = list(map(int, lines[1].split())) if len(lines) > 1 else []
    root = build_from_pre_in(preorder, inorder_values)
    print(level_order(root))"""
        })
    },

    # 29. Maximum Width of Binary Tree
    {
        "id": "dsa-tree-max-width",
        "problem_num": 164,
        "title": "Maximum Width of Binary Tree",
        "category": "Trees",
        "topic": "Tree Properties",
        "subtopic": "Level Width with Missing Nodes",
        "difficulty": "HARD",
        "description": "Find the maximum width of a binary tree across all levels, including null nodes between leftmost and rightmost non-null nodes.",
        "input_format": "Number of elements followed by level-order values ('N' for null).",
        "output_format": "Integer representing maximum width.",
        "constraints": "1 <= number of nodes <= 3000",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Google"],
        "examples": [
            {"input": "3\n1 2 3", "output": "2", "explanation": "Level 1 has nodes 2 and 3: width = 2."},
            {"input": "7\n1 3 2 5 3 N 9", "output": "4", "explanation": "Level 2 spans from position 0 to position 3: width = 4."},
            {"input": "1\n10", "output": "1", "explanation": "Width of single node tree is 1."}
        ],
        "test_cases": [
            {"input": "3\n1 2 3", "expected": "2", "is_hidden": False},
            {"input": "7\n1 3 2 5 3 N 9", "expected": "4", "is_hidden": False},
            {"input": "1\n10", "expected": "1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def maximum_width(root):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build_tree(char values[][20], int count) {
    if (count == 0 || strcmp(values[0], "N") == 0) return NULL;
    Node* root = createNode(atoi(values[0]));
    Node* q[4000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        Node* curr = q[head++];
        if (strcmp(values[i], "N") != 0) {
            curr->left = createNode(atoi(values[i]));
            q[tail++] = curr->left;
        }
        i++;
        if (i < count && strcmp(values[i], "N") != 0) {
            curr->right = createNode(atoi(values[i]));
            q[tail++] = curr->right;
        }
        i++;
    }
    return root;
}

typedef struct {
    Node* node;
    unsigned long long id;
} QItem;

int main() {
    char tok[50];
    if (scanf("%s", tok) != 1) return 0;
    char values[4000][20];
    int count = 0;
    while (scanf("%s", values[count]) == 1) {
        if (strcmp(values[count], "/") == 0) continue;
        count++;
    }
    Node* root = build_tree(values, count);
    if (!root) { printf("0\\n"); return 0; }

    QItem q[10000];
    int head = 0, tail = 0;
    q[tail].node = root;
    q[tail].id = 0;
    tail++;

    unsigned long long max_w = 0;

    while (head < tail) {
        int sz = tail - head;
        unsigned long long base = q[head].id;
        unsigned long long first = 0, last = 0;

        for (int i = 0; i < sz; i++) {
            QItem item = q[head++];
            unsigned long long cur_id = item.id - base;
            if (i == 0) first = cur_id;
            if (i == sz - 1) last = cur_id;

            if (item.node->left) {
                q[tail].node = item.node->left;
                q[tail].id = 2 * cur_id;
                tail++;
            }
            if (item.node->right) {
                q[tail].node = item.node->right;
                q[tail].id = 2 * cur_id + 1;
                tail++;
            }
        }
        if (last - first + 1 > max_w) max_w = last - first + 1;
    }

    printf("%llu\\n", max_w);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build_tree(const vector<string>& values) {
    if (values.empty() || values[0] == "N") return NULL;
    Node* root = new Node(stoi(values[0]));
    queue<Node*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        Node* curr = q.front();
        q.pop();
        if (values[i] != "N") {
            curr->left = new Node(stoi(values[i]));
            q.push(curr->left);
        }
        i++;
        if (i < values.size() && values[i] != "N") {
            curr->right = new Node(stoi(values[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    vector<string> values;
    while (cin >> token) {
        if (token != "/") values.push_back(token);
    }
    Node* root = build_tree(values);
    if (!root) { cout << 0 << "\\n"; return 0; }

    queue<pair<Node*, unsigned long long>> q;
    q.push(make_pair(root, 0ULL));
    unsigned long long ans = 0;

    while (!q.empty()) {
        int sz = q.size();
        unsigned long long base = q.front().second;
        unsigned long long first = 0, last = 0;

        for (int i = 0; i < sz; i++) {
            pair<Node*, unsigned long long> item = q.front();
            q.pop();
            unsigned long long index = item.second - base;
            if (i == 0) first = index;
            if (i == sz - 1) last = index;

            if (item.first->left) q.push(make_pair(item.first->left, 2 * index));
            if (item.first->right) q.push(make_pair(item.first->right, 2 * index + 1));
        }
        ans = max(ans, last - first + 1);
    }

    cout << ans << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static class Pair {
        Node node;
        long index;
        Pair(Node node, long index) { this.node = node; this.index = index; }
    }

    static Node build_tree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("N")) return null;
        Node root = new Node(Integer.parseInt(values.get(0)));
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.size()) {
            Node curr = q.poll();
            if (!values.get(i).equals("N")) {
                curr.left = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < values.size() && !values.get(i).equals("N")) {
                curr.right = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        sc.next();
        List<String> values = new ArrayList<>();
        while (sc.hasNext()) {
            String tok = sc.next();
            if (!tok.equals("/")) values.add(tok);
        }
        Node root = build_tree(values);
        if (root == null) { System.out.println(0); return; }

        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(root, 0));
        long ans = 0;

        while (!q.isEmpty()) {
            int sz = q.size();
            long base = q.peek().index;
            long first = 0, last = 0;

            for (int i = 0; i < sz; i++) {
                Pair item = q.poll();
                long index = item.index - base;
                if (i == 0) first = index;
                if (i == sz - 1) last = index;

                if (item.node.left != null) q.add(new Pair(item.node.left, 2 * index));
                if (item.node.right != null) q.add(new Pair(item.node.right, 2 * index + 1));
            }
            ans = Math.max(ans, last - first + 1);
        }

        System.out.println(ans);
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def maximum_width(root):
    if not root:
        return 0
    q = deque([(root, 0)])
    answer = 0
    while q:
        size = len(q)
        base = q[0][1]
        first = last = 0
        for i in range(size):
            node, index = q.popleft()
            index -= base
            if i == 0:
                first = index
            if i == size - 1:
                last = index
            if node.left:
                q.append((node.left, 2 * index))
            if node.right:
                q.append((node.right, 2 * index + 1))
        answer = max(answer, last - first + 1)
    return answer

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if raw:
        n = int(raw[0])
        values = raw[1:]
        root = build_tree(values)
        print(maximum_width(root))"""
        })
    },

    # 30. Recover Binary Search Tree
    {
        "id": "dsa-tree-recover-bst",
        "problem_num": 165,
        "title": "Recover Binary Search Tree",
        "category": "Trees",
        "topic": "Binary Search Tree",
        "subtopic": "BST Inorder Recovery",
        "difficulty": "HARD",
        "description": "Two nodes of a BST were swapped by mistake. Recover the tree without changing its structure, returning its inorder traversal.",
        "input_format": "Number of elements followed by level-order values ('N' for null).",
        "output_format": "Inorder traversal of the recovered BST.",
        "constraints": "Number of nodes [2, 1000]",
        "time_complexity": "O(N)",
        "space_complexity": "O(H)",
        "company_tags": ["Amazon", "Microsoft", "Google"],
        "examples": [
            {"input": "3\n2 3 1", "output": "[1, 2, 3]", "explanation": "Swapping 3 and 1 restores BST order [1, 2, 3]."},
            {"input": "3\n3 1 2", "output": "[1, 2, 3]", "explanation": "Swapping 3 and 2 restores BST order [1, 2, 3]."},
            {"input": "6\n3 1 4 N N 2", "output": "[1, 2, 3, 4]", "explanation": "Swapping 2 and 3 restores BST order [1, 2, 3, 4]."}
        ],
        "test_cases": [
            {"input": "3\n2 3 1", "expected": "[1, 2, 3]", "is_hidden": False},
            {"input": "3\n3 1 2", "expected": "[1, 2, 3]", "is_hidden": False},
            {"input": "6\n3 1 4 N N 2", "expected": "[1, 2, 3, 4]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def recover_tree(root):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *left, *right;
} Node;

Node* createNode(int val) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->left = n->right = NULL;
    return n;
}

Node* build_tree(char values[][20], int count) {
    if (count == 0 || strcmp(values[0], "N") == 0) return NULL;
    Node* root = createNode(atoi(values[0]));
    Node* q[2000];
    int head = 0, tail = 0;
    q[tail++] = root;
    int i = 1;
    while (head < tail && i < count) {
        Node* curr = q[head++];
        if (strcmp(values[i], "N") != 0) {
            curr->left = createNode(atoi(values[i]));
            q[tail++] = curr->left;
        }
        i++;
        if (i < count && strcmp(values[i], "N") != 0) {
            curr->right = createNode(atoi(values[i]));
            q[tail++] = curr->right;
        }
        i++;
    }
    return root;
}

Node *firstN = NULL, *secondN = NULL, *prevN = NULL;

void inorderCheck(Node* node) {
    if (!node) return;
    inorderCheck(node->left);
    if (prevN && prevN->val > node->val) {
        if (!firstN) firstN = prevN;
        secondN = node;
    }
    prevN = node;
    inorderCheck(node->right);
}

int in_vals[2000];
int in_count = 0;

void getInorder(Node* node) {
    if (!node) return;
    getInorder(node->left);
    in_vals[in_count++] = node->val;
    getInorder(node->right);
}

int main() {
    char tok[50];
    if (scanf("%s", tok) != 1) return 0;
    char values[2000][20];
    int count = 0;
    while (scanf("%s", values[count]) == 1) {
        if (strcmp(values[count], "/") == 0) continue;
        count++;
    }
    Node* root = build_tree(values, count);
    inorderCheck(root);
    if (firstN && secondN) {
        int temp = firstN->val;
        firstN->val = secondN->val;
        secondN->val = temp;
    }

    getInorder(root);
    printf("[");
    for (int i = 0; i < in_count; i++) {
        printf("%d%s", in_vals[i], (i == in_count - 1 ? "" : ", "));
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node* build_tree(const vector<string>& values) {
    if (values.empty() || values[0] == "N") return NULL;
    Node* root = new Node(stoi(values[0]));
    queue<Node*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        Node* curr = q.front();
        q.pop();
        if (values[i] != "N") {
            curr->left = new Node(stoi(values[i]));
            q.push(curr->left);
        }
        i++;
        if (i < values.size() && values[i] != "N") {
            curr->right = new Node(stoi(values[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

Node *firstNode = NULL, *secondNode = NULL, *prevNode = NULL;

void inorderCheck(Node* node) {
    if (!node) return;
    inorderCheck(node->left);
    if (prevNode && prevNode->val > node->val) {
        if (!firstNode) firstNode = prevNode;
        secondNode = node;
    }
    prevNode = node;
    inorderCheck(node->right);
}

void getInorder(Node* node, vector<int>& res) {
    if (!node) return;
    getInorder(node->left, res);
    res.push_back(node->val);
    getInorder(node->right, res);
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    vector<string> values;
    while (cin >> token) {
        if (token != "/") values.push_back(token);
    }
    Node* root = build_tree(values);
    inorderCheck(root);
    if (firstNode && secondNode) {
        swap(firstNode->val, secondNode->val);
    }

    vector<int> res;
    getInorder(root, res);
    cout << "[";
    for (size_t i = 0; i < res.size(); i++) {
        cout << res[i] << (i == res.size() - 1 ? "" : ", ");
    }
    cout << "]\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    static Node build_tree(List<String> values) {
        if (values.isEmpty() || values.get(0).equals("N")) return null;
        Node root = new Node(Integer.parseInt(values.get(0)));
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.size()) {
            Node curr = q.poll();
            if (!values.get(i).equals("N")) {
                curr.left = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.left);
            }
            i++;
            if (i < values.size() && !values.get(i).equals("N")) {
                curr.right = new Node(Integer.parseInt(values.get(i)));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    static Node firstNode = null, secondNode = null, prevNode = null;

    static void inorderCheck(Node node) {
        if (node == null) return;
        inorderCheck(node.left);
        if (prevNode != null && prevNode.val > node.val) {
            if (firstNode == null) firstNode = prevNode;
            secondNode = node;
        }
        prevNode = node;
        inorderCheck(node.right);
    }

    static void getInorder(Node node, List<Integer> res) {
        if (node == null) return;
        getInorder(node.left, res);
        res.add(node.val);
        getInorder(node.right, res);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        sc.next();
        List<String> values = new ArrayList<>();
        while (sc.hasNext()) {
            String tok = sc.next();
            if (!tok.equals("/")) values.add(tok);
        }
        Node root = build_tree(values);
        inorderCheck(root);
        if (firstNode != null && secondNode != null) {
            int temp = firstNode.val;
            firstNode.val = secondNode.val;
            secondNode.val = temp;
        }

        List<Integer> res = new ArrayList<>();
        getInorder(root, res);
        System.out.println(res.toString());
    }
}""",
            "python": """import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'N':
        return None
    root = Node(int(values[0]))
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if values[i] != 'N':
            node.left = Node(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'N':
            node.right = Node(int(values[i]))
            q.append(node.right)
        i += 1
    return root

def recover_tree(root):
    first = second = prev = None
    def inorder_check(node):
        nonlocal first, second, prev
        if not node:
            return
        inorder_check(node.left)
        if prev and prev.val > node.val:
            if first is None:
                first = prev
            second = node
        prev = node
        inorder_check(node.right)
    inorder_check(root)
    if first and second:
        first.val, second.val = second.val, first.val
    return root

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if raw:
        n = int(raw[0])
        values = raw[1:]
        root = build_tree(values)
        root = recover_tree(root)
        print(inorder(root))"""
        })
    }
]

problems.extend(tree_data)

with open("backend/app/data/dsa_problems_seed.json", "w", encoding="utf-8") as f:
    json.dump(problems, f, indent=2)

print(f"Successfully added 15 Tree problems! Total problems now: {len(problems)}")

