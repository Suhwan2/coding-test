from sys import stdin as st

s=[list(map(int,st.readline().split())) for _ in range(9)]
blank=[]

for i in range(9):
    for j in range(9):
        if s[i][j]==0:
            blank.append([i,j])
def check(x,y,num):
    xx=x//3
    yy=y//3
    for i in range(9):
        if s[x][i]==num or s[i][y]==num:
            return False
    for i in range(xx*3,xx*3+3):
        for j in range(yy*3,yy*3+3):
            if s[i][j]==num:
                return False
    return True
def dfs(idx):
    if idx==len(blank):
        for i in range(9):
            for j in range(9):
                print(s[i][j],end=' ')
            print()
        exit(0)
    for i in range(1,10):
        x=blank[idx][0]
        y=blank[idx][1]
        if check(x,y,i):
            s[x][y]=i
            dfs(idx+1)
            s[x][y]=0
dfs(0)

