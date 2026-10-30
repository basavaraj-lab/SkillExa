import logging
import re
import urllib.parse
from typing import Any, Dict, List
import httpx

logger = logging.getLogger("skillexa.web_search")

# Curated list of trusted educational and official government domains
TRUSTED_EDUCATION_DOMAINS = [
    "docs.python.org",
    "developer.mozilla.org",
    "geeksforgeeks.org",
    "gate2025.iitr.ac.in",
    "gate.iitk.ac.in",
    "ssc.gov.in",
    "upsc.gov.in",
    "kpsc.kar.nic.in",
    "nptel.ac.in",
    "ieeexplore.ieee.org",
    "en.wikipedia.org",
]

# Quick domain-specific fallback entries for high-demand topics
CANONICAL_EDUCATIONAL_INDEX = {
    "gate": [
        {
            "title": "GATE Official Portal - IIT Organizing Institute",
            "url": "https://gate2025.iitr.ac.in",
            "snippet": "Official Graduate Aptitude Test in Engineering (GATE) portal for examination dates, syllabus, admit card download, and result scorecards.",
            "source": "GATE Official",
        },
        {
            "title": "GATE ECE Syllabus & Exam Pattern",
            "url": "https://gate2025.iitr.ac.in/syllabus.html",
            "snippet": "Electronics & Communication Engineering (ECE) GATE syllabus: Engineering Mathematics, Networks, Signals & Systems, Electronic Devices, Analog & Digital Circuits, Control Systems, Communications, and Electromagnetics.",
            "source": "GATE Official",
        },
    ],
    "ssc": [
        {
            "title": "Staff Selection Commission (SSC) Official Portal",
            "url": "https://ssc.gov.in",
            "snippet": "Latest recruitment notices for SSC CGL, CHSL, MTS, GD Constable, application status, exam schedules, and official answer keys.",
            "source": "SSC Official",
        },
    ],
    "upsc": [
        {
            "title": "Union Public Service Commission (UPSC) Portal",
            "url": "https://upsc.gov.in",
            "snippet": "Official portal for Civil Services Examination (CSE), NDA, CDS, Engineering Services (ESE), active examinations, notifications, and results.",
            "source": "UPSC Official",
        },
    ],
    "kpsc": [
        {
            "title": "Karnataka Public Service Commission (KPSC)",
            "url": "https://kpsc.kar.nic.in",
            "snippet": "Karnataka government recruitment notifications, Gazetted Probationers (KAS), FDA, SDA, Technical posts, timetables, and eligibility criteria.",
            "source": "KPSC Official",
        },
    ],
    "python": [
        {
            "title": "Python 3 Official Documentation",
            "url": "https://docs.python.org/3/",
            "snippet": "Official tutorial, language reference, and standard library documentation for Python 3.",
            "source": "Python Software Foundation",
        },
    ],
    "mdn": [
        {
            "title": "MDN Web Docs - Web development tutorials & references",
            "url": "https://developer.mozilla.org",
            "snippet": "Comprehensive documentation for HTML, CSS, JavaScript, and Web APIs maintained by Mozilla and the web community.",
            "source": "MDN Web Docs",
        },
    ],
    "dsa": [
        {
            "title": "GeeksforGeeks - Data Structures and Algorithms",
            "url": "https://www.geeksforgeeks.org/data-structures/",
            "snippet": "Complete tutorial and practice problems for Arrays, Linked Lists, Trees, Graphs, Dynamic Programming, and Greedy algorithms.",
            "source": "GeeksforGeeks",
        },
    ],
}


class WebSearchService:
    """
    Educational Web Search Service.
    Searches online resources (DuckDuckGo HTML / Wikipedia / Official Education & Exam Portals)
    and formats verified clickable citations.
    """

    @classmethod
    async def search(cls, query: str, limit: int = 4) -> List[Dict[str, Any]]:
        clean_query = query.strip()
        if not clean_query:
            return []

        results: List[Dict[str, Any]] = []

        # 1. Try DuckDuckGo HTML Search
        try:
            ddg_results = await cls._search_duckduckgo(clean_query, limit=limit)
            if ddg_results:
                results.extend(ddg_results)
        except Exception as e:
            logger.warning("DuckDuckGo search error: %s", e)

        # 2. Try Wikipedia Search if needed
        if len(results) < limit:
            try:
                wiki_results = await cls._search_wikipedia(clean_query, limit=limit - len(results))
                if wiki_results:
                    results.extend(wiki_results)
            except Exception as e:
                logger.warning("Wikipedia search error: %s", e)

        # 3. Augment with Canonical Educational Index if relevant keywords match
        lower_q = clean_query.lower()
        for key, items in CANONICAL_EDUCATIONAL_INDEX.items():
            if key in lower_q:
                for item in items:
                    if not any(r.get("url") == item["url"] for r in results):
                        results.append(item)
                        if len(results) >= limit + 2:
                            break

        return results[:limit]

    @classmethod
    async def _search_duckduckgo(cls, query: str, limit: int = 4) -> List[Dict[str, Any]]:
        url = "https://html.duckduckgo.com/html/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        }
        data = {"q": f"{query} educational official"}

        async with httpx.AsyncClient(timeout=4.0, follow_redirects=True) as client:
            resp = await client.post(url, data=data, headers=headers)
            if resp.status_code != 200:
                return []

            html = resp.text
            # Extract links and snippets from DDG HTML
            # Results have <a class="result__snippet" ...> or <a class="result__url" ...>
            items = []
            
            # Match result elements
            link_pattern = re.compile(
                r'<a[^>]+class="result__url"[^>]+href="([^"]+)"[^>]*>\s*(?:<b>)?([^<]+)(?:</b>)?\s*</a>',
                re.IGNORECASE,
            )
            title_pattern = re.compile(
                r'<a[^>]+class="result__snippet"[^>]+href="([^"]+)"[^>]*>([\s\S]*?)</a>',
                re.IGNORECASE,
            )

            # Standard DDG html results often have:
            # <h2 class="result__title"><a class="result__a" href="//duckduckgo.com/l/?uddg=URL...">TITLE</a></h2>
            title_matches = re.findall(
                r'<h2[^>]*class="result__title"[^>]*>[\s\S]*?<a[^>]*class="result__a"[^>]*href="([^"]+)"[^>]*>([\s\S]*?)</a>',
                html,
                re.IGNORECASE,
            )
            snippet_matches = re.findall(
                r'<a[^>]*class="result__snippet"[^>]*>([\s\S]*?)</a>',
                html,
                re.IGNORECASE,
            )

            for i, (raw_href, raw_title) in enumerate(title_matches[:limit]):
                title = re.sub(r"<[^>]+>", "", raw_title).strip()
                # Parse actual destination URL from DDG redirect (uddg parameter)
                actual_url = raw_href
                if "uddg=" in raw_href:
                    try:
                        parsed = urllib.parse.urlparse(raw_href)
                        qs = urllib.parse.parse_qs(parsed.query)
                        if "uddg" in qs:
                            actual_url = qs["uddg"][0]
                    except Exception:
                        pass
                elif raw_href.startswith("//"):
                    actual_url = f"https:{raw_href}"

                snippet = ""
                if i < len(snippet_matches):
                    snippet = re.sub(r"<[^>]+>", "", snippet_matches[i]).strip()

                if title and actual_url.startswith("http"):
                    # Extract domain for clean display
                    try:
                        domain = urllib.parse.urlparse(actual_url).netloc
                    except Exception:
                        domain = "Web Source"
                    items.append({
                        "title": title,
                        "url": actual_url,
                        "snippet": snippet or f"Official educational resource for {title}",
                        "source": domain,
                    })

            return items

    @classmethod
    async def _search_wikipedia(cls, query: str, limit: int = 2) -> List[Dict[str, Any]]:
        endpoint = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "utf8": 1,
            "srlimit": limit,
        }
        headers = {"User-Agent": "SkillExaEducationalAssistant/2.0 (contact@skillexa.edu)"}

        async with httpx.AsyncClient(timeout=3.5) as client:
            resp = await client.get(endpoint, params=params, headers=headers)
            if resp.status_code != 200:
                return []

            data = resp.json()
            search_items = data.get("query", {}).get("search", [])
            results = []
            for item in search_items:
                title = item.get("title", "")
                snippet = re.sub(r"<[^>]+>", "", item.get("snippet", "")).strip()
                page_url = f"https://en.wikipedia.org/wiki/{urllib.parse.quote(title.replace(' ', '_'))}"
                results.append({
                    "title": f"{title} - Wikipedia",
                    "url": page_url,
                    "snippet": snippet,
                    "source": "Wikipedia",
                })
            return results

