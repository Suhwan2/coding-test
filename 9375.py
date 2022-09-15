import sys
t=int(input())

for i in range(t):
    n=int(input())
    dic={}

    for j in range(n):
        a,b=sys.stdin.readline().split()
        if b in dic:
            dic[b]+=1
        else:
            dic[b]=1


    result=1

    for j in dic.values():
        result*=(j+1)
    
    print(result-1)