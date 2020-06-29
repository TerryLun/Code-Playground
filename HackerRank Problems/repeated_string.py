"""
https://www.hackerrank.com/challenges/repeated-string/problem
"""


def repeatedString(s, n):
    a = s.count('a') * (n // len(s))
    b = s[:n % len(s)].count('a')
    return a + b
