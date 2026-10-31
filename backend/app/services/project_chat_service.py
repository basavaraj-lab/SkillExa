import json
import logging
import os
import random
import re
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import desc

from backend.app.models.project_chat import (
    AIConversation,
    AIMessage,
    AIProject,
    AIProjectMemory,
)
from backend.app.schemas.project_chat import (
    AIChatRequest,
    AIChatResponse,
    AIConversationCreate,
    AIConversationUpdate,
    AIProjectCreate,
    AIProjectUpdate,
)
from backend.app.services.ai_provider_service import AIProviderService
from backend.app.services.web_search_service import WebSearchService
from backend.app.services.academic_knowledge_engine import AcademicKnowledgeEngine, normalize_query
from backend.app.services.gemini_service import GeminiService

logger = logging.getLogger("skillexa.project_chat")

VARIED_ACKNOWLEDGEMENTS = [
    "Hey! I’m here. What can I help you with?",
    "Hello! I’m listening.",
    "Yes! Tell me what you need.",
    "I’m here. Let’s get started!",
]


def clean_for_speech(text: str) -> str:
    """Transform markdown/code response into concise, clean conversational speech."""
    if not text:
        return ""
    # Remove code blocks
    cleaned = re.sub(r"```[\s\S]*?```", " [code snippet shown on screen] ", text)
    # Remove inline code backticks
    cleaned = re.sub(r"`([^`]+)`", r"\1", cleaned)
    # Remove markdown links [title](url) -> title
    cleaned = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", cleaned)
    # Remove markdown headers and list bullets
    cleaned = re.sub(r"#{1,6}\s*", "", cleaned)
    cleaned = re.sub(r"(\*\*|\*|__|_)", "", cleaned)
    cleaned = re.sub(r"^\s*[-*+]\s+", "", cleaned, flags=re.MULTILINE)
    # Condense whitespace
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    # Limit to first 2-3 sentences for spoken output if it's too long
    sentences = re.split(r"(?<=[.!?])\s+", cleaned)
    if len(sentences) > 3:
        return " ".join(sentences[:3]) + " I've provided the full details and examples in the chat."
    return cleaned


class ProjectChatService:
    """
    Core orchestrator for Project-Wise Chat Management,
    Project-Specific AI Memory, Multi-Turn Voice/Text Dialogues,
    and Educational Web Search Grounding.
    """

    # -------------------------------------------------------------
    # 1. PROJECT MANAGEMENT
    # -------------------------------------------------------------
    @classmethod
    def get_or_create_default_project(cls, db: Session, student_id: str) -> AIProject:
        project = (
            db.query(AIProject)
            .filter(AIProject.student_id == student_id, AIProject.name == "General Chats")
            .first()
        )
        if not project:
            project = AIProject(
                student_id=student_id,
                name="General Chats",
                description="Default workspace for general questions, quick doubts, and spontaneous practice.",
                icon="message-square",
                is_pinned=True,
            )
            db.add(project)
            db.commit()
            db.refresh(project)

            # Initialize memory
            memory = AIProjectMemory(
                project_id=project.id,
                memory_summary="General discussions, introductory questions, and quick learning topics.",
                key_entities={"topics": []},
            )
            db.add(memory)
            db.commit()

        return project

    @classmethod
    def list_projects(cls, db: Session, student_id: str) -> List[Dict[str, Any]]:
        # Ensure default project exists
        cls.get_or_create_default_project(db, student_id)

        projects = (
            db.query(AIProject)
            .filter(AIProject.student_id == student_id)
            .order_by(desc(AIProject.is_pinned), desc(AIProject.updated_at))
            .all()
        )

        results = []
        for p in projects:
            conv_count = db.query(AIConversation).filter(AIConversation.project_id == p.id).count()
            results.append({
                "id": p.id,
                "student_id": p.student_id,
                "name": p.name,
                "description": p.description,
                "icon": p.icon,
                "context_prompt": p.context_prompt,
                "is_pinned": p.is_pinned,
                "conversation_count": conv_count,
                "created_at": p.created_at,
                "updated_at": p.updated_at,
            })
        return results

    @classmethod
    def create_project(cls, db: Session, student_id: str, data: AIProjectCreate) -> AIProject:
        project = AIProject(
            student_id=student_id,
            name=data.name.strip(),
            description=data.description,
            icon=data.icon or "folder",
            context_prompt=data.context_prompt,
        )
        db.add(project)
        db.commit()
        db.refresh(project)

        # Initialize project memory
        memory = AIProjectMemory(
            project_id=project.id,
            memory_summary=f"Project '{project.name}' initialized. Description: {data.description or 'No description provided.'}",
            key_entities={"topics": [], "components": [], "architecture": []},
        )
        db.add(memory)
        db.commit()

        return project

    @classmethod
    def update_project(cls, db: Session, project_id: str, student_id: str, data: AIProjectUpdate) -> Optional[AIProject]:
        project = (
            db.query(AIProject)
            .filter(AIProject.id == project_id, AIProject.student_id == student_id)
            .first()
        )
        if not project:
            return None

        if data.name is not None:
            project.name = data.name.strip()
        if data.description is not None:
            project.description = data.description
        if data.icon is not None:
            project.icon = data.icon
        if data.context_prompt is not None:
            project.context_prompt = data.context_prompt
        if data.is_pinned is not None:
            project.is_pinned = data.is_pinned

        project.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(project)
        return project

    @classmethod
    def delete_project(cls, db: Session, project_id: str, student_id: str) -> bool:
        project = (
            db.query(AIProject)
            .filter(AIProject.id == project_id, AIProject.student_id == student_id)
            .first()
        )
        if not project:
            return False

        # Prevent deletion of General Chats default project
        if project.name == "General Chats":
            return False

        db.delete(project)
        db.commit()
        return True

    # -------------------------------------------------------------
    # 2. CONVERSATION MANAGEMENT
    # -------------------------------------------------------------
    @classmethod
    def list_conversations(cls, db: Session, student_id: str, project_id: Optional[str] = None) -> List[Dict[str, Any]]:
        query = db.query(AIConversation).filter(AIConversation.student_id == student_id)
        if project_id:
            query = query.filter(AIConversation.project_id == project_id)
        
        conversations = query.order_by(desc(AIConversation.updated_at)).all()
        results = []
        for c in conversations:
            msg_count = db.query(AIMessage).filter(AIMessage.conversation_id == c.id).count()
            last_msg = (
                db.query(AIMessage)
                .filter(AIMessage.conversation_id == c.id)
                .order_by(desc(AIMessage.created_at))
                .first()
            )
            preview = last_msg.message_text[:80] if last_msg else None
            results.append({
                "id": c.id,
                "project_id": c.project_id,
                "project_name": c.project.name if c.project else "General Chats",
                "student_id": c.student_id,
                "title": c.title,
                "message_count": msg_count,
                "last_message_preview": preview,
                "created_at": c.created_at,
                "updated_at": c.updated_at,
            })
        return results

    @classmethod
    def create_conversation(cls, db: Session, student_id: str, data: AIConversationCreate) -> AIConversation:
        target_project_id = data.project_id
        if not target_project_id:
            default_proj = cls.get_or_create_default_project(db, student_id)
            target_project_id = default_proj.id

        conversation = AIConversation(
            project_id=target_project_id,
            student_id=student_id,
            title=(data.title or "New Conversation").strip(),
        )
        db.add(conversation)
        db.commit()
        db.refresh(conversation)
        return conversation

    @classmethod
    def get_conversation_detail(cls, db: Session, conversation_id: str, student_id: str) -> Optional[Dict[str, Any]]:
        conv = (
            db.query(AIConversation)
            .filter(AIConversation.id == conversation_id, AIConversation.student_id == student_id)
            .first()
        )
        if not conv:
            return None

        messages = (
            db.query(AIMessage)
            .filter(AIMessage.conversation_id == conv.id)
            .order_by(AIMessage.created_at)
            .all()
        )

        return {
            "id": conv.id,
            "project_id": conv.project_id,
            "project_name": conv.project.name if conv.project else "General Chats",
            "student_id": conv.student_id,
            "title": conv.title,
            "messages": [
                {
                    "id": m.id,
                    "conversation_id": m.conversation_id,
                    "sender_type": m.sender_type,
                    "message_text": m.message_text,
                    "input_type": m.input_type,
                    "search_sources": m.search_sources or [],
                    "created_at": m.created_at,
                }
                for m in messages
            ],
            "created_at": conv.created_at,
            "updated_at": conv.updated_at,
        }

    @classmethod
    def update_conversation(
        cls, db: Session, conversation_id: str, student_id: str, data: AIConversationUpdate
    ) -> Optional[AIConversation]:
        conv = (
            db.query(AIConversation)
            .filter(AIConversation.id == conversation_id, AIConversation.student_id == student_id)
            .first()
        )
        if not conv:
            return None

        if data.title is not None:
            conv.title = data.title.strip()
        if data.project_id is not None:
            # Verify project belongs to user
            target_proj = (
                db.query(AIProject)
                .filter(AIProject.id == data.project_id, AIProject.student_id == student_id)
                .first()
            )
            if target_proj:
                conv.project_id = target_proj.id

        conv.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(conv)
        return conv

    @classmethod
    def delete_conversation(cls, db: Session, conversation_id: str, student_id: str) -> bool:
        conv = (
            db.query(AIConversation)
            .filter(AIConversation.id == conversation_id, AIConversation.student_id == student_id)
            .first()
        )
        if not conv:
            return False

        db.delete(conv)
        db.commit()
        return True

    # -------------------------------------------------------------
    # 3. PROJECT-SPECIFIC MEMORY CONSOLIDATION
    # -------------------------------------------------------------
    @classmethod
    def get_project_memory(cls, db: Session, project_id: str, student_id: str) -> Optional[Dict[str, Any]]:
        project = (
            db.query(AIProject)
            .filter(AIProject.id == project_id, AIProject.student_id == student_id)
            .first()
        )
        if not project:
            return None

        memory = db.query(AIProjectMemory).filter(AIProjectMemory.project_id == project.id).first()
        summary = memory.memory_summary if memory else f"Workspace for {project.name}"
        entities = memory.key_entities if memory else {}

        return {
            "project_id": project.id,
            "project_name": project.name,
            "memory_summary": summary,
            "key_entities": entities,
            "updated_at": memory.updated_at if memory else project.updated_at,
        }

    @classmethod
    def update_project_memory(cls, db: Session, project_id: str, new_user_msg: str, new_ai_msg: str):
        """Asynchronously or synchronously update running project memory with key concepts."""
        memory = db.query(AIProjectMemory).filter(AIProjectMemory.project_id == project_id).first()
        if not memory:
            memory = AIProjectMemory(
                project_id=project_id,
                memory_summary="",
                key_entities={"topics": []},
            )
            db.add(memory)

        # Extract topics or entities from user message
        lowered = new_user_msg.lower()
        detected_topics = []
        for kw in [
            "python", "variable", "function", "oop", "class", "file handling", "exception",
            "pointer", "array", "linked list", "tree", "graph", "dynamic programming", "sorting",
            "microprocessor", "8085", "8086", "embedded", "vlsi", "signals", "gate", "ssc",
            "architecture", "database", "backend", "frontend", "api", "final year project"
        ]:
            if kw in lowered:
                detected_topics.append(kw.title())

        entities = dict(memory.key_entities or {})
        existing_topics = set(entities.get("topics", []))
        existing_topics.update(detected_topics)
        entities["topics"] = list(existing_topics)[:20]

        # Update summary text
        bullet = f"- Topic/Focus: {new_user_msg[:90]} (Discussed: {datetime.utcnow().strftime('%d %b %Y')})"
        current_lines = [line for line in (memory.memory_summary or "").split("\n") if line.strip()]
        current_lines.append(bullet)
        # Keep last 15 memory points to avoid memory bloat
        memory.memory_summary = "\n".join(current_lines[-15:])
        memory.key_entities = entities
        memory.updated_at = datetime.utcnow()
        db.commit()

    # -------------------------------------------------------------
    # 4. CHAT COMPLETION & VOICE/TEXT UNIVERSAL SYNC
    # -------------------------------------------------------------
    @classmethod
    async def chat(cls, db: Session, student_id: str, request: AIChatRequest) -> AIChatResponse:
        user_message_text = request.message.strip()

        # Step 0: Guard against empty user messages
        if not user_message_text:
            return AIChatResponse(
                project_id=request.project_id or "",
                project_name="General Chats",
                conversation_id=request.conversation_id or "",
                conversation_title="Conversation",
                reply="Please enter a question or topic so I can help you learn!",
                speech_text="Please ask a question or enter a topic so I can help you.",
                search_sources=[],
                memory_summary="",
                acknowledgement=None,
            )

        # Step A: Check for Project Creation Command (Scenario 3 in user request)
        # e.g., "Create a project called Final Year ECE Project"
        create_project_match = re.search(
            r"(?:create|make|start)\s+(?:a\s+)?project\s+(?:called|named)\s+([\"']?[a-zA-Z0-9\s_-]+[\"']?)",
            user_message_text,
            re.IGNORECASE,
        )
        if create_project_match:
            project_name = create_project_match.group(1).strip().strip("'\"")
            # Create project
            new_proj = cls.create_project(
                db,
                student_id,
                AIProjectCreate(
                    name=project_name,
                    description=f"Created via voice/chat prompt: '{user_message_text}'",
                    icon="folder",
                ),
            )
            # Create first conversation in new project
            new_conv = cls.create_conversation(
                db,
                student_id,
                AIConversationCreate(project_id=new_proj.id, title=f"Initial Discussion - {project_name}"),
            )
            # Record user message
            user_msg = AIMessage(
                conversation_id=new_conv.id,
                sender_type="user",
                message_text=user_message_text,
                input_type=request.input_type,
            )
            db.add(user_msg)

            reply_text = (
                f"✅ I have successfully created the project **{project_name}** for you! "
                f"I've initialized its dedicated workspace and memory. All your future notes, architecture decisions, "
                f"and questions under this project will be saved here."
            )
            ai_msg = AIMessage(
                conversation_id=new_conv.id,
                sender_type="assistant",
                message_text=reply_text,
                input_type="text",
            )
            db.add(ai_msg)
            db.commit()

            return AIChatResponse(
                project_id=new_proj.id,
                project_name=new_proj.name,
                conversation_id=new_conv.id,
                conversation_title=new_conv.title,
                reply=reply_text,
                speech_text=f"I've created the project {project_name} for you! What would you like to build or discuss first?",
                search_sources=[],
                memory_summary=new_proj.name,
                acknowledgement=random.choice(VARIED_ACKNOWLEDGEMENTS) if request.spoken_acknowledgement_needed else None,
            )

        # Step B: Resolve Active Project & Conversation
        project = None
        if request.project_id:
            project = (
                db.query(AIProject)
                .filter(AIProject.id == request.project_id, AIProject.student_id == student_id)
                .first()
            )
        if not project:
            project = cls.get_or_create_default_project(db, student_id)

        conversation = None
        if request.conversation_id:
            conversation = (
                db.query(AIConversation)
                .filter(AIConversation.id == request.conversation_id, AIConversation.student_id == student_id)
                .first()
            )
        if not conversation:
            # Generate a title from the first message
            words = user_message_text.split()
            title = " ".join(words[:5]) + ("..." if len(words) > 5 else "")
            conversation = cls.create_conversation(
                db,
                student_id,
                AIConversationCreate(project_id=project.id, title=title),
            )

        # Step C: Save User Message
        user_msg = AIMessage(
            conversation_id=conversation.id,
            sender_type="user",
            message_text=user_message_text,
            input_type=request.input_type,
        )
        db.add(user_msg)
        db.commit()

        # Step D: Retrieve Project-Specific Memory & Prior History
        memory_record = db.query(AIProjectMemory).filter(AIProjectMemory.project_id == project.id).first()
        project_memory_summary = memory_record.memory_summary if memory_record else ""
        project_topics = memory_record.key_entities.get("topics", []) if memory_record and memory_record.key_entities else []

        # Retrieve last 10 messages from current conversation for multi-turn context
        past_messages = (
            db.query(AIMessage)
            .filter(AIMessage.conversation_id == conversation.id)
            .order_by(AIMessage.created_at)
            .all()
        )

        # Step E: Handle Memory Recall Queries (Scenario 2: "What did we learn last time?", "Continue my project")
        lower_q = user_message_text.lower()
        is_memory_query = any(phrase in lower_q for phrase in [
            "what topic did we learn", "what did we learn", "what did we discuss",
            "what were we working on", "continue my previous project", "continue my project",
            "where did we stop", "remind me what"
        ])

        # Step F: Educational Web Search Trigger
        # Auto-trigger if query mentions live info, dates, exams, or if student enabled search toggle
        needs_search = request.search_enabled or any(term in lower_q for term in [
            "latest", "update", "dates", "exam date", "notification", "admit card",
            "gate ece", "ssc cgl 2024", "ssc cgl 2025", "upsc 2025", "current affairs",
            "official link", "find the latest"
        ])

        search_sources = []
        if needs_search:
            try:
                search_sources = await WebSearchService.search(user_message_text, limit=4)
            except Exception as e:
                logger.warning("Live web search failed: %s", e)

        # Step G: Generate Answer
        reply_markdown, speech_text = await cls._generate_educational_response(
            project=project,
            conversation=conversation,
            user_query=user_message_text,
            project_memory=project_memory_summary,
            project_topics=project_topics,
            past_messages=past_messages,
            is_memory_query=is_memory_query,
            search_sources=search_sources,
            file_data=request.file_data,
            file_name=request.file_name,
            file_mime_type=request.file_mime_type,
        )

        # Step H: Save Assistant Message
        assistant_msg = AIMessage(
            conversation_id=conversation.id,
            sender_type="assistant",
            message_text=reply_markdown,
            input_type="text",
            search_sources=search_sources,
        )
        db.add(assistant_msg)
        conversation.updated_at = datetime.utcnow()
        project.updated_at = datetime.utcnow()
        db.commit()

        # Step I: Update Project Memory
        try:
            cls.update_project_memory(db, project.id, user_message_text, reply_markdown)
        except Exception as e:
            logger.warning("Could not update project memory: %s", e)

        acknowledgement = random.choice(VARIED_ACKNOWLEDGEMENTS) if request.spoken_acknowledgement_needed else None

        return AIChatResponse(
            project_id=project.id,
            project_name=project.name,
            conversation_id=conversation.id,
            conversation_title=conversation.title,
            reply=reply_markdown,
            speech_text=speech_text,
            search_sources=search_sources,
            memory_summary=project_memory_summary,
            acknowledgement=acknowledgement,
        )

    # -------------------------------------------------------------
    # 5. UNIVERSAL GEMINI AI & DOMAIN RESPONSE GENERATOR
    # -------------------------------------------------------------
    @classmethod
    async def _generate_educational_response(
        cls,
        project: AIProject,
        conversation: AIConversation,
        user_query: str,
        project_memory: str,
        project_topics: List[str],
        past_messages: List[AIMessage],
        is_memory_query: bool,
        search_sources: List[Dict[str, Any]],
        file_data: Optional[str] = None,
        file_name: Optional[str] = None,
        file_mime_type: Optional[str] = None,
    ) -> Tuple[str, str]:
        """
        Universal Gemini-Powered Response Generator.
        Acts like ChatGPT / Google Gemini across all domains without restrictions:
        - Programming (Python, C, C++, Java, JS, HTML/CSS, React, Node, SQL, etc.)
        - Computer Science & DSA
        - Engineering (ECE, Mechanical, Civil, Electrical, VLSI, Robotics)
        - Mathematics, Physics, Chemistry, Biology
        - General Knowledge, Indian & World History, Polity, Economics
        - Competitive Examinations (UPSC, SSC, GATE, Banking, Police)
        - Career, Resumes, Interview Prep
        - Everyday Assistance, Writing, Problem Solving, and Novel Questions
        - Multimodal Image & Document Analysis
        """
        lower_q = user_query.lower()

        # 1. SPECIAL CASE: Project Memory Recall
        if is_memory_query:
            if project_topics or project_memory:
                topics_str = ", ".join(project_topics) if project_topics else "various core concepts"
                reply = (
                    f"### 🧠 Memory Log for **{project.name}**\n\n"
                    f"Last time in this project, we worked on:\n"
                    f"{project_memory}\n\n"
                    f"**Key Topics Covered So Far:**\n"
                    + "\n".join([f"- {t}" for t in project_topics[:8]])
                    + f"\n\nWould you like to continue building on this or dive into practice questions?"
                )
                speech = (
                    f"In your {project.name} project, we previously worked on {topics_str}. "
                    f"Shall we continue from where we left off, or would you like to review?"
                )
                return reply, speech
            else:
                reply = (
                    f"This is a fresh conversation in **{project.name}**. "
                    f"We haven't recorded prior topics yet. What would you like to start with today?"
                )
                speech = f"This is a new project conversation. What topic shall we begin with?"
                return reply, speech

        # 2. SPECIAL CASE: Web Search Results Grounding
        if search_sources:
            citations_md = "\n".join(
                [f"- **[{s['title']}]({s['url']})** ({s.get('source', 'Official Source')}): {s['snippet']}" for s in search_sources]
            )
            # Try primary Gemini LLM with search grounding first
            if GeminiService.is_configured():
                search_query = (
                    f"User Query: {user_query}\n\n"
                    f"Use these verified live search results to answer accurately:\n{citations_md}"
                )
                gemini_search_ans = GeminiService.generate_chat_response(
                    user_query=search_query,
                    past_messages=past_messages,
                    project_name=project.name,
                    project_memory=project_memory,
                    project_description=project.description or "",
                    file_data=file_data,
                    file_name=file_name,
                    file_mime_type=file_mime_type,
                )
                if gemini_search_ans:
                    return gemini_search_ans

            # Structured fallback with citations
            top_res = search_sources[0]
            reply = (
                f"### 🌐 Latest Verified Information\n\n"
                f"Based on official portals and latest notifications for **{user_query}**:\n\n"
                f"**Key Findings:**\n"
                f"- **{top_res['title']}**: {top_res['snippet']}\n\n"
                f"**Official Sources & Citations:**\n"
                f"{citations_md}\n\n"
                f"> [!NOTE]\n"
                f"> SkillExa cross-checks recruitment and academic schedules with official commission releases."
            )
            speech = (
                f"I found the latest updates for {user_query}. "
                f"According to {top_res.get('source', 'the official portal')}, {top_res['snippet'][:120]}. "
                f"I've linked the verified sources on your screen."
            )
            return reply, speech

        # 3. PRIMARY UNIVERSAL INTELLIGENCE: Google Gemini Flash (Official google-genai SDK)
        if GeminiService.is_configured():
            gemini_ans = GeminiService.generate_chat_response(
                user_query=user_query,
                past_messages=past_messages,
                project_name=project.name,
                project_memory=project_memory,
                project_description=project.description or "",
                file_data=file_data,
                file_name=file_name,
                file_mime_type=file_mime_type,
            )
            if gemini_ans:
                return gemini_ans

        # 4. SECONDARY ACADEMIC ENGINE (Direct topic definitions if Gemini is offline)
        academic_ans = AcademicKnowledgeEngine.answer(user_query, past_messages, project.name)
        if academic_ans:
            return academic_ans

        # 5. DIAGNOSTIC NOTICE: If Gemini API key is missing
        if not GeminiService.is_configured():
            reply = (
                f"### ⚙️ Gemini AI Configuration Notice\n\n"
                f"The Google Gemini API key is not configured on the SkillExa backend.\n\n"
                f"To enable dynamic AI responses for all user queries, ensure **`GEMINI_API_KEY`** is added to your environment variables on Render.\n\n"
                f"Currently, core curriculum topics like **CSS**, **HTML**, **Python**, **C**, **Java**, **DSA**, **Stacks**, **Pointers**, and **Aptitude** are available via the offline academic engine."
            )
            speech = "Please configure the Gemini API key in the backend environment variables to enable dynamic AI responses."
            return reply, speech

        # 6. POLITE NOTICE: Rate limit or temporary connection timeout
        clean_target = user_query.strip().strip("?.,!")
        reply = (
            f"### ⏳ SkillExa AI Temporary Notice\n\n"
            f"I was unable to complete the response for **{clean_target}** due to a temporary AI provider rate limit or network timeout.\n\n"
            f"Please wait a few seconds and try your question again."
        )
        speech = f"SkillExa AI is temporarily busy. Please try asking your question again in a moment."
        return reply, speech
