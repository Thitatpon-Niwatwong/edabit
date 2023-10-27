import math


def solutions(a, b, c):
    sum = b**2 - (4*a*c)
    if sum > 0:
        return 2
    if sum == 0:
        return 1
    else:
        return 0


print(solutions(1, 0, 1))
