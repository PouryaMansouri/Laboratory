import re


def phone_validation(phone: str):
    pattern = "^09\d{9}$"
    pattern2 = "^\+989\d{9}$"
    return True if re.match(pattern, phone) or re.match(pattern2, phone) else False