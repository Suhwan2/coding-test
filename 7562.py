import sys
from collections import deque

t=int(input())

def bfs(x,y,a,b):
    q=deque()
    q.append((x,y))

    dx=[-2,-1,1,2,-2,-1,1,2]
    dy=[-1,-2,2,1,1,2,-2,-1]

    while q and c[a][b]==0:
        v,u=q.popleft()

        for i in range(8):
            dv=v+dx[i]
            du=u+dy[i]
            if dv>-1 and dv<l and du>-1 and du<l and c[dv][du]==0:
                q.append((dv,du))
                c[dv][du]=c[v][u]+1
for _ in range(t):
    l=int(sys.stdin.readline())
    x,y=map(int,sys.stdin.readline().split())
    a,b=map(int,sys.stdin.readline().split())
    
    if x==a and y==b:
        print(0)
    else:
        c=[[0]*l for _ in range(l)]
        bfs(x,y,a,b)
        print(c[a][b])