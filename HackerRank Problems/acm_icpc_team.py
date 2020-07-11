"""
O(N^3) - TLE
"""

nm = input().split()

n = int(nm[0])

m = int(nm[1])

topic = []

d = {}
for _ in range(n):
    topic_item = input()

    for t in topic:
        r = 0
        for i in range(m):
            if t[i] == '1' or topic_item[i] == '1':
                r += 1
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    topic.append(topic_item)

result = []
for i in range(m, -1, -1):
    if i in d:
        print(i)
        print(d[i])
        exit()
