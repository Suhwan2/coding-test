n,r,c=map(int,input().split())

def serch(s,n,r,c):
    if n==1:
        if r==0:
            if c==0:
                return s
            else:
                return s+1
        else:
            if c==0:
                return s+2
            else:
                return s+3
    num=2**(n-1)
    if r<num:
        if c<num:
            return serch(s,n-1,r,c)
        else:
            return serch(s+num**2,n-1,r,c-num)
    else:
        if c<num:
            return serch(s+(num**2)*2,n-1,r-num,c)
        else:
            return serch(s+(num**2)*3,n-1,r-num,c-num)
        

print(serch(0,n,r,c))