def mystery_func(num):
    x = 10
    tan = len(str(num))
    sum = []
    y = 1
    r = 1
    while tan > 0:
        a = (num % x)
        b = (num % x) / y
        sum.append(b)
        num = num - a
        x *= 10
        y *= 10
        tan -= 1
    for i in sum:
        r = r * i
    return r


print(mystery_func(152))

# def mystery_func(num):
#     digits = [int(digit) for digit in str(num)]
#     product = 1

#     for digit in digits:
#         product *= digit

#     return product
