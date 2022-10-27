n=int(input())

dp=[0]*(n+1)

dp[1]=1

for i in range(2,n+1):
    for j in range(1,int(i**0.5)+1):
        m=min(4,dp[i-j**2]+1)
        if dp[i]:
            dp[i]=min(dp[i],m)
        else:
            dp[i]=m
print(dp[n])