"""
283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements.

Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 0
    while j < len(nums):
        if nums[i] != 0:
            i += 1
        elif nums[j] != 0:
            nums[i] = nums[j]
            i += 1
            nums[i] = 0
        j += 1
    while i < j:
        nums[i] = 0
        i += 1


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)

nums = [1, 0, 0, 3, 12]
moveZeroes(nums)
print(nums)

nums = []
moveZeroes(nums)
print(nums)

nums = [0]
moveZeroes(nums)
print(nums)

nums = [1]
moveZeroes(nums)
print(nums)

nums = [1, 3, 6, 3, 12]
moveZeroes(nums)
print(nums)

nums = [1, 3, 6, 3, 0]
moveZeroes(nums)
print(nums)