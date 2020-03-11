"""
345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Note: The vowels does not include the letter "y".
"""


def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    # # TLE:
    # if not s:
    #     return s
    # result = list(s)
    # vowels = set(['a', 'e', 'i', 'o', 'u', 'U','O','I','E','A'])
    # vow_dict = {}
    # for i in range(len(s)):
    #     if s[i] in vowels:
    #         vow_dict[i] = s[i]
    # vow_list = []
    # for k in sorted(vow_dict.keys()):
    #     vow_list.append(vow_dict[k])
    # vow_list.reverse()
    # for k, v in zip(sorted(vow_dict.keys()), vow_list):
    #     vow_dict[k] = v
    # print(vow_dict, vow_list)
    # for i in range(len(result)):
    #     if i in vow_dict.keys():
    #         result[i] = vow_dict[i]
    # return ''.join(result)

    # accepted
    st = list(s)
    vowels = set(['a', 'e', 'i', 'o', 'u', 'U', 'O', 'I', 'E', 'A'])
    i = 0
    j = len(st) - 1
    while i < j:
        if st[i] not in vowels:
            i += 1
        if st[j] not in vowels:
            j -= 1
        if st[i] in vowels and st[j] in vowels:
            temp = st[i]
            st[i] = st[j]
            st[j] = temp
            i += 1
            j -= 1
    return ''.join(st)


inp = "hello"
exp = "holle"
print(reverseVowels(inp) == exp)

inp = "leetcode"
exp = "leotcede"
print(reverseVowels(inp) == exp)

inp = "Aa"
exp = "aA"
print(reverseVowels(inp))
print(reverseVowels(inp) == exp)
