import sys, os
sys.path.insert(0, os.path.abspath('.'))
import json
from backend.app.services.execution_service import SandboxedExecutionService

# Load problem dsa-search-linear
with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    data = json.load(f)

problem = next(p for p in data if p["id"] == "dsa-search-linear")
test_cases = problem["test_cases"]

# 1. C solution
c_code = """#include <stdio.h>

int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target)
            return i;
    }
    return -1;
}

int main() {
    int n, target;
    if (scanf("%d", &n) != 1) return 0;
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    if (scanf("%d", &target) != 1) return 0;
    printf("%d\\n", linearSearch(arr, n, target));
    return 0;
}
"""

# 2. C++ solution
cpp_code = """#include <iostream>
#include <vector>

using namespace std;

int linearSearch(const vector<int>& arr, int target) {
    for (int i = 0; i < (int)arr.size(); i++) {
        if (arr[i] == target)
            return i;
    }
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, target;
    if (cin >> n) {
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];
        cin >> target;
        cout << linearSearch(arr, target) << "\\n";
    }
    return 0;
}
"""

# 3. Java solution
java_code = """import java.util.Scanner;

public class Main {
    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target)
                return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
            int target = sc.nextInt();
            System.out.println(linearSearch(arr, target));
        }
    }
}
"""

# 4. Python solution
python_code = """def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().split()))
    target = int(input().strip())
    print(linearSearch(arr, target))
"""

for lang, code in [("c", c_code), ("cpp", cpp_code), ("java", java_code), ("python", python_code)]:
    status, passed, total, logs = SandboxedExecutionService.run_test_cases(lang, code, test_cases)
    print(f"[{lang}] Status: {status.value} ({passed}/{total})")
    if status.value != "PASSED":
        print("  Logs:", logs)
