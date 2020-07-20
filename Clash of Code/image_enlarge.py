fact = int(input())
dim = int(input())
r = []
for i in range(dim):
    r.append([])
    for j in input().split():
        p = int(j)
        for k in range(fact):
            r[-1].append(p)

for i in r:
    for j in range(fact):
        print(*i)

"""
input:
4
3
1 2 3
4 5 6
7 8 9

output:
1 1 1 1 2 2 2 2 3 3 3 3
1 1 1 1 2 2 2 2 3 3 3 3
1 1 1 1 2 2 2 2 3 3 3 3
1 1 1 1 2 2 2 2 3 3 3 3
4 4 4 4 5 5 5 5 6 6 6 6
4 4 4 4 5 5 5 5 6 6 6 6
4 4 4 4 5 5 5 5 6 6 6 6
4 4 4 4 5 5 5 5 6 6 6 6
7 7 7 7 8 8 8 8 9 9 9 9
7 7 7 7 8 8 8 8 9 9 9 9
7 7 7 7 8 8 8 8 9 9 9 9
7 7 7 7 8 8 8 8 9 9 9 9
"""