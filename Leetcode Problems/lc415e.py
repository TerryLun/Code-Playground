"""
415. Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    carry = 0
    result = ''
    i = len(num1) - 1
    j = len(num2) - 1
    while carry or i >= 0 or j >= 0:
        summ = carry
        carry = 0
        if i >= 0:
            summ += ord(num1[i]) - ord('0')
            i -= 1
        if j >= 0:
            summ += ord(num2[j]) - ord('0')
            j -= 1
        carry, digit = divmod(summ, 10)
        result = str(digit) + result
    return result


s1 = '12'
s2 = '999'
print(addStrings(s1, s2))
