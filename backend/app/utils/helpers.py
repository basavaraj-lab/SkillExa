"""Utility helpers for formatting curriculum content, theory, and templates in SkillExa."""
from __future__ import annotations

import re
from typing import Any


def parse_theory(text: Any) -> dict[str, Any]:
    """
    Parses a theory or concept string into structured components:
    - intro: introductory text/lead paragraph before the numbered points
    - points: list of dictionaries [{"num": "1.", "raw_num": "1", "text": "...", "title": "...", "body": "..."}]
    - outro: trailing/concluding sentence or remarks after points
    - paragraphs: list of paragraph strings if multiple paragraphs without numbered points
    """
    if not text:
        return {"intro": "", "points": [], "outro": "", "paragraphs": []}

    if isinstance(text, (list, tuple)):
        pts = []
        for idx, item in enumerate(text, start=1):
            if isinstance(item, str):
                pts.append(_build_point(str(idx), item))
            elif isinstance(item, dict):
                pts.append(item)
        return {"intro": "", "points": pts, "outro": "", "paragraphs": []}

    text = str(text).strip()

    def _build_point(num: str, raw_text: str) -> dict[str, str]:
        clean_text = raw_text.strip().rstrip(";,")
        title = ""
        body = clean_text
        if ":" in clean_text:
            parts = clean_text.split(":", 1)
            if len(parts[0].strip()) < 60:
                title = parts[0].strip()
                body = parts[1].strip()
        elif " - " in clean_text:
            parts = clean_text.split(" - ", 1)
            if len(parts[0].strip()) < 60:
                title = parts[0].strip()
                body = parts[1].strip()

        display_num = str(num).strip()
        if display_num and not display_num.endswith(".") and display_num not in ("•", "-", "*"):
            display_num = f"{display_num}."

        return {
            "num": display_num,
            "raw_num": str(num).strip(),
            "text": clean_text,
            "title": title,
            "body": body,
        }

    # 1. Multiline with numbered points (1., 2.), bullets (-, *), or parenthesized (1)
    raw_lines = [line.strip() for line in text.splitlines() if line.strip()]
    point_regex = re.compile(r"^(?:([0-9]+)[\.\)]|\-\s*|\*\s*|\(([0-9]+)\)|•\s*)\s*(.+)$")
    has_multiline_points = any(point_regex.match(line) for line in raw_lines)

    if has_multiline_points:
        intro_lines = []
        points = []
        outro_lines = []
        found_point = False
        ended_points = False

        for line in raw_lines:
            m = point_regex.match(line)
            if m:
                found_point = True
                if ended_points:
                    ended_points = False
                num = m.group(1) or m.group(2) or "•"
                content = m.group(3).strip()
                points.append(_build_point(num, content))
            else:
                if not found_point:
                    intro_lines.append(line)
                else:
                    ended_points = True
                    outro_lines.append(line)

        return {
            "intro": "\n".join(intro_lines),
            "points": points,
            "outro": "\n".join(outro_lines),
            "paragraphs": [],
        }

    # 2. Inline parenthesized numbered points e.g. "(1) ... (2) ... (3) ..."
    if re.search(r"\([1-9]\)", text):
        parts = re.split(r"(?:[;,]?\s*(?:and\s+)?|\s+and\s+)?\(([0-9]+)\)\s*", text)
        if len(parts) >= 3:
            intro = parts[0].strip()
            points = []
            outro = ""
            for i in range(1, len(parts), 2):
                num = parts[i]
                content = parts[i + 1].strip() if i + 1 < len(parts) else ""
                if i + 2 >= len(parts):
                    m_dot = re.search(r"(\.[ \t]+)([A-Z0-9].+)$", content)
                    if m_dot:
                        outro = m_dot.group(2).strip()
                        content = content[: m_dot.start() + 1].strip()
                    else:
                        m_sent = re.search(r"\s+((?:All|These|This|Each|Note|In summary|Overall)\b.+)$", content, re.IGNORECASE)
                        if m_sent:
                            outro = m_sent.group(1).strip()
                            content = content[: m_sent.start()].strip()
                points.append(_build_point(num, content))
            return {"intro": intro, "points": points, "outro": outro, "paragraphs": []}

    # 3. Inline numbered points e.g. "1. ... 2. ... 3. ..."
    if re.search(r"(?:^|\s+)[1-9]\.\s+", text):
        parts = re.split(r"(?:[;,]?\s*(?:and\s+)?|\s+and\s+)?(?:^|\s+)([0-9]+)\.\s+", text)
        if len(parts) >= 3:
            intro = parts[0].strip()
            points = []
            outro = ""
            for i in range(1, len(parts), 2):
                num = parts[i]
                content = parts[i + 1].strip() if i + 1 < len(parts) else ""
                if i + 2 >= len(parts):
                    m_dot = re.search(r"(\.[ \t]+)([A-Z0-9].+)$", content)
                    if m_dot:
                        outro = m_dot.group(2).strip()
                        content = content[: m_dot.start() + 1].strip()
                    else:
                        m_sent = re.search(r"\s+((?:All|These|This|Each|Note|In summary|Overall)\b.+)$", content, re.IGNORECASE)
                        if m_sent:
                            outro = m_sent.group(1).strip()
                            content = content[: m_sent.start()].strip()
                points.append(_build_point(num, content))
            return {"intro": intro, "points": points, "outro": outro, "paragraphs": []}

    # 4. Multiline paragraphs without points
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    if len(paragraphs) > 1:
        return {"intro": "", "points": [], "outro": "", "paragraphs": paragraphs}

    return {"intro": text, "points": [], "outro": "", "paragraphs": []}
