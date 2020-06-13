n = int(input())
if 1 < n < 4:
    print('NO SOLUTION')
else:
    l = []
    r = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            l.append(i)
        else:
            r.append(i)
    l += r
    print(*l)
