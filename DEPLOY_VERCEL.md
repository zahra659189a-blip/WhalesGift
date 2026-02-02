# 🚀 دليل رفع Mini App على Vercel

## الخطوات بالتفصيل:

### 1️⃣ إنشاء حساب على Vercel

1. اذهب إلى: https://vercel.com
2. اضغط **Sign Up**
3. سجل باستخدام **GitHub** (موصى به)

---

### 2️⃣ رفع كود Mini App على GitHub

```bash
# في مجلد المشروع
cd "C:\Users\DELL\Desktop\بوت ارباح"

# إنشاء repository جديد
git init
git add mini_app/
git commit -m "Initial commit: Panda Giveaways Mini App"

# ربط مع GitHub (استبدل username و repo-name)
git remote add origin https://github.com/username/panda-giveaways.git
git branch -M main
git push -u origin main
```

---

### 3️⃣ ربط Vercel مع GitHub

1. افتح https://vercel.com/dashboard
2. اضغط **Add New** → **Project**
3. اختر **Import Git Repository**
4. اختر repository الخاص بك
5. اضغط **Import**

---

### 4️⃣ إعدادات المشروع

في صفحة الإعدادات:

**Framework Preset**: اختر `Other`

**Root Directory**: اكتب `mini_app`

**Build Command**: اتركه فارغ

**Output Directory**: اتركه فارغ

**Install Command**: اتركه فارغ

---

### 5️⃣ Environment Variables (المتغيرات)

اضغط **Environment Variables** وأضف:

```
BOT_USERNAME = PandaGiveawaysBot
```

---

### 6️⃣ Deploy (النشر)

1. اضغط **Deploy**
2. انتظر دقيقة
3. ستحصل على رابط مثل: `https://your-project.vercel.app`

---

### 7️⃣ تحديث البوت بالرابط

في ملف `.env`:

```env
MINI_APP_URL=https://your-project.vercel.app
```

---

### 8️⃣ إعادة تشغيل البوت

```bash
python panda_giveaways_bot.py
```

---

## ✅ جاهز!

الآن Mini App شغال على Vercel وجاهز للاستخدام!

---

## 🔄 تحديث Mini App

عند تعديل الكود:

```bash
git add mini_app/
git commit -m "Update: description"
git push
```

Vercel سيحدث تلقائياً! ✨

---

## 📱 فتح Mini App من البوت

```python
# الزر في البوت:
InlineKeyboardButton(
    "🎰 افتح Mini App",
    web_app=WebAppInfo(url=MINI_APP_URL)
)
```

---

## ⚠️ ملاحظات مهمة

1. ✅ Vercel مجاني للمشاريع الصغيرة
2. ✅ يدعم HTTPS تلقائياً
3. ✅ CDN سريع جداً
4. ⚠️ تأكد أن مجلد `mini_app` يحتوي على `index.html`
5. ⚠️ الرابط يجب أن يكون HTTPS (Vercel يوفره تلقائياً)

---

## 🆘 حل المشاكل

### المشكلة: "404 Not Found"
**الحل**: تأكد من:
- `Root Directory` = `mini_app`
- ملف `index.html` موجود في `mini_app/`

### المشكلة: "Build Failed"
**الحل**: 
- اترك `Build Command` فارغ
- Mini App لا يحتاج build

### المشكلة: Mini App لا يفتح من تليجرام
**الحل**:
- تأكد من `MINI_APP_URL` صحيح في `.env`
- أعد تشغيل البوت

---

**🎉 مبروك! Mini App شغال على Vercel!**
