"""
1221. Split a String in Balanced Strings

Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.

Constraints:
1 <= s.length <= 1000
s[i] = 'L' or 'R'
"""


def balancedStringSplit(s):
    r = []
    i = 1
    while s:
        if s[:i].count('L') == s[:i].count('R'):
            r.append(s[:i])
            s = s[i:]
            i = 0
        i += 1
    return len(r)
