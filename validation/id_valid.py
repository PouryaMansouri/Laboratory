import re


def id_validation(name: str):
    pattern = "^[\d]{4,10}$"
    return True if re.match(pattern, name) else False
