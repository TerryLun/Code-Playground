import os, sys
import generate_magic_squares

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def formingMagicSquare(s):
    msq = generate_magic_squares.generate_magic_squares_three_by_three()
    cost = float('inf')
    for m in msq:
        c = 0
        for x in range(len(s)):
            for y in range(len(s[0])):
                c += abs(int(m[x][y]) - s[x][y])
        if c < cost:
            cost = c
    return cost


m = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
print(formingMagicSquare(m))
m = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
print(formingMagicSquare(m))
