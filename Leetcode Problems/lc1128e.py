"""
1128. Number of Equivalent Domino Pairs

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if
either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.
Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Constraints:
1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
"""

def numEquivDominoPairs(dominoes):
    """
    :type dominoes: List[List[int]]
    :rtype: int
    """
    count = {}
    result = 0
    for dom in dominoes:
        num = min(dom[0], dom[1]) * 10 + max(dom[0], dom[1])
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for v in count.values():
        result += v * (v - 1) / 2
    return result


dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
exp = 1
print(numEquivDominoPairs(dominoes) == exp)
