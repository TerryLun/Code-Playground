def number_of_queens(bo):
    total = 0
    for r in bo:
        total += r.count('Q')
    return total


def validate(bo, x, y):
    # row
    if 'Q' in bo[x]:
        return False
    # col
    for r in bo:
        if r[y] == 'Q':
            return False
    # to top left
    for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
        if board[i][j] == 'Q':
            return False
    # to top right
    for i, j in zip(range(x, -1, -1), range(y, 8, 1)):
        if board[i][j] == 'Q':
            return False
    # to bottom left
    for i, j in zip(range(x, 8, 1), range(y, -1, -1)):
        if board[i][j] == 'Q':
            return False
    # to bottom right
    for i, j in zip(range(x, 8, 1), range(y, 8, 1)):
        if board[i][j] == 'Q':
            return False
    return True


def solve(bo):
    if number_of_queens(bo) == 8:
        return True

    for r in range(8):
        for c in range(8):
            if validate(bo, r, c) and bo[r][c] == '_':
                bo[r][c] = 'Q'
                if solve(bo):
                    return True
                bo[r][c] = '_'
    return False


def print_board(bo):
    for r in bo:
        for c in r:
            print(c, end=' ')
        print()


board = [['_' for _ in range(8)] for _ in range(8)]
solve(board)
print_board(board)
