"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and
return its sum.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is
more subtle.
"""


def dp(nums):
    # global_sum = 0
    # current_sum = nums[0]
    # for i in range(1, len(nums)):
    #     current_sum = max(nums[i], current_sum + nums[i])
    #     if current_sum > global_sum:
    #         global_sum = current_sum
    # return global_sum

    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] = nums[i] + nums[i - 1]
    return max(nums)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(dp(nums) == 6)
