"""
767. Reorganize String

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not
the same.

If possible, output any possible result.  If not possible, return the empty string.

Note:
S will consist of lowercase letters and have length in range [1, 500]
"""


def reorganizeString(S):
    def find_most_occ(dic, banned):
        high_v = 0
        high_k = '0'
        for k, v in dic.items():
            if v > high_v and k != banned:
                high_v = v
                high_k = k
        return high_k

    if not S:
        return ''

    result = ''
    count = {}
    for c in S:
        if c in count.keys():
            count[c] += 1
        else:
            count[c] = 1
    if max(count.values()) > (len(S) + 1) / 2:
        return result

    result += find_most_occ(count, '')
    count[find_most_occ(count, '')] -= 1

    while len(result) < len(S):
        result += find_most_occ(count, result[-1])
        count[find_most_occ(count, result[-2])] -= 1

    return result


s = "vvvlo"
e = "vlvov"
print(reorganizeString(s) == e)

s = "aab"
e = "aba"
print(reorganizeString(s) == e)

s = "aaab"
e = ""
print(reorganizeString(s) == e)

s = "a"
e = "a"
print(reorganizeString(s) == e)

s = ""
e = ""
print(reorganizeString(s) == e)
