import sys

t=int(sys.stdin.readline())

for _ in range(t):
    n,m=map(int,sys.stdin.readline().split())
    im=list(map(int,sys.stdin.readline().split()))
    
    start=0
    end=n
    cnt=0
    while start!=end:

        if im[start]==max(im[start:end]):
            cnt+=1
            if m==start:
                print(cnt)
                break
            start+=1

        else:
            if m==start:
                m+=end-start
            im.append(im[start])
            start+=1
            end+=1  


    
