def multiplication_table(n):
    final = []
    for a in range(1, n+1):
        final.append([])
    for i in range(1, n+1):
        for j in range(1, n+1):
            final[i-1].append(j*i)
    return final


print(multiplication_table(3))
