"""
Open Trivia Database API Adapter
FREE quiz questions for all subjects!
"""

from open_learning.http_client import safe_get
from open_learning.cache import cache_get, cache_set
from open_learning.schemas import QAItem
import html


def fetch_quiz(
    amount: int = 10, category: str = None, difficulty: str = None
) -> list[QAItem]:
    """Fetch quiz questions"""
    cache_key = f"trivia:{amount}:{category}:{difficulty}"
    cached = cache_get(cache_key)
    if cached:
        return cached

    url = "https://opentdb.com/api.php"
    params = {"amount": amount, "type": "multiple"}

    # Category mapping
    categories = {"science": 17, "math": 19, "history": 23, "geography": 22, "art": 25}

    if category and category.lower() in categories:
        params["category"] = categories[category.lower()]

    if difficulty in ["easy", "medium", "hard"]:
        params["difficulty"] = difficulty

    data = safe_get(url, params=params, default={})

    results = []
    for item in data.get("results", []):
        # Decode HTML entities
        question = html.unescape(item.get("question", ""))
        correct = html.unescape(item.get("correct_answer", ""))
        incorrect = [html.unescape(ans) for ans in item.get("incorrect_answers", [])]

        qa = QAItem(
            question=question,
            source="Open Trivia DB",
            choices=incorrect + [correct],  # Mix them up
            answer=correct,
            difficulty=item.get("difficulty"),
            category=item.get("category"),
        )
        results.append(qa)

    cache_set(cache_key, results, ttl=1800)  # Cache 30 min
    return results
