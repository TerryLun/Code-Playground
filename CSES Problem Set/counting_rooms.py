import collections

n, m = map(int, input().split())
a = []
count = 0




def dfs(a, i, j):
    """
    max recursion depth exceeded
    """
    if i < 0 or i == n or j < 0 or j == m or a[i][j] == '#':
        return
    else:
        a[i][j] = '#'
        dfs(a, i + 1, j)
        dfs(a, i, j + 1)
        dfs(a, i - 1, j)
        dfs(a, i, j - 1)


def bfs(a, i, j):
    """
    TLE
    """
    def is_floor(x, y):
        if 0 <= x < n and 0 <= y < m and a[x][y] == '.':
            return True
        else:
            return False

    q = collections.deque()
    q.append((i, j))
    while q:
        r, c = q.popleft()
        a[r][c] = "#"
        dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for d in dir:
            if is_floor(r + d[0], c + d[1]):
                q.append((r + d[0], c + d[1]))


for i in range(n):
    a.append(list(input()))

for i in range(n):
    for j in range(m):
        if a[i][j] == '.':
            bfs(a, i, j)
            count += 1

print(count)
