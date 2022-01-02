def count(lis) -> int:
    for i in lis:
        if lis.count(i) == 1:
            return i
        
count() #pass a list with integers