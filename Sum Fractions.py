from fractions import Fraction


def sum_of_fractions(fraction_list):
    total_fraction = Fraction(0, 1)

    for fraction in fraction_list:
        numerator, denominator = fraction
        fraction_obj = Fraction(numerator, denominator)
        total_fraction += fraction_obj

    return round(float(total_fraction))


# Example usage:
fractions = [[1, 2], [1, 3], [1, 6]]
result = sum_of_fractions(fractions)
print(result)  # Output: 1
