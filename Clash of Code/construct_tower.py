"""
sample test case:

in:
257
3 7
out:
83
"""

"""
dp
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

"""
simple
"""
big = 0
small = 0

while n > 0:
    if n % p == 0:
        small = n // p
        break
    else:
        if (n - p > 0):
            n -= q
            big += 1
        else:
            break

if (n % p != 0):
    print(0)
else:
    print(small + big)
