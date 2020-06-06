"""
https://www.hackerrank.com/challenges/30-binary-numbers/problem
"""

import re


def maximum_consecutive_ones(n):
    b = bin(n).replace('0b', '')
    a = re.split('0+', b)
    return max([len(x) for x in a])
