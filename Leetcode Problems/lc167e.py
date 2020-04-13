"""
167. Two Sum II - Input array is sorted
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


def twoSum(numbers, target):
    lo = 0
    hi = len(numbers) - 1
    while lo <= hi:
        s = numbers[lo] + numbers[hi]
        if s > target:
            hi -= 1
        elif s < target:
            lo += 1
        else:
            return [lo+1, hi+1]


print(twoSum([2, 7, 11, 15], 9))
