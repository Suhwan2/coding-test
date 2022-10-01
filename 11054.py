import sys

n=int(sys.stdin.readline())
p=list(map(int,sys.stdin.readline().split()))
pp=[a for a in p]
pp.reverse()

dp=[0]*n
dpp=[0]*n

dp[0]=1
dpp[0]=1

for i in range(1,n):
    dp[i]=1
    dpp[i]=1
    for j in range(i):
        if p[j]<p[i] and dp[i]<=dp[j]:
            dp[i]=dp[j]+1
        if pp[j]<pp[i] and dpp[i]<=dpp[j]:
            dpp[i]=dpp[j]+1 
dpp.reverse()

print(max(dp[k]+dpp[k]-1 for k in range(n)))