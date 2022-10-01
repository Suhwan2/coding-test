import sys

n,m=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))

arr=[]
arr.append(l[0])
for i in range(1,n):
    arr.append(arr[i-1]+l[i])

for _ in range(m):
    i,j=map(int,sys.stdin.readline().split())
    if i==1:
        print(arr[j-1])
    elif i==j:
        print(l[i-1])
    else:
        print(arr[j-1]-arr[i-2])
 
 