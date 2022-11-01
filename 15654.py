import sys

input=sys.stdin.readline

n,m=map(int,input().split())

num=list(map(int,input().split()))
visited=[0]*n
num.sort()

def dfs(x):
    if x==m:
        for i in result:
            print(i,end=' ')
        print()
        return 0    
    for i in range(n):
        if visited[i]==0:
            result.append(num[i])
            visited[i]=1
            dfs(x+1)
            visited[i]=0
            result.pop()
result=[]
dfs(0)
