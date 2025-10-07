"""
Script to initialize the database with the massive ELA curriculum
"""

from database import init_database
from MASSIVE_ELA_CURRICULUM import seed_massive_ela_curriculum


def init_and_seed():
    """Initialize database and seed with massive ELA curriculum."""

    print("Initializing database...")
    init_database()

    print("Seeding MASSIVE ELA curriculum...")
    seed_massive_ela_curriculum()

    print("Database initialized and seeded successfully!")


if __name__ == "__main__":
    init_and_seed()
