def cars_needed(n):
    if n % 5 == 0:
        sum = n//5
    else:
        sum = n//5 + 1
    return sum


print(cars_needed(5))
