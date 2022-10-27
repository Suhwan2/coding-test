import sys
input=sys.stdin.readline

n,m=map(int,input().split())

paper=[list(map(int,input().split())) for _ in range(n)]

visited=[[0]*m for _ in range(n)]

def dfs(x,y):
    global max_v
    if len(result)==4:
        max_v=max(max_v,sum(result))
        return 0
    
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    for i in range(4):
        a=x+dx[i]
        b=y+dy[i]
        if 0<=a<n and 0<=b<m and visited[a][b]==0:
            result.append(paper[a][b])
            visited[a][b]=1
            dfs(a,b)
            result.pop()
            visited[a][b]=0

def exel(x,y):
    global max_v

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    for i in range(4):
        v=paper[x][y]
        for j in range(4):
            if i==j:
                continue
            a,b=x+dx[j],y+dy[j]
            if 0<=a<n and 0<=b<m:
                v+=paper[a][b]
        max_v=max(max_v,v)

max_v=0
for i in range(n):
    for j in range(m):
        result=[]
        result.append(paper[i][j])
        visited[i][j]=1
        dfs(i,j)
        visited[i][j]=0

        exel(i,j)
print(max_v)