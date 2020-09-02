"""
print a 2d palindrome square

inp:
5
S
AR
TEN
OP
R

out:
SATOR
AREPO
TENET
OPERA
ROTAS

------

inp:
5
S
AR
TEN
OP
R

out:
TRAP
RAJA
AJAR
PART

------

inp:
3
W
ON
N

out:
WON
ONO
NOW
"""

n = int(input())
a = [['' for i in range(n)] for j in range(n)]
for i in range(n):
    line = input()
    for j in range(len(line)):
        a[i][j] = line[j]
for i in range(n):
    for j in range(n):
        if not a[i][j]:
            a[i][j] = a[j][i]
        if not a[i][j]:
            a[i][j] = a[n - i - 1][n - j - 1]
for r in a:
    print(*r, sep='')
