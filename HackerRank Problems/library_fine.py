def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 == y2 and m1 == m2 and d1 > d2:
        return (d1 - d2) * 15
    elif y1 == y2 and m1 > m2:
        return (m1 - m2) * 500
    elif y1 > y2:
        return 10000
    else:
        return 0


print(libraryFine(2, 7, 1014, 1, 1, 1015))
