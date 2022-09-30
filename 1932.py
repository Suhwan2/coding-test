import sys

n=int(sys.stdin.readline())
dp=[list(map(int,sys.stdin.readline().split())) for i in range(n)]

for i in range(1,n):
    dp[i][0]+=dp[i-1][0]
    dp[i][-1]+=dp[i-1][-1]
    for j in range(1,len(dp[i])-1):
        dp[i][j]+=max(dp[i-1][j-1],dp[i-1][j])

print(max(dp[n-1]))