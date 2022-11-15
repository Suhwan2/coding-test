import sys

input=sys.stdin.readline

def bf(x):
    inf=10000000000
    dist=[inf]*(n+1)
    dist[x]=0
    for i in range(n):
        for j in range(len(el)):
            cur,next,cost=el[j]

            if dist[next]>dist[cur]+cost:
                dist[next]=dist[cur]+cost

                if i==n-1:
                    return True
    return False

tc=int(input())

for _ in range(tc):
    n,m,w=map(int,input().split())

    vl=[i for i in range(1,n+1)]
    el=[]

    for _ in range(m):
        s,e,t=map(int,input().split())

        el.append((s,e,t))
        el.append((e,s,t))

    for _ in range(w):
        s,e,t=map(int,input().split())

        el.append((s,e,-t))

    if bf(1):
        print('YES')
    else:
        print("NO")