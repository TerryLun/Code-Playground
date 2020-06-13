# 0 1 2 3    4 5 6 7    8  9 10 11 (3,7,11)
# 1 2 3 4    5 6 7 8    9 10 11 12 (4,8,12)

n = int(input())
if (n + 1) % 4 == 0:
    print('YES')
    f = []
    s = []
    for i in range(1, n + 1):
        if i % 4 == 3 or i % 4 == 0:
            f.append(i)
        else:
            s.append(i)
    print(len(f))
    print(*f)
    print(len(s))
    print(*s)
elif n % 4 == 0:
    print('YES')
    f = []
    s = []
    for i in range(1, n + 1):
        if i % 4 == 1 or i % 4 == 0:
            f.append(i)
        else:
            s.append(i)
    print(len(f))
    print(*f)
    print(len(s))
    print(*s)
else:
    print('NO')
