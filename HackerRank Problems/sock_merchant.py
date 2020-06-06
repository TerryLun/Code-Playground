"""
https://www.hackerrank.com/challenges/sock-merchant/problem
"""


def sockMerchant(n, ar):
    d = {}
    result = 0
    for s in ar:
        if s not in d or d[s] == 0:
            d[s] = 1
        else:
            result += 1
            d[s] = 0
    return result
