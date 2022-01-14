def numsCheck(nums: list) -> bool:
    length = len(nums)
    ini = nums[0]
    for i in range(length):
        if nums[i] == ini:
            pass
        else:
            return False
    return True

numsCheck() # Pass a list of similar / dissimilar list of int lists, nested lists -> [[1,2,3], [1,2,3], [1,2,3], [1,2,3]]