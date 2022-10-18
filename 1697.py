import sys
from collections import deque

n,k=map(int,input().split())

l=[0]*100001

def bfs(n,k):
    q=deque()
    q.append(n)

    while q and l[k]==0:
        v=q.popleft()

        a=v+1
        b=v-1
        c=int(v*2)
        if a<=100000 and l[a]==0:
            l[a]=l[v]+1
            q.append(a)
        if b>-1 and l[b]==0:
            l[b]=l[v]+1
            q.append(b)
        if c<=100000 and l[c]==0:
            l[c]=l[v]+1
            q.append(c)

if n==k:
    print(0)
elif n>k:
    print(n-k)
else:
    bfs(n,k)
    print(l[k])