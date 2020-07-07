"""
Count how many directories to create
"""

n = int(input())
c = 0
s = set()
for j in range(n):
    path = input()
    for i in range(1, len(path)):
        if path[i - 1] == '/' and path[:i + 1] not in s:
            c += 1
            s.add(path[:i + 1])

print(c)

"""
5
/a/b/c/d/e
/a/b/c/d/e/f
/a/b/c/g
/a/b/c/h
/a/b/c/m/h/a/b

exp: 12
"""

"""
2
/a/b
/b/a

exp: 4
"""
