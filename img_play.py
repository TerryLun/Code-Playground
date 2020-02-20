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
    a = [1, 2, 3]
    b = [2, 4, 2]
    c = [a, b]
    d = {k: v+t for k, v, t in c}
    print(d)


if __name__ == '__main__':
    main()
