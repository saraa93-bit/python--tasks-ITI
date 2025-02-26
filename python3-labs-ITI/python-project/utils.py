import hashlib
import re

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_egyptian_phone(phone):
    pattern = r"^01[0-2]\d{8}$"
    return re.match(pattern, phone) is not None
