import itertools

a = [1, 2, 3, 4]

"""
itertools
"""
r1 = []
for i in range(0, len(a) + 1):
    for element in itertools.combinations(a, i):
        r1.append(list(element))
print(r1)

"""
power set
"""
n = len(a)
r2 = []
for bot_pattern in range(2 ** n):
    temp = []
    i = 0
    while bot_pattern:
        if bot_pattern & 1:
            temp.append(a[i])
        bot_pattern >>= 1
        i += 1
    r2.append(temp)
print(r2)

rs1 = {tuple(i) for i in r1}
rs2 = {tuple(i) for i in r2}
print(rs1 == rs2)
