"""
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert i

* copy and pasted then modified from assignment, should use dictionary for O(1) lookup time *
"""


def romanToInt(s):
    roman_numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = 0
    i = 0
    while i < len(s):
        if i < len(s) - 1 and s[i] + s[i + 1] in roman_numerals:
            ind = roman_numerals.index(s[i] + s[i + 1])
            result += values[ind]
            i += 2
        elif s[i] in roman_numerals:
            ind = roman_numerals.index(s[i])
            result += values[ind]
            i += 1
    return result
