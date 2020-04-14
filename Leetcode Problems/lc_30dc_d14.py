"""
30 day Challenge - Day 14 - Perform String Shifts


You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift).
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.

Return the final string after all operations.
"""


def stringShift(s, shift):
    """
    :type s: str
    :type shift: List[List[int]]
    :rtype: str
    """
    sh = 0
    for shi in shift:
        if shi[0] == 0:
            sh -= shi[1]
        else:
            sh += shi[1]
    sh %= len(s)
    print(sh)
    if sh > 0:
        return s[-sh:] + s[:-sh]
    elif sh < 0:
        return s[-sh:] + s[:-sh]
    else:
        return s


s = "abc"
shift = [[0, 1], [1, 2]]
print(stringShift(s, shift))

s = "abcdefg"
shift = [[1, 1], [1, 1], [0, 2], [1, 3]]
print(stringShift(s, shift))

s = "wpdhhcj"
shift = [[0, 7], [1, 7], [1, 0], [1, 3], [0, 3], [0, 6], [1, 2]]
print(stringShift(s, shift))

s = "xqgwkiqpif"
shift = [[1, 4], [0, 7], [0, 8], [0, 7], [0, 6], [1, 3], [0, 1], [1, 7], [0, 5], [0, 6]]
print(stringShift(s, shift))
