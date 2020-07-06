"""
1504. Count Submatrices With All Ones

Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

Example 1:

Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2.
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.

Example 2:

Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3.
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2.
There are 2 rectangles of side 3x1.
There is 1 rectangle of side 3x2.
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.

Example 3:

Input: mat = [[1,1,1,1,1,1]]
Output: 21

Example 4:

Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
Output: 5


Constraints:

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1
"""


def count(dp, mat):
    row = len(mat)
    col = len(mat[0])
    for i in range(0, row):
        for j in range(col - 1, -1, -1):
            if not mat[i][j]:
                continue
            if j != col - 1:
                dp[i][j] += dp[i][j + 1]
            dp[i][j] += mat[i][j]


def numSubmat(mat):
    row = len(mat)
    col = len(mat[0])
    dp = [[0 for i in range(col)] for j in range(row)]
    count(dp, mat)
    ans = 0

    for j in range(0, col):
        i = row - 1
        q = []
        to_sum = 0

        while i >= 0:
            c = 0
            while len(q) != 0 and q[-1][0] > dp[i][j]:
                to_sum -= (q[-1][1] + 1) * (q[-1][0] - dp[i][j])
                c += q[-1][1] + 1
                q.pop()
            to_sum += dp[i][j]
            ans += to_sum
            q.append((dp[i][j], c))
            i -= 1

    return ans
