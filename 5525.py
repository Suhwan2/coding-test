import sys
n=int(input())
m=int(input())
e=sys.stdin.readline().strip()

result,cnt=0,0

i=0
while i<m-1:
    if e[i:i+3]=='IOI':
        cnt+=1
        i+=2

        if cnt==n:
            result+=1
            cnt-=1
    else:
        i+=1
        cnt=0
print(result)
        