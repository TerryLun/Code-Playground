a = []
while 1:
    line = input()
    if not line:
        break
    a += [int(line)]

print("input get")


def get_sum(l, num):
    x = set()
    for n in l:
        if n in x:
            return n, num - n
        else:
            x.add(num - n)
    return (-1, -1)


for i, n in enumerate(a):
    z = get_sum(a[:i] + a[i:], 2020 - n)
    if z[0] != -1:
        print(n * z[0] * z[1])
        exit()
