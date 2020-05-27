"""
118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""


def generate(numRows):
    triangle = []
    if numRows == 0:
        return triangle
    triangle.append([1])
    for r in range(1, numRows):
        triangle.append([1])
        for i in range(1, r):
            triangle[r].append(triangle[r - 1][i] + triangle[r - 1][i - 1])
        triangle[r].append(1)
    return triangle


print(generate(0))
print(generate(1))
print(generate(2))
print(generate(3))
print(generate(10))
