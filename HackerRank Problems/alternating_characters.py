"""
https://www.hackerrank.com/challenges/alternating-characters/problem
"""


def alternatingCharacters(s):
    r = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            r += 1
    return r
