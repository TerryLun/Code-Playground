"""
https://www.hackerrank.com/challenges/append-and-delete/problem
"""


def appendAndDelete(s, t, k):
    i = 0
    same = 0
    while i < min(len(s), len(t)):
        if s[i] == t[i]:
            same += 1
            i += 1
        else:
            break
    diff = len(s) - same + len(t) - same
    if k >= len(s) + len(t):
        return 'Yes'
    elif same == 0:
        return 'Yes' if k >= diff else 'No'
    else:
        return 'Yes' if (k >= diff and k % 2 == diff % 2) else 'No'
