def anagramCheck(x, y) -> bool:
    word1 = set(x)
    word2 = set(y)
    if word1 == word2 and len(x) == len(y):
        return True
    else:
        return False

anagramCheck() # Pass two words into function