import sys
import heapq

input=sys.stdin.readline

V,E=map(int,input().split())

s=int(input())
INF=100000000
e=[[]*(V+1) for _ in range(V+1)]
distance=[INF]*(V+1)

for _ in range(E):
    a,b,c=map(int,input().split())
    e[a].append((b,c))

def dijkstra(s):
    q=[]
    heapq.heappush(q,(0,s))
    distance[s]=0

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue
        for i in e[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(s)

for i in range(1,V+1):
    if distance[i]==INF:
        print('INF')
    else:
        print(distance[i])
