#!/bin/bash
# Render Start Script - Backend API Server only (Frontend on Vercel)

echo "🎁 Starting Arab Ton Gifts Backend Services..."

# Start Flask web server (البوت هيشتغل تلقائياً من app.py)
echo "🌐 Starting Flask API Server on port $PORT..."
echo "📱 Frontend running on: https://whalesgift.vercel.app"
echo "⚠️ Using 1 worker to avoid bot conflicts"
exec gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120 --access-logfile - --error-logfile -
