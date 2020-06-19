"""
https://www.hackerrank.com/challenges/circular-array-rotation/problem
"""


def circularArrayRotation(a, k, queries):
    r = len(a) - (k % len(a))
    a = a[r:] + a[:r]
    return [a[x] for x in queries]
