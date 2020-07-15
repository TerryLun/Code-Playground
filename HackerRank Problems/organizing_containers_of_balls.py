"""
https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
"""


def organizingContainers(container):
    a = []
    b = []
    for r in container:
        a.append(sum(r))
    for c in list(zip(*container)):
        b.append(sum(c))
    if sorted(a) == sorted(b):
        return 'Possible'
    else:
        return 'Impossible'
