"""
703. Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains
initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth
largest element in the stream.

Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        store = []
        low_i = 0
        if len(nums) < k:
            for n in nums:
                store.append(n)
        else:
            for i in range(0, k):
                store.append(nums[i])
            low_i = store.index(min(store))
        for i in range(k, len(nums)):
            if nums[i] > store[low_i]:
                store[low_i] = nums[i]
                low_i = store.index(min(store))
        self.__nums = store
        self.__low_i = low_i
        self.__k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.__nums) < self.__k:
            self.__nums.append(val)
            self.__low_i = self.__nums.index(min(self.__nums))
            return self.__nums[self.__low_i]
        if val > self.__nums[self.__low_i]:
            self.__nums[self.__low_i] = val
            self.__low_i = self.__nums.index(min(self.__nums))
        return self.__nums[self.__low_i]


k = 3
arr = [4, 5, 8, 2]
kthLargest = KthLargest(k, arr)
print(kthLargest.add(3) == 4)
print(kthLargest.add(5) == 5)
print(kthLargest.add(10) == 5)
print(kthLargest.add(9) == 8)
print(kthLargest.add(4) == 8)

k = 2
arr = [0]
kthLargest2 = KthLargest(k, arr)
print(kthLargest2.add(-1) == -1)
print(kthLargest2.add(1) == 0)
print(kthLargest2.add(-2) == 0)
print(kthLargest2.add(-4) == 0)
print(kthLargest2.add(3) == 1)

k = 3
arr = [5, -1]
kthLargest3 = KthLargest(k, arr)
print(kthLargest3.add(2) == -1)
print(kthLargest3.add(1) == 1)
print(kthLargest3.add(-1) == 1)
print(kthLargest3.add(3) == 2)
print(kthLargest3.add(4) == 3)
