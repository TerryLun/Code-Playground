# pss = []
# temp = []
# while 1:
#     line = input()
#     if not line and not temp:
#         break
#     elif not line:
#         pss.append(' '.join(temp))
#         temp.clear()
#     else:
#         temp.append(line)
#
# print("eoi")
#
# rqf = ['byr',
#        'iyr',
#        'eyr',
#        'hgt',
#        'hcl',
#        'ecl',
#        'pid']
#
# r = 0
# vpss = []
#
# for ps in pss:
#     flag = True
#     for f in rqf:
#         if f not in ps:
#             flag = False
#     if flag:
#         vpss.append(ps)
#
# print(len(vpss))

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

r = 0

for ps in pss:
    flag = True
    for f in rqf:
        if f not in ps:
            flag = False
    if flag:
        ps = ps.split()
        for p in ps:
            p = p.split(':')
            if p[0] == 'byr':
                if not p[1].isdigit() or not 1920 <= int(p[1]) <= 2002:
                    flag = False
            elif p[0] == 'iyr':
                if not p[1].isdigit() or not 2010 <= int(p[1]) <= 2020:
                    flag = False
            elif p[0] == 'eyr':
                if not p[1].isdigit() or not 2020 <= int(p[1]) <= 2030:
                    flag = False
            elif p[0] == 'hgt':
                if not ('in' in p[1] or 'cm' in p[1]):
                    flag = False
                elif 'cm' in p[1]:
                    val = p[1].replace('cm', '')
                    if not val.isdigit():
                        flag = False
                    else:
                        val = int(val)
                        if not 150 <= val <= 193:
                            flag = False
                elif 'in' in p[1]:
                    val = p[1].replace('in', '')
                    if not val.isdigit():
                        flag = False
                    else:
                        val = int(val)
                        if not 59 <= val <= 76:
                            flag = False
                else:
                    flag = False
            elif p[0] == 'hcl':
                if len(p[1]) != 7 or not p[1][0] == '#':
                    flag = False
                else:
                    for i in p[1][1:]:
                        if i not in '0123456789abcdef':
                            flag = False
            elif p[0] == 'ecl':
                if p[1] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    flag = False
            elif p[0] == 'pid':
                if len(p[1]) != 9 or not p[1].isdigit():
                    flag = False
        if flag:
            r += 1
print(r)
