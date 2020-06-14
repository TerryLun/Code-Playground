"""
https://www.hackerrank.com/challenges/angry-professor/problem
"""


def angryProfessor(k, a):
    count = 0
    for i in a:
        if i <= 0:
            count += 1
    return 'NO' if count >= k else 'YES'
