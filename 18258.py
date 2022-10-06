import sys

q=[]

n=int(sys.stdin.readline())
start=end=0

for _ in range(n):
    word=sys.stdin.readline().strip()

    if word=='pop':
        if end-start>0:
            print(q[start])
            start+=1
        else:
            print(-1)
    elif word=='size':
        print(end-start)
    elif word=='empty':
        if end==start:
            print(1)
        else:
            print(0)
    elif word=='front':
        if end-start>0:
            print(q[start])
        else:
            print(-1)
    elif word=='back':
        if end-start>0:
            print(q[end-1])
        else:
            print(-1)
    else:
        a,b=word.split(' ')
        q.append(b)
        end+=1

