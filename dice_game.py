def dice_game(lst):
    sumAll = []
    if len(lst) == 3:
        for i in lst:
            a, b = i
            num = a+b
            sumAll.append(num)
        return sum(sumAll)
    return False


print(dice_game([(1, 2), (3, 4)]))
