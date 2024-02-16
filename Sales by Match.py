def sock_merchant(lst):
    stack = []
    num = 0
    for i in lst:
        if i not in stack:
            stack.append(i)
        else:
            stack.remove(i)
            print(stack)
            num += 1
    return num


print(sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]))
