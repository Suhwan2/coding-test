n=input()
m=int(input())
t=[]
if m:
    t=list(map(int,input().split()))
min_cnt=abs(int(n)-100)

for num in range(1000001):
    num=str(num)

    for j in range(len(num)):
        if int(num[j]) in t:
            break
        elif j==len(num)-1:
            min_cnt=min(abs(int(n)-int(num))+len(num),min_cnt)

print(min_cnt)

