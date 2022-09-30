import sys

n=int(sys.stdin.readline())
p=[int(sys.stdin.readline()) for _ in range(n)]

dp=[0]*n

dp[0]=p[0]
if n>1:
    dp[1]=p[0]+p[1]
if n>2:
    dp[2]=max(p[0],p[1])+p[2]
for i in range(3,n):

    dp[i]=max(dp[i-2],max(dp[j] for j in range(i-2))+p[i-1])+p[i]

print(max(dp))