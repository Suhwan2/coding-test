n=int(input())

num=1

for i in range(1,n+1):
    num*=i

if num<10:
    print(0)
else:
    count=1
    while True:
        if num%(10**count)!=0:
                print(count-1)
                break
        else:
            count+=1
