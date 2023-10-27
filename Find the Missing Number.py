def missing_num(lst):
    sum = [n for n in range(1, 11)]
    for b in lst:
        if b not in sum:
            return b


a = missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10])
print(a)
