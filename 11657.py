import sys

input=sys.stdin.readline

n,m=map(int,input().split())

e=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    e.append((a,b,c))

inf=10000000000
dist=[inf]*(n+1)

dist[1]=0

result=True
for i in range(n):
    for j in range(m):
        cur,next,cost=e[j]
        if dist[cur] !=inf and dist[next] > dist[cur]+cost:
            dist[next] = dist[cur]+cost
            if i==n-1:
                result=False

for i in range(n+1):
    if dist[i]==inf:
        dist[i]=-1

if result:
    for i in range(2,n+1):
        print(dist[i])
else:
    print('-1')