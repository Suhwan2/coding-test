import sys

k=int(sys.stdin.readline())

l=[]
for i in range(k):
    num=int(sys.stdin.readline())
    if num==0:
        l.pop()
    else:
        l.append(num)

print(sum(l))