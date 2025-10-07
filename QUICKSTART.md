# 🚀 Quick Start Guide

## Windows Users

### First Time Setup:
1. Make sure Python 3.8+ is installed
2. Double-click `setup.bat`
3. Wait for installation to complete

### Running the App:
Double-click `run.bat`

## Mac/Linux Users

### First Time Setup:
1. Make sure Python 3.8+ is installed
2. Open Terminal in this folder
3. Run: `chmod +x setup.sh run.sh`
4. Run: `./setup.sh`

### Running the App:
Run: `./run.sh`

## Alternative Method (All Systems)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run tutor.py
```

## First Time Using the App

1. The app opens automatically in your browser at http://localhost:8501
2. Click "📚 Subjects" in the sidebar
3. Choose a subject (try Mathematics!)
4. Select "Division Mastery" to see all 10 division methods
5. Click "Learn" on any lesson
6. Toggle to "Practice" to try problems with instant feedback!

## Tips

- 📤 **Upload files**: Click "Upload Files" to add PDF, Word, or images
- 🔍 **Search**: Use the search feature to find any topic quickly
- ❓ **Ask questions**: The "Ask Tutor" feature searches lessons + online resources
- 📊 **Track progress**: View your achievements and mastery levels in "Progress"
- 🌐 **Offline capable**: Works without internet (online resources require connection)

## Troubleshooting

**Problem**: ModuleNotFoundError
**Solution**: Run `setup.bat` (Windows) or `./setup.sh` (Mac/Linux)

**Problem**: Port already in use
**Solution**: Close other applications using port 8501, or run:
```bash
streamlit run tutor.py --server.port 8502
```

**Problem**: OCR not working on images
**Solution**: Install Tesseract OCR:
- Windows: https://github.com/UB-Mannheim/tesseract/wiki
- Mac: `brew install tesseract`
- Linux: `sudo apt-get install tesseract-ocr`

## Need Help?

Check the full README.md for detailed documentation.

---

**Happy Learning! 🎓**

