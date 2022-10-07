from sys import stdin as st

n=int(st.readline())
l=[list(map(int,st.readline().split())) for _ in range(n)]

def check(x,y,len):
    for i in range(x,x+len):
        for j in range(y,y+len):
            if l[x][y] != l[i][j]:
                return False
    return True
def paper(x,y,len):
    global a,b,c
    if check(x,y,len):
        if l[x][y]==-1:
            a+=1
        elif l[x][y]==0:
            b+=1
        else:
            c+=1
    else:
        for i in range(x,x+len,len//3):
            for j in range(y,y+len,len//3):
                paper(i,j,len//3)

a=b=c=0
paper(0,0,n)
print(f'{a}\n{b}\n{c}')