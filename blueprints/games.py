"""
Games blueprint for Ultimate Tutor
Handles multiplayer games and game state
"""

from flask import Blueprint, request, jsonify, session
from flask_socketio import emit, join_room, leave_room
import uuid
from datetime import datetime

games_bp = Blueprint("games", __name__)

# In-memory game state (TODO: Replace with Redis)
game_rooms = {}
user_sessions = {}


@games_bp.route("/games")
def games_page():
    """Games page."""
    return render_template("games.html")


@games_bp.route("/multiplayer")
def multiplayer_page():
    """Multiplayer page."""
    return render_template("multiplayer.html")


@games_bp.route("/achievements")
def achievements_page():
    """Achievements page."""
    return render_template("achievements.html")


@games_bp.route("/api/games/rooms")
def api_game_rooms():
    """Get active game rooms."""
    rooms = []
    for room_id, room_data in game_rooms.items():
        rooms.append(
            {
                "id": room_id,
                "name": room_data.get("name", "Game Room"),
                "players": len(room_data.get("players", [])),
                "max_players": room_data.get("max_players", 4),
                "game_type": room_data.get("game_type", "math"),
                "status": room_data.get("status", "waiting"),
            }
        )
    return jsonify(rooms)


@games_bp.route("/api/games/create-room", methods=["POST"])
def api_create_room():
    """Create a new game room."""
    try:
        data = request.get_json()
        room_name = data.get("name", "New Game Room")
        game_type = data.get("game_type", "math")
        max_players = data.get("max_players", 4)

        room_id = str(uuid.uuid4())[:8]
        game_rooms[room_id] = {
            "id": room_id,
            "name": room_name,
            "game_type": game_type,
            "max_players": max_players,
            "players": [],
            "status": "waiting",
            "created_at": datetime.now().isoformat(),
        }

        return jsonify(
            {"success": True, "room_id": room_id, "room": game_rooms[room_id]}
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@games_bp.route("/api/games/join-room/<room_id>", methods=["POST"])
def api_join_room(room_id):
    """Join a game room."""
    try:
        if room_id not in game_rooms:
            return jsonify({"error": "Room not found"}), 404

        room = game_rooms[room_id]
        if len(room["players"]) >= room["max_players"]:
            return jsonify({"error": "Room is full"}), 400

        # Add player to room
        player_id = str(uuid.uuid4())[:8]
        player = {
            "id": player_id,
            "name": f'Player {len(room["players"]) + 1}',
            "score": 0,
            "joined_at": datetime.now().isoformat(),
        }

        room["players"].append(player)

        return jsonify({"success": True, "player_id": player_id, "room": room})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@games_bp.route("/api/games/leave-room/<room_id>", methods=["POST"])
def api_leave_room(room_id):
    """Leave a game room."""
    try:
        data = request.get_json()
        player_id = data.get("player_id")

        if room_id not in game_rooms:
            return jsonify({"error": "Room not found"}), 404

        room = game_rooms[room_id]
        room["players"] = [p for p in room["players"] if p["id"] != player_id]

        # Delete room if empty
        if not room["players"]:
            del game_rooms[room_id]

        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@games_bp.route("/api/games/start-game/<room_id>", methods=["POST"])
def api_start_game(room_id):
    """Start a game in a room."""
    try:
        if room_id not in game_rooms:
            return jsonify({"error": "Room not found"}), 404

        room = game_rooms[room_id]
        if len(room["players"]) < 2:
            return jsonify({"error": "Need at least 2 players"}), 400

        room["status"] = "playing"
        room["started_at"] = datetime.now().isoformat()

        return jsonify({"success": True, "room": room})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@games_bp.route("/api/achievements")
def api_achievements():
    """Get user achievements."""
    # TODO: Implement achievements system
    achievements = [
        {
            "id": "first_lesson",
            "name": "First Steps",
            "description": "Complete your first lesson",
            "icon": "🎯",
            "earned": True,
            "earned_at": "2024-01-01T00:00:00Z",
        },
        {
            "id": "math_master",
            "name": "Math Master",
            "description": "Complete 10 math lessons",
            "icon": "🔢",
            "earned": False,
            "earned_at": None,
        },
    ]

    return jsonify(achievements)


@games_bp.route("/api/leaderboard")
def api_leaderboard():
    """Get game leaderboard."""
    # TODO: Implement leaderboard
    leaderboard = [
        {"rank": 1, "name": "Math Wizard", "score": 1500, "avatar": "🧙‍♂️"},
        {"rank": 2, "name": "Science Star", "score": 1200, "avatar": "⭐"},
        {"rank": 3, "name": "Reading Rockstar", "score": 1000, "avatar": "🎸"},
    ]

    return jsonify(leaderboard)
