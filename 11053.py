import sys

n=int(sys.stdin.readline())
p=list(map(int,sys.stdin.readline().split()))

dp=[0]*n
dp[0]=1

for i in range(1,n):
    dp[i]=1
    for j in range(i):
        if p[j]<p[i] and dp[i]<=dp[j]:
            dp[i]=dp[j]+1

print(max(dp))

