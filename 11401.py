n,k=map(int,input().split())
p=1000000007

def factorial(n):
    f=1
    for i in range(2,n+1):
        f=(f*i)%p
    return f

def square(n,k):
    if k==0:
        return 1
    elif k==1:
        return n

    tmp=square(n,k//2)
    if k%2==0:
        return tmp*tmp%p
    else:
        return tmp*tmp*n%p

print(factorial(n)*square(factorial(n-k)*factorial(k)%p,p-2)%p)
