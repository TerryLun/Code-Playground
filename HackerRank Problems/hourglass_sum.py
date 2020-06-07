"""
https://www.hackerrank.com/challenges/30-2d-arrays/problem
"""


def shape_sum(i, j, ar):
    shape = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)]
    result = 0
    for pos in range(len(shape)):
        result += ar[shape[pos][0] + i][shape[pos][1] + j]
    return result


def hourglass_sum(arr):
    sums = []
    for i in range(len(arr) - 2):
        for j in range(len(arr[0]) - 2):
            sums.append(shape_sum(i, j, arr))
    return max(sums)


arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]
print(hourglass_sum(arr))
