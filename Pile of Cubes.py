def pile_of_cubes(m):
    n = 0
    palimate = 1
    while palimate <= m:
        n += 1
        newpalimate = n**3
        palimate = palimate + newpalimate
    return n


cum = int(input('Enternumber : '))
print(pile_of_cubes(cum))
