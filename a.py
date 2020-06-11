import copy

import magic_square
import rotate_matrix
import flip_matrix


def generate_magic_squares_three_by_three():
    magic_squares = []

    m = magic_square.solve(3)
    magic_squares.append(copy.deepcopy(m))

    for _ in range(3):
        rotate_matrix.rotate_matrix(m)
        magic_squares.append(copy.deepcopy(m))

    flip_matrix.flip_matrix_horizontal(m)
    magic_squares.append(copy.deepcopy(m))

    for _ in range(3):
        rotate_matrix.rotate_matrix(m)
        magic_squares.append(copy.deepcopy(m))

    return magic_squares


def main():
    sq = generate_magic_squares_three_by_three()
    for i in sq:
        for r in i:
            print(*r)
        print()


if __name__ == '__main__':
    main()
