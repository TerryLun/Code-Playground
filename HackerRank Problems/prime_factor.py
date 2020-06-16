import math


def prime_factors(n):
    s = []
    # 2s
    while n % 2 == 0:
        s.append(2)
        n //= 2
    # from 3 and above
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            while n % i == 0:
                s.append(i)
                n //= i
    # if n is a prime number greater than 2
    if n > 2:
        s.append(n)
    return s


def main():
    pass


if __name__ == '__main__':
    main()
