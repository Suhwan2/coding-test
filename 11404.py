import sys

input=sys.stdin.readline

n=int(input())
m=int(input())
INF=10000000000000
e=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    if e[a][b]>c:
        e[a][b]=c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if e[i][k]+e[k][j]<e[i][j]:
                e[i][j]=e[i][k]+e[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or e[i][j]==INF:
            print('0',end=' ')
        else:
            print(e[i][j],end=' ')
    print()
