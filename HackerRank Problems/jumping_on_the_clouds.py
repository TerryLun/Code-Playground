"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
"""


def jumpingOnClouds(c):
    e = len(c) - 1
    i = 0
    r = 0
    while i != e:
        if i + 2 <= e and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        r += 1
    return r
