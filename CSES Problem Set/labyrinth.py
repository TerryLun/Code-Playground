"""
TLE
"""

import collections

n, m = map(int, input().split())
maze = []
found = False
visited = [[False for c in range(m)] for r in range(n)]
start = None
for r in range(n):
    line = input()
    maze.append(line)
    if 'A' in line:
        start = (r, line.index('A'))

q = collections.deque()

q.append((start, ''))
visited[start[0]][start[1]] = True

while q:
    pos, path = q.popleft()
    row, col = pos
    if maze[row][col] == 'B':
        found = True
        print('YES')
        print(len(path))
        print(path)
        break
    if col + 1 < m and maze[row][col + 1] != '#' and not visited[row][col + 1]:
        visited[row][col+1] = True
        q.append(((row, col + 1), path+'R'))
    if col - 1 >= 0 and maze[row][col - 1] != '#' and not visited[row][col - 1]:
        visited[row][col - 1] = True
        q.append(((row, col - 1), path+'L'))
    if row + 1 < n and maze[row + 1][col] != '#' and not visited[row + 1][col]:
        visited[row + 1][col] = True
        q.append(((row + 1, col), path+'D'))
    if row - 1 >= 0 and maze[row - 1][col] != '#' and not visited[row - 1][col]:
        visited[row - 1][col] = True
        q.append(((row - 1, col), path+'U'))

if not found:
    print('NO')