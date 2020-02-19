import copy

import cv2 as cv
import numpy as np
import random


def multiples_of_3(upperbound):
    total = 0
    for num in range(3, upperbound, 3):
        total += num
    return total


def multiples(upperbound):
    # n(a1+an)/2
    # change upperbound to exclusive
    upperbound -= 1
    return (upperbound // 3) * (3 + (upperbound - upperbound % 3)) / 2


def main():
    for i in range(10, 100):
        print('i = ', i)
        print(multiples_of_3(i))
        print(multiples(i))
        print()


if __name__ == '__main__':
    main()
