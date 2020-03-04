def bs(ls, n):
    if not ls:
        return -1
    low = 0
    high = len(ls) - 1

    def helper(lo, hi):
        mid = (lo + hi) // 2
        if lo == hi and ls[mid] != n:
            return -1
        if ls[mid] == n:
            return mid
        elif ls[mid] > n:
            return helper(lo, mid - 1)
        else:
            return helper(mid + 1, hi)

    return helper(low, high)


# unit tests
a = list(range(1, 2222))
print('mid in long list: ', bs(a, 1000) == 999)
print('first in long list: ', bs(a, 1) == 0)
print('last in long list: ', bs(a, 2221) == 2220)
print('not exist in long list: ', bs(a, 2222) == -1)
b = [1]
print('one element: ', bs(b, 1) == 0)
print('not exist in one element list: ', bs(b, 2) == -1)
c = [1, 2]
print('first in two element: ', bs(c, 1) == 0)
print('last in two element: ', bs(c, 2) == 1)
d = [1, 2, 3]
print('first in three element: ', bs(d, 1) == 0)
print('mid in three element: ', bs(d, 2) == 1)
print('last in three element: ', bs(d, 3) == 2)
e = []
print('empty list: ', bs(e, 1) == -1)
