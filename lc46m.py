"""
46. Permutations

Given a collection of distinct integers, return all possible permutations.
"""
import copy
import math
import itertools


# using library
def permute(nums):
    return list(map(list, list(itertools.permutations(nums))))


# backtracking
def backtrack(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def helper(perm, usd):
        # if perm list is finished, then it is a valid list to append to the result
        if len(perm) == len(nums):
            result.append(copy.deepcopy(perm))
            return
        for i in range(len(nums)):
            # ignore used, try next
            if usd[i]:
                continue
            # if number has not been used, append to perm then set to true
            perm.append(nums[i])
            usd[i] = True
            # next position
            helper(perm, usd)
            # backtracks
            perm.pop()
            usd[i] = False

    result = []
    if not nums:
        return [[]]
    used = [False for i in range(len(nums))]
    permutation = []
    helper(permutation, used)
    return result


# another way to do this
def copy_and_insert(nums):
    if not nums:
        return [[]]
    # make first list containing first number
    result = [[nums[0]]]

    for i in range(1, len(nums)):
        # make copy of existing lists in result and append i times
        temp = result[:]
        for _ in range(i):
            for ls in temp:
                result.append(copy.deepcopy(ls))
        # insert the number in nums to appropriate position
        for j in range(len(result)):
            result[j].insert(j // math.factorial(i), nums[i])
    return result


def compare(*lists):
    def convert(ls):
        list_str = []
        for l in ls[:]:
            s = [str(i) for i in l]
            list_str.append(''.join(s))
        return set(list_str)

    collector = []
    for lst in lists:
        collector.append(convert(lst))
    return collector[1:] == collector[:-1]


# tests
inp = []
exp = [[]]
print(permute(inp) == exp)

inp = [1]
exp = [[1]]
print(permute(inp) == exp)

inp = [1, 0]
exp = [[1, 0], [0, 1]]
print(permute(inp) == exp)

inp = [1, 2, 3]
exp = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(permute(inp) == exp)

inp = [1, 2, 3, 4]
exp = [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2],
       [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1],
       [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1],
       [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
print(permute(inp) == exp)

res1 = permute(inp)
res2 = backtrack(inp)
res3 = copy_and_insert(inp)
print(compare(res1, res2, res3))
