"""
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.
"""


from numpy import matrix


def solve(board):
    if not find_empty(board):
        return True
    else:
        x, y = find_empty(board)
    for num in range(1, 10):
        if validate(board, str(num), (x, y)):
            board[x][y] = str(num)
            if solve(board):
                return True
            board[x][y] = '.'
    return False


def find_empty(bo):
    for i in range(0, len(bo)):
        for j in range(0, len(bo[i])):
            if bo[i][j] == '.':
                return i, j
    return None


def validate(bo, num, pos):
    x, y = pos
    # row
    if num in bo[x]:
        return False
    # col
    for r in bo:
        if num in r[y]:
            return False
    # box
    box_x_start = x // 3 * 3
    box_y_start = y // 3 * 3
    for i in range(box_x_start, box_x_start + 3):
        for j in range(box_y_start, box_y_start + 3):
            if num == bo[i][j]:
                return False
    return True


board2 = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(matrix(board2))
solve(board2)
print('-' * 27)
print(matrix(board2))
