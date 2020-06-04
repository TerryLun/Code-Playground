def divisibleSumPairs(n, k, ar):
    hi = max(ar)
    lo = min(ar)
    d = {}
    result = 0
    for num in ar:
        if num in d:
            result += d[num]
        for f in range(k - num, hi + 1, k):
            if f in d:
                d[f] += 1
            else:
                d[f] = 1
        for b in range(-num, lo - 1, -k):
            if b in d:
                b[f] += 1
            else:
                b[f] = 1
    return result
