x=int(input())

dp=[[0] for i in range(x)]

dp[0]=0

for i in range(1,x):
    l=[]
    if (i+1)%3==0:
        l.append(dp[i//3])
    if (i+1)%2==0:
        l.append(dp[i//2])
    l.append(dp[i-1])
    dp[i]=min(l)+1

print(dp[x-1])
