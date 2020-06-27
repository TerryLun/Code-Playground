"""
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every
element is distinct.

"""


def contains_duplicate(nums):
    numbers = set()
    for num in nums:
        if num in numbers:
            return True
        else:
            numbers.add(num)
    return False


ls = [[1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]
expected = [True, False, True]
for l, e in zip(ls, expected):
    if contains_duplicate(l) == e:
        print('ok')
    else:
        print('oops')
