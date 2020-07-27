f, b, n = map(int, input().split())
a = []
for i in range(1, n + 1):
    if i % f != 0 and i % b != 0:
        a.append(str(i))
    elif i % f == 0 and i % b == 0:
        a.append('FizzBuzz')
    elif i % b == 0:
        a.append('Buzz')
    else:
        a.append('Fizz')
r = []
for i in a:
    if not r or i.isalpha():
        r.append([i])
    elif i.isnumeric() and r[-1][-1].isnumeric():
        r[-1].append(i)
    else:
        r.append([i])
for i in r:
    if len(i) == 1:
        print(*i)
    else:
        print(i[0] + '-' + i[-1])

"""
for input f, b, n
print from 1 to n inclusive:
group consecutive numbers;
if n % f == 0, print Fizz;
if n % b == 0, print Buzz;
if n % f == n % b == 0 ,print FizzBuzz;
print in separate line.

input:
5 3 15

output:
1-2
Buzz
4
Fizz
Buzz
7-8
Buzz
Fizz
11
Buzz
13-14
FizzBuzz
"""
