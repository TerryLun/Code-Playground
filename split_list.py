"""
Split list into three partitions which the total difference of each partitions is minimum
"""


def split_list(s):
    n = len(s)
    m = []
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            a = sum(s[:i + 1])
            b = sum(s[i + 1:j + 1])
            c = sum(s[j + 1:])
            m.append([abs(c - a) + abs(b - a) + abs(b - c), i, j])
    mn = min(m)
    i, j = mn[1], mn[2]
    a, b, c = s[:i + 1], s[i + 1:j + 1], s[j + 1:]
    return " | ".join([" ".join(map(str, a)), " ".join(map(str, b)), " ".join(map(str, c))])


inp = [5, 5, 3, 7, 2, 8]
print(split_list(inp))
inp = [1, 10, 100]
print(split_list(inp))
inp = [1, 1, 1, 1, 1, 1, 999, 3, 3]
print(split_list(inp))
