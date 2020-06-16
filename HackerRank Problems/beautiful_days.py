def beautifulDays(i, j, k):
    s = 0
    for n in range(i, j + 1):
        if abs(n - int(str(n)[::-1])) % k == 0:
            s += 1
    return s
