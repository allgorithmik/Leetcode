def listNodeRemove(lis: list, x: int) -> list():
    lisInv = lis[::-1]
    lisInv.pop(x-1)
    lisNew = lisInv[::-1]
    print(lisNew)

listNodeRemove() # Pass a list of integers and position from end(actual position DOES NOT start with ZERO) -- Remove Nth Node From End of List