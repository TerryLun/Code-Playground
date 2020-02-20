import copy

import cv2 as cv
import numpy as np
import random
import doctest

res = {k: 0 for k in range(1, 7)}
for _ in range(1_000_000):
    res[random.randint(1, 6)] += 1

for k, v in res.items():
    print('%d rolled %d times' % (k, v))
