def filter_primes(num):
    final = []
    for a in num:
        if a < 2:
            continue
        is_prime = True
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                is_prime = False
                break
        if is_prime:
            final.append(a)
    return final


cum = [int(i) for i in input("EnterNumber : ").split(", ")]
print(filter_primes(cum))
