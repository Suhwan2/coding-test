import sys

n=int(sys.stdin.readline())

l=[]
for i in range(n):
    num=int(sys.stdin.readline())
    l.append(num)

result=[]
stack=[]
j=0
for i in range(1,n+1):
    stack.append(i)
    result.append('+')
    while stack and j<n:
        if stack[-1]==l[j]:
            stack.pop()
            result.append('-')
            j+=1
        else:
            break
if j==n:
    for i in result:
        print(i)
else:
    print('NO')