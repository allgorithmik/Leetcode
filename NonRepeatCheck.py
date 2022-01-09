def nonRepeatCheck(string: str) -> int:
    strLis = list(string)
    for i in strLis:
        if strLis.count(i) == 1:
            return strLis.index(i)
    return -2

nonRepeatCheck() # Pass a string