import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())
real=list(map(int,input().split()))

if len(real):
    real=real[1:]

party=[list(map(int,input().split()))[1:] for _ in range(m)]

e=[[] for _ in range(n+1)]

for i in range(m):
    for j in range(len(party[i])):
        e[party[i][j]]+=party[i]
for i in range(1,n+1):
    e[i]=list(set(e[i]))

def bfs(x):
    q=deque()
    q.append(x)
    visited[x]=1

    while q:
        v=q.popleft()
        for i in e[v]:

            if visited[i]==0:
                visited[i]=1
                q.append(i)
                real.append(i)
visited=[0]*(n+1)
for i in range(len(real)):
    if visited[real[i]]==0:
        bfs(real[i])
cnt=m
for i in range(m):
    for j in range(len(party[i])):
        if party[i][j] in real:
            cnt-=1
            break
print(cnt)