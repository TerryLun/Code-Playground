"""
957. Prison Cells After N Days

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else
cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)


Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9
"""


def prisonAfterNDays(cells, N):
    """
    length of loop is 14 or 7 - Accepted
    """
    N = (N % 14) + 14
    memo = {}
    for d in range(N):
        s = ''.join(list(map(str, cells)))
        if s in memo:
            cells[:] = memo[s]
        else:
            a = cells[:]
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    a[i] = 1
                else:
                    a[i] = 0
            if d == 0 and cells[0] == 1:
                a[0] = 0
            if d == 0 and cells[-1] == 1:
                a[-1] = 0
            memo[s] = a[:]
            cells[:] = a[:]
    return cells


cells = [0, 1, 0, 1, 0, 1, 1, 1]
N = 30
print(prisonAfterNDays(cells, N))
