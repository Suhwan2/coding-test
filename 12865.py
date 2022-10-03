import sys

n,k=map(int,sys.stdin.readline().split())

dp=[[0]]
for i in range(n):
    w,v=map(int,sys.stdin.readline().split())
    for j in range(w,k+1):
        pass