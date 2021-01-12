import math


def CalculateHypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


def main():
    value1 = float(input('Triangle side 1 length: '))
    value2 = float(input('Triangle side 2 length: '))
    print('Hypotenuse: %.2f' % CalculateHypotenuse(value1, value2))


if __name__ == "__main__":
    main()

