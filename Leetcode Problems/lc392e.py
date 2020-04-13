"""
392. Is Subsequence

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long
(length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of
"abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has
its subsequence. In this scenario, how would you change your code?
"""


def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    while s != '':
        if s[0] not in t or t == '':
            return False
        else:
            t = t[t.find(s[0])+1:]
        s = s[1:]
    return True


def is_subsequence_preprocess(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    pos = {}
    cur_pos = 0
    # pre-process
    for i in range(len(t)):
        if t[i] in pos.keys():
            pos[t[i]].append(i)
        else:
            pos[t[i]] = [i]
    for c in s:
        if c in pos.keys() and cur_pos <= max(pos[c]):
            for v in pos[c]:
                if v >= cur_pos:
                    cur_pos = v
        else:
            return False
    return True


s = "abc"
t = "ahbgdc"
exp = True
print(is_subsequence_preprocess(s, t) == exp)

s = "axc"
t = "ahbgdc"
exp = False
print(is_subsequence_preprocess(s, t) == exp)

s = ""
t = "ahbgdc"
exp = True
print(is_subsequence_preprocess(s, t) == exp)

s = "axc"
t = ""
exp = False
print(is_subsequence_preprocess(s, t) == exp)

s = "leeeeetcode"
t = "ylyeyeyeytycyoydye"
exp = False
print(is_subsequence_preprocess(s, t) == exp)
