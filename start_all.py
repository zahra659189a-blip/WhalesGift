"""
🚀 تشغيل البوت والسيرفر معاً
"""
import os
import subprocess
import sys
import threading
import time

def run_bot():
    """تشغيل البوت"""
    print("🤖 Starting Telegram Bot...")
    subprocess.run([sys.executable, "panda_giveaways_bot.py"])

def run_server():
    """تشغيل Flask Server"""
    time.sleep(2)  # انتظر قليلاً حتى يبدأ البوت
    print("🌐 Starting Flask Server...")
    subprocess.run([sys.executable, "app.py"])

if __name__ == "__main__":
    print("=" * 60)
    print("🎁 Arab Ton Gifts - Starting All Services")
    print("=" * 60)
    
    # تشغيل البوت في thread منفصل
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # تشغيل السيرفر في الـ main thread
    run_server()
