s = input()
r = 1
t = 1
l = ''
for c in s:
    if c == l:
        t += 1
        r = max(t, r)
    else:
        t = 1
    l = c
print(r)
