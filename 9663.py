n=int(input())

visited=[[0]*n for _ in range(n)]

def dfs(x):
    if x==n:
        count+=1
        return
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            

count=0
dfs(0)
print(count)