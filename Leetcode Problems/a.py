# Enter your code here. Read input from STDIN. Print output to STDOUT

def isPrime(n):
    if n in [2, 3]:
        print('Prime')
        return
    if n == 1:
        print('Not prime')
        return
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            print('Not prime')
            return
        i += 1
    print('Prime')


T = int(input())
for _ in range(T):
    isPrime(int(input()))

