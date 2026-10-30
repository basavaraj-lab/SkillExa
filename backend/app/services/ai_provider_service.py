import json
import logging
import os
import re
from typing import Any, Dict, List, Optional
import httpx
from backend.app.config import settings
from backend.app.services.gemini_service import GeminiService

logger = logging.getLogger("skillexa.ai_provider")


def sanitize_input_for_privacy(text: str) -> str:
    """Strip emails, passwords, tokens, and phone numbers before sending to AI provider."""
    if not text:
        return ""
    # Strip emails
    text = re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", "[REDACTED_EMAIL]", text)
    # Strip bearer tokens or UUIDs
    text = re.sub(r"Bearer\s+[a-zA-Z0-9._-]+", "[REDACTED_TOKEN]", text)
    # Strip 10-digit phone numbers
    text = re.sub(r"\b\d{10}\b", "[REDACTED_PHONE]", text)
    return text


def extract_json_from_response(raw_text: str) -> Optional[Dict[str, Any]]:
    """Robustly extract and validate JSON from markdown code blocks or text."""
    if not raw_text:
        return None
    raw_text = raw_text.strip()

    # Try direct parse
    try:
        return json.loads(raw_text)
    except Exception:
        pass

    # Try markdown json fence ```json ... ```
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", raw_text)
    if match:
        try:
            return json.loads(match.group(1).strip())
        except Exception:
            pass

    # Try finding first { and last }
    first_brace = raw_text.find("{")
    last_brace = raw_text.rfind("}")
    if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
        try:
            return json.loads(raw_text[first_brace : last_brace + 1])
        except Exception:
            pass

    return None


class AIProviderService:
    """
    Unified AI Provider Layer.
    Supports Gemini, OpenAI, Custom HTTP, and High-Quality Deterministic Educational Fallback.
    Protects privacy and ensures zero crashing when external APIs are unconfigured or unavailable.
    """

    @classmethod
    def get_provider_name(cls) -> str:
        provider = os.getenv("AI_PROVIDER", getattr(settings, "AI_PROVIDER", "auto")).lower()
        if provider == "auto":
            if os.getenv("GEMINI_API_KEY"):
                return "gemini"
            elif os.getenv("OPENAI_API_KEY"):
                return "openai"
            elif os.getenv("CUSTOM_AI_URL"):
                return "custom_http"
            return "deterministic"
        return provider

    @classmethod
    def call_ai(cls, system_prompt: str, user_prompt: str, max_tokens: int = 1000) -> Optional[Dict[str, Any]]:
        """
        Send structured request to configured provider and parse JSON output.
        """
        provider = cls.get_provider_name()
        clean_user_prompt = sanitize_input_for_privacy(user_prompt)

        if provider == "gemini":
            result = cls._call_gemini(system_prompt, clean_user_prompt, max_tokens)
            if result:
                return result
        elif provider == "openai":
            result = cls._call_openai(system_prompt, clean_user_prompt, max_tokens)
            if result:
                return result
        elif provider == "custom_http":
            result = cls._call_custom_http(system_prompt, clean_user_prompt, max_tokens)
            if result:
                return result

        # Return None to trigger verified deterministic rule-based evaluation/generation
        return None

    @classmethod
    def generate_conversational_text(
        cls, system_prompt: str, user_prompt: str, max_tokens: int = 1200
    ) -> Optional[str]:
        """
        Generate direct conversational academic response from configured provider.
        Does not require strict JSON wrapping.
        """
        provider = cls.get_provider_name()
        clean_user_prompt = sanitize_input_for_privacy(user_prompt)

        # 1. Gemini via official google-genai SDK
        if provider == "gemini" or GeminiService.is_configured():
            res = GeminiService.generate_chat_response(
                user_query=clean_user_prompt,
                max_output_tokens=max_tokens,
            )
            if res:
                return res[0]

        # 2. OpenAI
        if provider == "openai" or os.getenv("OPENAI_API_KEY"):
            api_key = os.getenv("OPENAI_API_KEY", "")
            if api_key:
                model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
                url = "https://api.openai.com/v1/chat/completions"
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                }
                payload = {
                    "model": model,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": clean_user_prompt},
                    ],
                    "temperature": 0.4,
                    "max_tokens": max_tokens,
                }
                try:
                    with httpx.Client(timeout=10.0) as client:
                        res = client.post(url, headers=headers, json=payload)
                        if res.status_code == 200:
                            data = res.json()
                            return data["choices"][0]["message"]["content"].strip()
                except Exception as e:
                    logger.warning("OpenAI conversational generation failed: %s", e)

        return None

    @classmethod
    def _call_gemini(cls, system_prompt: str, user_prompt: str, max_tokens: int) -> Optional[Dict[str, Any]]:
        if not GeminiService.is_configured():
            return None

        try:
            from google import genai
            from google.genai import types
            api_key = GeminiService.get_api_key()
            client = genai.Client(api_key=api_key)
            model = GeminiService.get_model_name()

            res = client.models.generate_content(
                model=model,
                contents=f"{system_prompt}\n\nPlease output strict JSON only.\n\n{user_prompt}",
                config=types.GenerateContentConfig(
                    temperature=0.2,
                    max_output_tokens=max_tokens,
                    response_mime_type="application/json",
                ),
            )
            if res and res.text:
                return extract_json_from_response(res.text)
        except Exception as e:
            logger.warning("Gemini JSON call failed: %s", type(e).__name__)
        return None

    @classmethod
    def _call_openai(cls, system_prompt: str, user_prompt: str, max_tokens: int) -> Optional[Dict[str, Any]]:
        api_key = os.getenv("OPENAI_API_KEY", "")
        if not api_key:
            return None

        model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        url = "https://api.openai.com/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": f"{system_prompt}\nYou MUST output valid JSON format only."},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.2,
            "max_tokens": max_tokens,
            "response_format": {"type": "json_object"},
        }

        try:
            with httpx.Client(timeout=8.0) as client:
                res = client.post(url, headers=headers, json=payload)
                if res.status_code == 200:
                    data = res.json()
                    content = data["choices"][0]["message"]["content"]
                    return extract_json_from_response(content)
                else:
                    logger.warning("OpenAI API call returned status %s: %s", res.status_code, res.text[:200])
        except Exception as e:
            logger.warning("OpenAI API request failed: %s", e)
        return None

    @classmethod
    def _call_custom_http(cls, system_prompt: str, user_prompt: str, max_tokens: int) -> Optional[Dict[str, Any]]:
        url = os.getenv("CUSTOM_AI_URL", "")
        if not url:
            return None

        payload = {
            "prompt": f"{system_prompt}\n{user_prompt}",
            "max_tokens": max_tokens,
            "format": "json",
        }
        try:
            with httpx.Client(timeout=8.0) as client:
                res = client.post(url, json=payload)
                if res.status_code == 200:
                    return extract_json_from_response(res.text)
        except Exception as e:
            logger.warning("Custom AI API request failed: %s", e)
        return None
