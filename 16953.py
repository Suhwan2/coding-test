from collections import deque

a,b=map(int,input().split())

visited={}

def bfs(x):
    q=deque()
    q.append(x)

    visited[x]=1

    while q:
        v=q.popleft()
        next=[v*2,v*10+1]
        for dv in next:    
            if dv<=b:
                if dv not in visited:
                    visited[dv]=visited[v]+1
                elif visited[dv]>visited[v]+1:
                    visited[dv]=visited[v]+1
                q.append(dv)
        
bfs(a)

if b not in visited:
    print('-1')
else:
    print(visited[b])