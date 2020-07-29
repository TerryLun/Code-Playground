"""
1528. Shuffle String

Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Constraints:
s.length == indices.length == n
1 <= n <= 100
s contains only lower-case English letters.
0 <= indices[i] < n
All values of indices are unique (i.e. indices is a permutation of the integers from 0 to n - 1).
"""


def restoreString(s, indices):
    result = ['1'] * len(s)
    for i in range(len(indices)):
        result[indices[i]] = s[i]
    return ''.join(result)
