"""
1486. XOR Operation in an Array


Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

Constraints:
1 <= n <= 1000
0 <= start <= 1000
n == nums.length
"""


def xorOperation(n: int, start: int) -> int:
    result = start
    for n in range(start + 2, start + n * 2 - 1, 2):
        result ^= n
    return result
