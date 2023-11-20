def arithmetic_operation(n):
    x = n.split()
    for i in range(len(x)):
        if x[i] == '+':
            answer = int(x[i-1]) + int(x[i+1])
        elif x[i] == '-':
            answer = int(x[i-1]) - int(x[i+1])
        elif x[i] == '*':
            answer = int(x[i-1]) * int(x[i+1])
        elif x[i] == '//':
            if x[-1] == '0':
                return -1
            else:
                answer = int(x[i-1]) / int(x[i+1])

    return answer


print(arithmetic_operation("12 // 5"))
