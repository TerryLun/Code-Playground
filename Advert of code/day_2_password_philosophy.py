a = []
v = 0
while 1:
    line = input()
    if not line:
        break
    # parse input
    left, pw = line.split(': ')
    occ, char = left.split()
    l, h = map(int, occ.split('-'))
    v += 1 if l <= pw.count(char) <= h else 0
print(v)
