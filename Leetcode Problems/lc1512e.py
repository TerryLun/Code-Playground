"""
1512. Number of Good Pairs


Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""


def numIdenticalPairs(nums):
    num_dict = {}
    result = 0
    for n in nums:
        if n in num_dict:
            result += num_dict[n]
            num_dict[n] += 1
        else:
            num_dict[n] = 1
    return result
