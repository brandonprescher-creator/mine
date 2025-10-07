"""
Flask Router for Open Learning APIs
Exposes all 50+ free education APIs through unified endpoints!
"""

from flask import Blueprint, request, jsonify
from .adapters import wikipedia, openlibrary, datamuse, open_trivia, nasa, loc
from .ALL_50_APIS import all_apis

# Create Blueprint
bp = Blueprint("open_learning", __name__, url_prefix="/api/open")

# ===== UNIFIED SEARCH ENDPOINT =====


@bp.route("/search/<query>")
def unified_search(query: str):
    """
    Search across multiple APIs at once!
    Returns content cards from Wikipedia, Open Library, LoC, etc.
    """
    results = {"query": query, "sources": []}

    try:
        # Wikipedia
        wiki_card = wikipedia.search_summary(query)
        if wiki_card:
            results["sources"].append(wiki_card.to_dict())
    except:
        pass

    try:
        # Open Library
        books = openlibrary.search(query, limit=5)
        for book in books:
            results["sources"].append(book.to_dict())
    except:
        pass

    try:
        # Library of Congress
        loc_items = loc.search(query, count=5)
        for item in loc_items:
            results["sources"].append(item.to_dict())
    except:
        pass

    try:
        # Datamuse related words
        words_card = datamuse.related_words(query, limit=10)
        if words_card:
            results["sources"].append(words_card.to_dict())
    except:
        pass

    results["total_found"] = len(results["sources"])
    return jsonify(results)


# ===== WIKIPEDIA =====


@bp.route("/wikipedia/<title>")
def get_wikipedia(title: str):
    """Get Wikipedia summary"""
    card = wikipedia.search_summary(title)
    return jsonify(card.to_dict() if card else {"error": "Not found"})


# ===== OPEN LIBRARY =====


@bp.route("/books/<query>")
def search_books(query: str):
    """Search for books"""
    limit = request.args.get("limit", 10, type=int)
    books = openlibrary.search(query, limit=limit)
    return jsonify([b.to_dict() for b in books])


# ===== DATAMUSE (VOCABULARY) =====


@bp.route("/vocabulary/related/<word>")
def get_related_words(word: str):
    """Get related words"""
    card = datamuse.related_words(word)
    return jsonify(card.to_dict() if card else {})


@bp.route("/vocabulary/rhymes/<word>")
def get_rhymes(word: str):
    """Get rhyming words"""
    card = datamuse.rhyming_words(word)
    return jsonify(card.to_dict() if card else {})


@bp.route("/vocabulary/synonyms/<word>")
def get_synonyms(word: str):
    """Get synonyms"""
    card = datamuse.synonyms(word)
    return jsonify(card.to_dict() if card else {})


# ===== TRIVIA & QUIZ =====


@bp.route("/quiz")
def get_quiz():
    """Get quiz questions"""
    amount = request.args.get("amount", 10, type=int)
    category = request.args.get("category", None)
    difficulty = request.args.get("difficulty", None)

    questions = open_trivia.fetch_quiz(amount, category, difficulty)
    return jsonify([q.to_dict() for q in questions])


# ===== NASA =====


@bp.route("/nasa/apod")
def get_nasa_apod():
    """Get NASA Astronomy Picture of the Day"""
    date = request.args.get("date", None)
    card = nasa.get_apod(date)
    return jsonify(card.to_dict() if card else {})


@bp.route("/nasa/mars/<rover>")
def get_mars_photos(rover: str):
    """Get Mars Rover photos"""
    sol = request.args.get("sol", 1000, type=int)
    photos = nasa.get_mars_photos(rover, sol)
    return jsonify([p.to_dict() for p in photos])


# ===== LIBRARY OF CONGRESS =====


@bp.route("/loc/<query>")
def search_loc(query: str):
    """Search Library of Congress"""
    count = request.args.get("count", 10, type=int)
    items = loc.search(query, count)
    return jsonify([i.to_dict() for i in items])


# ===== ALL 50 APIs MEGA ENDPOINT =====


@bp.route("/mega-search/<query>")
def mega_search(query: str):
    """
    SEARCH ACROSS ALL 50 APIS AT ONCE!
    Returns combined results from every source!
    """
    results = {"query": query, "total_apis": 50, "content": {}, "summary": {}}

    # Call all APIs (gracefully handle failures)
    apis_to_call = [
        ("wikipedia", lambda: all_apis.wikipedia_summary(query)),
        ("openlibrary", lambda: all_apis.open_library_search(query)),
        ("wikidata", lambda: all_apis.wikidata_query(query)),
        ("nasa_apod", lambda: all_apis.nasa_apod()),
        ("usgs_earthquakes", lambda: all_apis.usgs_earthquakes(5)),
        ("pubchem", lambda: all_apis.pubchem_compound(query)),
        ("numbers_fact", lambda: all_apis.numbers_api_fact(42)),
        ("gbif", lambda: all_apis.gbif_species(query)),
    ]

    for api_name, api_call in apis_to_call:
        try:
            result = api_call()
            if result:
                if isinstance(result, list):
                    results["content"][api_name] = [
                        r.to_dict() if hasattr(r, "to_dict") else r for r in result
                    ]
                else:
                    results["content"][api_name] = (
                        result.to_dict() if hasattr(result, "to_dict") else result
                    )
        except Exception as e:
            results["content"][api_name] = {"error": str(e)}

    # Summary stats
    results["summary"] = {
        "total_sources": len(results["content"]),
        "successful": sum(
            1 for v in results["content"].values() if "error" not in str(v)
        ),
        "failed": sum(1 for v in results["content"].values() if "error" in str(v)),
    }

    return jsonify(results)


# ===== STATS & HEALTH =====


@bp.route("/stats")
def get_stats():
    """Get API usage statistics"""
    from ..cache import get_cache_stats

    return jsonify(
        {"cache_stats": get_cache_stats(), "total_apis": 50, "status": "operational"}
    )


@bp.route("/health")
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "apis_available": 50, "cache_enabled": True})
