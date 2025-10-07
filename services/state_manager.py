"""
State management service using Redis
Handles game rooms, user sessions, and real-time state
"""

import json
import uuid
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from config import get_config

try:
    import redis

    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False


class StateManager:
    """Manages application state with Redis or fallback to memory."""

    def __init__(self):
        self.config = get_config()
        self.redis_client = None
        self.memory_store = {}  # Fallback for development

        if REDIS_AVAILABLE and self.config.REDIS_URL:
            try:
                self.redis_client = redis.from_url(self.config.REDIS_URL)
                self.redis_client.ping()  # Test connection
                print("✅ Connected to Redis")
            except Exception as e:
                print(f"⚠️ Redis connection failed: {e}, using memory store")
                self.redis_client = None
        else:
            print("⚠️ Redis not available, using memory store")

    def _get_key(self, prefix: str, key: str) -> str:
        """Generate Redis key."""
        return f"tutor:{prefix}:{key}"

    def _serialize(self, data: Any) -> str:
        """Serialize data for storage."""
        return json.dumps(data, default=str)

    def _deserialize(self, data: str) -> Any:
        """Deserialize data from storage."""
        return json.loads(data) if data else None

    def set(self, prefix: str, key: str, value: Any, ttl: Optional[int] = None):
        """Set a value in the store."""
        serialized = self._serialize(value)

        if self.redis_client:
            redis_key = self._get_key(prefix, key)
            if ttl:
                self.redis_client.setex(redis_key, ttl, serialized)
            else:
                self.redis_client.set(redis_key, serialized)
        else:
            # Memory store
            if prefix not in self.memory_store:
                self.memory_store[prefix] = {}
            self.memory_store[prefix][key] = {
                "value": serialized,
                "expires": datetime.now() + timedelta(seconds=ttl) if ttl else None,
            }

    def get(self, prefix: str, key: str) -> Optional[Any]:
        """Get a value from the store."""
        if self.redis_client:
            redis_key = self._get_key(prefix, key)
            data = self.redis_client.get(redis_key)
            return self._deserialize(data) if data else None
        else:
            # Memory store
            if prefix not in self.memory_store or key not in self.memory_store[prefix]:
                return None

            item = self.memory_store[prefix][key]
            if item["expires"] and datetime.now() > item["expires"]:
                del self.memory_store[prefix][key]
                return None

            return self._deserialize(item["value"])

    def delete(self, prefix: str, key: str):
        """Delete a value from the store."""
        if self.redis_client:
            redis_key = self._get_key(prefix, key)
            self.redis_client.delete(redis_key)
        else:
            # Memory store
            if prefix in self.memory_store and key in self.memory_store[prefix]:
                del self.memory_store[prefix][key]

    def get_all(self, prefix: str) -> Dict[str, Any]:
        """Get all values for a prefix."""
        if self.redis_client:
            pattern = self._get_key(prefix, "*")
            keys = self.redis_client.keys(pattern)
            result = {}
            for key in keys:
                # Extract the actual key from the full Redis key
                actual_key = key.decode("utf-8").split(":")[-1]
                data = self.redis_client.get(key)
                if data:
                    result[actual_key] = self._deserialize(data)
            return result
        else:
            # Memory store
            if prefix not in self.memory_store:
                return {}

            result = {}
            for key, item in self.memory_store[prefix].items():
                if not item["expires"] or datetime.now() <= item["expires"]:
                    result[key] = self._deserialize(item["value"])
            return result

    def exists(self, prefix: str, key: str) -> bool:
        """Check if a key exists."""
        return self.get(prefix, key) is not None


class GameRoomManager:
    """Manages game rooms using state manager."""

    def __init__(self):
        self.state = StateManager()

    def create_room(self, name: str, game_type: str, max_players: int = 4) -> str:
        """Create a new game room."""
        room_id = str(uuid.uuid4())[:8]
        room_data = {
            "id": room_id,
            "name": name,
            "game_type": game_type,
            "max_players": max_players,
            "players": [],
            "status": "waiting",
            "created_at": datetime.now().isoformat(),
            "started_at": None,
        }

        self.state.set("game_rooms", room_id, room_data, ttl=3600)  # 1 hour TTL
        return room_id

    def get_room(self, room_id: str) -> Optional[Dict]:
        """Get a game room."""
        return self.state.get("game_rooms", room_id)

    def get_all_rooms(self) -> List[Dict]:
        """Get all active game rooms."""
        rooms = self.state.get_all("game_rooms")
        return list(rooms.values())

    def join_room(self, room_id: str, player_name: str) -> Optional[str]:
        """Join a game room."""
        room = self.get_room(room_id)
        if not room:
            return None

        if len(room["players"]) >= room["max_players"]:
            return None

        player_id = str(uuid.uuid4())[:8]
        player = {
            "id": player_id,
            "name": player_name,
            "score": 0,
            "joined_at": datetime.now().isoformat(),
        }

        room["players"].append(player)
        self.state.set("game_rooms", room_id, room, ttl=3600)
        return player_id

    def leave_room(self, room_id: str, player_id: str) -> bool:
        """Leave a game room."""
        room = self.get_room(room_id)
        if not room:
            return False

        room["players"] = [p for p in room["players"] if p["id"] != player_id]

        if not room["players"]:
            # Delete empty room
            self.state.delete("game_rooms", room_id)
        else:
            self.state.set("game_rooms", room_id, room, ttl=3600)

        return True

    def start_game(self, room_id: str) -> bool:
        """Start a game in a room."""
        room = self.get_room(room_id)
        if not room or len(room["players"]) < 2:
            return False

        room["status"] = "playing"
        room["started_at"] = datetime.now().isoformat()
        self.state.set("game_rooms", room_id, room, ttl=3600)
        return True

    def update_player_score(self, room_id: str, player_id: str, score: int):
        """Update a player's score."""
        room = self.get_room(room_id)
        if not room:
            return

        for player in room["players"]:
            if player["id"] == player_id:
                player["score"] = score
                break

        self.state.set("game_rooms", room_id, room, ttl=3600)


class UserSessionManager:
    """Manages user sessions using state manager."""

    def __init__(self):
        self.state = StateManager()

    def create_session(self, user_id: str, session_data: Dict) -> str:
        """Create a new user session."""
        session_id = str(uuid.uuid4())
        session_data.update(
            {
                "id": session_id,
                "user_id": user_id,
                "created_at": datetime.now().isoformat(),
                "last_activity": datetime.now().isoformat(),
            }
        )

        self.state.set("user_sessions", session_id, session_data, ttl=86400)  # 24 hours
        return session_id

    def get_session(self, session_id: str) -> Optional[Dict]:
        """Get a user session."""
        return self.state.get("user_sessions", session_id)

    def update_session(self, session_id: str, updates: Dict):
        """Update a user session."""
        session = self.get_session(session_id)
        if session:
            session.update(updates)
            session["last_activity"] = datetime.now().isoformat()
            self.state.set("user_sessions", session_id, session, ttl=86400)

    def delete_session(self, session_id: str):
        """Delete a user session."""
        self.state.delete("user_sessions", session_id)

    def get_user_sessions(self, user_id: str) -> List[Dict]:
        """Get all sessions for a user."""
        all_sessions = self.state.get_all("user_sessions")
        return [
            session
            for session in all_sessions.values()
            if session.get("user_id") == user_id
        ]


# Global instances
state_manager = StateManager()
game_room_manager = GameRoomManager()
user_session_manager = UserSessionManager()
