# fields
fields = {}
while 1:
    line = input()
    if not line:
        break
    field_name, ranges = line.split(': ')
    range1, range2 = ranges.split(' or ')
    n1, n2 = map(int, range1.split('-'))
    n3, n4 = map(int, range2.split('-'))
    fields[field_name] = ((n1, n2), (n3, n4))

# my tickets
input()
my_ticket = list(map(int, input().split(',')))

# nearby tickets
input()
input()
tickets = []
while 1:
    line = input()
    if not line:
        break
    tickets.append(list(map(int, line.split(','))))

# calc
res = 0
for ticket in tickets:
    for t in ticket:
        if not any(v1[0] <= t <= v1[1] or v2[0] <= t <= v2[1] for v1, v2 in fields.values()):
            res += t
print(res)
