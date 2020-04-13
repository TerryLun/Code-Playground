"""
643. Maximum Average Subarray I

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""


def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    sums = sum(nums[:k])
    maxs = sums
    for i in range(k, len(nums)):
        sums += nums[i] - nums[i - k]
        maxs = max(maxs, sums)
    return maxs / k


inp = [1, 12, -5, -6, 50, 3]
k = 4
exp = 12.75
print(findMaxAverage(inp, k))
