import sys
from collections import deque

input=sys.stdin.readline

n=int(input())

q=deque()

while True:
    pac=int(input())

    if pac==-1:
        break

    if pac==0:  
        q.popleft()
    elif len(q)<n:
        q.append(pac)
if q:
    for i in range(len(q)):
        print(q[i],end=' ')
else:
    print('empty') 