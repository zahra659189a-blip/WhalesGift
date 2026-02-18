"""
🎨 Modern Icons System للبوت - Material Design Style
استخدام Unicode Symbols متطورة بدلاً من الإيموجيات التقليدية
"""

# Modern Material Design-like Icons using Unicode
ICONS = {
    # Main Navigation (مثل الصورة)
    'users': '▣',           # Users icon
    'tasks': '≡',           # Tasks/Menu icon  
    'home': '⌂',            # Home icon
    'game': '◉',            # Game/Spin icon
    'wallet': '▭',          # Wallet icon
    
    # Modern Actions
    'check': '✓',           # Success
    'cross': '✕',           # Error/Cancel
    'info': 'ⓘ',            # Information
    'warning': '⚠',         # Warning
    'add': '＋',            # Add
    'remove': '－',         # Remove
    'edit': '✎',            # Edit
    'delete': '⌫',          # Delete
    'view': '👁',           # View
    'settings': '⚙',        # Settings
    
    # Status Indicators
    'active': '●',          # Active (green dot)
    'inactive': '○',        # Inactive (empty circle)
    'pending': '◐',         # Pending (half circle)
    'success': '◉',         # Success (filled circle with ring)
    'error': '◍',           # Error (circle with X)
    
    # Money & Rewards
    'coin': '◈',            # Coin
    'money': '◊',           # Money/Diamond
    'ticket': '▭',          # Ticket
    'prize': '◆',           # Prize
    'star': '★',            # Star (filled)
    'star_empty': '☆',      # Star (empty)
    
    # Communication
    'message': '💬',        # Message
    'broadcast': '📡',      # Broadcast
    'notification': '🔔',   # Notification
    'channel': '📢',        # Channel
    
    # Navigation Arrows
    'right': '▸',           # Right arrow
    'left': '◂',            # Left arrow
    'up': '▴',              # Up arrow
    'down': '▾',            # Down arrow
    'back': '◄',            # Back
    'next': '►',            # Next
    
    # Charts & Stats
    'chart': '▦',           # Chart
    'graph': '▤',           # Graph
    'stats': '▥',           # Stats
    'report': '▨',          # Report
    
    # Security
    'lock': '🔒',           # Locked
    'unlock': '🔓',         # Unlocked
    'key': '🔑',            # Key
    'admin': '👑',          # Admin
    
    # Special Shapes
    'square': '▪',          # Small square
    'square_large': '■',    # Large square
    'circle': '●',          # Circle
    'circle_outline': '○',  # Circle outline
    'diamond': '◆',         # Diamond
    'diamond_outline': '◇', # Diamond outline
    'triangle': '▲',        # Triangle
    
    # Bullets & Separators
    'bullet': '•',          # Bullet point
    'arrow': '→',           # Arrow
    'separator': '─',       # Line separator
    'dot': '·',             # Small dot
    
    # Loading & Progress
    'loading1': '◜',        # Loading animation frame 1
    'loading2': '◝',        # Loading animation frame 2
    'loading3': '◞',        # Loading animation frame 3
    'loading4': '◟',        # Loading animation frame 4
    
    # Brand
    'panda': '🐼',          # Panda
    'ton': '◈',             # TON coin symbol
}

def icon(name: str, fallback: str = '•') -> str:
    """احصل على الأيقونة بالاسم"""
    return ICONS.get(name, fallback)

def button_text(icon_name: str, text: str) -> str:
    """تنسيق نص زر مع أيقونة"""
    return f"{icon(icon_name)} {text}"

def title(icon_name: str, text: str) -> str:
    """تنسيق عنوان مع أيقونة"""
    return f"{icon(icon_name)} {text}"

def list_item(text: str, icon_name: str = 'bullet') -> str:
    """تنسيق عنصر قائمة"""
    return f"{icon(icon_name)} {text}"

def status_text(status: str, text: str) -> str:
    """تنسيق حالة مع أيقونة"""
    status_icons = {
        'active': 'active',
        'inactive': 'inactive',
        'pending': 'pending',
        'success': 'success',
        'error': 'error'
    }
    icon_name = status_icons.get(status, 'bullet')
    return f"{icon(icon_name)} {text}"

def section_divider(title: str = '') -> str:
    """فاصل بين الأقسام"""
    if title:
        return f"\n{icon('separator') * 20}\n{title}\n{icon('separator') * 20}\n"
    return f"\n{icon('separator') * 30}\n"

# Quick access to common combinations
QUICK = {
    'users_menu': f"{icon('users')} المستخدمين",
    'tasks_menu': f"{icon('tasks')} المهام",
    'home_menu': f"{icon('home')} الرئيسية",
    'game_menu': f"{icon('game')} دوّر العجلة",
    'wallet_menu': f"{icon('wallet')} المحفظة",
    'admin_panel': f"{icon('admin')} لوحة التحكم",
    'settings_menu': f"{icon('settings')} الإعدادات",
    'back_button': f"{icon('back')} رجوع",
    'success_msg': f"{icon('success')} تم بنجاح",
    'error_msg': f"{icon('error')} حدث خطأ",
    'pending_msg': f"{icon('pending')} قيد المعالجة",
}

