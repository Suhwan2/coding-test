from sys import stdin as st

def merge_sort(arr,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)

def merge(arr,p,q,r):
    i=p
    j=q+1
    tmp=[]
    while i<=q and j<=r:
        if arr[i]<=arr[j]:
            tmp.append(arr[i])
            i+=1
        else:
            tmp.append(arr[j])
            j+=1
    while i<=q:
        tmp.append(arr[i])
        i+=1
    while j<=r:
        tmp.append(arr[j])
        j+=1
    i=p
    t=0
    global cnt
    while i<=r:
        arr[i]=tmp[t]
        cnt+=1
        if cnt==k:
            print(tmp[t])
        i+=1
        t+=1


n,k=map(int,st.readline().split())
arr=list(map(int,st.readline().split()))
cnt=0
merge_sort(arr,0,n-1)
if cnt<k:
    print(-1)
