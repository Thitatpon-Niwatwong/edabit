def uncensor(txt, vowels):
    sum = []
    stat = 0
    for a in txt:
        if a == '*':
            sum.append(vowels[stat])
            stat += 1
        else:
            sum.append(a)
    return sum


print(uncensor("*PP*RC*S*", "UEAE"))
