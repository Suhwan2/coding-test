import sys

n,k=map(int,sys.stdin.readline().split())

p=[]

for _ in range(n):
    w,v=map(int,sys.stdin.readline().split())
    p.append([w,v])

dp=[[0 for _ in range(n)] for _ in range(n)]
print(dp)

for i in range(k):
    pass