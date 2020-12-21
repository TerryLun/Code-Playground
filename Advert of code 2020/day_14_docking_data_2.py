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

        bin_addr = bin(addr)[2:].rjust(len(mask), '0')

        masked_addr = ''

        for m, a in zip(mask, bin_addr):
            if m == '0':
                masked_addr += a
            else:
                masked_addr += m

        num_to_write = masked_addr.count('X')
        for i in range(2 ** num_to_write):
            bin_num = bin(i)[2:].rjust(num_to_write, '0')
            temp = masked_addr
            for b in bin_num:
                temp = temp.replace('X', b, 1)

            mem[int(temp, 2)] = val

print(sum(mem.values()))
