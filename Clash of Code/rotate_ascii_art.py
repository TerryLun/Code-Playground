"""
golf: rotate ascii art

inp:
4 6
0--0
1=-1
1=-1
1=-1
1=-1
0--0
"""

for x in[c[::-1]for c in list(zip(*[input()for i in' '*int(input().split()[1])]))]:print(*x,sep='')