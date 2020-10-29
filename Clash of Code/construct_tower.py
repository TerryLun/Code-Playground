"""
test cases:

in:
257
3 7
out:
83

in:
257
3 7
out:
83
"""

import sys

sys.setrecursionlimit(int(1e7))

n = int(input())
p, q = [int(i) for i in input().split()]

x = {}


def dp(n):
    if n in x: return x[n]
    if n == 0:
        return 0
    elif n < 0:
        return -1e9
    else:
        x[n] = max(dp(n - p) + 1, dp(n - q) + 1)
        return x[n]


print(max(0, dp(n)))
