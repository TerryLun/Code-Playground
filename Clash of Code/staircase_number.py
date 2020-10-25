"""
Staircase number is a number that starts with 1 and each subsequence number goes up by 1,
until it reaches the maximum N, then it goes back down until the last digit is 1

true:
1234567891011121110987654321
121
1

false:
2
131
2321
1234567891011131110987654321
"""

s = input()
n = 1
while s:
    if s.startswith(str(n)):
        s = s[len(str(n)):]
        n += 1
    else:
        break
n -= 2
while s or n:
    if s.startswith(str(n)):
        s = s[len(str(n)):]
        n -= 1
    else:
        print('false')
        exit()
print('true')
