def negative_sum(chars):
    final = []
    i = 0
    while i < len(chars):
        if chars[i] == '-':
            current_negative = '-'
            i += 1
            while i < len(chars) and (chars[i].isdigit() or chars[i] == '.'):
                current_negative += chars[i]
                i += 1
            final.append(float(current_negative))
        else:
            i += 1
    return sum(final)


print(negative_sum("-12 13%14&-11"))
