"""
525. Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""


def findMaxLength(nums):
    count = 0
    res = 0
    cnt_pos = {0: 0}
    for i, n in enumerate(nums, 1):
        count += 1 if n == 0 else -1
        if count in cnt_pos.keys():
            res = max(res, i - cnt_pos[count])
        else:
            cnt_pos[count] = i
    return res


inp = [0, 1]
exp = 2
print(findMaxLength(inp))
