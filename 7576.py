import sys
from collections import deque
import copy

m,n=map(int,input().split())
t=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def bfs(l):
    cnt=0
    q=deque(l)
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    while q:
        new_q=deque()
        cnt+=1
        while q:
            x,y=q.popleft()    
            for i in range(4):
                xx=x+dx[i]
                yy=y+dy[i]
                if xx>-1 and xx<n and yy>-1 and yy<m and t[xx][yy]==0:
                    t[xx][yy]=1
                    new_q.append((xx,yy))
        q=copy.deepcopy(new_q)
    return cnt-1
l=deque()
for i in range(n):
    for j in range(m):
        if t[i][j]==1:
            l.append((i,j))

cnt=bfs(l)

com=True
for i in range(n):
    for j in range(m):
        if t[i][j]==0:
            com=False
            break

if com:
    print(cnt)
else:
    print('-1')    