import sys

n,k=map(int,sys.stdin.readline().split())

item=[[0,0]]
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    item.append((a,b))

dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        w=item[i][0]
        v=item[i][1]

        if j<w:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)

print(dp[n][k])