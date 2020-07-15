"""
https://www.hackerrank.com/challenges/minimum-distances/problem
"""


def minimumDistances(a):
    d = {}
    r = float('inf')
    for i in range(len(a)):
        if a[i] in d:
            r = min(r, i-d[a[i]])
        d[a[i]] = i
    return r if r != float('inf') else -1
