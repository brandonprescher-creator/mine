"""
ULTIMATE MASTER LOADER
Initializes and seeds the complete educational platform
"""

import os
from database import init_database
from database_parent_features import init_parent_dashboard_tables
from LOAD_ULTIMATE_CURRICULUM import load_ultimate_curriculum
from NEW_SUBJECTS_CURRICULUM import seed_all_new_subjects
from COMPLETE_NEW_SUBJECTS_LESSONS import add_all_comprehensive_lessons
from UTAH_LOCAL_CURRICULUM import seed_utah_curriculum


def load_complete_platform():
    """Load the entire educational platform from scratch"""
    print("\n" + "="*80)
    print("🚀 LOADING THE ULTIMATE HOMESCHOOL PLATFORM")
    print("="*80 + "\n")
    
    # Step 1: Initialize core database
    print("📊 Step 1: Initializing core database...")
    init_database()
    print("✅ Core database initialized!\n")
    
    # Step 2: Initialize parent dashboard tables
    print("👨‍👩‍👧‍👧 Step 2: Initializing Parent Dashboard tables...")
    init_parent_dashboard_tables()
    print("✅ Parent Dashboard tables created!\n")
    
    # Step 3: Load massive core curriculum
    print("📚 Step 3: Loading massive core curriculum...")
    print("   (ELA, Math, Science, Social Studies, Arts, Experiments)")
    load_ultimate_curriculum()
    print("✅ Core curriculum loaded!\n")
    
    # Step 4: Add 50+ new subjects
    print("🎓 Step 4: Adding 50+ revolutionary new subjects...")
    seed_all_new_subjects()
    print("✅ New subjects added!\n")
    
    # Step 5: Add comprehensive lessons to new subjects
    print("📝 Step 5: Adding comprehensive lessons to new subjects...")
    add_all_comprehensive_lessons()
    print("✅ Comprehensive lessons added!\n")
    
    # Step 6: Add Utah-specific content
    print("🏔️ Step 6: Adding Utah & Cottonwood Heights local content...")
    seed_utah_curriculum()
    print("✅ Local curriculum added!\n")
    
    # Final summary
    print("\n" + "="*80)
    print("🎉 COMPLETE PLATFORM LOADED SUCCESSFULLY!")
    print("="*80)
    print("\nYour Ultimate Homeschool Platform now includes:")
    print("  ✅ Complete K-8 Core Curriculum (ELA, Math, Science, Social Studies)")
    print("  ✅ Arts & Music Education")
    print("  ✅ Science Experiments (30+ hands-on experiments)")
    print("  ✅ 50+ Revolutionary New Subjects:")
    print("      • 10 Future-Ready Technology subjects")
    print("      • 12 Life & Practical Skills subjects")
    print("      • 10 Creative & Critical Thinking subjects")
    print("      • 8 Interdisciplinary Thematic Units")
    print("      • 10 Advanced Specialized subjects")
    print("  ✅ Utah-Specific Local Content")
    print("  ✅ Parent Dashboard with Mission Control")
    print("  ✅ Sister Quest Collaborative System")
    print("  ✅ Interest-Based Personalization")
    print("  ✅ Reward & Achievement System")
    print("\n📈 TOTAL SUBJECTS: 60+")
    print("📈 TOTAL TOPICS: 300+")
    print("📈 TOTAL LESSONS: 600+")
    print("\n🎊 THIS IS THE MOST COMPREHENSIVE HOMESCHOOL PLATFORM EVER CREATED!")
    print("="*80 + "\n")


if __name__ == "__main__":
    # Check if database already exists
    if os.path.exists("tutor_app.db"):
        response = input("⚠️  Database already exists. Delete and rebuild? (yes/no): ")
        if response.lower() == "yes":
            os.remove("tutor_app.db")
            print("🗑️ Removed existing database\n")
        else:
            print("❌ Cancelled. Existing database preserved.")
            exit()
    
    load_complete_platform()

