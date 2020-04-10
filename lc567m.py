"""
567. Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one
of the first string's permutations is the substring of the second string.

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""


def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    low = 0
    high = len(s1) - 1
    while high < len(s2):
        if is_perm(s1, s2[low:high + 1]):
            return True
        low += 1
        high += 1
    return False


def is_perm(s1, s2):
    def turn_to_tup(s):
        res = [0] * 26
        for c in s:
            res[ord(c) - ord('a')] += 1
        return tuple(res)

    s1 = turn_to_tup(s1)
    s2 = turn_to_tup(s2)
    return s1 == s2


s1 = "ab"
s2 = "eidbaooo"
exp = True
print(checkInclusion(s1, s2) == exp)

s1 = "ab"
s2 = "eidboaoo"
exp = False
print(checkInclusion(s1, s2) == exp)
