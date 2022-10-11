from sys import stdin as st

n,c=map(int,st.readline().split())
l=[int(st.readline()) for _ in range(n)]
l.sort()

def serch(left,right):
    if left>right:
        return 0
    mid=(left+right)//2
    global result
    cnt=1
    prev=l[0]
    for i in range(1,len(l)):
        if l[i]-prev>=mid:
            cnt+=1
            prev=l[i]
    if cnt>=c:
        if result<mid:
            result=mid
        return serch(mid+1,right)
    else:
        serch(left,mid-1)
result=0
if c==2:
    print(l[-1]-l[0])
else:
    serch(1,l[-1]-l[0])
    print(result)   