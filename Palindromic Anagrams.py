def is_palindrome_possible(txt):
    max = 1
    final = {}
    for i in txt:
        if i not in final:
            final[i] = 1
        else:
            final[i] += 1
    for i in final.values():
        if i == 1:
            max -= 1
            continue
        if max < 0:
            return False
        if i % 2 != 0:
            return False
    return True


print(is_palindrome_possible("suhbeusheff"))
