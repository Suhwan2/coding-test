import sys
input=sys.stdin.readline

n,m=map(int,input().split())

id={}
for _ in range(n):
    a,b=input().strip().split()
    id[a]=b

for _ in range(m):
    ad=input().strip()
    print(id[ad])