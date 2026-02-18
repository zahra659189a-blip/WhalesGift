#!/usr/bin/env python3
"""
🐼 Panda Giveaways Bot - Runner
Quick start script for the bot
"""

import os
import sys
from pathlib import Path

def check_requirements():
    """التحقق من المتطلبات الأساسية"""
    print("🔍 Checking requirements...")
    
    # التحقق من Python version
    if sys.version_info < (3, 11):
        print("❌ Python 3.11 or higher is required!")
        print(f"   Your version: {sys.version}")
        return False
    
    print("✅ Python version OK")
    
    # التحقق من وجود .env
    if not Path(".env").exists():
        print("⚠️  .env file not found!")
        print("   Creating from .env.example...")
        
        if Path(".env.example").exists():
            import shutil
            shutil.copy(".env.example", ".env")
            print("✅ .env file created")
            print("⚠️  Please edit .env and add your configuration!")
            return False
        else:
            print("❌ .env.example not found!")
            return False
    
    print("✅ .env file found")
    
    # التحقق من المكتبات المطلوبة
    try:
        import telegram
        print("✅ python-telegram-bot installed")
    except ImportError:
        print("❌ python-telegram-bot not installed!")
        print("   Run: pip install -r requirements.txt")
        return False
    
    return True

def load_env():
    """تحميل المتغيرات البيئية"""
    print("📋 Loading environment variables...")
    
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("✅ Environment loaded")
        return True
    except ImportError:
        print("⚠️  python-dotenv not installed")
        print("   Installing...")
        os.system("pip install python-dotenv")
        from dotenv import load_dotenv
        load_dotenv()
        return True

def check_config():
    """التحقق من الإعدادات"""
    print("⚙️  Checking configuration...")
    
    bot_token = os.getenv("BOT_TOKEN")
    bot_username = os.getenv("BOT_USERNAME")
    
    if not bot_token or bot_token == "YOUR_BOT_TOKEN_HERE":
        print("❌ BOT_TOKEN not configured!")
        print("   Please edit .env and add your bot token")
        return False
    
    print(f"✅ Bot Token: {bot_token[:10]}...")
    
    if bot_username:
        print(f"✅ Bot Username: @{bot_username}")
    
    return True

def run_bot():
    """تشغيل البوت"""
    print("\n" + "="*50)
    print("🐼 Starting Panda Giveaways Bot...")
    print("="*50 + "\n")
    
    try:
        import panda_giveaways_bot
        print("✅ Bot module loaded")
        print("🚀 Bot is running!\n")
        panda_giveaways_bot.main()
    except KeyboardInterrupt:
        print("\n⏹️  Bot stopped by user")
    except Exception as e:
        print(f"\n❌ Error running bot: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

def main():
    """Main function"""
    print("""
╔══════════════════════════════════════════════════╗
║         🐼 PANDA GIVEAWAYS BOT 🐼                ║
║              Quick Start Script                  ║
╚══════════════════════════════════════════════════╝
    """)
    
    # التحقق من المتطلبات
    if not check_requirements():
        print("\n❌ Requirements check failed!")
        print("   Please fix the issues above and try again.\n")
        return
    
    # تحميل البيئة
    if not load_env():
        print("\n❌ Failed to load environment!")
        return
    
    # التحقق من الإعدادات
    if not check_config():
        print("\n❌ Configuration check failed!")
        print("   Please configure your .env file.\n")
        return
    
    # تشغيل البوت
    run_bot()

if __name__ == "__main__":
    main()
