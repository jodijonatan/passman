import base64
import hashlib
import string
import random
from passman.config import SALT

def simple_encrypt(text: str, key: str) -> str:
    key_stream = (key * (len(text) // len(key) + 1))[:len(text)]
    encrypted_bytes = bytes(ord(c) ^ ord(k) for c, k in zip(text, key_stream))
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def simple_decrypt(encrypted_text: str, key: str) -> str:
    encrypted_bytes = base64.b64decode(encrypted_text.encode('utf-8'))
    key_stream = (key * (len(encrypted_bytes) // len(key) + 1))[:len(encrypted_bytes)]
    decrypted = ''.join(chr(b ^ ord(k)) for b, k in zip(encrypted_bytes, key_stream))
    return decrypted

def hash_password(password: str) -> str:
    salted = f"{SALT}{password}{SALT}"
    return hashlib.sha256(salted.encode()).hexdigest()

def generate_strong_password(length: int = 16) -> str:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    all_chars = lowercase + uppercase + digits + symbols
    
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols),
    ]
    for _ in range(length - 4):
        password_chars.append(random.choice(all_chars))
    random.shuffle(password_chars)
    return ''.join(password_chars)

def calculate_password_strength(password: str) -> int:
    score = 0
    if len(password) >= 8:  score += 15
    if len(password) >= 12: score += 15
    if len(password) >= 16: score += 10
    if any(c.islower() for c in password):  score += 15
    if any(c.isupper() for c in password):  score += 15
    if any(c.isdigit() for c in password):  score += 15 # Koreksi dari c.isdigit() jika c adalah string tunggal, perbaiki logika asal Anda
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password): score += 15
    return min(score, 100)