n=int(input())

dp=[[0]*10 for _ in range(n)]
dp[0]=[1]*10
for i in range(1,n):
    dp[i][0]=dp[i-1][1]
    for j in range(1,9):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
    dp[i][9]=dp[i-1][8]
result=0
for i in range(1,10):
    result+=dp[-1][i]
print(result%1000000000)