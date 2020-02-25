s1 = '8974'
s2 = '32'

s1 = ''.join(reversed(s1))
s2 = ''.join(reversed(s2))

i = 0
carry = 0
result = ''
max_len = max(len(s1), len(s2))

while i < max_len or carry:
    if i < len(s1):
        v1 = v2 = 0
        v1 = int(s1[i])
    if i < len(s2):
        v2 = int(s2[i])
    carry, v = divmod(v1 + v2 + carry, 10)
    result += str(v)
    i += 1

print(int(''.join(reversed(result))))


