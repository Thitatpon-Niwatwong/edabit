def snakefill(n):
    x = 2
    num = n * n
    all = 0
    while num > x:
        x = x * 2
        all += 1
    return all


print(snakefill(5))
