"""
ULTIMATE BADASS TUTORING APP - FLASK VERSION
This is going to be INSANELY cool for kids!
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room
import sqlite3
import json
import os
import random
import time
from datetime import datetime
import threading

from services.upload_service import UploadService

app = Flask(__name__)
app.config.setdefault(
    "SECRET_KEY", os.getenv("SECRET_KEY", "badass_tutor_secret_key_2024")
)
app.config.setdefault("DATABASE_URL", os.getenv("DATABASE_URL", "tutor_app.db"))
socketio = SocketIO(app, cors_allowed_origins="*")

# Import our existing modules
from database import (
    init_database,
    get_all_subjects,
    get_topics_by_subject,
    get_lessons_by_topic,
    get_lesson_by_id,
    get_practice_problems_by_lesson,
    record_practice_attempt,
    get_lesson_progress,
    get_overall_progress,
    get_topic_by_id,
    get_subject_by_id,
    get_practice_problems_by_topic,
)
from curriculum_data import seed_curriculum
from file_processor import process_uploaded_file
from lesson_generator import generate_lesson_from_text, generate_practice_problems
from api_integrations import enrich_lesson_with_api_data, search_all_sources
from api_integrations_badass import (
    educational_apis,
    get_lesson_content,
    search_all_resources,
)
from worksheet_ai_converter import worksheet_converter, convert_worksheet_to_lesson
from MEGA_AI_TUTOR import mega_tutor, ask_tutor
from personalized_learning import personalized_learning, create_student_path
from visual_content_generator import visual_generator, generate_lesson_visuals
from worksheet_generator_api import worksheet_generator_api, generate_worksheet

# Database initialization guard
_database_initialized = False


def initialize_database():
    """Initialize and seed the database once per process."""
    global _database_initialized
    if _database_initialized:
        return
    init_database()
    seed_curriculum()
    _database_initialized = True


def ensure_database_ready():
    """Ensure the database is ready before serving traffic."""
    if app.config.get("TESTING"):
        return
    initialize_database()


# Register the function to run before first request
app.before_request(ensure_database_ready)


def create_app(config_override=None):
    """Return the configured Flask application."""
    if config_override:
        app.config.update(config_override)
    return app


# Register Open Learning Blueprint (50+ free APIs!)
from open_learning.router import bp as open_learning_bp

# Register Parent Dashboard Blueprint
from blueprints.parent import parent_bp

app.register_blueprint(open_learning_bp)
app.register_blueprint(parent_bp)

# Game state for multiplayer
game_rooms = {}
user_sessions = {}


@app.route("/")
def home():
    """BADASS Home Page with animations and games"""
    return render_template("home.html")


@app.route("/subjects")
def subjects():
    """Subjects page with interactive cards"""
    subjects = get_all_subjects()
    return render_template("subjects.html", subjects=subjects)


@app.route("/subject/<int:subject_id>")
def subject_topics(subject_id):
    """Topics for a specific subject"""
    subjects = get_all_subjects()
    subject = next((s for s in subjects if s["id"] == subject_id), None)
    if not subject:
        return redirect(url_for("subjects"))

    topics = get_topics_by_subject(subject_id)
    return render_template("topics.html", subject=subject, topics=topics)


@app.route("/api/subjects")
def api_subjects():
    """API endpoint to get all subjects"""
    subjects = get_all_subjects()
    return jsonify(subjects)


@app.route("/api/subject/<int:subject_id>/topics")
def api_subject_topics(subject_id):
    """API endpoint to get topics for a subject"""
    topics = get_topics_by_subject(subject_id)
    return jsonify(topics)


@app.route("/api/topic/<int:topic_id>/lessons")
def api_topic_lessons(topic_id):
    """API endpoint to get lessons for a topic"""
    lessons = get_lessons_by_topic(topic_id)
    return jsonify(lessons)


@app.route("/api/lesson/<int:lesson_id>")
def api_lesson(lesson_id):
    """API endpoint to get a specific lesson"""
    lesson = get_lesson_by_id(lesson_id)
    if not lesson:
        return jsonify({"error": "Lesson not found"}), 404
    return jsonify(lesson)


@app.route("/api/lesson/<int:lesson_id>/problems")
def api_lesson_problems(lesson_id):
    """API endpoint to get practice problems for a lesson"""
    problems = get_practice_problems_by_lesson(lesson_id)
    return jsonify(problems)


@app.route("/topic/<int:topic_id>")
def topic_lessons(topic_id):
    """Lessons for a specific topic"""
    topic = get_topic_by_id(topic_id)
    if not topic:
        return redirect(url_for("subjects"))

    lessons = get_lessons_by_topic(topic_id)
    return render_template("lessons.html", topic=topic, lessons=lessons)


@app.route("/lesson/<int:lesson_id>")
def lesson_view(lesson_id):
    """Individual lesson with games and animations"""
    lesson = get_lesson_by_id(lesson_id)
    if not lesson:
        return redirect(url_for("subjects"))

    # lesson already has subject_id and subject_name from the JOIN query
    return render_template("lesson.html", lesson=lesson)


@app.route("/practice/<int:lesson_id>")
def practice_view(lesson_id):
    """Practice mode with games and instant feedback"""
    lesson = get_lesson_by_id(lesson_id)
    if not lesson:
        return redirect(url_for("subjects"))

    problems = get_practice_problems_by_lesson(lesson_id)
    return render_template("practice.html", lesson=lesson, problems=problems)


@app.route("/games")
def games():
    """Interactive games hub"""
    return render_template("games.html")


@app.route("/achievements")
def achievements():
    """Achievement system with rewards"""
    progress = get_overall_progress()
    return render_template("achievements.html", progress=progress)


@app.route("/multiplayer")
def multiplayer():
    """Multiplayer learning challenges"""
    return render_template("multiplayer.html")


@app.route("/upload")
def upload_page():
    """Worksheet upload page"""
    return render_template("upload.html")


@app.route("/api/upload/worksheet", methods=["POST"])
def upload_worksheet():
    """API endpoint for worksheet upload and conversion"""
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    # Get subject from form
    subject = request.form.get("subject", "Math")

    upload_service = UploadService()
    file_info = upload_service.save_file(file)
    file_path = file_info["file_path"]
    filename = file_info["filename"]
    try:
        # Convert worksheet to lesson
        result = convert_worksheet_to_lesson(file_path, subject)

        # Clean up uploaded file
        upload_service.delete_file(filename)

        return jsonify(result)
    except Exception as e:
        # Clean up on error
        upload_service.delete_file(filename)
        return jsonify({"error": str(e)}), 500


@app.route("/api/submit_answer", methods=["POST"])
def submit_answer():
    """API endpoint for submitting answers with instant feedback"""
    data = request.json
    lesson_id = data.get("lesson_id")
    problem_id = data.get("problem_id")
    answer = data.get("answer")

    # Get the correct answer
    problems = get_practice_problems_by_lesson(lesson_id)
    problem = next((p for p in problems if p["id"] == problem_id), None)

    if not problem:
        return jsonify({"error": "Problem not found"}), 404

    is_correct = answer.strip().lower() == problem["answer"].strip().lower()

    # Record the attempt
    record_practice_attempt(lesson_id, problem_id, is_correct)

    # Emit real-time feedback
    socketio.emit(
        "answer_feedback",
        {
            "correct": is_correct,
            "correct_answer": problem["answer"],
            "user_answer": answer,
            "celebration": is_correct,
        },
    )

    return jsonify(
        {
            "correct": is_correct,
            "correct_answer": problem["answer"],
            "feedback": "AWESOME!" if is_correct else "Try again!",
        }
    )


@app.route("/api/start_game", methods=["POST"])
def start_game():
    """Start a multiplayer game"""
    data = request.json
    game_type = data.get("game_type")
    user_id = session.get("user_id", f"user_{random.randint(1000, 9999)}")

    # Create or join game room
    room_id = f"game_{game_type}_{int(time.time())}"
    if room_id not in game_rooms:
        game_rooms[room_id] = {
            "type": game_type,
            "players": [],
            "questions": [],
            "started": False,
        }

    game_rooms[room_id]["players"].append(user_id)
    session["room_id"] = room_id
    session["user_id"] = user_id

    return jsonify(
        {
            "room_id": room_id,
            "game_type": game_type,
            "players": len(game_rooms[room_id]["players"]),
        }
    )


# =============== BADASS API INTEGRATION ROUTES ===============


@app.route("/api/enrich/lesson/<int:lesson_id>")
def enrich_lesson(lesson_id):
    """Enrich lesson with external API data"""
    lesson = get_lesson_by_id(lesson_id)
    if not lesson:
        return jsonify({"error": "Lesson not found"}), 404

    # Get comprehensive content from all APIs
    enriched = get_lesson_content(
        lesson["title"], lesson.get("subject_name", "general")
    )

    return jsonify(enriched)


@app.route("/api/search/resources")
def search_resources():
    """Search all educational resources"""
    query = request.args.get("q", "")
    if not query:
        return jsonify({"error": "Query parameter required"}), 400

    results = search_all_resources(query)
    return jsonify(results)


@app.route("/api/math/explain/<topic>")
def explain_math(topic):
    """Get comprehensive math explanation"""
    result = educational_apis.get_math_concept(topic)
    return jsonify(result)


@app.route("/api/science/explore/<topic>")
def explore_science(topic):
    """Get comprehensive science content"""
    result = educational_apis.get_science_content(topic)
    return jsonify(result)


@app.route("/api/language/learn/<word>")
def learn_language(word):
    """Get language arts content"""
    result = educational_apis.get_language_arts_content(word)
    return jsonify(result)


@app.route("/api/social-studies/discover/<topic>")
def discover_social_studies(topic):
    """Get social studies content"""
    result = educational_apis.get_social_studies_content(topic)
    return jsonify(result)


@app.route("/api/videos/search")
def search_videos():
    """Search educational videos"""
    query = request.args.get("q", "")
    category = request.args.get("category", "")

    videos = educational_apis.search_educational_videos(query, category)
    return jsonify(videos)


@app.route("/api/trivia")
def get_trivia():
    """Get trivia questions"""
    category = request.args.get("category", "")
    difficulty = request.args.get("difficulty", "medium")

    questions = educational_apis.get_trivia_questions(category, difficulty)
    return jsonify(questions)


@app.route("/api/wikipedia/<topic>")
def get_wikipedia(topic):
    """Get Wikipedia summary"""
    result = educational_apis.get_wikipedia_summary(topic)
    return jsonify(result)


@app.route("/api/fun/quote")
def get_quote():
    """Get inspirational quote"""
    quote = educational_apis.get_fun_quotes()
    return jsonify(quote)


@app.route("/api/fun/fact")
def get_fact():
    """Get interesting fact"""
    topic = request.args.get("topic", "random")
    fact = educational_apis.get_interesting_fact(topic)
    return jsonify({"fact": fact})


@app.route("/api/nasa/apod")
def get_nasa_apod():
    """Get NASA Astronomy Picture of the Day"""
    result = educational_apis.get_nasa_content("space")
    return jsonify(result)


@app.route("/api/geography/<location>")
def get_geography(location):
    """Get geography information"""
    result = educational_apis.get_geography_info(location)
    return jsonify(result)


@app.route("/api/country/<country>")
def get_country(country):
    """Get country information"""
    result = educational_apis.get_country_info(country)
    return jsonify(result)


@app.route("/api/periodic-table/<element>")
def get_element(element):
    """Get periodic table element info"""
    result = educational_apis.get_periodic_table_info(element)
    return jsonify(result)


@app.route("/api/earthquake/recent")
def get_earthquakes():
    """Get recent earthquake data"""
    result = educational_apis.get_earthquake_data()
    return jsonify(result)


@app.route("/api/literature/search")
def search_literature():
    """Search literature"""
    query = request.args.get("q", "")
    result = educational_apis.search_literature(query)
    return jsonify(result)


@app.route("/api/poetry/search")
def search_poetry():
    """Search poetry"""
    query = request.args.get("q", "")
    result = educational_apis.search_poetry(query)
    return jsonify(result)


@app.route("/api/comprehensive/<int:grade>/<subject>")
def get_comprehensive_resources(grade, subject):
    """Get comprehensive resources for grade and subject"""
    result = educational_apis.get_comprehensive_resources(grade, subject)
    return jsonify(result)


# =============== AI TUTOR & PERSONALIZATION ROUTES ===============


@app.route("/api/ask-tutor", methods=["POST"])
def ask_ai_tutor():
    """Ask the AI tutor ANY question!"""
    data = request.json
    question = data.get("question", "")
    subject = data.get("subject", "general")
    level = data.get("level", "grade_5")

    if not question:
        return jsonify({"error": "Question required"}), 400

    answer = ask_tutor(question, subject, level)
    return jsonify(answer)


@app.route("/api/create-learning-path", methods=["POST"])
def create_learning_path():
    """Create personalized learning path for student"""
    profile = request.json

    path = create_student_path(profile)
    return jsonify(path)


@app.route("/api/study-plan/<topic>/<int:time>/<level>")
def get_study_plan(topic, time, level):
    """Get personalized study plan"""
    plan = mega_tutor.generate_study_plan(topic, time, level)
    return jsonify(plan)


@app.route("/api/tutor/conversation-history")
def get_tutor_history():
    """Get AI tutor conversation history"""
    history = mega_tutor.get_conversation_summary()
    return jsonify(history)


# =============== VISUAL CONTENT & WORKSHEET GENERATION ROUTES ===============


@app.route("/api/generate/visuals/<int:lesson_id>")
def generate_visuals_for_lesson(lesson_id):
    """Generate all visuals for a lesson"""
    lesson = get_lesson_by_id(lesson_id)
    if not lesson:
        return jsonify({"error": "Lesson not found"}), 404

    visuals = generate_lesson_visuals(lesson)
    return jsonify(visuals)


@app.route("/api/generate/worksheet", methods=["POST"])
def generate_worksheet_from_apis():
    """Generate worksheet using APIs"""
    data = request.json
    topic = data.get("topic", "Math")
    subject = data.get("subject", "Math")
    grade = data.get("grade", 5)

    worksheet = generate_worksheet(topic, subject, grade)
    return jsonify(worksheet)


@app.route("/api/generate/worksheet-pack/<int:grade>/<subject>")
def generate_worksheet_pack(grade, subject):
    """Generate complete worksheet pack"""
    worksheets = worksheet_generator_api.generate_comprehensive_worksheet_pack(
        grade, subject
    )
    return jsonify(
        {
            "grade": grade,
            "subject": subject,
            "worksheets": worksheets,
            "total_count": len(worksheets),
        }
    )


@app.route("/worksheets")
def worksheets_page():
    """Worksheet generator page"""
    return render_template("worksheets.html")


@app.route("/books-reader")
def books_reader_page():
    """Kids Book Reader - Read books in the app!"""
    return render_template("books_reader.html")


@app.route("/api-explorer")
def api_explorer_page():
    """API Directory - main page linking to all APIs"""
    return render_template("api_directory.html")


@app.route("/api/wikipedia")
def wikipedia_page():
    """Wikipedia API page with real content"""
    return render_template("api_wikipedia.html")


@app.route("/api/nasa")
def nasa_page():
    """NASA API page with real space content"""
    return render_template("api_nasa.html")


@app.route("/api/books")
def books_page():
    """Open Library API page"""
    return render_template("api_books.html")


@app.route("/api/quiz")
def quiz_page():
    """Open Trivia API page"""
    return render_template("api_quiz.html")


@app.route("/api/vocabulary")
def vocabulary_page():
    """Datamuse vocabulary API page"""
    return render_template("api_vocabulary.html")


@app.route("/api/dictionary")
def dictionary_page():
    """Free Dictionary API page"""
    return render_template("api_dictionary.html")


@app.route("/api/library-congress")
def loc_page():
    """Library of Congress API page"""
    return render_template("api_loc.html")


@app.route("/api/met-museum")
def met_page():
    """Met Museum API page"""
    return render_template("api_met.html")


@app.route("/api/earthquakes")
def earthquakes_page():
    """USGS Earthquakes API page"""
    return render_template("api_earthquakes.html")


@app.route("/api/numbers")
def numbers_page():
    """Numbers API page"""
    return render_template("api_numbers.html")


@app.route("/api/jeopardy")
def jeopardy_page():
    """JService Jeopardy API page"""
    return render_template("api_jeopardy.html")


@app.route("/api/poetry")
def poetry_page():
    """PoetryDB API page"""
    return render_template("api_poetry.html")


@app.route("/api/quotes")
def quotes_page():
    """Quotable API page"""
    return render_template("api_quotes.html")


@app.route("/api/pubchem")
def pubchem_page():
    """PubChem API page"""
    return render_template("api_pubchem.html")


@app.route("/api/nasa-mars")
def nasa_mars_page():
    """NASA Mars Rovers"""
    return render_template("api_nasa_mars.html")


@app.route("/api/wikidata")
def wikidata_page():
    return render_template("api_wikidata.html")


@app.route("/api/internet-archive")
def internet_archive_page():
    return render_template("api_internet_archive.html")


@app.route("/api/google-books")
def google_books_page():
    return render_template("api_google_books.html")


@app.route("/api/wordnik")
def wordnik_page():
    return render_template("api_wordnik.html")


@app.route("/api/tatoeba")
def tatoeba_page():
    return render_template("api_tatoeba.html")


@app.route("/api/rhymebrain")
def rhymebrain_page():
    return render_template("api_rhymebrain.html")


@app.route("/api/gbif")
def gbif_page():
    return render_template("api_gbif.html")


@app.route("/api/inaturalist")
def inaturalist_page():
    return render_template("api_inaturalist.html")


@app.route("/api/openweather")
def openweather_page():
    return render_template("api_openweather.html")


@app.route("/api/noaa")
def noaa_page():
    return render_template("api_noaa.html")


@app.route("/api/open-meteo")
def open_meteo_page():
    return render_template("api_open_meteo.html")


@app.route("/api/solar-system")
def solar_system_page():
    return render_template("api_solar_system.html")


@app.route("/api/oeis")
def oeis_page():
    return render_template("api_oeis.html")


@app.route("/api/rijksmuseum")
def rijksmuseum_page():
    return render_template("api_rijksmuseum.html")


@app.route("/api/harvard-art")
def harvard_art_page():
    return render_template("api_harvard_art.html")


@app.route("/api/smithsonian")
def smithsonian_page():
    return render_template("api_smithsonian.html")


@app.route("/api/europeana")
def europeana_page():
    return render_template("api_europeana.html")


@app.route("/api/dpla")
def dpla_page():
    return render_template("api_dpla.html")


@app.route("/api/openverse")
def openverse_page():
    return render_template("api_openverse.html")


@app.route("/api/national-gallery")
def national_gallery_page():
    return render_template("api_national_gallery.html")


@app.route("/api/brooklyn-museum")
def brooklyn_museum_page():
    return render_template("api_brooklyn_museum.html")


@app.route("/api/cmu-dict")
def cmu_dict_page():
    return render_template("api_cmu_dict.html")


@app.route("/api/wiktionary")
def wiktionary_page():
    return render_template("api_wiktionary.html")


@app.route("/api/wordnet")
def wordnet_page():
    return render_template("api_wordnet.html")


@app.route("/api/api-ninjas")
def api_ninjas_page():
    return render_template("api_api_ninjas.html")


@app.route("/api/random-org")
def random_org_page():
    return render_template("api_random_org.html")


@app.route("/api/xkcd")
def xkcd_page():
    return render_template("api_xkcd.html")


@app.route("/api/nasa-eonet")
def nasa_eonet_page():
    return render_template("api_nasa_eonet.html")


@app.route("/api/spacex")
def spacex_page():
    return render_template("api_spacex.html")


@app.route("/api/iss-location")
def iss_location_page():
    return render_template("api_iss_location.html")


@app.route("/api/astronomy-picture")
def astronomy_picture_page():
    return render_template("api_astronomy_picture.html")


@app.route("/api/countries")
def countries_page():
    return render_template("api_countries.html")


@app.route("/api/un-data")
def un_data_page():
    return render_template("api_un_data.html")


@app.route("/api/world-bank")
def world_bank_page():
    return render_template("api_world_bank.html")


@app.route("/api/census")
def census_page():
    return render_template("api_census.html")


@app.route("/api/nces")
def nces_page():
    return render_template("api_nces.html")


@app.route("/api/user/stats")
def get_user_stats():
    """Get user statistics"""
    progress = get_overall_progress()
    return jsonify(
        {
            "lessons": progress.get("lessons_started", 0),
            "problems": progress.get("problems_mastered", 0),
            "achievements": 0,  # Placeholder
            "streak": 0,  # Placeholder
        }
    )


@app.route("/api/leaderboard")
def get_leaderboard():
    """Get leaderboard data"""
    # Mock data for now
    return jsonify(
        {
            "top_players": [
                {"rank": 1, "name": "MathMaster99", "score": 2847, "avatar": "👑"},
                {"rank": 2, "name": "ScienceWiz", "score": 2634, "avatar": "🥈"},
                {"rank": 3, "name": "WordHunter", "score": 2421, "avatar": "🥉"},
            ]
        }
    )


# Socket.IO events for real-time features
@socketio.on("join_game")
def on_join_game(data):
    room_id = data["room_id"]
    user_id = session.get("user_id")
    join_room(room_id)

    if room_id in game_rooms:
        emit(
            "player_joined",
            {"user_id": user_id, "total_players": len(game_rooms[room_id]["players"])},
            room=room_id,
        )


@socketio.on("leave_game")
def on_leave_game(data):
    room_id = data["room_id"]
    user_id = session.get("user_id")
    leave_room(room_id)

    if room_id in game_rooms and user_id in game_rooms[room_id]["players"]:
        game_rooms[room_id]["players"].remove(user_id)
        emit(
            "player_left",
            {"user_id": user_id, "total_players": len(game_rooms[room_id]["players"])},
            room=room_id,
        )


@socketio.on("game_answer")
def on_game_answer(data):
    room_id = data["room_id"]
    answer = data["answer"]
    user_id = session.get("user_id")

    # Process answer and emit results
    emit(
        "answer_result",
        {
            "user_id": user_id,
            "answer": answer,
            "correct": True,  # This would be determined by game logic
        },
        room=room_id,
    )


if __name__ == "__main__":
    with app.app_context():
        initialize_database()
    socketio.run(app, debug=True, host="0.0.0.0", port=5001)
