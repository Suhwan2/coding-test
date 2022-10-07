from sys import stdin as st

n=int(st.readline())

l=[list(map(int,st.readline().split())) for _ in range(n)]

def check(x,y,len):
    if len==1:
        return True
    for i in range(x,x+len):
        for j in range(y,y+len):
            if l[x][y] != l[i][j]:
                return False
    return True
def square(x,y,len):
    global blue,white
    
    if check(x,y,len):
        if l[x][y]:
            blue+=1
        else:
            white+=1
    else:
        square(x,y,len//2)
        square(x,y+len//2,len//2)
        square(x+len//2,y,len//2)
        square(x+len//2,y+len//2,len//2)

blue=0
white=0
square(0,0,n)

print(white)
print(blue)

