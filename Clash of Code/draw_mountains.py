n = int(input())
lines = [['/\\']]
for i in range(1, n):
    lines.append(['/' + ' ' * (i * 2) + '\\'] + lines[-1])
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if j != len(lines[i]) - 1:
            print(' ' * (n - i - 1) + lines[i][j] + ' ' * (n - i - 1), end='')
        else:
            print(' ' * (n - i - 1) + lines[i][j])
