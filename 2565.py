import sys

n=int(sys.stdin.readline())

p=[]
for _ in range(n):
    a=list(map(int,sys.stdin.readline().split()))
    p.append(a)

p.sort()
arr=[0]

for i in p:
    if arr[-1]<i[1]:
        arr.append(i[1])
    else:
        left=0
        right=len(arr)

        while left<right:
            mid=(left+right)//2
            if i[1]>arr[mid]:
                left=mid+1
            else:
                right=mid
        arr[right]=i[1]
print(n-(len(arr)-1))