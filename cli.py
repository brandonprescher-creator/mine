"""
CLI management commands for Ultimate Tutor
Handles database initialization and seeding
"""

import click
import os
from flask.cli import with_appcontext
from database import init_database
from config import get_config


@click.group()
def cli():
    """Ultimate Tutor management commands."""
    pass


@cli.command()
@click.option(
    "--force", is_flag=True, help="Force reinitialize even if database exists"
)
def init_db(force=False):
    """Initialize the database."""
    config = get_config()

    if os.path.exists(config.DATABASE_URL) and not force:
        click.echo(
            f"Database {config.DATABASE_URL} already exists. Use --force to reinitialize."
        )
        return

    if force and os.path.exists(config.DATABASE_URL):
        os.remove(config.DATABASE_URL)
        click.echo(f"Removed existing database {config.DATABASE_URL}")

    click.echo("Initializing database...")
    init_database()
    click.echo("Database initialized successfully!")


@cli.command()
@click.option("--force", is_flag=True, help="Force reseed even if data exists")
def seed_curriculum(force=False):
    """Seed the database with curriculum data."""
    from curriculum_data import seed_curriculum

    if not force:
        from database import get_all_subjects

        existing_subjects = get_all_subjects()
        if existing_subjects:
            click.echo("Curriculum already exists. Use --force to reseed.")
            return

    click.echo("Seeding curriculum...")
    seed_curriculum()
    click.echo("Curriculum seeded successfully!")


@cli.command()
def seed_massive_curriculum():
    """Seed the database with MASSIVE curriculum."""
    from LOAD_ULTIMATE_CURRICULUM import load_ultimate_curriculum

    click.echo("Loading MASSIVE curriculum...")
    load_ultimate_curriculum()
    click.echo("MASSIVE curriculum loaded successfully!")


@cli.command()
def check_db():
    """Check database status and show statistics."""
    from database import get_connection

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Check tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()

        click.echo("Database Status:")
        click.echo(f"Tables: {len(tables)}")

        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            click.echo(f"  {table_name}: {count} records")

        conn.close()
        click.echo("Database is healthy!")

    except Exception as e:
        click.echo(f"Database error: {e}")


@cli.command()
@click.option("--port", default=5001, help="Port to run on")
@click.option("--host", default="0.0.0.0", help="Host to bind to")
def run(port=5001, host="0.0.0.0"):
    """Run the development server."""
    from app_factory import create_app

    app, socketio = create_app()
    socketio.run(app, host=host, port=port, debug=True)


@cli.command()
def test():
    """Run tests."""
    import subprocess

    subprocess.run(["pytest", "tests/", "-v"])


@cli.command()
def format_code():
    """Format code with black."""
    import subprocess

    subprocess.run(["black", "."])


@cli.command()
def lint():
    """Lint code with ruff."""
    import subprocess

    subprocess.run(["ruff", "check", "."])


@cli.command()
def type_check():
    """Type check with mypy."""
    import subprocess

    subprocess.run(["mypy", "."])


@cli.command()
def install_hooks():
    """Install pre-commit hooks."""
    import subprocess

    subprocess.run(["pre-commit", "install"])


@cli.command()
def init_parent_features():
    """Initialize Parent Dashboard database tables."""
    from database_parent_features import init_parent_dashboard_tables

    click.echo("Initializing Parent Dashboard tables...")
    init_parent_dashboard_tables()
    click.echo("Parent Dashboard tables created successfully!")


@cli.command()
def seed_new_subjects():
    """Seed the 50+ new revolutionary subjects."""
    from NEW_SUBJECTS_CURRICULUM import seed_all_new_subjects

    click.echo("Seeding 50+ new subjects...")
    seed_all_new_subjects()
    click.echo("New subjects seeded successfully!")


@cli.command()
@click.option("--name", prompt="Student name", help="Student's full name")
@click.option("--grade", prompt="Grade level", help="E.g., '4th Grade'")
@click.option("--age", prompt="Age", type=int, help="Student's age")
@click.option(
    "--interests", prompt="Interests (comma-separated)", help="E.g., 'horses,art,science'"
)
def create_student(name, grade, age, interests):
    """Create a new student profile."""
    from database_parent_features import create_student_profile
    import random

    student_id = f"student_{random.randint(1000, 9999)}"
    interest_list = [i.strip() for i in interests.split(",")]

    profile_id = create_student_profile(
        student_id=student_id,
        name=name,
        grade_level=grade,
        age=age,
        interests=interest_list,
    )

    click.echo(f"Student profile created! ID: {student_id}")


@cli.command()
def test_certificates():
    """Test certificate generation."""
    from certificate_generator import CertificateGenerator

    gen = CertificateGenerator()

    click.echo("Generating test certificates...")

    cert1 = gen.generate_certificate("Test Student", "Complete 10 Math Lessons")
    click.echo(f"Generated: {cert1}")

    cert2 = gen.generate_mastery_certificate("Test Student", "Mathematics", 15)
    click.echo(f"Generated: {cert2}")

    cert3 = gen.generate_sister_quest_certificate(
        "Student 1", "Student 2", "The Amazing Science Project"
    )
    click.echo(f"Generated: {cert3}")

    click.echo("All test certificates generated successfully!")


@cli.command()
def load_everything():
    """Load the complete platform - all subjects, lessons, and features."""
    from LOAD_EVERYTHING_ULTIMATE import load_complete_platform
    
    click.echo("Loading complete Ultimate Homeschool Platform...")
    load_complete_platform()


@cli.command()
def add_comprehensive_lessons():
    """Add comprehensive lessons to new subjects."""
    from COMPLETE_NEW_SUBJECTS_LESSONS import add_all_comprehensive_lessons
    
    click.echo("Adding comprehensive lessons...")
    add_all_comprehensive_lessons()
    click.echo("Comprehensive lessons added!")


@cli.command()
def add_utah_content():
    """Add Utah and Cottonwood Heights specific content."""
    from UTAH_LOCAL_CURRICULUM import seed_utah_curriculum
    
    click.echo("Adding Utah-specific curriculum...")
    seed_utah_curriculum()
    click.echo("Utah content added!")


@cli.command()
def generate_practice_problems():
    """Generate practice problems for all lessons."""
    from GENERATE_ALL_PRACTICE_PROBLEMS import generate_practice_for_all_lessons
    
    click.echo("Generating practice problems for all lessons...")
    generate_practice_for_all_lessons()
    click.echo("Practice problems generated!")


if __name__ == "__main__":
    cli()
