from sys import stdin as st

n,m=map(int,st.readline().split())

A=[list(map(int,st.readline().split())) for _ in range(n)]

m,k=map(int,st.readline().split())

B=[list(map(int,st.readline().split())) for _ in range(m)]

C=[[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            C[i][j]+=A[i][l]*B[l][j]

for i in range(n):
    for j in range(k):
        print(C[i][j],end=' ')
    print()