"""
367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.
"""


def isPerfectSquare(num):
    i = 1
    while num > 0:
        num -= i
        i += 2
    return num == 0


# # naive
# def isPerfectSquare(num):
#     n = 0
#     while True:
#         sq = n * n
#         if sq == num:
#             return True
#         elif sq > num:
#             return False
#         n += 1
#
#
# # prick
# def isPerfectSquare(num):
#     return num**0.5 == int(num**0.5)
