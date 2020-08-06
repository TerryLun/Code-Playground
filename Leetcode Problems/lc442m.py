"""
442. Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
"""


def solution(in_list):
    result = []
    for i in range(len(in_list)):
        if in_list[abs(in_list[i]) - 1] > 0:
            in_list[abs(in_list[i]) - 1] *= -1
        else:
            result.append(abs(in_list[i]))
    return result


l = [4, 3, 2, 7, 8, 2, 3, 1]
print(solution(l))
