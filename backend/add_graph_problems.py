import sys, os
sys.path.insert(0, os.path.abspath('.'))
import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    problems = json.load(f)

graph_ids = {
    "dsa-graph-adj-list", "dsa-graph-bfs", "dsa-graph-dfs", "dsa-graph-connected-components",
    "dsa-graph-valid-path", "dsa-graph-undirected-cycle", "dsa-graph-directed-cycle",
    "dsa-graph-topological-sort", "dsa-graph-shortest-path-unweighted", "dsa-graph-number-of-islands",
    "dsa-graph-dijkstra", "dsa-graph-bellman-ford", "dsa-graph-floyd-warshall",
    "dsa-graph-kruskal", "dsa-graph-word-ladder"
}
problems = [p for p in problems if p["id"] not in graph_ids]

graph_data = [
    # 1. Implement Graph Using Adjacency List
    {
        "id": "dsa-graph-adj-list",
        "problem_num": 166,
        "title": "Implement Graph Using Adjacency List",
        "category": "Graphs",
        "topic": "Graph Representation",
        "subtopic": "Adjacency List",
        "difficulty": "EASY",
        "description": "Create an undirected graph using an adjacency list and print its representation.",
        "input_format": "Number of vertices n and edges m, followed by m pairs of vertices representing edges.",
        "output_format": "Adjacency list representation formatted as '0:[neighbors], 1:[neighbors], ...'.",
        "constraints": "1 <= n <= 100, 0 <= m <= n*(n-1)/2, 0 <= u, v < n",
        "time_complexity": "O(V + E log E)",
        "space_complexity": "O(V + E)",
        "company_tags": ["Amazon", "Microsoft", "Google"],
        "examples": [
            {"input": "4 3 / 0 1 / 0 2 / 1 3", "output": "0:[1,2], 1:[0,3], 2:[0], 3:[1]", "explanation": "Node 0 connects to 1 and 2, Node 1 connects to 0 and 3, etc."},
            {"input": "3 2 / 0 1 / 1 2", "output": "0:[1], 1:[0,2], 2:[1]", "explanation": "Path graph connecting 0-1-2."},
            {"input": "3 0", "output": "0:[], 1:[], 2:[]", "explanation": "Disconnected graph with no edges."}
        ],
        "test_cases": [
            {"input": "4 3 / 0 1 / 0 2 / 1 3", "expected": "0:[1,2], 1:[0,3], 2:[0], 3:[1]", "is_hidden": False},
            {"input": "3 2 / 0 1 / 1 2", "expected": "0:[1], 1:[0,2], 2:[1]", "is_hidden": False},
            {"input": "3 0", "expected": "0:[], 1:[], 2:[]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def create_graph(n, edges):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    char token[100];
    int n = 0, m = 0;
    if (scanf("%s", token) != 1) return 0;
    n = atoi(token);
    if (scanf("%s", token) != 1) return 0;
    m = atoi(token);

    int graph[105][105];
    int deg[105] = {0};

    for (int i = 0; i < m; i++) {
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int u = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int v = atoi(token);
        graph[u][deg[u]++] = v;
        graph[v][deg[v]++] = u;
    }

    for (int i = 0; i < n; i++) {
        qsort(graph[i], deg[i], sizeof(int), cmp);
        printf("%d:[", i);
        for (int j = 0; j < deg[i]; j++) {
            printf("%d%s", graph[i][j], (j == deg[i] - 1) ? "" : ",");
        }
        printf("]%s", (i == n - 1) ? "\\n" : ", ");
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string token;
    if (!(cin >> token)) return 0;
    int n = stoi(token);
    if (!(cin >> token)) return 0;
    int m = stoi(token);

    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        while (cin >> token && token == "/");
        int u = stoi(token);
        while (cin >> token && token == "/");
        int v = stoi(token);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i = 0; i < n; i++) {
        sort(graph[i].begin(), graph[i].end());
        cout << i << ":[";
        for (size_t j = 0; j < graph[i].size(); j++) {
            cout << graph[i][j] << (j == graph[i].size() - 1 ? "" : ",");
        }
        cout << "]" << (i == n - 1 ? "" : ", ");
    }
    cout << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.size() < 2) return;
        int n = Integer.parseInt(tokens.get(0));
        int m = Integer.parseInt(tokens.get(1));

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());

        int idx = 2;
        for (int i = 0; i < m; i++) {
            int u = Integer.parseInt(tokens.get(idx++));
            int v = Integer.parseInt(tokens.get(idx++));
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            Collections.sort(graph.get(i));
            sb.append(i).append(":[");
            for (int j = 0; j < graph.get(i).size(); j++) {
                sb.append(graph.get(i).get(j));
                if (j < graph.get(i).size() - 1) sb.append(",");
            }
            sb.append("]");
            if (i < n - 1) sb.append(", ");
        }
        System.out.println(sb.toString());
    }
}""",
            "python": """import sys

def create_graph(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        n = int(tokens[0])
        m = int(tokens[1])
        idx = 2
        edges = []
        for _ in range(m):
            edges.append((int(tokens[idx]), int(tokens[idx + 1])))
            idx += 2
        graph = create_graph(n, edges)
        res = []
        for i in range(n):
            res.append(f"{i}:[{','.join(map(str, sorted(graph[i])))}]")
        print(", ".join(res))"""
        })
    },

    # 2. Breadth First Search (BFS)
    {
        "id": "dsa-graph-bfs",
        "problem_num": 167,
        "title": "Breadth First Search (BFS)",
        "category": "Graphs",
        "topic": "Graph Traversal",
        "subtopic": "BFS",
        "difficulty": "EASY",
        "description": "Traverse a graph level by level starting from a given source node.",
        "input_format": "Number of vertices n and edges m, followed by m edges, then the start node.",
        "output_format": "List of visited vertices in BFS order.",
        "constraints": "1 <= n <= 100, 0 <= m <= 500, 0 <= start < n",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V)",
        "company_tags": ["Amazon", "Microsoft", "Facebook", "Google"],
        "examples": [
            {"input": "5 4 / 0 1 / 0 2 / 1 3 / 2 4 / 0", "output": "[0, 1, 2, 3, 4]", "explanation": "Starting at 0, visits neighbors 1, 2, then their neighbors 3, 4."},
            {"input": "4 3 / 0 1 / 1 2 / 2 3 / 0", "output": "[0, 1, 2, 3]", "explanation": "Linear chain BFS."},
            {"input": "3 1 / 0 1 / 0", "output": "[0, 1]", "explanation": "Only components connected to start node 0 are traversed."}
        ],
        "test_cases": [
            {"input": "5 4 / 0 1 / 0 2 / 1 3 / 2 4 / 0", "expected": "[0, 1, 2, 3, 4]", "is_hidden": False},
            {"input": "4 3 / 0 1 / 1 2 / 2 3 / 0", "expected": "[0, 1, 2, 3]", "is_hidden": False},
            {"input": "3 1 / 0 1 / 0", "expected": "[0, 1]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <queue>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def bfs(graph, start):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    char token[100];
    int n = 0, m = 0;
    if (scanf("%s", token) != 1) return 0;
    n = atoi(token);
    if (scanf("%s", token) != 1) return 0;
    m = atoi(token);

    int graph[105][105];
    int deg[105] = {0};

    for (int i = 0; i < m; i++) {
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int u = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int v = atoi(token);
        graph[u][deg[u]++] = v;
        graph[v][deg[v]++] = u;
    }

    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    int start = atoi(token);

    for (int i = 0; i < n; i++) {
        qsort(graph[i], deg[i], sizeof(int), cmp);
    }

    int visited[105] = {0};
    int q[105], front = 0, back = 0;
    int result[105], rcount = 0;

    visited[start] = 1;
    q[back++] = start;

    while (front < back) {
        int node = q[front++];
        result[rcount++] = node;

        for (int i = 0; i < deg[node]; i++) {
            int neighbor = graph[node][i];
            if (!visited[neighbor]) {
                visited[neighbor] = 1;
                q[back++] = neighbor;
            }
        }
    }

    printf("[");
    for (int i = 0; i < rcount; i++) {
        printf("%d%s", result[i], (i == rcount - 1) ? "" : ", ");
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string token;
    if (!(cin >> token)) return 0;
    int n = stoi(token);
    if (!(cin >> token)) return 0;
    int m = stoi(token);

    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        while (cin >> token && token == "/");
        int u = stoi(token);
        while (cin >> token && token == "/");
        int v = stoi(token);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    while (cin >> token && token == "/");
    int start = stoi(token);

    for (int i = 0; i < n; i++) {
        sort(graph[i].begin(), graph[i].end());
    }

    vector<bool> visited(n, false);
    queue<int> q;
    vector<int> result;

    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        result.push_back(node);

        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }

    cout << "[";
    for (size_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : ", ");
    }
    cout << "]" << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.size() < 3) return;
        int n = Integer.parseInt(tokens.get(0));
        int m = Integer.parseInt(tokens.get(1));

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());

        int idx = 2;
        for (int i = 0; i < m; i++) {
            int u = Integer.parseInt(tokens.get(idx++));
            int v = Integer.parseInt(tokens.get(idx++));
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        int start = Integer.parseInt(tokens.get(idx));

        for (int i = 0; i < n; i++) Collections.sort(graph.get(i));

        boolean[] visited = new boolean[n];
        Queue<Integer> q = new LinkedList<>();
        List<Integer> result = new ArrayList<>();

        visited[start] = true;
        q.offer(start);

        while (!q.isEmpty()) {
            int node = q.poll();
            result.add(node);

            for (int neighbor : graph.get(node)) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.offer(neighbor);
                }
            }
        }

        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < result.size(); i++) {
            sb.append(result.get(i));
            if (i < result.size() - 1) sb.append(", ");
        }
        sb.append("]");
        System.out.println(sb.toString());
    }
}""",
            "python": """import sys
from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])
    result = []
    visited.add(start)

    while q:
        node = q.popleft()
        result.append(node)

        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

    return result

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        n = int(tokens[0])
        m = int(tokens[1])
        graph = [[] for _ in range(n)]
        idx = 2
        for _ in range(m):
            u = int(tokens[idx])
            v = int(tokens[idx + 1])
            idx += 2
            graph[u].append(v)
            graph[v].append(u)
        start = int(tokens[idx])
        print(bfs(graph, start))"""
        })
    },

    # 3. Depth First Search (DFS)
    {
        "id": "dsa-graph-dfs",
        "problem_num": 168,
        "title": "Depth First Search (DFS)",
        "category": "Graphs",
        "topic": "Graph Traversal",
        "subtopic": "DFS",
        "difficulty": "EASY",
        "description": "Traverse a graph by exploring as deeply as possible before backtracking.",
        "input_format": "Number of vertices n and edges m, followed by m edges, then the start node.",
        "output_format": "List of visited vertices in DFS order.",
        "constraints": "1 <= n <= 100, 0 <= m <= 500, 0 <= start < n",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V)",
        "company_tags": ["Amazon", "Microsoft", "Google", "Bloomberg"],
        "examples": [
            {"input": "5 4 / 0 1 / 0 2 / 1 3 / 2 4 / 0", "output": "[0, 1, 3, 2, 4]", "explanation": "DFS explores down branch 0->1->3 before backtracking to 2->4."},
            {"input": "4 3 / 0 1 / 1 2 / 2 3 / 0", "output": "[0, 1, 2, 3]", "explanation": "Linear path traversal."},
            {"input": "3 1 / 0 1 / 0", "output": "[0, 1]", "explanation": "Traverses connected component from node 0."}
        ],
        "test_cases": [
            {"input": "5 4 / 0 1 / 0 2 / 1 3 / 2 4 / 0", "expected": "[0, 1, 3, 2, 4]", "is_hidden": False},
            {"input": "4 3 / 0 1 / 1 2 / 2 3 / 0", "expected": "[0, 1, 2, 3]", "is_hidden": False},
            {"input": "3 1 / 0 1 / 0", "expected": "[0, 1]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def dfs(graph, start):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int graph[105][105];
int deg[105];
int visited[105];
int result[105], rcount = 0;

void solve(int node) {
    visited[node] = 1;
    result[rcount++] = node;
    for (int i = 0; i < deg[node]; i++) {
        int neighbor = graph[node][i];
        if (!visited[neighbor]) {
            solve(neighbor);
        }
    }
}

int main() {
    char token[100];
    int n = 0, m = 0;
    if (scanf("%s", token) != 1) return 0;
    n = atoi(token);
    if (scanf("%s", token) != 1) return 0;
    m = atoi(token);

    for (int i = 0; i < m; i++) {
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int u = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int v = atoi(token);
        graph[u][deg[u]++] = v;
        graph[v][deg[v]++] = u;
    }

    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    int start = atoi(token);

    for (int i = 0; i < n; i++) {
        qsort(graph[i], deg[i], sizeof(int), cmp);
    }

    solve(start);

    printf("[");
    for (int i = 0; i < rcount; i++) {
        printf("%d%s", result[i], (i == rcount - 1) ? "" : ", ");
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void solve(int node, const vector<vector<int>>& graph, vector<bool>& visited, vector<int>& result) {
    visited[node] = true;
    result.push_back(node);
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            solve(neighbor, graph, visited, result);
        }
    }
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    int n = stoi(token);
    if (!(cin >> token)) return 0;
    int m = stoi(token);

    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        while (cin >> token && token == "/");
        int u = stoi(token);
        while (cin >> token && token == "/");
        int v = stoi(token);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    while (cin >> token && token == "/");
    int start = stoi(token);

    for (int i = 0; i < n; i++) {
        sort(graph[i].begin(), graph[i].end());
    }

    vector<bool> visited(n, false);
    vector<int> result;
    solve(start, graph, visited, result);

    cout << "[";
    for (size_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : ", ");
    }
    cout << "]" << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static void solve(int node, List<List<Integer>> graph, boolean[] visited, List<Integer> result) {
        visited[node] = true;
        result.add(node);
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                solve(neighbor, graph, visited, result);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.size() < 3) return;
        int n = Integer.parseInt(tokens.get(0));
        int m = Integer.parseInt(tokens.get(1));

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());

        int idx = 2;
        for (int i = 0; i < m; i++) {
            int u = Integer.parseInt(tokens.get(idx++));
            int v = Integer.parseInt(tokens.get(idx++));
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        int start = Integer.parseInt(tokens.get(idx));

        for (int i = 0; i < n; i++) Collections.sort(graph.get(i));

        boolean[] visited = new boolean[n];
        List<Integer> result = new ArrayList<>();
        solve(start, graph, visited, result);

        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < result.size(); i++) {
            sb.append(result.get(i));
            if (i < result.size() - 1) sb.append(", ");
        }
        sb.append("]");
        System.out.println(sb.toString());
    }
}""",
            "python": """import sys

def dfs(graph, start):
    visited = set()
    result = []

    def solve(node):
        visited.add(node)
        result.append(node)

        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                solve(neighbor)

    solve(start)
    return result

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        n = int(tokens[0])
        m = int(tokens[1])
        graph = [[] for _ in range(n)]
        idx = 2
        for _ in range(m):
            u = int(tokens[idx])
            v = int(tokens[idx + 1])
            idx += 2
            graph[u].append(v)
            graph[v].append(u)
        start = int(tokens[idx])
        print(dfs(graph, start))"""
        })
    },

    # 4. Number of Connected Components
    {
        "id": "dsa-graph-connected-components",
        "problem_num": 169,
        "title": "Number of Connected Components",
        "category": "Graphs",
        "topic": "Graph Connectivity",
        "subtopic": "Connected Components",
        "difficulty": "EASY",
        "description": "Find the number of disconnected components in an undirected graph.",
        "input_format": "Number of vertices n and edges m, followed by m edges.",
        "output_format": "Total number of connected components.",
        "constraints": "1 <= n <= 2000, 0 <= m <= 5000",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V + E)",
        "company_tags": ["Amazon", "Twitter", "Google", "LinkedIn"],
        "examples": [
            {"input": "5 3 / 0 1 / 1 2 / 3 4", "output": "2", "explanation": "Component 1: {0, 1, 2}, Component 2: {3, 4}."},
            {"input": "4 3 / 0 1 / 1 2 / 2 3", "output": "1", "explanation": "All nodes form a single component."},
            {"input": "4 0", "output": "4", "explanation": "Each vertex is isolated, so 4 components."}
        ],
        "test_cases": [
            {"input": "5 3 / 0 1 / 1 2 / 3 4", "expected": "2", "is_hidden": False},
            {"input": "4 3 / 0 1 / 1 2 / 2 3", "expected": "1", "is_hidden": False},
            {"input": "4 0", "expected": "4", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def count_components(n, graph):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int graph[2005][2005];
int deg[2005];
int visited[2005];

void dfs(int node) {
    visited[node] = 1;
    for (int i = 0; i < deg[node]; i++) {
        int neighbor = graph[node][i];
        if (!visited[neighbor]) {
            dfs(neighbor);
        }
    }
}

int main() {
    char token[100];
    int n = 0, m = 0;
    if (scanf("%s", token) != 1) return 0;
    n = atoi(token);
    if (scanf("%s", token) != 1) return 0;
    m = atoi(token);

    for (int i = 0; i < m; i++) {
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int u = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int v = atoi(token);
        graph[u][deg[u]++] = v;
        graph[v][deg[v]++] = u;
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            count++;
            dfs(i);
        }
    }

    printf("%d\\n", count);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

void dfs(int node, const vector<vector<int>>& graph, vector<bool>& visited) {
    visited[node] = true;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, graph, visited);
        }
    }
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    int n = stoi(token);
    if (!(cin >> token)) return 0;
    int m = stoi(token);

    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        while (cin >> token && token == "/");
        int u = stoi(token);
        while (cin >> token && token == "/");
        int v = stoi(token);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<bool> visited(n, false);
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            count++;
            dfs(i, graph, visited);
        }
    }

    cout << count << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static void dfs(int node, List<List<Integer>> graph, boolean[] visited) {
        visited[node] = true;
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                dfs(neighbor, graph, visited);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.size() < 2) return;
        int n = Integer.parseInt(tokens.get(0));
        int m = Integer.parseInt(tokens.get(1));

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());

        int idx = 2;
        for (int i = 0; i < m; i++) {
            int u = Integer.parseInt(tokens.get(idx++));
            int v = Integer.parseInt(tokens.get(idx++));
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        boolean[] visited = new boolean[n];
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                count++;
                dfs(i, graph, visited);
            }
        }

        System.out.println(count);
    }
}""",
            "python": """import sys

def count_components(n, graph):
    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for i in range(n):
        if i not in visited:
            count += 1
            dfs(i)

    return count

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        n = int(tokens[0])
        m = int(tokens[1])
        graph = [[] for _ in range(n)]
        idx = 2
        for _ in range(m):
            u = int(tokens[idx])
            v = int(tokens[idx + 1])
            idx += 2
            graph[u].append(v)
            graph[v].append(u)
        print(count_components(n, graph))"""
        })
    },

    # 5. Find a Path Between Two Nodes
    {
        "id": "dsa-graph-valid-path",
        "problem_num": 170,
        "title": "Find a Path Between Two Nodes",
        "category": "Graphs",
        "topic": "Graph Traversal",
        "subtopic": "Path Finding",
        "difficulty": "EASY",
        "description": "Check whether a path exists between two given vertices.",
        "input_format": "Number of vertices n and edges m, followed by m edges, then source and destination nodes.",
        "output_format": "True if a path exists, otherwise False.",
        "constraints": "1 <= n <= 2000, 0 <= m <= 5000, 0 <= source, destination < n",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V + E)",
        "company_tags": ["Amazon", "Facebook", "Microsoft"],
        "examples": [
            {"input": "3 2 / 0 1 / 1 2 / 0 2", "output": "True", "explanation": "Path exists: 0 -> 1 -> 2."},
            {"input": "6 4 / 0 1 / 1 2 / 3 4 / 4 5 / 0 5", "output": "False", "explanation": "Vertices 0 and 5 are in separate disconnected components."},
            {"input": "2 0 / 0 1", "output": "False", "explanation": "No edges exist between 0 and 1."}
        ],
        "test_cases": [
            {"input": "3 2 / 0 1 / 1 2 / 0 2", "expected": "True", "is_hidden": False},
            {"input": "6 4 / 0 1 / 1 2 / 3 4 / 4 5 / 0 5", "expected": "False", "is_hidden": False},
            {"input": "2 0 / 0 1", "expected": "False", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def valid_path(graph, source, destination):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int graph[2005][2005];
int deg[2005];
int visited[2005];
int stack[2005], top = -1;

int main() {
    char token[100];
    int n = 0, m = 0;
    if (scanf("%s", token) != 1) return 0;
    n = atoi(token);
    if (scanf("%s", token) != 1) return 0;
    m = atoi(token);

    for (int i = 0; i < m; i++) {
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int u = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int v = atoi(token);
        graph[u][deg[u]++] = v;
        graph[v][deg[v]++] = u;
    }

    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    int source = atoi(token);
    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    int destination = atoi(token);

    stack[++top] = source;
    int found = 0;

    while (top >= 0) {
        int node = stack[top--];
        if (node == destination) {
            found = 1;
            break;
        }
        if (visited[node]) continue;
        visited[node] = 1;

        for (int i = 0; i < deg[node]; i++) {
            int neighbor = graph[node][i];
            if (!visited[neighbor]) {
                stack[++top] = neighbor;
            }
        }
    }

    printf("%s\\n", found ? "True" : "False");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    string token;
    if (!(cin >> token)) return 0;
    int n = stoi(token);
    if (!(cin >> token)) return 0;
    int m = stoi(token);

    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        while (cin >> token && token == "/");
        int u = stoi(token);
        while (cin >> token && token == "/");
        int v = stoi(token);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    while (cin >> token && token == "/");
    int source = stoi(token);
    while (cin >> token && token == "/");
    int destination = stoi(token);

    vector<bool> visited(n, false);
    vector<int> stack;
    stack.push_back(source);
    bool found = false;

    while (!stack.empty()) {
        int node = stack.back();
        stack.pop_back();

        if (node == destination) {
            found = true;
            break;
        }

        if (visited[node]) continue;
        visited[node] = true;

        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                stack.push_back(neighbor);
            }
        }
    }

    cout << (found ? "True" : "False") << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.size() < 4) return;
        int n = Integer.parseInt(tokens.get(0));
        int m = Integer.parseInt(tokens.get(1));

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());

        int idx = 2;
        for (int i = 0; i < m; i++) {
            int u = Integer.parseInt(tokens.get(idx++));
            int v = Integer.parseInt(tokens.get(idx++));
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        int source = Integer.parseInt(tokens.get(idx++));
        int destination = Integer.parseInt(tokens.get(idx++));

        boolean[] visited = new boolean[n];
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(source);
        boolean found = false;

        while (!stack.isEmpty()) {
            int node = stack.pop();
            if (node == destination) {
                found = true;
                break;
            }
            if (visited[node]) continue;
            visited[node] = true;

            for (int neighbor : graph.get(node)) {
                if (!visited[neighbor]) {
                    stack.push(neighbor);
                }
            }
        }

        System.out.println(found ? "True" : "False");
    }
}""",
            "python": """import sys

def valid_path(graph, source, destination):
    visited = set()
    stack = [source]

    while stack:
        node = stack.pop()
        if node == destination:
            return True
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    return False

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        n = int(tokens[0])
        m = int(tokens[1])
        graph = [[] for _ in range(n)]
        idx = 2
        for _ in range(m):
            u = int(tokens[idx])
            v = int(tokens[idx + 1])
            idx += 2
            graph[u].append(v)
            graph[v].append(u)
        source = int(tokens[idx])
        destination = int(tokens[idx + 1])
        print(valid_path(graph, source, destination))"""
        })
    },

    # 6. Detect Cycle in an Undirected Graph
    {
        "id": "dsa-graph-undirected-cycle",
        "problem_num": 171,
        "title": "Detect Cycle in an Undirected Graph",
        "category": "Graphs",
        "topic": "Graph Cycles",
        "subtopic": "Cycle in Undirected Graph",
        "difficulty": "MEDIUM",
        "description": "Determine whether an undirected graph contains a cycle.",
        "input_format": "Number of vertices n and edges m, followed by m pairs of vertices representing edges.",
        "output_format": "True if a cycle exists, otherwise False.",
        "constraints": "1 <= n <= 2000, 0 <= m <= 5000",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V + E)",
        "company_tags": ["Amazon", "Microsoft", "Google"],
        "examples": [
            {"input": "3 3 / 0 1 / 1 2 / 2 0", "output": "True", "explanation": "Edges 0-1, 1-2, 2-0 form a triangle cycle."},
            {"input": "3 2 / 0 1 / 1 2", "output": "False", "explanation": "Simple tree structure has no cycle."},
            {"input": "4 4 / 0 1 / 1 2 / 2 3 / 3 0", "output": "True", "explanation": "4-cycle 0-1-2-3-0."}
        ],
        "test_cases": [
            {"input": "3 3 / 0 1 / 1 2 / 2 0", "expected": "True", "is_hidden": False},
            {"input": "3 2 / 0 1 / 1 2", "expected": "False", "is_hidden": False},
            {"input": "4 4 / 0 1 / 1 2 / 2 3 / 3 0", "expected": "True", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def has_cycle(n, graph):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int graph[2005][2005];
int deg[2005];
int visited[2005];

int dfs(int node, int parent) {
    visited[node] = 1;
    for (int i = 0; i < deg[node]; i++) {
        int neighbor = graph[node][i];
        if (!visited[neighbor]) {
            if (dfs(neighbor, node)) return 1;
        } else if (neighbor != parent) {
            return 1;
        }
    }
    return 0;
}

int main() {
    char token[100];
    int n = 0, m = 0;
    if (scanf("%s", token) != 1) return 0;
    n = atoi(token);
    if (scanf("%s", token) != 1) return 0;
    m = atoi(token);

    for (int i = 0; i < m; i++) {
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int u = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int v = atoi(token);
        graph[u][deg[u]++] = v;
        graph[v][deg[v]++] = u;
    }

    int cycle = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            if (dfs(i, -1)) {
                cycle = 1;
                break;
            }
        }
    }

    printf("%s\\n", cycle ? "True" : "False");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool dfs(int node, int parent, const vector<vector<int>>& graph, vector<bool>& visited) {
    visited[node] = true;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            if (dfs(neighbor, node, graph, visited)) return true;
        } else if (neighbor != parent) {
            return true;
        }
    }
    return false;
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    int n = stoi(token);
    if (!(cin >> token)) return 0;
    int m = stoi(token);

    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        while (cin >> token && token == "/");
        int u = stoi(token);
        while (cin >> token && token == "/");
        int v = stoi(token);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<bool> visited(n, false);
    bool cycle = false;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            if (dfs(i, -1, graph, visited)) {
                cycle = true;
                break;
            }
        }
    }

    cout << (cycle ? "True" : "False") << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static boolean dfs(int node, int parent, List<List<Integer>> graph, boolean[] visited) {
        visited[node] = true;
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                if (dfs(neighbor, node, graph, visited)) return true;
            } else if (neighbor != parent) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.size() < 2) return;
        int n = Integer.parseInt(tokens.get(0));
        int m = Integer.parseInt(tokens.get(1));

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());

        int idx = 2;
        for (int i = 0; i < m; i++) {
            int u = Integer.parseInt(tokens.get(idx++));
            int v = Integer.parseInt(tokens.get(idx++));
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        boolean[] visited = new boolean[n];
        boolean cycle = false;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                if (dfs(i, -1, graph, visited)) {
                    cycle = true;
                    break;
                }
            }
        }

        System.out.println(cycle ? "True" : "False");
    }
}""",
            "python": """import sys

def has_cycle(n, graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for i in range(n):
        if i not in visited:
            if dfs(i, -1):
                return True
    return False

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        n = int(tokens[0])
        m = int(tokens[1])
        graph = [[] for _ in range(n)]
        idx = 2
        for _ in range(m):
            u = int(tokens[idx])
            v = int(tokens[idx + 1])
            idx += 2
            graph[u].append(v)
            graph[v].append(u)
        print(has_cycle(n, graph))"""
        })
    },

    # 7. Detect Cycle in a Directed Graph
    {
        "id": "dsa-graph-directed-cycle",
        "problem_num": 172,
        "title": "Detect Cycle in a Directed Graph",
        "category": "Graphs",
        "topic": "Graph Cycles",
        "subtopic": "Cycle in Directed Graph",
        "difficulty": "MEDIUM",
        "description": "Determine whether a directed graph contains a cycle.",
        "input_format": "Number of vertices n and edges m, followed by m directed edges u -> v.",
        "output_format": "True if a cycle exists, otherwise False.",
        "constraints": "1 <= n <= 2000, 0 <= m <= 5000",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V + E)",
        "company_tags": ["Amazon", "Microsoft", "Google", "Facebook"],
        "examples": [
            {"input": "3 3 / 0 1 / 1 2 / 2 0", "output": "True", "explanation": "Directed cycle: 0 -> 1 -> 2 -> 0."},
            {"input": "3 2 / 0 1 / 1 2", "output": "False", "explanation": "Directed acyclic path: 0 -> 1 -> 2."},
            {"input": "4 4 / 0 1 / 1 2 / 2 3 / 3 1", "output": "True", "explanation": "Cycle among nodes 1, 2, 3."}
        ],
        "test_cases": [
            {"input": "3 3 / 0 1 / 1 2 / 2 0", "expected": "True", "is_hidden": False},
            {"input": "3 2 / 0 1 / 1 2", "expected": "False", "is_hidden": False},
            {"input": "4 4 / 0 1 / 1 2 / 2 3 / 3 1", "expected": "True", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def has_cycle(n, graph):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int graph[2005][2005];
int deg[2005];
int visited[2005];
int path[2005];

int dfs(int node) {
    visited[node] = 1;
    path[node] = 1;

    for (int i = 0; i < deg[node]; i++) {
        int neighbor = graph[node][i];
        if (!visited[neighbor]) {
            if (dfs(neighbor)) return 1;
        } else if (path[neighbor]) {
            return 1;
        }
    }

    path[node] = 0;
    return 0;
}

int main() {
    char token[100];
    int n = 0, m = 0;
    if (scanf("%s", token) != 1) return 0;
    n = atoi(token);
    if (scanf("%s", token) != 1) return 0;
    m = atoi(token);

    for (int i = 0; i < m; i++) {
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int u = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int v = atoi(token);
        graph[u][deg[u]++] = v;
    }

    int cycle = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            if (dfs(i)) {
                cycle = 1;
                break;
            }
        }
    }

    printf("%s\\n", cycle ? "True" : "False");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool dfs(int node, const vector<vector<int>>& graph, vector<bool>& visited, vector<bool>& path) {
    visited[node] = true;
    path[node] = true;

    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            if (dfs(neighbor, graph, visited, path)) return true;
        } else if (path[neighbor]) {
            return true;
        }
    }

    path[node] = false;
    return false;
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    int n = stoi(token);
    if (!(cin >> token)) return 0;
    int m = stoi(token);

    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        while (cin >> token && token == "/");
        int u = stoi(token);
        while (cin >> token && token == "/");
        int v = stoi(token);
        graph[u].push_back(v);
    }

    vector<bool> visited(n, false);
    vector<bool> path(n, false);
    bool cycle = false;

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            if (dfs(i, graph, visited, path)) {
                cycle = true;
                break;
            }
        }
    }

    cout << (cycle ? "True" : "False") << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static boolean dfs(int node, List<List<Integer>> graph, boolean[] visited, boolean[] path) {
        visited[node] = true;
        path[node] = true;

        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                if (dfs(neighbor, graph, visited, path)) return true;
            } else if (path[neighbor]) {
                return true;
            }
        }

        path[node] = false;
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.size() < 2) return;
        int n = Integer.parseInt(tokens.get(0));
        int m = Integer.parseInt(tokens.get(1));

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());

        int idx = 2;
        for (int i = 0; i < m; i++) {
            int u = Integer.parseInt(tokens.get(idx++));
            int v = Integer.parseInt(tokens.get(idx++));
            graph.get(u).add(v);
        }

        boolean[] visited = new boolean[n];
        boolean[] path = new boolean[n];
        boolean cycle = false;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                if (dfs(i, graph, visited, path)) {
                    cycle = true;
                    break;
                }
            }
        }

        System.out.println(cycle ? "True" : "False");
    }
}""",
            "python": """import sys

def has_cycle(n, graph):
    visited = [False] * n
    path = [False] * n

    def dfs(node):
        visited[node] = True
        path[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif path[neighbor]:
                return True

        path[node] = False
        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i):
                return True

    return False

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        n = int(tokens[0])
        m = int(tokens[1])
        graph = [[] for _ in range(n)]
        idx = 2
        for _ in range(m):
            u = int(tokens[idx])
            v = int(tokens[idx + 1])
            idx += 2
            graph[u].append(v)
        print(has_cycle(n, graph))"""
        })
    },

    # 8. Topological Sorting
    {
        "id": "dsa-graph-topological-sort",
        "problem_num": 173,
        "title": "Topological Sorting",
        "category": "Graphs",
        "topic": "Topological Sort",
        "subtopic": "Kahn's Algorithm",
        "difficulty": "MEDIUM",
        "description": "Arrange vertices of a directed acyclic graph so that every directed edge u -> v places u before v. Return empty array if a cycle exists.",
        "input_format": "Number of vertices n and edges m, followed by m directed edges.",
        "output_format": "List of vertices in topological sort order, or empty list if cyclic.",
        "constraints": "1 <= n <= 2000, 0 <= m <= 5000",
        "time_complexity": "O(V + E log E)",
        "space_complexity": "O(V + E)",
        "company_tags": ["Amazon", "Microsoft", "Google", "Facebook", "Uber"],
        "examples": [
            {"input": "4 3 / 0 1 / 0 2 / 1 3", "output": "[0, 1, 2, 3]", "explanation": "Valid linear ordering respecting dependencies."},
            {"input": "3 2 / 0 1 / 1 2", "output": "[0, 1, 2]", "explanation": "Simple chain 0 -> 1 -> 2."},
            {"input": "3 3 / 0 1 / 1 2 / 2 0", "output": "[]", "explanation": "Graph contains a cycle, no topological ordering exists."}
        ],
        "test_cases": [
            {"input": "4 3 / 0 1 / 0 2 / 1 3", "expected": "[0, 1, 2, 3]", "is_hidden": False},
            {"input": "3 2 / 0 1 / 1 2", "expected": "[0, 1, 2]", "is_hidden": False},
            {"input": "3 3 / 0 1 / 1 2 / 2 0", "expected": "[]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <queue>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def topological_sort(n, graph):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int graph[2005][2005];
int deg[2005] = {0};
int indegree[2005] = {0};
int q[2005];
int result[2005];

int main() {
    char token[100];
    int n = 0, m = 0;
    if (scanf("%s", token) != 1) return 0;
    n = atoi(token);
    if (scanf("%s", token) != 1) return 0;
    m = atoi(token);

    for (int i = 0; i < m; i++) {
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int u = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int v = atoi(token);
        graph[u][deg[u]++] = v;
        indegree[v]++;
    }

    for (int i = 0; i < n; i++) {
        qsort(graph[i], deg[i], sizeof(int), cmp);
    }

    int front = 0, back = 0;
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) q[back++] = i;
    }

    int rcount = 0;
    while (front < back) {
        int node = q[front++];
        result[rcount++] = node;

        for (int i = 0; i < deg[node]; i++) {
            int neighbor = graph[node][i];
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                q[back++] = neighbor;
            }
        }
    }

    if (rcount != n) {
        printf("[]\\n");
    } else {
        printf("[");
        for (int i = 0; i < rcount; i++) {
            printf("%d%s", result[i], (i == rcount - 1) ? "" : ", ");
        }
        printf("]\\n");
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string token;
    if (!(cin >> token)) return 0;
    int n = stoi(token);
    if (!(cin >> token)) return 0;
    int m = stoi(token);

    vector<vector<int>> graph(n);
    vector<int> indegree(n, 0);

    for (int i = 0; i < m; i++) {
        while (cin >> token && token == "/");
        int u = stoi(token);
        while (cin >> token && token == "/");
        int v = stoi(token);
        graph[u].push_back(v);
        indegree[v]++;
    }

    for (int i = 0; i < n; i++) {
        sort(graph[i].begin(), graph[i].end());
    }

    queue<int> q;
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) q.push(i);
    }

    vector<int> result;
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        result.push_back(node);

        for (int neighbor : graph[node]) {
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }

    if ((int)result.size() != n) {
        cout << "[]" << endl;
    } else {
        cout << "[";
        for (size_t i = 0; i < result.size(); i++) {
            cout << result[i] << (i == result.size() - 1 ? "" : ", ");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.size() < 2) return;
        int n = Integer.parseInt(tokens.get(0));
        int m = Integer.parseInt(tokens.get(1));

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        int[] indegree = new int[n];

        int idx = 2;
        for (int i = 0; i < m; i++) {
            int u = Integer.parseInt(tokens.get(idx++));
            int v = Integer.parseInt(tokens.get(idx++));
            graph.get(u).add(v);
            indegree[v]++;
        }

        for (int i = 0; i < n; i++) Collections.sort(graph.get(i));

        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) q.offer(i);
        }

        List<Integer> result = new ArrayList<>();
        while (!q.isEmpty()) {
            int node = q.poll();
            result.add(node);

            for (int neighbor : graph.get(node)) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.offer(neighbor);
                }
            }
        }

        if (result.size() != n) {
            System.out.println("[]");
        } else {
            StringBuilder sb = new StringBuilder("[");
            for (int i = 0; i < result.size(); i++) {
                sb.append(result.get(i));
                if (i < result.size() - 1) sb.append(", ");
            }
            sb.append("]");
            System.out.println(sb.toString());
        }
    }
}""",
            "python": """import sys
from collections import deque

def topological_sort(n, graph):
    indegree = [0] * n

    for u in range(n):
        for v in graph[u]:
            indegree[v] += 1

    q = deque(i for i in range(n) if indegree[i] == 0)
    result = []

    while q:
        node = q.popleft()
        result.append(node)

        for neighbor in sorted(graph[node]):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return result if len(result) == n else []

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        n = int(tokens[0])
        m = int(tokens[1])
        graph = [[] for _ in range(n)]
        idx = 2
        for _ in range(m):
            u = int(tokens[idx])
            v = int(tokens[idx + 1])
            idx += 2
            graph[u].append(v)
        print(topological_sort(n, graph))"""
        })
    },

    # 9. Shortest Path in an Unweighted Graph
    {
        "id": "dsa-graph-shortest-path-unweighted",
        "problem_num": 174,
        "title": "Shortest Path in an Unweighted Graph",
        "category": "Graphs",
        "topic": "Shortest Path",
        "subtopic": "BFS Shortest Path",
        "difficulty": "MEDIUM",
        "description": "Find the shortest distance between a source and destination in an unweighted graph.",
        "input_format": "Number of vertices n and edges m, followed by m edges, then source and destination.",
        "output_format": "Shortest path distance, or -1 if unreachable.",
        "constraints": "1 <= n <= 2000, 0 <= m <= 5000",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V + E)",
        "company_tags": ["Amazon", "Google", "Facebook", "Microsoft"],
        "examples": [
            {"input": "5 5 / 0 1 / 0 2 / 1 3 / 2 3 / 3 4 / 0 4", "output": "3", "explanation": "Shortest path: 0 -> 1 -> 3 -> 4 has 3 edges."},
            {"input": "4 2 / 0 1 / 2 3 / 0 3", "output": "-1", "explanation": "Destination 3 cannot be reached from source 0."},
            {"input": "3 2 / 0 1 / 1 2 / 1 1", "output": "0", "explanation": "Source and destination are the same node."}
        ],
        "test_cases": [
            {"input": "5 5 / 0 1 / 0 2 / 1 3 / 2 3 / 3 4 / 0 4", "expected": "3", "is_hidden": False},
            {"input": "4 2 / 0 1 / 2 3 / 0 3", "expected": "-1", "is_hidden": False},
            {"input": "3 2 / 0 1 / 1 2 / 1 1", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <queue>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def shortest_path(n, graph, source, destination):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int graph[2005][2005];
int deg[2005];
int dist[2005];
int q[2005];

int main() {
    char token[100];
    int n = 0, m = 0;
    if (scanf("%s", token) != 1) return 0;
    n = atoi(token);
    if (scanf("%s", token) != 1) return 0;
    m = atoi(token);

    for (int i = 0; i < m; i++) {
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int u = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int v = atoi(token);
        graph[u][deg[u]++] = v;
        graph[v][deg[v]++] = u;
    }

    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    int source = atoi(token);
    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    int destination = atoi(token);

    for (int i = 0; i < n; i++) dist[i] = -1;

    int front = 0, back = 0;
    q[back++] = source;
    dist[source] = 0;

    while (front < back) {
        int node = q[front++];

        for (int i = 0; i < deg[node]; i++) {
            int neighbor = graph[node][i];
            if (dist[neighbor] == -1) {
                dist[neighbor] = dist[node] + 1;
                q[back++] = neighbor;
            }
        }
    }

    printf("%d\\n", dist[destination]);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int main() {
    string token;
    if (!(cin >> token)) return 0;
    int n = stoi(token);
    if (!(cin >> token)) return 0;
    int m = stoi(token);

    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        while (cin >> token && token == "/");
        int u = stoi(token);
        while (cin >> token && token == "/");
        int v = stoi(token);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    while (cin >> token && token == "/");
    int source = stoi(token);
    while (cin >> token && token == "/");
    int destination = stoi(token);

    vector<int> distance(n, -1);
    queue<int> q;
    q.push(source);
    distance[source] = 0;

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        for (int neighbor : graph[node]) {
            if (distance[neighbor] == -1) {
                distance[neighbor] = distance[node] + 1;
                q.push(neighbor);
            }
        }
    }

    cout << distance[destination] << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.size() < 4) return;
        int n = Integer.parseInt(tokens.get(0));
        int m = Integer.parseInt(tokens.get(1));

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());

        int idx = 2;
        for (int i = 0; i < m; i++) {
            int u = Integer.parseInt(tokens.get(idx++));
            int v = Integer.parseInt(tokens.get(idx++));
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        int source = Integer.parseInt(tokens.get(idx++));
        int destination = Integer.parseInt(tokens.get(idx++));

        int[] distance = new int[n];
        Arrays.fill(distance, -1);
        Queue<Integer> q = new LinkedList<>();
        q.offer(source);
        distance[source] = 0;

        while (!q.isEmpty()) {
            int node = q.poll();

            for (int neighbor : graph.get(node)) {
                if (distance[neighbor] == -1) {
                    distance[neighbor] = distance[node] + 1;
                    q.offer(neighbor);
                }
            }
        }

        System.out.println(distance[destination]);
    }
}""",
            "python": """import sys
from collections import deque

def shortest_path(n, graph, source, destination):
    distance = [-1] * n
    q = deque([source])
    distance[source] = 0

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + 1
                q.append(neighbor)

    return distance[destination]

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        n = int(tokens[0])
        m = int(tokens[1])
        graph = [[] for _ in range(n)]
        idx = 2
        for _ in range(m):
            u = int(tokens[idx])
            v = int(tokens[idx + 1])
            idx += 2
            graph[u].append(v)
            graph[v].append(u)
        source = int(tokens[idx])
        destination = int(tokens[idx + 1])
        print(shortest_path(n, graph, source, destination))"""
        })
    },

    # 10. Number of Islands
    {
        "id": "dsa-graph-number-of-islands",
        "problem_num": 175,
        "title": "Number of Islands",
        "category": "Graphs",
        "topic": "Grid Graphs",
        "subtopic": "Connected Components in Grid",
        "difficulty": "MEDIUM",
        "description": "Count the number of connected groups of land (1) in a grid of land (1) and water (0). Only horizontal and vertical connections count.",
        "input_format": "Number of rows and cols, followed by each row string of 0s and 1s.",
        "output_format": "Number of distinct islands.",
        "constraints": "1 <= rows, cols <= 300",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(M * N)",
        "company_tags": ["Amazon", "Microsoft", "Bloomberg", "Facebook", "Google"],
        "examples": [
            {"input": "4 5 / 11000 / 11000 / 00100 / 00011", "output": "3", "explanation": "Three separate islands of 1s."},
            {"input": "1 3 / 111", "output": "1", "explanation": "One single island of length 3."},
            {"input": "2 2 / 00 / 00", "output": "0", "explanation": "No land cells present."}
        ],
        "test_cases": [
            {"input": "4 5 / 11000 / 11000 / 00100 / 00011", "expected": "3", "is_hidden": False},
            {"input": "1 3 / 111", "expected": "1", "is_hidden": False},
            {"input": "2 2 / 00 / 00", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def num_islands(grid):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char grid[305][305];
int rows, cols;

void dfs(int r, int c) {
    if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] != '1') return;
    grid[r][c] = '0';
    dfs(r + 1, c);
    dfs(r - 1, c);
    dfs(r, c + 1);
    dfs(r, c - 1);
}

int main() {
    char token[305];
    if (scanf("%s", token) != 1) return 0;
    rows = atoi(token);
    if (scanf("%s", token) != 1) return 0;
    cols = atoi(token);

    for (int i = 0; i < rows; i++) {
        while (scanf("%s", grid[i]) == 1 && strcmp(grid[i], "/") == 0);
    }

    int count = 0;
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (grid[r][c] == '1') {
                count++;
                dfs(r, c);
            }
        }
    }

    printf("%d\\n", count);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

void dfs(int r, int c, vector<string>& grid, int rows, int cols) {
    if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] != '1') return;
    grid[r][c] = '0';
    dfs(r + 1, c, grid, rows, cols);
    dfs(r - 1, c, grid, rows, cols);
    dfs(r, c + 1, grid, rows, cols);
    dfs(r, c - 1, grid, rows, cols);
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    int rows = stoi(token);
    if (!(cin >> token)) return 0;
    int cols = stoi(token);

    vector<string> grid(rows);
    for (int i = 0; i < rows; i++) {
        while (cin >> grid[i] && grid[i] == "/");
    }

    int count = 0;
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (grid[r][c] == '1') {
                count++;
                dfs(r, c, grid, rows, cols);
            }
        }
    }

    cout << count << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static void dfs(int r, int c, char[][] grid, int rows, int cols) {
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] != '1') return;
        grid[r][c] = '0';
        dfs(r + 1, c, grid, rows, cols);
        dfs(r - 1, c, grid, rows, cols);
        dfs(r, c + 1, grid, rows, cols);
        dfs(r, c - 1, grid, rows, cols);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.size() < 2) return;
        int rows = Integer.parseInt(tokens.get(0));
        int cols = Integer.parseInt(tokens.get(1));

        char[][] grid = new char[rows][cols];
        for (int i = 0; i < rows; i++) {
            grid[i] = tokens.get(2 + i).toCharArray();
        }

        int count = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    count++;
                    dfs(r, c, grid, rows, cols);
                }
            }
        }

        System.out.println(count);
    }
}""",
            "python": """import sys

def num_islands(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(r, c):
        if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0'):
            return
        grid[r][c] = '0'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        rows = int(tokens[0])
        cols = int(tokens[1])
        grid = [list(tokens[2 + i]) for i in range(rows)]
        print(num_islands(grid))"""
        })
    },

    # 11. Dijkstra's Shortest Path
    {
        "id": "dsa-graph-dijkstra",
        "problem_num": 176,
        "title": "Dijkstra's Shortest Path",
        "category": "Graphs",
        "topic": "Shortest Path",
        "subtopic": "Dijkstra Algorithm",
        "difficulty": "HARD",
        "description": "Find the shortest distance from a source node to every other node in a weighted graph with non-negative edge weights.",
        "input_format": "Number of vertices n and edges m, followed by m triples (u, v, w), then source node.",
        "output_format": "List of shortest distances to all vertices, or -1 if unreachable.",
        "constraints": "1 <= n <= 1000, 0 <= m <= 5000, 0 <= weight <= 10^5",
        "time_complexity": "O((V + E) log V)",
        "space_complexity": "O(V + E)",
        "company_tags": ["Google", "Amazon", "Microsoft", "Uber"],
        "examples": [
            {"input": "5 6 / 0 1 2 / 0 2 4 / 1 2 1 / 1 3 7 / 2 4 3 / 3 4 1 / 0", "output": "[0, 2, 3, 7, 6]", "explanation": "Shortest paths from 0: dist to 1 is 2, to 2 is 3, to 4 is 6, to 3 is 8."},
            {"input": "3 2 / 0 1 5 / 1 2 3 / 0", "output": "[0, 5, 8]", "explanation": "Linear path with distances 0, 5, 8."},
            {"input": "4 2 / 0 1 2 / 2 3 4 / 0", "output": "[0, 2, -1, -1]", "explanation": "Nodes 2 and 3 are unreachable from source 0."}
        ],
        "test_cases": [
            {"input": "5 6 / 0 1 2 / 0 2 4 / 1 2 1 / 1 3 7 / 2 4 3 / 3 4 1 / 0", "expected": "[0, 2, 3, 7, 6]", "is_hidden": False},
            {"input": "3 2 / 0 1 5 / 1 2 3 / 0", "expected": "[0, 5, 8]", "is_hidden": False},
            {"input": "4 2 / 0 1 2 / 2 3 4 / 0", "expected": "[0, 2, -1, -1]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <queue>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def dijkstra(n, graph, source):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INF 1000000000

typedef struct {
    int v;
    int w;
} Edge;

Edge graph[1005][1005];
int deg[1005];
int dist[1005];
int visited[1005];

int main() {
    char token[100];
    int n = 0, m = 0;
    if (scanf("%s", token) != 1) return 0;
    n = atoi(token);
    if (scanf("%s", token) != 1) return 0;
    m = atoi(token);

    for (int i = 0; i < m; i++) {
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int u = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int v = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        int w = atoi(token);
        graph[u][deg[u]].v = v;
        graph[u][deg[u]++].w = w;
        graph[v][deg[v]].v = u;
        graph[v][deg[v]++].w = w;
    }

    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    int source = atoi(token);

    for (int i = 0; i < n; i++) dist[i] = INF;
    dist[source] = 0;

    for (int i = 0; i < n; i++) {
        int u = -1, min_d = INF;
        for (int j = 0; j < n; j++) {
            if (!visited[j] && dist[j] < min_d) {
                min_d = dist[j];
                u = j;
            }
        }
        if (u == -1) break;
        visited[u] = 1;

        for (int j = 0; j < deg[u]; j++) {
            int v = graph[u][j].v;
            int w = graph[u][j].w;
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    printf("[");
    for (int i = 0; i < n; i++) {
        int d = (dist[i] == INF) ? -1 : dist[i];
        printf("%d%s", d, (i == n - 1) ? "" : ", ");
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

const long long INF = 1e18;

int main() {
    string token;
    if (!(cin >> token)) return 0;
    int n = stoi(token);
    if (!(cin >> token)) return 0;
    int m = stoi(token);

    vector<vector<pair<int, int>>> graph(n);
    for (int i = 0; i < m; i++) {
        while (cin >> token && token == "/");
        int u = stoi(token);
        while (cin >> token && token == "/");
        int v = stoi(token);
        while (cin >> token && token == "/");
        int w = stoi(token);
        graph[u].push_back({v, w});
        graph[v].push_back({u, w});
    }

    while (cin >> token && token == "/");
    int source = stoi(token);

    vector<long long> dist(n, INF);
    dist[source] = 0;

    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    pq.push({0, source});

    while (!pq.empty()) {
        auto top = pq.top();
        pq.pop();
        long long distance = top.first;
        int node = top.second;

        if (distance > dist[node]) continue;

        for (auto& edge : graph[node]) {
            int neighbor = edge.first;
            int weight = edge.second;
            long long new_distance = distance + weight;

            if (new_distance < dist[neighbor]) {
                dist[neighbor] = new_distance;
                pq.push({new_distance, neighbor});
            }
        }
    }

    cout << "[";
    for (int i = 0; i < n; i++) {
        long long d = (dist[i] == INF) ? -1 : dist[i];
        cout << d << (i == n - 1 ? "" : ", ");
    }
    cout << "]" << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Edge {
        int to;
        long weight;
        Edge(int to, long weight) { this.to = to; this.weight = weight; }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.size() < 3) return;
        int n = Integer.parseInt(tokens.get(0));
        int m = Integer.parseInt(tokens.get(1));

        List<List<Edge>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());

        int idx = 2;
        for (int i = 0; i < m; i++) {
            int u = Integer.parseInt(tokens.get(idx++));
            int v = Integer.parseInt(tokens.get(idx++));
            long w = Long.parseLong(tokens.get(idx++));
            graph.get(u).add(new Edge(v, w));
            graph.get(v).add(new Edge(u, w));
        }
        int source = Integer.parseInt(tokens.get(idx));

        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[source] = 0;

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.offer(new long[]{0, source});

        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            long distance = curr[0];
            int node = (int) curr[1];

            if (distance > dist[node]) continue;

            for (Edge e : graph.get(node)) {
                long newDist = distance + e.weight;
                if (newDist < dist[e.to]) {
                    dist[e.to] = newDist;
                    pq.offer(new long[]{newDist, e.to});
                }
            }
        }

        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < n; i++) {
            long d = (dist[i] == Long.MAX_VALUE) ? -1 : dist[i];
            sb.append(d);
            if (i < n - 1) sb.append(", ");
        }
        sb.append("]");
        System.out.println(sb.toString());
    }
}""",
            "python": """import sys
import heapq

def dijkstra(n, graph, source):
    dist = [float('inf')] * n
    dist[source] = 0
    heap = [(0, source)]

    while heap:
        distance, node = heapq.heappop(heap)
        if distance > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_distance = distance + weight
            if new_distance < dist[neighbor]:
                dist[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return [-1 if x == float('inf') else x for x in dist]

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        n = int(tokens[0])
        m = int(tokens[1])
        graph = [[] for _ in range(n)]
        idx = 2
        for _ in range(m):
            u = int(tokens[idx])
            v = int(tokens[idx + 1])
            w = int(tokens[idx + 2])
            idx += 3
            graph[u].append((v, w))
            graph[v].append((u, w))
        source = int(tokens[idx])
        print(dijkstra(n, graph, source))"""
        })
    },

    # 12. Bellman-Ford Algorithm
    {
        "id": "dsa-graph-bellman-ford",
        "problem_num": 177,
        "title": "Bellman-Ford Algorithm",
        "category": "Graphs",
        "topic": "Shortest Path",
        "subtopic": "Bellman-Ford Algorithm",
        "difficulty": "HARD",
        "description": "Find shortest paths from a source vertex, even when some edges have negative weights. Detect reachable negative-weight cycles.",
        "input_format": "Number of vertices n and edges m, followed by m directed edges (u, v, w), then source node.",
        "output_format": "'Negative cycle' if a negative cycle is detected, otherwise list of shortest distances.",
        "constraints": "1 <= n <= 500, 0 <= m <= 2000, -10^4 <= weight <= 10^4",
        "time_complexity": "O(V * E)",
        "space_complexity": "O(V + E)",
        "company_tags": ["Amazon", "Microsoft", "Google"],
        "examples": [
            {"input": "5 8 / 0 1 -1 / 0 2 4 / 1 2 3 / 1 3 2 / 1 4 2 / 3 2 5 / 3 1 1 / 4 3 -3 / 0", "output": "[0, -1, 2, -2, 1]", "explanation": "Computes shortest paths correctly with negative weights."},
            {"input": "3 3 / 0 1 1 / 1 2 -2 / 2 1 1 / 0", "output": "Negative cycle", "explanation": "Cycle 1 -> 2 -> 1 has negative sum -1, creating unbounded distance decrease."},
            {"input": "3 1 / 0 1 5 / 0", "output": "[0, 5, -1]", "explanation": "Node 2 is unreachable from source 0."}
        ],
        "test_cases": [
            {"input": "5 8 / 0 1 -1 / 0 2 4 / 1 2 3 / 1 3 2 / 1 4 2 / 3 2 5 / 3 1 1 / 4 3 -3 / 0", "expected": "[0, -1, 2, -2, 1]", "is_hidden": False},
            {"input": "3 3 / 0 1 1 / 1 2 -2 / 2 1 1 / 0", "expected": "Negative cycle", "is_hidden": False},
            {"input": "3 1 / 0 1 5 / 0", "expected": "[0, 5, -1]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def bellman_ford(n, edges, source):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INF 1000000000

typedef struct {
    int u, v, w;
} Edge;

int main() {
    char token[100];
    int n = 0, m = 0;
    if (scanf("%s", token) != 1) return 0;
    n = atoi(token);
    if (scanf("%s", token) != 1) return 0;
    m = atoi(token);

    Edge edges[2005];
    for (int i = 0; i < m; i++) {
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        edges[i].u = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        edges[i].v = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        edges[i].w = atoi(token);
    }

    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    int source = atoi(token);

    int dist[505];
    for (int i = 0; i < n; i++) dist[i] = INF;
    dist[source] = 0;

    for (int i = 0; i < n - 1; i++) {
        int changed = 0;
        for (int j = 0; j < m; j++) {
            int u = edges[j].u;
            int v = edges[j].v;
            int w = edges[j].w;
            if (dist[u] != INF && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                changed = 1;
            }
        }
        if (!changed) break;
    }

    for (int j = 0; j < m; j++) {
        int u = edges[j].u;
        int v = edges[j].v;
        int w = edges[j].w;
        if (dist[u] != INF && dist[u] + w < dist[v]) {
            printf("Negative cycle\\n");
            return 0;
        }
    }

    printf("[");
    for (int i = 0; i < n; i++) {
        int d = (dist[i] == INF) ? -1 : dist[i];
        printf("%d%s", d, (i == n - 1) ? "" : ", ");
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int u, v, w;
};

int main() {
    string token;
    if (!(cin >> token)) return 0;
    int n = stoi(token);
    if (!(cin >> token)) return 0;
    int m = stoi(token);

    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        while (cin >> token && token == "/");
        edges[i].u = stoi(token);
        while (cin >> token && token == "/");
        edges[i].v = stoi(token);
        while (cin >> token && token == "/");
        edges[i].w = stoi(token);
    }

    while (cin >> token && token == "/");
    int source = stoi(token);

    vector<long long> dist(n, INF);
    dist[source] = 0;

    for (int i = 0; i < n - 1; i++) {
        bool changed = false;
        for (const auto& e : edges) {
            if (dist[e.u] != INF && dist[e.u] + e.w < dist[e.v]) {
                dist[e.v] = dist[e.u] + e.w;
                changed = true;
            }
        }
        if (!changed) break;
    }

    for (const auto& e : edges) {
        if (dist[e.u] != INF && dist[e.u] + e.w < dist[e.v]) {
            cout << "Negative cycle" << endl;
            return 0;
        }
    }

    cout << "[";
    for (int i = 0; i < n; i++) {
        long long d = (dist[i] == INF) ? -1 : dist[i];
        cout << d << (i == n - 1 ? "" : ", ");
    }
    cout << "]" << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Edge {
        int u, v, w;
        Edge(int u, int v, int w) { this.u = u; this.v = v; this.w = w; }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.size() < 3) return;
        int n = Integer.parseInt(tokens.get(0));
        int m = Integer.parseInt(tokens.get(1));

        List<Edge> edges = new ArrayList<>();
        int idx = 2;
        for (int i = 0; i < m; i++) {
            int u = Integer.parseInt(tokens.get(idx++));
            int v = Integer.parseInt(tokens.get(idx++));
            int w = Integer.parseInt(tokens.get(idx++));
            edges.add(new Edge(u, v, w));
        }
        int source = Integer.parseInt(tokens.get(idx));

        long INF = Long.MAX_VALUE / 2;
        long[] dist = new long[n];
        Arrays.fill(dist, INF);
        dist[source] = 0;

        for (int i = 0; i < n - 1; i++) {
            boolean changed = false;
            for (Edge e : edges) {
                if (dist[e.u] != INF && dist[e.u] + e.w < dist[e.v]) {
                    dist[e.v] = dist[e.u] + e.w;
                    changed = true;
                }
            }
            if (!changed) break;
        }

        for (Edge e : edges) {
            if (dist[e.u] != INF && dist[e.u] + e.w < dist[e.v]) {
                System.out.println("Negative cycle");
                return;
            }
        }

        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < n; i++) {
            long d = (dist[i] >= INF) ? -1 : dist[i];
            sb.append(d);
            if (i < n - 1) sb.append(", ");
        }
        sb.append("]");
        System.out.println(sb.toString());
    }
}""",
            "python": """import sys

def bellman_ford(n, edges, source):
    dist = [float('inf')] * n
    dist[source] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break

    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return "Negative cycle"

    return [-1 if x == float('inf') else x for x in dist]

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        n = int(tokens[0])
        m = int(tokens[1])
        edges = []
        idx = 2
        for _ in range(m):
            edges.append((int(tokens[idx]), int(tokens[idx + 1]), int(tokens[idx + 2])))
            idx += 3
        source = int(tokens[idx])
        print(bellman_ford(n, edges, source))"""
        })
    },

    # 13. Floyd-Warshall Algorithm
    {
        "id": "dsa-graph-floyd-warshall",
        "problem_num": 178,
        "title": "Floyd-Warshall Algorithm",
        "category": "Graphs",
        "topic": "All-Pairs Shortest Path",
        "subtopic": "Floyd-Warshall Algorithm",
        "difficulty": "HARD",
        "description": "Find the shortest distances between every pair of vertices in a weighted directed graph. Use 99999 to represent no direct edge.",
        "input_format": "Number of vertices n followed by the n x n distance matrix.",
        "output_format": "The all-pairs shortest distance matrix.",
        "constraints": "1 <= n <= 100, -1000 <= weight <= 1000, 99999 for infinity",
        "time_complexity": "O(V^3)",
        "space_complexity": "O(V^2)",
        "company_tags": ["Amazon", "Google", "Microsoft"],
        "examples": [
            {"input": "3 / 0 4 99999 / 99999 0 2 / 3 99999 0", "output": "0 4 6\n5 0 2\n3 7 0", "explanation": "Calculates shortest distances between all pairs of nodes."},
            {"input": "2 / 0 5 / 99999 0", "output": "0 5\n99999 0", "explanation": "Direct edge from 0 to 1, no return path."},
            {"input": "2 / 0 -2 / 99999 0", "output": "0 -2\n99999 0", "explanation": "Handles negative edge weights without negative cycles."}
        ],
        "test_cases": [
            {"input": "3 / 0 4 99999 / 99999 0 2 / 3 99999 0", "expected": "0 4 6\n5 0 2\n3 7 0", "is_hidden": False},
            {"input": "2 / 0 5 / 99999 0", "expected": "0 5\n99999 0", "is_hidden": False},
            {"input": "2 / 0 -2 / 99999 0", "expected": "0 -2\n99999 0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def floyd_warshall(dist):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char token[100];
    int n = 0;
    if (scanf("%s", token) != 1) return 0;
    n = atoi(token);

    int dist[105][105];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
            dist[i][j] = atoi(token);
        }
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][k] != 99999 && dist[k][j] != 99999) {
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d%s", dist[i][j], (j == n - 1) ? "" : " ");
        }
        printf("\\n");
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string token;
    if (!(cin >> token)) return 0;
    int n = stoi(token);

    vector<vector<int>> dist(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            while (cin >> token && token == "/");
            dist[i][j] = stoi(token);
        }
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][k] != 99999 && dist[k][j] != 99999) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << dist[i][j] << (j == n - 1 ? "" : " ");
        }
        cout << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.isEmpty()) return;
        int n = Integer.parseInt(tokens.get(0));

        int[][] dist = new int[n][n];
        int idx = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = Integer.parseInt(tokens.get(idx++));
            }
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dist[i][k] != 99999 && dist[k][j] != 99999) {
                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < n; j++) {
                sb.append(dist[i][j]);
                if (j < n - 1) sb.append(" ");
            }
            System.out.println(sb.toString());
        }
    }
}""",
            "python": """import sys

def floyd_warshall(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != 99999 and dist[k][j] != 99999:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        n = int(tokens[0])
        idx = 1
        dist = []
        for _ in range(n):
            row = [int(tokens[idx + j]) for j in range(n)]
            idx += n
            dist.append(row)
        res = floyd_warshall(dist)
        for row in res:
            print(" ".join(map(str, row)))"""
        })
    },

    # 14. Minimum Spanning Tree – Kruskal's Algorithm
    {
        "id": "dsa-graph-kruskal",
        "problem_num": 179,
        "title": "Minimum Spanning Tree – Kruskal's Algorithm",
        "category": "Graphs",
        "topic": "Minimum Spanning Tree",
        "subtopic": "Kruskal's Algorithm",
        "difficulty": "HARD",
        "description": "Find the minimum total edge weight required to connect all vertices without forming a cycle. Return -1 if the graph is disconnected.",
        "input_format": "Number of vertices n and edges m, followed by m triples (u, v, w).",
        "output_format": "Total weight of the minimum spanning tree, or -1 if disconnected.",
        "constraints": "1 <= n <= 2000, 0 <= m <= 10000, 0 <= weight <= 10^5",
        "time_complexity": "O(E log E)",
        "space_complexity": "O(V + E)",
        "company_tags": ["Amazon", "Microsoft", "Google", "Facebook"],
        "examples": [
            {"input": "4 5 / 0 1 10 / 0 2 6 / 0 3 5 / 1 3 15 / 2 3 4", "output": "19", "explanation": "Edges chosen: (2,3,4), (0,3,5), (0,1,10). Total = 19."},
            {"input": "3 3 / 0 1 1 / 1 2 2 / 0 2 3", "output": "3", "explanation": "Edges chosen: (0,1,1) and (1,2,2). Total = 3."},
            {"input": "3 1 / 0 1 5", "output": "-1", "explanation": "Node 2 cannot be connected, graph is disconnected."}
        ],
        "test_cases": [
            {"input": "4 5 / 0 1 10 / 0 2 6 / 0 3 5 / 1 3 15 / 2 3 4", "expected": "19", "is_hidden": False},
            {"input": "3 3 / 0 1 1 / 1 2 2 / 0 2 3", "expected": "3", "is_hidden": False},
            {"input": "3 1 / 0 1 5", "expected": "-1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def kruskal(n, edges):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int u, v, w;
} Edge;

int parent[2005];
int rnk[2005];

int find(int x) {
    if (parent[x] != x) {
        parent[x] = find(parent[x]);
    }
    return parent[x];
}

int unionSets(int a, int b) {
    int ra = find(a);
    int rb = find(b);
    if (ra == rb) return 0;
    if (rnk[ra] < rnk[rb]) {
        int tmp = ra; ra = rb; rb = tmp;
    }
    parent[rb] = ra;
    if (rnk[ra] == rnk[rb]) rnk[ra]++;
    return 1;
}

int cmp(const void *a, const void *b) {
    return (((Edge *)a)->w - ((Edge *)b)->w);
}

int main() {
    char token[100];
    int n = 0, m = 0;
    if (scanf("%s", token) != 1) return 0;
    n = atoi(token);
    if (scanf("%s", token) != 1) return 0;
    m = atoi(token);

    Edge edges[10005];
    for (int i = 0; i < m; i++) {
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        edges[i].u = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        edges[i].v = atoi(token);
        while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
        edges[i].w = atoi(token);
    }

    qsort(edges, m, sizeof(Edge), cmp);

    for (int i = 0; i < n; i++) {
        parent[i] = i;
        rnk[i] = 0;
    }

    int total = 0, count = 0;
    for (int i = 0; i < m; i++) {
        if (unionSets(edges[i].u, edges[i].v)) {
            total += edges[i].w;
            count++;
        }
    }

    if (count == n - 1) {
        printf("%d\\n", total);
    } else {
        printf("-1\\n");
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

struct Edge {
    int u, v, w;
};

int findParent(int x, vector<int>& parent) {
    if (parent[x] != x) parent[x] = findParent(parent[x], parent);
    return parent[x];
}

bool unionSets(int a, int b, vector<int>& parent, vector<int>& rank) {
    int ra = findParent(a, parent);
    int rb = findParent(b, parent);
    if (ra == rb) return false;
    if (rank[ra] < rank[rb]) swap(ra, rb);
    parent[rb] = ra;
    if (rank[ra] == rank[rb]) rank[ra]++;
    return true;
}

int main() {
    string token;
    if (!(cin >> token)) return 0;
    int n = stoi(token);
    if (!(cin >> token)) return 0;
    int m = stoi(token);

    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        while (cin >> token && token == "/");
        edges[i].u = stoi(token);
        while (cin >> token && token == "/");
        edges[i].v = stoi(token);
        while (cin >> token && token == "/");
        edges[i].w = stoi(token);
    }

    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.w < b.w;
    });

    vector<int> parent(n), rank(n, 0);
    for (int i = 0; i < n; i++) parent[i] = i;

    int total = 0, count = 0;
    for (const auto& e : edges) {
        if (unionSets(e.u, e.v, parent, rank)) {
            total += e.w;
            count++;
        }
    }

    cout << (count == n - 1 ? total : -1) << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static class Edge {
        int u, v, w;
        Edge(int u, int v, int w) { this.u = u; this.v = v; this.w = w; }
    }

    static int find(int x, int[] parent) {
        if (parent[x] != x) parent[x] = find(parent[x], parent);
        return parent[x];
    }

    static boolean union(int a, int b, int[] parent, int[] rank) {
        int ra = find(a, parent);
        int rb = find(b, parent);
        if (ra == rb) return false;
        if (rank[ra] < rank[rb]) {
            int t = ra; ra = rb; rb = t;
        }
        parent[rb] = ra;
        if (rank[ra] == rank[rb]) rank[ra]++;
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.size() < 2) return;
        int n = Integer.parseInt(tokens.get(0));
        int m = Integer.parseInt(tokens.get(1));

        List<Edge> edges = new ArrayList<>();
        int idx = 2;
        for (int i = 0; i < m; i++) {
            int u = Integer.parseInt(tokens.get(idx++));
            int v = Integer.parseInt(tokens.get(idx++));
            int w = Integer.parseInt(tokens.get(idx++));
            edges.add(new Edge(u, v, w));
        }

        edges.sort(Comparator.comparingInt(a -> a.w));

        int[] parent = new int[n];
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        int total = 0, count = 0;
        for (Edge e : edges) {
            if (union(e.u, e.v, parent, rank)) {
                total += e.w;
                count++;
            }
        }

        System.out.println(count == n - 1 ? total : -1);
    }
}""",
            "python": """import sys

def kruskal(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    edges.sort(key=lambda x: x[2])
    total = 0
    count = 0

    for u, v, w in edges:
        if union(u, v):
            total += w
            count += 1

    return total if count == n - 1 else -1

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        n = int(tokens[0])
        m = int(tokens[1])
        edges = []
        idx = 2
        for _ in range(m):
            edges.append((int(tokens[idx]), int(tokens[idx + 1]), int(tokens[idx + 2])))
            idx += 3
        print(kruskal(n, edges))"""
        })
    },

    # 15. Word Ladder
    {
        "id": "dsa-graph-word-ladder",
        "problem_num": 180,
        "title": "Word Ladder",
        "category": "Graphs",
        "topic": "Graph BFS",
        "subtopic": "Word Ladder",
        "difficulty": "HARD",
        "description": "Transform a starting word into an ending word by changing one character at a time. Every intermediate word must exist in the dictionary. Return the shortest transformation length, including the starting and ending words.",
        "input_format": "Starting word, ending word, and dictionary word list separated by spaces or slashes.",
        "output_format": "Shortest transformation length, or 0 if unreachable.",
        "constraints": "1 <= word.length <= 10, 1 <= wordList.length <= 5000",
        "time_complexity": "O(M^2 * N)",
        "space_complexity": "O(M * N)",
        "company_tags": ["Amazon", "Google", "Facebook", "Microsoft", "LinkedIn"],
        "examples": [
            {"input": "hit / cog / hot dot dog lot log cog", "output": "5", "explanation": "Shortest transformation: hit -> hot -> dot -> dog -> cog has length 5."},
            {"input": "hit / cog / hot dot dog lot log", "output": "0", "explanation": "Ending word 'cog' is not in the dictionary."},
            {"input": "a / c / a b c", "output": "2", "explanation": "Transformation: a -> c has length 2."}
        ],
        "test_cases": [
            {"input": "hit / cog / hot dot dog lot log cog", "expected": "5", "is_hidden": False},
            {"input": "hit / cog / hot dot dog lot log", "expected": "0", "is_hidden": False},
            {"input": "a / c / a b c", "expected": "2", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <queue>\n#include <unordered_set>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def word_ladder(begin, end, words):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char words[5005][20];
int wordCount = 0;
int visited[5005];

int diffOne(const char *a, const char *b, int len) {
    int diff = 0;
    for (int i = 0; i < len; i++) {
        if (a[i] != b[i]) {
            diff++;
            if (diff > 1) return 0;
        }
    }
    return diff == 1;
}

int main() {
    char token[100];
    char begin[20], end[20];

    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    strcpy(begin, token);
    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    strcpy(end, token);

    int targetIdx = -1;
    while (scanf("%s", token) == 1) {
        if (strcmp(token, "/") == 0) continue;
        strcpy(words[wordCount], token);
        if (strcmp(token, end) == 0) targetIdx = wordCount;
        wordCount++;
    }

    if (targetIdx == -1) {
        printf("0\\n");
        return 0;
    }

    int q_idx[5005], q_dist[5005];
    int front = 0, back = 0;
    int len = strlen(begin);

    for (int i = 0; i < wordCount; i++) {
        if (diffOne(begin, words[i], len)) {
            visited[i] = 1;
            q_idx[back] = i;
            q_dist[back] = 2;
            back++;
        }
    }

    int result = 0;
    while (front < back) {
        int curr = q_idx[front];
        int d = q_dist[front++];

        if (strcmp(words[curr], end) == 0) {
            result = d;
            break;
        }

        for (int i = 0; i < wordCount; i++) {
            if (!visited[i] && diffOne(words[curr], words[i], len)) {
                visited[i] = 1;
                q_idx[back] = i;
                q_dist[back] = d + 1;
                back++;
            }
        }
    }

    printf("%d\\n", result);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

int main() {
    string token;
    vector<string> tokens;
    while (cin >> token) {
        if (token != "/") tokens.push_back(token);
    }
    if (tokens.size() < 3) {
        cout << 0 << endl;
        return 0;
    }

    string begin = tokens[0];
    string end = tokens[1];
    unordered_set<string> word_set;
    for (size_t i = 2; i < tokens.size(); i++) {
        word_set.insert(tokens[i]);
    }

    if (word_set.find(end) == word_set.end()) {
        cout << 0 << endl;
        return 0;
    }

    queue<pair<string, int>> q;
    unordered_set<string> visited;
    q.push({begin, 1});
    visited.insert(begin);

    int result = 0;
    while (!q.empty()) {
        auto curr = q.front();
        q.pop();
        string word = curr.first;
        int length = curr.second;

        if (word == end) {
            result = length;
            break;
        }

        for (size_t i = 0; i < word.length(); i++) {
            string temp = word;
            for (char ch = 'a'; ch <= 'z'; ch++) {
                temp[i] = ch;
                if (word_set.count(temp) && !visited.count(temp)) {
                    visited.insert(temp);
                    q.push({temp, length + 1});
                }
            }
        }
    }

    cout << result << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String t = sc.next();
            if (!t.equals("/")) tokens.add(t);
        }
        if (tokens.size() < 3) {
            System.out.println(0);
            return;
        }

        String begin = tokens.get(0);
        String end = tokens.get(1);
        Set<String> wordSet = new HashSet<>();
        for (int i = 2; i < tokens.size(); i++) {
            wordSet.add(tokens.get(i));
        }

        if (!wordSet.contains(end)) {
            System.out.println(0);
            return;
        }

        Queue<String> queue = new LinkedList<>();
        Queue<Integer> lengthQueue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.offer(begin);
        lengthQueue.offer(1);
        visited.add(begin);

        int result = 0;
        while (!queue.isEmpty()) {
            String word = queue.poll();
            int length = lengthQueue.poll();

            if (word.equals(end)) {
                result = length;
                break;
            }

            char[] chars = word.toCharArray();
            for (int i = 0; i < chars.length; i++) {
                char orig = chars[i];
                for (char ch = 'a'; ch <= 'z'; ch++) {
                    chars[i] = ch;
                    String newWord = new String(chars);
                    if (wordSet.contains(newWord) && !visited.contains(newWord)) {
                        visited.add(newWord);
                        queue.offer(newWord);
                        lengthQueue.offer(length + 1);
                    }
                }
                chars[i] = orig;
            }
        }

        System.out.println(result);
    }
}""",
            "python": """import sys
from collections import deque

def word_ladder(begin, end, words):
    word_set = set(words)
    if end not in word_set:
        return 0

    q = deque([(begin, 1)])
    visited = {begin}

    while q:
        word, length = q.popleft()
        if word == end:
            return length

        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + ch + word[i + 1:]
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    q.append((new_word, length + 1))

    return 0

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if len(tokens) >= 3:
        begin = tokens[0]
        end = tokens[1]
        words = tokens[2:]
        print(word_ladder(begin, end, words))
    else:
        print(0)"""
        })
    }
]

problems.extend(graph_data)

with open("backend/app/data/dsa_problems_seed.json", "w", encoding="utf-8") as f:
    json.dump(problems, f, indent=2)

print(f"Successfully added 15 Graph problems! Total problems in seed: {len(problems)}")
