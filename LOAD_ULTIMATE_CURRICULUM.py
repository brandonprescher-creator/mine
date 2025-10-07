"""
Ultimate Curriculum Loader - Load EVERYTHING!
This loads all subjects and expansions
"""

import os
from database import init_database
from MASSIVE_ELA_CURRICULUM import seed_massive_ela_curriculum
from MASSIVE_MATH_CURRICULUM import seed_massive_math_curriculum
from MASSIVE_SCIENCE_CURRICULUM import seed_massive_science_curriculum
from MASSIVE_SOCIAL_STUDIES_CURRICULUM import seed_massive_social_studies_curriculum
from MASSIVE_ARTS_CURRICULUM import seed_massive_arts_curriculum
from SCIENCE_EXPERIMENTS_CURRICULUM import seed_science_experiments_curriculum
from EXPAND_MATH_LESSONS import expand_math_lessons


def load_ultimate_curriculum():
    """Load the ULTIMATE comprehensive curriculum."""

    print("=" * 60)
    print("LOADING ULTIMATE HOMESCHOOL CURRICULUM")
    print("=" * 60)

    # Remove existing database
    if os.path.exists("tutor_app.db"):
        os.remove("tutor_app.db")
        print("Removed existing database")

    # Initialize database
    print("\nInitializing database...")
    init_database()

    # Load all base curricula
    print("\n[1/7] Loading English Language Arts...")
    seed_massive_ela_curriculum()

    print("\n[2/7] Loading Mathematics...")
    seed_massive_math_curriculum()

    print("\n[3/7] Loading Science...")
    seed_massive_science_curriculum()

    print("\n[4/7] Loading Social Studies...")
    seed_massive_social_studies_curriculum()

    print("\n[5/7] Loading Arts & Music...")
    seed_massive_arts_curriculum()

    print("\n[6/7] Loading Science Experiments...")
    seed_science_experiments_curriculum()

    print("\n[7/7] Expanding Math with MORE lessons...")
    expand_math_lessons()

    print("\n" + "=" * 60)
    print("ULTIMATE CURRICULUM LOADED SUCCESSFULLY!")
    print("=" * 60)

    print("\nYOUR DAUGHTERS NOW HAVE ACCESS TO:")
    print("  - English Language Arts: 44 topics, 55+ lessons")
    print("  - Mathematics: 40 topics, 120+ lessons (EXPANDED!)")
    print("  - Science: 40 topics, 75+ lessons")
    print("  - Social Studies: 40 topics, 79+ lessons")
    print("  - Arts & Music: 25 topics, 35+ lessons (NEW!)")
    print("  - Science Experiments: 8 topics, 30+ hands-on experiments (NEW!)")
    print("\nTOTAL: 197+ TOPICS | 400+ LESSONS!")
    print("All organized by grade levels K-8!")
    print("\nReady for your homeschool daughters!")


if __name__ == "__main__":
    load_ultimate_curriculum()
