adapters = []

while 1:
    line = input()
    if not line:
        break
    adapters.append(int(line))

adapters.sort()

one = two = three = four = 0

for i in range(1, len(adapters)):
    curr = adapters[i]
    prev = adapters[i - 1]
    diff = curr - prev
    if diff == 1:
        one += 1
    elif diff == 2:
        two += 1
    elif diff == 3:
        three += 1
    else:
        four += 1

print(one, two, three, four)

print((one + 1) * (three + 1))
