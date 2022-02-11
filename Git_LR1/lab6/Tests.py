from Equations import *


def inputCoefficients():
    a = input("Введите коэффициент a: ")
    b = input("Введите коэффициент b: ")
    c = input("Введите коэффициент c: ")
    return [a, b, c]


def test():
    while True:
        coefficients = inputCoefficients()
        print(biSquareEquation(coefficients[0], coefficients[1], coefficients[2]))
        if input("\nХотите продолжить? Y/Т: ") == "N":
            break
        print()

test()

