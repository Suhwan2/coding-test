import sys
from collections import deque
import copy

m,n=map(int,input().split())
t=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def bfs(l,cnt):
    if l:
        q=deque(l)
        cnt+=1
        dx=[1,-1,0,0]
        dy=[0,0,1,-1]
        while q:
            new_q=deque()
            x,y=q.popleft()    
            for i in range(4):
                xx=x+dx[i]
                yy=y+dy[i]
                if xx>-1 and xx<n and yy>-1 and yy<m and t[xx][yy]==0:
                    t[xx][yy]=1
                    new_q.append((xx,yy))
        bfs(new_q,cnt)       
    else:
        return cnt
l=deque()
for i in range(n):
    for j in range(m):
        if t[i][j]==1:
            l.append((i,j))

print(bfs(l,0))
print(t)