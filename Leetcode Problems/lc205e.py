"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two
characters may map to the same character but a character may map to itself.

Note:
You may assume both s and t have the same length.
"""


def isIsomorphic(s, t):
    return convert(s) == convert(t)


def convert(s):
    track = {}
    count = 33
    for i in range(len(s)):
        c = s[i]
        if ord(c) - ord('0') not in track.keys():
            s = s[:i] + chr(count) + s[i + 1:]
            track[ord(c) - ord('0')] = chr(count)
            count += 1
        else:
            s = s[:i] + track[ord(c) - ord('0')] + s[i + 1:]
    return s


s1 = "qwertyuiop[]asdfghjkl;'\\zxcvbnm,./"
s2 = "',.pyfgcrl/=aoeuidhtns-\\;qjkxbmwvz"
print(convert(s1))
print(convert(s2))
print(isIsomorphic(s1, s2))
