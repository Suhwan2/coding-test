import sys
from collections import deque

n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(r):
    q=deque()
    q.append(r)
    visited[r]=1

    while q:
        v=q.popleft()
        for i in graph[v]:
            if visited[i]==0:
                visited[i]=visited[v]+1
                q.append(i)
    
for i in range(1,n+1):
    visited=[0]*(n+1)
    bfs(i)

    result=0
    for j in range(1,n+1):
        result+=visited[j]-1

    if i==1:
        min=result
        idx=1
    elif min>result:
        min=result
        idx=i
print(idx)