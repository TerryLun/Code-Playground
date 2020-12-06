# f=0 b=1
# r=1 l=0

seat_ids = []

while 1:
    line = input()
    if not line:
        break
    row = line[:7]
    col = line[7:]
    row_b = row.replace('F', '0').replace('B', '1')
    col_b = col.replace('L', '0').replace('R', '1')
    row_num = int(row_b, 2)
    col_num = int(col_b, 2)
    seat_id = row_num * 8 + col_num
    seat_ids.append(seat_id)

print(max(seat_ids))
