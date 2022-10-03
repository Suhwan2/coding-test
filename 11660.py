import sys

n,m=map(int,sys.stdin.readline().split())
l=[]
for _ in range(n):
   l.append(list(map(int,sys.stdin.readline().split()))) 

arr=[[0]*n for _ in range(n)]

for i in range(n):
    arr[i][0]=l[i][0]
for i in range(n):
    for j in range(1,n):
        arr[i][j]=arr[i][j-1]+l[i][j]

for _ in range(m):
    x,y,xx,yy=map(int,sys.stdin.readline().split())
    num=0
    
    if y==1:
        for i in range(x-1,xx):
            num+=arr[i][yy-1]
    else:
        for i in range(x-1,xx):
            num+=arr[i][yy-1]-arr[i][y-2]
    print(num)