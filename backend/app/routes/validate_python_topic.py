"""Validate the structure and runnable examples in python_topics.py."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import os
import tempfile
from pathlib import Path


TOPICS_FILE = Path(__file__).with_name("python_topics.py")
EXPECTED_LIST_LENGTHS = {
    "fill_blanks": 5,
    "quiz": 10,
    "practice": 5,
}


def load_topics() -> dict[int, dict[str, object]]:
    """Import and return the dataset from python_topics.py."""
    spec = importlib.util.spec_from_file_location("python_topics_module", TOPICS_FILE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {TOPICS_FILE}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.python_topics


def validate_structure(topics: dict[int, dict[str, object]]) -> list[str]:
    """Check the dataset shape and answer consistency."""
    issues: list[str] = []
    expected_ids = list(range(1, len(topics) + 1))

    if list(topics) != expected_ids:
        issues.append(
            f"Topic keys should be sequential from 1 to {len(topics)}; got {list(topics)}"
        )

    for key, topic in topics.items():
        title = topic.get("title", "<untitled>")

        if topic.get("id") != key:
            issues.append(f"Topic {key} ({title}) has mismatched id {topic.get('id')}")

        for field, expected_length in EXPECTED_LIST_LENGTHS.items():
            items = topic.get(field, [])
            if not isinstance(items, list):
                issues.append(f"Topic {key} ({title}) field {field} is not a list")
                continue

            if len(items) != expected_length:
                issues.append(
                    f"Topic {key} ({title}) field {field} should have "
                    f"{expected_length} items, found {len(items)}"
                )

        quiz = topic.get("quiz", [])
        if isinstance(quiz, list):
            for index, question in enumerate(quiz, start=1):
                if not isinstance(question, dict):
                    issues.append(
                        f"Topic {key} ({title}) quiz {index} is not a dictionary"
                    )
                    continue

                options = question.get("options", [])
                answer = question.get("answer")
                if answer not in options:
                    issues.append(
                        f"Topic {key} ({title}) quiz {index} answer {answer!r} "
                        "is not present in options"
                    )

    return issues


def validate_examples(topics: dict[int, dict[str, object]]) -> list[str]:
    """Execute each example and compare its stdout with the recorded output."""
    issues: list[str] = []
    original_cwd = Path.cwd()

    for key, topic in topics.items():
        title = topic.get("title", "<untitled>")
        code = topic.get("example")
        expected_output = topic.get("output")

        if not isinstance(code, str) or not isinstance(expected_output, str):
            issues.append(f"Topic {key} ({title}) example/output must be strings")
            continue

        captured = io.StringIO()

        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                os.chdir(temp_dir)
                with contextlib.redirect_stdout(captured):
                    exec(code, {})
        except Exception as exc:  # noqa: BLE001
            issues.append(
                f"Topic {key} ({title}) example raised {type(exc).__name__}: {exc}"
            )
        finally:
            os.chdir(original_cwd)

        actual_output = captured.getvalue().rstrip("\n")
        if actual_output != expected_output:
            issues.append(
                f"Topic {key} ({title}) output mismatch: expected "
                f"{expected_output!r}, got {actual_output!r}"
            )

    return issues


def main() -> int:
    """Run all validations and print a clear summary."""
    topics = load_topics()
    issues = [*validate_structure(topics), *validate_examples(topics)]

    if issues:
        print("Validation failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print(f"Validated {len(topics)} topics successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())