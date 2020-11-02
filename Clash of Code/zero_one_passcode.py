"""
replace ? with all possible 0 or 1
print in ascending order

input:
?
output:
1
0

input:
??
output:
00
01
10
11

input:
???
output:
000
001
010
011
100
101
110
111

input:
1?0?
output:
1000
1001
1100
1101
"""

a = input()  # The input string.

print('iterative:')
l = a.count('?')
for i in range(2 ** l):
    b = bin(i)[2:].rjust(len(bin(2 ** l - 1)[2:]), '0')
    r = a
    for d in b:
        r = r.replace('?', d, 1)
    print(r)

print("recursive:")
def pc(t, i):
    if i == len(t): return [t]
    c = t[i]
    if c == '?':
        a = t[:i] + '0' + t[i + 1:]
        b = t[:i] + '1' + t[i + 1:]
        return pc(a, i + 1) + pc(b, i + 1)
    else:
        return pc(t, i + 1)


l = pc(a, 0)

print(*sorted(l), sep='\n')
