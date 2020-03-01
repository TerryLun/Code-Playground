"""
46. Permutations

Given a collection of distinct integers, return all possible permutations.
"""

import itertools


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return itertools.permutations(nums)