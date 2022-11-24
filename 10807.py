import sys

input=sys.stdin.readline

n=int(input())

nl=list(map(int,input().split()))

v=int(input())

cnt=0

for i in range(len(nl)):
    if nl[i]==v:
        cnt+=1

print(cnt)