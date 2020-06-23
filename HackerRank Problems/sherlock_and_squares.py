"""
https://www.hackerrank.com/challenges/sherlock-and-squares/problem
"""

import math


def squares(a, b):
    sqa = math.sqrt(a)
    sqb = math.sqrt(b)
    return math.floor(sqb) - math.ceil(sqa) + 1
