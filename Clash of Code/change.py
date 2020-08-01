"""
During lunch break at your school, one of your friends asks you if you can exchange his K dollar bill to lower value
bills.

You have an unlimited number of bills of N distinct values.
Can you exchange your friends money?

Example: Your friend wants change for 50 dollars and you have an unlimited number of 5 dollar bills, so you offer him
10 5 dollar bills in return.


Input:
Line 1: K value of your friend's bill.
Line 2: N different types of bills you have at your disposal.
Line 3: N numbers representing the values of your bills.

Output:
Line 1: "Yes" if you are able to exchange the money or "No" if you are unable to exchange his money.

Constraints:
5 ≤ K ≤ 1000
1 ≤ N ≤ 10
1 ≤ value of your bills < K

Test cases:
50
2
2 5
Yes

250
1
100
No

25
2
2 3
Yes

1000
10
7 4 3 50 60 5 19 64 54 23
Yes

525
3
2 3 50
Yes

1000
1
1
Yes

81
3
2 10 12
No

185
2
75 40
No
"""


import collections

q = collections.deque()
q.append(int(input()))
input()
changes = list(map(int, input().split()))
added = {q[0]}
while q:
    valid_total = q.popleft()
    for c in changes:
        if valid_total % c == 0:
            print('Yes')
            exit()
        elif valid_total - c > 0 and valid_total - c not in added:
            q.append(valid_total - c)
            added.add(valid_total - c)
print('No')
