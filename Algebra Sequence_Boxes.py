def box_seq(step):
    if step % 2 == 0:
        sum = step
    else:
        sum = step * 2 + 1
    return sum


print(box_seq(2))
