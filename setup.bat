@echo off
echo.
echo ========================================
echo   Ultimate Tutoring Program Setup
echo ========================================
echo.
echo Installing required Python packages...
echo.

python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo To start the tutor, run: run.bat
echo Or type: streamlit run tutor.py
echo.
echo The app will open at: http://localhost:8501
echo.
pause

