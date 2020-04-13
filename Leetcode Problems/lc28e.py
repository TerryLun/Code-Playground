"""
28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if needle == haystack[i:i + len(needle)]:
                return i
    return -1
