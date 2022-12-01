import sys

input=sys.stdin.readline

while True:
    t=list(map(int,input().split()))

    n=t.pop(0)
    
    if n==0:
        break
    q=[]

    result=0

    for i in range(len(t)):
    
        while q and t[q[-1]]>t[i]:
            h=q.pop()
            if not q:
                area=t[h]*i
            else:
                area=t[h]*(i-q[-1]-1)
            result=max(result,area)
        q.append(i)

    while q:
        h=q.pop()
        if not q:
            area=t[h]*n
        else:
            area=t[h]*(n-q[-1]-1)
        result=max(result,area)
    
    print(result)