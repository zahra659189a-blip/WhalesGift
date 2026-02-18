# استخدام Python 3.12.7 (إجباري!)
FROM python:3.12.7-slim

# تعيين مجلد العمل
WORKDIR /app

# نسخ الملفات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# تعيين PORT الافتراضي (Render هيحدده تلقائياً)
ENV PORT=10000

# تشغيل gunicorn
CMD gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120 --access-logfile - --error-logfile -
