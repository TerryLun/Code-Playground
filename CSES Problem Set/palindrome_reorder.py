s = input()
count = [0] * 26
for c in s:
    count[ord(c) - ord('A')] += 1
odd = 0
mid = ''
left = ''
for i in range(len(count)):
    if count[i] % 2 != 0:
        odd += 1
        mid = chr(i + ord('A')) * count[i]
    else:
        left += chr(i + ord('A')) * (count[i] // 2)
    if odd > 1:
        print('NO SOLUTION')
        exit()
print(left + mid + left[::-1])
