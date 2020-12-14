dep = int(input())
start = dep
bus = []
line = input().split(',')
for i in line:
    if i != 'x':
        bus.append(int(i))

while 1:
    for i in bus:
        if dep % i == 0:
            print(i * (dep - start))
            exit()
    dep += 1
