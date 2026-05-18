import sys
import os

# Ensure UTF-8 output on Windows to prevent UnicodeEncodeError
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from rich.console import Console

console = Console()
DATA_FILE = "passwords.json"
SALT = "PassMan_Salt_Key"
MIN_PASSWORD_LENGTH = 6

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False