"""
14. Longest Common Prefix


Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""


def longestCommonPrefix(strs):
    pref = ''
    if not strs:
        return pref
    i = 0
    min_len = len(min(strs, key=len))
    c = set()
    while i < min_len:
        for s in strs:
            c.add(s[i])
        if len(c) == 1:
            pref += strs[0][i]
            c.clear()
        else:
            break
        i += 1
    return pref


in1 = ["flower", "flow", "flight"]
actual = longestCommonPrefix(in1)
expected = 'fl'
print(expected == actual)

in2 = ["dog", "racecar", "car"]
actual = longestCommonPrefix(in2)
expected = ''
print(expected == actual)

in3 = ["", "racecar", "car"]
actual = longestCommonPrefix(in3)
expected = ''
print(expected == actual)
