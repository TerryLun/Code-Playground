"""
Welcome to Iwakuni.
It is a quiet old castle town.
You have been assigned as a tourist guide.

The name of each landmark that the tourer wants to visit is given, followed by its position.

The first place is always station.

Please connect the landmarks you want to visit, starting from the station, in order based on the next closest point.
It is not always the shortest path overall.

Always move the shortest distance from each landmark.

Find the total distance using Euclidean distance.


Test inputs:
-----------------------------------
2
kintaikyoBridge 400 500
station 3800 400
-----------------------------------
3
iwakuniCastle 0 0
kintaikyoBridge 400 500
station 3800 400
-----------------------------------
9
iwakuniCastle 0 0
kikkoPark 200 400
hotSpring 500 400
kintaikyoBridge 400 500
whiteSnakeShrine 3000 1100
nagayamaPark 2500 1300
mac 2600 100
shoppingStreet 3700 700
station 3800 400
-----------------------------------
"""

n = int(input())
d = {}
for i in range(n):
    place, x, y = input().split(' ')
    d[place] = (int(x), int(y))
start = 'station'
start_x = d[start][0]
start_y = d[start][1]
d.pop(start)
result = ['station']
while d:
    min_dis = float('inf')
    go = ''
    for k, v in d.items():
        dis = ((v[0] - start_x) ** 2 + (v[1] - start_y) ** 2)
        if dis < min_dis:
            min_dis = dis
            go = k
    result.append(go)
    start_x = d[go][0]
    start_y = d[go][1]
    d.pop(go)
print(*result)
