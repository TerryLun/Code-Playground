import math

a=list(map(int,input().split()))
p=math.prod(a)
r=[]
for i,n in enumerate(a):
    if n:
        r.append(p//n)
    else:
        r.append(math.prod(a[:i])*math.prod(a[i+1:]))
print(r)