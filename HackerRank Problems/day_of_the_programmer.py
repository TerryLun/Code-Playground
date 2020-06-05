"""
https://www.hackerrank.com/challenges/day-of-the-programmer/problem
"""


def dayOfProgrammer(year):
    if year == 1918:
        return '26.09.1918'
    leap = '12.09.'
    nonleap = '13.09.'
    if (year < 1918 and year % 4 == 0) or (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return leap + str(year)
    else:
        return nonleap + str(year)
