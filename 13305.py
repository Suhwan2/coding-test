import sys

n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
gas=list(map(int,sys.stdin.readline().split()))

gas=gas[:-1]

cost=l[0]*gas[0]
prev=gas[0]
for i in range(1,len(gas)):
    if gas[i]<prev:
        prev=gas[i]
    cost+=l[i]*prev
print(cost)

