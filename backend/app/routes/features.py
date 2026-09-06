from typing import Any, Dict, List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import subprocess
import sys

router = APIRouter(prefix="/api", tags=["features"])

# --- DSA PRACTICE DATA & ENDPOINTS ---

DSA_PROBLEMS: List[Dict[str, Any]] = [
    {
        "id": "two-sum",
        "title": "1. Two Sum",
        "category": "Arrays",
        "difficulty": "Easy",
        "description": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.",
        "input_example": "nums = [2, 7, 11, 15], target = 9",
        "output_example": "[0, 1]",
        "starter_code": """def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

# Test execution
print(two_sum([2, 7, 11, 15], 9))
"""
    },
    {
        "id": "reverse-linked-list",
        "title": "2. Reverse a Linked List",
        "category": "Linked Lists",
        "difficulty": "Easy",
        "description": "Given the `head` of a singly linked list, reverse the list and return its reversed representation.",
        "input_example": "head = [1, 2, 3, 4, 5]",
        "output_example": "[5, 4, 3, 2, 1]",
        "starter_code": """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# Helper to build & print list
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

rev = reverse_list(node1)
res = []
while rev:
    res.append(rev.val)
    rev = rev.next
print(res)
"""
    },
    {
        "id": "valid-parentheses",
        "title": "3. Valid Parentheses",
        "category": "Stack & Queue",
        "difficulty": "Easy",
        "description": "Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
        "input_example": "s = \"()[]{}\"",
        "output_example": "True",
        "starter_code": """def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

print(is_valid("()[]{}"))
"""
    },
    {
        "id": "binary-tree-inorder",
        "title": "4. Binary Tree Inorder Traversal",
        "category": "Trees & Graphs",
        "difficulty": "Medium",
        "description": "Given the root of a binary tree, return the inorder traversal of its nodes' values.",
        "input_example": "root = [1, null, 2, 3]",
        "output_example": "[1, 3, 2]",
        "starter_code": """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    res = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        res.append(node.val)
        helper(node.right)
    helper(root)
    return res

# Tree: 1 -> right: 2 -> left: 3
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(inorder_traversal(root))
"""
    },
    {
        "id": "climbing-stairs",
        "title": "5. Climbing Stairs",
        "category": "Dynamic Programming",
        "difficulty": "Easy",
        "description": "You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
        "input_example": "n = 5",
        "output_example": "8",
        "starter_code": """def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    one, two = 1, 2
    for _ in range(3, n + 1):
        one, two = two, one + two
    return two

print("Ways to climb 5 steps:", climb_stairs(5))
"""
    }
]

class DSASubmission(BaseModel):
    problem_id: str
    code: str

@router.get("/dsa/problems")
def get_dsa_problems() -> List[Dict[str, Any]]:
    return DSA_PROBLEMS

@router.post("/dsa/submit")
def submit_dsa_solution(payload: DSASubmission) -> Dict[str, Any]:
    try:
        completed = subprocess.run(
            [sys.executable, "-c", payload.code],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        return {
            "success": completed.returncode == 0,
            "output": completed.stdout.rstrip("\n"),
            "error": completed.stderr.rstrip("\n"),
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "output": "",
            "error": "Execution timed out after 5 seconds.",
        }


# --- AI MOCK INTERVIEW DATA & ENDPOINTS ---

INTERVIEW_QUESTIONS: Dict[str, List[Dict[str, Any]]] = {
    "Backend Systems": [
        {
            "id": "b1",
            "question": "How do you design a high-throughput, low-latency rate limiter system in Python or Go?",
            "key_points": ["Token bucket / Leaky bucket algorithm", "Redis / Distributed memory cache", "Sliding window counter"],
            "difficulty": "Hard"
        },
        {
            "id": "b2",
            "question": "Explain the difference between SQL transactions (ACID) and NoSQL eventual consistency.",
            "key_points": ["Atomicity, Consistency, Isolation, Durability", "CAP Theorem", "WAL logs and replication"],
            "difficulty": "Medium"
        }
    ],
    "Frontend Engineer": [
        {
            "id": "f1",
            "question": "Explain how the Browser Event Loop handles microtasks (Promises) vs macrotasks (setTimeout).",
            "key_points": ["Call stack", "Microtask queue priority", "Event loop cycle"],
            "difficulty": "Medium"
        },
        {
            "id": "f2",
            "question": "How do you optimize page render time and eliminate Cumulative Layout Shift (CLS)?",
            "key_points": ["Preloading fonts/assets", "Explicit dimensions for images/iframes", "Critical CSS rendering"],
            "difficulty": "Medium"
        }
    ],
    "Full Stack": [
        {
            "id": "fs1",
            "question": "Walk me through how JWT authentication works end-to-end between a SPA frontend and REST API backend.",
            "key_points": ["Header, Payload, Signature", "HttpOnly Cookies vs LocalStorage", "Refresh token rotation"],
            "difficulty": "Medium"
        }
    ]
}

class InterviewStartRequest(BaseModel):
    role: str

class InterviewSubmitRequest(BaseModel):
    role: str
    question_id: str
    user_answer: str

@router.post("/interview/start")
def start_interview(payload: InterviewStartRequest) -> Dict[str, Any]:
    role = payload.role if payload.role in INTERVIEW_QUESTIONS else "Backend Systems"
    questions = INTERVIEW_QUESTIONS.get(role, INTERVIEW_QUESTIONS["Backend Systems"])
    return {
        "status": "active",
        "role": role,
        "questions": questions,
        "current_question": questions[0]
    }

@router.post("/interview/submit")
def submit_interview_answer(payload: InterviewSubmitRequest) -> Dict[str, Any]:
    answer = payload.user_answer.strip()
    if len(answer) < 15:
        score = 45
        feedback = "Answer is too brief. Provide more technical details, mention specific data structures, algorithms, or architectural patterns."
        status = "Needs Improvement"
    else:
        score = min(98, 70 + min(28, len(answer) // 8))
        feedback = "Strong technical explanation! Great breakdown of core architectural concepts and trade-offs."
        status = "Passed"
        
    return {
        "score": score,
        "status": status,
        "feedback": feedback,
        "metrics": {
            "technical_depth": min(100, score + 2),
            "clarity": min(100, score - 3),
            "edge_case_handling": min(100, score - 5),
        }
    }


# --- AI RESUME BUILDER ENDPOINTS ---

class ResumePayload(BaseModel):
    full_name: str
    title: str
    email: str
    phone: str
    location: str
    summary: str
    skills: str
    experience: str
    projects: str
    education: str

@router.post("/resume/generate")
def generate_resume(payload: ResumePayload) -> Dict[str, Any]:
    skills_list = [s.strip() for s in payload.skills.split(",") if s.strip()]
    
    formatted_markdown = f"""# {payload.full_name or 'John Doe'}
**{payload.title or 'Full Stack Software Engineer'}**
📧 {payload.email or 'john@example.com'} | 📱 {payload.phone or '+1 555-0199'} | 📍 {payload.location or 'San Francisco, CA'}

---

## 💡 Executive Summary
{payload.summary or 'Passionate software engineer experienced in building high-scalability web applications and distributed backend microservices.'}

## 🛠 Tech Skills
{', '.join(skills_list) if skills_list else 'Python, FastAPI, C, JavaScript, PostgreSQL, Docker, Git'}

## 💼 Work Experience
{payload.experience or '• Senior Developer @ SkillExa (2024 - Present)\n  - Engineered RESTful microservices with 99.9% uptime.\n  - Optimized SQL query response times by 40%.'}

## 🚀 Key Projects
{payload.projects or '• SkillExa Learning Platform: Full-stack interactive code execution engine and DSA studio.'}

## 🎓 Education
{payload.education or 'B.S. in Computer Science - University of Technology'}
"""
    return {
        "success": True,
        "markdown": formatted_markdown,
        "preview_data": payload.model_dump()
    }
