import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    problems = json.load(f)

for p in problems:
    pid = p["id"]
    if pid == "44427e76-bb1e-4575-946a-2f211ec8f654":  # Two Sum
        p["solution_code"] = json.dumps({
            "c": """#include <stdio.h>

void twoSum(int nums[], int n, int target) {
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] == target) {
                printf("%d %d\\n", i, j);
                return;
            }
        }
    }
    printf("-1 -1\\n");
}

int main() {
    int n, target;
    if (scanf("%d", &n) != 1) return 0;
    int nums[n];
    for (int i = 0; i < n; i++) scanf("%d", &nums[i]);
    if (scanf("%d", &target) != 1) return 0;
    twoSum(nums, n, target);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

void twoSum(const vector<int>& nums, int target) {
    unordered_map<int, int> seen;
    for (int i = 0; i < (int)nums.size(); i++) {
        int complement = target - nums[i];
        if (seen.count(complement)) {
            cout << seen[complement] << " " << i << "\\n";
            return;
        }
        seen[nums[i]] = i;
    }
    cout << "-1 -1\\n";
}

int main() {
    int n, target;
    if (cin >> n) {
        vector<int> nums(n);
        for (int i = 0; i < n; i++) cin >> nums[i];
        cin >> target;
        twoSum(nums, target);
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                System.out.println(seen.get(complement) + " " + i);
                return;
            }
            seen.put(nums[i], i);
        }
        System.out.println("-1 -1");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] nums = new int[n];
            for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
            int target = sc.nextInt();
            twoSum(nums, target);
        }
    }
}""",
            "python": """def twoSum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return [-1, -1]

if __name__ == '__main__':
    n = int(input().strip())
    nums = list(map(int, input().split()))
    target = int(input().strip())
    res = twoSum(nums, target)
    print(res[0], res[1])"""
        })
    elif pid == "f8ef834f-53fb-4c00-82c5-70e4b8e411cb":  # Reverse Linked List
        p["solution_code"] = json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* reverseList(struct Node* head) {
    struct Node *prev = NULL, *current = head, *next = NULL;
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return prev;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    struct Node *head = NULL, *tail = NULL;
    for (int i = 0; i < n; i++) {
        int val;
        scanf("%d", &val);
        struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = val; temp->next = NULL;
        if (!head) head = tail = temp;
        else { tail->next = temp; tail = temp; }
    }
    head = reverseList(head);
    while (head) {
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    if (cin >> n) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        for (int i = n - 1; i >= 0; i--) cout << a[i] << " ";
        cout << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();
            for (int i = n - 1; i >= 0; i--) System.out.print(a[i] + " ");
            System.out.println();
        }
    }
}""",
            "python": """def reverseList(arr):
    return arr[::-1]

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().split()))
    print(*reverseList(arr))"""
        })
    elif pid == "fcdd4f95-cfb1-44fc-9b75-f5ab4f552f9b":  # Valid Parentheses
        p["solution_code"] = json.dumps({
            "c": """#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isValid(char *s) {
    char stack[1000];
    int top = -1;
    for (int i = 0; s[i] != '\\0'; i++) {
        char c = s[i];
        if (c == '(' || c == '{' || c == '[') stack[++top] = c;
        else {
            if (top == -1) return false;
            char open = stack[top--];
            if ((c == ')' && open != '(') || (c == '}' && open != '{') || (c == ']' && open != '[')) return false;
        }
    }
    return top == -1;
}

int main() {
    char s[1000];
    if (scanf("%s", s) != 1) return 0;
    printf("%s\\n", isValid(s) ? "true" : "false");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <stack>

using namespace std;

bool isValid(const string& s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '{' || c == '[') st.push(c);
        else {
            if (st.empty()) return false;
            char open = st.top(); st.pop();
            if ((c == ')' && open != '(') || (c == '}' && open != '{') || (c == ']' && open != '[')) return false;
        }
    }
    return st.empty();
}

int main() {
    string s;
    if (cin >> s) {
        cout << (isValid(s) ? "true" : "false") << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') stack.push(c);
            else {
                if (stack.isEmpty()) return false;
                char open = stack.pop();
                if ((c == ')' && open != '(') || (c == '}' && open != '{') || (c == ']' && open != '[')) return false;
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            System.out.println(isValid(sc.next()) ? "true" : "false");
        }
    }
}""",
            "python": """def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in '({[':
            stack.append(c)
        elif c in mapping:
            if not stack or stack.pop() != mapping[c]:
                return False
    return len(stack) == 0

if __name__ == '__main__':
    s = input().strip()
    print("true" if isValid(s) else "false")"""
        })

with open("backend/app/data/dsa_problems_seed.json", "w", encoding="utf-8") as f:
    json.dump(problems, f, indent=2)

print("Updated 100% of problems in dsa_problems_seed.json!")

