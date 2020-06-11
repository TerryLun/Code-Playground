def rotate_matrix(mat):
    n = len(mat)
    for x in range(0, n // 2):
        for y in range(x, n - x - 1):
            mat[x][y], mat[y][n - x - 1], mat[n - 1 - x][n - 1 - y], mat[n - y - 1][x] = mat[y][n - x - 1], \
                                                                                         mat[n - 1 - x][n - 1 - y], \
                                                                                         mat[n - y - 1][x], mat[x][y]


def print_matrix(mat):
    for r in mat:
        print(*r)
    print()


def main():
    m = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    print_matrix(m)

    rotate_matrix(m)
    print_matrix(m)

    rotate_matrix(m)
    print_matrix(m)

    rotate_matrix(m)
    print_matrix(m)


if __name__ == '__main__':
    main()
