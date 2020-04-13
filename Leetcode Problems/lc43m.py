"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also
represented as a string.

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    to_add = []
    i = len(num1) - 1
    while i >= 0:
        j = len(num2) - 1
        while j >= 0:
            n1 = (ord(num1[i]) - ord('0'))
            n2 = (ord(num2[j]) - ord('0'))
            zeros = ((len(num1) - i - 1) + (len(num2) - j - 1))
            to_add.append(n1 * n2 * (10 ** zeros))
            j -= 1
        i -= 1
    total = sum(to_add)
    return str(total)


# tests
num1 = "2"
num2 = "3"
exp = "6"
print(multiply(num1, num2) == exp)

num1 = "123"
num2 = "456"
exp = "56088"
print(multiply(num1, num2) == exp)

num1 = "1"
num2 = "456"
exp = "456"
print(multiply(num1, num2) == exp)

num1 = "0"
num2 = "456"
exp = "0"
print(multiply(num1, num2) == exp)
