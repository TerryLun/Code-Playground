"""
https://www.hackerrank.com/challenges/palindrome-index/problem
"""


def palindromeIndex_bf(s):
    """
    brute force O(n^2)
    """
    if s == s[::-1]:
        return -1
    for i in range(len(s)):
        t = s[:i] + s[i + 1:]
        if t == t[::-1]:
            return i
    return -1


def palindromeIndex(s):
    """
    two pointers: O(n)
    """
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            break
        i += 1
        j -= 1
    if i > j:
        return -1

    def helper(x):
        return x == x[::-1]

    if helper(s[i + 1:j + 1]):
        return i
    elif helper(s[i:j]):
        return j
    else:
        return -1
