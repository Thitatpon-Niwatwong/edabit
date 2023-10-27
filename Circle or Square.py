import math
from math import pi


def circle_or_square(rad, area):
    lengthOfCurcle = 2 * math.pi * rad
    lengthOfArea = (math.sqrt(area)) * 4
    if lengthOfCurcle > lengthOfArea:
        return True
    return False


print(circle_or_square(8, 144))
