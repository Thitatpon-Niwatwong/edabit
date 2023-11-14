def encrypt(word):
    num = []
    b = [a for a in word[::-1]]
    dic = {
        'a': 0,
        'e': 1,
        'i': 2,
        'o': 2,
        'u': 3
    }
    for c in b:
        if c in dic.keys():
            c = dic[c]
        num.append(str(c))
    nums = ''.join(num)
    return nums

print(encrypt("apple"))
