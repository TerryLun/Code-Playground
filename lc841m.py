"""
841. Keys and Rooms
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.
Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.
Initially, all the rooms start locked (except for room 0).
You can walk back and forth between rooms freely.
Return true if and only if you can enter every room.
"""


def canVisitAllRooms(rooms):
    key_box = []
    visit = [False for _ in range(len(rooms))]
    visit[0] = True
    for k in rooms[0]:
        if k not in key_box:
            key_box.append(k)
    # while key box is not empty
    while key_box:
        key = key_box.pop()
        visit[key] = True
        for k in rooms[key]:
            if k not in key_box and visit[k] is False:
                key_box.append(k)
    if False not in visit:
        return True
    return False


print(canVisitAllRooms([[1], [1, 1]]) is True)
print(canVisitAllRooms([[1], [2], [3], []]) is True)
print(canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) is False)
print(canVisitAllRooms([[4], [3], [], [2, 5, 7], [1], [], [8, 9], [], [], [6]]) is False)
