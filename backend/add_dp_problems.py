import sys, os
sys.path.insert(0, os.path.abspath('.'))
import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    problems = json.load(f)

dp_ids = {
    "dsa-dp-fibonacci", "dsa-dp-climbing-stairs", "dsa-dp-min-cost-climbing-stairs",
    "dsa-dp-house-robber", "dsa-dp-kadane", "dsa-dp-coin-change", "dsa-dp-01-knapsack",
    "dsa-dp-lcs", "dsa-dp-lis", "dsa-dp-unique-paths", "dsa-dp-edit-distance",
    "dsa-dp-matrix-chain", "dsa-dp-word-break", "dsa-dp-partition-equal-subset", "dsa-dp-burst-balloons"
}
problems = [p for p in problems if p["id"] not in dp_ids]

dp_data = [
    # 16. Fibonacci Number
    {
        "id": "dsa-dp-fibonacci",
        "problem_num": 181,
        "title": "Fibonacci Number",
        "category": "Dynamic Programming",
        "topic": "1D DP",
        "subtopic": "Basic Recurrence",
        "difficulty": "EASY",
        "description": "Find the Nth Fibonacci number using Dynamic Programming.",
        "input_format": "A single non-negative integer N.",
        "output_format": "The Nth Fibonacci number.",
        "constraints": "0 <= N <= 30",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Microsoft", "Apple", "Facebook"],
        "examples": [
            {"input": "5", "output": "5", "explanation": "F(5) = F(4) + F(3) = 3 + 2 = 5."},
            {"input": "7", "output": "13", "explanation": "F(7) = 13."},
            {"input": "0", "output": "0", "explanation": "F(0) = 0."}
        ],
        "test_cases": [
            {"input": "5", "expected": "5", "is_hidden": False},
            {"input": "7", "expected": "13", "is_hidden": False},
            {"input": "0", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def fibonacci(n):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int fibonacci(int n) {
    if (n <= 1) return n;
    int dp[35];
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        printf("%d\\n", fibonacci(n));
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

int fibonacci(int n) {
    if (n <= 1) return n;
    vector<int> dp(n + 1, 0);
    dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}

int main() {
    int n;
    if (cin >> n) {
        cout << fibonacci(n) << endl;
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int fibonacci(int n) {
        if (n <= 1) return n;
        int[] dp = new int[n + 1];
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            System.out.println(fibonacci(n));
        }
    }
}""",
            "python": """import sys

def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

if __name__ == '__main__':
    data = sys.stdin.read().strip()
    if data:
        n = int(data)
        print(fibonacci(n))"""
        })
    },

    # 17. Climbing Stairs
    {
        "id": "dsa-dp-climbing-stairs",
        "problem_num": 182,
        "title": "Climbing Stairs",
        "category": "Dynamic Programming",
        "topic": "1D DP",
        "subtopic": "Fibonacci Variations",
        "difficulty": "EASY",
        "description": "You can climb either one or two steps at a time. Find the number of different ways to reach step N.",
        "input_format": "A single integer N.",
        "output_format": "Total number of distinct ways to climb to the top.",
        "constraints": "1 <= N <= 45",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Google", "Apple", "Microsoft"],
        "examples": [
            {"input": "2", "output": "2", "explanation": "Ways: (1+1) and (2)."},
            {"input": "3", "output": "3", "explanation": "Ways: (1+1+1), (1+2), (2+1)."},
            {"input": "5", "output": "8", "explanation": "8 distinct combinations."}
        ],
        "test_cases": [
            {"input": "2", "expected": "2", "is_hidden": False},
            {"input": "3", "expected": "3", "is_hidden": False},
            {"input": "5", "expected": "8", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def climb_stairs(n):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int climb_stairs(int n) {
    if (n <= 2) return n;
    int dp[50];
    dp[1] = 1;
    dp[2] = 2;
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        printf("%d\\n", climb_stairs(n));
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

int climb_stairs(int n) {
    if (n <= 2) return n;
    vector<int> dp(n + 1);
    dp[1] = 1;
    dp[2] = 2;
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}

int main() {
    int n;
    if (cin >> n) {
        cout << climb_stairs(n) << endl;
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int climbStairs(int n) {
        if (n <= 2) return n;
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            System.out.println(climbStairs(n));
        }
    }
}""",
            "python": """import sys

def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

if __name__ == '__main__':
    data = sys.stdin.read().strip()
    if data:
        n = int(data)
        print(climb_stairs(n))"""
        })
    },

    # 18. Minimum Cost Climbing Stairs
    {
        "id": "dsa-dp-min-cost-climbing-stairs",
        "problem_num": 183,
        "title": "Minimum Cost Climbing Stairs",
        "category": "Dynamic Programming",
        "topic": "1D DP",
        "subtopic": "Cost Optimization",
        "difficulty": "EASY",
        "description": "Each stair has a cost. Find the minimum cost to reach beyond the last stair. You can start from step 0 or step 1.",
        "input_format": "Space-separated list of stair costs.",
        "output_format": "Minimum cost to reach the top floor.",
        "constraints": "2 <= cost.length <= 1000, 0 <= cost[i] <= 999",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Apple", "Bloomberg"],
        "examples": [
            {"input": "10 15 20", "output": "15", "explanation": "Start at index 1 with cost 15, then take two steps to reach the top."},
            {"input": "1 100 1 1 1 100 1 1 100 1", "output": "6", "explanation": "Step through low cost stairs to minimize total sum."},
            {"input": "5 10", "output": "5", "explanation": "Start at index 0 and jump two steps."}
        ],
        "test_cases": [
            {"input": "10 15 20", "expected": "15", "is_hidden": False},
            {"input": "1 100 1 1 1 100 1 1 100 1", "expected": "6", "is_hidden": False},
            {"input": "5 10", "expected": "5", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def min_cost(cost):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

int min_cost(int cost[], int n) {
    int dp[1005];
    dp[0] = 0;
    dp[1] = 0;
    for (int i = 2; i <= n; i++) {
        int a = dp[i - 1] + cost[i - 1];
        int b = dp[i - 2] + cost[i - 2];
        dp[i] = (a < b) ? a : b;
    }
    return dp[n];
}

int main() {
    int cost[1005];
    int n = 0;
    while (scanf("%d", &cost[n]) == 1) {
        n++;
    }
    printf("%d\\n", min_cost(cost, n));
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int min_cost(const vector<int>& cost) {
    int n = cost.size();
    vector<int> dp(n + 1, 0);
    for (int i = 2; i <= n; i++) {
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
    }
    return dp[n];
}

int main() {
    vector<int> cost;
    int val;
    while (cin >> val) {
        cost.push_back(val);
    }
    cout << min_cost(cost) << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int minCost(int[] cost) {
        int n = cost.length;
        int[] dp = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            dp[i] = Math.min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) {
            list.add(sc.nextInt());
        }
        int[] cost = new int[list.size()];
        for (int i = 0; i < list.size(); i++) cost[i] = list.get(i);
        System.out.println(minCost(cost));
    }
}""",
            "python": """import sys

def min_cost(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(
            dp[i - 1] + cost[i - 1],
            dp[i - 2] + cost[i - 2]
        )
    return dp[n]

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        cost = list(map(int, tokens))
        print(min_cost(cost))"""
        })
    },

    # 19. House Robber
    {
        "id": "dsa-dp-house-robber",
        "problem_num": 184,
        "title": "House Robber",
        "category": "Dynamic Programming",
        "topic": "1D DP",
        "subtopic": "Non-Adjacent Choices",
        "difficulty": "EASY",
        "description": "Find the maximum amount of money you can rob without robbing two adjacent houses.",
        "input_format": "Space-separated list of house values.",
        "output_format": "Maximum stolen amount.",
        "constraints": "1 <= nums.length <= 1000, 0 <= nums[i] <= 1000",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "company_tags": ["Amazon", "Google", "Microsoft", "LinkedIn"],
        "examples": [
            {"input": "1 2 3 1", "output": "4", "explanation": "Rob house 1 (money 1) and house 3 (money 3). Total = 4."},
            {"input": "2 7 9 3 1", "output": "12", "explanation": "Rob house 1 (2), house 3 (9), house 5 (1). Total = 12."},
            {"input": "2 1 1 2", "output": "4", "explanation": "Rob house 1 (2) and house 4 (2). Total = 4."}
        ],
        "test_cases": [
            {"input": "1 2 3 1", "expected": "4", "is_hidden": False},
            {"input": "2 7 9 3 1", "expected": "12", "is_hidden": False},
            {"input": "2 1 1 2", "expected": "4", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def rob(nums):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int rob(int nums[], int n) {
    int prev1 = 0, prev2 = 0;
    for (int i = 0; i < n; i++) {
        int val = prev2 + nums[i];
        int current = (prev1 > val) ? prev1 : val;
        prev2 = prev1;
        prev1 = current;
    }
    return prev1;
}

int main() {
    int nums[1005];
    int n = 0;
    while (scanf("%d", &nums[n]) == 1) {
        n++;
    }
    printf("%d\\n", rob(nums, n));
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int rob(const vector<int>& nums) {
    int prev1 = 0, prev2 = 0;
    for (int num : nums) {
        int current = max(prev1, prev2 + num);
        prev2 = prev1;
        prev1 = current;
    }
    return prev1;
}

int main() {
    vector<int> nums;
    int val;
    while (cin >> val) {
        nums.push_back(val);
    }
    cout << rob(nums) << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int rob(int[] nums) {
        int prev1 = 0, prev2 = 0;
        for (int num : nums) {
            int current = Math.max(prev1, prev2 + num);
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) {
            list.add(sc.nextInt());
        }
        int[] nums = new int[list.size()];
        for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);
        System.out.println(rob(nums));
    }
}""",
            "python": """import sys

def rob(nums):
    prev1 = 0
    prev2 = 0
    for num in nums:
        current = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = current
    return prev1

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        nums = list(map(int, tokens))
        print(rob(nums))"""
        })
    },

    # 20. Maximum Subarray Sum – Kadane's Algorithm
    {
        "id": "dsa-dp-kadane",
        "problem_num": 185,
        "title": "Maximum Subarray Sum – Kadane's Algorithm",
        "category": "Dynamic Programming",
        "topic": "Kadane's Algorithm",
        "subtopic": "Max Subarray",
        "difficulty": "EASY",
        "description": "Find the maximum sum of a contiguous subarray.",
        "input_format": "Space-separated array of integers.",
        "output_format": "The maximum contiguous subarray sum.",
        "constraints": "1 <= nums.length <= 10^5, -10^4 <= nums[i] <= 10^4",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "company_tags": ["Amazon", "Microsoft", "Google", "Apple", "LinkedIn"],
        "examples": [
            {"input": "-2 1 -3 4 -1 2 1 -5 4", "output": "6", "explanation": "The subarray [4, -1, 2, 1] has the largest sum = 6."},
            {"input": "1", "output": "1", "explanation": "Single element array."},
            {"input": "5 4 -1 7 8", "output": "23", "explanation": "Entire array sums to 23."}
        ],
        "test_cases": [
            {"input": "-2 1 -3 4 -1 2 1 -5 4", "expected": "6", "is_hidden": False},
            {"input": "1", "expected": "1", "is_hidden": False},
            {"input": "5 4 -1 7 8", "expected": "23", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def max_subarray(nums):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int max_subarray(int nums[], int n) {
    int current = nums[0];
    int maximum = nums[0];
    for (int i = 1; i < n; i++) {
        int sum = current + nums[i];
        current = (nums[i] > sum) ? nums[i] : sum;
        if (current > maximum) maximum = current;
    }
    return maximum;
}

int main() {
    int nums[100005];
    int n = 0;
    while (scanf("%d", &nums[n]) == 1) {
        n++;
    }
    printf("%d\\n", max_subarray(nums, n));
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int max_subarray(const vector<int>& nums) {
    int current = nums[0];
    int maximum = nums[0];
    for (size_t i = 1; i < nums.size(); i++) {
        current = max(nums[i], current + nums[i]);
        maximum = max(maximum, current);
    }
    return maximum;
}

int main() {
    vector<int> nums;
    int val;
    while (cin >> val) {
        nums.push_back(val);
    }
    cout << max_subarray(nums) << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int maxSubArray(int[] nums) {
        int current = nums[0];
        int maximum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            current = Math.max(nums[i], current + nums[i]);
            maximum = Math.max(maximum, current);
        }
        return maximum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) {
            list.add(sc.nextInt());
        }
        int[] nums = new int[list.size()];
        for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);
        System.out.println(maxSubArray(nums));
    }
}""",
            "python": """import sys

def max_subarray(nums):
    current = nums[0]
    maximum = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        maximum = max(maximum, current)
    return maximum

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        nums = list(map(int, tokens))
        print(max_subarray(nums))"""
        })
    },

    # 21. Coin Change
    {
        "id": "dsa-dp-coin-change",
        "problem_num": 186,
        "title": "Coin Change",
        "category": "Dynamic Programming",
        "topic": "Knapsack Variations",
        "subtopic": "Unbounded Knapsack",
        "difficulty": "MEDIUM",
        "description": "Find the minimum number of coins required to make a given amount. Return -1 if impossible.",
        "input_format": "List of coin denominations followed by the target amount.",
        "output_format": "Minimum number of coins, or -1 if impossible.",
        "constraints": "1 <= coins.length <= 12, 1 <= coins[i] <= 2^31 - 1, 0 <= amount <= 10^4",
        "time_complexity": "O(amount * N)",
        "space_complexity": "O(amount)",
        "company_tags": ["Amazon", "Google", "Microsoft", "Bloomberg"],
        "examples": [
            {"input": "1 2 5 / 11", "output": "3", "explanation": "11 = 5 + 5 + 1 (3 coins)."},
            {"input": "2 / 3", "output": "-1", "explanation": "Cannot form 3 using only coin of 2."},
            {"input": "1 / 0", "output": "0", "explanation": "0 coins needed for amount 0."}
        ],
        "test_cases": [
            {"input": "1 2 5 / 11", "expected": "3", "is_hidden": False},
            {"input": "2 / 3", "expected": "-1", "is_hidden": False},
            {"input": "1 / 0", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def coin_change(coins, amount):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INF 1000000000

int main() {
    char token[100];
    int coins[100];
    int numCoins = 0;
    int amount = 0;

    int slashSeen = 0;
    while (scanf("%s", token) == 1) {
        if (strcmp(token, "/") == 0) {
            slashSeen = 1;
            continue;
        }
        if (slashSeen) {
            amount = atoi(token);
        } else {
            coins[numCoins++] = atoi(token);
        }
    }

    if (!slashSeen && numCoins > 1) {
        amount = coins[numCoins - 1];
        numCoins--;
    }

    int dp[10005];
    for (int i = 0; i <= amount; i++) dp[i] = INF;
    dp[0] = 0;

    for (int i = 1; i <= amount; i++) {
        for (int j = 0; j < numCoins; j++) {
            if (i >= coins[j]) {
                if (dp[i - coins[j]] != INF && dp[i - coins[j]] + 1 < dp[i]) {
                    dp[i] = dp[i - coins[j]] + 1;
                }
            }
        }
    }

    printf("%d\\n", dp[amount] == INF ? -1 : dp[amount]);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
    string token;
    vector<int> coins;
    int amount = 0;
    bool slashSeen = false;

    while (cin >> token) {
        if (token == "/") {
            slashSeen = true;
            continue;
        }
        if (slashSeen) {
            amount = stoi(token);
        } else {
            coins.push_back(stoi(token));
        }
    }

    if (!slashSeen && coins.size() > 1) {
        amount = coins.back();
        coins.pop_back();
    }

    vector<int> dp(amount + 1, INF);
    dp[0] = 0;

    for (int i = 1; i <= amount; i++) {
        for (int coin : coins) {
            if (i >= coin && dp[i - coin] != INF) {
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }
    }

    cout << (dp[amount] == INF ? -1 : dp[amount]) << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> coins = new ArrayList<>();
        int amount = 0;
        boolean slashSeen = false;

        while (sc.hasNext()) {
            String token = sc.next();
            if (token.equals("/")) {
                slashSeen = true;
                continue;
            }
            if (slashSeen) {
                amount = Integer.parseInt(token);
            } else {
                coins.add(Integer.parseInt(token));
            }
        }

        if (!slashSeen && coins.size() > 1) {
            amount = coins.remove(coins.size() - 1);
        }

        int INF = 1_000_000_000;
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i >= coin && dp[i - coin] != INF) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        System.out.println(dp[amount] == INF ? -1 : dp[amount]);
    }
}""",
            "python": """import sys

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[amount] == float('inf') else dp[amount]

if __name__ == '__main__':
    text = sys.stdin.read().strip()
    if text:
        if '/' in text:
            parts = text.split('/')
            coins = list(map(int, parts[0].split()))
            amount = int(parts[1].strip())
        else:
            tokens = list(map(int, text.split()))
            coins = tokens[:-1]
            amount = tokens[-1]
        print(coin_change(coins, amount))"""
        })
    },

    # 22. 0/1 Knapsack Problem
    {
        "id": "dsa-dp-01-knapsack",
        "problem_num": 187,
        "title": "0/1 Knapsack Problem",
        "category": "Dynamic Programming",
        "topic": "Knapsack",
        "subtopic": "0/1 Knapsack",
        "difficulty": "MEDIUM",
        "description": "Given weights and values of items, find the maximum value that can fit into a bag of capacity W. Each item can be selected at most once.",
        "input_format": "Weights list, values list, and capacity separated by slashes or newlines.",
        "output_format": "Maximum value within capacity.",
        "constraints": "1 <= N <= 100, 1 <= capacity <= 1000",
        "time_complexity": "O(N * W)",
        "space_complexity": "O(W)",
        "company_tags": ["Amazon", "Google", "Microsoft"],
        "examples": [
            {"input": "1 2 3 / 6 10 12 / 5", "output": "22", "explanation": "Pick items 2 (wt 2, val 10) and 3 (wt 3, val 12). Total weight 5, max value 22."},
            {"input": "2 3 4 5 / 3 4 5 6 / 5", "output": "7", "explanation": "Pick items with weights 2 and 3 for value 3 + 4 = 7."},
            {"input": "1 2 / 10 20 / 0", "output": "0", "explanation": "Bag capacity is 0."}
        ],
        "test_cases": [
            {"input": "1 2 3 / 6 10 12 / 5", "expected": "22", "is_hidden": False},
            {"input": "2 3 4 5 / 3 4 5 6 / 5", "expected": "7", "is_hidden": False},
            {"input": "1 2 / 10 20 / 0", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def knapsack(weights, values, capacity):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char token[100];
    int weights[1000], values[1000];
    int n_w = 0, n_v = 0, capacity = 0;
    int section = 0;

    while (scanf("%s", token) == 1) {
        if (strcmp(token, "/") == 0) {
            section++;
            continue;
        }
        if (section == 0) {
            weights[n_w++] = atoi(token);
        } else if (section == 1) {
            values[n_v++] = atoi(token);
        } else if (section == 2) {
            capacity = atoi(token);
        }
    }

    int dp[1005] = {0};
    for (int i = 0; i < n_w; i++) {
        for (int w = capacity; w >= weights[i]; w--) {
            int val = values[i] + dp[w - weights[i]];
            if (val > dp[w]) dp[w] = val;
        }
    }

    printf("%d\\n", dp[capacity]);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int main() {
    string input, full;
    while (getline(cin, input)) {
        full += input + " ";
    }

    vector<string> parts;
    stringstream ss(full);
    string segment;
    while (getline(ss, segment, '/')) {
        parts.push_back(segment);
    }

    vector<int> weights, values;
    int capacity = 0;

    if (parts.size() >= 1) {
        stringstream s1(parts[0]);
        int val;
        while (s1 >> val) weights.push_back(val);
    }
    if (parts.size() >= 2) {
        stringstream s2(parts[1]);
        int val;
        while (s2 >> val) values.push_back(val);
    }
    if (parts.size() >= 3) {
        stringstream s3(parts[2]);
        s3 >> capacity;
    }

    vector<int> dp(capacity + 1, 0);
    for (size_t i = 0; i < weights.size(); i++) {
        for (int w = capacity; w >= weights[i]; w--) {
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]]);
        }
    }

    cout << dp[capacity] << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        while (sc.hasNextLine()) {
            sb.append(sc.nextLine()).append(" ");
        }
        String full = sb.toString();
        String[] parts = full.split("/");

        List<Integer> weights = new ArrayList<>();
        List<Integer> values = new ArrayList<>();
        int capacity = 0;

        if (parts.length >= 1) {
            Scanner s1 = new Scanner(parts[0]);
            while (s1.hasNextInt()) weights.add(s1.nextInt());
        }
        if (parts.length >= 2) {
            Scanner s2 = new Scanner(parts[1]);
            while (s2.hasNextInt()) values.add(s2.nextInt());
        }
        if (parts.length >= 3) {
            Scanner s3 = new Scanner(parts[2]);
            if (s3.hasNextInt()) capacity = s3.nextInt();
        }

        int[] dp = new int[capacity + 1];
        for (int i = 0; i < weights.size(); i++) {
            int wt = weights.get(i);
            int val = values.get(i);
            for (int w = capacity; w >= wt; w--) {
                dp[w] = Math.max(dp[w], val + dp[w - wt]);
            }
        }

        System.out.println(dp[capacity]);
    }
}""",
            "python": """import sys

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(
                dp[w],
                values[i] + dp[w - weights[i]]
            )
    return dp[capacity]

if __name__ == '__main__':
    text = sys.stdin.read().strip()
    if text:
        parts = text.split('/')
        weights = list(map(int, parts[0].split()))
        values = list(map(int, parts[1].split()))
        capacity = int(parts[2].strip())
        print(knapsack(weights, values, capacity))"""
        })
    },

    # 23. Longest Common Subsequence
    {
        "id": "dsa-dp-lcs",
        "problem_num": 188,
        "title": "Longest Common Subsequence",
        "category": "Dynamic Programming",
        "topic": "String DP",
        "subtopic": "2D Grid DP",
        "difficulty": "MEDIUM",
        "description": "Find the length of the longest subsequence common to two strings. Characters must appear in the same relative order, but need not be continuous.",
        "input_format": "Two strings separated by a slash or on separate lines.",
        "output_format": "Length of the longest common subsequence.",
        "constraints": "1 <= text1.length, text2.length <= 1000",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(M * N)",
        "company_tags": ["Amazon", "Google", "Microsoft", "Facebook"],
        "examples": [
            {"input": "abcde / ace", "output": "3", "explanation": "The longest common subsequence is 'ace' and its length is 3."},
            {"input": "abc / abc", "output": "3", "explanation": "Identical strings match completely."},
            {"input": "abc / def", "output": "0", "explanation": "No common characters."}
        ],
        "test_cases": [
            {"input": "abcde / ace", "expected": "3", "is_hidden": False},
            {"input": "abc / abc", "expected": "3", "is_hidden": False},
            {"input": "abc / def", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def lcs(a, b):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

int dp[1005][1005];

int main() {
    char token[1005];
    char a[1005] = "", b[1005] = "";

    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    strcpy(a, token);
    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    strcpy(b, token);

    int m = strlen(a);
    int n = strlen(b);

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (a[i - 1] == b[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = (dp[i - 1][j] > dp[i][j - 1]) ? dp[i - 1][j] : dp[i][j - 1];
            }
        }
    }

    printf("%d\\n", dp[m][n]);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    string a, b, token;
    vector<string> tokens;
    while (cin >> token) {
        if (token != "/") tokens.push_back(token);
    }
    if (tokens.size() >= 2) {
        a = tokens[0];
        b = tokens[1];
    }

    int m = a.length(), n = b.length();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (a[i - 1] == b[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    cout << dp[m][n] << endl;
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
        if (tokens.size() < 2) {
            System.out.println(0);
            return;
        }
        String a = tokens.get(0);
        String b = tokens.get(1);

        int m = a.length();
        int n = b.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (a.charAt(i - 1) == b.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        System.out.println(dp[m][n]);
    }
}""",
            "python": """import sys

def lcs(a, b):
    m = len(a)
    n = len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[m][n]

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if len(tokens) >= 2:
        print(lcs(tokens[0], tokens[1]))
    else:
        print(0)"""
        })
    },

    # 24. Longest Increasing Subsequence
    {
        "id": "dsa-dp-lis",
        "problem_num": 189,
        "title": "Longest Increasing Subsequence",
        "category": "Dynamic Programming",
        "topic": "1D DP",
        "subtopic": "Subsequence DP",
        "difficulty": "MEDIUM",
        "description": "Find the length of the longest strictly increasing subsequence in an array.",
        "input_format": "Space-separated array of integers.",
        "output_format": "Length of the longest strictly increasing subsequence.",
        "constraints": "1 <= nums.length <= 2500, -10^4 <= nums[i] <= 10^4",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Google", "Microsoft", "Apple"],
        "examples": [
            {"input": "10 9 2 5 3 7 101 18", "output": "4", "explanation": "The longest increasing subsequence is [2, 3, 7, 101], length 4."},
            {"input": "0 1 0 3 2 3", "output": "4", "explanation": "Subsequence [0, 1, 2, 3] has length 4."},
            {"input": "7 7 7 7", "output": "1", "explanation": "Strictly increasing requires strictly greater elements."}
        ],
        "test_cases": [
            {"input": "10 9 2 5 3 7 101 18", "expected": "4", "is_hidden": False},
            {"input": "0 1 0 3 2 3", "expected": "4", "is_hidden": False},
            {"input": "7 7 7 7", "expected": "1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def lis(nums):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int lis(int nums[], int n) {
    if (n == 0) return 0;
    int dp[2505];
    int max_len = 1;
    for (int i = 0; i < n; i++) {
        dp[i] = 1;
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                if (dp[j] + 1 > dp[i]) dp[i] = dp[j] + 1;
            }
        }
        if (dp[i] > max_len) max_len = dp[i];
    }
    return max_len;
}

int main() {
    int nums[2505];
    int n = 0;
    while (scanf("%d", &nums[n]) == 1) {
        n++;
    }
    printf("%d\\n", lis(nums, n));
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int lis(const vector<int>& nums) {
    if (nums.empty()) return 0;
    vector<int> dp(nums.size(), 1);
    int max_len = 1;
    for (size_t i = 0; i < nums.size(); i++) {
        for (size_t j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        max_len = max(max_len, dp[i]);
    }
    return max_len;
}

int main() {
    vector<int> nums;
    int val;
    while (cin >> val) nums.push_back(val);
    cout << lis(nums) << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int lis(int[] nums) {
        if (nums.length == 0) return 0;
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        int maxLen = 1;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxLen = Math.max(maxLen, dp[i]);
        }
        return maxLen;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] nums = new int[list.size()];
        for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);
        System.out.println(lis(nums));
    }
}""",
            "python": """import sys

def lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        nums = list(map(int, tokens))
        print(lis(nums))"""
        })
    },

    # 25. Unique Paths
    {
        "id": "dsa-dp-unique-paths",
        "problem_num": 190,
        "title": "Unique Paths",
        "category": "Dynamic Programming",
        "topic": "Grid DP",
        "subtopic": "Combinatorial Grid",
        "difficulty": "MEDIUM",
        "description": "A robot starts at the top-left corner of an M x N grid. It can move only right or down. Find the number of ways to reach the bottom-right corner.",
        "input_format": "Two integers M and N.",
        "output_format": "Number of unique paths.",
        "constraints": "1 <= M, N <= 100",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(M * N)",
        "company_tags": ["Amazon", "Google", "Bloomberg", "Facebook"],
        "examples": [
            {"input": "3 7", "output": "28", "explanation": "28 unique paths in a 3x7 grid."},
            {"input": "3 2", "output": "3", "explanation": "Three paths: Right->Down->Down, Down->Right->Down, Down->Down->Right."},
            {"input": "1 1", "output": "1", "explanation": "Already at destination."}
        ],
        "test_cases": [
            {"input": "3 7", "expected": "28", "is_hidden": False},
            {"input": "3 2", "expected": "3", "is_hidden": False},
            {"input": "1 1", "expected": "1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def unique_paths(m, n):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int unique_paths(int m, int n) {
    long long dp[105][105];
    for (int i = 0; i < m; i++) dp[i][0] = 1;
    for (int j = 0; j < n; j++) dp[0][j] = 1;

    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }
    return (int)dp[m - 1][n - 1];
}

int main() {
    int m, n;
    if (scanf("%d %d", &m, &n) == 2) {
        printf("%d\\n", unique_paths(m, n));
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

int unique_paths(int m, int n) {
    vector<vector<int>> dp(m, vector<int>(n, 1));
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }
    return dp[m - 1][n - 1];
}

int main() {
    int m, n;
    if (cin >> m >> n) {
        cout << unique_paths(m, n) << endl;
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) dp[i][0] = 1;
        for (int j = 0; j < n; j++) dp[0][j] = 1;

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m - 1][n - 1];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            int n = sc.nextInt();
            System.out.println(uniquePaths(m, n));
        }
    }
}""",
            "python": """import sys

def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if len(tokens) >= 2:
        m, n = int(tokens[0]), int(tokens[1])
        print(unique_paths(m, n))"""
        })
    },

    # 26. Edit Distance
    {
        "id": "dsa-dp-edit-distance",
        "problem_num": 191,
        "title": "Edit Distance",
        "category": "Dynamic Programming",
        "topic": "String DP",
        "subtopic": "Levenshtein Distance",
        "difficulty": "HARD",
        "description": "Find the minimum number of operations required to convert one string into another. Allowed operations are insertion, deletion, and replacement.",
        "input_format": "Two strings separated by slash or newline.",
        "output_format": "Minimum number of edit operations.",
        "constraints": "0 <= word1.length, word2.length <= 500",
        "time_complexity": "O(M * N)",
        "space_complexity": "O(M * N)",
        "company_tags": ["Amazon", "Google", "Microsoft", "Uber"],
        "examples": [
            {"input": "horse / ros", "output": "3", "explanation": "horse -> rorse (replace 'h' with 'r') -> rose (remove 'r') -> ros (remove 'e')."},
            {"input": "intention / execution", "output": "5", "explanation": "5 operations required."},
            {"input": "abc / abc", "output": "0", "explanation": "Strings are identical."}
        ],
        "test_cases": [
            {"input": "horse / ros", "expected": "3", "is_hidden": False},
            {"input": "intention / execution", "expected": "5", "is_hidden": False},
            {"input": "abc / abc", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def edit_distance(a, b):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

int min3(int a, int b, int c) {
    int m = a;
    if (b < m) m = b;
    if (c < m) m = c;
    return m;
}

int dp[505][505];

int main() {
    char token[505];
    char a[505] = "", b[505] = "";

    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    strcpy(a, token);
    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    strcpy(b, token);

    int m = strlen(a);
    int n = strlen(b);

    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (a[i - 1] == b[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = 1 + min3(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
            }
        }
    }

    printf("%d\\n", dp[m][n]);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    string a, b, token;
    vector<string> tokens;
    while (cin >> token) {
        if (token != "/") tokens.push_back(token);
    }
    if (tokens.size() >= 2) {
        a = tokens[0];
        b = tokens[1];
    }

    int m = a.length(), n = b.length();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (a[i - 1] == b[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
            }
        }
    }

    cout << dp[m][n] << endl;
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
        if (tokens.size() < 2) {
            System.out.println(0);
            return;
        }
        String a = tokens.get(0);
        String b = tokens.get(1);

        int m = a.length();
        int n = b.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (a.charAt(i - 1) == b.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + Math.min(dp[i - 1][j], Math.min(dp[i][j - 1], dp[i - 1][j - 1]));
                }
            }
        }

        System.out.println(dp[m][n]);
    }
}""",
            "python": """import sys

def edit_distance(a, b):
    m = len(a)
    n = len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                )

    return dp[m][n]

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if len(tokens) >= 2:
        print(edit_distance(tokens[0], tokens[1]))
    else:
        print(0)"""
        })
    },

    # 27. Matrix Chain Multiplication
    {
        "id": "dsa-dp-matrix-chain",
        "problem_num": 192,
        "title": "Matrix Chain Multiplication",
        "category": "Dynamic Programming",
        "topic": "Interval DP",
        "subtopic": "MCM",
        "difficulty": "HARD",
        "description": "Find the minimum number of scalar multiplications required to multiply a sequence of matrices.",
        "input_format": "Space-separated array p of matrix dimensions where matrix i has dimensions p[i] x p[i+1].",
        "output_format": "Minimum scalar multiplication operations.",
        "constraints": "2 <= p.length <= 100, 1 <= p[i] <= 500",
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N^2)",
        "company_tags": ["Amazon", "Google", "Microsoft"],
        "examples": [
            {"input": "40 20 30 10 30", "output": "26000", "explanation": "Optimal parenthesization requires 26000 scalar operations."},
            {"input": "10 20 30", "output": "6000", "explanation": "Two matrices: 10x20 and 20x30 requires 10*20*30 = 6000."},
            {"input": "10 20 30 40", "output": "18000", "explanation": "Three matrices optimal multiplication cost is 18000."}
        ],
        "test_cases": [
            {"input": "40 20 30 10 30", "expected": "26000", "is_hidden": False},
            {"input": "10 20 30", "expected": "6000", "is_hidden": False},
            {"input": "10 20 30 40", "expected": "18000", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def matrix_chain(p):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

#define INF 2000000000

int main() {
    int p[105];
    int size = 0;
    while (scanf("%d", &p[size]) == 1) {
        size++;
    }

    int n = size - 1;
    long long dp[105][105] = {0};

    for (int length = 2; length <= n; length++) {
        for (int i = 0; i <= n - length; i++) {
            int j = i + length - 1;
            dp[i][j] = INF;

            for (int k = i; k < j; k++) {
                long long cost = dp[i][k] + dp[k + 1][j] + (long long)p[i] * p[k + 1] * p[j + 1];
                if (cost < dp[i][j]) {
                    dp[i][j] = cost;
                }
            }
        }
    }

    printf("%lld\\n", dp[0][n - 1]);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

int main() {
    vector<long long> p;
    long long val;
    while (cin >> val) p.push_back(val);

    int n = p.size() - 1;
    vector<vector<long long>> dp(n, vector<long long>(n, 0));

    for (int length = 2; length <= n; length++) {
        for (int i = 0; i <= n - length; i++) {
            int j = i + length - 1;
            dp[i][j] = INF;

            for (int k = i; k < j; k++) {
                long long cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1];
                dp[i][j] = min(dp[i][j], cost);
            }
        }
    }

    cout << dp[0][n - 1] << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Long> pList = new ArrayList<>();
        while (sc.hasNextLong()) pList.add(sc.nextLong());

        int n = pList.size() - 1;
        long[][] dp = new long[n][n];

        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                dp[i][j] = Long.MAX_VALUE / 2;

                for (int k = i; k < j; k++) {
                    long cost = dp[i][k] + dp[k + 1][j] + pList.get(i) * pList.get(k + 1) * pList.get(j + 1);
                    dp[i][j] = Math.min(dp[i][j], cost);
                }
            }
        }

        System.out.println(dp[0][n - 1]);
    }
}""",
            "python": """import sys

def matrix_chain(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (
                    dp[i][k] +
                    dp[k + 1][j] +
                    p[i] * p[k + 1] * p[j + 1]
                )
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        p = list(map(int, tokens))
        print(matrix_chain(p))"""
        })
    },

    # 28. Word Break Problem
    {
        "id": "dsa-dp-word-break",
        "problem_num": 193,
        "title": "Word Break Problem",
        "category": "Dynamic Programming",
        "topic": "String DP",
        "subtopic": "Segmentation DP",
        "difficulty": "HARD",
        "description": "Determine whether a string can be divided into valid dictionary words.",
        "input_format": "String s followed by dictionary word list, separated by a slash or spaces.",
        "output_format": "True if s can be segmented, otherwise False.",
        "constraints": "1 <= s.length <= 300, 1 <= wordDict.length <= 1000",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Bloomberg", "Google", "Facebook"],
        "examples": [
            {"input": "leetcode / leet code", "output": "True", "explanation": "'leetcode' can be segmented as 'leet' and 'code'."},
            {"input": "applepenapple / apple pen", "output": "True", "explanation": "'applepenapple' can be segmented as 'apple', 'pen', 'apple'."},
            {"input": "catsandog / cats dog sand and cat", "output": "False", "explanation": "Cannot segment without overlapping or missing letters."}
        ],
        "test_cases": [
            {"input": "leetcode / leet code", "expected": "True", "is_hidden": False},
            {"input": "applepenapple / apple pen", "expected": "True", "is_hidden": False},
            {"input": "catsandog / cats dog sand and cat", "expected": "False", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <unordered_set>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def word_break(s, words):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

char words[1005][100];
int wordCount = 0;

int inDict(const char *sub) {
    for (int i = 0; i < wordCount; i++) {
        if (strcmp(words[i], sub) == 0) return 1;
    }
    return 0;
}

int main() {
    char token[305];
    char s[305] = "";

    while (scanf("%s", token) == 1 && strcmp(token, "/") == 0);
    strcpy(s, token);

    while (scanf("%s", token) == 1) {
        if (strcmp(token, "/") == 0) continue;
        strcpy(words[wordCount++], token);
    }

    int n = strlen(s);
    int dp[305] = {0};
    dp[0] = 1;

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            if (dp[j]) {
                char sub[305];
                int len = i - j;
                strncpy(sub, s + j, len);
                sub[len] = '\\0';
                if (inDict(sub)) {
                    dp[i] = 1;
                    break;
                }
            }
        }
    }

    printf("%s\\n", dp[n] ? "True" : "False");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
    string token;
    vector<string> tokens;
    while (cin >> token) {
        if (token != "/") tokens.push_back(token);
    }
    if (tokens.empty()) return 0;

    string s = tokens[0];
    unordered_set<string> word_set;
    for (size_t i = 1; i < tokens.size(); i++) {
        word_set.insert(tokens[i]);
    }

    int n = s.length();
    vector<bool> dp(n + 1, false);
    dp[0] = true;

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            if (dp[j] && word_set.count(s.substr(j, i - j))) {
                dp[i] = true;
                break;
            }
        }
    }

    cout << (dp[n] ? "True" : "False") << endl;
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

        String s = tokens.get(0);
        Set<String> wordSet = new HashSet<>();
        for (int i = 1; i < tokens.size(); i++) {
            wordSet.add(tokens.get(i));
        }

        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        System.out.println(dp[n] ? "True" : "False");
    }
}""",
            "python": """import sys

def word_break(s, words):
    word_set = set(words)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]

if __name__ == '__main__':
    tokens = sys.stdin.read().replace('/', ' ').split()
    if tokens:
        s = tokens[0]
        words = tokens[1:]
        print(word_break(s, words))"""
        })
    },

    # 29. Partition Equal Subset Sum
    {
        "id": "dsa-dp-partition-equal-subset",
        "problem_num": 194,
        "title": "Partition Equal Subset Sum",
        "category": "Dynamic Programming",
        "topic": "Knapsack",
        "subtopic": "Subset Sum",
        "difficulty": "HARD",
        "description": "Determine whether an array can be divided into two subsets having equal sums.",
        "input_format": "Space-separated array of positive integers.",
        "output_format": "True if equal partition is possible, otherwise False.",
        "constraints": "1 <= nums.length <= 200, 1 <= nums[i] <= 100",
        "time_complexity": "O(N * sum)",
        "space_complexity": "O(sum)",
        "company_tags": ["Amazon", "Google", "Facebook", "Microsoft"],
        "examples": [
            {"input": "1 5 11 5", "output": "True", "explanation": "The array can be partitioned as [1, 5, 5] and [11]."},
            {"input": "1 2 3 5", "output": "False", "explanation": "Sum is 11 (odd), cannot be divided equally."},
            {"input": "2 2 2 2", "output": "True", "explanation": "Partition into [2, 2] and [2, 2]."}
        ],
        "test_cases": [
            {"input": "1 5 11 5", "expected": "True", "is_hidden": False},
            {"input": "1 2 3 5", "expected": "False", "is_hidden": False},
            {"input": "2 2 2 2", "expected": "True", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def can_partition(nums):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int main() {
    int nums[205];
    int n = 0;
    int total = 0;

    while (scanf("%d", &nums[n]) == 1) {
        total += nums[n];
        n++;
    }

    if (total % 2 != 0) {
        printf("False\\n");
        return 0;
    }

    int target = total / 2;
    int dp[20005] = {0};
    dp[0] = 1;

    for (int i = 0; i < n; i++) {
        for (int j = target; j >= nums[i]; j--) {
            if (dp[j - nums[i]]) dp[j] = 1;
        }
    }

    printf("%s\\n", dp[target] ? "True" : "False");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    vector<int> nums;
    int val;
    int total = 0;
    while (cin >> val) {
        nums.push_back(val);
        total += val;
    }

    if (total % 2 != 0) {
        cout << "False" << endl;
        return 0;
    }

    int target = total / 2;
    vector<bool> dp(target + 1, false);
    dp[0] = true;

    for (int num : nums) {
        for (int j = target; j >= num; j--) {
            dp[j] = dp[j] || dp[j - num];
        }
    }

    cout << (dp[target] ? "True" : "False") << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> nums = new ArrayList<>();
        int total = 0;
        while (sc.hasNextInt()) {
            int val = sc.nextInt();
            nums.add(val);
            total += val;
        }

        if (total % 2 != 0) {
            System.out.println("False");
            return;
        }

        int target = total / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;

        for (int num : nums) {
            for (int j = target; j >= num; j--) {
                dp[j] = dp[j] || dp[j - num];
            }
        }

        System.out.println(dp[target] ? "True" : "False");
    }
}""",
            "python": """import sys

def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        nums = list(map(int, tokens))
        print(can_partition(nums))"""
        })
    },

    # 30. Burst Balloons
    {
        "id": "dsa-dp-burst-balloons",
        "problem_num": 195,
        "title": "Burst Balloons",
        "category": "Dynamic Programming",
        "topic": "Interval DP",
        "subtopic": "Matrix Interval",
        "difficulty": "HARD",
        "description": "Given balloons with numbers, burst them to maximize coins. When balloon i is burst, you earn the product of its value and its current left and right neighbors. Missing neighbors have value 1.",
        "input_format": "Space-separated array of balloon values.",
        "output_format": "Maximum coins obtainable.",
        "constraints": "1 <= nums.length <= 300, 0 <= nums[i] <= 100",
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N^2)",
        "company_tags": ["Google", "Amazon", "Samsung", "Bloomberg"],
        "examples": [
            {"input": "3 1 5 8", "output": "167", "explanation": "nums = [3,1,5,8] -> [3,5,8] -> [3,8] -> [8] -> [] gives coins = 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167."},
            {"input": "1 5", "output": "10", "explanation": "Burst 1 first (1*1*5=5) then 5 (1*5*1=5) gives 10."},
            {"input": "7", "output": "7", "explanation": "Single balloon gives 1*7*1 = 7."}
        ],
        "test_cases": [
            {"input": "3 1 5 8", "expected": "167", "is_hidden": False},
            {"input": "1 5", "expected": "10", "is_hidden": False},
            {"input": "7", "expected": "7", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def max_coins(nums):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int dp[305][305];

int main() {
    int nums[305];
    int raw[305];
    int count = 0;
    while (scanf("%d", &raw[count]) == 1) {
        count++;
    }

    nums[0] = 1;
    for (int i = 0; i < count; i++) nums[i + 1] = raw[i];
    nums[count + 1] = 1;
    int n = count + 2;

    for (int length = 2; length < n; length++) {
        for (int left = 0; left < n - length; left++) {
            int right = left + length;
            for (int k = left + 1; k < right; k++) {
                int coins = nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right];
                if (coins > dp[left][right]) {
                    dp[left][right] = coins;
                }
            }
        }
    }

    printf("%d\\n", dp[0][n - 1]);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> raw;
    int val;
    while (cin >> val) raw.push_back(val);

    vector<int> nums = {1};
    nums.insert(nums.end(), raw.begin(), raw.end());
    nums.push_back(1);

    int n = nums.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));

    for (int length = 2; length < n; length++) {
        for (int left = 0; left < n - length; left++) {
            int right = left + length;
            for (int k = left + 1; k < right; k++) {
                int coins = nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right];
                dp[left][right] = max(dp[left][right], coins);
            }
        }
    }

    cout << dp[0][n - 1] << endl;
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> raw = new ArrayList<>();
        while (sc.hasNextInt()) raw.add(sc.nextInt());

        int[] nums = new int[raw.size() + 2];
        nums[0] = 1;
        for (int i = 0; i < raw.size(); i++) nums[i + 1] = raw.get(i);
        nums[nums.length - 1] = 1;

        int n = nums.length;
        int[][] dp = new int[n][n];

        for (int length = 2; length < n; length++) {
            for (int left = 0; left < n - length; left++) {
                int right = left + length;
                for (int k = left + 1; k < right; k++) {
                    int coins = nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right];
                    dp[left][right] = Math.max(dp[left][right], coins);
                }
            }
        }

        System.out.println(dp[0][n - 1]);
    }
}""",
            "python": """import sys

def max_coins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for k in range(left + 1, right):
                coins = (
                    nums[left] * nums[k] * nums[right]
                    + dp[left][k]
                    + dp[k][right]
                )
                dp[left][right] = max(
                    dp[left][right],
                    coins
                )

    return dp[0][n - 1]

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        nums = list(map(int, tokens))
        print(max_coins(nums))"""
        })
    }
]

problems.extend(dp_data)

with open("backend/app/data/dsa_problems_seed.json", "w", encoding="utf-8") as f:
    json.dump(problems, f, indent=2)

print(f"Successfully added 15 DP problems! Total problems in seed: {len(problems)}")
