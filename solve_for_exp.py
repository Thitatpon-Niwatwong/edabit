def solve_for_exp(a, b):
    n = 1
    m = a
    while m != b:
        m *= a
        n += 1
    return n


x = solve_for_exp(9, 3486784401)
print(x)
