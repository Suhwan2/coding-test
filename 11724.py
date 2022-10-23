import sys
from collections import deque

n,m=map(int,input().split())

e=[[] for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    e[a].append(b)
    e[b].append(a)

def bfs(r):
    visited[r]=1
    q=deque()
    q.append(r)

    while q:
        v=q.popleft()
        for i in e[v]:
            if visited[i]==0:
                visited[i]=1
                q.append(i)

cnt=0
for i in range(1,n+1):
    if visited[i]==0:
        cnt+=1
        bfs(i)
print(cnt)