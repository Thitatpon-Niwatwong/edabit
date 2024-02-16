def cup_swapping(swaps):
    finalCup = "B"
    for i in swaps:
        if finalCup in i:
            finalCup = i.replace(finalCup, "")
            print(finalCup)
        else:
            continue
    return finalCup


print(cup_swapping(["AC", "CA", "CA", "AC"]))
