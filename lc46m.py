"""
46. Permutations

Given a collection of distinct integers, return all possible permutations.
"""
import copy


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def helper(perm, usd):
        if len(perm) == len(nums):
            result.append(copy.deepcopy(perm))
            return
        for i in range(len(nums)):
            if usd[i]:
                continue
            usd[i] = True
            perm.append(nums[i])
            helper(perm, usd)
            perm.pop()
            usd[i] = False

    result = []
    if not nums:
        return result
    used = [False for i in range(len(nums))]
    permutation = []
    helper(permutation, used)
    return result


inp = [1, 2]
exp = [[1, 2], [2, 1]]
print(permute(inp) == exp)

inp = [1, 2, 3]
exp = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]
print(permute(inp) == exp)