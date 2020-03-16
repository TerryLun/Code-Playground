"""
476. Number Complement

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary
representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
"""


def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    n = 1
    a = 1
    while n < num:
        n = 2 ** a - 1
        a += 1
    return n - num
