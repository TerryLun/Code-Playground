"""
367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.
"""


def isPerfectSquare(num):
    i = 1
    while num > 0:
        num -= i
        i += 2
    return num == 0


