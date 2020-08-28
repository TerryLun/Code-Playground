"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer
overflows.
"""


def reverse(x):
    r = 0
    if not -2 ** 31 < x < 2 ** 31 - 1:
        return r
    neg = False
    if x < 0:
        neg = True
        x = -x
    while x:
        r = r * 10 + x % 10
        x //= 10
    if not -2 ** 31 < r < 2 ** 31 - 1:
        return 0
    return r if not neg else -r
