def returnMiddle(tree: list) -> list:
    if len(tree) % 2 == 0:
        newLen = tree[(int(len(tree) / 2) - 1) + 1 :]
        return newLen
    else:
        newLen = tree[int(len(tree) / 2) :]
        return newLen

returnMiddle() #Pass a list with either even or odd number of elements, list comprehension can also be passed