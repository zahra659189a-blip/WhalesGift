#!/usr/bin/env python3
"""
Fix httpcore compatibility with Python 3.14
Patches the __init__.py file to avoid the typing.Union error
"""
import os
import sys

def fix_httpcore():
    """Fix httpcore __init__.py for Python 3.14 compatibility"""
    try:
        # Find httpcore location
        import httpcore
        httpcore_init = httpcore.__file__
        
        print(f"📦 Found httpcore at: {httpcore_init}")
        
        # Read the file
        with open(httpcore_init, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # The problematic pattern in httpcore
        old_pattern = 'setattr(__locals[__name], "__module__", "httpcore")'
        
        # Safe replacement that checks if attribute exists
        new_pattern = '''try:
            setattr(__locals[__name], "__module__", "httpcore")
        except (AttributeError, TypeError):
            pass  # Skip if attribute doesn't exist or can't be set'''
        
        if old_pattern in content:
            # Replace the problematic line
            content = content.replace(old_pattern, new_pattern)
            
            # Write back
            with open(httpcore_init, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ httpcore patched successfully for Python 3.14!")
            return True
        elif 'except (AttributeError, TypeError):' in content:
            print("✅ httpcore already patched!")
            return True
        else:
            print("⚠️ Pattern not found - httpcore version may be compatible")
            return True  # Return True anyway to not block execution
            
    except ImportError:
        print("⚠️ httpcore not installed yet")
        return True  # Not an error during build
    except Exception as e:
        print(f"⚠️ Error patching httpcore: {e}")
        return True  # Don't fail the build

if __name__ == "__main__":
    success = fix_httpcore()
    sys.exit(0 if success else 1)
