import sys
from collections import deque

n,m=map(int,input().split())

w=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

visited=[[[0 for _ in range(2)] for _ in range(m)]for _ in range(n)]

def bfs(x,y,z):
    q=deque()
    q.append((x,y,z))
    visited[x][y][z]=1

    while q:
        a,b,c=q.popleft()
        dx=[1,-1,0,0]
        dy=[0,0,1,-1]

        if a==n-1 and b==m-1:
            return visited[a][b][c]
        for i in range(4):
            da=a+dx[i]
            db=b+dy[i]
            if -1<da<n and -1<db<m:
                if w[da][db]==0 and visited[da][db][c]==0:
                    visited[da][db][c]=visited[a][b][c]+1
                    q.append((da,db,c))
                elif w[da][db]==1 and c==0:
                    visited[da][db][1]=visited[a][b][0]+1
                    q.append((da,db,1))
    return -1

print(bfs(0,0,0))
