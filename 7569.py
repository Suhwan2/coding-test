import sys
from collections import deque
import copy

m,n,h=map(int,sys.stdin.readline().split())

t=[]
for _ in range(h):
    tmp=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    t.append(tmp)

def bfs(q):
    q=deque(q)
    cnt=0
    while q:
        cnt+=1
        new_q=deque()
        while q:
            z,x,y=q.popleft()
            dz=[1,-1,0,0,0,0]
            dx=[0,0,1,-1,0,0]
            dy=[0,0,0,0,1,-1]
            
            for i in range(6):
                c=z+dz[i]
                a=x+dx[i]
                b=y+dy[i]
                if -1<c<h and -1<a<n and -1<b<m and t[c][a][b]==0:
                    new_q.append((c,a,b))
                    t[c][a][b]=1
        q=copy.deepcopy(new_q)
    return cnt-1
q=[]
for i in range(h):
    for j in range(n):
        for l in range(m):
            if t[i][j][l]==1:
                q.append((i,j,l))

cnt=bfs(q)
com=True

for i in range(h):
    for j in range(n):
        for l in range(m):
            if t[i][j][l]==0:
                com=False
                break
if com:
    print(cnt)
else:
    print('-1')