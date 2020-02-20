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
    lox = [1, 2, 3]
    loy = [1, 5]
    print([[x + y for x in lox] for y in loy])

    print(np.matrix([[r + c for r in range(8)] for c in range(8)]))


if __name__ == '__main__':
    main()
