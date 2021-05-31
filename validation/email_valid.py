import re

def email_validation(email: str):
    pattern = "[\w\.{1}\-{1}]+@\w+\.\w+"
    return True if re.match(pattern, email) else False
