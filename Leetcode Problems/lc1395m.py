"""
1395. Count Number of Teams

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example 1:
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

Example 2:
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:
Input: rating = [1,2,3,4]
Output: 4

Constraints:
n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5
"""


def numTeams(rating):
    result = 0
    for i, n in enumerate(rating):
        left_less = left_greater = right_less = right_greater = 0
        for left in rating[:i]:
            if left > n:
                left_greater += 1
            elif left < n:
                left_less += 1
        for right in rating[i + 1:]:
            if right > n:
                right_greater += 1
            elif right < n:
                right_less += 1
        result += left_greater * right_less + left_less * right_greater
    return result
