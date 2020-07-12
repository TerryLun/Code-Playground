ub = 1000
p = [n for n in range(2, ub) if 0 not in [n % i for i in range(2, n)]]
