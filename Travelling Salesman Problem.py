def paths(n):
    sum = 1
    while n > 0:
        sum = sum * n
        n -= 1
    return sum


print(paths(0))
