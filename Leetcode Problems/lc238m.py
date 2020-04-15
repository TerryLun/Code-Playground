"""
238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of

all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole
array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of
space complexity analysis.)
"""


def productExceptSelf(nums):
    length = len(nums)
    L, R, res = [0] * length, [0] * length, [0] * length

    L[0] = 1
    for i in range(1, length):
        L[i] = L[i - 1] * nums[i - 1]

    R[-1] = 1
    for i in range(-2, -length - 1, -1):
        R[i] = R[i + 1] * nums[i + 1]

    for i in range(length):
        res[i] = L[i] * R[i]

    return res


inp = [1, 2, 3, 4]
exp = [24, 12, 8, 6]
print(productExceptSelf(inp) == exp)
