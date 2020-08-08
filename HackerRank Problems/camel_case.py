"""
https://www.hackerrank.com/challenges/camelcase/problem
"""

import re


def camelcase(s):
    a = re.findall(r'[A-Z]', s)
    return len(a) + 1
