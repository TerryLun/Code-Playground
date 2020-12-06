pss = []
temp = []
while 1:
    line = input()
    if not line and not temp:
        break
    elif not line:
        pss.append(' '.join(temp))
        temp.clear()
    else:
        temp.append(line)

print("eoi")

rqf = ['byr',
       'iyr',
       'eyr',
       'hgt',
       'hcl',
       'ecl',
       'pid']

print(pss)

r = 0

for ps in pss:
    flag = True
    for f in rqf:
        if f not in ps:
            flag = False
    if flag:
        r += 1
print(r)
