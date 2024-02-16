def remap(value, low1, high1, low2, high2):
    if high2 > low2:
        answer = (value - low1) / (high1 - low1) * high2 - low2
    else:
        answer = low2 - ((value - low1) / (high1 - low1) * abs(high2 - low2))
    return answer


print(remap(17, 5, 55, 100, 30))
