"""
1295. Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain an even number of digits.

Constraints:
1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""


def findNumbers(nums):
    r = 0
    for n in nums:
        if 9 < n < 100 or 999 < n < 10000 or n == 100000:
            r += 1
    return r
