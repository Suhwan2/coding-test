n=int(input())

arr=[1,1]

for i in range(n-1):
    pre=arr[1]
    arr[1]=(arr[0]+arr[1])%15746
    arr[0]=pre
print(arr[1])