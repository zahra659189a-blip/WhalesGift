#!/usr/bin/env python3
"""
Fix httpcore compatibility with Python 3.14
Patches the __init__.py file to avoid the typing.Union error
"""
import os
import sys
import sysconfig

def fix_httpcore():
    """Fix httpcore __init__.py for Python 3.14 compatibility"""
    try:
        # Get site-packages directory
        site_packages = sysconfig.get_path('purelib')
        httpcore_init = os.path.join(site_packages, 'httpcore', '__init__.py')
        
        if not os.path.exists(httpcore_init):
            print(f"⚠️ httpcore not found at {httpcore_init}")
            # Try alternative locations
            import site
            for path in site.getsitepackages():
                alt_path = os.path.join(path, 'httpcore', '__init__.py')
                if os.path.exists(alt_path):
                    httpcore_init = alt_path
                    break
            else:
                print("⚠️ httpcore not installed - skipping patch")
                return True
        
        print(f"📦 Found httpcore at: {httpcore_init}")
        
        # Read the file
        with open(httpcore_init, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already patched
        if 'Python 3.14 compatibility' in content:
            print("✅ httpcore already patched!")
            return True
        
        # The problematic line (line 140)
        old_pattern = 'setattr(__locals[__name], "__module__", "httpcore")  # noqa'
        
        # Safe replacement with try/except
        new_pattern = '''try:
        setattr(__locals[__name], "__module__", "httpcore")  # noqa
    except (AttributeError, TypeError):
        pass  # Python 3.14 compatibility'''
        
        if old_pattern in content:
            # Replace the problematic line
            content = content.replace(old_pattern, new_pattern)
            
            # Write back
            with open(httpcore_init, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ httpcore patched successfully for Python 3.14!")
            print(f"   Modified: {httpcore_init}")
            return True
        else:
            # Try alternative pattern without # noqa
            alt_pattern = 'setattr(__locals[__name], "__module__", "httpcore")'
            if alt_pattern in content:
                new_alt = '''try:
        setattr(__locals[__name], "__module__", "httpcore")
    except (AttributeError, TypeError):
        pass  # Python 3.14 compatibility'''
                content = content.replace(alt_pattern, new_alt)
                with open(httpcore_init, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("✅ httpcore patched (alternative pattern)!")
                return True
            
            print("⚠️ Pattern not found - httpcore may already be compatible")
            print(f"   Checked: {httpcore_init}")
            return True
            
    except Exception as e:
        print(f"❌ Error patching httpcore: {e}")
        import traceback
        traceback.print_exc()
        return False  # Fail the build if patch fails

if __name__ == "__main__":
    print("🔧 Patching httpcore for Python 3.14 compatibility...")
    success = fix_httpcore()
    if success:
        print("✅ Patch completed successfully!")
    else:
        print("❌ Patch failed!")
    sys.exit(0 if success else 1)
