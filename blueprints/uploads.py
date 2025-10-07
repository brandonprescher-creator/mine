"""
Uploads blueprint
Handles secure file uploads and worksheet processing
"""

from flask import Blueprint, render_template, request, jsonify
from services.upload_service import UploadService
from worksheet_ai_converter import convert_worksheet_to_lesson

uploads_bp = Blueprint("uploads", __name__)


@uploads_bp.route("/upload")
def upload_page():
    """Upload page."""
    return render_template("upload.html")


@uploads_bp.route("/api/upload/worksheet", methods=["POST"])
def upload_worksheet():
    """Secure worksheet upload endpoint."""
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file provided"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400

        # Use secure upload service
        upload_service = UploadService()
        file_info = upload_service.save_file(file)

        # Process the worksheet
        try:
            lesson_data = convert_worksheet_to_lesson(file_info["file_path"])

            upload_service.delete_file(file_info["filename"])

            return jsonify(
                {
                    "success": True,
                    "message": "Worksheet uploaded and processed successfully!",
                    "lesson_data": lesson_data,
                }
            )

        except Exception as e:
            # Clean up uploaded file if processing fails
            upload_service.delete_file(file_info["filename"])
            return jsonify({"error": f"Failed to process worksheet: {str(e)}"}), 500

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Upload failed: {str(e)}"}), 500


@uploads_bp.route("/api/upload/status/<filename>")
def upload_status(filename):
    """Get upload status."""
    upload_service = UploadService()
    file_info = upload_service.get_file_info(filename)

    if not file_info:
        return jsonify({"error": "File not found"}), 404

    return jsonify({"file_info": file_info})
