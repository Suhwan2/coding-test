import sys
from collections import deque

sys.setrecursionlimit(1000000)

n,m,r=map(int,sys.stdin.readline().split())
e=[[] for _ in range(n+1)]
visited_dfs=[0]*(n+1)
visited_bfs=[0]*(n+1)

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    e[a].append(b)
    e[b].append(a)

for i in range(1,n+1):
    e[i].sort()

def dfs(r):
    visited_dfs[r]=1
    result_dfs.append(r)
    for i in e[r]:
        if visited_dfs[i]==0:
            dfs(i)

def bfs(r):
    visited_bfs[r]=1
    q=deque()
    q.append(r)
    result_bfs.append(r)
    while q:
        u=q.popleft()
        for i in e[u]:
            if visited_bfs[i]==0:
                q.append(i)
                visited_bfs[i]=1
                result_bfs.append(i)

result_dfs=[]
dfs(r)
result_bfs=[]
bfs(r)

for i in result_dfs:
    print(i,end=' ')
print()
for i in result_bfs:
    print(i,end=' ')