"""
https://en.wikipedia.org/wiki/Least_common_multiple
"""

from euclidean_gcd import gcd


def lcm(num1, num2):
    return abs(int(num1 * num2 / gcd(num1, num2)))

