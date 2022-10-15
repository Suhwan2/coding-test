from sys import stdin as st
import sys
sys.setrecursionlimit(3000)
t=int(st.readline())

def check(x,y,m,n):
    if x==-1 or y==-1 or x==m or y==n:
        return 0
    if f[x][y]==1:
        f[x][y]=0
        check(x+1,y,m,n)
        check(x-1,y,m,n)
        check(x,y+1,m,n)
        check(x,y-1,m,n)

for _ in range(t):
    m,n,k=map(int,st.readline().split())

    f=[[0]*n for _ in range(m)]
    for _ in range(k):
        x,y=map(int,st.readline().split())
        f[x][y]=1
    cnt=0
    if k==1:
        print('1')
    else:
        for i in range(m):
            for j in range(n):
                if f[i][j]==1:
                    cnt+=1
                    check(i,j,m,n)
        print(cnt)