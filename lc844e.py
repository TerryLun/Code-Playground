"""
844. Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
"""


def backspaceCompare(s, t):
    i = 0
    j = 0
    ss = ''
    tt = ''
    while i < len(s):
        if s[i] != '#':
            ss += s[i]
        else:
            ss = ss[:-1]
        i += 1
    while j < len(t):
        if t[j] != '#':
            tt += t[j]
        else:
            tt = tt[:-1]
        j += 1
    return True if ss == tt else False


s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t) is True)

s = "ab##"
t = "c#d#"
print(backspaceCompare(s, t) is True)

s = "a##c"
t = "#a#c"
print(backspaceCompare(s, t) is True)

s = "a#c"
t = "b"
print(backspaceCompare(s, t) is False)
