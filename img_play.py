import copy

import cv2 as cv
import numpy as np
import random


def pre_pender(first, second):
    count = 0
    for num in first:
        if num % second == 0 and num != 0:
            count += 1
    return count


def unicode(s):
    return [ord(c) for c in s]


def main():
    print({x: int(x / 2 * (x + 1)) for x in [n for n in range(1, 100, 2) if 0 not in [n % i for i in range(2, n)]]})

    ls = {x: sum(range(x + 1)) for x in [n for n in range(2, 100) if 0 not in [n % i for i in range(2, n)]]}
    print(ls)

    print(*list(n for n in range(33,50)))
    print(*list(n for n in range(10,0,-1)))



if __name__ == '__main__':
    main()
