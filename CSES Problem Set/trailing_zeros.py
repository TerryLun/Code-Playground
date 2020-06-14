n = int(input())
r = n // 5
i = 25
while i < n:
    r += n // i
    i *= 5
print(r)
