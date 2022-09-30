import sys

n=int(sys.stdin.readline())
p=[int(sys.stdin.readline()) for i in range(n)]

dp=[[0] for i in range(n)]

if n==1:
    print(p[0])
elif n==2:
    print(p[0]+p[1])
else:
    dp[0]=p[0]
    dp[1]=p[0]+p[1]
    dp[2]=max(dp[0],p[1])+p[2]

    for i in range(3,n):
        dp[i]=max(dp[i-2],dp[i-3]+p[i-1])+p[i]
    print(dp[n-1])