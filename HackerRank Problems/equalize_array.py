"""
https://www.hackerrank.com/challenges/equality-in-a-array/problem
"""
import collections


def equalizeArray(arr):
    c = dict(collections.Counter(arr))
    return len(arr) - max(c.values())
