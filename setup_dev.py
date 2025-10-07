"""
Development setup script
Sets up the development environment
"""

import os
import subprocess
import sys


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False


def setup_development():
    """Set up development environment."""
    print("🚀 Setting up Ultimate Tutor Development Environment")
    print("=" * 60)

    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        return False

    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

    # Install dependencies
    if not run_command(
        "pip install -r requirements_flask.txt", "Installing dependencies"
    ):
        return False

    # Create .env file if it doesn't exist
    if not os.path.exists(".env"):
        if os.path.exists("env.example"):
            run_command("copy env.example .env", "Creating .env file")
            print("📝 Please edit .env file with your configuration")
        else:
            print("⚠️  No env.example found, creating basic .env")
            with open(".env", "w") as f:
                f.write("FLASK_ENV=development\n")
                f.write("SECRET_KEY=dev-secret-key-change-in-production\n")

    # Create uploads directory
    os.makedirs("uploads", exist_ok=True)
    print("✅ Created uploads directory")

    # Initialize database
    if not run_command("python cli.py init-db", "Initializing database"):
        return False

    # Seed curriculum
    if not run_command("python cli.py seed-massive-curriculum", "Seeding curriculum"):
        return False

    print("\n" + "=" * 60)
    print("🎉 Development environment setup complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Edit .env file with your configuration")
    print("2. Run: python cli.py run")
    print("3. Visit: http://localhost:5001")
    print("\nFor testing:")
    print("1. Run: pytest tests/")
    print("2. Run: black .")
    print("3. Run: ruff check .")

    return True


if __name__ == "__main__":
    setup_development()
