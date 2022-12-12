"""
Description:
Module to format numbers to
find their right declination

Creation date: 01/11/2022

Author: Aleksandr Gordienko
Version: 0.11A
"""
import math


def plurals(number, form1, form2, form3, splitter=" "):
    """
    Function to format numbers to string
    with various declinations

    @param number - number to process declination
    @param form1 - form for numbers ending on 1
    @param form2 - form for numbers ending on from 2 to 4
    @param form3 - form for numbers ending on from 5 to 0

    @return line number with splitter and selected form
    """
    return f"{str(number).zfill(2)}{splitter}{plurals2(number, form1, form2, form3)}"


def plurals2(number, form1, form2, form3):
    """
    Function to format numbers and return their
    declination

    @param number - number to process declination
    @param form1 - form for numbers ending on 1
    @param form2 - form for numbers ending on from 2 to 4
    @param form3 - form for numbers ending on from 5 to 0

    @return right form for number
    """
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
