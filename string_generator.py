"""
Redo BCIT CP club week 1 problem:

Print all combinations of string with length l, with h '#'s, and the rest with '_'

l: length of the strings
h: number of hash tags


Time taken: 6 min
"""


def string_gen(l, h):
    for i in range(0, int(('1' * l), 2) + 1):
        if num_of_ones(i) == h:
            st = str(bin(i)).replace('0b', '').zfill(l).replace('0', '_').replace('1', '#')
            print(st)


def num_of_ones(n):
    r = 0
    while n != 0:
        n = n & (n - 1)
        r += 1
    return r


string_gen(5, 3)
