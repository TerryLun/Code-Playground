"""
A clock clap is a time when hour hand and minute hand overlap.
Find the time in seconds to the next clock clap given hour, minute and second of the time of the day. If the given time
is a clock clap output 0.

Note: Hour and minute hands move at constant rates, i.e. continuous sweep.

Input
Line 1: An integer for hour of time
Line 2: An integer for minute of time
Line 3: An integer for second of time

Output
A single line containing the number of seconds it takes to the next clock clap to the nearest integer or 0 if the input
is already a clock clap.
Constraints
0 ≤ hour ≤ 23
0 ≤ minute ≤ 59
0 ≤ second ≤ 59
"""

"""
1
5
0

27
"""

"""
6
30
0

164
"""

"""
12
0
0

0
"""

"""
18
18
18

866
"""

"""
1
5
27

0
"""

"""
0
0
1

3926
"""

"""
8
16
29

1629
"""
import math


def convert_to_s(h, m, s):
    return h * 60 * 60 + m * 60 + s


def convert_to_hms(s):
    h = m = 0
    if s >= 3600:
        h = s // 3600
        s %= 3600
    if s >= 60:
        m = s // 60
        s %= 60
    return h, m, s


def is_clap(h, m, s):
    minute_block_per_sec = 1 / 60
    hour_block_per_sec = 5 / 3600
    minute_in_sec = convert_to_s(0, m, s)
    hour_in_sec = convert_to_s(h, m, s)
    m_pos_in_block = minute_in_sec * minute_block_per_sec
    h_pos_in_block = hour_in_sec * hour_block_per_sec
    return math.isclose(m_pos_in_block, h_pos_in_block, abs_tol=0.007)


clap_time_in_sec = []
for i in range(3600 * 12):
    h, m, s = convert_to_hms(i)
    if is_clap(h, m, s):
        clap_time_in_sec.append(i)

# for sec in a:
#     print(convert_to_hms(sec))
# print(a)  # [0, 3927, 7855, 11782, 15709, 19636, 23564, 27491, 31418, 35345, 39273]

h, m, s = [int(input()) for i in range(3)]
h %= 12
time_in_sec = convert_to_s(h, m, s)
i = 0
while time_in_sec > clap_time_in_sec[i]:
    i += 1
print(clap_time_in_sec[i] - time_in_sec)
