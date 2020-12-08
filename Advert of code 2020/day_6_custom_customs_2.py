temp = []
qs = []

while 1:
    line = input()
    if not line and not temp:
        break
    elif not line:
        qs.append(temp[:])
        temp.clear()
    else:
        temp.append(set(line))

print(qs)

r = 0

for q in qs:
    r += len(q[0].intersection(*q))

print(r)
