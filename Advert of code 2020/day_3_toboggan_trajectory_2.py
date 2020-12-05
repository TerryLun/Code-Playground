a = []
mat = []
while 1:
    line = input()
    if not line:
        break

    mat.append(line)

print("eoi")


def num_trees(m, dx, dy) -> int:
    r = 0
    x = y = 0
    while y < len(m):
        if m[y][x] == '#':
            r += 1
        x += dx
        if x >= len(m[0]):
            x %= len(m[0])
        y += dy
    return r


result = 1
result *= num_trees(mat, 1, 1)
result *= num_trees(mat, 3, 1)
result *= num_trees(mat, 5, 1)
result *= num_trees(mat, 7, 1)
result *= num_trees(mat, 1, 2)
print(result)
