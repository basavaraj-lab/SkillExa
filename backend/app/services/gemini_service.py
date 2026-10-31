import base64
import logging
import os
import re
import socket
import time
from typing import Any, Dict, List, Optional, Tuple

# Prioritize IPv4 DNS resolution on macOS to prevent IPv6 connection packet drops/timeouts
try:
    _orig_getaddrinfo = socket.getaddrinfo

    def _getaddrinfo_ipv4(host, port, family=0, type=0, proto=0, flags=0):
        try:
            res = _orig_getaddrinfo(host, port, family, type, proto, flags)
            ipv4_res = [r for r in res if r[0] == socket.AF_INET]
            return ipv4_res if ipv4_res else res
        except Exception:
            return _orig_getaddrinfo(host, port, family, type, proto, flags)

    socket.getaddrinfo = _getaddrinfo_ipv4
except Exception:
    pass

try:
    from google import genai
    from google.genai import types
    from google.genai import errors
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False
    genai = None
    types = None
    errors = None

from backend.app.config import settings

logger = logging.getLogger("skillexa.gemini_service")


def clean_for_speech(text: str) -> str:
    """
    Transforms markdown and code response into concise, natural, spoken conversational text.
    Eliminates code blocks, headers, bullets, and URLs so the Web Speech API/TTS
    sounds like a friendly, clear human tutor.
    """
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
    # Remove alert tags like > [!NOTE]
    cleaned = re.sub(r">\s*\[![A-Z]+\]", "", cleaned)
    cleaned = re.sub(r"^>\s*", "", cleaned, flags=re.MULTILINE)
    # Condense whitespace
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    # Limit to first 2-3 sentences for spoken output if it's too long
    sentences = re.split(r"(?<=[.!?])\s+", cleaned)
    if len(sentences) > 3:
        return " ".join(sentences[:3]) + " I've provided the complete code and detailed breakdown on your screen."
    return cleaned


def build_system_instruction(
    project_name: str = "General Chats",
    project_memory: str = "",
    project_description: str = "",
) -> str:
    """
    Constructs the universal ChatGPT/Gemini-style system instruction for SkillExa AI.
    Allows answering ANY reasonable question across all domains without restriction.
    """
    memory_section = f"\nWORKSPACE CONTEXT & MEMORY FOR PROJECT '{project_name}':\n{project_memory}\n" if project_memory else ""
    desc_section = f"Project Description: {project_description}\n" if project_description else ""

    return (
        "You are SkillExa AI, an intelligent, universal conversational AI assistant and personal mentor powered by Google Gemini, similar in breadth and capability to ChatGPT and Google Gemini.\n\n"
        "Your mission is to understand and accurately answer ANY reasonable question or prompt asked by the user, across all subjects and domains without restriction.\n\n"
        "Core Capabilities & Domains:\n"
        "1. Programming & Technology: Python, C, C++, Java, JavaScript, TypeScript, HTML, CSS, React, React Native, Node.js, FastAPI, SQL, Databases, AI, ML, Data Science, Cloud, Cybersecurity, Git, APIs.\n"
        "2. Computer Science: Data Structures and Algorithms (Arrays, Linked Lists, Trees, Graphs, Stacks, Queues, DP), OS, Networks, DBMS, System Design, Compilers, Architecture.\n"
        "3. Engineering: Electronics & Communication (ECE), Electrical, Mechanical, Civil, VLSI, Microprocessors (8085/8086), Digital & Analog Electronics, DSP, Signals, IoT, Robotics.\n"
        "4. Mathematics & Sciences: Calculus, Linear Algebra, Probability, Statistics, Physics, Chemistry, Biology, Logic.\n"
        "5. General Knowledge & Current Affairs: Indian & World History, Geography, Indian Constitution & Polity, Economics, Important Personalities, Sports, Science.\n"
        "6. Competitive Exams: SSC, UPSC, IBPS, KPSC, Police, Railway, GATE, Quantitative & Logical Aptitude.\n"
        "7. Career & Everyday Life: Resume drafting, Technical/HR interview preparation, Email drafting, Creative writing, Business ideas, Travel, Personal productivity, Problem solving, and any novel question.\n\n"
        "Response Guidelines:\n"
        "- Give direct, clear, helpful, and beginner-friendly answers based exactly on the user's intent.\n"
        "- If the user asks for code, provide clean, complete, working, and commented code blocks.\n"
        "- If the user asks to explain or debug code, explain step-by-step and provide the corrected version.\n"
        "- If the user asks for a comparison, format it clearly using Markdown tables.\n"
        "- If the user attaches an image, screenshot, or document, thoroughly analyze its visual or textual contents and answer their specific question.\n"
        "- Format responses using clean GitHub-style Markdown: headings, bullet points, and syntax-highlighted code fences.\n"
        "- Avoid unnecessary fluff, boilerplate apologies, or refusing questions within educational or general domain scope.\n"
        f"Active Workspace Context: {project_name}\n"
        f"{desc_section}"
        f"{memory_section}"
    )


class GeminiService:
    """
    Production-grade Google Gemini LLM Service powered by the official google-genai SDK.
    Features:
    - Primary universal intelligence for SkillExa AI Assistant (text, voice & multimodal).
    - Multi-turn conversation history grounding.
    - Automatic multi-key failover and quota resilience.
    - Automatic fallback across models (gemini-flash-lite-latest -> gemini-2.5-flash-lite -> gemini-2.5-flash -> gemini-2.0-flash -> gemini-flash-latest).
    - Image and document understanding (PNG, JPEG, PDF, Code, Text).
    - Safe credential handling (zero raw API key logging).
    """

    SUPPORTED_MODELS = [
        "gemini-flash-lite-latest",
        "gemini-2.5-flash-lite",
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-flash-latest",
    ]

    @classmethod
    def get_api_keys(cls) -> List[str]:
        """
        Safely retrieves available Gemini API keys from environment variables.
        Supports comma-separated keys for automatic failover.
        Never hardcodes secret credentials.
        """
        keys: List[str] = []
        env_val = (
            os.getenv("GEMINI_API_KEY")
            or getattr(settings, "GEMINI_API_KEY", "")
            or os.getenv("GOOGLE_API_KEY", "")
        )
        if env_val:
            for k in str(env_val).split(","):
                k = k.strip()
                if k and k not in keys:
                    keys.append(k)
        return keys

    @classmethod
    def get_api_key(cls) -> str:
        keys = cls.get_api_keys()
        return keys[0] if keys else ""

    @classmethod
    def is_configured(cls) -> bool:
        """Checks if the official SDK is installed and at least one API key is provided."""
        return bool(GENAI_AVAILABLE and cls.get_api_keys())

    @classmethod
    def get_model_name(cls) -> str:
        """Resolves the configured Gemini Flash model."""
        model = os.getenv("GEMINI_MODEL") or getattr(settings, "GEMINI_MODEL", "") or "gemini-flash-lite-latest"
        return model.strip()

    @classmethod
    def _create_client(cls, api_key: Optional[str] = None) -> Optional[Any]:
        """Initializes the official google-genai Client."""
        if not GENAI_AVAILABLE:
            logger.warning("google-genai SDK is not installed in the python environment.")
            return None

        key_to_use = api_key or cls.get_api_key()
        if not key_to_use:
            return None

        try:
            return genai.Client(
                api_key=key_to_use,
                http_options=types.HttpOptions(
                    api_version="v1beta",
                    timeout=10000,
                ),
            )
        except Exception as e:
            logger.error("Failed to initialize google-genai Client: %s", type(e).__name__)
            return None

    @classmethod
    def generate_chat_response(
        cls,
        user_query: str,
        past_messages: Optional[List[Any]] = None,
        project_name: str = "General Chats",
        project_memory: str = "",
        project_description: str = "",
        file_data: Optional[str] = None,
        file_mime_type: Optional[str] = None,
        file_name: Optional[str] = None,
        temperature: float = 0.5,
        max_output_tokens: int = 2048,
    ) -> Optional[Tuple[str, str]]:
        """
        Generates a comprehensive universal response using Google Gemini.
        Supports multimodal image and document inputs.
        Returns:
            Tuple[str, str]: (reply_markdown, speech_text)
            or None if all candidate keys and models fail.
        """
        if not cls.is_configured():
            logger.info("Gemini API key is not configured; deferring to academic knowledge engine.")
            return None

        # Build system instruction
        system_instruction = build_system_instruction(
            project_name=project_name,
            project_memory=project_memory,
            project_description=project_description,
        )

        # Build multi-turn contents list
        contents: List[types.Content] = []

        if past_messages:
            # Include up to the last 8 messages for relevant conversation context
            recent = past_messages[-8:]
            for msg in recent:
                sender = getattr(msg, "sender_type", "")
                text = getattr(msg, "message_text", "")
                if not text or not text.strip():
                    continue

                if sender == "user":
                    contents.append(
                        types.Content(
                            role="user",
                            parts=[types.Part.from_text(text=text.strip())],
                        )
                    )
                elif sender == "assistant":
                    truncated_reply = text[:1500]
                    contents.append(
                        types.Content(
                            role="model",
                            parts=[types.Part.from_text(text=truncated_reply)],
                        )
                    )

        # Build parts for current user query
        user_parts: List[types.Part] = []

        # Process attached file / image if provided
        if file_data and file_data.strip():
            raw_b64 = file_data.strip()
            mime = file_mime_type

            # Strip data URL prefix if present (e.g. data:image/png;base64,...)
            if "," in raw_b64 and "base64" in raw_b64[:60]:
                header, raw_b64 = raw_b64.split(",", 1)
                if not mime and ":" in header and ";" in header:
                    mime = header.split(":", 1)[1].split(";", 1)[0]

            try:
                file_bytes = base64.b64decode(raw_b64)
                if len(file_bytes) > 15 * 1024 * 1024:
                    logger.warning("Uploaded file exceeds 15MB size limit.")
                else:
                    if not mime:
                        mime = "image/jpeg"
                    if file_name and (not file_mime_type or file_mime_type == "application/octet-stream"):
                        ext = file_name.lower().split(".")[-1]
                        mime_map = {
                            "png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
                            "webp": "image/webp", "pdf": "application/pdf",
                            "py": "text/plain", "js": "text/plain", "ts": "text/plain",
                            "java": "text/plain", "c": "text/plain", "cpp": "text/plain",
                            "html": "text/html", "css": "text/css", "json": "application/json",
                            "txt": "text/plain", "csv": "text/plain"
                        }
                        mime = mime_map.get(ext, mime)

                    user_parts.append(types.Part.from_bytes(data=file_bytes, mime_type=mime))
                    logger.info("Successfully attached %s (%s, %d bytes) to Gemini payload", file_name or "file", mime, len(file_bytes))
            except Exception as e:
                logger.warning("Could not decode attachment base64: %s", e)

        # Add text prompt
        user_parts.append(types.Part.from_text(text=user_query.strip()))

        contents.append(
            types.Content(
                role="user",
                parts=user_parts,
            )
        )

        config = types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )

        primary_model = cls.get_model_name()
        candidate_models = [primary_model] + [m for m in cls.SUPPORTED_MODELS if m != primary_model]
        api_keys = cls.get_api_keys()

        for api_key in api_keys:
            client = cls._create_client(api_key=api_key)
            if not client:
                continue

            for model_to_try in candidate_models:
                try:
                    start_time = time.time()
                    response = client.models.generate_content(
                        model=model_to_try,
                        contents=contents,
                        config=config,
                    )
                    latency = round((time.time() - start_time) * 1000, 1)

                    if response and response.text:
                        reply_text = response.text.strip()
                        spoken_text = clean_for_speech(reply_text)
                        logger.info("Gemini response generated via %s (key ...%s) in %sms", model_to_try, api_key[-4:], latency)
                        return reply_text, spoken_text

                except errors.APIError as api_err:
                    error_code = getattr(api_err, "code", "UNKNOWN")
                    # If 401/403 or PERMISSION_DENIED on this key, break to try the next API key
                    if error_code in (401, 403, "PERMISSION_DENIED"):
                        logger.warning("Gemini key permission denied (%s), trying next key", error_code)
                        break
                    # If 429 rate limit or 404/503/504 on this model, try next candidate model
                    continue
                except Exception as e:
                    logger.warning("Gemini generation error on model %s: %s", model_to_try, type(e).__name__)
                    continue

        logger.warning("All Gemini candidate models and keys exhausted; falling back to secondary academic engine.")
        return None

    @classmethod
    def test_connection(cls, test_prompt: str = "Explain Python in 15 words.") -> Dict[str, Any]:
        """
        Diagnostic method to test live connection to Google Gemini API.
        Never reveals or prints secret keys.
        """
        api_key = cls.get_api_key()
        if not api_key:
            return {
                "success": False,
                "configured": False,
                "error": "GEMINI_API_KEY is not set in backend/.env",
            }

        if not GENAI_AVAILABLE:
            return {
                "success": False,
                "configured": True,
                "error": "google-genai SDK package is not installed",
            }

        client = cls._create_client()
        if not client:
            return {
                "success": False,
                "configured": True,
                "error": "Failed to create google-genai Client instance",
            }

        primary_model = cls.get_model_name()
        candidate_models = [primary_model] + [m for m in cls.SUPPORTED_MODELS if m != primary_model]
        last_error = None

        for model_to_try in candidate_models:
            start = time.time()
            try:
                res = client.models.generate_content(
                    model=model_to_try,
                    contents=test_prompt,
                    config=types.GenerateContentConfig(
                        max_output_tokens=100,
                        temperature=0.2,
                    ),
                )
                duration_ms = round((time.time() - start) * 1000, 1)

                if res and res.text:
                    return {
                        "success": True,
                        "configured": True,
                        "model": model_to_try,
                        "latency_ms": duration_ms,
                        "reply_preview": res.text.strip()[:200],
                    }
            except errors.APIError as e:
                error_code = getattr(e, "code", "API_ERROR")
                last_error = {
                    "success": False,
                    "configured": True,
                    "model": model_to_try,
                    "error_code": error_code,
                    "error_message": getattr(e, "message", str(e))[:200],
                }
                if error_code in (404, "NOT_FOUND", 503, "UNAVAILABLE", 429, "RESOURCE_EXHAUSTED", 504, "DEADLINE_EXCEEDED"):
                    continue
                return last_error
            except Exception as e:
                last_error = {
                    "success": False,
                    "configured": True,
                    "model": model_to_try,
                    "error": f"{type(e).__name__}: {str(e)[:200]}",
                }
                continue

        return last_error or {
            "success": False,
            "configured": True,
            "model": primary_model,
            "error": "All candidate Gemini models failed to generate content.",
        }

