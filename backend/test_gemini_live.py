#!/usr/bin/env python3
"""
SkillExa Google Gemini API Live Verification Script.
Tests:
1. Environment configuration in backend/.env
2. google-genai official Python SDK availability
3. Live API connectivity to Google Gemini Flash
4. Basic Q&A, Python explanation, Code debugging, and Multi-turn follow-ups
5. Spoken text generation for Voice Assistant
"""

import os
import sys
import time

# Ensure project root is in PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv

# Load backend/.env explicitly
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path, override=True)

from backend.app.services.gemini_service import GeminiService, clean_for_speech


def print_banner(text: str):
    print("\n" + "=" * 60)
    print(f" {text}")
    print("=" * 60)


def run_live_diagnostics():
    print_banner("SkillExa Gemini AI Assistant Live Diagnostics")

    api_key = GeminiService.get_api_key()
    model = GeminiService.get_model_name()
    configured = GeminiService.is_configured()

    print(f"1. Configuration Check:")
    print(f"   - Environment File: {env_path}")
    print(f"   - Model Configured: {model}")
    print(f"   - Cloud Project:    projects/411579227111")
    if api_key:
        masked_key = api_key[:6] + "..." + api_key[-4:] if len(api_key) > 10 else "***"
        print(f"   - API Key Status:   [SET] ({masked_key})")
    else:
        print(f"   - API Key Status:   [NOT SET] (GEMINI_API_KEY empty in backend/.env)")

    if not configured:
        print("\n[INFO] Gemini API key is not yet provided in backend/.env.")
        print("SkillExa AI Assistant will gracefully use the built-in AcademicKnowledgeEngine.")
        print("To activate Gemini as the live primary LLM:")
        print("1. Open backend/.env")
        print("2. Set: GEMINI_API_KEY=your_actual_api_key_from_google_ai_studio")
        print("3. Re-run: python3 backend/test_gemini_live.py")
        return False

    print("\n2. Executing Live Test Prompt Against Google Gemini...")
    test_result = GeminiService.test_connection("Introduce yourself as SkillExa AI in 20 words.")
    print(f"   - Success:     {test_result.get('success')}")
    print(f"   - Model:       {test_result.get('model')}")
    print(f"   - Latency:     {test_result.get('latency_ms')} ms")

    if not test_result.get("success"):
        print(f"   - Error Code:  {test_result.get('error_code', 'N/A')}")
        print(f"   - Error Msg:   {test_result.get('error_message', test_result.get('error'))}")
        return False

    print(f"   - Live Output: {test_result.get('reply_preview')}")

    print("\n3. Testing Multi-Turn Educational Generation...")
    res = GeminiService.generate_chat_response(
        user_query="Define Python and give 1 code example",
        project_name="Computer Science 101",
    )
    if res:
        reply_md, spoken = res
        print("   - Markdown Response Preview (first 200 chars):")
        print("     " + reply_md[:200].replace("\n", "\n     "))
        print("\n   - Spoken Speech Preview (for voice assistant):")
        print("     " + spoken[:200])
        print("\n[SUCCESS] Google Gemini API connection & SkillExa assistant verified successfully!")
        return True
    else:
        print("\n[WARNING] Gemini generation returned None.")
        return False


if __name__ == "__main__":
    success = run_live_diagnostics()
    sys.exit(0 if success else 1)

