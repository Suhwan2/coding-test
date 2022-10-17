import sys
from collections import deque

n,m=map(int,input().split())
l=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

visited=[[0]*m for _ in range(n)]

def bfs(x,y):
    visited[x][y]=1
    q=deque()
    q.append((x,y))

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    while q:
        a,b=q.popleft()
        for i in range(4):
            da=a+dx[i]
            db=b+dy[i]
            if da!=-1 and da!=n and db!=-1 and db!=m:
                if l[da][db]!=0 and visited[da][db]==0:
                    visited[da][db]=1
                    q.append((da,db))
                    l[da][db]=l[a][b]+1
    
bfs(0,0)
print(l[n-1][m-1])