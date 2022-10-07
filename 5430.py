from collections import deque
from sys import stdin as st

t=int(st.readline())

for _ in range(t):
    fuc=st.readline().strip()
    n=int(st.readline())
    l=input()[1:-1].split(",")
    d=deque(l)
    if n==0:
        d=deque([])

    r=0
    er=False
    for i in fuc:
        if i=='R':
            r+=1
        else:
            if len(d)==0:
                er=True
                break
            if r%2==0:
                d.popleft()
            else:
                d.pop()
    if er:
        print('error')
    else:
        if r%2==1:
            d.reverse()
        if len(d)==0:
            print('[]')
        else:
            print('[',end='')
            for i in range(len(d)-1):
                print(f'{d[i]},',end='')
            print(f'{d[-1]}]')