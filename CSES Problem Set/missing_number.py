n = int(input())
s = 0
s = list(map(int, input().split(' ')))
ss = n * (1 + n) // 2
print(ss - sum(s))
