n,m=map(int,input().split())

def prin():
    for i in answer:
        print(i,end=' ')
    print()
def dfs(cnt):
    if cnt==m:
        prin()
    else:
        for i in range(1,n+1):
            if visited[i]:
                continue
            if cnt>=1:
                if answer[-1]<i:
                    visited[i]=1
                    answer.append(i)
                    dfs(cnt+1)
                    visited[i]=0
                    answer.pop()
            else:
                visited[i]=1
                answer.append(i)
                dfs(cnt+1)
                visited[i]=0
                answer.pop()
visited=[]
answer=[]
for i in range(n+1):
    visited.append(0)
dfs(0)

