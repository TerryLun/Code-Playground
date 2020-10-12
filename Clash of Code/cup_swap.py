# number of cups
tops_line = input()
num_cups = tops_line.count('_')

# find ball pos
sides_line = input() + ' '
ball_pos = 0
pos = 1
for i in range(0, len(sides_line) - 1, 4):
    if sides_line[i + 1] == 'o':
        ball_pos = pos
    pos += 1

a = [0] * (num_cups + 1)
a[ball_pos] = 1

# swaps
z = int(input())
for i in range(z):
    s1, s2 = [int(j) for j in input().split()]
    a[s1], a[s2] = a[s2], a[s1]

# find ball
final_ball_pos = a.index(1)

# construct result side line
result_side_line = []
for i in range(num_cups):
    result_side_line.append('| |' if final_ball_pos != i + 1 else '|o|')

# print both line of results
print(tops_line)
print(*result_side_line)
