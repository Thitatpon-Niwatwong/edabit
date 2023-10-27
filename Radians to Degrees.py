from math import pi


def radians_to_degrees(rad):
    mum = rad/pi * 180
    return (round(mum, 1))


print(radians_to_degrees(1))
