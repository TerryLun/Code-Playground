"""
n1
4
n2 n3
n4 n2
n1 n2
n3 n4
"""
s = input()
n = int(input())
d = {}
for i in ' ' * n:
    a, b = input().split()
    if a in d:
        d[a].append(b)
    else:
        d[a] = [b]
        d[b] = []
v = {k: False for k in d.keys()}


def dfs(n):
    v[n] = True
    for x in d[n]:
        if v[x]:
            print('cycle')
            exit()
        else:
            dfs(x)


dfs(s)

print('no cycle')
