"""
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.


Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = set()
    for n in nums:
        if n not in count:
            count.add(n)
        else:
            count.remove(n)
    return count.pop()


inp = [1]
exp = 1
print(singleNumber(inp) == exp)

inp = [2, 2, 1]
exp = 1
print(singleNumber(inp) == exp)

inp = [4, 1, 2, 1, 2]
exp = 4
print(singleNumber(inp) == exp)
