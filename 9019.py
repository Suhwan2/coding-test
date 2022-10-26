from collections import deque
import sys

input=sys.stdin.readline
t=int(input())

def D(n):
    return (n*2)%10000
def S(n):
    if n==0:
        return 9999
    return n-1
def L(n):
    if n<=9:
        d_1=d_2=d_3=0
        d_4=n
    elif n<=99:
        d_1=d_2=0
        d_3,d_4=map(int,str(n))
    elif n<=999:
        d_1=0
        d_2,d_3,d_4=map(int,str(n))
    else:
        d_1,d_2,d_3,d_4=map(int,str(n))
    return ((d_2*10 +d_3)*10 + d_4)*10 +d_1
def R(n):
    if n<=9:
        d_1=d_2=d_3=0
        d_4=n
    elif n<=99:
        d_1=d_2=0
        d_3,d_4=map(int,str(n))
    elif n<=999:
        d_1=0
        d_2,d_3,d_4=map(int,str(n))
    else:
        d_1,d_2,d_3,d_4=map(int,str(n))
    return ((d_4*10 +d_1)*10 + d_2)*10 +d_3

for _ in range(t):
    a,b=map(int,input().split())

    q=deque()
    q.append((a,''))
    visited=[0]*10000
    while q:
        x,path=q.popleft()
        visited[x]=1

        if x==b:
            print(path)
            break

        y=D(x)
        if not visited[y]:
            q.append((y,path+'D'))
            visited[y]=1
        y=S(x)
        if not visited[y]:
            q.append((y,path+'S'))
            visited[y]=1
        y=L(x)
        if not visited[y]:
            q.append((y,path+'L'))
            visited[y]=1
        y=R(x)
        if not visited[y]:
            q.append((y,path+'R'))
            visited[y]=1
        
            
