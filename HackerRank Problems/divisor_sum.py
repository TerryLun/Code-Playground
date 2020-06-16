import prime_factor
import time


def divisor_sum_in_pair(n):
    i = 1
    s = 0
    while i * i <= n:
        if n % i == 0:
            if n // i == i:
                s += i
            else:
                s += i + n // i
        i += 1
    return s


def divisor_sum_using_prime_factors(n):
    pf = list(set(prime_factor.prime_factors(n)))
    s = 1
    for p in pf:
        k = 0
        while n % p == 0:
            k += 1
            n //= p
        s *= (p ** (k + 1) - 1) // (p - 1)
    return s


s = time.time()
print(divisor_sum_in_pair(180000000000000))
print(time.time() - s)

s = time.time()
print(divisor_sum_using_prime_factors(180000000000000))
print(time.time() - s)
