import sys

s=sys.stdin.readline().strip()

q=int(sys.stdin.readline())

arr=[[0]*len(s) for _ in range(26)]

for i in range(26):
    if ord(s[0])==97+i:
        arr[i][0]=1

for i in range(26):
    for j in range(1,len(s)):
        if ord(s[j])==97+i:
            arr[i][j]=arr[i][j-1]+1
        else:
            arr[i][j]=arr[i][j-1]

for _ in range(q):
    alr=list(sys.stdin.readline().split())
    a=alr[0]
    l,r=int(alr[1]),int(alr[2])
    num=ord(a)-97
    cnt=0
    if l==r:
        if s[l]==a:
            cnt+=1
    elif l==0:
        cnt+=arr[num][r]
    else:
        cnt+=(arr[num][r]-arr[num][l-1])
    print(cnt)