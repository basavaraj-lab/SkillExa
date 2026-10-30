import sys, os
sys.path.insert(0, os.path.abspath('.'))
import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    problems = json.load(f)

hash_ids = {
    "dsa-hash-two-sum", "dsa-hash-contains-duplicate", "dsa-hash-frequency-counter",
    "dsa-hash-intersection-two-arrays", "dsa-hash-first-unique-char", "dsa-hash-group-anagrams",
    "dsa-hash-longest-consecutive-sequence", "dsa-hash-subarray-sum-equals-k", "dsa-hash-top-k-frequent",
    "dsa-hash-4sum-ii", "dsa-hash-min-window-substring", "dsa-hash-count-smaller-after-self",
    "dsa-hash-longest-duplicate-substring", "dsa-hash-substring-concat-all-words", "dsa-hash-distinct-echo-substrings"
}
problems = [p for p in problems if p["id"] not in hash_ids]

hash_data = [
    # 1. Two Sum
    {
        "id": "dsa-hash-two-sum",
        "problem_num": 136,
        "title": "Two Sum",
        "category": "Hashing",
        "topic": "Hash Maps",
        "subtopic": "Complement Lookup",
        "difficulty": "EASY",
        "description": "Given an array of integers and an integer target, return the indices of the two numbers such that they add up to target.",
        "input_format": "Array elements followed by target.",
        "output_format": "List of two 0-based indices [index1, index2].",
        "constraints": "2 <= nums.length <= 10^4, -10^9 <= nums[i] <= 10^9",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Google", "Microsoft", "Facebook", "Apple"],
        "examples": [
            {"input": "2 7 11 15\n9", "output": "[0, 1]", "explanation": "nums[0] + nums[1] = 2 + 7 = 9"},
            {"input": "3 2 4\n6", "output": "[1, 2]", "explanation": "nums[1] + nums[2] = 2 + 4 = 6"},
            {"input": "3 3\n6", "output": "[0, 1]", "explanation": "nums[0] + nums[1] = 3 + 3 = 6"}
        ],
        "test_cases": [
            {"input": "2 7 11 15\n9", "expected": "[0, 1]", "is_hidden": False},
            {"input": "3 2 4\n6", "expected": "[1, 2]", "is_hidden": False},
            {"input": "3 3\n6", "expected": "[0, 1]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def two_sum(nums, target):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char token[100];
    int nums[5000];
    int count = 0;
    while (scanf("%s", token) == 1) {
        if (strcmp(token, "/") == 0) continue;
        nums[count++] = atoi(token);
    }
    if (count < 2) return 0;
    int target = nums[count - 1];
    int n = count - 1;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] == target) {
                printf("[%d, %d]\\n", i, j);
                return 0;
            }
        }
    }
    printf("[]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    string token;
    vector<int> nums;
    while (cin >> token) {
        if (token == "/") continue;
        nums.push_back(stoi(token));
    }
    if (nums.size() < 2) return 0;
    int target = nums.back();
    nums.pop_back();

    unordered_map<int, int> seen;
    for (int i = 0; i < (int)nums.size(); i++) {
        int diff = target - nums[i];
        if (seen.find(diff) != seen.end()) {
            cout << "[" << seen[diff] << ", " << i << "]\\n";
            return 0;
        }
        seen[nums[i]] = i;
    }
    cout << "[]\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> nums = new ArrayList<>();
        while (sc.hasNext()) {
            String token = sc.next();
            if (token.equals("/")) continue;
            nums.add(Integer.parseInt(token));
        }
        if (nums.size() < 2) return;
        int target = nums.remove(nums.size() - 1);
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums.get(i);
            if (seen.containsKey(diff)) {
                System.out.println("[" + seen.get(diff) + ", " + i + "]");
                return;
            }
            seen.put(nums.get(i), i);
        }
        System.out.println("[]");
    }
}""",
            "python": """import sys

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if len(raw) >= 2:
        nums = list(map(int, raw[:-1]))
        target = int(raw[-1])
        print(two_sum(nums, target))"""
        })
    },

    # 2. Contains Duplicate
    {
        "id": "dsa-hash-contains-duplicate",
        "problem_num": 137,
        "title": "Contains Duplicate",
        "category": "Hashing",
        "topic": "Hash Sets",
        "subtopic": "Uniqueness Check",
        "difficulty": "EASY",
        "description": "Given an integer array nums, return true if any value appears at least twice, and false if every element is distinct.",
        "input_format": "Space-separated integers.",
        "output_format": "True or False.",
        "constraints": "1 <= nums.length <= 10^5, -10^9 <= nums[i] <= 10^9",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Apple", "Adobe"],
        "examples": [
            {"input": "1 2 3 1", "output": "True", "explanation": "1 appears twice."},
            {"input": "1 2 3 4", "output": "False", "explanation": "All elements distinct."},
            {"input": "5 5 5", "output": "True", "explanation": "5 appears multiple times."}
        ],
        "test_cases": [
            {"input": "1 2 3 1", "expected": "True", "is_hidden": False},
            {"input": "1 2 3 4", "expected": "False", "is_hidden": False},
            {"input": "5 5 5", "expected": "True", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_set>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def contains_duplicate(nums):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int nums[50000];
    int n = 0;
    while (scanf("%d", &nums[n]) == 1) n++;
    qsort(nums, n, sizeof(int), cmp);
    for (int i = 1; i < n; i++) {
        if (nums[i] == nums[i - 1]) {
            printf("True\\n");
            return 0;
        }
    }
    printf("False\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
    int x;
    unordered_set<int> seen;
    bool has_dup = false;
    while (cin >> x) {
        if (seen.find(x) != seen.end()) {
            has_dup = true;
        }
        seen.insert(x);
    }
    cout << (has_dup ? "True" : "False") << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Set<Integer> seen = new HashSet<>();
        boolean hasDup = false;
        while (sc.hasNextInt()) {
            int x = sc.nextInt();
            if (!seen.add(x)) {
                hasDup = true;
            }
        }
        System.out.println(hasDup ? "True" : "False");
    }
}""",
            "python": """import sys

def contains_duplicate(nums):
    return len(nums) != len(set(nums))

if __name__ == '__main__':
    nums = list(map(int, sys.stdin.read().split()))
    if nums:
        print(contains_duplicate(nums))"""
        })
    },

    # 3. Frequency Counter
    {
        "id": "dsa-hash-frequency-counter",
        "problem_num": 138,
        "title": "Frequency Counter",
        "category": "Hashing",
        "topic": "Hash Maps",
        "subtopic": "Counting Elements",
        "difficulty": "EASY",
        "description": "Count how many times each element appears in an array and print the frequency dictionary sorted by key.",
        "input_format": "Space-separated integers.",
        "output_format": "Dictionary representation {k1: v1, k2: v2} sorted by key.",
        "constraints": "1 <= nums.length <= 10^4",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "company_tags": ["TCS", "Infosys", "Wipro"],
        "examples": [
            {"input": "1 2 2 3 3 3", "output": "{1: 1, 2: 2, 3: 3}", "explanation": "1: 1 time, 2: 2 times, 3: 3 times."},
            {"input": "5 5 5", "output": "{5: 3}", "explanation": "5 appears 3 times."},
            {"input": "1 2 3", "output": "{1: 1, 2: 1, 3: 1}", "explanation": "Each appears once."}
        ],
        "test_cases": [
            {"input": "1 2 2 3 3 3", "expected": "{1: 1, 2: 2, 3: 3}", "is_hidden": False},
            {"input": "5 5 5", "expected": "{5: 3}", "is_hidden": False},
            {"input": "1 2 3", "expected": "{1: 1, 2: 1, 3: 1}", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <map>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def frequency(nums):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int nums[10000];
    int n = 0;
    while (scanf("%d", &nums[n]) == 1) n++;
    if (n == 0) { printf("{}\\n"); return 0; }
    qsort(nums, n, sizeof(int), cmp);

    printf("{");
    int i = 0;
    while (i < n) {
        int val = nums[i];
        int count = 0;
        while (i < n && nums[i] == val) {
            count++;
            i++;
        }
        printf("%d: %d%s", val, count, (i < n ? ", " : ""));
    }
    printf("}\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <map>

using namespace std;

int main() {
    int x;
    map<int, int> freq;
    while (cin >> x) {
        freq[x]++;
    }
    cout << "{";
    auto it = freq.begin();
    while (it != freq.end()) {
        cout << it->first << ": " << it->second;
        if (++it != freq.end()) cout << ", ";
    }
    cout << "}\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<Integer, Integer> freq = new TreeMap<>();
        while (sc.hasNextInt()) {
            int x = sc.nextInt();
            freq.put(x, freq.getOrDefault(x, 0) + 1);
        }
        StringBuilder sb = new StringBuilder("{");
        int count = 0, size = freq.size();
        for (Map.Entry<Integer, Integer> e : freq.entrySet()) {
            sb.append(e.getKey()).append(": ").append(e.getValue());
            if (++count < size) sb.append(", ");
        }
        sb.append("}");
        System.out.println(sb.toString());
    }
}""",
            "python": """import sys

def frequency(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq

if __name__ == '__main__':
    nums = list(map(int, sys.stdin.read().split()))
    if nums:
        print(dict(sorted(frequency(nums).items())))"""
        })
    },

    # 4. Intersection of Two Arrays
    {
        "id": "dsa-hash-intersection-two-arrays",
        "problem_num": 139,
        "title": "Intersection of Two Arrays",
        "category": "Hashing",
        "topic": "Hash Sets",
        "subtopic": "Set Intersection",
        "difficulty": "EASY",
        "description": "Given two integer arrays, return a sorted array of their unique intersection.",
        "input_format": "Two lines or separated by '/' containing the arrays.",
        "output_format": "Sorted list of unique common elements.",
        "constraints": "1 <= nums1.length, nums2.length <= 1000",
        "time_complexity": "O(N + M + K log K)",
        "space_complexity": "O(N + M)",
        "company_tags": ["Google", "Facebook", "Amazon"],
        "examples": [
            {"input": "1 2 2 1\n2 2", "output": "[2]", "explanation": "2 is the only common element."},
            {"input": "4 9 5\n9 4 9 8 4", "output": "[4, 9]", "explanation": "4 and 9 are present in both."},
            {"input": "1 2 3\n4 5 6", "output": "[]", "explanation": "No common elements."}
        ],
        "test_cases": [
            {"input": "1 2 2 1\n2 2", "expected": "[2]", "is_hidden": False},
            {"input": "4 9 5\n9 4 9 8 4", "expected": "[4, 9]", "is_hidden": False},
            {"input": "1 2 3\n4 5 6", "expected": "[]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <set>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def intersection(a, b):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
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

    int a[1000], b[1000];
    int na = 0, nb = 0;
    char *tok = strtok(line1, " \\t\\r\\n");
    while (tok) {
        a[na++] = atoi(tok);
        tok = strtok(NULL, " \\t\\r\\n");
    }
    tok = strtok(line2, " \\t\\r\\n");
    while (tok) {
        b[nb++] = atoi(tok);
        tok = strtok(NULL, " \\t\\r\\n");
    }

    int res[1000];
    int nr = 0;
    for (int i = 0; i < na; i++) {
        for (int j = 0; j < nb; j++) {
            if (a[i] == b[j]) {
                int already = 0;
                for (int k = 0; k < nr; k++) {
                    if (res[k] == a[i]) { already = 1; break; }
                }
                if (!already) res[nr++] = a[i];
                break;
            }
        }
    }
    qsort(res, nr, sizeof(int), cmp);

    printf("[");
    for (int i = 0; i < nr; i++) {
        printf("%d%s", res[i], (i == nr - 1 ? "" : ", "));
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <set>

using namespace std;

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

    set<int> setA;
    stringstream ss1(line1);
    int x;
    while (ss1 >> x) setA.insert(x);

    set<int> result;
    stringstream ss2(line2);
    while (ss2 >> x) {
        if (setA.count(x)) result.insert(x);
    }

    cout << "[";
    auto it = result.begin();
    while (it != result.end()) {
        cout << *it;
        if (++it != result.end()) cout << ", ";
    }
    cout << "]\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
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

        Set<Integer> setA = new HashSet<>();
        Scanner s1 = new Scanner(line1);
        while (s1.hasNextInt()) setA.add(s1.nextInt());

        Set<Integer> result = new TreeSet<>();
        Scanner s2 = new Scanner(line2);
        while (s2.hasNextInt()) {
            int val = s2.nextInt();
            if (setA.contains(val)) result.add(val);
        }

        System.out.println(result.toString());
    }
}""",
            "python": """import sys

def intersection(a, b):
    return sorted(list(set(a) & set(b)))

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if '/' in raw:
        parts = raw.split('/')
        a = list(map(int, parts[0].split()))
        b = list(map(int, parts[1].split()))
    else:
        lines = [l for l in raw.splitlines() if l.strip()]
        a = list(map(int, lines[0].split())) if len(lines) > 0 else []
        b = list(map(int, lines[1].split())) if len(lines) > 1 else []
    print(intersection(a, b))"""
        })
    },

    # 5. First Unique Character
    {
        "id": "dsa-hash-first-unique-char",
        "problem_num": 140,
        "title": "First Unique Character in a String",
        "category": "Hashing",
        "topic": "Hash Maps",
        "subtopic": "Frequency Count",
        "difficulty": "EASY",
        "description": "Find the index of the first non-repeating character in a string. Return -1 if none exists.",
        "input_format": "A single string s.",
        "output_format": "0-based index or -1.",
        "constraints": "1 <= s.length <= 10^5, s consists of lowercase English letters.",
        "time_complexity": "O(N)",
        "space_complexity": "O(1) (26 characters)",
        "company_tags": ["Amazon", "Bloomberg", "Microsoft"],
        "examples": [
            {"input": "leetcode", "output": "0", "explanation": "'l' is the first unique character."},
            {"input": "loveleetcode", "output": "2", "explanation": "'v' is the first unique character at index 2."},
            {"input": "aabb", "output": "-1", "explanation": "No unique characters."}
        ],
        "test_cases": [
            {"input": "leetcode", "expected": "0", "is_hidden": False},
            {"input": "loveleetcode", "expected": "2", "is_hidden": False},
            {"input": "aabb", "expected": "-1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def first_unique(s):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

int main() {
    char s[100005];
    if (scanf("%s", s) != 1) return 0;
    int freq[256] = {0};
    int len = strlen(s);
    for (int i = 0; i < len; i++) {
        freq[(unsigned char)s[i]]++;
    }
    for (int i = 0; i < len; i++) {
        if (freq[(unsigned char)s[i]] == 1) {
            printf("%d\\n", i);
            return 0;
        }
    }
    printf("-1\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    string s;
    if (cin >> s) {
        unordered_map<char, int> freq;
        for (char ch : s) freq[ch]++;
        for (int i = 0; i < (int)s.length(); i++) {
            if (freq[s[i]] == 1) {
                cout << i << "\\n";
                return 0;
            }
        }
        cout << -1 << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            Map<Character, Integer> freq = new HashMap<>();
            for (char ch : s.toCharArray()) freq.put(ch, freq.getOrDefault(ch, 0) + 1);
            for (int i = 0; i < s.length(); i++) {
                if (freq.get(s.charAt(i)) == 1) {
                    System.out.println(i);
                    return;
                }
            }
            System.out.println(-1);
        }
    }
}""",
            "python": """import sys

def first_unique(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        print(first_unique(s))"""
        })
    },

    # 6. Group Anagrams
    {
        "id": "dsa-hash-group-anagrams",
        "problem_num": 141,
        "title": "Group Anagrams",
        "category": "Hashing",
        "topic": "Hash Maps",
        "subtopic": "Anagram Categorization",
        "difficulty": "MEDIUM",
        "description": "Group words that contain the same characters in any order.",
        "input_format": "Space-separated words.",
        "output_format": "List of lists of grouped anagrams.",
        "constraints": "1 <= words.length <= 10^4",
        "time_complexity": "O(N * K log K)",
        "space_complexity": "O(N * K)",
        "company_tags": ["Amazon", "Microsoft", "Uber"],
        "examples": [
            {"input": "eat tea tan ate nat bat", "output": "[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]", "explanation": "Grouped by identical character counts."},
            {"input": "abc bca cab", "output": "[['abc', 'bca', 'cab']]", "explanation": "All three words are anagrams."},
            {"input": "a b c", "output": "[['a'], ['b'], ['c']]", "explanation": "Each is distinct."}
        ],
        "test_cases": [
            {"input": "eat tea tan ate nat bat", "expected": "[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]", "is_hidden": False},
            {"input": "abc bca cab", "expected": "[['abc', 'bca', 'cab']]", "is_hidden": False},
            {"input": "a b c", "expected": "[['a'], ['b'], ['c']]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_map>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def group_anagrams(words):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int cmpChar(const void *a, const void *b) {
    return (*(char*)a - *(char*)b);
}

int main() {
    char words[1000][50];
    char keys[1000][50];
    int n = 0;
    while (scanf("%s", words[n]) == 1) {
        strcpy(keys[n], words[n]);
        qsort(keys[n], strlen(keys[n]), sizeof(char), cmpChar);
        n++;
    }

    char unique_keys[1000][50];
    int uk_count = 0;
    for (int i = 0; i < n; i++) {
        int found = 0;
        for (int j = 0; j < uk_count; j++) {
            if (strcmp(unique_keys[j], keys[i]) == 0) { found = 1; break; }
        }
        if (!found) strcpy(unique_keys[uk_count++], keys[i]);
    }

    printf("[");
    for (int i = 0; i < uk_count; i++) {
        printf("[");
        int first = 1;
        for (int j = 0; j < n; j++) {
            if (strcmp(unique_keys[i], keys[j]) == 0) {
                if (!first) printf(", ");
                printf("'%s'", words[j]);
                first = 0;
            }
        }
        printf("]%s", (i == uk_count - 1 ? "" : ", "));
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    string word;
    vector<string> words;
    vector<string> order_keys;
    map<string, vector<string>> groups;

    while (cin >> word) {
        string key = word;
        sort(key.begin(), key.end());
        if (groups.find(key) == groups.end()) {
            order_keys.push_back(key);
        }
        groups[key].push_back(word);
    }

    cout << "[";
    for (size_t i = 0; i < order_keys.size(); i++) {
        cout << "[";
        const auto& grp = groups[order_keys[i]];
        for (size_t j = 0; j < grp.size(); j++) {
            cout << "'" << grp[j] << "'" << (j == grp.size() - 1 ? "" : ", ");
        }
        cout << "]" << (i == order_keys.size() - 1 ? "" : ", ");
    }
    cout << "]\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<String, List<String>> groups = new LinkedHashMap<>();
        while (sc.hasNext()) {
            String word = sc.next();
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            groups.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
        }

        StringBuilder sb = new StringBuilder("[");
        int count = 0, total = groups.size();
        for (List<String> grp : groups.values()) {
            sb.append("[");
            for (int i = 0; i < grp.size(); i++) {
                sb.append("'").append(grp.get(i)).append("'").append(i == grp.size() - 1 ? "" : ", ");
            }
            sb.append("]").append(++count == total ? "" : ", ");
        }
        sb.append("]");
        System.out.println(sb.toString());
    }
}""",
            "python": """import sys

def group_anagrams(words):
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())

if __name__ == '__main__':
    words = sys.stdin.read().split()
    if words:
        print(group_anagrams(words))"""
        })
    },

    # 7. Longest Consecutive Sequence
    {
        "id": "dsa-hash-longest-consecutive-sequence",
        "problem_num": 142,
        "title": "Longest Consecutive Sequence",
        "category": "Hashing",
        "topic": "Hash Sets",
        "subtopic": "Sequence Extension",
        "difficulty": "MEDIUM",
        "description": "Given an unsorted array of integers, find the length of the longest consecutive elements sequence in O(N) time.",
        "input_format": "Space-separated integers.",
        "output_format": "Length of longest consecutive sequence.",
        "constraints": "0 <= nums.length <= 10^5",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Google", "Amazon", "Spotify"],
        "examples": [
            {"input": "100 4 200 1 3 2", "output": "4", "explanation": "[1, 2, 3, 4] length is 4."},
            {"input": "0 3 7 2 5 8 4 6 0 1", "output": "9", "explanation": "[0, 1, 2, 3, 4, 5, 6, 7, 8] length is 9."},
            {"input": "10 20 30", "output": "1", "explanation": "No consecutive pairs, max length is 1."}
        ],
        "test_cases": [
            {"input": "100 4 200 1 3 2", "expected": "4", "is_hidden": False},
            {"input": "0 3 7 2 5 8 4 6 0 1", "expected": "9", "is_hidden": False},
            {"input": "10 20 30", "expected": "1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_set>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def longest_consecutive(nums):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int nums[50000];
    int n = 0;
    while (scanf("%d", &nums[n]) == 1) n++;
    if (n == 0) { printf("0\\n"); return 0; }
    qsort(nums, n, sizeof(int), cmp);

    int longest = 1;
    int curr = 1;
    for (int i = 1; i < n; i++) {
        if (nums[i] == nums[i - 1]) continue;
        if (nums[i] == nums[i - 1] + 1) {
            curr++;
        } else {
            if (curr > longest) longest = curr;
            curr = 1;
        }
    }
    if (curr > longest) longest = curr;
    printf("%d\\n", longest);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

int main() {
    int x;
    unordered_set<int> s;
    while (cin >> x) s.insert(x);

    int longest = 0;
    for (int num : s) {
        if (s.find(num - 1) == s.end()) {
            int length = 1;
            while (s.find(num + length) != s.end()) {
                length++;
            }
            longest = max(longest, length);
        }
    }
    cout << longest << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Set<Integer> set = new HashSet<>();
        while (sc.hasNextInt()) set.add(sc.nextInt());

        int longest = 0;
        for (int num : set) {
            if (!set.contains(num - 1)) {
                int length = 1;
                while (set.contains(num + length)) length++;
                longest = Math.max(longest, length);
            }
        }
        System.out.println(longest);
    }
}""",
            "python": """import sys

def longest_consecutive(nums):
    s = set(nums)
    longest = 0
    for num in s:
        if num - 1 not in s:
            length = 1
            while num + length in s:
                length += 1
            longest = max(longest, length)
    return longest

if __name__ == '__main__':
    nums = list(map(int, sys.stdin.read().split()))
    if nums:
        print(longest_consecutive(nums))
    else:
        print(0)"""
        })
    },

    # 8. Subarray Sum Equals K
    {
        "id": "dsa-hash-subarray-sum-equals-k",
        "problem_num": 143,
        "title": "Subarray Sum Equals K",
        "category": "Hashing",
        "topic": "Prefix Sums",
        "subtopic": "Prefix Sum Frequency",
        "difficulty": "MEDIUM",
        "description": "Find the total number of continuous subarrays whose sum equals to k.",
        "input_format": "Array elements followed by k (or separated by '/').",
        "output_format": "Count of valid subarrays.",
        "constraints": "1 <= nums.length <= 2 * 10^4",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Facebook", "Amazon", "Google"],
        "examples": [
            {"input": "1 1 1\n2", "output": "2", "explanation": "[1, 1] at start, and [1, 1] at end."},
            {"input": "1 2 3\n3", "output": "2", "explanation": "[1, 2] and [3]."},
            {"input": "1 -1 0\n0", "output": "3", "explanation": "[1, -1], [0], and [1, -1, 0]."}
        ],
        "test_cases": [
            {"input": "1 1 1\n2", "expected": "2", "is_hidden": False},
            {"input": "1 2 3\n3", "expected": "2", "is_hidden": False},
            {"input": "1 -1 0\n0", "expected": "3", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def subarray_sum(nums, k):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char token[100];
    int nums[50000];
    int count = 0;
    while (scanf("%s", token) == 1) {
        if (strcmp(token, "/") == 0) continue;
        nums[count++] = atoi(token);
    }
    if (count < 2) { printf("0\\n"); return 0; }
    int k = nums[count - 1];
    int n = count - 1;

    int ans = 0;
    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = i; j < n; j++) {
            sum += nums[j];
            if (sum == k) ans++;
        }
    }
    printf("%d\\n", ans);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    string token;
    vector<int> nums;
    while (cin >> token) {
        if (token == "/") continue;
        nums.push_back(stoi(token));
    }
    if (nums.size() < 2) { cout << 0 << "\\n"; return 0; }
    int k = nums.back();
    nums.pop_back();

    unordered_map<int, int> freq;
    freq[0] = 1;
    int count = 0, total = 0;
    for (int num : nums) {
        total += num;
        if (freq.find(total - k) != freq.end()) {
            count += freq[total - k];
        }
        freq[total]++;
    }
    cout << count << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> nums = new ArrayList<>();
        while (sc.hasNext()) {
            String token = sc.next();
            if (token.equals("/")) continue;
            nums.add(Integer.parseInt(token));
        }
        if (nums.size() < 2) { System.out.println(0); return; }
        int k = nums.remove(nums.size() - 1);
        Map<Integer, Integer> freq = new HashMap<>();
        freq.put(0, 1);
        int count = 0, total = 0;
        for (int num : nums) {
            total += num;
            count += freq.getOrDefault(total - k, 0);
            freq.put(total, freq.getOrDefault(total, 0) + 1);
        }
        System.out.println(count);
    }
}""",
            "python": """import sys

def subarray_sum(nums, k):
    count = 0
    total = 0
    freq = {0: 1}
    for num in nums:
        total += num
        count += freq.get(total - k, 0)
        freq[total] = freq.get(total, 0) + 1
    return count

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if len(raw) >= 2:
        nums = list(map(int, raw[:-1]))
        k = int(raw[-1])
        print(subarray_sum(nums, k))"""
        })
    },

    # 9. Top K Frequent Elements
    {
        "id": "dsa-hash-top-k-frequent",
        "problem_num": 144,
        "title": "Top K Frequent Elements",
        "category": "Hashing",
        "topic": "Hash Maps",
        "subtopic": "Frequency Sorting",
        "difficulty": "MEDIUM",
        "description": "Given an integer array nums and an integer k, return the k most frequent elements sorted by highest frequency (and smaller number first on ties).",
        "input_format": "Array elements followed by k.",
        "output_format": "List of top k elements.",
        "constraints": "1 <= nums.length <= 10^5, k is valid.",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Facebook", "Microsoft"],
        "examples": [
            {"input": "1 1 1 2 2 3\n2", "output": "[1, 2]", "explanation": "1 appears 3 times, 2 appears 2 times."},
            {"input": "1 2 2 3 3 3\n2", "output": "[3, 2]", "explanation": "3 appears 3 times, 2 appears 2 times."},
            {"input": "4 4 5 5 6\n2", "output": "[4, 5]", "explanation": "4 and 5 tie at 2 each, smaller 4 comes first."}
        ],
        "test_cases": [
            {"input": "1 1 1 2 2 3\n2", "expected": "[1, 2]", "is_hidden": False},
            {"input": "1 2 2 3 3 3\n2", "expected": "[3, 2]", "is_hidden": False},
            {"input": "4 4 5 5 6\n2", "expected": "[4, 5]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\n#include <algorithm>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def top_k(nums, k):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    int val;
    int freq;
} Pair;

int cmp(const void *a, const void *b) {
    Pair *p1 = (Pair*)a;
    Pair *p2 = (Pair*)b;
    if (p1->freq != p2->freq) return p2->freq - p1->freq;
    return p1->val - p2->val;
}

int main() {
    char token[100];
    int nums[50000];
    int count = 0;
    while (scanf("%s", token) == 1) {
        if (strcmp(token, "/") == 0) continue;
        nums[count++] = atoi(token);
    }
    if (count < 2) return 0;
    int k = nums[count - 1];
    int n = count - 1;

    Pair pairs[5000];
    int np = 0;
    for (int i = 0; i < n; i++) {
        int found = 0;
        for (int j = 0; j < np; j++) {
            if (pairs[j].val == nums[i]) {
                pairs[j].freq++;
                found = 1;
                break;
            }
        }
        if (!found) {
            pairs[np].val = nums[i];
            pairs[np].freq = 1;
            np++;
        }
    }

    qsort(pairs, np, sizeof(Pair), cmp);

    printf("[");
    for (int i = 0; i < k && i < np; i++) {
        printf("%d%s", pairs[i].val, (i == k - 1 || i == np - 1) ? "" : ", ");
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    string token;
    vector<int> nums;
    while (cin >> token) {
        if (token == "/") continue;
        nums.push_back(stoi(token));
    }
    if (nums.size() < 2) return 0;
    int k = nums.back();
    nums.pop_back();

    unordered_map<int, int> freq;
    for (int x : nums) freq[x]++;

    vector<pair<int, int>> items;
    for (auto& p : freq) items.push_back(p);

    sort(items.begin(), items.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        if (a.second != b.second) return a.second > b.second;
        return a.first < b.first;
    });

    cout << "[";
    for (int i = 0; i < k && i < (int)items.size(); i++) {
        cout << items[i].first << (i == k - 1 || i == (int)items.size() - 1 ? "" : ", ");
    }
    cout << "]\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> nums = new ArrayList<>();
        while (sc.hasNext()) {
            String token = sc.next();
            if (token.equals("/")) continue;
            nums.add(Integer.parseInt(token));
        }
        if (nums.size() < 2) return;
        int k = nums.remove(nums.size() - 1);

        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) freq.put(x, freq.getOrDefault(x, 0) + 1);

        List<Integer> keys = new ArrayList<>(freq.keySet());
        keys.sort((a, b) -> {
            int fa = freq.get(a), fb = freq.get(b);
            if (fa != fb) return fb - fa;
            return a - b;
        });

        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < k && i < keys.size(); i++) {
            sb.append(keys.get(i)).append(i == k - 1 || i == keys.size() - 1 ? "" : ", ");
        }
        sb.append("]");
        System.out.println(sb.toString());
    }
}""",
            "python": """import sys

def top_k(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return sorted(freq, key=lambda x: (-freq[x], x))[:k]

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if len(raw) >= 2:
        nums = list(map(int, raw[:-1]))
        k = int(raw[-1])
        print(top_k(nums, k))"""
        })
    },

    # 10. 4Sum II
    {
        "id": "dsa-hash-4sum-ii",
        "problem_num": 145,
        "title": "4Sum II",
        "category": "Hashing",
        "topic": "Hash Maps",
        "subtopic": "Tuple Sum Zero",
        "difficulty": "MEDIUM",
        "description": "Given four integer arrays a, b, c, and d, return the number of tuples (i, j, k, l) such that a[i] + b[j] + c[k] + d[l] == 0.",
        "input_format": "Four lines or token groups representing a, b, c, d.",
        "output_format": "Count of qualifying quadruplets.",
        "constraints": "1 <= a.length, b.length, c.length, d.length <= 200",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)",
        "company_tags": ["Amazon", "Uber"],
        "examples": [
            {"input": "1 2\n-2 -1\n-1 2\n0 2", "output": "2", "explanation": "Tuples (0, 0, 0, 1) and (1, 1, 0, 0)."},
            {"input": "0\n0\n0\n0", "output": "1", "explanation": "Single tuple 0+0+0+0 = 0."},
            {"input": "1\n1\n1\n3", "output": "0", "explanation": "No tuple sums to zero."}
        ],
        "test_cases": [
            {"input": "1 2\n-2 -1\n-1 2\n0 2", "expected": "2", "is_hidden": False},
            {"input": "0\n0\n0\n0", "expected": "1", "is_hidden": False},
            {"input": "1\n1\n1\n3", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def four_sum_count(a, b, c, d):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int a[300], b[300], c[300], d[300];
    int na = 0, nb = 0, nc = 0, nd = 0;
    char line[2000];
    int arr_idx = 0;

    while (arr_idx < 4 && fgets(line, sizeof(line), stdin)) {
        char *tok = strtok(line, " \\t\\r\\n");
        int found = 0;
        while (tok) {
            if (strcmp(tok, "/") == 0) {
                arr_idx++;
            } else {
                found = 1;
                if (arr_idx == 0) a[na++] = atoi(tok);
                else if (arr_idx == 1) b[nb++] = atoi(tok);
                else if (arr_idx == 2) c[nc++] = atoi(tok);
                else if (arr_idx == 3) d[nd++] = atoi(tok);
            }
            tok = strtok(NULL, " \\t\\r\\n");
        }
        if (found) arr_idx++;
    }

    int count = 0;
    for (int i = 0; i < na; i++) {
        for (int j = 0; j < nb; j++) {
            int sumAB = a[i] + b[j];
            for (int k = 0; k < nc; k++) {
                for (int l = 0; l < nd; l++) {
                    if (sumAB + c[k] + d[l] == 0) count++;
                }
            }
        }
    }
    printf("%d\\n", count);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>

using namespace std;

vector<int> parseTokens(const string& line) {
    stringstream ss(line);
    string tok;
    vector<int> res;
    while (ss >> tok) {
        if (tok != "/") res.push_back(stoi(tok));
    }
    return res;
}

int main() {
    string lines[4];
    int idx = 0;
    string line;
    while (idx < 4 && getline(cin, line)) {
        if (line.find('/') != string::npos) {
            stringstream ss(line);
            string segment;
            while (getline(ss, segment, '/')) {
                if (idx < 4) lines[idx++] = segment;
            }
        } else {
            lines[idx++] = line;
        }
    }

    vector<int> a = parseTokens(lines[0]);
    vector<int> b = parseTokens(lines[1]);
    vector<int> c = parseTokens(lines[2]);
    vector<int> d = parseTokens(lines[3]);

    unordered_map<int, int> freq;
    for (int x : a) {
        for (int y : b) freq[x + y]++;
    }

    int count = 0;
    for (int x : c) {
        for (int y : d) {
            auto it = freq.find(-(x + y));
            if (it != freq.end()) count += it->second;
        }
    }
    cout << count << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static List<Integer> parseTokens(String line) {
        List<Integer> res = new ArrayList<>();
        Scanner sc = new Scanner(line);
        while (sc.hasNext()) {
            String s = sc.next();
            if (!s.equals("/")) res.add(Integer.parseInt(s));
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> raw = new ArrayList<>();
        while (sc.hasNextLine() && raw.size() < 4) {
            String line = sc.nextLine();
            if (line.contains("/")) {
                for (String part : line.split("/")) {
                    if (raw.size() < 4) raw.add(part);
                }
            } else {
                raw.add(line);
            }
        }

        List<Integer> a = raw.size() > 0 ? parseTokens(raw.get(0)) : new ArrayList<>();
        List<Integer> b = raw.size() > 1 ? parseTokens(raw.get(1)) : new ArrayList<>();
        List<Integer> c = raw.size() > 2 ? parseTokens(raw.get(2)) : new ArrayList<>();
        List<Integer> d = raw.size() > 3 ? parseTokens(raw.get(3)) : new ArrayList<>();

        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : a) {
            for (int y : b) freq.put(x + y, freq.getOrDefault(x + y, 0) + 1);
        }

        int count = 0;
        for (int x : c) {
            for (int y : d) {
                count += freq.getOrDefault(-(x + y), 0);
            }
        }
        System.out.println(count);
    }
}""",
            "python": """import sys

def four_sum_count(a, b, c, d):
    freq = {}
    for x in a:
        for y in b:
            freq[x + y] = freq.get(x + y, 0) + 1
    count = 0
    for x in c:
        for y in d:
            count += freq.get(-(x + y), 0)
    return count

if __name__ == '__main__':
    content = sys.stdin.read().strip()
    if '/' in content:
        parts = [p.strip() for p in content.split('/') if p.strip()]
    else:
        parts = [l.strip() for l in content.splitlines() if l.strip()]

    a = list(map(int, parts[0].split())) if len(parts) > 0 else []
    b = list(map(int, parts[1].split())) if len(parts) > 1 else []
    c = list(map(int, parts[2].split())) if len(parts) > 2 else []
    d = list(map(int, parts[3].split())) if len(parts) > 3 else []
    print(four_sum_count(a, b, c, d))"""
        })
    },

    # 11. Minimum Window Substring
    {
        "id": "dsa-hash-min-window-substring",
        "problem_num": 146,
        "title": "Minimum Window Substring",
        "category": "Hashing",
        "topic": "Sliding Window",
        "subtopic": "Substring Inclusion",
        "difficulty": "HARD",
        "description": "Find the minimum window substring of s that contains every character in t (including duplicates).",
        "input_format": "Two lines or separated by '/' containing s and t.",
        "output_format": "The minimum window substring, or empty string (\\\"\\\") if none exists.",
        "constraints": "1 <= s.length, t.length <= 10^5",
        "time_complexity": "O(S + T)",
        "space_complexity": "O(S + T)",
        "company_tags": ["Facebook", "Amazon", "LinkedIn", "Google"],
        "examples": [
            {"input": "ADOBECODEBANC\nABC", "output": "BANC", "explanation": "'BANC' contains 'A', 'B', 'C'."},
            {"input": "a\na", "output": "a", "explanation": "Exact match 'a'."},
            {"input": "a\naa", "output": "", "explanation": "'aa' cannot be found in 'a'."}
        ],
        "test_cases": [
            {"input": "ADOBECODEBANC\nABC", "expected": "BANC", "is_hidden": False},
            {"input": "a\na", "expected": "a", "is_hidden": False},
            {"input": "a\naa", "expected": "", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def min_window(s, t):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

int main() {
    char full[10000];
    int flen = fread(full, 1, sizeof(full) - 1, stdin);
    full[flen] = '\\0';

    char s[5000] = "", t[5000] = "";
    char *slash = strchr(full, '/');
    if (slash) {
        *slash = '\\0';
        sscanf(full, "%s", s);
        sscanf(slash + 1, "%s", t);
    } else {
        sscanf(full, "%s %s", s, t);
    }

    int need[256] = {0};
    int t_len = strlen(t);
    for (int i = 0; i < t_len; i++) need[(unsigned char)t[i]]++;

    int missing = t_len;
    int left = 0, start = 0, end = 0;
    int s_len = strlen(s);

    for (int right = 1; right <= s_len; right++) {
        char ch = s[right - 1];
        if (need[(unsigned char)ch] > 0) missing--;
        need[(unsigned char)ch]--;

        if (missing == 0) {
            while (left < right && need[(unsigned char)s[left]] < 0) {
                need[(unsigned char)s[left]]++;
                left++;
            }
            if (end == 0 || right - left < end - start) {
                start = left;
                end = right;
            }
            need[(unsigned char)s[left]]++;
            missing++;
            left++;
        }
    }

    if (end > 0) {
        for (int i = start; i < end; i++) putchar(s[i]);
        putchar('\\n');
    } else {
        printf("\\n");
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string s, t;
    string token;
    vector<string> tokens;
    while (cin >> token) {
        if (token != "/") tokens.push_back(token);
    }
    if (tokens.size() >= 2) {
        s = tokens[0];
        t = tokens[1];
    } else return 0;

    vector<int> need(256, 0);
    for (char ch : t) need[(unsigned char)ch]++;
    int missing = (int)t.length();
    int left = 0, start = 0, end = 0;

    for (int right = 1; right <= (int)s.length(); right++) {
        char ch = s[right - 1];
        if (need[(unsigned char)ch] > 0) missing--;
        need[(unsigned char)ch]--;

        if (missing == 0) {
            while (left < right && need[(unsigned char)s[left]] < 0) {
                need[(unsigned char)s[left]]++;
                left++;
            }
            if (end == 0 || right - left < end - start) {
                start = left;
                end = right;
            }
            need[(unsigned char)s[left]]++;
            missing++;
            left++;
        }
    }

    if (end > 0) cout << s.substr(start, end - start) << "\\n";
    else cout << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> tokens = new ArrayList<>();
        while (sc.hasNext()) {
            String token = sc.next();
            if (!token.equals("/")) tokens.add(token);
        }
        if (tokens.size() < 2) return;
        String s = tokens.get(0);
        String t = tokens.get(1);

        int[] need = new int[256];
        for (char ch : t.toCharArray()) need[ch]++;
        int missing = t.length();
        int left = 0, start = 0, end = 0;

        for (int right = 1; right <= s.length(); right++) {
            char ch = s.charAt(right - 1);
            if (need[ch] > 0) missing--;
            need[ch]--;

            if (missing == 0) {
                while (left < right && need[s.charAt(left)] < 0) {
                    need[s.charAt(left)]++;
                    left++;
                }
                if (end == 0 || right - left < end - start) {
                    start = left;
                    end = right;
                }
                need[s.charAt(left)]++;
                missing++;
                left++;
            }
        }

        if (end > 0) System.out.println(s.substring(start, end));
        else System.out.println();
    }
}""",
            "python": """import sys
from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""
    need = Counter(t)
    missing = len(t)
    left = start = end = 0
    for right, ch in enumerate(s, 1):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if end == 0 or right - left < end - start:
                start, end = left, right
            need[s[left]] += 1
            missing += 1
            left += 1
    return s[start:end]

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if len(raw) >= 2:
        print(min_window(raw[0], raw[1]))"""
        })
    },

    # 12. Count of Smaller Numbers After Self
    {
        "id": "dsa-hash-count-smaller-after-self",
        "problem_num": 147,
        "title": "Count of Smaller Numbers After Self",
        "category": "Hashing",
        "topic": "Divide and Conquer",
        "subtopic": "Inversion Counting",
        "difficulty": "HARD",
        "description": "Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].",
        "input_format": "Space-separated integers.",
        "output_format": "List of smaller counts.",
        "constraints": "1 <= nums.length <= 10^5, -10^4 <= nums[i] <= 10^4",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "company_tags": ["Google", "Amazon"],
        "examples": [
            {"input": "5 2 6 1", "output": "[2, 1, 1, 0]", "explanation": "To right of 5: 2 and 1 (2). Right of 2: 1 (1). Right of 6: 1 (1). Right of 1: none (0)."},
            {"input": "-1", "output": "[0]", "explanation": "Single element has 0 smaller to right."},
            {"input": "-1 -1", "output": "[0, 0]", "explanation": "Equal elements do not count as strictly smaller."}
        ],
        "test_cases": [
            {"input": "5 2 6 1", "expected": "[2, 1, 1, 0]", "is_hidden": False},
            {"input": "-1", "expected": "[0]", "is_hidden": False},
            {"input": "-1 -1", "expected": "[0, 0]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def count_smaller(nums):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int main() {
    int nums[50000];
    int n = 0;
    while (scanf("%d", &nums[n]) == 1) n++;
    if (n == 0) { printf("[]\\n"); return 0; }

    int counts[50000] = {0};
    for (int i = 0; i < n; i++) {
        int sm = 0;
        for (int j = i + 1; j < n; j++) {
            if (nums[j] < nums[i]) sm++;
        }
        counts[i] = sm;
    }

    printf("[");
    for (int i = 0; i < n; i++) {
        printf("%d%s", counts[i], (i == n - 1 ? "" : ", "));
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

int main() {
    int x;
    vector<int> nums;
    while (cin >> x) nums.push_back(x);

    int n = nums.size();
    vector<int> counts(n, 0);
    for (int i = 0; i < n; i++) {
        int sm = 0;
        for (int j = i + 1; j < n; j++) {
            if (nums[j] < nums[i]) sm++;
        }
        counts[i] = sm;
    }

    cout << "[";
    for (int i = 0; i < n; i++) {
        cout << counts[i] << (i == n - 1 ? "" : ", ");
    }
    cout << "]\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> nums = new ArrayList<>();
        while (sc.hasNextInt()) nums.add(sc.nextInt());

        int n = nums.size();
        int[] counts = new int[n];
        for (int i = 0; i < n; i++) {
            int sm = 0;
            for (int j = i + 1; j < n; j++) {
                if (nums.get(j) < nums.get(i)) sm++;
            }
            counts[i] = sm;
        }

        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < n; i++) {
            sb.append(counts[i]).append(i == n - 1 ? "" : ", ");
        }
        sb.append("]");
        System.out.println(sb.toString());
    }
}""",
            "python": """import sys

def count_smaller(nums):
    result = [0] * len(nums)
    arr = list(enumerate(nums))

    def merge_sort(left, right):
        if right - left <= 1:
            return
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid, right)
        temp = []
        i, j = left, mid
        smaller = 0
        while i < mid and j < right:
            if arr[j][1] < arr[i][1]:
                temp.append(arr[j])
                smaller += 1
                j += 1
            else:
                result[arr[i][0]] += smaller
                temp.append(arr[i])
                i += 1
        while i < mid:
            result[arr[i][0]] += smaller
            temp.append(arr[i])
            i += 1
        while j < right:
            temp.append(arr[j])
            j += 1
        arr[left:right] = temp

    merge_sort(0, len(arr))
    return result

if __name__ == '__main__':
    nums = list(map(int, sys.stdin.read().split()))
    if nums:
        print(count_smaller(nums))"""
        })
    },

    # 13. Longest Duplicate Substring
    {
        "id": "dsa-hash-longest-duplicate-substring",
        "problem_num": 148,
        "title": "Longest Duplicate Substring",
        "category": "Hashing",
        "topic": "String Hashing",
        "subtopic": "Rabin-Karp / Substring Search",
        "difficulty": "HARD",
        "description": "Given a string s, consider all duplicated substrings: substrings of s that occur 2 or more times. Return any duplicated substring that has the longest possible length.",
        "input_format": "A single string s.",
        "output_format": "Longest duplicate substring, or empty string if none.",
        "constraints": "2 <= s.length <= 3 * 10^4",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "company_tags": ["Google", "Microsoft"],
        "examples": [
            {"input": "banana", "output": "ana", "explanation": "'ana' appears at index 1 and 3."},
            {"input": "abcd", "output": "", "explanation": "No duplicate substrings."},
            {"input": "aaaaa", "output": "aaaa", "explanation": "'aaaa' appears at index 0 and 1."}
        ],
        "test_cases": [
            {"input": "banana", "expected": "ana", "is_hidden": False},
            {"input": "abcd", "expected": "", "is_hidden": False},
            {"input": "aaaaa", "expected": "aaaa", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def longest_dup(s):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

int main() {
    char s[5000];
    if (scanf("%s", s) != 1) return 0;
    int n = strlen(s);

    for (int len = n - 1; len >= 1; len--) {
        for (int i = 0; i <= n - len; i++) {
            for (int j = i + 1; j <= n - len; j++) {
                if (strncmp(s + i, s + j, len) == 0) {
                    for (int k = 0; k < len; k++) putchar(s[i + k]);
                    putchar('\\n');
                    return 0;
                }
            }
        }
    }
    printf("\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

string longest_dup(const string& s) {
    int n = s.length();
    for (int len = n - 1; len >= 1; len--) {
        unordered_set<string> seen;
        for (int i = 0; i <= n - len; i++) {
            string sub = s.substr(i, len);
            if (seen.count(sub)) return sub;
            seen.insert(sub);
        }
    }
    return "";
}

int main() {
    string s;
    if (cin >> s) {
        cout << longest_dup(s) << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static String longest_dup(String s) {
        int n = s.length();
        for (int len = n - 1; len >= 1; len--) {
            Set<String> seen = new HashSet<>();
            for (int i = 0; i <= n - len; i++) {
                String sub = s.substring(i, i + len);
                if (seen.contains(sub)) return sub;
                seen.add(sub);
            }
        }
        return "";
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            System.out.println(longest_dup(sc.next()));
        }
    }
}""",
            "python": """import sys

def longest_dup(s):
    n = len(s)
    for length in range(n - 1, 0, -1):
        seen = set()
        for i in range(n - length + 1):
            sub = s[i:i + length]
            if sub in seen:
                return sub
            seen.add(sub)
    return ""

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        print(longest_dup(s))"""
        })
    },

    # 14. Substring with Concatenation of All Words
    {
        "id": "dsa-hash-substring-concat-all-words",
        "problem_num": 149,
        "title": "Substring with Concatenation of All Words",
        "category": "Hashing",
        "topic": "Sliding Window",
        "subtopic": "Word Concatenation",
        "difficulty": "HARD",
        "description": "Find all starting indices of substring(s) in s that is a concatenation of each given word of equal length exactly once and without any intervening characters.",
        "input_format": "String s followed by list of words on next line (or separated by '/').",
        "output_format": "List of starting indices.",
        "constraints": "1 <= s.length <= 10^4, 1 <= words.length <= 5000",
        "time_complexity": "O(S * N * W)",
        "space_complexity": "O(N * W)",
        "company_tags": ["Amazon", "Microsoft"],
        "examples": [
            {"input": "barfoothefoobarman\nfoo bar", "output": "[0, 9]", "explanation": "Indices 0 ('barfoo') and 9 ('foobar')."},
            {"input": "wordgoodgoodgoodbestword\nword good best good", "output": "[8]", "explanation": "Only index 8 qualifies."},
            {"input": "barfoofoobarthefoobarman\nbar foo the", "output": "[6, 9, 12]", "explanation": "Valid substrings start at 6, 9, 12."}
        ],
        "test_cases": [
            {"input": "barfoothefoobarman\nfoo bar", "expected": "[0, 9]", "is_hidden": False},
            {"input": "wordgoodgoodgoodbestword\nword good best good", "expected": "[8]", "is_hidden": False},
            {"input": "barfoofoobarthefoobarman\nbar foo the", "expected": "[6, 9, 12]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_map>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def find_substring(s, words):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

int main() {
    char s[5000];
    char words[100][50];
    int nwords = 0;
    char token[100];

    if (scanf("%s", s) != 1) return 0;
    while (scanf("%s", token) == 1) {
        if (strcmp(token, "/") == 0) continue;
        strcpy(words[nwords++], token);
    }
    if (nwords == 0) { printf("[]\\n"); return 0; }

    int word_len = strlen(words[0]);
    int total_len = word_len * nwords;
    int s_len = strlen(s);

    int results[1000];
    int nres = 0;

    for (int i = 0; i <= s_len - total_len; i++) {
        int used[100] = {0};
        int matched = 0;
        for (int j = 0; j < nwords; j++) {
            char sub[50];
            strncpy(sub, s + i + j * word_len, word_len);
            sub[word_len] = '\\0';

            int found = 0;
            for (int k = 0; k < nwords; k++) {
                if (!used[k] && strcmp(words[k], sub) == 0) {
                    used[k] = 1;
                    matched++;
                    found = 1;
                    break;
                }
            }
            if (!found) break;
        }
        if (matched == nwords) results[nres++] = i;
    }

    printf("[");
    for (int i = 0; i < nres; i++) {
        printf("%d%s", results[i], (i == nres - 1 ? "" : ", "));
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    string s;
    if (!(cin >> s)) return 0;

    vector<string> words;
    string w;
    while (cin >> w) {
        if (w != "/") words.push_back(w);
    }
    if (words.empty()) { cout << "[]\\n"; return 0; }

    int word_len = words[0].length();
    int total_len = word_len * words.size();
    int s_len = s.length();

    unordered_map<string, int> need;
    for (const string& word : words) need[word]++;

    vector<int> result;
    for (int i = 0; i <= s_len - total_len; i++) {
        unordered_map<string, int> seen;
        int matched = 0;
        for (size_t j = 0; j < words.size(); j++) {
            string sub = s.substr(i + j * word_len, word_len);
            if (need.find(sub) != need.end()) {
                seen[sub]++;
                if (seen[sub] > need[sub]) break;
                matched++;
            } else {
                break;
            }
        }
        if (matched == (int)words.size()) result.push_back(i);
    }

    cout << "[";
    for (size_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : ", ");
    }
    cout << "]\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String s = sc.next();
        List<String> words = new ArrayList<>();
        while (sc.hasNext()) {
            String token = sc.next();
            if (!token.equals("/")) words.add(token);
        }
        if (words.isEmpty()) { System.out.println("[]"); return; }

        int wordLen = words.get(0).length();
        int totalLen = wordLen * words.size();
        Map<String, Integer> need = new HashMap<>();
        for (String w : words) need.put(w, need.getOrDefault(w, 0) + 1);

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i <= s.length() - totalLen; i++) {
            Map<String, Integer> seen = new HashMap<>();
            int matched = 0;
            for (int j = 0; j < words.size(); j++) {
                String sub = s.substring(i + j * wordLen, i + (j + 1) * wordLen);
                if (need.containsKey(sub)) {
                    seen.put(sub, seen.getOrDefault(sub, 0) + 1);
                    if (seen.get(sub) > need.get(sub)) break;
                    matched++;
                } else {
                    break;
                }
            }
            if (matched == words.size()) result.add(i);
        }

        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < result.size(); i++) {
            sb.append(result.get(i)).append(i == result.size() - 1 ? "" : ", ");
        }
        sb.append("]");
        System.out.println(sb.toString());
    }
}""",
            "python": """import sys
from collections import Counter

def find_substring(s, words):
    if not words:
        return []
    word_len = len(words[0])
    total_len = word_len * len(words)
    need = Counter(words)
    result = []
    for i in range(len(s) - total_len + 1):
        parts = [s[j:j + word_len] for j in range(i, i + total_len, word_len)]
        if Counter(parts) == need:
            result.append(i)
    return result

if __name__ == '__main__':
    raw = sys.stdin.read().replace('/', ' ').split()
    if raw:
        s = raw[0]
        words = raw[1:]
        print(find_substring(s, words))"""
        })
    },

    # 15. Distinct Echo Substrings
    {
        "id": "dsa-hash-distinct-echo-substrings",
        "problem_num": 150,
        "title": "Distinct Echo Substrings",
        "category": "Hashing",
        "topic": "String Hashing",
        "subtopic": "Echo Substring Count",
        "difficulty": "HARD",
        "description": "Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself (e.g. 'abcabc').",
        "input_format": "A single string s.",
        "output_format": "Count of distinct echo substrings.",
        "constraints": "1 <= s.length <= 2000",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)",
        "company_tags": ["Google", "Amazon"],
        "examples": [
            {"input": "abcabcabc", "output": "3", "explanation": "'abcabc', 'bcabca', and 'cabcab'."},
            {"input": "leetcodeleetcode", "output": "2", "explanation": "'ee' and 'leetcodeleetcode'."},
            {"input": "aaaa", "output": "2", "explanation": "'aa' and 'aaaa'."}
        ],
        "test_cases": [
            {"input": "abcabcabc", "expected": "3", "is_hidden": False},
            {"input": "leetcodeleetcode", "expected": "2", "is_hidden": False},
            {"input": "aaaa", "expected": "2", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n#include <unordered_set>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def distinct_echo(s):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

int main() {
    char s[3000];
    if (scanf("%s", s) != 1) return 0;
    int n = strlen(s);

    char echo_list[3000][200];
    int count = 0;

    for (int len = 1; len <= n / 2; len++) {
        for (int i = 0; i <= n - 2 * len; i++) {
            if (strncmp(s + i, s + i + len, len) == 0) {
                char candidate[200];
                strncpy(candidate, s + i, 2 * len);
                candidate[2 * len] = '\\0';

                int already = 0;
                for (int k = 0; k < count; k++) {
                    if (strcmp(echo_list[k], candidate) == 0) {
                        already = 1;
                        break;
                    }
                }
                if (!already) strcpy(echo_list[count++], candidate);
            }
        }
    }
    printf("%d\\n", count);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

int main() {
    string s;
    if (cin >> s) {
        int n = s.length();
        unordered_set<string> result;
        for (int len = 1; len <= n / 2; len++) {
            for (int i = 0; i <= n - 2 * len; i++) {
                if (s.compare(i, len, s, i + len, len) == 0) {
                    result.insert(s.substr(i, 2 * len));
                }
            }
        }
        cout << result.size() << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            int n = s.length();
            Set<String> result = new HashSet<>();
            for (int len = 1; len <= n / 2; len++) {
                for (int i = 0; i <= n - 2 * len; i++) {
                    String first = s.substring(i, i + len);
                    String second = s.substring(i + len, i + 2 * len);
                    if (first.equals(second)) {
                        result.add(first + second);
                    }
                }
            }
            System.out.println(result.size());
        }
    }
}""",
            "python": """import sys

def distinct_echo(s):
    result = set()
    n = len(s)
    for length in range(1, n // 2 + 1):
        for i in range(n - 2 * length + 1):
            first = s[i:i + length]
            second = s[i + length:i + 2 * length]
            if first == second:
                result.add(first + second)
    return len(result)

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        print(distinct_echo(s))"""
        })
    }
]

problems.extend(hash_data)

with open("backend/app/data/dsa_problems_seed.json", "w", encoding="utf-8") as f:
    json.dump(problems, f, indent=2)

print(f"Successfully added 15 Hashing problems! Total problems: {len(problems)}")

