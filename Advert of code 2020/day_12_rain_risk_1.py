x = 0
y = 0
dir = 0

while 1:
    line = input()
    if not line:
        break

    d = line[0]
    n = int(line[1:])

    if d == 'R':
        n //= 90
        dir += n
        dir %= 4
    elif d == 'L':
        n //= 90
        dir -= n
        dir %= 4
    elif d == 'F':
        if dir == 3:
            y += n
        elif dir == 1:
            y -= n
        elif dir == 0:
            x += n
        elif dir == 2:
            x -= n
    elif d == 'N':
        y += n
    elif d == 'S':
        y -= n
    elif d == 'E':
        x += n
    elif d == 'W':
        x -= n

print(abs(x) + abs(y))
