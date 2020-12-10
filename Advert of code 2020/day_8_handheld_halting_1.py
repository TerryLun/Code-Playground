instructions = []

while 1:
    line = input()
    if not line:
        break
    ins, val = line.split()
    val = int(val)
    instructions.append((ins, val))

print(*instructions, sep='\n')

exed = set()
i = 0
acc = 0

while i not in exed:
    op, val = instructions[i]
    exed.add(i)
    if op == 'acc':
        acc += val
    elif op == 'jmp':
        i += val
        continue
    i += 1

print(acc)
