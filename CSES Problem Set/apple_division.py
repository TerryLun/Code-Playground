import itertools
import math

n = int(input())
a = list(map(int, input().split(' ')))
s = sum(a)
md = float('inf')
for i in range(1, math.ceil(n / 2) + 1):
    c = itertools.combinations(a, i)
    for left in c:
        sl = sum(left)
        md = min(md, abs(sl * 2 - s))
print(md)
