n,m=map(int,input().split())

result=1

for i in range(m):
    result*=(n-i)
for i in range(m):
    result//=(m-i)

if result<10:
    print(0)
else:
    count=1
    while True:
        if result%(10**count)!=0:
                print(count-1)
                break
        else:
            count+=1
