def max_collatz(num):
    max_value = num
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        max_value = max(num, max_value)
    return max(max_value, 1)


print(max_collatz(2))
