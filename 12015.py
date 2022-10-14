from sys import stdin as st

n=int(st.readline())
l=list(map(int,st.readline().split()))

arr=[0]

for i in l:
    if arr[-1]<i:
        arr.append(i)
    else:
        left=0
        right=len(arr)
        
        while left < right:
            mid=(left+right)//2
            if arr[mid]<i:
                left=mid+1
            else:
                right=mid
        arr[right]=i

print(len(arr)-1)