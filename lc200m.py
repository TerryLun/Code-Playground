"""
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.
"""
import collections


def numIslands(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '1':
                count += 1
                bfs(grid, r, c)
    return count


def dfs(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] == '0':
        return
    grid[r][c] = '0'
    dfs(grid, r + 1, c)
    dfs(grid, r - 1, c)
    dfs(grid, r, c + 1)
    dfs(grid, r, c - 1)


def bfs(grid, r, c):
    que = collections.deque()
    que.append((r, c))
    while que:
        r, c = que.popleft()
        grid[r][c] = '0'
        for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = r + direction[0]
            nc = c + direction[1]
            if len(grid) > nr >= 0 and len(grid[0]) > nc >= 0 and grid[nr][nc] == '1':
                que.append((nr, nc))


# unit tests
grid = [["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]
got = numIslands(grid)
expected = 1
print(got == expected)

grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]
got = numIslands(grid)
expected = 3
print(got == expected)
