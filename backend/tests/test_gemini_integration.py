import os
import sys
from unittest.mock import MagicMock, patch
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from backend.app.database.database import Base
from backend.app.models.project_chat import AIConversation, AIMessage, AIProject, AIProjectMemory
from backend.app.schemas.project_chat import AIChatRequest, AIConversationCreate, AIProjectCreate
from backend.app.services.academic_knowledge_engine import AcademicKnowledgeEngine
from backend.app.services.gemini_service import GeminiService, clean_for_speech, build_system_instruction
from backend.app.services.project_chat_service import ProjectChatService


@pytest.fixture
def db_session():
    """In-memory SQLite session for testing."""
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# -------------------------------------------------------------
# Test 1: Basic Q&A and Formatting
# -------------------------------------------------------------
def test_clean_for_speech_removes_markdown_and_code():
    raw_markdown = (
        "### 🐍 Python: Core Definition\n\n"
        "Python is a **high-level**, interpreted language. See [Python Docs](https://python.org).\n\n"
        "```python\nprint('Hello World')\n```\n\n"
        "> [!NOTE]\n> Widely used in AI."
    )
    spoken = clean_for_speech(raw_markdown)
    assert "###" not in spoken
    assert "```" not in spoken
    assert "print('Hello World')" not in spoken
    assert "[code snippet shown on screen]" in spoken
    assert "Python is a high-level, interpreted language." in spoken
    assert "https://python.org" not in spoken
    assert "[!NOTE]" not in spoken


def test_system_instruction_construction():
    instruction = build_system_instruction(
        project_name="Final Year ECE",
        project_memory="Discussed 8085 pins and UART baud rate.",
        project_description="Cap-stone robotics system",
    )
    assert "Final Year ECE" in instruction
    assert "8085 pins and UART baud rate" in instruction
    assert "Cap-stone robotics system" in instruction
    assert "SkillExa AI" in instruction


# -------------------------------------------------------------
# Test 2: Python & DSA Explanations
# -------------------------------------------------------------
def test_gemini_service_generates_python_and_dsa(db_session):
    mock_response = MagicMock()
    mock_response.text = (
        "### 📊 Binary Search in Python\n\n"
        "Binary search is an efficient algorithm with $O(\\log n)$ time complexity.\n\n"
        "```python\ndef binary_search(arr, target):\n    low, high = 0, len(arr) - 1\n```\n"
    )

    with patch.object(GeminiService, "is_configured", return_value=True), \
         patch.object(GeminiService, "_create_client") as mock_create_client:
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value = mock_response
        mock_create_client.return_value = mock_client

        reply, speech = GeminiService.generate_chat_response(
            user_query="Explain binary search and its time complexity",
            project_name="DSA Prep",
        )
        assert reply is not None
        assert "Binary Search in Python" in reply
        assert "$O(\\log n)$" in reply
        assert "```python" in reply
        assert speech is not None
        assert "```" not in speech


# -------------------------------------------------------------
# Test 3: Programming Code Debugging
# -------------------------------------------------------------
def test_gemini_code_debugging_guidelines(db_session):
    buggy_code_prompt = "Fix this Python code: my_list = [1, 2]; print(my_list[5])"
    mock_debug_response = MagicMock()
    mock_debug_response.text = (
        "### 🐞 Bug Analysis: IndexError\n\n"
        "**Root Cause**: You are attempting to access index 5, but the list only has 2 items (indices 0 and 1).\n\n"
        "#### Corrected Code:\n"
        "```python\nmy_list = [1, 2]\nif len(my_list) > 5:\n    print(my_list[5])\nelse:\n    print('Index out of bounds')\n```"
    )

    with patch.object(GeminiService, "is_configured", return_value=True), \
         patch.object(GeminiService, "_create_client") as mock_create_client:
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value = mock_debug_response
        mock_create_client.return_value = mock_client

        reply, speech = GeminiService.generate_chat_response(
            user_query=buggy_code_prompt,
            project_name="Python Debugging",
        )
        assert "IndexError" in reply
        assert "Root Cause" in reply
        assert "Corrected Code" in reply


# -------------------------------------------------------------
# Test 4: Follow-up Questions Using Conversation History
# -------------------------------------------------------------
def test_follow_up_question_with_past_messages():
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "Here is an example of recursion in Python: calculating factorial."
    mock_client.models.generate_content.return_value = mock_response

    msg1 = MagicMock(sender_type="user", message_text="What is recursion?")
    msg2 = MagicMock(sender_type="assistant", message_text="Recursion is a process where a function calls itself.")

    with patch.object(GeminiService, "is_configured", return_value=True), \
         patch.object(GeminiService, "_create_client", return_value=mock_client):
        reply, speech = GeminiService.generate_chat_response(
            user_query="Give me an example",
            past_messages=[msg1, msg2],
            project_name="General Chats",
        )
        assert reply is not None
        assert "factorial" in reply

        # Check that past messages were passed as structured contents
        call_kwargs = mock_client.models.generate_content.call_args[1]
        contents = call_kwargs["contents"]
        assert len(contents) == 3  # user msg1, model msg2, user current query
        assert contents[0].role == "user"
        assert contents[1].role == "model"
        assert contents[2].role == "user"
        assert contents[2].parts[0].text == "Give me an example"


# -------------------------------------------------------------
# Test 5: Voice Assistant Integration
# -------------------------------------------------------------
@pytest.mark.anyio
async def test_voice_assistant_chat_flow(db_session):
    student_id = "student_voice_001"
    request = AIChatRequest(
        message="define pyhton",
        input_type="voice",
        spoken_acknowledgement_needed=True,
    )

    response = await ProjectChatService.chat(db_session, student_id, request)

    assert response is not None
    assert response.project_name == "General Chats"
    assert response.reply is not None
    assert response.speech_text is not None
    # Spoken text must not contain raw code blocks or markdown hash headers
    assert "###" not in response.speech_text
    assert "```" not in response.speech_text
    assert len(response.speech_text) > 20
    assert response.acknowledgement in [
        "Hey! I’m here. What can I help you with?",
        "Hello! I’m listening.",
        "Yes! Tell me what you need.",
        "I’m here. Let’s get started!",
    ]


# -------------------------------------------------------------
# Test 6: API Failures & Rate Limits Fallback
# -------------------------------------------------------------
@pytest.mark.anyio
async def test_api_failure_fallback_to_academic_engine(db_session):
    """
    If Gemini throws an error or rate limit, ProjectChatService
    must gracefully fall back to AcademicKnowledgeEngine without throwing.
    """
    from google.genai import errors

    student_id = "student_fallback_002"
    request = AIChatRequest(
        message="define python",
        input_type="text",
    )

    # Simulate Gemini client raising an APIError (e.g. 429 quota or 500 server error)
    mock_client = MagicMock()
    mock_client.models.generate_content.side_effect = errors.APIError(code=429, response_json={"error": {"message": "Resource exhausted quota limit"}})

    with patch.object(GeminiService, "is_configured", return_value=True), \
         patch.object(GeminiService, "_create_client", return_value=mock_client):
        response = await ProjectChatService.chat(db_session, student_id, request)

        # Fallback to AcademicKnowledgeEngine produces the exact 6-section structure
        assert response is not None
        assert "Python" in response.reply
        assert "1. Definition" in response.reply
        assert "2. Simple Explanation" in response.reply
        assert "3. Important Features" in response.reply
        assert "4. Real-World Applications" in response.reply
        assert "5. Working Example" in response.reply
        assert "6. Summary" in response.reply


# -------------------------------------------------------------
# Test 7: Multiple Users & Separate Conversations
# -------------------------------------------------------------
@pytest.mark.anyio
async def test_multi_user_and_project_isolation(db_session):
    user_a = "user_alice@kvgce.edu.in"
    user_b = "user_bob@kvgce.edu.in"

    # User A creates a specialized Robotics project
    proj_a = ProjectChatService.create_project(
        db_session,
        user_a,
        AIProjectCreate(name="Robotics Lab", description="Embedded firmware"),
    )

    # User B creates a separate GATE ECE project
    proj_b = ProjectChatService.create_project(
        db_session,
        user_b,
        AIProjectCreate(name="GATE ECE Prep", description="Exam syllabus"),
    )

    req_a = AIChatRequest(
        project_id=proj_a.id,
        message="Explain microprocessors",
    )
    resp_a = await ProjectChatService.chat(db_session, user_a, req_a)
    assert resp_a.project_id == proj_a.id
    assert resp_a.project_name == "Robotics Lab"

    req_b = AIChatRequest(
        project_id=proj_b.id,
        message="Explain pointers in C",
    )
    resp_b = await ProjectChatService.chat(db_session, user_b, req_b)
    assert resp_b.project_id == proj_b.id
    assert resp_b.project_name == "GATE ECE Prep"

    # Verify that User A only sees their own projects
    user_a_projects = ProjectChatService.list_projects(db_session, user_a)
    user_a_names = [p["name"] for p in user_a_projects]
    assert "Robotics Lab" in user_a_names
    assert "GATE ECE Prep" not in user_a_names

    # Verify User B only sees their own projects
    user_b_projects = ProjectChatService.list_projects(db_session, user_b)
    user_b_names = [p["name"] for p in user_b_projects]
    assert "GATE ECE Prep" in user_b_names
    assert "Robotics Lab" not in user_b_names
