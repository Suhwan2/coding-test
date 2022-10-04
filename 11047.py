import sys

n,k=map(int,sys.stdin.readline().split())

coin=[int(sys.stdin.readline()) for _ in range(n)]

cnt=0
for i in range(n-1,-1,-1):
    if k==0:
        break
    if coin[i]>k:
        continue
    num=k//coin[i]
    cnt+=num
    k-=num*coin[i]
print(cnt)