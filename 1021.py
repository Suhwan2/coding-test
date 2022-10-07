import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
q=deque()
for i in range(1,n+1):
    q.append(i)
tar=list(map(int,sys.stdin.readline().split()))

cnt=0
for i in range(len(tar)):

    idx=q.index(tar[i])
    if idx>n//2:
        while True:
            if tar[i] ==q[0]:
                q.popleft()
                n-=1
                break
            q.insert(0,q[-1])
            q.pop()
            cnt+=1
    else:
        while True:
            if tar[i] ==q[0]:
                q.popleft()
                n-=1
                break
            q.insert(n,q[0])
            q.popleft()
            cnt+=1
print(cnt)       



