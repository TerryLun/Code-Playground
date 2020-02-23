"""
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


def twoSum(nums, target):
    comp = {}
    for i in range(len(nums)):
        if nums[i] in comp.keys():
            return [comp[nums[i]], i]
        else:
            comp[target - nums[i]] = i


print(twoSum([2, 7, 11, 15], 9) == [0, 1])
