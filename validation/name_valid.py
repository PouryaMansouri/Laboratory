import re


def name_validation(name: str):
    pattern = "^[\w_]{5,14}$"
    return True if re.match(pattern, name) else False
