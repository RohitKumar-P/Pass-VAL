import re

def validate_password(password):
    pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$^!?~]).{8,}'
    result = re.fullmatch(pattern, password)
    if result:
        return True
    else:
        return False