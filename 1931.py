import sys

n=int(sys.stdin.readline())

cnt=0

l=[]
for _ in range(n):
    a=list(map(int,sys.stdin.readline().split()))
    l.append(a)

l.sort(key=lambda x : (x[1],x[0]))

cnt=1
end=l[0][1]
for i in range(1,n):
    if l[i][0]==l[i][1]:
        cnt+=1
        continue
    if end<=l[i][0]:
        cnt+=1
        end=l[i][1]
print(cnt)