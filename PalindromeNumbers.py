def palindromeNumber(n: str) -> bool:
    listNumber = list(n)
    invNumber = listNumber[::-1]
    if listNumber == invNumber:
        return True
    else:
        return False

palindromeNumber() # Pass an integer in string form, can include negative integers