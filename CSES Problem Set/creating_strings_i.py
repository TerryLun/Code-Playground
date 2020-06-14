import itertools

s = input()

a = itertools.permutations(s)
b= [''.join(z) for z in a]
c=list(set(b))
for i in c:
    print(i)
