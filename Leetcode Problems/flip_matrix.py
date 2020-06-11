def flip_matrix_horizontal(mat):
    n = len(mat)
    for r in mat:
        for y in range(0, n // 2):
            r[y], r[n - y - 1] = r[n - y - 1], r[y]


def print_matrix(mat):
    for r in mat:
        print(*r)
    print()


def main():
    m = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    print_matrix(m)

    flip_matrix_horizontal(m)
    print_matrix(m)

    flip_matrix_horizontal(m)
    print_matrix(m)

    flip_matrix_horizontal(m)
    print_matrix(m)


if __name__ == '__main__':
    main()