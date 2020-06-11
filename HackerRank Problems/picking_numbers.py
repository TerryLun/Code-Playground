"""
https://www.hackerrank.com/challenges/picking-numbers/problem
"""


def pickingNumbers(a):
    c = [0] * 101
    for n in a:
        c[n] += 1
    hi = 0
    for i in range(len(c) - 1):
        hi = max(hi, (c[i] + c[i + 1]))
    return hi


inp = [4, 6, 5, 3, 3, 1]
exp = 3
print(pickingNumbers(inp) == exp)

inp = [1, 2, 2, 3, 1, 2]
exp = 5
print(pickingNumbers(inp) == exp)
