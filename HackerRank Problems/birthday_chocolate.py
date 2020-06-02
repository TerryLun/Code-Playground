def birthday(s, d, m):
    if m > len(s):
        return 0
    window_sum = sum(s[:m])
    result = 0
    if window_sum == d:
        result += 1
    for i in range(1, len(s)-m+1):
        window_sum += s[i+m-1] - s[i-1]
        if window_sum == d:
            result += 1
    return result


print(birthday([1, 2, 1, 3, 2], 3, 2) == 2)
