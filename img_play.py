import copy

import cv2 as cv
import numpy as np
import random



def name_list():
    names = {}
    name = input('Enter a name: (\'quit\' to finish)')
    while name != 'quit':
        if len(name) not in names:
            names[len(name)] = []
        names[len(name)].append(name)
        name = input('Enter a name: (\'quit\' to finish)')
    return names


def main():
    print(name_list())


if __name__ == '__main__':
    main()
