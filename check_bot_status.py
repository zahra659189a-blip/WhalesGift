#!/usr/bin/env python3
"""
🔍 فحص حالة بوت الباندا - Bot Health Check
يقوم بفحص:
- حالة البوت
- حالة Flask server
- الاتصال بـ Telegram API
- قاعدة البيانات
"""

import requests
import sqlite3
import os
import sys
from datetime import datetime

def check_bot_health():
    """فحص شامل لصحة البوت"""
    print("🔍 Panda Giveaways Bot - Health Check")
    print("=" * 50)
    
    # 1. فحص Flask Verification Server
    print("\n1. 🌐 Flask Verification Server (Port 8081):")
    try:
        response = requests.get('http://localhost:8081/', timeout=10)
        if response.ok:
            data = response.json()
            print(f"   ✅ Status: {data.get('status', 'unknown')}")
            print(f"   📡 Service: {data.get('service', 'N/A')}")
            print(f"   🕐 Timestamp: {data.get('timestamp', 'N/A')}")
        else:
            print(f"   ❌ Server responded with status: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("   🔴 Server is NOT running on port 8081")
    except requests.exceptions.Timeout:
        print("   ⏰ Server timeout (may be overloaded)")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # 2. فحص اتصال Telegram API
    print("\n2. 🤖 Telegram Bot API:")
    try:
        # قراءة التوكن من متغير البيئة أو الملف
        bot_token = os.environ.get('BOT_TOKEN')
        if not bot_token:
            print("   ⚠️ BOT_TOKEN not found in environment variables")
            # يمكن إضافة قراءة من ملف إعدادات هنا
            return
            
        response = requests.get(f'https://api.telegram.org/bot{bot_token}/getMe', timeout=10)
        if response.ok:
            bot_info = response.json()['result']
            print(f"   ✅ Bot connected: @{bot_info['username']}")
            print(f"   📝 Name: {bot_info['first_name']}")
            print(f"   🆔 ID: {bot_info['id']}")
        else:
            print(f"   ❌ API Error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # 3. فحص قاعدة البيانات
    print("\n3. 🗄️ Database:")
    try:
        db_path = 'Arab_ton.db'
        if os.path.exists(db_path):
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # عدد المستخدمين
            cursor.execute("SELECT COUNT(*) FROM users")
            user_count = cursor.fetchone()[0]
            print(f"   👥 Total users: {user_count}")
            
            # عدد القنوات النشطة
            cursor.execute("SELECT COUNT(*) FROM required_channels WHERE is_active = 1")
            channel_count = cursor.fetchone()[0]
            print(f"   📺 Active channels: {channel_count}")
            
            # عدد المهام النشطة
            cursor.execute("SELECT COUNT(*) FROM tasks WHERE is_active = 1")
            task_count = cursor.fetchone()[0]
            print(f"   📋 Active tasks: {task_count}")
            
            conn.close()
            print("   ✅ Database accessible")
        else:
            print("   ❌ Database file not found")
    except Exception as e:
        print(f"   ❌ Database error: {e}")
    
    # 4. فحص الملفات المهمة
    print("\n4. 📁 Important files:")
    files_to_check = [
        'app.py',
        'panda_giveaways_bot.py',
        'public/index.html',
        'public/js/app.js',
        'public/js/config.js'
    ]
    
    for file_path in files_to_check:
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"   ✅ {file_path} ({size} bytes)")
        else:
            print(f"   ❌ {file_path} - NOT FOUND")
    
    # 5. نصائح الصيانة
    print("\n🛠️ Maintenance Tips:")
    print("   - إذا كان Flask server لا يعمل: python panda_giveaways_bot.py")
    print("   - إذا كان Telegram API لا يرد: تحقق من BOT_TOKEN")
    print("   - للتحقق من لوج البوت: tail -f bot.log")
    print("   - إعادة تشغيل الخدمات: bash start.sh")
    
    print(f"\n🕐 Health check completed at: {datetime.now()}")
    print("=" * 50)

if __name__ == "__main__":
    check_bot_health()