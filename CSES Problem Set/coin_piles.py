i = int(input())
for _ in range(i):
    m, n = map(int, input().split(' '))
    if (m + n) % 3 != 0 or max(m, n) / 2 > min(m, n):
        print('NO')
    else:
        print('YES')
