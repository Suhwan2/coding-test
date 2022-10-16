from sys import stdin as st
import sys
sys.setrecursionlimit(1000000)
n,m,r=map(int,st.readline().split())

visited=[0]*(n+1)
e=[[] for _ in range(n+1)]
result=[0]*(n+1)

for _ in range(m):
    a,b=map(int,st.readline().split())
    e[a].append(b)
    e[b].append(a)
for i in range(1,n+1):
    e[i].sort()

def dfs(r):
    global cnt
    cnt+=1
    visited[r]=1
    result[r]=cnt
    for i in e[r]:
        if visited[i]==0:
            dfs(i)
cnt=0
dfs(r)

for i in range(1,n+1):
    print(result[i])