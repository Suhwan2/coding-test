import sys
from collections import deque

k=int(input())

def bfs(r):
    visited[r]=1
    color[r]=1
    q=deque()
    q.append(r)

    while q:
        v=q.popleft()
        for i in e[v]:
            if visited[i]==0:
                visited[i]=1
                q.append(i)
                if color[v]==1:
                    color[i]=-1
                else:
                    color[i]=1
            elif color[v]==color[i]:
                return False
    return True
for _ in range(k):
    v,n=map(int,input().split())
    e=[[] for _ in range(v+1)]
    for i in range(n):
        a,b=map(int,sys.stdin.readline().split())
        e[a].append(b)
        e[b].append(a)
    visited=[0]*(v+1)
    color=[0]*(v+1)

    result=True
    
    for i in range(1,v+1):
        if visited[i]==0:
            if not bfs(i):
                result=False
                break
        
    if result:
        print("YES")
    else:
        print("NO")
         