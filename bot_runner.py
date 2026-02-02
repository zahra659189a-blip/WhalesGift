"""
🤖 Telegram Bot Wrapper for Background Execution
يشتغل في الخلفية بدون blocking
"""
import subprocess
import sys
import os
import time

def start_bot():
    """تشغيل البوت في subprocess منفصل"""
    try:
        print("🤖 Starting Telegram Bot in background...")
        
        # تشغيل البوت كـ subprocess
        process = subprocess.Popen(
            [sys.executable, "panda_giveaways_bot.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        
        print(f"✅ Bot started with PID: {process.pid}")
        
        # قراءة الـ output في الخلفية
        while True:
            output = process.stdout.readline()
            if output:
                print(f"[BOT] {output.strip()}")
            
            # التحقق من أن البوت لسه شغال
            if process.poll() is not None:
                print(f"⚠️ Bot process ended with code: {process.returncode}")
                break
                
            time.sleep(0.1)
            
    except Exception as e:
        print(f"❌ Error starting bot: {e}")

if __name__ == "__main__":
    start_bot()
