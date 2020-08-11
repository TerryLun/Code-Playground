"""
https://www.hackerrank.com/challenges/pangrams/problem
"""


def pangrams(s):
    a = [0] * 26
    for c in s:
        if c.isalpha():
            a[ord(c.lower()) - ord('a')] = 1
    return 'not pangram' if 0 in a else 'pangram'
