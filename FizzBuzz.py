def fizzBuzz(n: int) -> list:
    lis = [x for x in range(n+1)]
    for i in lis:
        if i % 3 == 0:
            lis[i] = "Fizz"
        if i % 5 == 0:
            lis[i] = "Buzz"
        if i % 3 == 0 and i % 5 == 0:
            lis[i] = "FizzBuzz"

    lis.pop(0) ## Getting index error hence this workaround
    return lis

fizzBuzz() # Pass an integer