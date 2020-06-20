"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
"""


def jumpingOnClouds(c, k):
    if k == len(c):
        return 99 if c[0] == 0 else 97
    pos = k
    e = 97 if c[pos] == 1 else 99
    while pos != 0 and e > 0:
        pos = (pos + k) % len(c)
        e -= 1
        if c[pos] == 1:
            e -= 2
    return max(e, 0)


c = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1]
k = 19
print(jumpingOnClouds(c, k))
