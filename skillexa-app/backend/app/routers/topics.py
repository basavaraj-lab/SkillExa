from collections import defaultdict
from typing import Any, Dict, List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from backend.app.schemas.common import ApiResponse

router = APIRouter(prefix="/topics", tags=["Language Learning Topics & Curriculum"])

# Per-language topic unlock & completion state tracking
UNLOCKED_TOPICS: Dict[str, set] = defaultdict(lambda: {1})
COMPLETED_TOPICS: Dict[str, set] = defaultdict(set)


def get_language_catalog(language: str):
    lang = (language or "python").lower()
    if lang in ["c"]:
        from backend.app.models.c_topic_catalog import C_TOPIC_CATALOG, C_TOPIC_CORE
        return C_TOPIC_CATALOG, C_TOPIC_CORE, "C Programming Track"
    elif lang in ["cpp", "c++"]:
        from backend.app.models.cpp_topic_catalog import CPP_TOPIC_CATALOG
        import backend.app.models.cpp_topic_catalog as cpp_mod
        cpp_core = getattr(cpp_mod, "CPP_TOPIC_CORE", {})
        return CPP_TOPIC_CATALOG, cpp_core, "C++ Programming Track"
    elif lang in ["java"]:
        from backend.app.models.java_topic_catalog import JAVA_TOPIC_CATALOG
        import backend.app.models.java_topic_catalog as java_mod
        java_core = getattr(java_mod, "JAVA_TOPIC_CORE", {})
        return JAVA_TOPIC_CATALOG, java_core, "Java Track"
    elif lang in ["js", "javascript"]:
        from backend.app.models.js_topic_catalog import JS_TOPIC_CATALOG
        import backend.app.models.js_topic_catalog as js_mod
        js_core = getattr(js_mod, "JS_TOPIC_CORE", {})
        return JS_TOPIC_CATALOG, js_core, "JavaScript Track"
    else:
        from backend.app.models.topic_catalog import TOPIC_CATALOG, TOPIC_CORE
        return TOPIC_CATALOG, TOPIC_CORE, "Python Track"


@router.get("", response_model=ApiResponse[Dict[str, Any]])
def get_language_topics(
    language: str = Query("python", description="Language track: 'python', 'c', 'cpp', 'java', 'js'"),
):
    """
    Returns full topic catalog list for requested programming language track.
    """
    catalog, _, track_title = get_language_catalog(language)
    lang_key = (language or "python").lower()

    unlocked = UNLOCKED_TOPICS[lang_key]
    completed = COMPLETED_TOPICS[lang_key]

    topics_list = []
    for t in catalog:
        t_id = t["id"]
        is_comp = t_id in completed
        is_unl = t_id in unlocked or is_comp or t_id == 1

        if is_comp:
            t_status = "COMPLETED"
            comp_pct = 100
        elif is_unl:
            t_status = "IN_PROGRESS"
            comp_pct = 0
        else:
            t_status = "LOCKED"
            comp_pct = 0

        topics_list.append({
            "id": t_id,
            "title": t["title"],
            "difficulty": t.get("difficulty", "Beginner"),
            "duration": t.get("duration", "20 min"),
            "category": t.get("category", f"{language.title()} Fundamentals"),
            "status": t_status,
            "completeness": comp_pct,
            "is_unlocked": is_unl,
        })

    category_name = f"{track_title} ({len(topics_list)} Topics)"

    return ApiResponse(
        success=True,
        message=f"Retrieved {len(topics_list)} topics for {language.upper()} track.",
        data={
            "language": language,
            "category_name": category_name,
            "total_topics": len(topics_list),
            "topics": topics_list,
        },
    )


@router.post("/{topic_id}/complete", response_model=ApiResponse[Dict[str, Any]])
def complete_topic(
    topic_id: int,
    language: str = Query("python", description="Language track: 'python', 'c', 'cpp', 'java', 'js'"),
    score: int = Query(100, description="Test score percentage achieved"),
):
    """
    Marks topic_id as COMPLETED and unlocks topic_id + 1 for requested language track.
    """
    if score >= 50:
        lang_key = (language or "python").lower()
        catalog, _, _ = get_language_catalog(lang_key)

        COMPLETED_TOPICS[lang_key].add(topic_id)
        next_topic_id = topic_id + 1
        UNLOCKED_TOPICS[lang_key].add(next_topic_id)

        next_topic = next((t for t in catalog if t["id"] == next_topic_id), None)
        next_title = next_topic["title"] if next_topic else f"Topic {next_topic_id}"

        return ApiResponse(
            success=True,
            message=f"Topic {topic_id} completed! Topic {next_topic_id} ({next_title}) is now unlocked.",
            data={
                "language": language,
                "completed_topic_id": topic_id,
                "unlocked_topic_id": next_topic_id,
                "next_topic_title": next_title,
                "score": score,
            },
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Score must be at least 50% to complete topic.",
        )


@router.get("/{topic_id}/details", response_model=ApiResponse[Dict[str, Any]])
def get_topic_details(
    topic_id: int,
    language: str = Query("python", description="Language track: 'python', 'c', 'cpp', 'java', 'js'"),
):
    """
    Returns 5-step learning flow content for requested language and topic.
    """
    catalog, core_dict, _ = get_language_catalog(language)
    lang_key = (language or "python").lower()

    raw_topic = next((t for t in catalog if t["id"] == topic_id), None)
    if not raw_topic:
        raw_topic = {
            "id": topic_id,
            "title": f"Topic {topic_id}",
            "difficulty": "Beginner",
            "duration": "20 min",
            "category": f"{language.title()} Fundamentals",
        }

    core = core_dict.get(topic_id, {})

    # Default syntax per language
    default_syntax_map = {
        "python": '# Hello World in Python\nprint("Hello, World!")',
        "c": '#include <stdio.h>\n\nint main(void) {\n    printf("Hello, World!\\n");\n    return 0;\n}',
        "cpp": '#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << "Hello, World!" << endl;\n    return 0;\n}',
        "java": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
        "js": '// Hello World in JavaScript\nconsole.log("Hello, World!");',
    }

    syntax_code = core.get("syntax") or default_syntax_map.get(lang_key, default_syntax_map["python"])
    concept_text = core.get("concept") or f"Learn {raw_topic['title']} in {language.upper()}."

    raw_example = core.get("example") if isinstance(core.get("example"), dict) else {}
    ex_code = raw_example.get("code") or syntax_code
    ex_output = raw_example.get("output") or "Hello, World!"
    raw_exp = raw_example.get("explanation")
    if isinstance(raw_exp, str):
        if "\n" in raw_exp:
            exp_list = [line.strip() for line in raw_exp.split("\n") if line.strip()]
        else:
            exp_list = [raw_exp.strip()]
    elif isinstance(raw_exp, list):
        exp_list = [str(x) for x in raw_exp]
    else:
        exp_list = [f"1. Demonstrates key principles of {raw_topic['title']} in {language.upper()}."]

    example_data = {
        "code": ex_code,
        "output": ex_output,
        "explanation": exp_list,
    }

    def _clean_code(val: Any) -> Any:
        if isinstance(val, str):
            return val.replace(r"\(", "(").replace(r"\)", ")")
        return val

    compiler_data = core.get("compiler") or {}
    prog_options_map = {
        "python": ["print", "input", "echo", "printf"],
        "c": ["printf", "scanf", "main", "include"],
        "cpp": ["cout", "cin", "endl", "main"],
        "java": ["System.out.println", "Scanner", "public", "class"],
        "js": ["console.log", "let", "const", "function"],
    }
    programming_task = {
        "title": compiler_data.get("title") or f"{raw_topic['title']} Sandbox",
        "question": compiler_data.get("question") or f"Write a program in {language.upper()} demonstrating {raw_topic['title']}.",
        "starter_code": _clean_code(compiler_data.get("starter_code") or syntax_code),
        "options": compiler_data.get("options") or prog_options_map.get(lang_key, prog_options_map["python"]),
        "answer": compiler_data.get("answer") or (compiler_data.get("options", [None])[0]),
    }

    fill_blanks_data = core.get("fill_blanks") or {}
    fill_blanks = {
        "question": _clean_code(fill_blanks_data.get("question") or f"// Complete {raw_topic['title']} snippet\n_____(\"Hello, World!\")\n"),
        "answers": fill_blanks_data.get("answers") or [prog_options_map.get(lang_key, ["print"])[0]],
        "options": fill_blanks_data.get("options") or prog_options_map.get(lang_key, prog_options_map["python"]),
    }

    raw_test = core.get("skill_exa_test") or []
    test_questions = []
    if raw_test:
        for idx, q in enumerate(raw_test, 1):
            ans_val = q.get("answer")
            opts = q.get("options", [])
            correct_idx = 0
            if ans_val in opts:
                correct_idx = opts.index(ans_val)
            test_questions.append({
                "id": idx,
                "question": q.get("question", ""),
                "options": opts,
                "correct_answer": correct_idx,
                "answer": ans_val,
            })

    t_title = raw_topic.get("title", f"Topic {topic_id}")
    lang_name = language.upper()
    pad_questions = [
        {
            "question": f"What is the primary role of '{t_title}' in {lang_name} programming?",
            "options": [
                f"A core programming concept in {raw_topic.get('category', 'Fundamentals')} for {t_title}",
                "An unused CSS styling directive",
                "A hardware driver protocol only used in firmware",
                "A database table locking rule",
            ],
            "answer": f"A core programming concept in {raw_topic.get('category', 'Fundamentals')} for {t_title}",
        },
        {
            "question": f"Which standard keyword or construct is fundamental to '{t_title}' in {lang_name}?",
            "options": [
                prog_options_map.get(lang_key, ["print"])[0],
                "Direct raw disk sector formatting",
                "Unbounded buffer overflow execution",
                "Operating system power cycle reset",
            ],
            "answer": prog_options_map.get(lang_key, ["print"])[0],
        },
        {
            "question": f"What is the recommended best practice when working with '{t_title}' in {lang_name}?",
            "options": [
                f"Write structured, maintainable code following {lang_name} clean code standards",
                "Hardcode magic numbers without comments or error checks",
                "Ignore compiler warnings and memory safety guidelines",
                "Bypass function scope and use global state everywhere",
            ],
            "answer": f"Write structured, maintainable code following {lang_name} clean code standards",
        },
        {
            "question": f"What potential error or bug can happen if '{t_title}' is implemented incorrectly?",
            "options": [
                f"Syntax or runtime execution errors in {lang_name}",
                "Physical GPU fan speed reduction",
                "Static HTML layout shift",
                "Automatic database deletion",
            ],
            "answer": f"Syntax or runtime execution errors in {lang_name}",
        },
        {
            "question": f"How does mastering '{t_title}' benefit software development in {lang_name}?",
            "options": [
                "Improves program modularity, execution safety, and readability",
                "Slows down program compilation by 10x",
                "Prevents the program from running on modern operating systems",
                "Removes the need for variable type definitions",
            ],
            "answer": "Improves program modularity, execution safety, and readability",
        },
    ]

    while len(test_questions) < 5:
        idx = len(test_questions) + 1
        q_item = pad_questions[(idx - 1) % len(pad_questions)]
        ans_val = q_item["answer"]
        opts = q_item["options"]
        correct_idx = opts.index(ans_val) if ans_val in opts else 0
        test_questions.append({
            "id": idx,
            "question": q_item["question"],
            "options": opts,
            "correct_answer": correct_idx,
            "answer": ans_val,
        })

    return ApiResponse(
        success=True,
        message=f"Retrieved topic {topic_id} details for {language.upper()}.",
        data={
            "id": topic_id,
            "title": raw_topic["title"],
            "difficulty": raw_topic.get("difficulty", "Beginner"),
            "duration": raw_topic.get("duration", "20 min"),
            "category": raw_topic.get("category", f"{language.title()} Fundamentals"),
            "status": "IN_PROGRESS" if topic_id == 1 else "LOCKED",
            "information": {
                "concept": concept_text,
                "syntax": syntax_code,
            },
            "examples": example_data,
            "programming": programming_task,
            "fill_blanks": fill_blanks,
            "test": test_questions,
        },
    )
