import copy

import cv2 as cv
import numpy as np
import random
import doctest


def solution(s):
    d = {}
    for c in s:
        if c not in d.keys():
            d[c] = 1
        else:
            d[c] += 1
    for c in s:
        if d[c] == 1:
            return c
    return '_'


s0 = ''
s1 = 'aaabcccdeeef'
s2 = 'abcbad'
s3 = 'abcabcabc'
s4 = 'a'
print(solution(s0))
print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
