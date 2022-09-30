import sys

n=int(sys.stdin.readline())
dp=[list(map(int,sys.stdin.readline().split())) for i in range(n)]

p=[[0,0,0] for i in range(n)]
p[0]=dp[0]

for i in range(1,n):
    p[i][0]=min(p[i-1][1],p[i-1][2])+dp[i][0]
    p[i][1]=min(p[i-1][0],p[i-1][2])+dp[i][1]
    p[i][2]=min(p[i-1][0],p[i-1][1])+dp[i][2]

print(min(p[n-1]))