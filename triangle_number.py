def triangle(n):
    m = n
    while n > 0:
        m = m + n-1
        n -= 1
    return m


a = triangle(215)
print(a)
