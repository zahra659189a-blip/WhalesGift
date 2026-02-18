#!/bin/bash
# Render Start Script - Backend API Server only (Frontend on Vercel)

echo "🐼 Starting Arab ton gifts Backend Services..."

# حذف virtualenv القديم إذا كان موجوداً لضمان استخدام Python الصحيح
if [ -d ".venv" ]; then
    echo "🧹 Cleaning old virtual environment..."
    rm -rf .venv
fi

# Start Flask web server (البوت هيشتغل تلقائياً من app.py)
echo "🌐 Starting Flask API Server on port $PORT..."
echo "📱 Frontend running on: https://arabton.vercel.app"
exec gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120 --access-logfile - --error-logfile -
