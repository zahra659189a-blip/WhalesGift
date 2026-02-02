# 🚀 دليل نشر Mini App على Render

## الخطوات بالتفصيل:

### 1️⃣ إنشاء Web Service على Render

1. اذهب إلى: https://render.com
2. سجل دخول أو أنشئ حساب جديد
3. اضغط **New +** → **Web Service**

---

### 2️⃣ ربط GitHub Repository

1. اختر repository الخاص بك
2. أو استخدم **Public Git Repository**:
   - الصق رابط repo الخاص بك

---

### 3️⃣ إعدادات الخدمة

**Name**: `panda-giveaways-mini-app` (أو أي اسم تريده)

**Root Directory**: اتركه فارغ (أو اكتب `.`)

**Environment**: `Python 3`

**Build Command**:
```bash
pip install -r requirements.txt
```

**Start Command**:
```bash
gunicorn app:app
```

---

### 4️⃣ Environment Variables

في قسم **Environment**، أضف:

```env
PYTHON_VERSION=3.11
PORT=10000
```

---

### 5️⃣ النشر

1. اختر **Free Plan**
2. اضغط **Create Web Service**
3. انتظر حتى يكتمل Build (2-5 دقائق)
4. ستحصل على رابط مثل: `https://panda-giveaways-mini-app.onrender.com`

---

### 6️⃣ تحديث Bot

بعد الحصول على رابط Render:

1. افتح ملف `.env`
2. عدل:
```env
MINI_APP_URL=https://your-app-name.onrender.com
```

3. أعد تشغيل البوت

---

### 7️⃣ اختبار Mini App

1. افتح البوت على Telegram
2. اضغط "🎰 افتح Panda Giveaway"
3. يجب أن يفتح Mini App بشكل صحيح

---

## 📝 ملاحظات مهمة

### ✅ المزايا:
- **مجاني تماماً** (Free Plan)
- **SSL مجاني** (HTTPS تلقائي)
- **Auto-deploy** (كل push على GitHub)
- **لا يحتاج خادم**

### ⚠️ القيود:
- Free Plan ينام بعد 15 دقيقة خمول
- يستيقظ تلقائياً عند أول طلب (قد يستغرق 30 ثانية)

### 🔧 الحل:
استخدم خدمة Cron Job مجانية مثل:
- **UptimeRobot** (https://uptimerobot.com)
- أو **Cron-Job.org** (https://cron-job.org)

أضف Health Check URL:
```
https://your-app-name.onrender.com/health
```

---

## 🗂️ هيكل المشروع

```
project/
├── app.py              # Flask server
├── public/             # Mini App files
│   ├── index.html      # الصفحة الرئيسية
│   ├── admin.html      # صفحة الأدمن
│   ├── css/            # ملفات الأنماط
│   ├── js/             # ملفات JavaScript
│   └── img/            # الصور
├── requirements.txt    # Python dependencies
└── .env                # Environment variables
```

---

## 🔍 Troubleshooting

### المشكلة: Build فشل

**الحل**:
- تأكد من `requirements.txt` صحيح
- تأكد من Python version = 3.11

### المشكلة: Mini App لا يفتح

**الحل**:
- تأكد من `MINI_APP_URL` في `.env` صحيح
- تأكد من الملفات في `public/` موجودة
- افتح الرابط في المتصفح مباشرة للتأكد

### المشكلة: CSS/JS لا يعمل

**الحل**:
- تأكد من المسارات في HTML صحيحة
- استخدم مسارات نسبية: `./css/style.css`

---

## 📞 الدعم

إذا واجهت مشكلة:
1. تحقق من Logs في Render Dashboard
2. تأكد من Build نجح 100%
3. اختبر health check: `/health`
