from sys import stdin as st

t=int(st.readline())

for _ in range(t):
    k=int(st.readline())
    p=list(map(int,st.readline().split()))

    s=[0]
    for i in range(len(p)):
        s.append(s[-1]+p[i])
        
    dp=[[0]*k for _ in range(k)]

    for i in range(1,k):
        for j in range(k-i):
            dp[j][j+i]=min(dp[j][j+l] + dp[j+l+1][j+i] for l in range(i))+(s[j+i+1]-s[j])
    print(dp[0][k-1])