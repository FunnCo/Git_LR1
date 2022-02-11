import math


def biSquareEquation(a, b, c):
    answers = []
    if areCoefficientsValid(a, b, c):
        a = float(a)
        b = float(b)
        c = float(c)
        listOfTempResults = squareEquation(a, b, c)
        for temp in listOfTempResults:
            if temp > 0:
                answers.append(floatToInt(math.sqrt(temp)))
                answers.append(floatToInt(-math.sqrt(temp)))
            elif temp == 0:
                answers.append(floatToInt(math.sqrt(temp)))
        if len(answers) == 0:
            return "Вещественных корней нет"
        return answers
    return "Ошибка"


def squareEquation(a, b, c):
    answers = []
    d = b * b - a * c * 4
    if d < 0:
        return answers
    answers.append((math.sqrt(d) - b) / 2 / a)
    if d == 0:
        return answers
    answers.append((-math.sqrt(d) - b) / 2 / a)
    return answers


def areCoefficientsValid(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return False
    return a != 0

def floatToInt(value):
    if int(value)==value:
        return int(value)
    return value