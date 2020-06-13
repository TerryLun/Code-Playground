for i in range(int(input())):
    r, c = map(int, input().split())
    if r <= c:
        if c % 2 != 0:
            print(c ** 2 - r + 1)
        else:
            print((c - 1) ** 2 + 1 + r - 1)
    else:
        if r % 2 == 0:
            print(r ** 2 - c + 1)
        else:
            print((r - 1) ** 2 + 1 + c - 1)
