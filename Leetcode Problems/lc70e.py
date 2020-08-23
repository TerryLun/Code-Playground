"""
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def memoize(f):
    memo = {}

    def helper(n):
        if n not in memo:
            memo[n] = f(n)
        return memo[n]

    return helper


@memoize
def climbStairs(n):
    # recursion
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 2
    return climbStairs(n - 1) + climbStairs(n - 2)

    # climb = [1, 1, 2]
    # for i in range(3, n + 1):
    #     climb.append(climb[i - 1] + climb[i - 2])
    # return climb[n]


inp = 2
exp = 2
print(climbStairs(inp) == exp)

inp = 300
exp = 359579325206583560961765665172189099052367214309267232255589801
print(climbStairs(inp) == exp)
