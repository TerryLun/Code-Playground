"""
https://www.hackerrank.com/challenges/the-birthday-bar/problem
"""

def birthday(s, d, m):
    if m > len(s):
        return 0
    window_sum = sum(s[:m])
    result = 0
    if window_sum == d:
        result += 1
    for i in range(0, len(s)-m):
        window_sum += s[i+m] - s[i]
        if window_sum == d:
            result += 1
    return result


print(birthday([1, 2, 1, 3, 2], 3, 2) == 2)
