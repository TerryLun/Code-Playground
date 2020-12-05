a = []
while 1:
    line = input()
    if not line:
        break
    a += [int(line)]

s = {a[0]}
for n in a:
    for m in s:
        s.add(n * m)
    if 2020-n in s:
        print(n*(2020-n))
