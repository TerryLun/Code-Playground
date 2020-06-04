import random
import time


def divisibleSumPairs(n, k, ar):
    """
    O(n)
    """
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
                d[b] += 1
            else:
                d[b] = 1
    return result


def bruteForce(n, k, ar):
    """
    O(n*n)
    """
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                result += 1
    return result


inp = [random.randint(1, 10) for _ in range(10000)]
k = 3
n = len(inp)

start = time.time()
print(divisibleSumPairs(n, k, inp))
print(time.time() - start)

start = time.time()
print(bruteForce(n, k, inp))
print(time.time() - start)
