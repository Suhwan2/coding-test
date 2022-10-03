import sys

n,m=map(int,sys.stdin.readline().split())
p=list(map(int,sys.stdin.readline().split()))

s=[0]*n
s[0]=p[0]%m
dp=[0]*m
dp[s[0]]+=1
for i in range(1,n):
    s[i]=(s[i-1]+p[i]%m)%m
    dp[s[i]]+=1

cnt=dp[0]
for i in range(m):
    cnt+= dp[i]*(dp[i]-1)//2
print(cnt)

