import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())

    p=[list(map(int,input().split())) for _ in range(2)]
    dp=[[0]*n for _ in range(2)]

    dp[0][0]=p[0][0]
    dp[1][0]=p[1][0]

    for i in range(1,n):
        dp[0][i]=max(p[0][i]+dp[1][i-1],dp[0][i-1])
        dp[1][i]=max(p[1][i]+dp[0][i-1],dp[1][i-1])
    
    print(max(dp[0][n-1],dp[1][n-1]))