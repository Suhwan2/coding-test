n=int(input())
k=int(input())

def serch(left,right):
    if left>right:
        return 0
    mid=(left+right)//2
    cnt=0
    for i in range(1,n+1):
        cnt+=min(mid//i,n)
    global result
    if cnt>=k:
        result=mid
        return serch(left,mid-1)
    else:
        return serch(mid+1,right)
result=0
serch(1,k)
print(result)