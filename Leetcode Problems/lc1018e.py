"""
1018. Binary Prefix Divisible By 5

Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number
(from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

Note:
1 <= A.length <= 30000
A[i] is 0 or 1
"""


def prefixesDivBy5(A):
    """
    :type A: List[int]
    :rtype: List[bool]
    """
    num = 0
    result = []
    for a in A:
        num = num * 2 if a == 0 else num * 2 + 1
        result.append(True if num % 5 == 0 else False)
    return result


inp = [0, 1, 1]
exp = [True, False, False]
print(prefixesDivBy5(inp) == exp)
inp = [1, 1, 1]
exp = [False, False, False]
print(prefixesDivBy5(inp) == exp)
inp = [0, 1, 1, 1, 1, 1]
exp = [True, False, False, False, True, False]
print(prefixesDivBy5(inp) == exp)
inp = [1, 1, 1, 0, 1]
exp = [False, False, False, False, False]
print(prefixesDivBy5(inp) == exp)
