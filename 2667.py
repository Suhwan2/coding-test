import sys
from collections import deque

n=int(input())
l=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

def bfs(x,y):
    l[x][y]=0
    q=deque()
    q.append((x,y))
    result=[]
    result.append((x,y))
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    while q:
        a,b=q.popleft()
        for i in range(4):
            da=a+dx[i]
            db=b+dy[i]
            if da!=-1 and da!=n and db!=-1 and db!=n:
                if l[da][db]==1:
                    l[da][db]=0
                    q.append((da,db))
                    result.append((da,db))
    return len(result)
cnt=0
answer=[]
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            cnt+=1
            answer.append(bfs(i,j))
answer.sort()
print(cnt)
for i in answer:
    print(i)