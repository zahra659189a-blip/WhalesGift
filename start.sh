#!/bin/bash

# 🐼 Panda Giveaways Bot - Linux/Mac Launcher

echo "╔══════════════════════════════════════════════════╗"
echo "║         🐼 PANDA GIVEAWAYS BOT 🐼                ║"
echo "║          Linux/Mac Launcher Script               ║"
echo "╚══════════════════════════════════════════════════╝"
echo ""

# التحقق من Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed!"
    echo "   Install it with: sudo apt install python3"
    exit 1
fi

echo "✅ Python found"

# التحقق من venv
if [ ! -d "venv" ]; then
    echo "⚠️  Virtual environment not found!"
    echo "   Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

# تفعيل venv
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# تثبيت المتطلبات
echo "📦 Installing/Updating requirements..."
pip install -r requirements.txt --quiet

# تشغيل البوت
echo ""
echo "🚀 Starting bot..."
echo ""
python3 run.py
