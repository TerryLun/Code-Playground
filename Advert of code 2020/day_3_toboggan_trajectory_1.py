a = []
r = 0
x = 0
while 1:
    line = input()
    if not line:
        break
    # parse input
    if line[x]=='#':
        r+=1

    x += 3
    if x >= len(line):
        x %= len(line)

print(r)
