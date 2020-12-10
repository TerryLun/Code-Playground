instructions = []

while 1:
    line = input()
    if not line:
        break
    ins, val = line.split()
    val = int(val)
    instructions.append([ins, val])


def run():
    exed = set()
    i = 0
    acc = 0
    error_exit = True

    while i not in exed and i < len(instructions):
        op, val = instructions[i]
        exed.add(i)
        if op == 'acc':
            acc += val
        elif op == 'jmp':
            i += val
            continue
        i += 1

    if i == len(instructions):
        error_exit = False
    return error_exit, acc


for i, ins in enumerate(instructions):
    if ins[0] == 'nop':
        instructions[i][0] = 'jmp'
    elif ins[0] == 'jmp':
        instructions[i][0] = 'nop'

    err_acc = run()

    if err_acc[0] is False:
        print(err_acc[1])
        exit()

    if ins[0] == 'nop':
        instructions[i][0] = 'jmp'
    elif ins[0] == 'jmp':
        instructions[i][0] = 'nop'

