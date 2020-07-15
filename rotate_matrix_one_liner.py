def rotate(m):
    return [list(reversed(list(l))) for l in list(zip(*m))]


m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(rotate(m))
