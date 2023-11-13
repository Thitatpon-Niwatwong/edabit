def not_good_math(n, k):
    for i in range(k):
        if n % 10 != 0:
            n -= 1
        else:
            n /= 10
    return int(n)


print(not_good_math(1000000000, 9))
