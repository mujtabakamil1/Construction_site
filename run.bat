@echo off
REM PCS Puri Construction Services - Windows Startup Script

echo.
echo ========================================
echo PCS Puri Construction Services
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if venv exists, if not create it
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created.
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install/upgrade dependencies
echo.
echo Installing dependencies...
pip install -r requirements.txt

REM Run Flask app
echo.
echo Starting Flask application...
echo.
echo ========================================
echo Server running at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python app.py

pause
