import itertools

a = [1, 2, 3, 4]

"""
itertools
"""
r = []
for i in range(0, len(a) + 1):
    for element in itertools.combinations(a, i):
        r.append(list(element))
print(r)

"""
power set
"""
n = len(a)
r = []
for bot_pattern in range(2 ** n):
    temp = []
    i = 0
    while bot_pattern:
        if bot_pattern & 1:
            temp.append(a[i])
        bot_pattern >>= 1
        i += 1
    r.append(temp)
print(r)
