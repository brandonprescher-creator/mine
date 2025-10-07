"""
Secure file upload service
Handles file validation, sanitization, and storage
"""

import os
import uuid
from werkzeug.utils import secure_filename
from typing import Optional, List
from config import get_config


class UploadService:
    """Handles secure file uploads."""

    def __init__(self):
        self.config = get_config()
        self.upload_folder = self.config.UPLOAD_FOLDER
        self.allowed_extensions = self.config.ALLOWED_EXTENSIONS
        self.max_size = self.config.MAX_CONTENT_LENGTH

        # Ensure upload directory exists
        os.makedirs(self.upload_folder, exist_ok=True)

    def is_allowed_file(self, filename: str) -> bool:
        """Check if file extension is allowed."""
        if not filename or "." not in filename:
            return False

        extension = filename.rsplit(".", 1)[1].lower()
        return extension in self.allowed_extensions

    def is_safe_filename(self, filename: str) -> bool:
        """Check if filename is safe (no path traversal)."""
        if not filename:
            return False

        # Check for path traversal attempts
        if ".." in filename or "/" in filename or "\\" in filename:
            return False

        # Check for dangerous characters
        dangerous_chars = ["<", ">", ":", '"', "|", "?", "*"]
        if any(char in filename for char in dangerous_chars):
            return False

        return True

    def generate_unique_filename(self, original_filename: str) -> str:
        """Generate a unique, secure filename."""
        if not self.is_safe_filename(original_filename):
            raise ValueError("Unsafe filename detected")

        # Get secure filename
        secure_name = secure_filename(original_filename)

        # Generate unique ID
        unique_id = str(uuid.uuid4())[:8]

        # Split filename and extension
        if "." in secure_name:
            name, ext = secure_name.rsplit(".", 1)
            return f"{name}_{unique_id}.{ext}"
        else:
            return f"{secure_name}_{unique_id}"

    def save_file(self, file, custom_filename: Optional[str] = None) -> dict:
        """Save uploaded file securely."""
        if not file or not file.filename:
            raise ValueError("No file provided")

        # Validate file
        if not self.is_allowed_file(file.filename):
            raise ValueError(
                f"File type not allowed. Allowed: {', '.join(self.allowed_extensions)}"
            )

        # Check file size
        file.seek(0, 2)  # Seek to end
        file_size = file.tell()
        file.seek(0)  # Reset to beginning

        if file_size > self.max_size:
            raise ValueError(f"File too large. Max size: {self.max_size} bytes")

        # Generate secure filename
        if custom_filename:
            filename = self.generate_unique_filename(custom_filename)
        else:
            filename = self.generate_unique_filename(file.filename)

        # Save file
        file_path = os.path.join(self.upload_folder, filename)
        file.save(file_path)

        return {
            "filename": filename,
            "original_filename": file.filename,
            "file_path": file_path,
            "file_size": file_size,
            "content_type": file.content_type,
        }

    def delete_file(self, filename: str) -> bool:
        """Delete a file from uploads."""
        if not self.is_safe_filename(filename):
            return False

        file_path = os.path.join(self.upload_folder, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False

    def get_file_info(self, filename: str) -> Optional[dict]:
        """Get information about an uploaded file."""
        if not self.is_safe_filename(filename):
            return None

        file_path = os.path.join(self.upload_folder, filename)
        if not os.path.exists(file_path):
            return None

        stat = os.stat(file_path)
        return {
            "filename": filename,
            "file_path": file_path,
            "file_size": stat.st_size,
            "created_at": stat.st_ctime,
            "modified_at": stat.st_mtime,
        }
