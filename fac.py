def fac(a):
    sum = 1
    sums = 1
    while a > 0:
        sum = sum * sums
        a -= 1
        sums += 1
    return sum


print(fac(0))
