#!/bin/bash
# Render Start Script - Backend API Server only (Frontend on Vercel)

echo "🐼 Starting Arab ton gifts Backend Services..."

# Start Flask web server (البوت هيشتغل تلقائياً من app.py)
echo "🌐 Starting Flask API Server on port $PORT..."
echo "📱 Frontend running on: https://arabton.vercel.app"
exec python app.py
