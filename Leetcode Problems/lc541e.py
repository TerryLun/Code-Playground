"""
541. Reverse String II

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the
start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but
greater than or equal to k characters, then reverse the first k characters and left the other as original.

Restrictions:
1. The string consists of lower English letters only.
2. Length of the given string and k will in the range [1, 10000]
"""


def reverseStr(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    rev = True
    result = ''

    def reverse(st):
        res = ''
        for c in st:
            res = c + res
        return res

    while len(s) > k:
        result += reverse(s[:k]) if rev else s[:k]
        s = s[k:]
        rev = not rev
    if s and rev:
        result += reverse(s)
    elif s and not rev:
        result += s
    return result


s = "abcdefg"
k = 2
exp = "bacdfeg"
print(reverseStr(s, k) == exp)

s = "abcdef"
k = 2
exp = "bacdfe"
print(reverseStr(s, k) == exp)

s = "abcd"
k = 2
exp = "bacd"
print(reverseStr(s, k) == exp)

s = "ab"
k = 2
exp = "ba"
print(reverseStr(s, k) == exp)

s = ""
k = 2
exp = ""
print(reverseStr(s, k) == exp)
