"""
https://www.hackerrank.com/challenges/taum-and-bday/problem
"""


def taumBday(b, w, bc, wc, z):
    bc = min(bc, wc + z)
    wc = min(wc, bc + z)
    return b * bc + w * wc
