'''
36. Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''
def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # row
    s = set()
    for r in board:
        for c in r:
            if c == '.':
                continue
            if c in s:
                return False
            else:
                s.add(c)
        s.clear()

    # col
    for j in range(9):
        for i in range(9):
            if board[i][j] == '.':
                continue
            if board[i][j] in s:
                return False
            else:
                s.add(board[i][j])
        s.clear()

    # box
    for i in range(1, 8, 3):
        for j in range(1, 8, 3):
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if board[x][y] == '.':
                        continue
                    if board[x][y] in s:
                        return False
                    else:
                        s.add(board[x][y])
            s.clear()

    return True


bo = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "."],
      ["5", ".", ".", ".", ".", ".", ".", "9", "."],
      [".", ".", ".", "5", "6", ".", ".", ".", "."],
      ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
      [".", ".", ".", "7", ".", ".", ".", ".", "."],
      [".", ".", ".", "5", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "."]]

print(isValidSudoku(bo))
