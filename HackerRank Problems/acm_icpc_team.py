"""
O(N^2) - Accepted
"""

nm = input().split()

n = int(nm[0])

m = int(nm[1])

topic = []

d = {}
for _ in range(n):
    topic_item = input()

    for t in topic:
        r = bin(int(topic_item,2)|int(t,2))[2:].count('1')
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
