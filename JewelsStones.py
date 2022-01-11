def stonesJewels(jewels: str, stones: str) -> int():
    x = 0
    lisJewels = list(jewels)
    lisStones = list(stones)
    for i in range(len(lisJewels)):
        if lisJewels[i] == lisStones[i]:
            x += 1

    return x

stonesJewels("aA", "aAAbbbb") # Pass two strings, case sensitive, some charecters among two strings must repeat