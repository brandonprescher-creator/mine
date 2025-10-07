"""
Script to clear and reseed the database with the MASSIVE ELA curriculum
"""

import sqlite3
import os
from MASSIVE_ELA_CURRICULUM import seed_massive_ela_curriculum

def clear_and_reseed():
    """Clear the database and reseed with massive ELA curriculum."""
    
    # Remove existing database
    if os.path.exists('tutor.db'):
        os.remove('tutor.db')
        print("Removed existing database")
    
    # Create new database and seed
    print("Seeding MASSIVE ELA curriculum...")
    seed_massive_ela_curriculum()
    print("MASSIVE ELA curriculum seeded successfully!")

if __name__ == "__main__":
    clear_and_reseed()
