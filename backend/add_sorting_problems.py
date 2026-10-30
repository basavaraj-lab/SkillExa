import sys, os
sys.path.insert(0, os.path.abspath('.'))
import json

with open("backend/app/data/dsa_problems_seed.json", "r", encoding="utf-8") as f:
    problems = json.load(f)

# Ensure existing list doesn't have duplicates of our new IDs
new_ids = {
    "dsa-sort-array", "dsa-sort-bubble", "dsa-sort-selection", "dsa-sort-insertion",
    "dsa-sort-012", "dsa-sort-colors", "dsa-sort-merge-sorted-array", "dsa-sort-merge-sort",
    "dsa-sort-frequency", "dsa-sort-min-platforms", "dsa-sort-count-inversions",
    "dsa-sort-reverse-pairs", "dsa-sort-largest-number", "dsa-sort-median-two-sorted-arrays",
    "dsa-sort-count-smaller"
}
problems = [p for p in problems if p["id"] not in new_ids]

sorting_problems_data = [
    # 1. Sort an Array
    {
        "id": "dsa-sort-array",
        "problem_num": 61,
        "title": "Sort an Array",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "Comparison Sort",
        "difficulty": "EASY",
        "description": "Given an array of integers, sort the array in ascending order without using any built-in sorting function.",
        "input_format": "Space-separated integers representing the array elements.",
        "output_format": "Space-separated sorted integers in ascending order.",
        "constraints": "1 <= arr.length <= 10^4\n-10^5 <= arr[i] <= 10^5",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(1)",
        "company_tags": ["Amazon", "TCS", "Infosys"],
        "examples": [
            {"input": "5 2 8 1 3", "output": "1 2 3 5 8", "explanation": "Sorted in ascending order."},
            {"input": "9 7 5 3 1", "output": "1 3 5 7 9", "explanation": "Reversed array sorted."},
            {"input": "4 4 2 1 2", "output": "1 2 2 4 4", "explanation": "Array with duplicates sorted."}
        ],
        "test_cases": [
            {"input": "5 2 8 1 3", "expected": "1 2 3 5 8", "is_hidden": False},
            {"input": "9 7 5 3 1", "expected": "1 3 5 7 9", "is_hidden": False},
            {"input": "4 4 2 1 2", "expected": "1 2 2 4 4", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nvoid sortArray(int arr[], int n) {\n    // Your code here\n}\n\nint main() {\n    int arr[10000], n = 0;\n    while (scanf(\"%d\", &arr[n]) == 1) n++;\n    sortArray(arr, n);\n    for (int i = 0; i < n; i++) printf(\"%d%c\", arr[i], i == n - 1 ? '\\n' : ' ');\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvoid sortArray(vector<int>& arr) {\n    // Your code here\n}\n\nint main() {\n    vector<int> arr; int x;\n    while (cin >> x) arr.push_back(x);\n    sortArray(arr);\n    for (int i = 0; i < (int)arr.size(); i++) cout << arr[i] << (i == (int)arr.size() - 1 ? \"\\n\" : \" \");\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void sortArray(int[] arr) {\n        // Your code here\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] arr = list.stream().mapToInt(i -> i).toArray();\n        sortArray(arr);\n        for (int i = 0; i < arr.length; i++) System.out.print(arr[i] + (i == arr.length - 1 ? \"\\n\" : \" \"));\n    }\n}",
            "python": "def sortArray(arr):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    arr = list(map(int, input().split()))\n    res = sortArray(arr)\n    print(*res)"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

void sortArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main() {
    int arr[10000], n = 0;
    while (scanf("%d", &arr[n]) == 1) n++;
    sortArray(arr, n);
    for (int i = 0; i < n; i++) printf("%d%c", arr[i], i == n - 1 ? '\\n' : ' ');
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

void sortArray(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                swap(arr[i], arr[j]);
            }
        }
    }
}

int main() {
    vector<int> arr; int x;
    while (cin >> x) arr.push_back(x);
    sortArray(arr);
    for (int i = 0; i < (int)arr.size(); i++) cout << arr[i] << (i == (int)arr.size() - 1 ? "\\n" : " ");
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void sortArray(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[i] > arr[j]) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] arr = list.stream().mapToInt(i -> i).toArray();
        sortArray(arr);
        for (int i = 0; i < arr.length; i++) System.out.print(arr[i] + (i == arr.length - 1 ? "\\n" : " "));
    }
}""",
            "python": """def sortArray(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(*sortArray(arr))"""
        })
    },

    # 2. Bubble Sort
    {
        "id": "dsa-sort-bubble",
        "problem_num": 62,
        "title": "Bubble Sort",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "Bubble Sort",
        "difficulty": "EASY",
        "description": "Given an array of integers, sort it using Bubble Sort by comparing adjacent elements and swapping them if they are in the wrong order.",
        "input_format": "Space-separated integers.",
        "output_format": "Space-separated sorted integers.",
        "constraints": "1 <= arr.length <= 10^4\n-10^5 <= arr[i] <= 10^5",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(1)",
        "company_tags": ["Wipro", "TCS", "Accenture"],
        "examples": [
            {"input": "5 3 8 2 1", "output": "1 2 3 5 8", "explanation": "Bubble sort passes."},
            {"input": "1 2 3 4 5", "output": "1 2 3 4 5", "explanation": "Already sorted."},
            {"input": "9 7 5 3", "output": "3 5 7 9", "explanation": "Reversed array sorted."}
        ],
        "test_cases": [
            {"input": "5 3 8 2 1", "expected": "1 2 3 5 8", "is_hidden": False},
            {"input": "1 2 3 4 5", "expected": "1 2 3 4 5", "is_hidden": False},
            {"input": "9 7 5 3", "expected": "3 5 7 9", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nvoid bubbleSort(int arr[], int n) {\n    // Your code here\n}\n\nint main() {\n    int arr[10000], n = 0;\n    while (scanf(\"%d\", &arr[n]) == 1) n++;\n    bubbleSort(arr, n);\n    for (int i = 0; i < n; i++) printf(\"%d%c\", arr[i], i == n - 1 ? '\\n' : ' ');\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvoid bubbleSort(vector<int>& arr) {\n    // Your code here\n}\n\nint main() {\n    vector<int> arr; int x;\n    while (cin >> x) arr.push_back(x);\n    bubbleSort(arr);\n    for (int i = 0; i < (int)arr.size(); i++) cout << arr[i] << (i == (int)arr.size() - 1 ? \"\\n\" : \" \");\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void bubbleSort(int[] arr) {\n        // Your code here\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] arr = list.stream().mapToInt(i -> i).toArray();\n        bubbleSort(arr);\n        for (int i = 0; i < arr.length; i++) System.out.print(arr[i] + (i == arr.length - 1 ? \"\\n\" : \" \"));\n    }\n}",
            "python": "def bubbleSort(arr):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    arr = list(map(int, input().split()))\n    print(*bubbleSort(arr))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int arr[10000], n = 0;
    while (scanf("%d", &arr[n]) == 1) n++;
    bubbleSort(arr, n);
    for (int i = 0; i < n; i++) printf("%d%c", arr[i], i == n - 1 ? '\\n' : ' ');
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int main() {
    vector<int> arr; int x;
    while (cin >> x) arr.push_back(x);
    bubbleSort(arr);
    for (int i = 0; i < (int)arr.size(); i++) cout << arr[i] << (i == (int)arr.size() - 1 ? "\\n" : " ");
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] arr = list.stream().mapToInt(i -> i).toArray();
        bubbleSort(arr);
        for (int i = 0; i < arr.length; i++) System.out.print(arr[i] + (i == arr.length - 1 ? "\\n" : " "));
    }
}""",
            "python": """def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(*bubbleSort(arr))"""
        })
    },

    # 3. Selection Sort
    {
        "id": "dsa-sort-selection",
        "problem_num": 63,
        "title": "Selection Sort",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "Selection Sort",
        "difficulty": "EASY",
        "description": "Given an array, sort it using Selection Sort. Repeatedly find the minimum element from the unsorted portion and place it at the beginning.",
        "input_format": "Space-separated integers.",
        "output_format": "Space-separated sorted integers.",
        "constraints": "1 <= arr.length <= 10^4\n-10^5 <= arr[i] <= 10^5",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(1)",
        "company_tags": ["Cognizant", "Infosys"],
        "examples": [
            {"input": "64 25 12 22 11", "output": "11 12 22 25 64", "explanation": "Sorted using selection sort."},
            {"input": "5 4 3 2 1", "output": "1 2 3 4 5", "explanation": "Reversed array sorted."},
            {"input": "10 10 5 2", "output": "2 5 10 10", "explanation": "Array with duplicate elements sorted."}
        ],
        "test_cases": [
            {"input": "64 25 12 22 11", "expected": "11 12 22 25 64", "is_hidden": False},
            {"input": "5 4 3 2 1", "expected": "1 2 3 4 5", "is_hidden": False},
            {"input": "10 10 5 2", "expected": "2 5 10 10", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nvoid selectionSort(int arr[], int n) {\n    // Your code here\n}\n\nint main() {\n    int arr[10000], n = 0;\n    while (scanf(\"%d\", &arr[n]) == 1) n++;\n    selectionSort(arr, n);\n    for (int i = 0; i < n; i++) printf(\"%d%c\", arr[i], i == n - 1 ? '\\n' : ' ');\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvoid selectionSort(vector<int>& arr) {\n    // Your code here\n}\n\nint main() {\n    vector<int> arr; int x;\n    while (cin >> x) arr.push_back(x);\n    selectionSort(arr);\n    for (int i = 0; i < (int)arr.size(); i++) cout << arr[i] << (i == (int)arr.size() - 1 ? \"\\n\" : \" \");\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void selectionSort(int[] arr) {\n        // Your code here\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] arr = list.stream().mapToInt(i -> i).toArray();\n        selectionSort(arr);\n        for (int i = 0; i < arr.length; i++) System.out.print(arr[i] + (i == arr.length - 1 ? \"\\n\" : \" \"));\n    }\n}",
            "python": "def selectionSort(arr):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    arr = list(map(int, input().split()))\n    print(*selectionSort(arr))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        int min_index = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_index]) {
                min_index = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[min_index];
        arr[min_index] = temp;
    }
}

int main() {
    int arr[10000], n = 0;
    while (scanf("%d", &arr[n]) == 1) n++;
    selectionSort(arr, n);
    for (int i = 0; i < n; i++) printf("%d%c", arr[i], i == n - 1 ? '\\n' : ' ');
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        int min_index = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_index]) {
                min_index = j;
            }
        }
        swap(arr[i], arr[min_index]);
    }
}

int main() {
    vector<int> arr; int x;
    while (cin >> x) arr.push_back(x);
    selectionSort(arr);
    for (int i = 0; i < (int)arr.size(); i++) cout << arr[i] << (i == (int)arr.size() - 1 ? "\\n" : " ");
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            int min_index = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[min_index]) {
                    min_index = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[min_index];
            arr[min_index] = temp;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] arr = list.stream().mapToInt(i -> i).toArray();
        selectionSort(arr);
        for (int i = 0; i < arr.length; i++) System.out.print(arr[i] + (i == arr.length - 1 ? "\\n" : " "));
    }
}""",
            "python": """def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(*selectionSort(arr))"""
        })
    },

    # 4. Insertion Sort
    {
        "id": "dsa-sort-insertion",
        "problem_num": 64,
        "title": "Insertion Sort",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "Insertion Sort",
        "difficulty": "EASY",
        "description": "Given an array of integers, sort it using Insertion Sort by inserting each element into its correct position in the already sorted portion.",
        "input_format": "Space-separated integers.",
        "output_format": "Space-separated sorted integers.",
        "constraints": "1 <= arr.length <= 10^4\n-10^5 <= arr[i] <= 10^5",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(1)",
        "company_tags": ["TCS", "Accenture", "Capgemini"],
        "examples": [
            {"input": "12 11 13 5 6", "output": "5 6 11 12 13", "explanation": "Sorted array using insertion sort."},
            {"input": "1 2 3 4", "output": "1 2 3 4", "explanation": "Already sorted."},
            {"input": "9 7 5 3 1", "output": "1 3 5 7 9", "explanation": "Reversed array sorted."}
        ],
        "test_cases": [
            {"input": "12 11 13 5 6", "expected": "5 6 11 12 13", "is_hidden": False},
            {"input": "1 2 3 4", "expected": "1 2 3 4", "is_hidden": False},
            {"input": "9 7 5 3 1", "expected": "1 3 5 7 9", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nvoid insertionSort(int arr[], int n) {\n    // Your code here\n}\n\nint main() {\n    int arr[10000], n = 0;\n    while (scanf(\"%d\", &arr[n]) == 1) n++;\n    insertionSort(arr, n);\n    for (int i = 0; i < n; i++) printf(\"%d%c\", arr[i], i == n - 1 ? '\\n' : ' ');\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvoid insertionSort(vector<int>& arr) {\n    // Your code here\n}\n\nint main() {\n    vector<int> arr; int x;\n    while (cin >> x) arr.push_back(x);\n    insertionSort(arr);\n    for (int i = 0; i < (int)arr.size(); i++) cout << arr[i] << (i == (int)arr.size() - 1 ? \"\\n\" : \" \");\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void insertionSort(int[] arr) {\n        // Your code here\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] arr = list.stream().mapToInt(i -> i).toArray();\n        insertionSort(arr);\n        for (int i = 0; i < arr.length; i++) System.out.print(arr[i] + (i == arr.length - 1 ? \"\\n\" : \" \"));\n    }\n}",
            "python": "def insertionSort(arr):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    arr = list(map(int, input().split()))\n    print(*insertionSort(arr))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int arr[10000], n = 0;
    while (scanf("%d", &arr[n]) == 1) n++;
    insertionSort(arr, n);
    for (int i = 0; i < n; i++) printf("%d%c", arr[i], i == n - 1 ? '\\n' : ' ');
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
    vector<int> arr; int x;
    while (cin >> x) arr.push_back(x);
    insertionSort(arr);
    for (int i = 0; i < (int)arr.size(); i++) cout << arr[i] << (i == (int)arr.size() - 1 ? "\\n" : " ");
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] arr = list.stream().mapToInt(i -> i).toArray();
        insertionSort(arr);
        for (int i = 0; i < arr.length; i++) System.out.print(arr[i] + (i == arr.length - 1 ? "\\n" : " "));
    }
}""",
            "python": """def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(*insertionSort(arr))"""
        })
    },

    # 5. Sort an Array of 0s, 1s and 2s
    {
        "id": "dsa-sort-012",
        "problem_num": 65,
        "title": "Sort an Array of 0s, 1s and 2s",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "Dutch National Flag",
        "difficulty": "EASY",
        "description": "Given an array containing only 0s, 1s and 2s, sort the array in ascending order in linear time without using a built-in sorting function.",
        "input_format": "Space-separated integers 0, 1, or 2.",
        "output_format": "Space-separated sorted integers.",
        "constraints": "1 <= arr.length <= 10^5\narr[i] in {0, 1, 2}",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "company_tags": ["Amazon", "Microsoft", "Paytm"],
        "examples": [
            {"input": "2 0 2 1 1 0", "output": "0 0 1 1 2 2", "explanation": "Sorted in-place."},
            {"input": "2 2 1 0", "output": "0 1 2 2", "explanation": "Sorted in-place."},
            {"input": "0 0 0 1 1", "output": "0 0 0 1 1", "explanation": "Already sorted."}
        ],
        "test_cases": [
            {"input": "2 0 2 1 1 0", "expected": "0 0 1 1 2 2", "is_hidden": False},
            {"input": "2 2 1 0", "expected": "0 1 2 2", "is_hidden": False},
            {"input": "0 0 0 1 1", "expected": "0 0 0 1 1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nvoid sort012(int arr[], int n) {\n    // Your code here\n}\n\nint main() {\n    int arr[100000], n = 0;\n    while (scanf(\"%d\", &arr[n]) == 1) n++;\n    sort012(arr, n);\n    for (int i = 0; i < n; i++) printf(\"%d%c\", arr[i], i == n - 1 ? '\\n' : ' ');\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvoid sort012(vector<int>& arr) {\n    // Your code here\n}\n\nint main() {\n    vector<int> arr; int x;\n    while (cin >> x) arr.push_back(x);\n    sort012(arr);\n    for (int i = 0; i < (int)arr.size(); i++) cout << arr[i] << (i == (int)arr.size() - 1 ? \"\\n\" : \" \");\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void sort012(int[] arr) {\n        // Your code here\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] arr = list.stream().mapToInt(i -> i).toArray();\n        sort012(arr);\n        for (int i = 0; i < arr.length; i++) System.out.print(arr[i] + (i == arr.length - 1 ? \"\\n\" : \" \"));\n    }\n}",
            "python": "def sort012(arr):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    arr = list(map(int, input().split()))\n    print(*sort012(arr))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

void sort012(int arr[], int n) {
    int low = 0, mid = 0, high = n - 1;
    while (mid <= high) {
        if (arr[mid] == 0) {
            int temp = arr[low];
            arr[low] = arr[mid];
            arr[mid] = temp;
            low++;
            mid++;
        } else if (arr[mid] == 1) {
            mid++;
        } else {
            int temp = arr[mid];
            arr[mid] = arr[high];
            arr[high] = temp;
            high--;
        }
    }
}

int main() {
    int arr[100000], n = 0;
    while (scanf("%d", &arr[n]) == 1) n++;
    sort012(arr, n);
    for (int i = 0; i < n; i++) printf("%d%c", arr[i], i == n - 1 ? '\\n' : ' ');
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

void sort012(vector<int>& arr) {
    int low = 0, mid = 0, high = (int)arr.size() - 1;
    while (mid <= high) {
        if (arr[mid] == 0) {
            swap(arr[low], arr[mid]);
            low++;
            mid++;
        } else if (arr[mid] == 1) {
            mid++;
        } else {
            swap(arr[mid], arr[high]);
            high--;
        }
    }
}

int main() {
    vector<int> arr; int x;
    while (cin >> x) arr.push_back(x);
    sort012(arr);
    for (int i = 0; i < (int)arr.size(); i++) cout << arr[i] << (i == (int)arr.size() - 1 ? "\\n" : " ");
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void sort012(int[] arr) {
        int low = 0, mid = 0, high = arr.length - 1;
        while (mid <= high) {
            if (arr[mid] == 0) {
                int temp = arr[low];
                arr[low] = arr[mid];
                arr[mid] = temp;
                low++;
                mid++;
            } else if (arr[mid] == 1) {
                mid++;
            } else {
                int temp = arr[mid];
                arr[mid] = arr[high];
                arr[high] = temp;
                high--;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] arr = list.stream().mapToInt(i -> i).toArray();
        sort012(arr);
        for (int i = 0; i < arr.length; i++) System.out.print(arr[i] + (i == arr.length - 1 ? "\\n" : " "));
    }
}""",
            "python": """def sort012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(*sort012(arr))"""
        })
    },

    # 6. Sort Colors
    {
        "id": "dsa-sort-colors",
        "problem_num": 66,
        "title": "Sort Colors",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "In-place Array Partition",
        "difficulty": "MEDIUM",
        "description": "Given an array containing red, white and blue objects represented by 0, 1 and 2 respectively, sort the array in-place so that objects of the same color are adjacent in the order 0, 1 and 2.",
        "input_format": "Space-separated integers 0, 1, or 2.",
        "output_format": "Space-separated sorted integers.",
        "constraints": "1 <= nums.length <= 300\nnums[i] is either 0, 1, or 2.",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)",
        "company_tags": ["Microsoft", "Amazon", "Facebook"],
        "examples": [
            {"input": "2 0 2 1 1 0", "output": "0 0 1 1 2 2", "explanation": "Sorted in-place."},
            {"input": "2 0 1", "output": "0 1 2", "explanation": "Sorted in-place."},
            {"input": "0 0 1 1 2 2", "output": "0 0 1 1 2 2", "explanation": "Already sorted."}
        ],
        "test_cases": [
            {"input": "2 0 2 1 1 0", "expected": "0 0 1 1 2 2", "is_hidden": False},
            {"input": "2 0 1", "expected": "0 1 2", "is_hidden": False},
            {"input": "0 0 1 1 2 2", "expected": "0 0 1 1 2 2", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nvoid sortColors(int nums[], int n) {\n    // Your code here\n}\n\nint main() {\n    int nums[500], n = 0;\n    while (scanf(\"%d\", &nums[n]) == 1) n++;\n    sortColors(nums, n);\n    for (int i = 0; i < n; i++) printf(\"%d%c\", nums[i], i == n - 1 ? '\\n' : ' ');\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvoid sortColors(vector<int>& nums) {\n    // Your code here\n}\n\nint main() {\n    vector<int> nums; int x;\n    while (cin >> x) nums.push_back(x);\n    sortColors(nums);\n    for (int i = 0; i < (int)nums.size(); i++) cout << nums[i] << (i == (int)nums.size() - 1 ? \"\\n\" : \" \");\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void sortColors(int[] nums) {\n        // Your code here\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] nums = list.stream().mapToInt(i -> i).toArray();\n        sortColors(nums);\n        for (int i = 0; i < nums.length; i++) System.out.print(nums[i] + (i == nums.length - 1 ? \"\\n\" : \" \"));\n    }\n}",
            "python": "def sortColors(nums):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    nums = list(map(int, input().split()))\n    print(*sortColors(nums))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

void sortColors(int nums[], int n) {
    int low = 0, mid = 0, high = n - 1;
    while (mid <= high) {
        if (nums[mid] == 0) {
            int temp = nums[low];
            nums[low] = nums[mid];
            nums[mid] = temp;
            low++;
            mid++;
        } else if (nums[mid] == 1) {
            mid++;
        } else {
            int temp = nums[mid];
            nums[mid] = nums[high];
            nums[high] = temp;
            high--;
        }
    }
}

int main() {
    int nums[500], n = 0;
    while (scanf("%d", &nums[n]) == 1) n++;
    sortColors(nums, n);
    for (int i = 0; i < n; i++) printf("%d%c", nums[i], i == n - 1 ? '\\n' : ' ');
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0, mid = 0, high = (int)nums.size() - 1;
    while (mid <= high) {
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        } else if (nums[mid] == 1) {
            mid++;
        } else {
            swap(nums[mid], nums[high]);
            high--;
        }
    }
}

int main() {
    vector<int> nums; int x;
    while (cin >> x) nums.push_back(x);
    sortColors(nums);
    for (int i = 0; i < (int)nums.size(); i++) cout << nums[i] << (i == (int)nums.size() - 1 ? "\\n" : " ");
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                int temp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = temp;
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                int temp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = temp;
                high--;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] nums = list.stream().mapToInt(i -> i).toArray();
        sortColors(nums);
        for (int i = 0; i < nums.length; i++) System.out.print(nums[i] + (i == nums.length - 1 ? "\\n" : " "));
    }
}""",
            "python": """def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(*sortColors(nums))"""
        })
    },

    # 7. Merge Sorted Array
    {
        "id": "dsa-sort-merge-sorted-array",
        "problem_num": 67,
        "title": "Merge Sorted Array",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "Two Pointers Merge",
        "difficulty": "MEDIUM",
        "description": "Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array in-place from the end.",
        "input_format": "Line 1: m and n\nLine 2: m integers of nums1 followed by n zeros\nLine 3: n integers of nums2",
        "output_format": "Space-separated merged sorted integers.",
        "constraints": "nums1.length == m + n\n0 <= m, n <= 200",
        "time_complexity": "O(m + n)",
        "space_complexity": "O(1)",
        "company_tags": ["Facebook", "Microsoft", "Google"],
        "examples": [
            {"input": "3 3\\n1 2 3 0 0 0\\n2 5 6", "output": "1 2 2 3 5 6", "explanation": "Merged [1,2,3] and [2,5,6]."},
            {"input": "1 0\\n1\\n", "output": "1", "explanation": "nums2 is empty."},
            {"input": "0 1\\n0\\n1", "output": "1", "explanation": "nums1 originally empty."}
        ],
        "test_cases": [
            {"input": "3 3\n1 2 3 0 0 0\n2 5 6", "expected": "1 2 2 3 5 6", "is_hidden": False},
            {"input": "1 0\n1", "expected": "1", "is_hidden": False},
            {"input": "0 1\n0\n1", "expected": "1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nvoid merge(int nums1[], int m, int nums2[], int n) {\n    // Your code here\n}\n\nint main() {\n    int m, n;\n    if (scanf(\"%d %d\", &m, &n) != 2) return 0;\n    int nums1[500], nums2[500];\n    for (int i = 0; i < m + n; i++) scanf(\"%d\", &nums1[i]);\n    for (int i = 0; i < n; i++) scanf(\"%d\", &nums2[i]);\n    merge(nums1, m, nums2, n);\n    for (int i = 0; i < m + n; i++) printf(\"%d%c\", nums1[i], i == m + n - 1 ? '\\n' : ' ');\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvoid merge(vector<int>& nums1, int m, const vector<int>& nums2, int n) {\n    // Your code here\n}\n\nint main() {\n    int m, n;\n    if (cin >> m >> n) {\n        vector<int> nums1(m + n), nums2(n);\n        for (int i = 0; i < m + n; i++) cin >> nums1[i];\n        for (int i = 0; i < n; i++) cin >> nums2[i];\n        merge(nums1, m, nums2, n);\n        for (int i = 0; i < m + n; i++) cout << nums1[i] << (i == m + n - 1 ? \"\\n\" : \" \");\n    }\n    return 0;\n}",
            "java": "import java.util.Scanner;\n\npublic class Main {\n    public static void merge(int[] nums1, int m, int[] nums2, int n) {\n        // Your code here\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int m = sc.nextInt(), n = sc.nextInt();\n            int[] nums1 = new int[m + n];\n            for (int i = 0; i < m + n; i++) nums1[i] = sc.nextInt();\n            int[] nums2 = new int[n];\n            for (int i = 0; i < n; i++) nums2[i] = sc.nextInt();\n            merge(nums1, m, nums2, n);\n            for (int i = 0; i < m + n; i++) System.out.print(nums1[i] + (i == m + n - 1 ? \"\\n\" : \" \"));\n        }\n    }\n}",
            "python": "def merge(nums1, m, nums2, n):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    import sys\n    lines = sys.stdin.read().split()\n    if lines:\n        m, n = int(lines[0]), int(lines[1])\n        nums1 = [int(x) for x in lines[2:2 + m + n]]\n        nums2 = [int(x) for x in lines[2 + m + n:2 + m + n + n]]\n        print(*merge(nums1, m, nums2, n))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>

void merge(int nums1[], int m, int nums2[], int n) {
    int i = m - 1;
    int j = n - 1;
    int k = m + n - 1;

    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[k] = nums1[i];
            i--;
        } else {
            nums1[k] = nums2[j];
            j--;
        }
        k--;
    }
}

int main() {
    int m, n;
    if (scanf("%d %d", &m, &n) != 2) return 0;
    int nums1[500], nums2[500];
    for (int i = 0; i < m + n; i++) scanf("%d", &nums1[i]);
    for (int i = 0; i < n; i++) scanf("%d", &nums2[i]);
    merge(nums1, m, nums2, n);
    for (int i = 0; i < m + n; i++) printf("%d%c", nums1[i], i == m + n - 1 ? '\\n' : ' ');
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int>& nums1, int m, const vector<int>& nums2, int n) {
    int i = m - 1;
    int j = n - 1;
    int k = m + n - 1;

    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[k] = nums1[i];
            i--;
        } else {
            nums1[k] = nums2[j];
            j--;
        }
        k--;
    }
}

int main() {
    int m, n;
    if (cin >> m >> n) {
        vector<int> nums1(m + n), nums2(n);
        for (int i = 0; i < m + n; i++) cin >> nums1[i];
        for (int i = 0; i < n; i++) cin >> nums2[i];
        merge(nums1, m, nums2, n);
        for (int i = 0; i < m + n; i++) cout << nums1[i] << (i == m + n - 1 ? "\\n" : " ");
    }
    return 0;
}""",
            "java": """import java.util.Scanner;

public class Main {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;

        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k] = nums1[i];
                i--;
            } else {
                nums1[k] = nums2[j];
                j--;
            }
            k--;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt(), n = sc.nextInt();
            int[] nums1 = new int[m + n];
            for (int i = 0; i < m + n; i++) nums1[i] = sc.nextInt();
            int[] nums2 = new int[n];
            for (int i = 0; i < n; i++) nums2[i] = sc.nextInt();
            merge(nums1, m, nums2, n);
            for (int i = 0; i < m + n; i++) System.out.print(nums1[i] + (i == m + n - 1 ? "\\n" : " "));
        }
    }
}""",
            "python": """def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    return nums1

if __name__ == '__main__':
    import sys
    tokens = sys.stdin.read().split()
    if tokens:
        m, n = int(tokens[0]), int(tokens[1])
        nums1 = [int(x) for x in tokens[2:2 + m + n]]
        nums2 = [int(x) for x in tokens[2 + m + n:2 + m + n + n]]
        print(*merge(nums1, m, nums2, n))"""
        })
    },

    # 8. Merge Sort
    {
        "id": "dsa-sort-merge-sort",
        "problem_num": 68,
        "title": "Merge Sort",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "Divide and Conquer",
        "difficulty": "MEDIUM",
        "description": "Given an array of integers, sort the array using the Merge Sort algorithm by dividing the array into halves, sorting recursively and merging.",
        "input_format": "Space-separated integers.",
        "output_format": "Space-separated sorted integers.",
        "constraints": "1 <= arr.length <= 10^5\n-10^5 <= arr[i] <= 10^5",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Uber", "Goldman Sachs"],
        "examples": [
            {"input": "38 27 43 3 9 82 10", "output": "3 9 10 27 38 43 82", "explanation": "Sorted via divide and conquer."},
            {"input": "5 4 3 2 1", "output": "1 2 3 4 5", "explanation": "Reversed array sorted."},
            {"input": "10 20 10 5 2", "output": "2 5 10 10 20", "explanation": "Duplicates handled."}
        ],
        "test_cases": [
            {"input": "38 27 43 3 9 82 10", "expected": "3 9 10 27 38 43 82", "is_hidden": False},
            {"input": "5 4 3 2 1", "expected": "1 2 3 4 5", "is_hidden": False},
            {"input": "10 20 10 5 2", "expected": "2 5 10 10 20", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nvoid mergeSort(int arr[], int l, int r) {\n    // Your code here\n}\n\nint main() {\n    int arr[100000], n = 0;\n    while (scanf(\"%d\", &arr[n]) == 1) n++;\n    mergeSort(arr, 0, n - 1);\n    for (int i = 0; i < n; i++) printf(\"%d%c\", arr[i], i == n - 1 ? '\\n' : ' ');\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvoid mergeSort(vector<int>& arr, int l, int r) {\n    // Your code here\n}\n\nint main() {\n    vector<int> arr; int x;\n    while (cin >> x) arr.push_back(x);\n    mergeSort(arr, 0, (int)arr.size() - 1);\n    for (int i = 0; i < (int)arr.size(); i++) cout << arr[i] << (i == (int)arr.size() - 1 ? \"\\n\" : \" \");\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void mergeSort(int[] arr, int l, int r) {\n        // Your code here\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] arr = list.stream().mapToInt(i -> i).toArray();\n        mergeSort(arr, 0, arr.length - 1);\n        for (int i = 0; i < arr.length; i++) System.out.print(arr[i] + (i == arr.length - 1 ? \"\\n\" : \" \"));\n    }\n}",
            "python": "def mergeSort(arr):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    arr = list(map(int, input().split()))\n    print(*mergeSort(arr))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1, n2 = r - m;
    int L[n1], R[n2];
    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int main() {
    int arr[100000], n = 0;
    while (scanf("%d", &arr[n]) == 1) n++;
    if (n > 0) mergeSort(arr, 0, n - 1);
    for (int i = 0; i < n; i++) printf("%d%c", arr[i], i == n - 1 ? '\\n' : ' ');
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int>& arr, int l, int m, int r) {
    vector<int> left(arr.begin() + l, arr.begin() + m + 1);
    vector<int> right(arr.begin() + m + 1, arr.begin() + r + 1);
    int i = 0, j = 0, k = l;
    while (i < (int)left.size() && j < (int)right.size()) {
        if (left[i] <= right[j]) arr[k++] = left[i++];
        else arr[k++] = right[j++];
    }
    while (i < (int)left.size()) arr[k++] = left[i++];
    while (j < (int)right.size()) arr[k++] = right[j++];
}

void mergeSort(vector<int>& arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int main() {
    vector<int> arr; int x;
    while (cin >> x) arr.push_back(x);
    if (!arr.empty()) mergeSort(arr, 0, (int)arr.size() - 1);
    for (int i = 0; i < (int)arr.size(); i++) cout << arr[i] << (i == (int)arr.size() - 1 ? "\\n" : " ");
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void merge(int[] arr, int l, int m, int r) {
        int n1 = m - l + 1, n2 = r - m;
        int[] L = new int[n1], R = new int[n2];
        for (int i = 0; i < n1; i++) L[i] = arr[l + i];
        for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) arr[k++] = L[i++];
            else arr[k++] = R[j++];
        }
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }

    public static void mergeSort(int[] arr, int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] arr = list.stream().mapToInt(i -> i).toArray();
        if (arr.length > 0) mergeSort(arr, 0, arr.length - 1);
        for (int i = 0; i < arr.length; i++) System.out.print(arr[i] + (i == arr.length - 1 ? "\\n" : " "));
    }
}""",
            "python": """def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(*mergeSort(arr))"""
        })
    },

    # 9. Sort Array by Increasing Frequency
    {
        "id": "dsa-sort-frequency",
        "problem_num": 69,
        "title": "Sort Array by Increasing Frequency",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "Custom Comparator & Hash Sort",
        "difficulty": "MEDIUM",
        "description": "Given an array of integers, sort the elements by increasing frequency. If two elements have the same frequency, sort them in decreasing numerical order.",
        "input_format": "Space-separated integers.",
        "output_format": "Space-separated sorted integers.",
        "constraints": "1 <= nums.length <= 200\n-100 <= nums[i] <= 100",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "company_tags": ["Oracle", "Amazon"],
        "examples": [
            {"input": "1 1 2 2 2 3", "output": "3 1 1 2 2 2", "explanation": "'3' has freq 1, '1' has freq 2, '2' has freq 3."},
            {"input": "2 3 1 3 2", "output": "1 3 3 2 2", "explanation": "'1' freq 1. '3' and '2' freq 2: 3 sorted before 2."},
            {"input": "-1 1 -6 4 5 -6 1 4 1", "output": "5 -1 4 4 -6 -6 1 1 1", "explanation": "Sorted by freq ascending then val descending."}
        ],
        "test_cases": [
            {"input": "1 1 2 2 2 3", "expected": "3 1 1 2 2 2", "is_hidden": False},
            {"input": "2 3 1 3 2", "expected": "1 3 3 2 2", "is_hidden": False},
            {"input": "-1 1 -6 4 5 -6 1 4 1", "expected": "5 -1 4 4 -6 -6 1 1 1", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nvoid frequencySort(int nums[], int n) {\n    // Your code here\n}\n\nint main() {\n    int nums[500], n = 0;\n    while (scanf(\"%d\", &nums[n]) == 1) n++;\n    frequencySort(nums, n);\n    for (int i = 0; i < n; i++) printf(\"%d%c\", nums[i], i == n - 1 ? '\\n' : ' ');\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvoid frequencySort(vector<int>& nums) {\n    // Your code here\n}\n\nint main() {\n    vector<int> nums; int x;\n    while (cin >> x) nums.push_back(x);\n    frequencySort(nums);\n    for (int i = 0; i < (int)nums.size(); i++) cout << nums[i] << (i == (int)nums.size() - 1 ? \"\\n\" : \" \");\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static void frequencySort(int[] nums) {\n        // Your code here\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] nums = list.stream().mapToInt(i -> i).toArray();\n        frequencySort(nums);\n        for (int i = 0; i < nums.length; i++) System.out.print(nums[i] + (i == nums.length - 1 ? \"\\n\" : \" \"));\n    }\n}",
            "python": "def frequencySort(nums):\n    # Your code here\n    pass\n\nif __name__ == '__main__':\n    nums = list(map(int, input().split()))\n    print(*frequencySort(nums))"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

int freq[201]; // offset +100

int cmp(const void *a, const void *b) {
    int x = *(int*)a;
    int y = *(int*)b;
    int fx = freq[x + 100];
    int fy = freq[y + 100];
    if (fx != fy) return fx - fy;
    return y - x;
}

void frequencySort(int nums[], int n) {
    for (int i = 0; i <= 200; i++) freq[i] = 0;
    for (int i = 0; i < n; i++) freq[nums[i] + 100]++;
    qsort(nums, n, sizeof(int), cmp);
}

int main() {
    int nums[500], n = 0;
    while (scanf("%d", &nums[n]) == 1) n++;
    frequencySort(nums, n);
    for (int i = 0; i < n; i++) printf("%d%c", nums[i], i == n - 1 ? '\\n' : ' ');
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

void frequencySort(vector<int>& nums) {
    unordered_map<int, int> count;
    for (int x : nums) count[x]++;
    sort(nums.begin(), nums.end(), [&](int a, int b) {
        if (count[a] != count[b]) return count[a] < count[b];
        return a > b;
    });
}

int main() {
    vector<int> nums; int x;
    while (cin >> x) nums.push_back(x);
    frequencySort(nums);
    for (int i = 0; i < (int)nums.size(); i++) cout << nums[i] << (i == (int)nums.size() - 1 ? "\\n" : " ");
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void frequencySort(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) freq.put(x, freq.getOrDefault(x, 0) + 1);

        List<Integer> list = new ArrayList<>();
        for (int x : nums) list.add(x);

        list.sort((a, b) -> {
            int fa = freq.get(a), fb = freq.get(b);
            if (fa != fb) return Integer.compare(fa, fb);
            return Integer.compare(b, a);
        });

        for (int i = 0; i < nums.length; i++) nums[i] = list.get(i);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] nums = list.stream().mapToInt(i -> i).toArray();
        frequencySort(nums);
        for (int i = 0; i < nums.length; i++) System.out.print(nums[i] + (i == nums.length - 1 ? "\\n" : " "));
    }
}""",
            "python": """from collections import Counter

def frequencySort(nums):
    freq = Counter(nums)
    nums.sort(key=lambda x: (freq[x], -x))
    return nums

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(*frequencySort(nums))"""
        })
    },

    # 10. Minimum Number of Platforms
    {
        "id": "dsa-sort-min-platforms",
        "problem_num": 70,
        "title": "Minimum Number of Platforms",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "Interval Scheduling",
        "difficulty": "MEDIUM",
        "description": "Given arrival and departure times of trains at a railway station, find the minimum number of platforms required so that no train has to wait.",
        "input_format": "Line 1: Space-separated arrival times\nLine 2: Space-separated departure times",
        "output_format": "An integer representing the minimum platforms required.",
        "constraints": "1 <= N <= 50000\n0000 <= arr[i] <= dep[i] <= 2359",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(1)",
        "company_tags": ["Amazon", "Microsoft", "D-E-Shaw"],
        "examples": [
            {"input": "900 940 950 1100 1500 1800\\n910 1200 1120 1130 1900 2000", "output": "3", "explanation": "Max overlapping trains = 3."},
            {"input": "900 1100 1235\\n1000 1200 1240", "output": "1", "explanation": "No overlaps."},
            {"input": "900 940 950\\n1000 1100 1200", "output": "3", "explanation": "All 3 overlap."}
        ],
        "test_cases": [
            {"input": "900 940 950 1100 1500 1800\n910 1200 1120 1130 1900 2000", "expected": "3", "is_hidden": False},
            {"input": "900 1100 1235\n1000 1200 1240", "expected": "1", "is_hidden": False},
            {"input": "900 940 950\n1000 1100 1200", "expected": "3", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nint findPlatform(int arr[], int dep[], int n) {\n    // Your code here\n    return 0;\n}\n\nint main() {\n    // Read input\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint findPlatform(vector<int>& arr, vector<int>& dep) {\n    // Your code here\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static int findPlatform(int[] arr, int[] dep) {\n        // Your code here\n        return 0;\n    }\n}",
            "python": "def findPlatform(arr, dep):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int findPlatform(int arr[], int dep[], int n) {
    qsort(arr, n, sizeof(int), cmp);
    qsort(dep, n, sizeof(int), cmp);

    int platforms = 0, max_platforms = 0;
    int i = 0, j = 0;

    while (i < n && j < n) {
        if (arr[i] <= dep[j]) {
            platforms++;
            if (platforms > max_platforms) max_platforms = platforms;
            i++;
        } else {
            platforms--;
            j++;
        }
    }
    return max_platforms;
}

int main() {
    int arr[50000], dep[50000];
    int n = 0, m = 0;
    char line[1000000];

    if (fgets(line, sizeof(line), stdin)) {
        char *ptr = line; int val, offset;
        while (sscanf(ptr, "%d%n", &val, &offset) == 1) {
            arr[n++] = val;
            ptr += offset;
        }
    }
    if (fgets(line, sizeof(line), stdin)) {
        char *ptr = line; int val, offset;
        while (sscanf(ptr, "%d%n", &val, &offset) == 1) {
            dep[m++] = val;
            ptr += offset;
        }
    }
    printf("%d\\n", findPlatform(arr, dep, n));
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int findPlatform(vector<int>& arr, vector<int>& dep) {
    sort(arr.begin(), arr.end());
    sort(dep.begin(), dep.end());

    int n = arr.size();
    int platforms = 0, max_platforms = 0;
    int i = 0, j = 0;

    while (i < n && j < n) {
        if (arr[i] <= dep[j]) {
            platforms++;
            max_platforms = max(max_platforms, platforms);
            i++;
        } else {
            platforms--;
            j++;
        }
    }
    return max_platforms;
}

int main() {
    string l1, l2;
    if (getline(cin, l1) && getline(cin, l2)) {
        stringstream ss1(l1), ss2(l2);
        vector<int> arr, dep; int x;
        while (ss1 >> x) arr.push_back(x);
        while (ss2 >> x) dep.push_back(x);
        cout << findPlatform(arr, dep) << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static int findPlatform(int[] arr, int[] dep) {
        Arrays.sort(arr);
        Arrays.sort(dep);

        int n = arr.length;
        int platforms = 0, max_platforms = 0;
        int i = 0, j = 0;

        while (i < n && j < n) {
            if (arr[i] <= dep[j]) {
                platforms++;
                max_platforms = Math.max(max_platforms, platforms);
                i++;
            } else {
                platforms--;
                j++;
            }
        }
        return max_platforms;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String[] s1 = sc.nextLine().trim().split("\\\\s+");
            String[] s2 = sc.nextLine().trim().split("\\\\s+");
            int[] arr = new int[s1.length];
            int[] dep = new int[s2.length];
            for (int i = 0; i < s1.length; i++) arr[i] = Integer.parseInt(s1[i]);
            for (int i = 0; i < s2.length; i++) dep[i] = Integer.parseInt(s2[i]);
            System.out.println(findPlatform(arr, dep));
        }
    }
}""",
            "python": """def findPlatform(arr, dep):
    arr.sort()
    dep.sort()
    n = len(arr)
    platforms = 0
    max_platforms = 0
    i = 0
    j = 0

    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1

    return max_platforms

if __name__ == '__main__':
    import sys
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    if len(lines) >= 2:
        arr = list(map(int, lines[0].split()))
        dep = list(map(int, lines[1].split()))
        print(findPlatform(arr, dep))"""
        })
    },

    # 11. Count Inversions
    {
        "id": "dsa-sort-count-inversions",
        "problem_num": 71,
        "title": "Count Inversions",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "Inversion Counting",
        "difficulty": "HARD",
        "description": "Given an array of integers, count the number of inversions. An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j].",
        "input_format": "Space-separated integers.",
        "output_format": "An integer representing inversion count.",
        "constraints": "1 <= arr.length <= 10^5\n-10^9 <= arr[i] <= 10^9",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "company_tags": ["Amazon", "Google", "Flipkart"],
        "examples": [
            {"input": "2 4 1 3 5", "output": "3", "explanation": "Pairs: (2,1), (4,1), (4,3)."},
            {"input": "5 4 3 2 1", "output": "10", "explanation": "Reverse sorted array has N*(N-1)/2 inversions."},
            {"input": "1 2 3 4 5", "output": "0", "explanation": "Already sorted, 0 inversions."}
        ],
        "test_cases": [
            {"input": "2 4 1 3 5", "expected": "3", "is_hidden": False},
            {"input": "5 4 3 2 1", "expected": "10", "is_hidden": False},
            {"input": "1 2 3 4 5", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nlong long countInversions(long long arr[], int n) {\n    // Your code here\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nlong long countInversions(vector<long long>& arr) {\n    // Your code here\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static long countInversions(long[] arr) {\n        // Your code here\n        return 0;\n    }\n}",
            "python": "def countInversions(arr):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

long long merge(long long arr[], long long temp[], int l, int m, int r) {
    int i = l, j = m + 1, k = l;
    long long count = 0;
    while (i <= m && j <= r) {
        if (arr[i] <= arr[j]) temp[k++] = arr[i++];
        else {
            temp[k++] = arr[j++];
            count += (m - i + 1);
        }
    }
    while (i <= m) temp[k++] = arr[i++];
    while (j <= r) temp[k++] = arr[j++];
    for (i = l; i <= r; i++) arr[i] = temp[i];
    return count;
}

long long mergeSortCount(long long arr[], long long temp[], int l, int r) {
    long long count = 0;
    if (l < r) {
        int m = l + (r - l) / 2;
        count += mergeSortCount(arr, temp, l, m);
        count += mergeSortCount(arr, temp, m + 1, r);
        count += merge(arr, temp, l, m, r);
    }
    return count;
}

int main() {
    long long arr[100000], temp[100000];
    int n = 0;
    while (scanf("%lld", &arr[n]) == 1) n++;
    printf("%lld\\n", mergeSortCount(arr, temp, 0, n - 1));
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

long long merge(vector<long long>& arr, vector<long long>& temp, int l, int m, int r) {
    int i = l, j = m + 1, k = l;
    long long count = 0;
    while (i <= m && j <= r) {
        if (arr[i] <= arr[j]) temp[k++] = arr[i++];
        else {
            temp[k++] = arr[j++];
            count += (m - i + 1);
        }
    }
    while (i <= m) temp[k++] = arr[i++];
    while (j <= r) temp[k++] = arr[j++];
    for (i = l; i <= r; i++) arr[i] = temp[i];
    return count;
}

long long mergeSortCount(vector<long long>& arr, vector<long long>& temp, int l, int r) {
    long long count = 0;
    if (l < r) {
        int m = l + (r - l) / 2;
        count += mergeSortCount(arr, temp, l, m);
        count += mergeSortCount(arr, temp, m + 1, r);
        count += merge(arr, temp, l, m, r);
    }
    return count;
}

int main() {
    vector<long long> arr; long long x;
    while (cin >> x) arr.push_back(x);
    vector<long long> temp(arr.size());
    cout << mergeSortCount(arr, temp, 0, (int)arr.size() - 1) << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static long merge(long[] arr, long[] temp, int l, int m, int r) {
        int i = l, j = m + 1, k = l;
        long count = 0;
        while (i <= m && j <= r) {
            if (arr[i] <= arr[j]) temp[k++] = arr[i++];
            else {
                temp[k++] = arr[j++];
                count += (m - i + 1);
            }
        }
        while (i <= m) temp[k++] = arr[i++];
        while (j <= r) temp[k++] = arr[j++];
        for (i = l; i <= r; i++) arr[i] = temp[i];
        return count;
    }

    public static long mergeSortCount(long[] arr, long[] temp, int l, int r) {
        long count = 0;
        if (l < r) {
            int m = l + (r - l) / 2;
            count += mergeSortCount(arr, temp, l, m);
            count += mergeSortCount(arr, temp, m + 1, r);
            count += merge(arr, temp, l, m, r);
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Long> list = new ArrayList<>();
        while (sc.hasNextLong()) list.add(sc.nextLong());
        long[] arr = list.stream().mapToLong(i -> i).toArray();
        long[] temp = new long[arr.length];
        System.out.println(mergeSortCount(arr, temp, 0, arr.length - 1));
    }
}""",
            "python": """def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, count1 = mergeSort(arr[:mid])
    right, count2 = mergeSort(arr[mid:])

    merged = []
    i = 0
    j = 0
    count = count1 + count2

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, count

def countInversions(arr):
    return mergeSort(arr)[1]

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(countInversions(arr))"""
        })
    },

    # 12. Reverse Pairs
    {
        "id": "dsa-sort-reverse-pairs",
        "problem_num": 72,
        "title": "Reverse Pairs",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "Divide and Conquer",
        "difficulty": "HARD",
        "description": "Given an integer array nums, count the number of reverse pairs. A reverse pair is a pair (i, j) where i < j and nums[i] > 2 * nums[j].",
        "input_format": "Space-separated integers.",
        "output_format": "An integer representing the count of reverse pairs.",
        "constraints": "1 <= nums.length <= 50000\n-2^31 <= nums[i] <= 2^31 - 1",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "company_tags": ["Google", "Amazon"],
        "examples": [
            {"input": "1 3 2 3 1", "output": "2", "explanation": "Reverse pairs: (3, 1) and (3, 1)."},
            {"input": "2 4 3 5 1", "output": "3", "explanation": "Pairs: (4,1), (3,1), (5,1)."},
            {"input": "5 4 3 2 1", "output": "4", "explanation": "Reverse pairs identified."}
        ],
        "test_cases": [
            {"input": "1 3 2 3 1", "expected": "2", "is_hidden": False},
            {"input": "2 4 3 5 1", "expected": "3", "is_hidden": False},
            {"input": "5 4 3 2 1", "expected": "4", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nlong long reversePairs(int nums[], int n) {\n    // Your code here\n    return 0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint reversePairs(vector<int>& nums) {\n    // Your code here\n    return 0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static int reversePairs(int[] nums) {\n        // Your code here\n        return 0;\n    }\n}",
            "python": "def reversePairs(nums):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

long long mergeSort(long long arr[], int l, int r) {
    if (l >= r) return 0;
    int m = l + (r - l) / 2;
    long long count = mergeSort(arr, l, m) + mergeSort(arr, m + 1, r);

    int j = m + 1;
    for (int i = l; i <= m; i++) {
        while (j <= r && arr[i] > 2LL * arr[j]) j++;
        count += (j - (m + 1));
    }

    long long temp[r - l + 1];
    int i = l; j = m + 1; int k = 0;
    while (i <= m && j <= r) {
        if (arr[i] <= arr[j]) temp[k++] = arr[i++];
        else temp[k++] = arr[j++];
    }
    while (i <= m) temp[k++] = arr[i++];
    while (j <= r) temp[k++] = arr[j++];
    for (int p = 0; p < k; p++) arr[l + p] = temp[p];
    return count;
}

int main() {
    long long nums[50000];
    int n = 0;
    while (scanf("%lld", &nums[n]) == 1) n++;
    printf("%lld\\n", mergeSort(nums, 0, n - 1));
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

long long mergeSort(vector<long long>& nums, int l, int r) {
    if (l >= r) return 0;
    int m = l + (r - l) / 2;
    long long count = mergeSort(nums, l, m) + mergeSort(nums, m + 1, r);

    int j = m + 1;
    for (int i = l; i <= m; i++) {
        while (j <= r && nums[i] > 2LL * nums[j]) j++;
        count += (j - (m + 1));
    }

    vector<long long> temp;
    int i = l; j = m + 1;
    while (i <= m && j <= r) {
        if (nums[i] <= nums[j]) temp.push_back(nums[i++]);
        else temp.push_back(nums[j++]);
    }
    while (i <= m) temp.push_back(nums[i++]);
    while (j <= r) temp.push_back(nums[j++]);
    for (size_t p = 0; p < temp.size(); p++) nums[l + p] = temp[p];
    return count;
}

int main() {
    vector<long long> nums; long long x;
    while (cin >> x) nums.push_back(x);
    cout << mergeSort(nums, 0, (int)nums.size() - 1) << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static long mergeSort(long[] nums, int l, int r) {
        if (l >= r) return 0;
        int m = l + (r - l) / 2;
        long count = mergeSort(nums, l, m) + mergeSort(nums, m + 1, r);

        int j = m + 1;
        for (int i = l; i <= m; i++) {
            while (j <= r && nums[i] > 2L * nums[j]) j++;
            count += (j - (m + 1));
        }

        long[] temp = new long[r - l + 1];
        int i = l; j = m + 1; int k = 0;
        while (i <= m && j <= r) {
            if (nums[i] <= nums[j]) temp[k++] = nums[i++];
            else temp[k++] = nums[j++];
        }
        while (i <= m) temp[k++] = nums[i++];
        while (j <= r) temp[k++] = nums[j++];
        for (int p = 0; p < k; p++) nums[l + p] = temp[p];
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Long> list = new ArrayList<>();
        while (sc.hasNextLong()) list.add(sc.nextLong());
        long[] nums = list.stream().mapToLong(i -> i).toArray();
        System.out.println(mergeSort(nums, 0, nums.length - 1));
    }
}""",
            "python": """def reversePairs(nums):
    def mergeSort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, count1 = mergeSort(arr[:mid])
        right, count2 = mergeSort(arr[mid:])

        count = count1 + count2
        j = 0
        for x in left:
            while j < len(right) and x > 2 * right[j]:
                j += 1
            count += j

        merged = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, count

    return mergeSort(nums)[1]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(reversePairs(nums))"""
        })
    },

    # 13. Largest Number
    {
        "id": "dsa-sort-largest-number",
        "problem_num": 73,
        "title": "Largest Number",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "Custom String Sort",
        "difficulty": "HARD",
        "description": "Given a list of non-negative integers, arrange them such that they form the largest possible number. Return the result as a string.",
        "input_format": "Space-separated integers.",
        "output_format": "A single string representing the largest number formed.",
        "constraints": "1 <= nums.length <= 100\n0 <= nums[i] <= 10^9",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "company_tags": ["Microsoft", "Amazon", "Apple"],
        "examples": [
            {"input": "10 2", "output": "210", "explanation": "210 is larger than 102."},
            {"input": "3 30 34 5 9", "output": "9534330", "explanation": "Arranged to form max number."},
            {"input": "0 0", "output": "0", "explanation": "Multiple zeros reduce to a single 0."}
        ],
        "test_cases": [
            {"input": "10 2", "expected": "210", "is_hidden": False},
            {"input": "3 30 34 5 9", "expected": "9534330", "is_hidden": False},
            {"input": "0 0", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nvoid largestNumber(int nums[], int n) {\n    // Your code here\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nstring largestNumber(vector<int>& nums) {\n    // Your code here\n    return \"\";\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static String largestNumber(int[] nums) {\n        // Your code here\n        return \"\";\n    }\n}",
            "python": "def largestNumber(nums):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp(const void *a, const void *b) {
    char s1[100], s2[100];
    sprintf(s1, "%s%s", *(char**)b, *(char**)a);
    sprintf(s2, "%s%s", *(char**)a, *(char**)b);
    return strcmp(s1, s2);
}

int main() {
    char *nums[500];
    int n = 0;
    char buffer[50];
    while (scanf("%s", buffer) == 1) {
        nums[n] = strdup(buffer);
        n++;
    }
    qsort(nums, n, sizeof(char*), cmp);
    if (strcmp(nums[0], "0") == 0) {
        printf("0\\n");
        return 0;
    }
    for (int i = 0; i < n; i++) printf("%s", nums[i]);
    printf("\\n");
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string largestNumber(vector<int>& nums) {
    vector<string> s;
    for (int x : nums) s.push_back(to_string(x));
    sort(s.begin(), s.end(), [](const string& a, const string& b) {
        return a + b > b + a;
    });
    if (s[0] == "0") return "0";
    string res = "";
    for (const string& str : s) res += str;
    return res;
}

int main() {
    vector<int> nums; int x;
    while (cin >> x) nums.push_back(x);
    cout << largestNumber(nums) << "\\n";
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static String largestNumber(int[] nums) {
        String[] s = new String[nums.length];
        for (int i = 0; i < nums.length; i++) s[i] = String.valueOf(nums[i]);
        Arrays.sort(s, (a, b) -> (b + a).compareTo(a + b));
        if (s[0].equals("0")) return "0";
        StringBuilder sb = new StringBuilder();
        for (String str : s) sb.append(str);
        return sb.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] nums = list.stream().mapToInt(i -> i).toArray();
        System.out.println(largestNumber(nums));
    }
}""",
            "python": """from functools import cmp_to_key

def largestNumber(nums):
    nums = list(map(str, nums))

    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        return 0

    nums.sort(key=cmp_to_key(compare))
    result = ''.join(nums)
    if result[0] == '0':
        return '0'
    return result

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(largestNumber(nums))"""
        })
    },

    # 14. Median of Two Sorted Arrays
    {
        "id": "dsa-sort-median-two-sorted-arrays",
        "problem_num": 74,
        "title": "Median of Two Sorted Arrays",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "Binary Search Partition",
        "difficulty": "HARD",
        "description": "Given two sorted arrays nums1 and nums2 of sizes m and n, find the median of the two sorted arrays with runtime complexity of O(log(min(m, n))).",
        "input_format": "Line 1: Space-separated elements of nums1\nLine 2: Space-separated elements of nums2",
        "output_format": "A single number (formatted as integer if whole, or float) representing the median.",
        "constraints": "nums1.length == m, nums2.length == n\n0 <= m, n <= 1000\n1 <= m + n <= 2000",
        "time_complexity": "O(log(min(m, n)))",
        "space_complexity": "O(1)",
        "company_tags": ["Google", "Microsoft", "Amazon"],
        "examples": [
            {"input": "1 3\\n2", "output": "2", "explanation": "Merged array = [1, 2, 3], median is 2."},
            {"input": "1 2\\n3 4", "output": "2.5", "explanation": "Merged array = [1, 2, 3, 4], median is (2 + 3) / 2 = 2.5."},
            {"input": "0 0\\n0 0", "output": "0", "explanation": "Median is 0."}
        ],
        "test_cases": [
            {"input": "1 3\n2", "expected": "2", "is_hidden": False},
            {"input": "1 2\n3 4", "expected": "2.5", "is_hidden": False},
            {"input": "0 0\n0 0", "expected": "0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\ndouble findMedianSortedArrays(int nums1[], int m, int nums2[], int n) {\n    // Your code here\n    return 0.0;\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\ndouble findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {\n    // Your code here\n    return 0.0;\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {\n        // Your code here\n        return 0.0;\n    }\n}",
            "python": "def findMedianSortedArrays(nums1, nums2):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <limits.h>

double findMedianSortedArrays(int nums1[], int m, int nums2[], int n) {
    if (m > n) return findMedianSortedArrays(nums2, n, nums1, m);
    int low = 0, high = m;
    while (low <= high) {
        int part1 = (low + high) / 2;
        int part2 = (m + n + 1) / 2 - part1;

        int maxL1 = (part1 == 0) ? INT_MIN : nums1[part1 - 1];
        int minR1 = (part1 == m) ? INT_MAX : nums1[part1];
        int maxL2 = (part2 == 0) ? INT_MIN : nums2[part2 - 1];
        int minR2 = (part2 == n) ? INT_MAX : nums2[part2];

        if (maxL1 <= minR2 && maxL2 <= minR1) {
            if ((m + n) % 2 == 0) {
                int leftMax = maxL1 > maxL2 ? maxL1 : maxL2;
                int rightMin = minR1 < minR2 ? minR1 : minR2;
                return (leftMax + rightMin) / 2.0;
            } else {
                return (maxL1 > maxL2 ? maxL1 : maxL2);
            }
        } else if (maxL1 > minR2) high = part1 - 1;
        else low = part1 + 1;
    }
    return 0.0;
}

int main() {
    int nums1[1000], nums2[1000];
    int m = 0, n = 0;
    char line[10000];
    if (fgets(line, sizeof(line), stdin)) {
        char *ptr = line; int val, offset;
        while (sscanf(ptr, "%d%n", &val, &offset) == 1) { nums1[m++] = val; ptr += offset; }
    }
    if (fgets(line, sizeof(line), stdin)) {
        char *ptr = line; int val, offset;
        while (sscanf(ptr, "%d%n", &val, &offset) == 1) { nums2[n++] = val; ptr += offset; }
    }
    double med = findMedianSortedArrays(nums1, m, nums2, n);
    if (med == (long long)med) printf("%lld\\n", (long long)med);
    else printf("%.1f\\n", med);
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>
#include <sstream>
#include <climits>
#include <algorithm>

using namespace std;

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    if (nums1.size() > nums2.size()) return findMedianSortedArrays(nums2, nums1);
    int m = nums1.size(), n = nums2.size();
    int low = 0, high = m;
    while (low <= high) {
        int part1 = (low + high) / 2;
        int part2 = (m + n + 1) / 2 - part1;

        int maxL1 = (part1 == 0) ? INT_MIN : nums1[part1 - 1];
        int minR1 = (part1 == m) ? INT_MAX : nums1[part1];
        int maxL2 = (part2 == 0) ? INT_MIN : nums2[part2 - 1];
        int minR2 = (part2 == n) ? INT_MAX : nums2[part2];

        if (maxL1 <= minR2 && maxL2 <= minR1) {
            if ((m + n) % 2 == 0) {
                return (max(maxL1, maxL2) + min(minR1, minR2)) / 2.0;
            }
            return max(maxL1, maxL2);
        } else if (maxL1 > minR2) high = part1 - 1;
        else low = part1 + 1;
    }
    return 0.0;
}

int main() {
    string l1, l2;
    if (getline(cin, l1) && getline(cin, l2)) {
        stringstream ss1(l1), ss2(l2);
        vector<int> nums1, nums2; int x;
        while (ss1 >> x) nums1.push_back(x);
        while (ss2 >> x) nums2.push_back(x);
        double med = findMedianSortedArrays(nums1, nums2);
        if (med == (long long)med) cout << (long long)med << "\\n";
        else cout << med << "\\n";
    }
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) return findMedianSortedArrays(nums2, nums1);
        int m = nums1.length, n = nums2.length;
        int low = 0, high = m;
        while (low <= high) {
            int part1 = (low + high) / 2;
            int part2 = (m + n + 1) / 2 - part1;

            int maxL1 = (part1 == 0) ? Integer.MIN_VALUE : nums1[part1 - 1];
            int minR1 = (part1 == m) ? Integer.MAX_VALUE : nums1[part1];
            int maxL2 = (part2 == 0) ? Integer.MIN_VALUE : nums2[part2 - 1];
            int minR2 = (part2 == n) ? Integer.MAX_VALUE : nums2[part2];

            if (maxL1 <= minR2 && maxL2 <= minR1) {
                if ((m + n) % 2 == 0) {
                    return (Math.max(maxL1, maxL2) + Math.min(minR1, minR2)) / 2.0;
                }
                return Math.max(maxL1, maxL2);
            } else if (maxL1 > minR2) high = part1 - 1;
            else low = part1 + 1;
        }
        return 0.0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String[] s1 = sc.nextLine().trim().split("\\\\s+");
            String[] s2 = sc.nextLine().trim().split("\\\\s+");
            int[] nums1 = new int[s1.length];
            int[] nums2 = new int[s2.length];
            for (int i = 0; i < s1.length; i++) nums1[i] = Integer.parseInt(s1[i]);
            for (int i = 0; i < s2.length; i++) nums2[i] = Integer.parseInt(s2[i]);
            double med = findMedianSortedArrays(nums1, nums2);
            if (med == (long)med) System.out.println((long)med);
            else System.out.println(med);
        }
    }
}""",
            "python": """def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m = len(nums1)
    n = len(nums2)
    low = 0
    high = m

    while low <= high:
        partition1 = (low + high) // 2
        partition2 = (m + n + 1) // 2 - partition1

        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]

        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]

        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            if (m + n) % 2 == 0:
                res = (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                return int(res) if res.is_integer() else res
            res = max(maxLeft1, maxLeft2)
            return int(res) if isinstance(res, float) and res.is_integer() else res

        elif maxLeft1 > minRight2:
            high = partition1 - 1
        else:
            low = partition1 + 1

if __name__ == '__main__':
    import sys
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    if len(lines) >= 2:
        nums1 = list(map(int, lines[0].split()))
        nums2 = list(map(int, lines[1].split()))
        print(findMedianSortedArrays(nums1, nums2))"""
        })
    },

    # 15. Count of Smaller Numbers After Self
    {
        "id": "dsa-sort-count-smaller",
        "problem_num": 75,
        "title": "Count of Smaller Numbers After Self",
        "category": "Sorting",
        "topic": "Sorting",
        "subtopic": "Merge Sort with Inversion Count",
        "difficulty": "HARD",
        "description": "Given an integer array nums, return an array where each element represents the number of smaller elements to its right.",
        "input_format": "Space-separated integers.",
        "output_format": "Space-separated counts of smaller elements to the right.",
        "constraints": "1 <= nums.length <= 10^5\n-10^4 <= nums[i] <= 10^4",
        "time_complexity": "O(N log N)",
        "space_complexity": "O(N)",
        "company_tags": ["Google", "Amazon"],
        "examples": [
            {"input": "5 2 6 1", "output": "2 1 1 0", "explanation": "To right of 5: 2 and 1 (count 2). To right of 2: 1 (count 1). To right of 6: 1 (count 1). To right of 1: none (0)."},
            {"input": "-1", "output": "0", "explanation": "Single element has 0 smaller to right."},
            {"input": "-1 -1", "output": "0 0", "explanation": "Equal elements have 0 smaller to right."}
        ],
        "test_cases": [
            {"input": "5 2 6 1", "expected": "2 1 1 0", "is_hidden": False},
            {"input": "-1", "expected": "0", "is_hidden": False},
            {"input": "-1 -1", "expected": "0 0", "is_hidden": False}
        ],
        "starter_code_map": {
            "c": "#include <stdio.h>\n\nvoid countSmaller(int nums[], int n, int result[]) {\n    // Your code here\n}",
            "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvector<int> countSmaller(vector<int>& nums) {\n    // Your code here\n    return {};\n}",
            "java": "import java.util.*;\n\npublic class Main {\n    public static int[] countSmaller(int[] nums) {\n        // Your code here\n        return new int[0];\n    }\n}",
            "python": "def countSmaller(nums):\n    # Your code here\n    pass"
        },
        "solution_code": json.dumps({
            "c": """#include <stdio.h>
#include <stdlib.h>

void mergeSort(int nums[], int indices[], int result[], int left, int right) {
    if (right - left <= 1) return;
    int mid = left + (right - left) / 2;
    mergeSort(nums, indices, result, left, mid);
    mergeSort(nums, indices, result, mid, right);

    int temp[right - left];
    int i = left, j = mid, k = 0, right_count = 0;

    while (i < mid && j < right) {
        if (nums[indices[j]] < nums[indices[i]]) {
            temp[k++] = indices[j++];
            right_count++;
        } else {
            result[indices[i]] += right_count;
            temp[k++] = indices[i++];
        }
    }
    while (i < mid) {
        result[indices[i]] += right_count;
        temp[k++] = indices[i++];
    }
    while (j < right) temp[k++] = indices[j++];
    for (int p = 0; p < k; p++) indices[left + p] = temp[p];
}

int main() {
    int nums[100000], indices[100000], result[100000];
    int n = 0;
    while (scanf("%d", &nums[n]) == 1) {
        indices[n] = n;
        result[n] = 0;
        n++;
    }
    mergeSort(nums, indices, result, 0, n);
    for (int i = 0; i < n; i++) printf("%d%c", result[i], i == n - 1 ? '\\n' : ' ');
    return 0;
}""",
            "cpp": """#include <iostream>
#include <vector>

using namespace std;

void mergeSort(vector<int>& nums, vector<int>& indices, vector<int>& result, int left, int right) {
    if (right - left <= 1) return;
    int mid = left + (right - left) / 2;
    mergeSort(nums, indices, result, left, mid);
    mergeSort(nums, indices, result, mid, right);

    vector<int> temp;
    int i = left, j = mid, right_count = 0;
    while (i < mid && j < right) {
        if (nums[indices[j]] < nums[indices[i]]) {
            temp.push_back(indices[j++]);
            right_count++;
        } else {
            result[indices[i]] += right_count;
            temp.push_back(indices[i++]);
        }
    }
    while (i < mid) {
        result[indices[i]] += right_count;
        temp.push_back(indices[i++]);
    }
    while (j < right) temp.push_back(indices[j++]);
    for (size_t p = 0; p < temp.size(); p++) indices[left + p] = temp[p];
}

int main() {
    vector<int> nums; int x;
    while (cin >> x) nums.push_back(x);
    int n = nums.size();
    vector<int> indices(n), result(n, 0);
    for (int i = 0; i < n; i++) indices[i] = i;
    mergeSort(nums, indices, result, 0, n);
    for (int i = 0; i < n; i++) cout << result[i] << (i == n - 1 ? "\\n" : " ");
    return 0;
}""",
            "java": """import java.util.*;

public class Main {
    public static void mergeSort(int[] nums, int[] indices, int[] result, int left, int right) {
        if (right - left <= 1) return;
        int mid = left + (right - left) / 2;
        mergeSort(nums, indices, result, left, mid);
        mergeSort(nums, indices, result, mid, right);

        int[] temp = new int[right - left];
        int i = left, j = mid, k = 0, right_count = 0;
        while (i < mid && j < right) {
            if (nums[indices[j]] < nums[indices[i]]) {
                temp[k++] = indices[j++];
                right_count++;
            } else {
                result[indices[i]] += right_count;
                temp[k++] = indices[i++];
            }
        }
        while (i < mid) {
            result[indices[i]] += right_count;
            temp[k++] = indices[i++];
        }
        while (j < right) temp[k++] = indices[j++];
        for (int p = 0; p < k; p++) indices[left + p] = temp[p];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while (sc.hasNextInt()) list.add(sc.nextInt());
        int[] nums = list.stream().mapToInt(i -> i).toArray();
        int n = nums.length;
        int[] indices = new int[n];
        int[] result = new int[n];
        for (int i = 0; i < n; i++) indices[i] = i;
        mergeSort(nums, indices, result, 0, n);
        for (int i = 0; i < n; i++) System.out.print(result[i] + (i == n - 1 ? "\\n" : " "));
    }
}""",
            "python": """def countSmaller(nums):
    n = len(nums)
    result = [0] * n
    indexes = list(range(n))

    def mergeSort(left, right):
        if right - left <= 1:
            return

        mid = (left + right) // 2
        mergeSort(left, mid)
        mergeSort(mid, right)

        temp = []
        i = left
        j = mid
        right_count = 0

        while i < mid and j < right:
            if nums[indexes[j]] < nums[indexes[i]]:
                temp.append(indexes[j])
                right_count += 1
                j += 1
            else:
                result[indexes[i]] += right_count
                temp.append(indexes[i])
                i += 1

        while i < mid:
            result[indexes[i]] += right_count
            temp.append(indexes[i])
            i += 1

        while j < right:
            temp.append(indexes[j])
            j += 1

        indexes[left:right] = temp

    mergeSort(0, n)
    return result

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(*countSmaller(nums))"""
        })
    }
]

problems.extend(sorting_problems_data)

# Re-order and clean problem_num
for idx, p in enumerate(problems):
    p["problem_num"] = idx + 1

with open("backend/app/data/dsa_problems_seed.json", "w", encoding="utf-8") as f:
    json.dump(problems, f, indent=2)

print(f"Successfully added 15 sorting problems! Total problems now: {len(problems)}")

