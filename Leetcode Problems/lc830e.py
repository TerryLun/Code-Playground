"""
830. Positions of Large Groups

In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large
group.
The final answer should be in lexicographic order.

Note:  1 <= S.length <= 1000
"""

import re


# regex
def largeGroupPositions_regex(S):
    """
    :type S: str
    :rtype: List[List[int]]
    """
    result = []
    pattern = re.compile(r'(\w)\1{2,}')
    match_obj = re.finditer(pattern, S)
    for m in match_obj:
        result.append([m.span()[0], m.span()[1] - 1])
    return result


# pointers
def largeGroupPositions(S):
    """
    :type S: str
    :rtype: List[List[int]]
    """
    hi = 1
    lo = 0
    result = []
    while hi < len(S):
        if S[hi] != S[lo] and hi - lo <= 2:
            lo = hi
        elif S[hi] != S[lo] and hi - lo > 2:
            result.append([lo, hi - 1])
            lo = hi
        hi += 1
    # check last character since it skipped checking if S[hi] == S[lo]
    if S[hi-1] == S[lo] and hi - lo > 2:
        result.append([lo, hi - 1])
    return result


s = "abbxxxxzzy"
exp = [[3, 6]]
print(largeGroupPositions(s) == exp)

s = "abc"
exp = []
print(largeGroupPositions(s) == exp)

s = "abcdddeeeeaabbbcd"
exp = [[3, 5], [6, 9], [12, 14]]
print(largeGroupPositions(s) == exp)

s = "abcdddeeeeaabbb"
exp = [[3, 5], [6, 9], [12, 14]]
print(largeGroupPositions(s) == exp)

s = "abcdddeeeeaabee"
exp = [[3, 5], [6, 9]]
print(largeGroupPositions(s) == exp)
