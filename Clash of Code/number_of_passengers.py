"""
print number of passenger in the bus in the terminus station.
terminus station is the N+1 stop

first line: number of stops
second line: number of passengers get on the bus at each stop
third line: number of stops each person will stay on the buss

inp:
3
1 2 2
1 3 1 2 1
"""

n = int(input())
s=[]
for i,r in enumerate(map(int,input().split())):
    s+=[n-i]*r
r=0
p = list(map(int,input().split()))
for ss,pp in zip(s,p):
    if ss<=pp:
        r+=1
print(r)