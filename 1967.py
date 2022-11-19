import sys
from collections import deque

input=sys.stdin.readline

n=int(input())

tree=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c=map(int,input().split()) 
    tree[a].append((b,c))
    tree[b].append((a,c))

def bfs(x):
    visited[x]=1
    q=deque()
    q.append(x)

    while q:
        v=q.popleft()
        for i in tree[v]:
            if visited[i[0]]==0:
                dist[i[0]]+=dist[v]+i[1]
                q.append(i[0])
                visited[i[0]]=1

visited=[0]*(n+1)
dist=[0]*(n+1)
bfs(1)

idx=dist.index(max(dist))

visited=[0]*(n+1)
dist=[0]*(n+1)
bfs(idx)

print(max(dist))
