def blocks(step):
    one = 5
    plus = 7
    i = 1
    while i < step:
        one = one + plus
        plus += 1
        i += 1
    return one


print(blocks(5))
