#!/bin/bash
# ═══════════════════════════════════════════════════════════════
# 🔄 Panda Bot Restart Script - إعادة تشغيل البوت بأمان
# ═══════════════════════════════════════════════════════════════

echo "🐼 Panda Giveaways Bot - Restart Script"
echo "═══════════════════════════════════════════════════════"

# إيقاف العمليات الحالية
echo "🛑 Stopping current processes..."
pkill -f "python.*panda_giveaways_bot.py" 2>/dev/null
pkill -f "python.*app.py" 2>/dev/null
sleep 2

# فحص المنافذ
echo "🔍 Checking ports..."
if lsof -ti:8080 >/dev/null 2>&1; then
    echo "⚠️ Port 8080 still in use, force killing..."
    kill -9 $(lsof -ti:8080) 2>/dev/null
fi

if lsof -ti:8081 >/dev/null 2>&1; then
    echo "⚠️ Port 8081 still in use, force killing..."
    kill -9 $(lsof -ti:8081) 2>/dev/null
fi

# انتظار قصير
sleep 3

# فحص صحة النظام
echo "🔍 Running health check..."
python3 check_bot_status.py

echo ""
echo "🚀 Starting services..."

# تشغيل Flask server (في الخلفية)
echo "🌐 Starting Flask web server..."
nohup python3 app.py > flask.log 2>&1 &
FLASK_PID=$!
echo "   Flask PID: $FLASK_PID"

# انتظار تشغيل Flask
sleep 3

# تشغيل البوت
echo "🤖 Starting Telegram Bot..."
nohup python3 panda_giveaways_bot.py > bot.log 2>&1 &
BOT_PID=$!
echo "   Bot PID: $BOT_PID"

# انتظار تشغيل البوت
sleep 5

# فحص حالة الخدمات
echo ""
echo "🔍 Verifying services..."

# فحص Flask
if curl -s http://localhost:8080/health >/dev/null 2>&1; then
    echo "✅ Flask server (port 8080) - Running"
else
    echo "❌ Flask server (port 8080) - Not responding"
fi

# فحص Bot verification server
if curl -s http://localhost:8081/ >/dev/null 2>&1; then
    echo "✅ Bot verification server (port 8081) - Running"
else
    echo "❌ Bot verification server (port 8081) - Not responding"
fi

echo ""
echo "📋 Process Status:"
echo "Flask PID: $FLASK_PID"
echo "Bot PID: $BOT_PID"

echo ""
echo "🎯 Useful commands:"
echo "   Monitor Flask: tail -f flask.log"
echo "   Monitor Bot: tail -f bot.log"
echo "   Check health: python3 check_bot_status.py"
echo "   Stop all: pkill -f 'python.*panda'"

echo ""
echo "✅ Restart completed!"
echo "═══════════════════════════════════════════════════════"