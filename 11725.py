import sys
input=sys.stdin.readline

from collections import deque

n=int(input())
e=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    e[a].append(b)
    e[b].append(a)

def bfs(x):
    q=deque()
    q.append(x)

    visited[x]=1

    while q:
        v=q.popleft()

        for i in e[v]:
            if visited[i]==0:
                visited[i]+=visited[v]+1
                q.append(i)
bfs(1)

for i in range(1,n+1):
    e[i].sort(key= lambda x:visited[x])

for i in range(2,n+1):
    print(e[i][0])