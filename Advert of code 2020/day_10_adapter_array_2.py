adapters = []

while 1:
    line = input()
    if not line:
        break
    adapters.append(int(line))

adapters.append(0)
adapters.sort()

dp = [0] * len(adapters)
dp[0] = 1

for i in range(1, len(adapters)):
    curr = adapters[i]
    for j in range(1, 4):
        if i - j >= 0:
            prev = adapters[i - j]
            if curr - prev <= 3:
                dp[i] += dp[i - j]

print(dp[-1])
