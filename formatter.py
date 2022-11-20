import math


def plurals(number, form1, form2, form3, splitter=" "):
    return f"{number}{splitter}{plurals2(number, form1, form2, form3)}"


def plurals2(number, form1, form2, form3):
    if number == 0:
        return form3
    else:
        number = math.fabs(number) % 100
        if 10 < number < 20:
            return form3
        else:
            number %= 10
            if 1 < number < 5:
                return form2
            else:
                return form1 if number == 1 else form3
