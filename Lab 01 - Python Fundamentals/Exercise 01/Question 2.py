import math


def get_hypotenuse(side1, side2):
    hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)
    return hypotenuse

print(get_hypotenuse(3, 4))