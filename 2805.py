from sys import stdin as st

n,m=map(int,st.readline().split())
t=list(map(int,st.readline().split()))

def serch(left,right):
    if left>right:
        return 0
    global result
    mid=(left+right)//2
    cnt=0
    for i in t:
        if i>mid:
            cnt+=i-mid
    if cnt>=m:
        if result<mid:
            result=mid
        return serch(mid+1,right)
    else:
        return serch(left,mid-1)

max=max(t)
result=0
serch(0,max)
print(result)