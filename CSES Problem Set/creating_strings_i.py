import itertools

s = input()

a = itertools.permutations(s)
b= [''.join(z) for z in a]
c=list(set(b))
c.sort()
print(len(c))
for i in c:
    print(i)
