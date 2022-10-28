import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
sea=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if sea[i][j]==9:
            sea[i][j]=0
            x,y=i,j
            break

def bfs(x,y):
    global eat,power,sec

    visited=[[0]*n for _ in range(n)]

    visited[x][y]=1
    q=deque()
    q.append((x,y))

    dx=[-1,0,0,1]
    dy=[0,-1,1,0]

    mx=my=-1
    d=n**2

    while q:
        a,b=q.popleft()

        for i in range(4):
            da=a+dx[i]
            db=b+dy[i]

            if 0<=da<n and 0<=db<n and sea[da][db]<=power and not visited[da][db]:
                visited[da][db]=visited[a][b]+1
                if 0<sea[da][db]<power and d>visited[da][db]:
                    mx,my=da,db
                    d=visited[da][db]
                elif 0<sea[da][db]<power and d==visited[da][db]:
                    if da<mx:
                        mx,my=da,db
                        d=visited[da][db]
                    elif db<my and da==mx:
                        mx,my=da,db
                        d=visited[da][db]

                q.append((da,db))

    if mx!=-1:
        sea[mx][my]=0
        eat+=1
        if eat==power:
            power+=1
            eat=0
        sec+=visited[mx][my]-1

        # for i in range(n):
        #     for j in range(n):
        #         print(sea[i][j],end=' ')
            # print()
        # print(sec)
        bfs(mx,my)
power=2
eat=0
sec=0
bfs(x,y)

print(sec)