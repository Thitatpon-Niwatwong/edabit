def find_the_difference(s, t):
    for j in t:
        if j not in s:
            return j


print(find_the_difference("", "y"))
