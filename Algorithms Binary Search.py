primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def is_prime(primes, num, left=0, right=None):
    right = len(primes) - 1 if right is None else right

    while left <= right:
        mid = (left + right) // 2
        if primes[mid] == num:
            return True  # Found in the primes list
        elif primes[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return False  # Number is not in the primes list


print(is_prime(primes, 2))  # Test if 3 is prime
