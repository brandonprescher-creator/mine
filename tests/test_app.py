"""
Basic smoke tests for Ultimate Tutor
"""

import pytest
import os
import tempfile
from app_factory import create_app_only
from database import init_database


@pytest.fixture
def app():
    """Create test app."""
    # Create temporary database
    db_fd, db_path = tempfile.mkstemp()

    app = create_app_only()
    app.config.update(
        {
            "TESTING": True,
            "DATABASE_URL": db_path,
        }
    )

    with app.app_context():
        init_database()

    yield app

    # Cleanup
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()


def test_home_page(client):
    """Test home page loads."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"ULTIMATE" in response.data


def test_subjects_page(client):
    """Test subjects page loads."""
    response = client.get("/subjects")
    assert response.status_code == 200
    assert b"Subjects" in response.data


def test_upload_page(client):
    """Test upload page loads."""
    response = client.get("/uploads/upload")
    assert response.status_code == 200


def test_api_upload_no_file(client):
    """Test upload API without file."""
    response = client.post("/uploads/api/upload/worksheet")
    assert response.status_code == 400
    assert b"No file provided" in response.data


def test_health_check(client):
    """Test basic health check."""
    response = client.get("/")
    assert response.status_code == 200
