from sys import stdin as st

a,b,c=map(int,st.readline().split())


def remain(a,b,c):
    if b==1:
        return a%c
    elif b%2==0:
        temp=remain(a,b//2,c)
        return (temp*temp)%c
    else:
        temp=remain(a,b//2,c)
        return (a*temp*temp)%c

print(remain(a,b,c))
