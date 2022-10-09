from sys import stdin as st

n=int(st.readline())

l=[st.readline().strip() for _ in range(n)]

def check(x,y,len):
    for i in range(x,x+len):
        for j in range(y,y+len):
            if l[x][y] != l[i][j]:
                return False
    return True
def dfs(x,y,len):
    if check(x,y,len):
        result.append(l[x][y])
    else:
        result.append('(')
        dfs(x,y,len//2)
        dfs(x,y+len//2,len//2)
        dfs(x+len//2,y,len//2)
        dfs(x+len//2,y+len//2,len//2)
        result.append(')')

result=[]
dfs(0,0,n)

for i in result:
    print(i,end='')