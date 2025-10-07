import os
import io
from typing import Tuple, Optional
import PyPDF2
import pdfplumber
from docx import Document
from PIL import Image
import pytesseract


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract text from PDF file."""
    text = ""

    # Try pdfplumber first (better for complex PDFs)
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n\n"
    except Exception as e:
        print(f"pdfplumber failed: {e}, trying PyPDF2...")

        # Fallback to PyPDF2
        try:
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n\n"
        except Exception as e:
            print(f"PyPDF2 also failed: {e}")
            return ""

    return text.strip()


def extract_text_from_word(file_bytes: bytes) -> str:
    """Extract text from Word document."""
    try:
        doc = Document(io.BytesIO(file_bytes))
        text = "\n\n".join(
            [paragraph.text for paragraph in doc.paragraphs if paragraph.text]
        )
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from Word: {e}")
        return ""


def extract_text_from_image(file_bytes: bytes) -> str:
    """Extract text from image using OCR."""
    try:
        image = Image.open(io.BytesIO(file_bytes))
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error performing OCR on image: {e}")
        return "OCR failed. Make sure tesseract is installed on your system."


def extract_text_from_text_file(file_bytes: bytes) -> str:
    """Extract text from plain text file."""
    try:
        text = file_bytes.decode("utf-8")
        return text.strip()
    except UnicodeDecodeError:
        try:
            text = file_bytes.decode("latin-1")
            return text.strip()
        except Exception as e:
            print(f"Error reading text file: {e}")
            return ""


def process_uploaded_file(filename: str, file_bytes: bytes) -> Tuple[str, str]:
    """
    Process uploaded file and extract text.
    Returns (file_type, extracted_text)
    """
    file_extension = os.path.splitext(filename)[1].lower()

    if file_extension == ".pdf":
        text = extract_text_from_pdf(file_bytes)
        return ("pdf", text)

    elif file_extension in [".docx", ".doc"]:
        text = extract_text_from_word(file_bytes)
        return ("word", text)

    elif file_extension in [".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".gif"]:
        text = extract_text_from_image(file_bytes)
        return ("image", text)

    elif file_extension in [".txt", ".text"]:
        text = extract_text_from_text_file(file_bytes)
        return ("text", text)

    else:
        return ("unknown", f"Unsupported file type: {file_extension}")
