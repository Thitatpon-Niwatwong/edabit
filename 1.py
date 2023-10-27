def stutter(word):
    a = f"{word[0]}{word[1]}...{word[0]}{word[1]}...{word}?"
    return a


s = stutter("adfsaf")
print(s)
