"""
Counting Elements

Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.
"""


def countElements(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    target = set()
    result = 0
    for n in arr:
        target.add(n - 1)
    for n in arr:
        if n in target:
            result += 1
    return result


inp = [1, 1, 2] #01
exp = 2
print(countElements(inp) == exp)

inp = [1, 1, 2, 2] #01
exp = 2
print(countElements(inp) == exp)

inp = [1, 3, 2, 3, 5, 0] #-10124
exp = 3
print(countElements(inp) == exp)
