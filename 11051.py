n,k=map(int,input().split())

result=1

if k > (n//2):
    k=n-k
for i in range(k):
    result*=(n-i)
for i in range(k):
    result//=(k-i)
print(int(result%10007))