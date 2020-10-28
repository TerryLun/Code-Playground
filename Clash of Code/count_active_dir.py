"""
2
/a/b
/b/a
"""
folders = {}

total = 0

n = int(input())
for i in range(n):
    path = input().split('/')[1:]
    current = folders
    for d in path:
        if d not in current:
            total += 1
            current[d] = {}
        current = current[d]

print(total)
