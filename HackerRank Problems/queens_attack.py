def queensAttack(n, k, r_q, c_q, obstacles):
    res = 0

    # up
    o = [i for i in obstacles if i[1] == c_q and i[0] > r_q]
    if o:
        res += min(o)[0] - r_q - 1
    else:
        res += n - r_q

    # down
    o = [i for i in obstacles if i[1] == c_q and i[0] < r_q]
    if o:
        res += r_q - max(o)[0] - 1
    else:
        res += r_q - 1

    # right
    o = [i for i in obstacles if i[0] == r_q and i[1] > c_q]
    if o:
        res += min(o)[1] - c_q - 1
    else:
        res += n - c_q

    # left
    o = [i for i in obstacles if i[0] == r_q and i[1] < c_q]
    if o:
        res += c_q - max(o)[1] - 1
    else:
        res += c_q - 1

    # to top right
    o = [i for i in obstacles if i[0] - i[1] == r_q - c_q and i[0] > r_q]
    if o:
        res += min(o)[0] - r_q - 1
    else:
        res += min(n - r_q, n - c_q)

    # to bottom left
    o = [i for i in obstacles if i[0] - i[1] == r_q - c_q and i[0] < r_q]
    if o:
        res += r_q - max(o)[0] - 1
    else:
        res += min(r_q - 1, c_q - 1)

    # to top left
    o = [i for i in obstacles if i[0] + i[1] == r_q + c_q and i[0] > r_q]
    if o:
        res += min(o)[0] - r_q - 1
    else:
        res += min(c_q - 1, n - r_q)

    # to bottom right
    o = [i for i in obstacles if i[0] + i[1] == r_q + c_q and i[0] < r_q]
    if o:
        res += r_q - max(o)[0] - 1
    else:
        res += min(n - c_q, r_q - 1)

    return res


nk = input().split()

n = int(nk[0])

k = int(nk[1])

r_qC_q = input().split()

r_q = int(r_qC_q[0])

c_q = int(r_qC_q[1])

obstacles = []

for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))

result = queensAttack(n, k, r_q, c_q, obstacles)

print(result)
