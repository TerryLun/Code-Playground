from collections import deque

# E S W N
pos = deque([0, 0, 0, 0])
piv = deque([10, 0, 0, 1])

while 1:
    line = input()
    if not line:
        break

    d = line[0]
    n = int(line[1:])

    if d == 'N':
        piv[3] += n
    elif d == 'S':
        piv[1] += n
    elif d == 'E':
        piv[0] += n
    elif d == 'W':
        piv[2] += n

    elif d == 'R':
        n //= 90
        piv.rotate(n)
    elif d == 'L':
        n //= 90
        piv.rotate(-n)

    elif d == 'F':
        for i in range(4):
            pos[i] += piv[i] * n

print(abs(pos[0] - pos[2]) + abs(pos[1] - pos[3]))
