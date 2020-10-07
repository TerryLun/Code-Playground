"""
https://www.hackerrank.com/challenges/string-construction/problem
"""


def stringConstruction(s):
    a = set()
    r = 0
    for c in s:
        if c not in a:
            r += 1
        a.add(c)
    return len(a)
