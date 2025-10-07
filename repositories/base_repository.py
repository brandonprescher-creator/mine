"""
Base repository class with common database operations
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Any, TypeVar, Generic
from database_enhanced import DatabaseManager

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):
    """Base repository class with common operations."""

    def __init__(self):
        self.db = DatabaseManager()

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]:
        """Get entity by ID."""
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        """Get all entities."""
        pass

    @abstractmethod
    def create(self, data: Dict[str, Any]) -> T:
        """Create new entity."""
        pass

    @abstractmethod
    def update(self, id: int, data: Dict[str, Any]) -> Optional[T]:
        """Update entity."""
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        """Delete entity."""
        pass

    def exists(self, id: int) -> bool:
        """Check if entity exists."""
        return self.get_by_id(id) is not None

    def count(self) -> int:
        """Get total count of entities."""
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
            return cursor.fetchone()[0]

    def get_paginated(self, page: int = 1, per_page: int = 20) -> Dict[str, Any]:
        """Get paginated results."""
        offset = (page - 1) * per_page

        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM {self.table_name} LIMIT ? OFFSET ?", (per_page, offset)
            )
            rows = cursor.fetchall()

            total = self.count()

            return {
                "items": [dict(row) for row in rows],
                "total": total,
                "page": page,
                "per_page": per_page,
                "pages": (total + per_page - 1) // per_page,
            }
