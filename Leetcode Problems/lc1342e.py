"""
1342. Number of Steps to Reduce a Number to Zero

Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even,
you have to divide it by 2, otherwise, you have to subtract 1 from it.
"""


def numberOfSteps(num):
    steps = 0
    while num != 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        steps += 1
    return steps

    """
    or:
    For the binary representation from right to left(until we find the leftmost 1):
    if we meet 0, result += 1 because we are doing divide;
    if we meet 1, result += 2 because we first do "-1" then do a divide;
    ony exception is the leftmost 1, we just do a "-1" and it becomse 0 already.
    """
    # if num == 0:
    #     return 0
    # steps = 0
    # while num != 0:
    #     if num & 1:
    #         steps += 2
    #     else:
    #         steps += 1
    #     num >>= 1
    # return steps - 1


