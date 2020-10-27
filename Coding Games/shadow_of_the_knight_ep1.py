"""
Batman will look for the hostages on a given building by jumping from one window to another using his grapnel gun.
Batman's goal is to jump to the window where the hostages are located in order to disarm the bombs. Unfortunately he has
a limited number of jumps before the bombs go off...

Rules:
Before each jump, the heat-signature device will provide Batman with the direction of the bombs based on Batman current
position:
U (Up)
UR (Up-Right)
R (Right)
DR (Down-Right)
D (Down)
DL (Down-Left)
L (Left)
UL (Up-Left)

Your mission is to program the device so that it indicates the location of the next window Batman should jump to in
order to reach the bombs' room as soon as possible.

Buildings are represented as a rectangular array of windows, the window in the top left corner of the building is at
index (0,0).
"""

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]

lx = ly = 0
hx = w - 1
hy = h - 1

# game loop
while True:

    bd = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if bd == 'U':
        hy = y - 1
        y = (ly + hy) // 2
    elif bd == 'R':
        lx = x + 1
        x = (hx + lx) // 2
    elif bd == 'D':
        ly = y + 1
        y = (hy + ly) // 2
    elif bd == 'L':
        hx = x - 1
        x = (lx + hx) // 2
    elif bd == 'UR':
        hy = y - 1
        y = (ly + hy) // 2
        lx = x + 1
        x = (hx + lx) // 2
    elif bd == 'DR':
        ly = y + 1
        y = (hy + ly) // 2
        lx = x + 1
        x = (hx + lx) // 2
    elif bd == 'DL':
        ly = y + 1
        y = (hy + ly) // 2
        hx = x - 1
        x = (lx + hx) // 2
    elif bd == 'UL':
        hy = y - 1
        y = (ly + hy) // 2
        hx = x - 1
        x = (lx + hx) // 2

    print(x, y)
