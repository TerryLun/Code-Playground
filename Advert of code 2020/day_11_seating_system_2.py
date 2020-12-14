mat = []

while 1:
    line = input()
    if not line:
        break
    mat.append(list(line))


def find_occupied(mat, i, j):
    r = 0
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if not di == dj == 0:
                ii = i + di
                jj = j + dj
                while 0 <= ii < len(mat) and 0 <= jj < len(mat[0]) and mat[ii][jj] == '.':
                    ii = ii + di
                    jj = jj + dj
                if 0 <= ii < len(mat) and 0 <= jj < len(mat[0]) and mat[ii][jj] == '#':
                    r += 1
    return r


while 1:
    temp = [['.' for j in range(len(mat[0]))] for i in range(len(mat))]
    changed = 0

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 'L' and find_occupied(mat, i, j) == 0:
                temp[i][j] = '#'
                changed += 1
            elif mat[i][j] == '#' and find_occupied(mat, i, j) >= 5:
                temp[i][j] = 'L'
                changed += 1
            else:
                temp[i][j] = mat[i][j]

    mat = temp

    if not changed:
        break
    print('changed', changed)

r = 0
for i in mat:
    for j in i:
        if j == "#":
            r += 1
print(r)
