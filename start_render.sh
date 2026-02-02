#!/bin/bash
# Render Start Script - تشغيل البوت والسيرفر معاً

echo "🐼 Starting Panda Giveaways Services..."

# Start Telegram Bot in background (with nohup to keep it running)
echo "🤖 Starting Telegram Bot..."
nohup python panda_giveaways_bot.py > bot.log 2>&1 &
BOT_PID=$!
echo "✅ Bot started with PID: $BOT_PID"

# Wait for bot to initialize
sleep 2

# Start Flask web server (this will block and keep the container alive)
echo "🌐 Starting Flask Server on port $PORT..."
exec gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --access-logfile - --error-logfile -
