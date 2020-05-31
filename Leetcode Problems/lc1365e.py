"""
1365. How Many Numbers Are Smaller Than the Current Number


Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each
nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""


def smallerNumbersThanCurrent(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    count = [0 for _ in range(0, 101)]
    result = []
    for n in nums:
        count[n] += 1
    for i in range(1, len(count) - 1):
        count[i] += count[i - 1]
    for n in nums:
        if n == 0:
            result.append(0)
        else:
            result.append(count[n - 1])
    return result


# unit tests
ls = [6, 5, 4, 8]
exp = [2, 1, 0, 3]
print(exp == smallerNumbersThanCurrent(ls))

ls = [8, 1, 2, 2, 3]
exp = [4, 0, 1, 1, 3]
print(exp == smallerNumbersThanCurrent(ls))
