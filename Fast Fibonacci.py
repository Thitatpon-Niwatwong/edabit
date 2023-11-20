def fib_fast(num):
    x1 = 0
    x2 = 1
    i = 1
    while i < num:
        x3 = x1 + x2
        x1 = x2
        x2 = x3
        i += 1
    return x3


print(fib_fast(0))
