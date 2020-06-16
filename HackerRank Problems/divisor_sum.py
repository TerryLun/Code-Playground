n = int(input())
i = 1
s = 0
while i * i <= n:
    if n % i == 0:
        if n // i == i:
            s += i
        else:
            s += i + n // i
    i += 1
print(s)
