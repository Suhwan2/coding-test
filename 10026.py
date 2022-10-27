import sys
from collections import deque

input=sys.stdin.readline

n=int(input())

m=[input().strip() for _ in range(n)]

visited=[[0 for _ in range(n)] for _ in range(n)]
visited_2=[[0 for _ in range(n)] for _ in range(n)]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    while q:
        a,b=q.popleft()

        for i in range(4):
            da=a+dx[i]
            db=b+dy[i]

            if 0<=da<n and 0<=db<n and visited[da][db]==0 and m[da][db]==m[a][b]:
                visited[da][db]=1
                q.append((da,db))

def bfs_2(x,y):
    q=deque()
    q.append((x,y))
    visited_2[x][y]=1
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    rg=['R','G']
    while q:
        a,b=q.popleft()

        for i in range(4):
            da=a+dx[i]
            db=b+dy[i]

            if 0<=da<n and 0<=db<n and visited_2[da][db]==0 :
                if m[da][db]==m[a][b] or (m[da][db] in rg and m[a][b] in rg):
                    visited_2[da][db]=1
                    q.append((da,db))

cnt=0
cnt_2=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            bfs(i,j)
            cnt+=1
        if visited_2[i][j]==0:
            bfs_2(i,j)
            cnt_2+=1

print(cnt,cnt_2)