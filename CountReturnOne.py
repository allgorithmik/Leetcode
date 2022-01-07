def returnOne(x: list) -> int:
    for i in x:
        if x.count(i) == 1:
            return i

returnOne() #Enter a list of ints with at least 1 unique int