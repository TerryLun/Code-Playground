n = int(input())
a = []
for i in input().split():
    p = int(i)
    a.append(p)
b = [[a[0]]]
for i in range(1, len(a)):
    if a[i] - 1 == b[-1][-1]:
        b[-1].append(a[i])
    else:
        b.append([a[i]])
r = ''
for i in range(len(b)):
    if len(b[i]) == 1:
        b[i] = b[i][0]
    else:
        b[i] = str(b[i][0]) + '-' + str(b[i][-1])
print(*b, sep=',')

"""
input:
6
1 2 3 5 7 8

exp output:
1-3,5,7-8
"""
