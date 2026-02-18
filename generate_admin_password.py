#!/usr/bin/env python3
"""
🔐 Admin Password Hash Generator
يساعد في إنشاء password hash لنظام Admin Panel
"""

import hashlib
import sys

def generate_password_hash(password):
    """إنشاء SHA-256 hash لكلمة السر"""
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    print("=" * 60)
    print("🔐 Admin Password Hash Generator")
    print("   لإنشاء password hash لنظام Admin Panel")
    print("=" * 60)
    print()
    
    if len(sys.argv) > 1:
        # إذا تم تمرير كلمة السر كـ argument
        password = sys.argv[1]
    else:
        # طلب كلمة السر من المستخدم
        password = input("أدخل كلمة السر الجديدة: ").strip()
    
    if not password:
        print("❌ خطأ: يجب إدخال كلمة سر")
        sys.exit(1)
    
    if len(password) < 8:
        print("⚠️  تحذير: كلمة السر قصيرة جداً (يفضل 12+ حرف)")
        confirm = input("هل تريد المتابعة؟ (y/n): ").strip().lower()
        if confirm != 'y':
            print("تم الإلغاء")
            sys.exit(0)
    
    # إنشاء Hash
    password_hash = generate_password_hash(password)
    
    print()
    print("✅ تم إنشاء Password Hash بنجاح!")
    print()
    print("-" * 60)
    print("📋 انسخ السطر التالي وأضفه لمتغيرات البيئة:")
    print("-" * 60)
    print(f"ADMIN_PASSWORD_HASH={password_hash}")
    print("-" * 60)
    print()
    print("📝 ملاحظات:")
    print("  1. لا تشارك هذا الـ hash مع أحد")
    print("  2. احتفظ بنسخة احتياطية منه")
    print("  3. بعد إضافته، أعد تشغيل السيرفر")
    print()
    
    # عرض أمثلة للاستخدام
    print("💡 كيفية الاستخدام:")
    print()
    print("  في ملف .env:")
    print(f"    ADMIN_PASSWORD_HASH={password_hash}")
    print()
    print("  في Render.com:")
    print("    اذهب إلى Environment → Add Environment Variable")
    print("    Key: ADMIN_PASSWORD_HASH")
    print(f"    Value: {password_hash}")
    print()
    print("  في Vercel:")
    print("    Settings → Environment Variables → Add New")
    print("    Name: ADMIN_PASSWORD_HASH")
    print(f"    Value: {password_hash}")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ تم الإلغاء بواسطة المستخدم")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ خطأ: {e}")
        sys.exit(1)
