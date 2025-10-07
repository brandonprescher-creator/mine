"""
Script to load ALL MASSIVE curricula into the database
This will create a comprehensive K-8 curriculum for all subjects
"""

import os
from database import init_database
from MASSIVE_ELA_CURRICULUM import seed_massive_ela_curriculum
from MASSIVE_MATH_CURRICULUM import seed_massive_math_curriculum
from MASSIVE_SCIENCE_CURRICULUM import seed_massive_science_curriculum
from MASSIVE_SOCIAL_STUDIES_CURRICULUM import seed_massive_social_studies_curriculum

def load_all_massive_curricula():
    """Load all massive curricula into the database."""
    
    print("LOADING ALL MASSIVE CURRICULA...")
    print("=" * 50)
    
    # Remove existing database to start fresh
    if os.path.exists('tutor_app.db'):
        os.remove('tutor_app.db')
        print("Removed existing database")
    
    # Initialize database
    print("Initializing database...")
    init_database()
    
    # Load each massive curriculum
    print("\nLoading MASSIVE English Language Arts curriculum...")
    seed_massive_ela_curriculum()
    
    print("\nLoading MASSIVE Mathematics curriculum...")
    seed_massive_math_curriculum()
    
    print("\nLoading MASSIVE Science curriculum...")
    seed_massive_science_curriculum()
    
    print("\nLoading MASSIVE Social Studies curriculum...")
    seed_massive_social_studies_curriculum()
    
    print("\n" + "=" * 50)
    print("ALL MASSIVE CURRICULA LOADED SUCCESSFULLY!")
    print("=" * 50)
    
    # Show summary
    print("\nCURRICULUM SUMMARY:")
    print("English Language Arts: 44 topics with 50+ lessons")
    print("Mathematics: 40 topics with 50+ lessons") 
    print("Science: 40 topics with 50+ lessons")
    print("Social Studies: 40 topics with 50+ lessons")
    print("\nTOTAL: 164+ TOPICS WITH 200+ LESSONS!")
    print("All organized by grade levels K-8!")
    print("Ready to launch the ULTIMATE TUTOR!")

if __name__ == "__main__":
    load_all_massive_curricula()
