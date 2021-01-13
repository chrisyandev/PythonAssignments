import math


def CalculateHypotenuse(a, b):
    """
    Calculates the hypotenuse for a right-angled triangle.
    :param a: one side of the triangle
    :param b: another side of the triangle
    :return: the hypotenuse of the triangle
    """
    return math.sqrt(a**2 + b**2)


def main():
    """
    Drives the program.
    :return: none
    """
    value1 = float(input('Triangle side 1 length: '))
    value2 = float(input('Triangle side 2 length: '))
    print('Hypotenuse: %.2f' % CalculateHypotenuse(value1, value2))


if __name__ == "__main__":
    main()

