export interface DsaCodingProblem {
  id: string;
  title: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  statement: string;
  inputDesc: string;
  outputDesc: string;
  constraints: string;
  sampleInput: string;
  sampleOutput: string;
  starterCode: string;
  solutionCode: string;
  testCases: { input: string; expected: string }[];
}

export interface DsaTopic {
  id: string;
  number: number;
  name: string;
  desc: string;
  complexity: string;
  theory: string;
  syntaxAndCode: string;
  explanation: string;
  inputOutputExample: { input: string; output: string; desc: string };
  interviewQuestions: string[];
  mcqs: { question: string; options: string[]; correctIndex: number; explanation: string }[];
  problem: DsaCodingProblem;
}

export const DSA_TOPICS_LIST = [
  'Basics of DSA',
  'Time & Space Complexity',
  'Arrays',
  'Strings',
  'Linked Lists',
  'Stack',
  'Queue',
  'Recursion',
  'Searching',
  'Sorting',
  'Hashing',
  'Trees',
  'Binary Search Tree',
  'Heap / Priority Queue',
  'Graphs',
  'Greedy Algorithms',
  'Dynamic Programming',
  'Backtracking',
];

export const DSA_DATABASE: {
  c: Record<string, DsaTopic>;
  python: Record<string, DsaTopic>;
} = {
  // ==========================================
  // DSA IN C
  // ==========================================
  c: {
    'Arrays': {
      id: 'c-arrays',
      number: 3,
      name: 'Arrays in C',
      desc: 'Contiguous memory allocation, pointer arithmetic, 2D matrices, and sliding window.',
      complexity: 'Access: O(1) | Insertion/Deletion: O(N) | Space: O(N)',
      theory: 'An array in C is a contiguous block of memory storing elements of the same data type. Because arrays are zero-indexed, the address of element arr[i] is computed as: Base_Address + (i * sizeof(datatype)). Pointers and arrays are closely linked in C — the array name evaluates to the address of the first element (arr == &arr[0]).',
      syntaxAndCode: `#include <stdio.h>

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", *(arr + i)); // Pointer arithmetic equivalent to arr[i]
    }
    printf("\\n");
}

int main() {
    int numbers[5] = {10, 20, 30, 40, 50};
    int n = sizeof(numbers) / sizeof(numbers[0]);
    printArray(numbers, n);
    return 0;
}`,
      explanation: 'In C, passing an array to a function decays the array to a pointer (`int*`). Modifying the array inside the helper function modifies the original caller memory directly.',
      inputOutputExample: {
        input: 'Array: [10, 20, 30, 40, 50]',
        output: '10 20 30 40 50',
        desc: 'Sequential traversal using pointer arithmetic *(arr + i).',
      },
      interviewQuestions: [
        'How does C manage memory for dynamic arrays created with malloc() vs static stack arrays?',
        'What happens when you access an index out of bounds in C? (Undefined behavior, segmentation fault)',
        'How do you pass a 2D array to a function in C? (Specify column dimension: int arr[][COL])',
      ],
      mcqs: [
        {
          question: 'In C, if `arr` is an integer array of base address 2000, and `sizeof(int)` is 4 bytes, what is the value of `arr + 3`?',
          options: ['2003', '2012', '2006', '2000'],
          correctIndex: 1,
          explanation: 'Pointer arithmetic increments by index * sizeof(type) = 2000 + 3 * 4 = 2012.',
        },
        {
          question: 'What is the time complexity of searching an element in an unsorted C array of size N?',
          options: ['O(1)', 'O(log N)', 'O(N)', 'O(N^2)'],
          correctIndex: 2,
          explanation: 'Linear scan requires checking each of the N elements in the worst case.',
        },
      ],
      problem: {
        id: 'c-prob-reverse-array',
        title: 'Reverse an Array in Place',
        difficulty: 'Easy',
        statement: 'Given an array of integers, reverse the array in place using two pointers in C.',
        inputDesc: 'First line contains integer N. Second line contains N space-separated integers.',
        outputDesc: 'Print the reversed array elements separated by spaces.',
        constraints: '1 <= N <= 10^5, -10^9 <= arr[i] <= 10^9',
        sampleInput: '5\n1 2 3 4 5',
        sampleOutput: '5 4 3 2 1',
        starterCode: `#include <stdio.h>

void reverseArray(int arr[], int n) {
    int left = 0, right = n - 1;
    while (left < right) {
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = 5;
    reverseArray(arr, n);
    for(int i=0; i<n; i++) printf("%d ", arr[i]);
    return 0;
}`,
        solutionCode: `#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    
    int l = 0, r = n - 1;
    while (l < r) {
        int t = arr[l];
        arr[l] = arr[r];
        arr[r] = t;
        l++; r--;
    }
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}`,
        testCases: [
          { input: '5\n1 2 3 4 5', expected: '5 4 3 2 1' },
          { input: '4\n10 20 30 40', expected: '40 30 20 10' },
        ],
      },
    },

    'Linked Lists': {
      id: 'c-linked-list',
      number: 5,
      name: 'Linked Lists in C',
      desc: 'Dynamic node allocation with malloc(), singly, doubly, and circular linked lists.',
      complexity: 'Access: O(N) | Insertion at Head: O(1) | Space: O(N)',
      theory: 'A linked list in C is a linear collection of struct nodes where each node contains data and a pointer (`next`) to the next node in heap memory. Unlike arrays, nodes are not stored contiguously, allowing efficient O(1) insertions and deletions without memory reallocation.',
      syntaxAndCode: `#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* createNode(int val) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = val;
    newNode->next = NULL;
    return newNode;
}

int main() {
    struct Node* head = createNode(10);
    head->next = createNode(20);
    head->next->next = createNode(30);
    
    struct Node* curr = head;
    while (curr != NULL) {
        printf("%d -> ", curr->data);
        curr = curr->next;
    }
    printf("NULL\\n");
    return 0;
}`,
      explanation: 'Every node is dynamically allocated on the heap via `malloc()`. Always free allocated memory with `free()` when deleting nodes to prevent memory leaks.',
      inputOutputExample: {
        input: 'Nodes: 10, 20, 30',
        output: '10 -> 20 -> 30 -> NULL',
        desc: 'Traversal through struct node pointers until reaching NULL.',
      },
      interviewQuestions: [
        'How do you detect a cycle in a singly linked list in C? (Floyd Cycle-Finding / Tortoise and Hare algorithm)',
        'What is the difference between malloc() and calloc() when creating linked list nodes in C?',
        'How do you find the middle element of a linked list in a single pass? (Fast & Slow pointer)',
      ],
      mcqs: [
        {
          question: 'What is the time complexity to insert a new node at the beginning of a singly linked list in C?',
          options: ['O(1)', 'O(N)', 'O(log N)', 'O(N^2)'],
          correctIndex: 0,
          explanation: 'Updating the new node next pointer to head and updating head is done in O(1) constant time.',
        },
      ],
      problem: {
        id: 'c-prob-reverse-ll',
        title: 'Reverse a Singly Linked List',
        difficulty: 'Medium',
        statement: 'Given the head of a singly linked list, reverse the list and return the new head pointer in C.',
        inputDesc: 'Space separated integers ending with -1.',
        outputDesc: 'Space separated reversed integers.',
        constraints: '0 <= Number of nodes <= 5000',
        sampleInput: '1 2 3 4 5 -1',
        sampleOutput: '5 4 3 2 1',
        starterCode: `struct Node* reverseList(struct Node* head) {\n    struct Node *prev = NULL, *curr = head, *next = NULL;\n    while (curr != NULL) {\n        next = curr->next;\n        curr->next = prev;\n        prev = curr;\n        curr = next;\n    }\n    return prev;\n}`,
        solutionCode: `struct Node* reverseList(struct Node* head) {\n    struct Node *prev = NULL, *curr = head, *next = NULL;\n    while (curr != NULL) {\n        next = curr->next;\n        curr->next = prev;\n        prev = curr;\n        curr = next;\n    }\n    return prev;\n}`,
        testCases: [{ input: '1 2 3 -1', expected: '3 2 1' }],
      },
    },
  },

  // ==========================================
  // DSA IN PYTHON
  // ==========================================
  python: {
    'Arrays': {
      id: 'py-arrays',
      number: 3,
      name: 'Arrays & Lists in Python',
      desc: 'Dynamic arrays (list), slicing, list comprehensions, two-pointer techniques, and prefix sums.',
      complexity: 'Access: O(1) | Append: O(1) amortized | Insert/Delete: O(N) | Space: O(N)',
      theory: 'In Python, standard arrays are implemented via dynamic `list` objects. Python lists store references to objects contiguously in memory. When the capacity is exceeded, Python over-allocates extra memory, giving amortized O(1) append operations.',
      syntaxAndCode: `# Two-pointer technique for checking palindromes
def is_palindrome(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True

nums = [1, 2, 3, 2, 1]
print("Is Palindrome:", is_palindrome(nums)) # True`,
      explanation: 'Python slicing `nums[::-1]` creates a reversed copy in O(N) time and O(N) space. The two-pointer in-place approach uses O(1) auxiliary space.',
      inputOutputExample: {
        input: 'nums = [1, 2, 3, 2, 1]',
        output: 'Is Palindrome: True',
        desc: 'Comparing elements from outer boundaries moving inward.',
      },
      interviewQuestions: [
        'How does Python list resizing work under the hood? (Over-allocation formula: 0, 4, 8, 16, 25, 35...)',
        'What is the difference between list.append() and list.extend() in Python?',
        'How do you find the contiguous subarray with the maximum sum in Python? (Kadane Algorithm)',
      ],
      mcqs: [
        {
          question: 'What is the time complexity of `list.pop(0)` in Python?',
          options: ['O(1)', 'O(N)', 'O(log N)', 'O(N^2)'],
          correctIndex: 1,
          explanation: 'Removing the first element requires shifting all remaining N-1 elements to the left, taking O(N) time.',
        },
      ],
      problem: {
        id: 'py-prob-two-sum',
        title: 'Two Sum Problem',
        difficulty: 'Easy',
        statement: 'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.',
        inputDesc: 'nums = [2, 7, 11, 15], target = 9',
        outputDesc: '[0, 1]',
        constraints: '2 <= len(nums) <= 10^4',
        sampleInput: '[2, 7, 11, 15], 9',
        sampleOutput: '[0, 1]',
        starterCode: `def two_sum(nums, target):\n    seen = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in seen:\n            return [seen[complement], i]\n        seen[num] = i\n    return []`,
        solutionCode: `def two_sum(nums, target):\n    seen = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in seen:\n            return [seen[complement], i]\n        seen[num] = i\n    return []`,
        testCases: [
          { input: 'nums=[2, 7, 11, 15], target=9', expected: '[0, 1]' },
          { input: 'nums=[3, 2, 4], target=6', expected: '[1, 2]' },
        ],
      },
    },

    'Linked Lists': {
      id: 'py-linked-list',
      number: 5,
      name: 'Linked Lists in Python',
      desc: 'Object-oriented Node classes, Singly/Doubly Linked Lists, Fast & Slow pointers.',
      complexity: 'Access: O(N) | Prepend: O(1) | Delete Node: O(1) with pointer | Space: O(N)',
      theory: 'Linked Lists in Python are constructed using class objects. Each ListNode holds a `val` attribute and a `next` reference. Python automatic garbage collection cleans up unreferenced nodes.',
      syntaxAndCode: `class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    curr = head
    res = []
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(res) + " -> None")

# Creating linked list: 1 -> 2 -> 3
head = ListNode(1, ListNode(2, ListNode(3)))
print_list(head)`,
      explanation: 'Python uses object references. Traversal proceeds until `curr` evaluates to `None`.',
      inputOutputExample: {
        input: 'ListNode(1, ListNode(2, ListNode(3)))',
        output: '1 -> 2 -> 3 -> None',
        desc: 'Formatted traversal string of linked nodes.',
      },
      interviewQuestions: [
        'How do you find the intersection node of two singly linked lists in Python?',
        'Explain Floyd Cycle detection algorithm using slow and fast pointers.',
      ],
      mcqs: [
        {
          question: 'What is the auxiliary space complexity of reversing a linked list iteratively in Python?',
          options: ['O(1)', 'O(N)', 'O(log N)', 'O(N^2)'],
          correctIndex: 0,
          explanation: 'Iterative reversal only requires three pointer variables (prev, curr, next), taking O(1) space.',
        },
      ],
      problem: {
        id: 'py-prob-middle-ll',
        title: 'Middle of the Linked List',
        difficulty: 'Easy',
        statement: 'Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.',
        inputDesc: 'head = [1,2,3,4,5]',
        outputDesc: '[3,4,5]',
        constraints: '1 <= Number of nodes <= 100',
        sampleInput: '[1,2,3,4,5]',
        sampleOutput: '[3,4,5]',
        starterCode: `def middleNode(head):\n    slow = fast = head\n    while fast and fast.next:\n        slow = slow.next\n        fast = fast.next.next\n    return slow`,
        solutionCode: `def middleNode(head):\n    slow = fast = head\n    while fast and fast.next:\n        slow = slow.next\n        fast = fast.next.next\n    return slow`,
        testCases: [{ input: '[1,2,3,4,5]', expected: '[3,4,5]' }],
      },
    },
  },
};

export function getDsaTopic(language: 'c' | 'python', topicName: string): DsaTopic {
  const langDb = DSA_DATABASE[language] || DSA_DATABASE.c;
  if (langDb[topicName]) return langDb[topicName];

  // Try partial match
  const foundKey = Object.keys(langDb).find(k => k.toLowerCase().includes(topicName.toLowerCase()) || topicName.toLowerCase().includes(k.toLowerCase()));
  if (foundKey && langDb[foundKey]) return langDb[foundKey];

  // Fallback high-yield template
  const isC = language === 'c';
  return {
    id: `${language}-${topicName.toLowerCase().replace(/[^a-z0-9]/g, '-')}`,
    number: 1,
    name: `${topicName} (${isC ? 'C' : 'Python'})`,
    desc: `Comprehensive algorithmic principles, memory layout, and implementation of ${topicName} in ${isC ? 'C' : 'Python'}.`,
    complexity: 'Time: O(N) | Space: O(1)',
    theory: `${topicName} is a foundational data structure/algorithm topic. In ${isC ? 'C, low-level pointer management and explicit memory bounds are paramount.' : 'Python, high-level abstractions and expressive built-in data types streamline implementation.'}`,
    syntaxAndCode: isC
      ? `// ${topicName} in C\n#include <stdio.h>\n\nint main() {\n    printf("Mastering ${topicName} in C.\\n");\n    return 0;\n}`
      : `# ${topicName} in Python\ndef solve_${topicName.toLowerCase().replace(/[^a-z0-9]/g, '_')}():\n    print("Mastering ${topicName} in Python")\n\nsolve_${topicName.toLowerCase().replace(/[^a-z0-9]/g, '_')}()`,
    explanation: `Analyze step-by-step state transitions and invariant properties of ${topicName}.`,
    inputOutputExample: {
      input: 'Sample Problem Input',
      output: 'Optimal Result',
      desc: `Demonstrates the core algorithmic transformation for ${topicName}.`,
    },
    interviewQuestions: [
      `What are the best, average, and worst-case time complexities of ${topicName}?`,
      `How does ${topicName} compare against alternative data structures for frequent lookups?`,
    ],
    mcqs: [
      {
        question: `What is the primary design trade-off when selecting ${topicName}?`,
        options: ['Time vs Space Complexity', 'Color Scheme', 'Operating System', 'File System'],
        correctIndex: 0,
        explanation: 'Algorithmic engineering fundamentally balances time efficiency against memory usage.',
      },
    ],
    problem: {
      id: `${language}-prob-${topicName.toLowerCase().replace(/[^a-z0-9]/g, '-')}`,
      title: `${topicName} Practice Challenge`,
      difficulty: 'Medium',
      statement: `Implement an optimal solution for the classic ${topicName} problem in ${isC ? 'C' : 'Python'}.`,
      inputDesc: 'Standard test input',
      outputDesc: 'Expected output',
      constraints: 'N <= 10^5',
      sampleInput: '5',
      sampleOutput: '5',
      starterCode: isC ? '#include <stdio.h>\nint main() {\n    // Code here\n    return 0;\n}' : 'def solve():\n    pass',
      solutionCode: isC ? '#include <stdio.h>\nint main() {\n    return 0;\n}' : 'def solve():\n    return True',
      testCases: [{ input: '5', expected: '5' }],
    },
  };
}
