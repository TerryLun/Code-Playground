import copy

import cv2 as cv
import numpy as np
import random


def roll_die():
    number_of_rolls = int(input('rolls: '))
    number_of_sides = int(input('sides: '))
    counts = {value: 0 for value in range(1, number_of_sides+1)}
    for _ in range(0, number_of_rolls):
        counts[random.randint(1, number_of_sides)] += 1
    print(counts)


def main():
    roll_die()


if __name__ == '__main__':
    main()
