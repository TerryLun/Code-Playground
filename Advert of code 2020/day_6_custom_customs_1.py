temp = []
qs = []

while 1:
    line = input()
    if not line and not temp:
        break
    elif not line:
        qs.append(' '.join(temp))
        temp.clear()
    else:
        temp.append(line)

r = 0

for q in qs:
    q = q.replace(' ', '')
    q = set(q)
    r += len(q)
print(r)
