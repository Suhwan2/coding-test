import sys
from collections import deque

n,m,r=map(int,sys.stdin.readline().split())
visted=[0]*(n+1)
e=[[] for _ in range(n+1)]
result=[0]*(n+1)

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    e[a].append(b)
    e[b].append(a)

for i in range(1,n+1):
    e[i].sort(reverse=True)


def bfs(r):
    visted[r]=1
    q=deque()
    q.append(r)
    cnt=1
    result[r]=cnt
    while q:
        u=q.popleft()
        for i in e[u]:
            if visted[i]==0:
                cnt+=1
                result[i]=cnt
                visted[i]=1
                q.append(i)
bfs(r)

for i in range(1,n+1):
    print(result[i])