#!/bin/bash
# Render Start Script - تشغيل البوت والسيرفر معاً

echo "🐼 Starting Panda Giveaways Services..."

# Start Flask web server in background
echo "🌐 Starting Flask Server on port $PORT..."
gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120 &
WEB_PID=$!

# Wait for web server to start
sleep 3

# Start Telegram Bot in background
echo "🤖 Starting Telegram Bot..."
python panda_giveaways_bot.py &
BOT_PID=$!

echo "✅ All services started!"
echo "   Web Server PID: $WEB_PID"
echo "   Bot PID: $BOT_PID"

# Keep script running and monitor processes
wait -n

# If any process exits, kill the other and exit
kill $WEB_PID $BOT_PID 2>/dev/null
exit $?
