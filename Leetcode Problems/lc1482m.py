def number_to_harvest(bloomDay, k, day):
    n = 0
    adj = 0
    for bd in bloomDay:
        if bd <= day:
            adj += 1
        else:
            adj = 0

        if adj == k:
            n += 1
            adj = 0
    return n


def minDays(bloomDay, m, k):
    if m * k > len(bloomDay):
        return -1
    lo = 0
    hi = max(bloomDay)
    while lo < hi:
        mid = (lo + hi) // 2
        if number_to_harvest(bloomDay, k, mid) < m:
            lo = mid + 1
        else:
            hi = mid
    return lo


# test cases
bloomDay = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
m = 4
k = 2
exp = 9
print(minDays(bloomDay, m, k), 'Pass' if minDays(bloomDay, m, k) == exp else 'Fail')

bloomDay = [1000000000, 1000000000]
m = 1
k = 1
exp = 1000000000
print(minDays(bloomDay, m, k), 'Pass' if minDays(bloomDay, m, k) == exp else 'Fail')

bloomDay = [7, 7, 7, 7, 12, 7, 7]
m = 2
k = 3
exp = 12
print(minDays(bloomDay, m, k), 'Pass' if minDays(bloomDay, m, k) == exp else 'Fail')

bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 2
exp = -1
print(minDays(bloomDay, m, k), 'Pass' if minDays(bloomDay, m, k) == exp else 'Fail')

bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
exp = 3
print(minDays(bloomDay, m, k), 'Pass' if minDays(bloomDay, m, k) == exp else 'Fail')
