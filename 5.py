def missing_num(lst):
    sum_list = [n for n in range(1, 11) if n not in lst]
    if sum_list:
        return sum_list[0]


a = missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10])
print(a)
#
