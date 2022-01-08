def missingNumber(lis: list) -> int:
    length = len(lis)
    nums = [x for x in range(length + 1)]
    for i in nums:
        if lis.count(i) > 0:
            pass
        else:
            return i

missingNumber() # pass list of integers in sequence with 1 missing int