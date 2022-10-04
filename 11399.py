import sys

n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))

l.sort()
num=l[0]
prev=l[0]
for i in range(1,n):
    num+=prev+l[i]
    prev+=l[i]
print(num)