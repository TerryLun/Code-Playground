"""
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    # # recursion
    # if n == 1 or n == 0:
    #     return 1
    # if n == 2:
    #     return 2
    # return climbStairs(n - 1) + climbStairs(n - 2)

    climb = [1, 1, 2]
    for i in range(3, n + 1):
        climb.append(climb[i - 1] + climb[i - 2])
    return climb[n]


inp = 2
exp = 2
print(climbStairs(inp) == exp)

inp = 30
exp = 1346269
print(climbStairs(inp) == exp)
