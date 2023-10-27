def eda_bit(start, end):
    sum = []
    for i in range(start, end+1):
        if i % 15 == 0:

            sum.append("Edabit")

        elif i % 5 == 0:

            sum.append("bit")

        elif i % 3 == 0:

            sum.append("Eda")

        else:
            sum.append(i)

    return sum


print(eda_bit(0, 10))
