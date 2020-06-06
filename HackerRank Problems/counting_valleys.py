"""
https://www.hackerrank.com/challenges/counting-valleys/problem
"""


def countingValleys(n, s):
    h = 0
    c = 0
    for i in s:
        if h == 0 and i == 'D':
            c += 1
            h -= 1
        elif i == 'D':
            h -= 1
        else:
            h += 1
    return c
