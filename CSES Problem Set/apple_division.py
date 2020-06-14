"""
TC7-12 TLE
"""

import itertools
import math
import copy

n = int(input())
a = list(map(int, input().split(' ')))
md = float('inf')
for i in range(1, math.ceil(n / 2) + 1):
    c = itertools.combinations(a, i)
    for left in c:
        right = copy.deepcopy(a)
        for leftn in left:
            right.remove(leftn)
        md = min(md, abs(sum(left) - sum(right)))
print(md)
