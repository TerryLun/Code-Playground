def climbingLeaderboard_bf(scores, alice):
    """
    Brute force (TLE)
    """
    r = []
    sc = set(scores)
    scores = sorted(list(sc), reverse=True)
    for a in alice:
        scores.append(a)
        scores.sort(reverse=True)
        r.append(scores.index(a) + 1)
        scores.remove(a)
    return r


def climbingLeaderboard_hsbf(scores, alice):
    """
    Optimized with hash set (Still TLE)
    """
    r = []
    for a in alice:
        higher = set()
        i = 0
        while i < len(scores) and scores[i] > a:
            higher.add(scores[i])
            i += 1
        r.append(len(higher) + 1)
    return r


def climbingLeaderboard(scores, alice):
    """
    Two pointers (Accepted O(M+N) )
    """
    si = 0
    current_rank = 1
    result = []
    for ai in range(len(alice) - 1, -1, -1):
        while si != len(scores) and alice[ai] < scores[si]:
            if scores[si] != scores[si - 1]:
                current_rank += 1
            si += 1
        if si == len(scores) or alice[ai] >= scores[si]:
            result.append(current_rank)
    result.reverse()
    return result


s = [100, 100, 50, 40, 40, 20, 10]
a = [5, 25, 50, 120]
print(climbingLeaderboard(s, a))
