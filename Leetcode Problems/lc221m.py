"""
221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""


def maximalSquare(matrix):
    if not matrix:
        return 0
    row = len(matrix)
    col = len(matrix[0])
    new_mat = [[0 for i in range(col + 1)]]
    for m in matrix:
        new_mat.append([0] + m)
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if new_mat[i][j] == '1':
                new_mat[i][j] = int(min(new_mat[i - 1][j], new_mat[i - 1][j - 1], new_mat[i][j - 1])) + 1
            else:
                new_mat[i][j] = 0
    res = 0
    for m in new_mat:
        for i in m:
            res = max(res, i)
    return res ** 2


m = [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]
print(maximalSquare(m))
