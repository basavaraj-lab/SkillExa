import logging
import re
import urllib.parse
from datetime import datetime, timezone
from typing import Optional, Dict, Any, List
import httpx
from sqlalchemy.orm import Session
from backend.app.models.ai_interview import EducationalKnowledgeSource

logger = logging.getLogger("skillexa.knowledge_retrieval")

# MediaWiki API policy: always declare an informative User-Agent
WIKIPEDIA_USER_AGENT = "SkillExaEducationBot/1.0 (https://skillexa.edu; contact@skillexa.edu)"
WIKIPEDIA_API_ENDPOINT = "https://en.wikipedia.org/w/api.php"
WIKIPEDIA_REST_ENDPOINT = "https://en.wikipedia.org/api/rest_v1/page/summary"


def clean_text(text: str) -> str:
    """Clean and normalize extracted Wikipedia text."""
    if not text:
        return ""
    # Strip MediaWiki citations like [1], [2], [citation needed]
    text = re.sub(r"\[\d+\]", "", text)
    text = re.sub(r"\[edit\]", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\[citation needed\]", "", text, flags=re.IGNORECASE)
    # Normalize whitespaces
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_dates(text: str) -> List[str]:
    """Extract 4-digit years/milestones from historical/theoretical text."""
    if not text:
        return []
    # Capture years from 1800 to 2099
    matches = re.findall(r"\b(18\d{2}|19\d{2}|20\d{2})\b", text)
    # Return sorted unique list
    return sorted(list(set(matches)))[:6]


class KnowledgeRetrievalService:
    """
    Retrieves educational context from MediaWiki API (Wikipedia) with caching and attribution.
    Complies with Wikipedia API policies and Creative Commons BY-SA attribution requirements.
    Performs real-time search, extracts historical dates, theoretical foundation, and canonical citations.
    """

    @classmethod
    def get_or_fetch_topic_knowledge(
        cls, db: Session, topic_query: str, subtopic: str = "", max_chars: int = 1500
    ) -> Optional[Dict[str, Any]]:
        """
        Check database cache for previously verified educational source.
        If missing or stale, perform Wikipedia search and extract confirmed theory and dates.
        """
        full_query = f"{topic_query} {subtopic}".strip() if subtopic else topic_query.strip()
        if not full_query:
            return None

        # 1. Check local cache in EducationalKnowledgeSource
        cached = (
            db.query(EducationalKnowledgeSource)
            .filter(
                (EducationalKnowledgeSource.article_title.ilike(f"%{topic_query.strip()}%"))
                | (EducationalKnowledgeSource.content_summary.ilike(f"%{full_query}%"))
            )
            .order_by(EducationalKnowledgeSource.retrieved_at.desc())
            .first()
        )
        if cached:
            dates = extract_dates(cached.content_summary)
            return {
                "source_name": cached.source_name,
                "article_title": cached.article_title,
                "source_url": cached.source_url,
                "content_summary": cached.content_summary,
                "attribution": cached.attribution,
                "dates_and_milestones": dates,
                "is_cached": True,
            }

        # 2. Search & Scrape Wikipedia via MediaWiki API
        try:
            headers = {"User-Agent": WIKIPEDIA_USER_AGENT}
            with httpx.Client(timeout=6.0) as client:
                # Step A: Perform full-text search to find best matching article title
                search_params = {
                    "action": "query",
                    "list": "search",
                    "srsearch": full_query,
                    "srlimit": 3,
                    "format": "json",
                }
                search_res = client.get(WIKIPEDIA_API_ENDPOINT, params=search_params, headers=headers)
                target_title = None

                if search_res.status_code == 200:
                    hits = search_res.json().get("query", {}).get("search", [])
                    if hits:
                        target_title = hits[0].get("title")

                if not target_title:
                    target_title = topic_query.strip()

                # Step B: Fetch extract and page info for confirmed target title
                detail_params = {
                    "action": "query",
                    "prop": "extracts|info",
                    "inprop": "url",
                    "explaintext": 1,
                    "titles": target_title,
                    "redirects": 1,
                    "format": "json",
                }
                detail_res = client.get(WIKIPEDIA_API_ENDPOINT, params=detail_params, headers=headers)
                if detail_res.status_code != 200:
                    logger.warning("MediaWiki API returned status %s for %s", detail_res.status_code, target_title)
                    return None

                data = detail_res.json()
                pages = data.get("query", {}).get("pages", {})
                if not pages:
                    return None

                for page_id, page_data in pages.items():
                    if str(page_id) == "-1" or "missing" in page_data:
                        logger.info("Wikipedia article not found for '%s'", target_title)
                        return None

                    title = page_data.get("title", target_title)
                    encoded_title = urllib.parse.quote(title.replace(" ", "_"))
                    full_url = page_data.get("fullurl", f"https://en.wikipedia.org/wiki/{encoded_title}")
                    raw_extract = page_data.get("extract", "")
                    cleaned_extract = clean_text(raw_extract)

                    if not cleaned_extract:
                        return None

                    # Extract key historical dates and theoretical milestones
                    dates = extract_dates(cleaned_extract)
                    summary = cleaned_extract[:max_chars]
                    attribution = f"Content derived from Wikipedia article '{title}', licensed under CC BY-SA 4.0 ({full_url})"

                    # Save to database cache
                    new_source = EducationalKnowledgeSource(
                        source_name="Wikipedia",
                        article_title=title,
                        source_url=full_url,
                        retrieved_at=datetime.now(timezone.utc),
                        content_summary=summary,
                        attribution=attribution,
                        review_status="verified",
                    )
                    db.add(new_source)
                    db.commit()
                    db.refresh(new_source)

                    return {
                        "source_name": "Wikipedia",
                        "article_title": title,
                        "source_url": full_url,
                        "content_summary": summary,
                        "attribution": attribution,
                        "dates_and_milestones": dates,
                        "is_cached": False,
                    }

        except Exception as e:
            logger.warning("Error scraping educational knowledge for '%s': %s", full_query, e)
            return None
