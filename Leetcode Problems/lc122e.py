"""
122. Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and
sell one share of the stock multiple times).


Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    res = 0
    for i in range(1, len(prices)):
        if prices[i] - prices[i - 1] > 0:
            res += prices[i] - prices[i - 1]
    return res


inp = [7, 1, 5, 3, 6, 4]
exp = 7
print(maxProfit(inp) == exp)

inp = [1, 2, 3, 4, 5]
exp = 4
print(maxProfit(inp) == exp)

inp = [7, 6, 4, 3, 1]
exp = 0
print(maxProfit(inp) == exp)
