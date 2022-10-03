import sys

n,k=map(int,sys.stdin.readline().split())

l=list(map(int,sys.stdin.readline().split()))

arr=[0]*n
arr[0]=l[0]

for i in range(1,n):
    arr[i]=arr[i-1]+l[i]

sum=[0]*(n-k+1)
sum[0]=arr[k-1]

for i in range(1,n-k+1):
    sum[i]=arr[k-1+i]-arr[i-1]
print(max(sum))

