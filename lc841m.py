"""
841. Keys and Rooms
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.
Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.
Initially, all the rooms start locked (except for room 0).
You can walk back and forth between rooms freely.
Return true if and only if you can enter every room.
"""


def canVisitAllRooms(rooms):
    key_box = {}
    for r in rooms:
        for k in r:
            if k in key_box.keys():
                key_box[k] += 1
            else:
                key_box[k] = 1

    for i in range(1, len(rooms)):
        for k in rooms[i]:
            key_box[k] -= 1
        if i not in key_box or key_box[i] == 0:
            return False
        for k in rooms[i]:
            key_box[k] += 1
    return True


print(canVisitAllRooms([[4], [3], [], [2, 5, 7], [1], [], [8, 9], [], [], [6]]))
