"""
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false

Constraints:
s consists only of printable ASCII characters.
"""


def isPalindrome(s: str) -> bool:
    fs = ''
    for c in s:
        if c.isalnum():
            fs += c.lower()
    return fs == fs[::-1]
