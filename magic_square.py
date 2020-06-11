def pick_empty(board):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == '':
                return r, c
    else:
        return None


def validate(board, num, pos):
    x, y = pos
    n = len(board)
    target_sum = 1 + n * n + (1 + n * n) // 2
    board[x][y] = str(num)

    # row
    if '' not in board[x] and sum(list(map(int, board[x]))) != target_sum:
        board[x][y] = ''
        return False

    # col
    c = []
    for r in board:
        c.append(r[y])
    if '' not in c and sum(list(map(int, c))) != target_sum:
        board[x][y] = ''
        return False
    c.clear()
    # diag

    if x == y:
        for i in range(0, n):
            c.append(board[i][i])
        if '' not in c and sum(list(map(int, c))) != target_sum:
            board[x][y] = '_'
            return False
    c.clear()

    if x + y == n - 1:
        for i in range(0, n):
            c.append(board[n - 1 - i][i])
        if '' not in c and sum(list(map(int, c))) != target_sum:
            board[x][y] = ''
            return False

    board[x][y] = ''
    return True


def print_board(board):
    for r in board:
        for c in r:
            if c == '':
                print('_', end=' ')
            else:
                print(c, end=' ')
        print()


def solve(n):
    def helper(board, used, upperbound):
        empty = pick_empty(board)

        if not empty:
            return True
        else:
            r, c = empty

        for num in range(1, upperbound):
            if used[num]:
                continue
            if validate(board, num, empty):
                board[r][c] = str(num)
                used[num] = True
                if helper(board, used, upperbound):
                    return True
            board[r][c] = ''
            used[num] = False
        return False

    board = [['' for i in range(n)] for i in range(n)]
    upperbound = n * n + 1
    used = [False] * (upperbound)
    helper(board, used, upperbound)
    print_board(board)
    return board


# driver code
solve(3)
