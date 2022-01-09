def ransomCheck(ransom: str, message: str) -> bool:
    if ransom in message:
        return True
    else:
        return False

ransomCheck() #pass two strings ransom and message, message string is the superset of ransom