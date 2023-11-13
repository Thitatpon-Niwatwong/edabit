def count_overlapping(intervals, point):
    num = 0
    sum = []
    for a in intervals:
        b, c = a
        for d in range(b, c+1):
            sum.append(d)
        if point in sum:
            num += 1
        print(sum)
        sum = []
    return num


print(count_overlapping([[1, 2], [2, 3], [1, 3], [4, 5], [0, 1]], 2))
