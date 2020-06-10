"""
https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
"""


def designerPdfViewer(h, word):
    return max([h[ord(c) - ord('a')] for c in word]) * len(word)
