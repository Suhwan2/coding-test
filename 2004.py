n,m=map(int,input().split())

two=0
five=0


def div(a,b):
    cnt=0
    num=b
    while b<=a:
        cnt+=(int(a//b))
        b*=num
    return cnt

two+=div(n,2)
five+=div(n,5)

two-=div(n-m,2)
five-=div(n-m,5)

two-=div(m,2)
five-=div(m,5)

if two>five:
    print(five)
else:
    print(two)