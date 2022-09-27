n=int(input())

for i in range(n):
    
    l=[1,1,1,2,2]
    t=int(input())

    for i in range(5,t):
        l.append(l[i-5]+l[i-1])
    print(l[t-1])