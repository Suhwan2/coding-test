from sys import stdin as st

k,n=map(int,st.readline().split())

l=[int(st.readline()) for _ in range(k)]

def cal(mid):
    cnt=0
    for i in l:
        cnt+=(i//mid)
    if cnt>=n:
        return True
    else:
        return False

def serch(left,right):
    if left>right:
        return 0
    mid=(left+right)//2
    global result
    if cal(mid):
        if mid>result:
            result=mid
        return serch(mid+1,right)
    else:
        return serch(left,mid-1)

m=max(l)
result=0
serch(1,m)
print(result)