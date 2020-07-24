"""
1281. Subtract the Product and Sum of Digits of an Integer


Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Constraints:
1 <= n <= 10^5
"""

def subtractProductAndSum(n: int) -> int:
    str_n = str(n)
    sum_of_digit = 0
    product_of_digits = 1
    for d in str_n:
        d = int(d)
        sum_of_digit += d
        product_of_digits *= d
    return product_of_digits - sum_of_digit
