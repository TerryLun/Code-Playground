a=[]
while 1:
    line = input()
    if not line:
        break
    a+=[int(line)]

s = set()
for n in a:
    if n in s:
        print(n*(2020-n))
    else:
        s.add(2020-n)
