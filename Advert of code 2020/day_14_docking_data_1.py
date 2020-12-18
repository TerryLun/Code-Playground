mem = {}
mask = ''
val = 0
addr = 0
while 1:
    line = input()
    if not line:
        break

    if line.startswith('mask'):
        mask = line.split(' = ')[1]
    else:
        left, right = line.split(' = ')
        val = int(right)
        addr = int(left.lstrip('mem[').rstrip(']'))

        bin_val = bin(val)[2:].rjust(len(mask), '0')

        write_value = ''
        for i in range(len(mask)):
            if mask[i] == 'X':
                write_value += bin_val[i]
            else:
                write_value += mask[i]

        mem[addr] = write_value

res = 0
for v in mem.values():
    res += int(v, 2)

print(res)