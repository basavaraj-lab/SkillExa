import sys, os
sys.path.insert(0, os.path.abspath('.'))
import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    problems = json.load(f)

rec_ids = {
    "dsa-rec-factorial", "dsa-rec-fibonacci", "dsa-rec-sum-of-digits",
    "dsa-rec-reverse-string", "dsa-rec-check-palindrome", "dsa-rec-power",
    "dsa-rec-all-subsequences", "dsa-rec-permutations", "dsa-rec-combination-sum",
    "dsa-rec-generate-parentheses", "dsa-rec-n-queens", "dsa-rec-sudoku-solver",
    "dsa-rec-word-search", "dsa-rec-rat-in-maze", "dsa-rec-palindrome-partitioning"
}
problems = [p for p in problems if p["id"] not in rec_ids]

rec_data = [
    # 1. Factorial Using Recursion
    {
        "id": "dsa-rec-factorial",
        "problem_num": 121,
        "title": "Factorial Using Recursion",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "Base Case & Reduction",
        "difficulty": "EASY",
        "description": "Given a non-negative integer N, calculate its factorial using recursion.",
        "input_format": "A single non-negative integer N.",
        "output_format": "The factorial value of N.",
        "constraints": "0 <= N <= 12",
        "time_complexity": "O(N)",
        "space_complexity": "O(N) call stack",
        "company_tags": ["TCS", "Infosys", "Wipro", "Cognizant"],
        "examples": [
            {"input": "5", "output": "120", "explanation": "5! = 5 * 4 * 3 * 2 * 1 = 120"},
            {"input": "0", "output": "1", "explanation": "0! = 1"},
            {"input": "7", "output": "5040", "explanation": "7! = 5040"}
        ],
        "test_cases": [
            {"input": "5", "expected": "120", "is_hidden": False},
            {"input": "0", "expected": "1", "is_hidden": False},
            {"input": "7", "expected": "5040", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nlong long factorial(int n) {\n    // Your code here\n    return 1;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) printf(\"%lld\\n\", factorial(n));\n    return 0;\n}",
            "cpp": "#include <iostream>\nusing namespace std;\n\nlong long factorial(int n) {\n    // Your code here\n    return 1;\n}\n\nint main() {\n    int n;\n    if (cin >> n) cout << factorial(n) << \"\\n\";\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static long factorial(int n) {\n        // Your code here\n        return 1;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) System.out.println(factorial(sc.nextInt()));\n    }\n}",
            "python": "def factorial(n):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    import sys\n    tokens = sys.stdin.read().split()\n    if tokens: print(factorial(int(tokens[0])))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

long long factorial(int n) {
    if (n == 0 || n == 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        printf("%lld\\n", factorial(n));
    }
    return 0;
}""",
            "cpp": """#include <iostream>

using namespace std;

long long factorial(int n) {
    if (n == 0 || n == 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    int n;
    if (cin >> n) {
        cout << factorial(n) << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static long factorial(int n) {
        if (n == 0 || n == 1) return 1;
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            System.out.println(factorial(sc.nextInt()));
        }
    }
}""",
            "python": """import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        print(factorial(n))"""
        })
    },

    # 2. Fibonacci Number Using Recursion
    {
        "id": "dsa-rec-fibonacci",
        "problem_num": 122,
        "title": "Fibonacci Number Using Recursion",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "Binary Tree Recursion",
        "difficulty": "EASY",
        "description": "Given an integer N, find the Nth Fibonacci number using recursion where F(0)=0 and F(1)=1.",
        "input_format": "A single non-negative integer N.",
        "output_format": "The Nth Fibonacci number.",
        "constraints": "0 <= N <= 25",
        "time_complexity": "O(2^N)",
        "space_complexity": "O(N) call stack",
        "company_tags": ["Amazon", "Microsoft", "Accenture"],
        "examples": [
            {"input": "5", "output": "5", "explanation": "F(5) = 5"},
            {"input": "7", "output": "13", "explanation": "F(7) = 13"},
            {"input": "0", "output": "0", "explanation": "F(0) = 0"}
        ],
        "test_cases": [
            {"input": "5", "expected": "5", "is_hidden": False},
            {"input": "7", "expected": "13", "is_hidden": False},
            {"input": "0", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint fibonacci(int n) {\n    // Your code here\n    return 0;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) printf(\"%d\\n\", fibonacci(n));\n    return 0;\n}",
            "cpp": "#include <iostream>\nusing namespace std;\n\nint fibonacci(int n) {\n    // Your code here\n    return 0;\n}\n\nint main() {\n    int n;\n    if (cin >> n) cout << fibonacci(n) << \"\\n\";\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static int fibonacci(int n) {\n        // Your code here\n        return 0;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) System.out.println(fibonacci(sc.nextInt()));\n    }\n}",
            "python": "def fibonacci(n):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    import sys\n    tokens = sys.stdin.read().split()\n    if tokens: print(fibonacci(int(tokens[0])))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        printf("%d\\n", fibonacci(n));
    }
    return 0;
}""",
            "cpp": """#include <iostream>

using namespace std;

int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n;
    if (cin >> n) {
        cout << fibonacci(n) << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int fibonacci(int n) {
        if (n <= 1) return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            System.out.println(fibonacci(sc.nextInt()));
        }
    }
}""",
            "python": """import sys

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        print(fibonacci(n))"""
        })
    },

    # 3. Sum of Digits Using Recursion
    {
        "id": "dsa-rec-sum-of-digits",
        "problem_num": 123,
        "title": "Sum of Digits Using Recursion",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "Numeric Recursion",
        "difficulty": "EASY",
        "description": "Given a positive integer N, find the sum of its digits using recursion.",
        "input_format": "A single non-negative integer N.",
        "output_format": "Sum of the digits of N.",
        "constraints": "0 <= N <= 10^9",
        "time_complexity": "O(log10(N))",
        "space_complexity": "O(log10(N)) call stack",
        "company_tags": ["TCS", "Cognizant", "Capgemini"],
        "examples": [
            {"input": "1234", "output": "10", "explanation": "1 + 2 + 3 + 4 = 10"},
            {"input": "555", "output": "15", "explanation": "5 + 5 + 5 = 15"},
            {"input": "9", "output": "9", "explanation": "Single digit sum is itself"}
        ],
        "test_cases": [
            {"input": "1234", "expected": "10", "is_hidden": False},
            {"input": "555", "expected": "15", "is_hidden": False},
            {"input": "9", "expected": "9", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint sumDigits(int n) {\n    // Your code here\n    return 0;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) printf(\"%d\\n\", sumDigits(n));\n    return 0;\n}",
            "cpp": "#include <iostream>\nusing namespace std;\n\nint sumDigits(int n) {\n    // Your code here\n    return 0;\n}\n\nint main() {\n    int n;\n    if (cin >> n) cout << sumDigits(n) << \"\\n\";\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static int sumDigits(int n) {\n        // Your code here\n        return 0;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) System.out.println(sumDigits(sc.nextInt()));\n    }\n}",
            "python": "def sumDigits(n):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    import sys\n    tokens = sys.stdin.read().split()\n    if tokens: print(sumDigits(int(tokens[0])))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int sumDigits(int n) {
    if (n == 0) return 0;
    return (n % 10) + sumDigits(n / 10);
}

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        printf("%d\\n", sumDigits(n));
    }
    return 0;
}""",
            "cpp": """#include <iostream>

using namespace std;

int sumDigits(int n) {
    if (n == 0) return 0;
    return (n % 10) + sumDigits(n / 10);
}

int main() {
    int n;
    if (cin >> n) {
        cout << sumDigits(n) << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int sumDigits(int n) {
        if (n == 0) return 0;
        return (n % 10) + sumDigits(n / 10);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            System.out.println(sumDigits(sc.nextInt()));
        }
    }
}""",
            "python": """import sys

def sumDigits(n):
    if n == 0:
        return 0
    return n % 10 + sumDigits(n // 10)

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        print(sumDigits(n))"""
        })
    },

    # 4. Reverse a String Using Recursion
    {
        "id": "dsa-rec-reverse-string",
        "problem_num": 124,
        "title": "Reverse a String Using Recursion",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "String Recursion",
        "difficulty": "EASY",
        "description": "Given a string, reverse it using recursion.",
        "input_format": "A single string s.",
        "output_format": "The reversed string.",
        "constraints": "1 <= s.length <= 1000",
        "time_complexity": "O(N)",
        "space_complexity": "O(N) call stack",
        "company_tags": ["Amazon", "Adobe", "Wipro"],
        "examples": [
            {"input": "hello", "output": "olleh", "explanation": "hello reversed is olleh"},
            {"input": "python", "output": "nohtyp", "explanation": "python reversed is nohtyp"},
            {"input": "abc", "output": "cba", "explanation": "abc reversed is cba"}
        ],
        "test_cases": [
            {"input": "hello", "expected": "olleh", "is_hidden": False},
            {"input": "python", "expected": "nohtyp", "is_hidden": False},
            {"input": "abc", "expected": "cba", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <string.h>\n\nvoid reverseString(char *s, int l, int r) {\n    // Your code here\n}\n\nint main() {\n    char s[1005];\n    if (scanf(\"%s\", s) == 1) {\n        reverseString(s, 0, strlen(s) - 1);\n        printf(\"%s\\n\", s);\n    }\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\n\nstring reverseString(string s) {\n    // Your code here\n    return s;\n}\n\nint main() {\n    string s;\n    if (cin >> s) cout << reverseString(s) << \"\\n\";\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static String reverseString(String s) {\n        // Your code here\n        return s;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) System.out.println(reverseString(sc.next()));\n    }\n}",
            "python": "def reverseString(s):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    import sys\n    s = sys.stdin.read().strip()\n    if s: print(reverseString(s))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

void reverseHelper(char *s, int l, int r) {
    if (l >= r) return;
    char temp = s[l];
    s[l] = s[r];
    s[r] = temp;
    reverseHelper(s, l + 1, r - 1);
}

int main() {
    char s[1005];
    if (scanf("%s", s) == 1) {
        reverseHelper(s, 0, strlen(s) - 1);
        printf("%s\\n", s);
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>

using namespace std;

string reverseString(string s) {
    if (s.length() <= 1) return s;
    return reverseString(s.substr(1)) + s[0];
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
        if (s.length() <= 1) return s;
        return reverseString(s.substring(1)) + s.charAt(0);
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
    if len(s) <= 1:
        return s
    return reverseString(s[1:]) + s[0]

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        print(reverseString(s))"""
        })
    },

    # 5. Check Palindrome Using Recursion
    {
        "id": "dsa-rec-check-palindrome",
        "problem_num": 125,
        "title": "Check Palindrome Using Recursion",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "Two-Pointer Recursion",
        "difficulty": "EASY",
        "description": "Given a string, determine whether it is a palindrome using two-pointer recursion.",
        "input_format": "A single string s.",
        "output_format": "True if palindrome, else False.",
        "constraints": "1 <= s.length <= 1000",
        "time_complexity": "O(N)",
        "space_complexity": "O(N) call stack",
        "company_tags": ["Amazon", "TCS", "Accenture"],
        "examples": [
            {"input": "madam", "output": "True", "explanation": "madam reads same forward and backward"},
            {"input": "level", "output": "True", "explanation": "level is palindrome"},
            {"input": "hello", "output": "False", "explanation": "hello is not palindrome"}
        ],
        "test_cases": [
            {"input": "madam", "expected": "True", "is_hidden": False},
            {"input": "level", "expected": "True", "is_hidden": False},
            {"input": "hello", "expected": "False", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n\nbool isPalindrome(char *s, int left, int right) {\n    // Your code here\n    return false;\n}\n\nint main() {\n    char s[1005];\n    if (scanf(\"%s\", s) == 1) {\n        printf(\"%s\\n\", isPalindrome(s, 0, strlen(s) - 1) ? \"True\" : \"False\");\n    }\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\n\nbool isPalindrome(string s, int left, int right) {\n    // Your code here\n    return false;\n}\n\nint main() {\n    string s;\n    if (cin >> s) cout << (isPalindrome(s, 0, s.length() - 1) ? \"True\" : \"False\") << \"\\n\";\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static boolean isPalindrome(String s, int left, int right) {\n        // Your code here\n        return false;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) {\n            String s = sc.next();\n            System.out.println(isPalindrome(s, 0, s.length() - 1) ? \"True\" : \"False\");\n        }\n    }\n}",
            "python": "def isPalindrome(s, left, right):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    import sys\n    s = sys.stdin.read().strip()\n    if s: print(isPalindrome(s, 0, len(s) - 1))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isPalindrome(char *s, int left, int right) {
    if (left >= right) return true;
    if (s[left] != s[right]) return false;
    return isPalindrome(s, left + 1, right - 1);
}

int main() {
    char s[1005];
    if (scanf("%s", s) == 1) {
        printf("%s\\n", isPalindrome(s, 0, strlen(s) - 1) ? "True" : "False");
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <string>

using namespace std;

bool isPalindrome(const string& s, int left, int right) {
    if (left >= right) return true;
    if (s[left] != s[right]) return false;
    return isPalindrome(s, left + 1, right - 1);
}

int main() {
    string s;
    if (cin >> s) {
        cout << (isPalindrome(s, 0, s.length() - 1) ? "True" : "False") << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static boolean isPalindrome(String s, int left, int right) {
        if (left >= right) return true;
        if (s.charAt(left) != s.charAt(right)) return false;
        return isPalindrome(s, left + 1, right - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            System.out.println(isPalindrome(s, 0, s.length() - 1) ? "True" : "False");
        }
    }
}""",
            "python": """import sys

def isPalindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return isPalindrome(s, left + 1, right - 1)

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        print(isPalindrome(s, 0, len(s) - 1))"""
        })
    },

    # 6. Power of a Number
    {
        "id": "dsa-rec-power",
        "problem_num": 126,
        "title": "Power of a Number",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "Divide & Conquer Power",
        "difficulty": "MEDIUM",
        "description": "Given two integers X and N, calculate X raised to the power N using recursion.",
        "input_format": "Two integers X and N.",
        "output_format": "The value of X^N.",
        "constraints": "1 <= X <= 10\n0 <= N <= 10",
        "time_complexity": "O(N)",
        "space_complexity": "O(N) call stack",
        "company_tags": ["Amazon", "Google", "Microsoft"],
        "examples": [
            {"input": "2 5", "output": "32", "explanation": "2^5 = 32"},
            {"input": "3 3", "output": "27", "explanation": "3^3 = 27"},
            {"input": "5 0", "output": "1", "explanation": "5^0 = 1"}
        ],
        "test_cases": [
            {"input": "2 5", "expected": "32", "is_hidden": False},
            {"input": "3 3", "expected": "27", "is_hidden": False},
            {"input": "5 0", "expected": "1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nlong long power(int x, int n) {\n    // Your code here\n    return 1;\n}\n\nint main() {\n    int x, n;\n    if (scanf(\"%d %d\", &x, &n) == 2) printf(\"%lld\\n\", power(x, n));\n    return 0;\n}",
            "cpp": "#include <iostream>\nusing namespace std;\n\nlong long power(int x, int n) {\n    // Your code here\n    return 1;\n}\n\nint main() {\n    int x, n;\n    if (cin >> x >> n) cout << power(x, n) << \"\\n\";\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static long power(int x, int n) {\n        // Your code here\n        return 1;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) System.out.println(power(sc.nextInt(), sc.nextInt()));\n    }\n}",
            "python": "def power(x, n):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    import sys\n    tokens = sys.stdin.read().split()\n    if tokens: print(power(int(tokens[0]), int(tokens[1])))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

long long power(int x, int n) {
    if (n == 0) return 1;
    return x * power(x, n - 1);
}

int main() {
    int x, n;
    if (scanf("%d %d", &x, &n) == 2) {
        printf("%lld\\n", power(x, n));
    }
    return 0;
}""",
            "cpp": """#include <iostream>

using namespace std;

long long power(int x, int n) {
    if (n == 0) return 1;
    return x * power(x, n - 1);
}

int main() {
    int x, n;
    if (cin >> x >> n) {
        cout << power(x, n) << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static long power(int x, int n) {
        if (n == 0) return 1;
        return x * power(x, n - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int x = sc.nextInt();
            int n = sc.nextInt();
            System.out.println(power(x, n));
        }
    }
}""",
            "python": """import sys

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        x = int(tokens[0])
        n = int(tokens[1])
        print(power(x, n))"""
        })
    },

    # 7. Generate All Subsequences of a String
    {
        "id": "dsa-rec-all-subsequences",
        "problem_num": 127,
        "title": "Generate All Subsequences of a String",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "Pick / Don't Pick Recursion",
        "difficulty": "MEDIUM",
        "description": "Given a string, generate all possible subsequences maintaining character order.",
        "input_format": "A single string s.",
        "output_format": "Comma-separated list of subsequences (with empty string shown as \"\").",
        "constraints": "1 <= s.length <= 10",
        "time_complexity": "O(2^N)",
        "space_complexity": "O(N) call stack",
        "company_tags": ["Amazon", "Google", "Paytm"],
        "examples": [
            {"input": "ab", "output": "\"\", b, a, ab", "explanation": "Subsequences of 'ab'."},
            {"input": "a", "output": "\"\", a", "explanation": "Subsequences of 'a'."},
            {"input": "abc", "output": "\"\", c, b, bc, a, ac, ab, abc", "explanation": "All 8 subsequences."}
        ],
        "test_cases": [
            {"input": "ab", "expected": "\"\", b, a, ab", "is_hidden": False},
            {"input": "a", "expected": "\"\", a", "is_hidden": False},
            {"input": "abc", "expected": "\"\", c, b, bc, a, ac, ab, abc", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <string.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def generateSubsequences(s, index, current, result):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

char results[2000][20];
int res_count = 0;

void generateSubsequences(char *s, int index, char *current, int len) {
    if (s[index] == '\\0') {
        current[len] = '\\0';
        if (len == 0) {
            results[res_count][0] = '\"';
            results[res_count][1] = '\"';
            results[res_count][2] = '\\0';
            res_count++;
        } else {
            strcpy(results[res_count++], current);
        }
        return;
    }
    generateSubsequences(s, index + 1, current, len);
    current[len] = s[index];
    generateSubsequences(s, index + 1, current, len + 1);
}

int main() {
    char s[20];
    if (scanf("%s", s) != 1) return 0;
    char current[20];
    generateSubsequences(s, 0, current, 0);
    for (int i = 0; i < res_count; i++) {
        printf("%s%s", results[i], (i == res_count - 1) ? "\\n" : ", ");
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

void generateSubsequences(const string& s, int index, string current, vector<string>& result) {
    if (index == (int)s.length()) {
        if (current.empty()) {
            string empty_token = "";
            empty_token += '\"';
            empty_token += '\"';
            result.push_back(empty_token);
        } else {
            result.push_back(current);
        }
        return;
    }
    generateSubsequences(s, index + 1, current, result);
    generateSubsequences(s, index + 1, current + s[index], result);
}

int main() {
    string s;
    if (cin >> s) {
        vector<string> res;
        generateSubsequences(s, 0, "", res);
        for (int i = 0; i < (int)res.size(); i++) {
            cout << res[i] << (i == (int)res.size() - 1 ? "\\n" : ", ");
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void generateSubsequences(String s, int index, String current, List<String> result) {
        if (index == s.length()) {
            result.add(current.isEmpty() ? String.valueOf('\"') + '\"' : current);
            return;
        }
        generateSubsequences(s, index + 1, current, result);
        generateSubsequences(s, index + 1, current + s.charAt(index), result);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            List<String> res = new ArrayList<>();
            generateSubsequences(s, 0, "", res);
            for (int i = 0; i < res.size(); i++) {
                System.out.print(res.get(i) + (i == res.size() - 1 ? "\\n" : ", "));
            }
        }
    }
}""",
            "python": """import sys

def generateSubsequences(s, index, current, res):
    if index == len(s):
        res.append(current if current else '""')
        return

    generateSubsequences(s, index + 1, current, res)
    generateSubsequences(s, index + 1, current + s[index], res)

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        res = []
        generateSubsequences(s, 0, "", res)
        print(", ".join(res))"""
        })
    },

    # 8. Generate All Permutations of a String
    {
        "id": "dsa-rec-permutations",
        "problem_num": 128,
        "title": "Generate All Permutations of a String",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "Permutation Backtracking",
        "difficulty": "MEDIUM",
        "description": "Given a string of distinct characters, generate all possible permutations.",
        "input_format": "A single string s.",
        "output_format": "Comma-separated string permutations.",
        "constraints": "1 <= s.length <= 8",
        "time_complexity": "O(N!)",
        "space_complexity": "O(N) call stack",
        "company_tags": ["Amazon", "Microsoft", "Google"],
        "examples": [
            {"input": "ab", "output": "ab, ba", "explanation": "2 permutations of 'ab'."},
            {"input": "abc", "output": "abc, acb, bac, bca, cab, cba", "explanation": "6 permutations of 'abc'."},
            {"input": "a", "output": "a", "explanation": "1 permutation of 'a'."}
        ],
        "test_cases": [
            {"input": "ab", "expected": "ab, ba", "is_hidden": False},
            {"input": "abc", "expected": "abc, acb, bac, bca, cab, cba", "is_hidden": False},
            {"input": "a", "expected": "a", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <string.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def permutations(s, current=\"\", res=None):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

char results[50000][10];
int res_count = 0;

void permutations(char *s, char *current, int len) {
    int n = strlen(s);
    if (n == 0) {
        current[len] = '\\0';
        strcpy(results[res_count++], current);
        return;
    }
    for (int i = 0; i < n; i++) {
        char rem[10];
        int r_idx = 0;
        for (int j = 0; j < n; j++) {
            if (j != i) rem[r_idx++] = s[j];
        }
        rem[r_idx] = '\\0';

        current[len] = s[i];
        permutations(rem, current, len + 1);
    }
}

int main() {
    char s[10];
    if (scanf("%s", s) != 1) return 0;
    char current[10];
    permutations(s, current, 0);
    for (int i = 0; i < res_count; i++) {
        printf("%s%s", results[i], (i == res_count - 1) ? "\\n" : ", ");
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

void permutations(string s, string current, vector<string>& res) {
    if (s.empty()) {
        res.push_back(current);
        return;
    }
    for (int i = 0; i < (int)s.length(); i++) {
        string rem = s.substr(0, i) + s.substr(i + 1);
        permutations(rem, current + s[i], res);
    }
}

int main() {
    string s;
    if (cin >> s) {
        vector<string> res;
        permutations(s, "", res);
        for (int i = 0; i < (int)res.size(); i++) {
            cout << res[i] << (i == (int)res.size() - 1 ? "\\n" : ", ");
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void permutations(String s, String current, List<String> res) {
        if (s.isEmpty()) {
            res.add(current);
            return;
        }
        for (int i = 0; i < s.length(); i++) {
            String rem = s.substring(0, i) + s.substring(i + 1);
            permutations(rem, current + s.charAt(i), res);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            List<String> res = new ArrayList<>();
            permutations(s, "", res);
            for (int i = 0; i < res.size(); i++) {
                System.out.print(res.get(i) + (i == res.size() - 1 ? "\\n" : ", "));
            }
        }
    }
}""",
            "python": """import sys

def permutations(s, current="", res=None):
    if res is None:
        res = []
    if len(s) == 0:
        res.append(current)
        return res

    for i in range(len(s)):
        remaining = s[:i] + s[i + 1:]
        permutations(remaining, current + s[i], res)
    return res

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        res = permutations(s)
        print(", ".join(res))"""
        })
    },

    # 9. Combination Sum
    {
        "id": "dsa-rec-combination-sum",
        "problem_num": 129,
        "title": "Combination Sum",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "Unbounded Backtracking",
        "difficulty": "MEDIUM",
        "description": "Given distinct positive integers and target value, find all unique combinations whose sum equals the target. Elements can be used multiple times.",
        "input_format": "N followed by N integers and target on next line.",
        "output_format": "List of lists format (e.g., '[[2, 2, 2], [3, 3], [6]]').",
        "constraints": "1 <= candidates.length <= 30\n1 <= target <= 40",
        "time_complexity": "O(2^target)",
        "space_complexity": "O(target) call stack",
        "company_tags": ["Airbnb", "Amazon", "Apple", "Google"],
        "examples": [
            {"input": "3 2 3 6 6", "output": "[[2, 2, 2], [3, 3], [6]]", "explanation": "Target 6 combinations."},
            {"input": "4 2 3 5 7 7", "output": "[[2, 2, 3], [2, 5], [7]]", "explanation": "Target 7 combinations."},
            {"input": "2 2 4 3", "output": "[]", "explanation": "No combination sums to 3."}
        ],
        "test_cases": [
            {"input": "3 2 3 6 6", "expected": "[[2, 2, 2], [3, 3], [6]]", "is_hidden": False},
            {"input": "4 2 3 5 7 7", "expected": "[[2, 2, 3], [2, 5], [7]]", "is_hidden": False},
            {"input": "2 2 4 3", "expected": "[]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def combinationSum(candidates, target):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

int candidates[40];
int n, target;
int current[50];
int current_len = 0;
int results[500][50];
int res_lens[500];
int res_count = 0;

void backtrack(int start, int total) {
    if (total == target) {
        for (int i = 0; i < current_len; i++) {
            results[res_count][i] = current[i];
        }
        res_lens[res_count] = current_len;
        res_count++;
        return;
    }
    if (total > target) return;

    for (int i = start; i < n; i++) {
        current[current_len++] = candidates[i];
        backtrack(i, total + candidates[i]);
        current_len--;
    }
}

int main() {
    if (scanf("%d", &n) != 1) return 0;
    for (int i = 0; i < n; i++) scanf("%d", &candidates[i]);
    scanf("%d", &target);

    backtrack(0, 0);

    printf("[");
    for (int i = 0; i < res_count; i++) {
        printf("[");
        for (int j = 0; j < res_lens[i]; j++) {
            printf("%d%s", results[i][j], (j == res_lens[i] - 1) ? "" : ", ");
        }
        printf("]%s", (i == res_count - 1) ? "" : ", ");
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

void backtrack(const vector<int>& candidates, int target, int start, int total, vector<int>& current, vector<vector<int> >& result) {
    if (total == target) {
        result.push_back(current);
        return;
    }
    if (total > target) return;

    for (int i = start; i < (int)candidates.size(); i++) {
        current.push_back(candidates[i]);
        backtrack(candidates, target, i, total + candidates[i], current, result);
        current.pop_back();
    }
}

int main() {
    int n;
    if (cin >> n) {
        vector<int> candidates(n);
        for (int i = 0; i < n; i++) cin >> candidates[i];
        int target; cin >> target;

        vector<vector<int> > result;
        vector<int> current;
        backtrack(candidates, target, 0, 0, current, result);

        cout << "[";
        for (int i = 0; i < (int)result.size(); i++) {
            cout << "[";
            for (int j = 0; j < (int)result[i].size(); j++) {
                cout << result[i][j] << (j == (int)result[i].size() - 1 ? "" : ", ");
            }
            cout << "]" << (i == (int)result.size() - 1 ? "" : ", ");
        }
        cout << "]\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void backtrack(int[] candidates, int target, int start, int total, List<Integer> current, List<List<Integer>> result) {
        if (total == target) {
            result.add(new ArrayList<>(current));
            return;
        }
        if (total > target) return;

        for (int i = start; i < candidates.length; i++) {
            current.add(candidates[i]);
            backtrack(candidates, target, i, total + candidates[i], current, result);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] candidates = new int[n];
        for (int i = 0; i < n; i++) candidates[i] = sc.nextInt();
        int target = sc.nextInt();

        List<List<Integer>> result = new ArrayList<>();
        backtrack(candidates, target, 0, 0, new ArrayList<>(), result);

        System.out.print("[");
        for (int i = 0; i < result.size(); i++) {
            System.out.print("[");
            for (int j = 0; j < result.get(i).size(); j++) {
                System.out.print(result.get(i).get(j) + (j == result.get(i).size() - 1 ? "" : ", "));
            }
            System.out.print("]" + (i == result.size() - 1 ? "" : ", "));
        }
        System.out.println("]");
    }
}""",
            "python": """import sys

def combinationSum(candidates, target):
    result = []

    def backtrack(start, current, total):
        if total == target:
            result.append(current[:])
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, total + candidates[i])
            current.pop()

    backtrack(0, [], 0)
    return result

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        candidates = [int(x) for x in tokens[1:1+n]]
        target = int(tokens[1+n])
        print(combinationSum(candidates, target))"""
        })
    },

    # 10. Generate Parentheses
    {
        "id": "dsa-rec-generate-parentheses",
        "problem_num": 130,
        "title": "Generate Parentheses",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "Catalan Backtracking",
        "difficulty": "MEDIUM",
        "description": "Given N pairs of parentheses, generate all combinations of well-formed parentheses.",
        "input_format": "A single positive integer N.",
        "output_format": "List of strings in format (e.g., '[\"(())()\", ...]').",
        "constraints": "1 <= N <= 8",
        "time_complexity": "O(4^N / sqrt(N))",
        "space_complexity": "O(N) call stack",
        "company_tags": ["Amazon", "Google", "Facebook", "Microsoft"],
        "examples": [
            {"input": "1", "output": "[\"()\"]", "explanation": "1 pair gives ()"},
            {"input": "2", "output": "[\"(())\", \"()()\"]", "explanation": "2 pairs"},
            {"input": "3", "output": "[\"((()))\", \"(()())\", \"(())()\", \"()(())\", \"()()()\"]", "explanation": "3 pairs"}
        ],
        "test_cases": [
            {"input": "1", "expected": "[\"()\"]", "is_hidden": False},
            {"input": "2", "expected": "[\"(())\", \"()()\"]", "is_hidden": False},
            {"input": "3", "expected": "[\"((()))\", \"(()())\", \"(())()\", \"()(())\", \"()()()\"]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def generateParenthesis(n):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

char current[50];
char results[5000][50];
int res_count = 0;

void backtrack(int n, int open_count, int close_count, int idx) {
    if (idx == 2 * n) {
        current[idx] = '\\0';
        strcpy(results[res_count++], current);
        return;
    }
    if (open_count < n) {
        current[idx] = '(';
        backtrack(n, open_count + 1, close_count, idx + 1);
    }
    if (close_count < open_count) {
        current[idx] = ')';
        backtrack(n, open_count, close_count + 1, idx + 1);
    }
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    backtrack(n, 0, 0, 0);

    printf("[");
    for (int i = 0; i < res_count; i++) {
        printf("\\\"%s\\\"%s", results[i], (i == res_count - 1) ? "" : ", ");
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

void backtrack(int n, string current, int open_count, int close_count, vector<string>& result) {
    if ((int)current.length() == 2 * n) {
        result.push_back(current);
        return;
    }
    if (open_count < n) {
        backtrack(n, current + "(", open_count + 1, close_count, result);
    }
    if (close_count < open_count) {
        backtrack(n, current + ")", open_count, close_count + 1, result);
    }
}

int main() {
    int n;
    if (cin >> n) {
        vector<string> result;
        backtrack(n, "", 0, 0, result);
        cout << "[";
        for (int i = 0; i < (int)result.size(); i++) {
            cout << "\\\"" << result[i] << "\\\"" << (i == (int)result.size() - 1 ? "" : ", ");
        }
        cout << "]\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void backtrack(int n, String current, int openCount, int closeCount, List<String> result) {
        if (current.length() == 2 * n) {
            result.add(current);
            return;
        }
        if (openCount < n) {
            backtrack(n, current + "(", openCount + 1, closeCount, result);
        }
        if (closeCount < openCount) {
            backtrack(n, current + ")", openCount, closeCount + 1, result);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        List<String> result = new ArrayList<>();
        backtrack(n, "", 0, 0, result);

        System.out.print("[");
        for (int i = 0; i < result.size(); i++) {
            System.out.print("\\\"" + result.get(i) + "\\\"" + (i == result.size() - 1 ? "" : ", "));
        }
        System.out.println("]");
    }
}""",
            "python": """import sys
import json

def generateParenthesis(n):
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        print(json.dumps(generateParenthesis(n)))"""
        })
    },

    # 11. N-Queens Problem
    {
        "id": "dsa-rec-n-queens",
        "problem_num": 131,
        "title": "N-Queens Problem",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "Diagonal Safety Backtracking",
        "difficulty": "HARD",
        "description": "Place N queens on an N x N chessboard so that no two queens attack each other. Return number of distinct solutions.",
        "input_format": "A single integer N.",
        "output_format": "A single integer total solutions.",
        "constraints": "1 <= N <= 12",
        "time_complexity": "O(N!)",
        "space_complexity": "O(N)",
        "company_tags": ["Google", "Amazon", "Microsoft"],
        "examples": [
            {"input": "1", "output": "1", "explanation": "1 solution for 1 queen."},
            {"input": "4", "output": "2", "explanation": "2 solutions for 4 queens."},
            {"input": "5", "output": "10", "explanation": "10 solutions for 5 queens."}
        ],
        "test_cases": [
            {"input": "1", "expected": "1", "is_hidden": False},
            {"input": "4", "expected": "2", "is_hidden": False},
            {"input": "5", "expected": "10", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def totalNQueens(n):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

int cols[20] = {0};
int d1[40] = {0};
int d2[40] = {0};
int total_count = 0;

void backtrack(int row, int n) {
    if (row == n) {
        total_count++;
        return;
    }
    for (int col = 0; col < n; col++) {
        int diag1 = row - col + n;
        int diag2 = row + col;
        if (cols[col] || d1[diag1] || d2[diag2]) continue;

        cols[col] = 1;
        d1[diag1] = 1;
        d2[diag2] = 1;

        backtrack(row + 1, n);

        cols[col] = 0;
        d1[diag1] = 0;
        d2[diag2] = 0;
    }
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    backtrack(0, n);
    printf("%d\\n", total_count);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

int total_count = 0;
int cols[20] = {0};
int d1[40] = {0};
int d2[40] = {0};

void backtrack(int row, int n) {
    if (row == n) {
        total_count++;
        return;
    }
    for (int col = 0; col < n; col++) {
        int diag1 = row - col + n;
        int diag2 = row + col;
        if (cols[col] || d1[diag1] || d2[diag2]) continue;

        cols[col] = 1;
        d1[diag1] = 1;
        d2[diag2] = 1;

        backtrack(row + 1, n);

        cols[col] = 0;
        d1[diag1] = 0;
        d2[diag2] = 0;
    }
}

int main() {
    int n;
    if (cin >> n) {
        backtrack(0, n);
        cout << total_count << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static int totalCount = 0;
    static boolean[] cols = new boolean[20];
    static boolean[] d1 = new boolean[40];
    static boolean[] d2 = new boolean[40];

    public static void backtrack(int row, int n) {
        if (row == n) {
            totalCount++;
            return;
        }
        for (int col = 0; col < n; col++) {
            int diag1 = row - col + n;
            int diag2 = row + col;
            if (cols[col] || d1[diag1] || d2[diag2]) continue;

            cols[col] = true;
            d1[diag1] = true;
            d2[diag2] = true;

            backtrack(row + 1, n);

            cols[col] = false;
            d1[diag1] = false;
            d2[diag2] = false;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        backtrack(0, n);
        System.out.println(totalCount);
    }
}""",
            "python": """import sys

def totalNQueens(n):
    count = 0
    cols = set()
    diagonals1 = set()
    diagonals2 = set()

    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return

        for col in range(n):
            d1 = row - col
            d2 = row + col
            if col in cols or d1 in diagonals1 or d2 in diagonals2:
                continue

            cols.add(col)
            diagonals1.add(d1)
            diagonals2.add(d2)

            backtrack(row + 1)

            cols.remove(col)
            diagonals1.remove(d1)
            diagonals2.remove(d2)

    backtrack(0)
    return count

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        print(totalNQueens(n))"""
        })
    },

    # 12. Sudoku Solver
    {
        "id": "dsa-rec-sudoku-solver",
        "problem_num": 132,
        "title": "Sudoku Solver",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "Constraint Satisfaction Backtracking",
        "difficulty": "HARD",
        "description": "Given a 9x9 board with empty cells marked as '.', fill all cells so each row, column, and 3x3 box contains digits 1-9.",
        "input_format": "81 tokens representing the 9x9 board.",
        "output_format": "Solved 9x9 board with rows on separate lines.",
        "constraints": "Board is 9x9, uniquely solvable.",
        "time_complexity": "O(9^(empty cells))",
        "space_complexity": "O(1) (recursion depth <= 81)",
        "company_tags": ["Google", "Microsoft", "Uber"],
        "examples": [
            {
                "input": "5 3 . . 7 . . . . 6 . . 1 9 5 . . . . 9 8 . . . . 6 . 8 . . . 6 . . . 3 4 . . 8 . 3 . . 1 7 . . . 2 . . . 6 . 6 . . . . 2 8 . . . . 4 1 9 . . 5 . . . . 8 . . 7 9",
                "output": "5 3 4 6 7 8 9 1 2\n6 7 2 1 9 5 3 4 8\n1 9 8 3 4 2 5 6 7\n8 5 9 7 6 1 4 2 3\n4 2 6 8 5 3 7 9 1\n7 1 3 9 2 4 8 5 6\n9 6 1 5 3 7 2 8 4\n2 8 7 4 1 9 6 3 5\n3 4 5 2 8 6 1 7 9",
                "explanation": "Completed Sudoku solution."
            }
        ],
        "test_cases": [
            {
                "input": "5 3 . . 7 . . . . 6 . . 1 9 5 . . . . 9 8 . . . . 6 . 8 . . . 6 . . . 3 4 . . 8 . 3 . . 1 7 . . . 2 . . . 6 . 6 . . . . 2 8 . . . . 4 1 9 . . 5 . . . . 8 . . 7 9",
                "expected": "5 3 4 6 7 8 9 1 2\n6 7 2 1 9 5 3 4 8\n1 9 8 3 4 2 5 6 7\n8 5 9 7 6 1 4 2 3\n4 2 6 8 5 3 7 9 1\n7 1 3 9 2 4 8 5 6\n9 6 1 5 3 7 2 8 4\n2 8 7 4 1 9 6 3 5\n3 4 5 2 8 6 1 7 9",
                "is_hidden": False
            }
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def solveSudoku(board):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdbool.h>

char board[9][9];

bool isValid(int row, int col, char num) {
    for (int i = 0; i < 9; i++) {
        if (board[row][i] == num) return false;
        if (board[i][col] == num) return false;
    }
    int sr = (row / 3) * 3;
    int sc = (col / 3) * 3;
    for (int i = sr; i < sr + 3; i++) {
        for (int j = sc; j < sc + 3; j++) {
            if (board[i][j] == num) return false;
        }
    }
    return true;
}

bool backtrack() {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (board[i][j] == '.') {
                for (char num = '1'; num <= '9'; num++) {
                    if (isValid(i, j, num)) {
                        board[i][j] = num;
                        if (backtrack()) return true;
                        board[i][j] = '.';
                    }
                }
                return false;
            }
        }
    }
    return true;
}

int main() {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            char s[5];
            if (scanf("%s", s) != 1) return 0;
            board[i][j] = s[0];
        }
    }
    backtrack();
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            printf("%c%s", board[i][j], (j == 8) ? "\\n" : " ");
        }
    }
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

bool isValid(vector<vector<char> >& board, int row, int col, char num) {
    for (int i = 0; i < 9; i++) {
        if (board[row][i] == num) return false;
        if (board[i][col] == num) return false;
    }
    int sr = (row / 3) * 3, sc = (col / 3) * 3;
    for (int i = sr; i < sr + 3; i++) {
        for (int j = sc; j < sc + 3; j++) {
            if (board[i][j] == num) return false;
        }
    }
    return true;
}

bool backtrack(vector<vector<char> >& board) {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (board[i][j] == '.') {
                for (char num = '1'; num <= '9'; num++) {
                    if (isValid(board, i, j, num)) {
                        board[i][j] = num;
                        if (backtrack(board)) return true;
                        board[i][j] = '.';
                    }
                }
                return false;
            }
        }
    }
    return true;
}

int main() {
    vector<vector<char> > board(9, vector<char>(9));
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) cin >> board[i][j];
    }
    backtrack(board);
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cout << board[i][j] << (j == 8 ? "\\n" : " ");
        }
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static boolean isValid(char[][] board, int row, int col, char num) {
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == num) return false;
            if (board[i][col] == num) return false;
        }
        int sr = (row / 3) * 3, sc = (col / 3) * 3;
        for (int i = sr; i < sr + 3; i++) {
            for (int j = sc; j < sc + 3; j++) {
                if (board[i][j] == num) return false;
            }
        }
        return true;
    }

    public static boolean backtrack(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    for (char num = '1'; num <= '9'; num++) {
                        if (isValid(board, i, j, num)) {
                            board[i][j] = num;
                            if (backtrack(board)) return true;
                            board[i][j] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[][] board = new char[9][9];
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                board[i][j] = sc.next().charAt(0);
            }
        }
        backtrack(board);
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print(board[i][j] + (j == 8 ? "\\n" : " "));
            }
        }
    }
}""",
            "python": """import sys

def solveSudoku(board):
    def isValid(row, col, num):
        for i in range(9):
            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if isValid(i, j, num):
                            board[i][j] = num
                            if backtrack():
                                return True
                            board[i][j] = '.'
                    return False
        return True

    backtrack()
    return board

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if len(tokens) >= 81:
        board = []
        for i in range(9):
            board.append(tokens[i*9:(i+1)*9])
        solveSudoku(board)
        for row in board:
            print(*row)"""
        })
    },

    # 13. Word Search
    {
        "id": "dsa-rec-word-search",
        "problem_num": 133,
        "title": "Word Search",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "2D Grid Path Backtracking",
        "difficulty": "HARD",
        "description": "Given a 2D character board and a word, return True if word exists in grid moving horizontally or vertically.",
        "input_format": "rows cols followed by rows strings and the target word.",
        "output_format": "True if word exists, else False.",
        "constraints": "1 <= rows, cols <= 6\n1 <= word.length <= 15",
        "time_complexity": "O(rows * cols * 4^L)",
        "space_complexity": "O(L) call stack",
        "company_tags": ["Amazon", "Microsoft", "Bloomberg", "Google"],
        "examples": [
            {"input": "3 4 ABCE SFCS ADEE ABCCED", "output": "True", "explanation": "ABCCED found in board."},
            {"input": "3 4 ABCE SFCS ADEE SEE", "output": "True", "explanation": "SEE found in board."},
            {"input": "3 4 ABCE SFCS ADEE ABCB", "output": "False", "explanation": "ABCB cannot reuse cell B."}
        ],
        "test_cases": [
            {"input": "3 4 ABCE SFCS ADEE ABCCED", "expected": "True", "is_hidden": False},
            {"input": "3 4 ABCE SFCS ADEE SEE", "expected": "True", "is_hidden": False},
            {"input": "3 4 ABCE SFCS ADEE ABCB", "expected": "False", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n#include <stdbool.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def exist(board, word):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdbool.h>
#include <string.h>

char board[20][20];
int rows, cols;
char word[100];

bool backtrack(int r, int c, int index) {
    if (index == (int)strlen(word)) return true;
    if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != word[index]) return false;

    char temp = board[r][c];
    board[r][c] = '#';

    bool found = backtrack(r + 1, c, index + 1) ||
                 backtrack(r - 1, c, index + 1) ||
                 backtrack(r, c + 1, index + 1) ||
                 backtrack(r, c - 1, index + 1);

    board[r][c] = temp;
    return found;
}

int main() {
    if (scanf("%d %d", &rows, &cols) != 2) return 0;
    for (int i = 0; i < rows; i++) scanf("%s", board[i]);
    scanf("%s", word);

    bool exists = false;
    for (int i = 0; i < rows && !exists; i++) {
        for (int j = 0; j < cols && !exists; j++) {
            if (backtrack(i, j, 0)) exists = true;
        }
    }
    printf("%s\\n", exists ? "True" : "False");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool backtrack(vector<string>& board, const string& word, int r, int c, int index) {
    if (index == (int)word.length()) return true;
    int rows = board.size(), cols = board[0].size();
    if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != word[index]) return false;

    char temp = board[r][c];
    board[r][c] = '#';

    bool found = backtrack(board, word, r + 1, c, index + 1) ||
                 backtrack(board, word, r - 1, c, index + 1) ||
                 backtrack(board, word, r, c + 1, index + 1) ||
                 backtrack(board, word, r, c - 1, index + 1);

    board[r][c] = temp;
    return found;
}

bool exist(vector<string>& board, string word) {
    int rows = board.size(), cols = board[0].size();
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (backtrack(board, word, i, j, 0)) return true;
        }
    }
    return false;
}

int main() {
    int rows, cols;
    if (cin >> rows >> cols) {
        vector<string> board(rows);
        for (int i = 0; i < rows; i++) cin >> board[i];
        string word; cin >> word;
        cout << (exist(board, word) ? "True" : "False") << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static boolean backtrack(char[][] board, String word, int r, int c, int index) {
        if (index == word.length()) return true;
        int rows = board.length, cols = board[0].length;
        if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != word.charAt(index)) return false;

        char temp = board[r][c];
        board[r][c] = '#';

        boolean found = backtrack(board, word, r + 1, c, index + 1) ||
                        backtrack(board, word, r - 1, c, index + 1) ||
                        backtrack(board, word, r, c + 1, index + 1) ||
                        backtrack(board, word, r, c - 1, index + 1);

        board[r][c] = temp;
        return found;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int rows = sc.nextInt(), cols = sc.nextInt();
        char[][] board = new char[rows][cols];
        for (int i = 0; i < rows; i++) {
            board[i] = sc.next().toCharArray();
        }
        String word = sc.next();

        boolean exists = false;
        for (int i = 0; i < rows && !exists; i++) {
            for (int j = 0; j < cols && !exists; j++) {
                if (backtrack(board, word, i, j, 0)) exists = true;
            }
        }
        System.out.println(exists ? "True" : "False");
    }
}""",
            "python": """import sys

def exist(board, word):
    rows = len(board)
    cols = len(board[0])

    def backtrack(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False

        temp = board[r][c]
        board[r][c] = '#'
        found = (
            backtrack(r + 1, c, index + 1) or
            backtrack(r - 1, c, index + 1) or
            backtrack(r, c + 1, index + 1) or
            backtrack(r, c - 1, index + 1)
        )
        board[r][c] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    return False

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        rows = int(tokens[0])
        cols = int(tokens[1])
        board = [list(tokens[2 + i]) for i in range(rows)]
        word = tokens[2 + rows]
        print(exist(board, word))"""
        })
    },

    # 14. Rat in a Maze
    {
        "id": "dsa-rec-rat-in-maze",
        "problem_num": 134,
        "title": "Rat in a Maze",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "Maze Navigation",
        "difficulty": "HARD",
        "description": "Given an N x N maze (1=open, 0=blocked), find all paths from (0,0) to (N-1, N-1) in lexicographical order (D, L, R, U).",
        "input_format": "N followed by N x N maze values.",
        "output_format": "List of path strings (e.g. \"['DR', 'RD']\").",
        "constraints": "2 <= N <= 5",
        "time_complexity": "O(4^(N^2))",
        "space_complexity": "O(N^2)",
        "company_tags": ["Amazon", "Microsoft", "Paytm"],
        "examples": [
            {"input": "2 1 1 1 1", "output": "['DR', 'RD']", "explanation": "Both paths reach destination."},
            {"input": "3 1 0 0 1 1 0 0 1 1", "output": "['DRDR']", "explanation": "Single valid path DRDR."},
            {"input": "2 1 0 0 1", "output": "[]", "explanation": "Blocked destination."}
        ],
        "test_cases": [
            {"input": "2 1 1 1 1", "expected": "['DR', 'RD']", "is_hidden": False},
            {"input": "3 1 0 0 1 1 0 0 1 1", "expected": "['DRDR']", "is_hidden": False},
            {"input": "2 1 0 0 1", "expected": "[]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def findPaths(maze):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>

int maze[10][10];
int visited[10][10] = {0};
int n;
char path[100];
char results[500][100];
int res_count = 0;

int dr[] = {1, 0, 0, -1};
int dc[] = {0, -1, 1, 0};
char move_ch[] = {'D', 'L', 'R', 'U'};

void backtrack(int r, int c, int len) {
    if (r == n - 1 && c == n - 1) {
        path[len] = '\\0';
        strcpy(results[res_count++], path);
        return;
    }
    visited[r][c] = 1;

    for (int d = 0; d < 4; d++) {
        int nr = r + dr[d];
        int nc = c + dc[d];
        if (nr >= 0 && nr < n && nc >= 0 && nc < n && maze[nr][nc] == 1 && !visited[nr][nc]) {
            path[len] = move_ch[d];
            backtrack(nr, nc, len + 1);
        }
    }
    visited[r][c] = 0;
}

int main() {
    if (scanf("%d", &n) != 1) return 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) scanf("%d", &maze[i][j]);
    }

    if (maze[0][0] == 1 && maze[n - 1][n - 1] == 1) {
        backtrack(0, 0, 0);
    }

    printf("[");
    for (int i = 0; i < res_count; i++) {
        printf("'%s'%s", results[i], (i == res_count - 1) ? "" : ", ");
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int dr[] = {1, 0, 0, -1};
int dc[] = {0, -1, 1, 0};
char move_ch[] = {'D', 'L', 'R', 'U'};

void backtrack(vector<vector<int> >& maze, int n, int r, int c, string path, vector<vector<bool> >& visited, vector<string>& result) {
    if (r == n - 1 && c == n - 1) {
        result.push_back(path);
        return;
    }
    visited[r][c] = true;

    for (int d = 0; d < 4; d++) {
        int nr = r + dr[d], nc = c + dc[d];
        if (nr >= 0 && nr < n && nc >= 0 && nc < n && maze[nr][nc] == 1 && !visited[nr][nc]) {
            backtrack(maze, n, nr, nc, path + move_ch[d], visited, result);
        }
    }
    visited[r][c] = false;
}

int main() {
    int n;
    if (cin >> n) {
        vector<vector<int> > maze(n, vector<int>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) cin >> maze[i][j];
        }

        vector<string> result;
        if (maze[0][0] == 1 && maze[n - 1][n - 1] == 1) {
            vector<vector<bool> > visited(n, vector<bool>(n, false));
            backtrack(maze, n, 0, 0, "", visited, result);
            sort(result.begin(), result.end());
        }

        cout << "[";
        for (int i = 0; i < (int)result.size(); i++) {
            cout << "'" << result[i] << "'" << (i == (int)result.size() - 1 ? "" : ", ");
        }
        cout << "]\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    static int[] dr = {1, 0, 0, -1};
    static int[] dc = {0, -1, 1, 0};
    static char[] moveCh = {'D', 'L', 'R', 'U'};

    public static void backtrack(int[][] maze, int n, int r, int c, String path, boolean[][] visited, List<String> result) {
        if (r == n - 1 && c == n - 1) {
            result.add(path);
            return;
        }
        visited[r][c] = true;

        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && maze[nr][nc] == 1 && !visited[nr][nc]) {
                backtrack(maze, n, nr, nc, path + moveCh[d], visited, result);
            }
        }
        visited[r][c] = false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[][] maze = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) maze[i][j] = sc.nextInt();
        }

        List<String> result = new ArrayList<>();
        if (maze[0][0] == 1 && maze[n - 1][n - 1] == 1) {
            boolean[][] visited = new boolean[n][n];
            backtrack(maze, n, 0, 0, "", visited, result);
            Collections.sort(result);
        }

        System.out.print("[");
        for (int i = 0; i < result.size(); i++) {
            System.out.print("'" + result.get(i) + "'" + (i == result.size() - 1 ? "" : ", "));
        }
        System.out.println("]");
    }
}""",
            "python": """import sys

def findPaths(maze):
    n = len(maze)
    result = []
    if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
        return result

    visited = [[False] * n for _ in range(n)]
    directions = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]

    def backtrack(r, c, path):
        if r == n - 1 and c == n - 1:
            result.append(path)
            return

        visited[r][c] = True
        for dr, dc, move in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1 and not visited[nr][nc]:
                backtrack(nr, nc, path + move)
        visited[r][c] = False

    backtrack(0, 0, "")
    return sorted(result)

if __name__ == '__main__':
    tokens = sys.stdin.read().split()
    if tokens:
        n = int(tokens[0])
        idx = 1
        maze = []
        for _ in range(n):
            maze.append([int(x) for x in tokens[idx:idx+n]])
            idx += n
        print(findPaths(maze))"""
        })
    },

    # 15. Palindrome Partitioning
    {
        "id": "dsa-rec-palindrome-partitioning",
        "problem_num": 135,
        "title": "Palindrome Partitioning",
        "category": "Recursion",
        "topic": "Recursion",
        "subtopic": "Partition Backtracking",
        "difficulty": "HARD",
        "description": "Given a string, partition it such that every substring of the partition is a palindrome. Return all possible palindrome partitionings.",
        "input_format": "A single string s.",
        "output_format": "List of lists format (e.g., \"[['a', 'a', 'b'], ['aa', 'b']]\").",
        "constraints": "1 <= s.length <= 16",
        "time_complexity": "O(N * 2^N)",
        "space_complexity": "O(N) call stack",
        "company_tags": ["Amazon", "Bloomberg", "Google", "Microsoft"],
        "examples": [
            {"input": "aab", "output": "[['a', 'a', 'b'], ['aa', 'b']]", "explanation": "2 valid palindrome partitions."},
            {"input": "a", "output": "[['a']]", "explanation": "Single partition."},
            {"input": "aba", "output": "[['a', 'b', 'a'], ['aba']]", "explanation": "2 palindrome partitions."}
        ],
        "test_cases": [
            {"input": "aab", "expected": "[['a', 'a', 'b'], ['aa', 'b']]", "is_hidden": False},
            {"input": "a", "expected": "[['a']]", "is_hidden": False},
            {"input": "aba", "expected": "[['a', 'b', 'a'], ['aba']]", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n    }\n}",
            "python": "def partition(s):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <string.h>
#include <stdbool.h>

char s[20];
int n;
char current[20][20];
int cur_len = 0;
char results[500][20][20];
int res_lens[500];
int res_count = 0;

bool isPalindrome(char *str, int start, int end) {
    while (start < end) {
        if (str[start++] != str[end--]) return false;
    }
    return true;
}

void backtrack(int start) {
    if (start == n) {
        for (int i = 0; i < cur_len; i++) {
            strcpy(results[res_count][i], current[i]);
        }
        res_lens[res_count++] = cur_len;
        return;
    }
    for (int end = start; end < n; end++) {
        if (isPalindrome(s, start, end)) {
            int sub_len = end - start + 1;
            strncpy(current[cur_len], s + start, sub_len);
            current[cur_len][sub_len] = '\\0';
            cur_len++;

            backtrack(end + 1);

            cur_len--;
        }
    }
}

int main() {
    if (scanf("%s", s) != 1) return 0;
    n = strlen(s);
    backtrack(0);

    printf("[");
    for (int i = 0; i < res_count; i++) {
        printf("[");
        for (int j = 0; j < res_lens[i]; j++) {
            printf("'%s'%s", results[i][j], (j == res_lens[i] - 1) ? "" : ", ");
        }
        printf("]%s", (i == res_count - 1) ? "" : ", ");
    }
    printf("]\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isPalindrome(const string& text, int start, int end) {
    while (start < end) {
        if (text[start++] != text[end--]) return false;
    }
    return true;
}

void backtrack(const string& s, int start, vector<string>& current, vector<vector<string> >& result) {
    if (start == (int)s.length()) {
        result.push_back(current);
        return;
    }
    for (int end = start; end < (int)s.length(); end++) {
        if (isPalindrome(s, start, end)) {
            current.push_back(s.substr(start, end - start + 1));
            backtrack(s, end + 1, current, result);
            current.pop_back();
        }
    }
}

int main() {
    string s;
    if (cin >> s) {
        vector<vector<string> > result;
        vector<string> current;
        backtrack(s, 0, current, result);

        cout << "[";
        for (int i = 0; i < (int)result.size(); i++) {
            cout << "[";
            for (int j = 0; j < (int)result[i].size(); j++) {
                cout << "'" << result[i][j] << "'" << (j == (int)result[i].size() - 1 ? "" : ", ");
            }
            cout << "]" << (i == (int)result.size() - 1 ? "" : ", ");
        }
        cout << "]\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static boolean isPalindrome(String text, int start, int end) {
        while (start < end) {
            if (text.charAt(start++) != text.charAt(end--)) return false;
        }
        return true;
    }

    public static void backtrack(String s, int start, List<String> current, List<List<String>> result) {
        if (start == s.length()) {
            result.add(new ArrayList<>(current));
            return;
        }
        for (int end = start; end < s.length(); end++) {
            if (isPalindrome(s, start, end)) {
                current.add(s.substring(start, end + 1));
                backtrack(s, end + 1, current, result);
                current.remove(current.size() - 1);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        String s = sc.next();
        List<List<String>> result = new ArrayList<>();
        backtrack(s, 0, new ArrayList<>(), result);

        System.out.print("[");
        for (int i = 0; i < result.size(); i++) {
            System.out.print("[");
            for (int j = 0; j < result.get(i).size(); j++) {
                System.out.print("'" + result.get(i).get(j) + "'" + (j == result.get(i).size() - 1 ? "" : ", "));
            }
            System.out.print("]" + (i == result.size() - 1 ? "" : ", "));
        }
        System.out.println("]");
    }
}""",
            "python": """import sys

def partition(s):
    result = []

    def isPalindrome(text):
        return text == text[::-1]

    def backtrack(start, current):
        if start == len(s):
            result.append(current[:])
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if isPalindrome(substring):
                current.append(substring)
                backtrack(end, current)
                current.pop()

    backtrack(0, [])
    return result

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        print(partition(s))"""
        })
    }
]

problems.extend(rec_data)

with open("backend/app/data/dsa_problems_seed.json", "w", encoding="utf-8") as f:
    json.dump(problems, f, indent=2)

print(f"Successfully added 15 Recursion problems! Total problems now: {len(problems)}")

