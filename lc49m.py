"""
49. Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anadict = {}
    result = []
    for i in range(len(strs)):
        temp = {}
        for c in strs[i]:
            if c in temp.keys():
                temp[c] += 1
            else:
                temp[c] = 1
        anadict[i] = temp
    while anadict:
        item = anadict.popitem()  # (i,dict)
        sub = [strs[item[0]]]
        for k, v in anadict.copy().items():
            if item[1] == v:
                sub.append(strs[k])
                anadict.pop(k)
        result.append(sub)
    return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
