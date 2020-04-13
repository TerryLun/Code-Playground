"""
1010. Pairs of Songs With Total Durations Divisible by 60

In a list of songs, the i-th song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the
number of indices i < j with (time[i] + time[j]) % 60 == 0.

1 <= time.length <= 60000
1 <= time[i] <= 500
"""


def numPairsDivisibleBy60(time):
    """
    :type time: List[int]
    :rtype: int
    """

    result = 0
    count = {}
    for t in time:
        t = t % 60
        if t in count.keys():
            count[t] += 1
        else:
            count[t] = 1
    keys = [k for k in count.keys()]
    for k in keys:
        if k == 30 or k == 0:
            result += count[k] * (count[k] - 1) / 2
        elif 0 < k < 30:
            comp = 60 - k
            if comp in keys:
                result += count[k] * count[comp]
    return int(result)


# tests
inp = [30, 20, 150, 100, 40]
exp = 3
print(numPairsDivisibleBy60(inp) == exp)

inp = [60, 60, 60]
exp = 3
print(numPairsDivisibleBy60(inp) == exp)

inp = [15, 63, 451, 213, 37, 209, 343, 319]
exp = 1
print(numPairsDivisibleBy60(inp) == exp)

inp = [418, 204, 77, 278, 239, 457, 284, 263, 372, 279, 476, 416, 360, 18]
exp = 1
print(numPairsDivisibleBy60(inp) == exp)
