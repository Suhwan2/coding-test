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
            if cnt==0:
                answer.append(i)
                dfs(cnt+1)
                answer.pop()
            else:
                if answer[-1]<=i:
                    answer.append(i)
                    dfs(cnt+1)
                    answer.pop()


answer=[]
dfs(0)