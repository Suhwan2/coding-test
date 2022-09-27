def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    if l[a-1][b-1][c-1] != 0:
        return l[a-1][b-1][c-1]
    elif a<b and b<c:
        l[a-1][b-1][c-1]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
        return l[a-1][b-1][c-1]
    else:
        l[a-1][b-1][c-1]=w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        return l[a-1][b-1][c-1]

while True:
    a,b,c=map(int,input().split())
    l=[[[0]*20 for i in range(20)]for j in range(20)]
    if a==-1 and b== -1 and c==-1:
        break
    else:
        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')