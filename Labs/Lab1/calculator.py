from hypotenuse import CalculateHypotenuse


def Sum(a, b):
    return a + b


def Multiply(a, b):
    return a * b


def Divide(a, b):
    return a / b


def Subtract(a, b):
    return a - b


def main():
    while True:
        print('1 to calculate hypotenuse')
        print('2 to add')
        print('3 to subtract')
        print('4 to multiply')
        print('5 to divide')

        choice = int(input())

        if choice == 1:
            result = CalculateHypotenuse(
                float(input('enter first number: ')),
                float(input('enter second number: '))
            )
            print('%.1f' % result)
        elif choice == 2:
            result = Sum(
                float(input('enter first number: ')),
                float(input('enter second number: '))
            )
            print('%.1f' % result)
        elif choice == 3:
            result = Subtract(
                float(input('enter first number: ')),
                float(input('enter second number: '))
            )
            print('%.1f' % result)
        elif choice == 4:
            result = Multiply(
                float(input('enter first number: ')),
                float(input('enter second number: '))
            )
            print('%.1f' % result)
        elif choice == 5:
            result = Divide(
                float(input('enter first number: ')),
                float(input('enter second number: '))
            )
            print('%.1f' % result)


if __name__ == "__main__":
    main()
