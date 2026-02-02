"""
🌐 Flask Server لخدمة Mini App على Render
"""
from flask import Flask, send_from_directory, request
import os

app = Flask(__name__, static_folder='public', static_url_path='')

@app.route('/')
def index():
    """الصفحة الرئيسية"""
    return send_from_directory('public', 'index.html')

@app.route('/admin')
def admin():
    """صفحة الأدمن"""
    return send_from_directory('public', 'admin.html')

@app.route('/<path:path>')
def serve_static(path):
    """خدمة الملفات الثابتة (CSS, JS, Images)"""
    return send_from_directory('public', path)

@app.route('/health')
def health():
    """Health check لـ Render"""
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
