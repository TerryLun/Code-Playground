"""
https://en.wikipedia.org/wiki/Greatest_common_divisor
"""


def gcd(num1, num2):
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return abs(num2)
