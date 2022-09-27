def fib(n):
    global cnt_1
    if n==1 or n==2:
        cnt_1+=1
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibonacci(n):
    f=[1,1]
    global cnt_2
    for i in range(2,n):
        f.append(f[i-1]+f[i-2])
        cnt_2+=1
    return f[n-1]

n=int(input())
cnt_1=0
cnt_2=0
fib(n)
fibonacci(n)

print(cnt_1,cnt_2)