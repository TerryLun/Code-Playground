import copy

import cv2 as cv
import numpy as np
import random


def prepender(first, second):
    count = 0
    for num in first:
        if num % second == 0 and num != 0:
            count += 1
    return count


def main():
    s = [1, 2, 2, 3, 4, 5, 6, 7, 87, 8, 9, 0, 4, 5, 6, 7, 7, 5, 5, 67, 4]
    print(prepender(s, 3))


if __name__ == '__main__':
    main()
