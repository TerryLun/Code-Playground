"""
994. Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible,
return -1 instead.

Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""

import collections


def orangesRotting(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    que = collections.deque()




inp = [[2,1,1],[1,1,0],[0,1,1]]
exp = 4
print(orangesRotting(inp) == exp)

inp = [[2,1,1],[0,1,1],[1,0,1]]
exp = -1
print(orangesRotting(inp) == exp)

inp = [[0,2]]
exp = 0
print(orangesRotting(inp) == exp)
