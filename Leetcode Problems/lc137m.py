"""
137. Single Number II

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once.
Find that single one.


Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = {}
    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    for k, v in count.items():
        if v == 1:
            return k


inp = [2, 2, 3, 2]
exp = 3
print(singleNumber(inp) == exp)

inp = [0, 1, 0, 1, 0, 1, 99]
exp = 99
print(singleNumber(inp) == exp)
