n = int(input())

for row in range(-n + 1, n):
    for col in range(-n + 1, n):
        if row + col > n - 1 or row + col < -n + 1 or col - row > n - 1 or col - row < -n + 1:
            char = '-'
        else:
            char = chr(ord('a') + abs(row + col))
        if col == 0:
            print(char, end='')
        if col < 0:
            print(char + '-', end='')
        if col > 0:
            print('-' + char, end='')
    print()


# one line ruby
# (1..n*2-1).map{|i|puts (1..n*2-1).map{a=(n-i).abs+(n-_1).abs;a<n ?(a+97).chr: ?-}*?-}