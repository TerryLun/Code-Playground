n = int(input())
for i in range(n + 2):
    if i == 0:
        print(' '.join([' _ ' for x in range(n)]))
    elif i == 1:
        print('_'.join(['/ \\' for x in range(n)]))
    elif i == 2:
        print(' '.join(['\\_/' for x in range(n)]))
    else:
        print('  ' * (i - 2) + ' '.join(['\\_/' for x in range(n - i + 2)]))
