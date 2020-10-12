"""
https://www.hackerrank.com/challenges/anagram/problem
"""
import collections


def anagram(s):
    if len(s) % 2 != 0:
        return -1
    x = len(s) - 1
    l = s[:x // 2 + 1]
    r = s[x // 2 + 1:]
    c1 = collections.Counter(l)
    c2 = collections.Counter(r)
    z = 0
    for k, v in c1.items():
        if k in c2:
            z += min(v, c2[k])
    y = sum(c1.values()) - z
    return len(l) - z
