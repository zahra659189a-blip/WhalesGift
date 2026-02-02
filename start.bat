@echo off
title Panda Giveaways Bot Launcher

echo ╔══════════════════════════════════════════════════╗
echo ║         🐼 PANDA GIVEAWAYS BOT 🐼                ║
echo ║           Windows Launcher Script                ║
echo ╚══════════════════════════════════════════════════╝
echo.

REM التحقق من وجود Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH!
    echo    Please install Python 3.11+ from python.org
    pause
    exit /b
)

echo ✅ Python found

REM التحقق من وجود venv
if not exist "venv\" (
    echo ⚠️  Virtual environment not found!
    echo    Creating virtual environment...
    python -m venv venv
    echo ✅ Virtual environment created
)

REM تفعيل venv
echo 🔄 Activating virtual environment...
call venv\Scripts\activate.bat

REM تثبيت المتطلبات
echo 📦 Installing/Updating requirements...
pip install -r requirements.txt --quiet

REM تشغيل البوت
echo.
echo 🚀 Starting bot...
echo.
python run.py

pause
