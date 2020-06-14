"""
http://oeis.org/A172132
"""

i = int(input())
for n in range(1, i + 1):
    print((n - 1) * (n + 4) * (n ** 2 - 3 * n + 4) // 2)
