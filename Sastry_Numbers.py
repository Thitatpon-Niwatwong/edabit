def is_sastry(n):
    from math import sqrt
    if sqrt(n) % 1 == 0:
        print(sqrt(n))
        return True
    else:
        print(sqrt(n))
        return False


print(is_sastry(5))
print("s")
# print("a")
