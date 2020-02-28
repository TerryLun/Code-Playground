from numpy import matrix
import time


def number_of_queens(bo):
    total = 0
    for r in bo:
        total += r.count(1)
    return total


def validate(bo, x, y):
    # row
    if 1 in bo[x]:
        return False
    # col
    for r in bo:
        if r[y] == 1:
            return False
    # to top left
    for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
        if board[i][j] == 1:
            return False
    # to top right
    for i, j in zip(range(x, -1, -1), range(y, 8, 1)):
        if board[i][j] == 1:
            return False
    # to bottom left
    for i, j in zip(range(x, 8, 1), range(y, -1, -1)):
        if board[i][j] == 1:
            return False
    # to bottom right
    for i, j in zip(range(x, 8, 1), range(y, 8, 1)):
        if board[i][j] == 1:
            return False
    return True


def solve(bo):
    if number_of_queens(bo) == 8:
        return True

    for r in range(8):
        for c in range(8):
            if validate(bo, r, c) and bo[r][c] == 0:
                bo[r][c] = 1
                if solve(bo):
                    return True
                bo[r][c] = 0
    return False


board = [[0 for _ in range(8)] for _ in range(8)]
solve(board)
print(matrix(board))
