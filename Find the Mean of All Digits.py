def mean(num):
    x = 10
    bit = 0
    sum = 0
    y = 1
    n = 0
    while y <= num:
        bit = num % x
        bits = bit/y
        sum = sum + bits
        num = num - bit
        x = x * 10
        y = y * 10
        n += 1
        print(bits)
    return sum/n


print(mean(12))

# i = "123"
# a = [int(x) for x in str(i)]
# print(sum(a))
