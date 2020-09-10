import collections


def dfs(i, j):
    """
    max recursion depth exceeded
    """
    if i < 0 or i == n or j < 0 or j == m or grid[i][j] == '#':
        return
    else:
        grid[i][j] = '#'
        dfs(i + 1, j)
        dfs(i, j + 1)
        dfs(i - 1, j)
        dfs(i, j - 1)


def bfs(i, j):
    """
    TLE
    """

    def is_floor(x, y):
        if 0 <= x < n and 0 <= y < m and grid[x][y] == '.' and (x, y) not in q and not visited[x][y]:
            return True
        else:
            return False

    q = collections.deque()
    q.append((i, j))
    while q:
        r, c = q.popleft()
        visited[r][c] = True
        dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for d in dir:
            if is_floor(r + d[0], c + d[1]):
                q.append((r + d[0], c + d[1]))


n, m = map(int, input().split())
grid = []
# visited = []
# for i in range(n):
#     visited.append([False] * m)
count = 0

for i in range(n):
    grid.append(list(input()))

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            dfs(i, j)
            count += 1

print(count)
