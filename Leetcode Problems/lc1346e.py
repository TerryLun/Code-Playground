"""
1346. Check If N and Its Double Exist

Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Constraints:
2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3
"""


def checkIfExist(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    target = set()
    for n in arr:
        if n in target:
            return True
        else:
            target.add(n * 2)
            target.add(n / 2)
    return False


inp = [3, 1, 7, 11]
exp = False
print(checkIfExist(inp) == exp)
