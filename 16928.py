import sys
from collections import deque

n,m=map(int,input().split())

n_dic={}
m_dic={}
for _ in range(n):
    a,b=map(int,sys.stdin.readline().split())
    n_dic[a]=b

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    m_dic[a]=b

g=[0]*101

def bfs(r):
    q=deque()
    q.append(r)
    while q:
        v=q.popleft()
        if v==100:
            return 0
        for i in range(1,7):
            u=v+i
            if u>100 or g[u]!=0:
                continue     
            if n_dic.get(u):
                u=n_dic[u]
            if m_dic.get(u):
                u=m_dic[u]
            if g[u]==0 :
                g[u]=g[v]+1 
                q.append(u)
bfs(1)
print(g[-1])