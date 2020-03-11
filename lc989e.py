"""
989. Add to Array-Form of Integer

For a non-negative integer X, the array-form of X is an array of its digits in left to right order.
For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.
"""


def addToArrayForm(a, k):
    """
    :type a: List[int]
    :type k: int
    :rtype: List[int]
    """
        i = len(a) - 1
        while k or i >= 0:
            if i >= 0:
                sum = a[i] + k
                k, a[i] = divmod(sum, 10)
                i -= 1
            else:
                a.insert(0, k % 10)
                k = k // 10
        return a


# unit tests
a = [1, 2, 0, 0]
k = 34
output = [1, 2, 3, 4]
print(addToArrayForm(a, k) == output)

a = [2, 7, 4]
k = 181
output = [4, 5, 5]
print(addToArrayForm(a, k) == output)

a = [2, 1, 5]
k = 806
output = [1, 0, 2, 1]
print(addToArrayForm(a, k) == output)

a = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
k = 1
output = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(addToArrayForm(a, k) == output)

a = [1]
k = 1
output = [2]
print(addToArrayForm(a, k) == output)
