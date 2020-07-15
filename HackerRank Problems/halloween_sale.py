"""
https://www.hackerrank.com/challenges/halloween-sale/problem
"""


def howManyGames(p, d, m, s):
    r = 0
    while s > 0:
        s -= p
        p = max(p - d, m)
        r += 1
        print(s)
    return r if s == 0 else r - 1


print(howManyGames(20, 3, 6, 80))
