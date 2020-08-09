"""
https://www.hackerrank.com/challenges/mars-exploration/problem
"""


def marsExploration(s):
    m = 'SOS'
    r = 0
    for i in range(len(s)):
        if s[i] != m[i % 3]:
            r += 1
    return r
