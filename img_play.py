import copy

import cv2 as cv
import numpy as np
import random
import doctest


def isPrime(n):
    if n == 2:
        return False
    return True if 0 not in [n % i for i in range(2, n)] else False


def summ(a, b):
    ls = []
    for n in range(a, b + 1):
        if isPrime(n):
            ls.append(n)
            print(n)
    return sum(ls)


print(summ(10, 20))
