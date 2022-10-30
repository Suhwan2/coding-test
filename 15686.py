import sys
from itertools import combinations
input=sys.stdin.readline

n,m=map(int,input().split())

city=[list(map(int,input().split())) for _ in range(n)]

house=[]
chicken=[]
min_v=1000000000

for i in range(n):
    for j in range(n):
        if city[i][j]==1:
            house.append((i,j))
        if city[i][j]==2:
            chicken.append((i,j))

for c in combinations(chicken,m):
    val=0
    for h in house:
        lenth=n**2
        for i in range(m):
            lenth=min(lenth,abs(h[0]-c[i][0])+abs(h[1]-c[i][1]))
        val+=lenth
    if min_v>val:
        min_v=val

print(min_v)

