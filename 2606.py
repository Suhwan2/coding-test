import sys
from collections import deque

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

e=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    e[a].append(b)
    e[b].append(a)

cnt=0

def bfs(r):
    global cnt
    visited[r]=1
    q=deque()
    q.append(r)
    while q:
        u=q.popleft()
        for i in e[u]:
            if visited[i]==0:
                visited[i]=1
                cnt+=1
                q.append(i)
    print(cnt)

bfs(1)