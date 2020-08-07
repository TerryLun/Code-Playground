"""
https://www.hackerrank.com/challenges/reduced-string/problem
"""


def superReducedString(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]
            i -= 1 if i > 0 else i
        else:
            i += 1
    return s if s else 'Empty String'
