import sys
from collections import deque

input=sys.stdin.readline

n,k=map(int,input().split())
l=[-1]*100001
l[n]=0

def bfs(n,k):
    q=deque()
    q.append(n)
    while l[k]==-1 and q:
        v=q.popleft()

        a=v-1
        b=v*2
        c=v+1

        if a>=0 and l[a]==-1:
            l[a]=l[v]+1
            q.append(a)
        if 0<b<=100000 and l[b]==-1:
            l[b]=l[v]
            q.appendleft(b)
        if c<=100000 and l[c]==-1:
            l[c]=l[v]+1
            q.append(c)
    return l[k]
if n==k:
    print('0')
elif n>k:
    print(n-k)
else:
    print(bfs(n,k))
