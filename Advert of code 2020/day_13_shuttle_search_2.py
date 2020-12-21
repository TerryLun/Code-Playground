input()

inp = list(map(int, input().replace('x', '0').split(',')))

step = inp[0]

for i in range(1, len(inp)):

    if not inp[i]:
        continue

    s = 0
    while 1:
        if (inp[0] + step * s + i) % inp[i] == 0:
            inp[0] += step * s
            step *= inp[i]
            break
        s += 1

print(inp[0])
