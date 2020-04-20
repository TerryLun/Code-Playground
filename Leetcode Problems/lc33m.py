"""
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        lo = 0
        hi = len(nums) - 1

        # find pivot
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        # lo is the pivot
        start = lo
        lo = 0
        hi = len(nums) - 1

        # now we have two sorted array
        # decide which one to search
        if nums[start] <= target <= nums[hi]:
            lo = start
        else:
            hi = start

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


s = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
exp = 4
print(s.search(nums, target) == exp)

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
exp = -1
print(s.search(nums, target) == exp)
