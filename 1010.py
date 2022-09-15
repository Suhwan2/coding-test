t=int(input())

for i in range(t):
    n,m=map(int,input().split())

    num=1

    for i in range(n):
        num*=(m-i)
    for i in range(n):
        num//=(n-i)
    print(int(num))


    