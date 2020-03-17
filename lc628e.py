"""
628. Maximum Product of Three Numbers

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""


def maximumProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    highs = [float('-inf'), float('-inf'), float('-inf')]
    lows = [0, 0]
    for n in nums:
        if n > highs[0]:
            highs[2] = highs[1]
            highs[1] = highs[0]
            highs[0] = n
        elif n > highs[1]:
            highs[2] = highs[1]
            highs[1] = n
        elif n > highs[2]:
            highs[2] = n

        if n < lows[0]:
            lows[1] = lows[0]
            lows[0] = n
        elif n < lows[1]:
            lows[1] = n
    print(highs, lows)
    return max(highs[0] * highs[1] * highs[2], highs[0] * lows[0] * lows[1])


inp = [1, 2, 3]
exp = 6
print(maximumProduct(inp) == exp)

inp = [1, 2, 3, 4]
exp = 24
print(maximumProduct(inp) == exp)

inp = [1, 2, 3, 4, -2, -9]
exp = 4 * -2 * -9
print(maximumProduct(inp) == exp)

inp = [1, 2, 3, 4, -2, -3]
exp = 4 * 2 * 3
print(maximumProduct(inp) == exp)

inp = [1, 2, 3, 4, -2, -1]
exp = 4 * 2 * 3
print(maximumProduct(inp) == exp)

inp = [-1, -2, -3]
exp = -6
print(maximumProduct(inp) == exp)
print(maximumProduct(inp))
