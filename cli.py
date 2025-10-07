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


if __name__ == "__main__":
    cli()
