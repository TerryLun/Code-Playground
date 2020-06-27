"""
https://www.hackerrank.com/challenges/cut-the-sticks/problem
"""
import collections


def cutTheSticks(arr):
    c = dict(collections.Counter(arr))
    r = []
    while c:
        r.append(sum(c.values()))
        c.pop(min(c.keys()))
    return r
