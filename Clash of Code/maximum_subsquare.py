"""
Given a binary matrix, find out the maximum side length of square sub-matrix with all 1s.
"""

n = int(input())
m = []

for _ in range(n):
    m.append(list(map(int, input().split())))
dp = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(n):
    for j in range(n):
        if m[i][j] == 1:
            dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1] ) + 1

hi = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        hi = max(dp[i][j], hi)

print(hi)

"""
5
0  1  1  0  1
1  1  0  1  0
0  1  1  1  0
1  1  1  1  0
1  1  1  1  1
"""