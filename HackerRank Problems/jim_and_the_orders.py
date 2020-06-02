"""
https://www.hackerrank.com/challenges/jim-and-the-orders/problem
"""


def jimOrders(orders):
    time = {k + 1: sum(orders[k]) for k in range(len(orders))}
    sorted_time = sorted(time.items(), key=lambda x: x[1])
    return [st[0] for st in sorted_time]


inp = [[8, 1], [4, 2], [5, 6], [3, 1], [4, 3]]
exp = [4, 2, 5, 1, 3]
print(jimOrders(inp))
