"""
🌐 Flask Server لخدمة Mini App على Render
"""
from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import os
import sys

# إضافة المسار الحالي لـ Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# استيراد DatabaseManager من البوت
try:
    from panda_giveaways_bot import DatabaseManager, db
except ImportError:
    # إذا لم ينجح، نستخدم SQLite مباشرة
    db = None

app = Flask(__name__, static_folder='public', static_url_path='')
CORS(app)  # السماح بـ CORS

# ═══════════════════════════════════════════════════════════════
# 🌐 ROUTES - Static Files
# ═══════════════════════════════════════════════════════════════

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

# ═══════════════════════════════════════════════════════════════
# 🔌 API ENDPOINTS
# ═══════════════════════════════════════════════════════════════

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user_data(user_id):
    """الحصول على بيانات المستخدم"""
    try:
        if db is None:
            return jsonify({
                'success': False,
                'error': 'Database not available'
            }), 500
        
        user = db.get_user(user_id)
        if user:
            return jsonify({
                'success': True,
                'data': {
                    'user_id': user.user_id,
                    'username': user.username,
                    'full_name': user.full_name,
                    'balance': float(user.balance),
                    'available_spins': user.available_spins,
                    'total_spins': user.total_spins,
                    'total_referrals': user.total_referrals,
                    'created_at': user.created_at,
                    'is_banned': user.is_banned
                }
            })
        else:
            return jsonify({
                'success': False,
                'error': 'User not found'
            }), 404
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/user/<int:user_id>/referrals', methods=['GET'])
def get_user_referrals(user_id):
    """الحصول على إحالات المستخدم"""
    try:
        if db is None:
            return jsonify({'success': False, 'error': 'Database not available'}), 500
        
        referrals = db.get_user_referrals(user_id)
        return jsonify({
            'success': True,
            'data': referrals
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/user/<int:user_id>/spins', methods=['GET'])
def get_user_spins(user_id):
    """الحصول على تاريخ لفات المستخدم"""
    try:
        if db is None:
            return jsonify({'success': False, 'error': 'Database not available'}), 500
        
        limit = request.args.get('limit', 50, type=int)
        spins = db.get_user_spins_history(user_id, limit)
        return jsonify({
            'success': True,
            'data': spins
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/spin', methods=['POST'])
def perform_spin():
    """تنفيذ لفة العجلة"""
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        
        if not user_id:
            return jsonify({'success': False, 'error': 'User ID required'}), 400
        
        # التحقق من توفر لفات
        user = db.get_user(user_id)
        if not user or user.available_spins <= 0:
            return jsonify({
                'success': False,
                'error': 'No spins available'
            }), 400
        
        # تنفيذ اللفة (هنا يجب استدعاء منطق عجلة الحظ)
        # نستخدم الكود من البوت
        from panda_giveaways_bot import wheel
        result = wheel.spin()
        
        # تسجيل النتيجة
        import hashlib
        import datetime
        spin_hash = hashlib.sha256(f"{user_id}{datetime.datetime.now().isoformat()}{result['amount']}".encode()).hexdigest()
        
        db.record_spin(user_id, result['name'], result['amount'], spin_hash)
        db.update_user_balance(user_id, result['amount'], add=True)
        db.update_available_spins(user_id, -1)
        
        # إرجاع النتيجة المحدثة
        updated_user = db.get_user(user_id)
        
        return jsonify({
            'success': True,
            'data': {
                'prize': result,
                'new_balance': float(updated_user.balance),
                'remaining_spins': updated_user.available_spins
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def get_bot_stats():
    """إحصائيات البوت (للأدمن)"""
    try:
        if db is None:
            return jsonify({'success': False, 'error': 'Database not available'}), 500
        
        stats = db.get_bot_statistics()
        return jsonify({
            'success': True,
            'data': stats
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check لـ Render"""
    return {'status': 'ok', 'service': 'Panda Giveaways Mini App'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)

